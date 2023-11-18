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
from source.utils.randomExtras import hintCountRandom
from source.model.hint.unpickedItemsForCategories \
    import unpickedItemsForCategories


def cleanUnpickedList(unpickedList, excludedLots, excludedItemEntries):
    cleanUnpicked = []
    for itemEntry in unpickedList:
        if itemEntry["lotID"] in excludedLots or \
                itemEntry in excludedItemEntries:
            continue
        cleanUnpicked.append(itemEntry)
    return cleanUnpicked


# Place random hints on the given lots
def buildRandomLots(lots, allHintEntries, hintCategories, categories, percent):
    limit = int(float(len(lots)) * percent / 100.0)
    if not limit:
        return 0
    lots.sort()
    rng.shuffle(lots)
    count = 0
    unpicked = []
    excluding = False
    for lotID in lots:
        hintEntries = []
        # numberInLot = 4
        numberInLot = hintCountRandom()
        for i in range(numberInLot):
            # get a fresh base unpicked list if we don't have one
            if not unpicked or excluding:
                unpicked = unpickedItemsForCategories(hintCategories,
                                                      categories)
                excluding = False
            # get a clean unpicked list without this lot or any hint entries
            # we've already picked
            cleanUnpicked = cleanUnpickedList(unpicked, [lotID], hintEntries)
            # if we don't have any choices, get a base unpicked list that
            # excludes this lot or any hint entries we've already picked
            if not cleanUnpicked:
                unpicked = unpickedItemsForCategories(hintCategories,
                                                      categories,
                                                      [lotID],
                                                      hintEntries)
                # make a copy as the "clean" list so the removals will work
                cleanUnpicked = deepcopy(unpicked)
                excluding = True
            # if there are choices, pick one and remove it from both the base
            # and clean unpicked lists
            if cleanUnpicked:
                pick = rng.choice(cleanUnpicked)
                # update the count of hints this item has had
                pick["hintCount"] += 1
                hintEntries.append(pick)
                cleanUnpicked.remove(pick)
                unpicked.remove(pick)
        if hintEntries:
            allHintEntries.append({
                "lotID": lotID,
                "hintEntries": hintEntries
            })
            count += 1
        if count == limit:
            break
    return count
