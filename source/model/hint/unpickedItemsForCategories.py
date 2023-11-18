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

import sys
from warnings import warn


# Within the given categories, find the items that have the least number of
# previously generated hints
def unpickedItemsForCategories(hintCategories, categories, excludedLotIDs=None,
                               excludedItemEntries=None):
    if not excludedLotIDs:
        excludedLotIDs = []
    if not excludedItemEntries:
        excludedItemEntries = []
    # calculate the minimum number of already generated hints for the given
    # categories
    minHints = sys.maxsize
    for category in categories:
        if category not in hintCategories:
            warn("Unknown categoroy: " + category, RuntimeWarning)
            continue
        for item in hintCategories[category]:
            if "itemEntries" not in hintCategories[category][item]:
                continue
            # For a single item type, we want the maximum number of hints for
            # any member of that type, so we don't end up giving no hints for
            # other item types due to a potentially disproportionate number of
            # possibilities for this item type while still maintaining an even
            # distribution of hints in the category
            # example: Golden Seeds in the Recovery category getting the same
            # priority as other singleton items while not preventing those
            # other items from getting hints if we've already picked some Golden
            # Seeds
            maxItemHints = 0
            for itemEntry in hintCategories[category][item]["itemEntries"]:
                if itemEntry["hintCount"] > maxItemHints:
                    maxItemHints = itemEntry["hintCount"]
            if maxItemHints < minHints:
                minHints = maxItemHints

    # generate the list of item entries in the given categories that are at or
    # under the minimum.  raise the minimum allowed hints if that will prevent
    # getting an empty list
    itemEntries = []
    while True:
        allItemsUnderMin = True
        # need to sort the categories and the hint category keys to avoid
        # an undefined order that would interfere with the seeded random
        # sequence
        # not sure why it's needed specifically for the dictionary keys, since
        # other instances of shuffled keys in the rest of the project don't
        # mess up the rng
        categoryList = list(categories)
        categoryList.sort()
        for category in categoryList:
            items = list(hintCategories[category].keys())
            items.sort()
            for item in items:
                if "itemEntries" not in hintCategories[category][item]:
                    continue
                minItemHints = sys.maxsize
                for itemEntry in hintCategories[category][item]["itemEntries"]:
                    if itemEntry["lotID"] in excludedLotIDs or \
                            itemEntry in excludedItemEntries:
                        continue
                    if itemEntry["hintCount"] < minItemHints:
                        minItemHints = itemEntry["hintCount"]
                    if itemEntry["hintCount"] > minHints:
                        allItemsUnderMin = False
                for itemEntry in hintCategories[category][item]["itemEntries"]:
                    if itemEntry["lotID"] in excludedLotIDs or \
                            itemEntry in excludedItemEntries:
                        continue
                    if itemEntry["hintCount"] <= minItemHints and \
                            itemEntry["hintCount"] <= minHints and \
                            itemEntry not in itemEntries:
                        itemEntries.append(itemEntry)
        if itemEntries or allItemsUnderMin:
            break
        minHints += 1
    return itemEntries
