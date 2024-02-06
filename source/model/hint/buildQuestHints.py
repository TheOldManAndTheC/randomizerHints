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
from source.data.model.hintData.buildQuestHintsData import questHints


# Create NPC quest item hints from file:
# Format:
# lotID: desired lot ID for this hint object
# lotItems: list of randomized items with the lots where the hint object(s)
#       will go
#   - will override lotID
#   - for round robin hint object chains, all items will be used, otherwise
#       only the first will
# roundRobin: True, only included to indicate a round robin hint chain
#   - only used with lotItems
# excludeShop: True, used to de-prioritize hints to shop items
#   - if there are no non-shop items, shop items will be hinted anyway
# hintItems: list of item names the hints will reference
# hintNumber: the number of hints to generate in this hint object
#   - only included if the number is to be greater than 1
#   - hints will only be generated from the first entry in hintItems
# hintName: the name of the hint object
# hintDescription: the description of the hint object
# hintIconTypes: the allowed icon types for the hint object
# altLotID: an alternate lot to use if there is no room in the given one
#   - if this lot also has no room the hint object will not be generated
# altHintName: the unique name of an alternate hint object to contain the
#       hints if there is no room in the given lot
#   - there must be enough room for the hints or they will be cut off at
#       the maximum of four
#   - overridden by altLotID
# shopValue: string with the price of the hint object
#   - only included if it's a shop object
def buildQuestHints(allHintEntries, randomized, params):
    count = 0
    for hintEntryDict in questHints:
        # if this is a round-robin hint chain
        if "roundRobin" in hintEntryDict:
            # get all the item entries for these items and shuffle them
            # TODO: order by geographic proximity to start?
            #   the round robin item quests are doable up to the end of the
            #   game so don't really need to do this but might make it less
            #   frustrating
            itemEntries = []
            for itemName in hintEntryDict["lotItems"]:
                if itemName in randomized:
                    itemEntries += randomized[itemName]
            if not itemEntries:
                continue
            rng.shuffle(itemEntries)

            # split all the item entries into open, full, and shop categories
            openItemEntries = []
            fullItemEntries = []
            shopItemEntries = []
            for itemEntry in itemEntries:
                if "isShop" in itemEntry:
                    shopItemEntries.append(itemEntry)
                elif freeRange(itemEntry["lotID"], params["ItemLotParam_map"]):
                    openItemEntries.append(itemEntry)
                else:
                    fullItemEntries.append(itemEntry)
            # step through all the open item entries, these are our round robin
            # anchor nodes
            # note it might be possible for no hints or insufficient hints to be
            # generated here if too many item entries are in shops or have no
            # lot space
            # TODO: add overflow items to hint items elsewhere?  notify the
            #   user that some hints may be unavailable?
            for index in range(len(openItemEntries)):
                # get the next open item entry in the list, looping around
                nextIndex = index + 1
                if nextIndex == len(openItemEntries):
                    nextIndex = 0
                hintEntries = []
                # if the next open item entry is this item entry, don't generate
                # a hint to itself
                if nextIndex != index:
                    hintEntries.append(openItemEntries[nextIndex])
                # add any available full lot hints to the hint item
                while fullItemEntries and len(hintEntries) < 4:
                    hintEntries.append(fullItemEntries[0])
                    fullItemEntries.pop(0)
                # add any available shop lot hints to the hint item
                while shopItemEntries and len(hintEntries) < 4:
                    hintEntries.append(shopItemEntries[0])
                    shopItemEntries.pop(0)
                # add this hint entry dict to the master list
                # we're doing multiple lots here so make sure we have a
                # separate entry for each one
                newHintEntryDict = deepcopy(hintEntryDict)
                newHintEntryDict["hintEntries"] = hintEntries
                newHintEntryDict["lotID"] = openItemEntries[index]["lotID"]
                allHintEntries.append(newHintEntryDict)
                count += 1
            # done with this round-robin hint entry dict
            continue

        # if this is a dynamic hint that needs to be placed in a randomized
        # item location, we need to get a lotID
        if "lotItems" in hintEntryDict:
            # get the first item entry for this item name
            # TODO: allow for multiple item names and random selection of lots
            if hintEntryDict["lotItems"][0] not in randomized:
                continue
            itemEntry = randomized[hintEntryDict["lotItems"][0]][0]
            # if there's a free lot there, add the lotID to the hint entry dict
            if "isShop" not in itemEntry and \
                    freeRange(itemEntry["lotID"], params["ItemLotParam_map"]):
                hintEntryDict["lotID"] = itemEntry["lotID"]
            # if there's no free lot and there's an alternate lot ID, use that
            elif "altLotID" in hintEntryDict:
                hintEntryDict["lotID"] = hintEntryDict["altLotID"]
            # if there's no free lot and there's an alternate hint object given,
            # add the hint to that hint object's entry dict
            # WARNING: make sure these are uniquely named because the first
            # one found is the one picked, and that there will be room
            elif "altHintName" in hintEntryDict:
                hintEntry = [x for x in allHintEntries if "hintName" in x and
                             x["hintName"] == hintEntryDict["altHintName"]][0]
                for itemName in hintEntryDict["hintItems"]:
                    # don't add if we've already reached the limit
                    if len(hintEntry["hintEntries"]) == 4:
                        break
                    if itemName in randomized:
                        hintEntry["hintEntries"].append(randomized[itemName][0])
                # we've added the hints to the alternate hint entry dict, move
                # on
                continue
            else:
                # can't place the lot, skip this hint entry dict
                continue
        # build the hint entries
        hintEntries = []
        # get the number of hints to generate
        # WARNING: only use a hintNumber with a length one hintItems list
        if "hintNumber" in hintEntryDict:
            hintNumber = hintEntryDict["hintNumber"]
        else:
            hintNumber = 1
        # step through all the items we want to make hints for
        for itemName in hintEntryDict["hintItems"]:
            # get lists of all the item entries for this item name
            itemEntries = []
            nonShopItemEntries = []
            if itemName not in randomized:
                continue
            for itemEntry in randomized[itemName]:
                itemEntries.append(itemEntry)
                if "isShop" not in itemEntry:
                    nonShopItemEntries.append(itemEntry)
            # generate the given number of hints
            for i in range(hintNumber):
                # stop if we've run out of entries or generated the maximum
                if not itemEntries or len(hintEntries) == 4:
                    break
                # if we want to exclude shops, try to pick a non-shop entry,
                # but if there are only shops pick one anyway
                if "excludeShop" in hintEntryDict and nonShopItemEntries:
                    itemEntry = rng.choice(nonShopItemEntries)
                    nonShopItemEntries.remove(itemEntry)
                else:
                    itemEntry = rng.choice(itemEntries)
                # remove the entry from the unpicked list
                itemEntries.remove(itemEntry)
                # add the entry to the hintEntries
                hintEntries.append(itemEntry)
        # finish generating the hint and add it to the master list
        if not hintEntries:
            continue
        hintEntryDict["hintEntries"] = hintEntries
        allHintEntries.append(hintEntryDict)
        count += 1

    return count
