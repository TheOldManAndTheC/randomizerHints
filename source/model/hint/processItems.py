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

from source.utils.rng import rng
from source.model.params.freeRange import freeRange


# All item containers that are considered to be chests
chests = [
    "Book Imp",
    "Caravan Chest",
    "Chest",
    "Chest with Chain",
    "Greataxe Caravan Chest",
    "Great Rune",
    "Lidded Farum Azula Chest",
    "Lidded River Chest",
    "Painting",
    "Stone Chest"
]


# process all item entries to get all the lots we want to place items in
# and build the hintCategories data structure
def processItems(randomized, hintCategories, params, localize):
    lotsByID = dict()
    chestLots = []
    bossLots = []
    # shuffle the order of processing all the item entries so our final
    # category structure and hint list isn't always biased towards particular
    # lots
    items = list(randomized.keys())
    rng.shuffle(items)
    for item in items:
        localizedItem = localize[item]
        rng.shuffle(randomized[item])
        for itemEntry in randomized[item]:
            # skip unreachable lots
            if "graphRegion" in itemEntry and \
                    itemEntry["graphRegion"] == "UNREACHABLE":
                continue
            lotID = itemEntry["lotID"]
            lotRange = freeRange(lotID, params["ItemLotParam_map"])
            if lotID and lotRange and "dropChance" not in itemEntry and \
                    "isShop" not in itemEntry:
                if lotID not in lotsByID:
                    lotsByID[lotID] = [itemEntry]
                else:
                    lotsByID[lotID].append(itemEntry)
                # get all chest lots that have room
                if itemEntry["container"] in chests and lotID not in chestLots:
                    chestLots.append(lotID)
                # get all boss lots that have room
                if "tags" in itemEntry and "boss" in itemEntry["tags"] and \
                        lotID not in bossLots:
                    bossLots.append(lotID)
            # process categories
            for category in hintCategories:
                categoryDict = hintCategories[category]
                if localizedItem in categoryDict:
                    categoryItemDict = categoryDict[localizedItem]
                    # if it's only supposed to be drops and shops, don't
                    # add any locational or book lots for consideration
                    if "drop" in categoryItemDict and \
                            (("book" in itemEntry) or
                             ("dropChance" not in itemEntry and
                              "isShop" not in itemEntry)):
                        continue
                    itemEntry["hintCount"] = 0
                    if "categories" not in itemEntry:
                        itemEntry["categories"] = [category]
                    elif category not in itemEntry["categories"]:
                        itemEntry["categories"].append(category)
                    if "itemEntries" in categoryItemDict:
                        categoryItemDict["itemEntries"].append(itemEntry)
                    else:
                        categoryItemDict["itemEntries"] = [itemEntry]
    return {
        "lotsByID": lotsByID,
        "chestLots": chestLots,
        "bossLots": bossLots
    }
