# Copyright (c) 2023 The Old Man and the C
#
# This file is part of Elden Ring Randomizer Hints.
#
# Elden Ring Randomizer Hints is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Elden Ring Randomizer Hints is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License along
# with Elden Ring Randomizer Hints. If not, see <https://www.gnu.org/licenses/>.

from copy import deepcopy
from source.utils.rng import rng
from source.model.params.freeRange import freeRange
from source.data.model.hintData.neighboringRegions import neighboringRegions
from source.data.model.paramData.itemLotParam_mapTemplate \
    import itemLotParam_mapTemplate

fingerMaidenHintEntry = {
    "lotID": "10010000",
    "hintName": "Finger Maiden's Guidance",
    "hintDescription": "Finger Maiden's Guidance.\nHelpful instructions from "
                       "a Finger Maiden who was slain before she could meet "
                       "her Tarnished.",
    "hintIconTypes": ["book", "scroll"]
}


def buildFingerMaidenItems(allHintEntries, randomized, hintCategories, params,
                           itemInfo, maidenItems, useRandomizer,
                           useNeighboringBias):
    lotRange = freeRange("10010000", params["ItemLotParam_map"])
    if not lotRange:
        return 0
    freeLotID = int(lotRange["freeLotID"])
    lotLength = int(lotRange["freeLotLength"])
    if "lotFlag" in lotRange:
        lotFlag = lotRange["lotFlag"]
    else:
        lotFlag = None
    if "newItemLotParam_map" in params:
        newItemLotParam_map = params["newItemLotParam_map"]
    else:
        newItemLotParam_map = dict()

    count = 0
    hintCount = 0
    itemCount = 0
    hintEntries = []
    hintEntryDict = deepcopy(fingerMaidenHintEntry)
    hintEntryDicts = []
    for displayName in maidenItems:
        quantity = 1
        if "quantity" in maidenItems[displayName]:
            quantity = maidenItems[displayName]["quantity"]
        if "isItem" in maidenItems[displayName]:
            # if we're already on the last open slot and there are hints that
            # are already in the queue to be added, skip this item to let them
            # be completed first
            if count == lotLength - 1 and hintEntries:
                continue
            itemInfoEntry = itemInfo[displayName]
            newLot = deepcopy(itemLotParam_mapTemplate)
            newLot["ID"] = str(freeLotID)
            newLot["lotItemId01"] = itemInfoEntry["equipId"]
            newLot["lotItemCategory01"] = itemInfoEntry["lotItemCategory01"]
            newLot["lotItemNum01"] = str(quantity)
            if lotFlag:
                newLot["getItemFlagId"] = lotFlag
            newItemLotParam_map[newLot["ID"]] = newLot
            # Also add it to the existing ItemLotParam_map to make sure that
            # hints don't overwrite each other
            params["ItemLotParam_map"][newLot["ID"]] = newLot
            freeLotID += 1
            itemCount += 1
            count += 1
            if count == lotLength:
                break
            continue
        if not useRandomizer:
            continue
        if "isCategory" in maidenItems[displayName]:
            category = hintCategories[displayName]
        else:
            # create a temporary singleton category for this item
            category = {
                displayName: deepcopy(maidenItems[displayName])
            }
            categoryItemDict = category[displayName]
            categoryItemDict["itemEntries"] = []
            itemName = itemInfo[displayName]["name"]
            if itemName not in randomized:
                continue
            for itemEntry in randomized[itemName]:
                # if it's only supposed to be drops and shops, don't
                # add any locational or book lots for consideration
                if "drop" in categoryItemDict and \
                        (("book" in itemEntry) or
                         ("dropChance" not in itemEntry and
                          "isShop" not in itemEntry)):
                    continue
                categoryItemDict["itemEntries"].append(itemEntry)
        for _ in range(quantity):
            itemEntries = []
            phase = 0
            if useNeighboringBias:
                phase = 2
            while True:
                for itemName in category:
                    # possible for there to be no entries for the item if for
                    # example the user chooses an item which is never dropped
                    # and sets it to drop only
                    if "itemEntries" not in category[itemName]:
                        continue
                    for itemEntry in category[itemName]["itemEntries"]:
                        # if we've already picked this entry, here or in a
                        # previous hintEntryDict, skip it
                        if itemEntry in itemEntries or itemEntry in hintEntries:
                            continue
                        found = False
                        for previousHintEntryDict in hintEntryDicts:
                            if itemEntry in \
                                    previousHintEntryDict["hintEntries"]:
                                found = True
                                break
                        if found:
                            continue
                        # first see if we can get a list from just Limgrave,
                        # then areas around Limgrave, then anywhere if those
                        # fail
                        if phase == 0:
                            if "hintRegion" in itemEntry and \
                                    itemEntry["hintRegion"] == \
                                    "western Limgrave":
                                itemEntries.append(itemEntry)
                        if phase == 1:
                            if "hintRegion" in itemEntry and \
                                    itemEntry["hintRegion"] in \
                                    neighboringRegions["western Limgrave"]:
                                itemEntries.append(itemEntry)
                        if phase > 1:
                            itemEntries.append(itemEntry)
                if itemEntries or phase > 1:
                    break
                phase += 1
            if itemEntries:
                hintEntries.append(rng.choice(itemEntries))

            # if we've filled this hint up, put it in the list and make a new
            # one
            if len(hintEntries) > 3:
                hintEntryDict["hintEntries"] = hintEntries
                hintEntryDicts.append(hintEntryDict)
                hintEntries = []
                hintEntryDict = deepcopy(fingerMaidenHintEntry)
                hintCount += 1
                count += 1
                if count == lotLength:
                    break
        if count == lotLength:
            break
    if hintEntries:
        hintEntryDict["hintEntries"] = hintEntries
        hintEntryDicts.append(hintEntryDict)
        hintCount += 1
    # add the hintEntryDicts to the main list
    for hintEntryDict in hintEntryDicts:
        allHintEntries.append(hintEntryDict)
    if newItemLotParam_map:
        params["newItemLotParam_map"] = newItemLotParam_map
    return hintCount, itemCount
