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
from source.utils.randomExtras import hintCountRandom
from source.model.hint.regionalItemEntries import regionalItemEntries
from source.model.hint.unpickedItemsForCategories \
    import unpickedItemsForCategories


# Probabilities for the item sources for each pick in the category item
# hint generation
# additive probabilities are the keys, the random number picked is compared
# successively with each one until a key which is greater than or equal to
# the random number is found.  the final number should always be 100.
# values are the highest tier of item pool to start picking from
# 3 - items from the category in the same region
# 2 - items from the category in neighboring regions
# 1 - items from the category from anywhere
# 0 - items from any category from anywhere
pickProbabilities = [
    {
        100: 3
    },
    {
        70: 3,
        90: 2,
        100: 1
    },
    {
        40: 3,
        70: 2,
        95: 1,
        100: 0
    },
    {
        50: 2,
        90: 1,
        100: 0
    },
]


# build the web of hints for each category
def buildCategoryHints(lots, allHintEntries, hintCategories, categories,
                       useNeighboringBias, localize):
    lotIDs = list(lots.keys())
    rng.shuffle(lotIDs)
    count = 0
    for lotID in lotIDs:
        itemList = lots[lotID]
        # get the set of categories for the items in this lot
        lotCategories = set()
        for itemEntry in itemList:
            if "categories" not in itemEntry:
                continue
            localizedItem = localize[itemEntry["newItem"]]
            for category in itemEntry["categories"]:
                # only interested in items from the given categories
                if category not in categories:
                    continue
                # only interested in items that aren't drop/shop only
                if "drop" not in hintCategories[category][localizedItem]:
                    lotCategories.add(category)
        # if there are no categories for this lot, skip it
        if not lotCategories:
            continue
        # get an item entry from the lot to use for regional comparisons
        itemEntry = itemList[0]
        # may deprecate this, at this point we definitely don't want hints to
        # the lot the hint is in, but multiple hints to different items in the
        # same lot is fine.  but there could be other uses for multiple
        # excluded lot IDs later
        excludedLotIDs = [lotID]
        # randomly pick other lots in the same category and add them
        # to this lot entry to have hints built for them
        # TODO: add priority
        # pick the number of hints in this lot (max 4), bias for more
        # numberInLot = 4
        numberInLot = hintCountRandom()
        hintEntries = []
        for i in range(numberInLot):
            # get the probabilities for this hint and pick a number
            # to get the tier
            probabilities = pickProbabilities[i]
            percent = rng.randint(1, 100)
            tier = 0
            for probability in probabilities:
                if percent <= probability:
                    tier = probabilities[probability]
                    break
            # if we're not using the neighboring bias, start with the same
            # categories but anywhere tier
            if not useNeighboringBias:
                tier = 1
            # make a pick based on our probabilities, but make sure
            # we don't pick something already in the hint list or an
            # item on this lot
            tierList = []
            unpicked = None
            if tier > 0:
                unpicked = unpickedItemsForCategories(hintCategories,
                                                      lotCategories,
                                                      excludedLotIDs,
                                                      hintEntries)
            # try nearby regions by default to mitigate clumping of hints
            # # same region
            # if tier >= 3:
            #     tierList = regionalItemEntries(unpicked, itemEntry)
            # skip the checking for this tier since we've got it disabled
            if tier >= 3:
                tier = 2
            # nearby regions
            if not tierList and tier >= 2:
                tierList = regionalItemEntries(unpicked, itemEntry,
                                               neighboring=True)
            # anywhere
            if not tierList and tier >= 1:
                tierList = unpicked
            # anywhere and any category
            if not tierList:
                tierList = unpickedItemsForCategories(hintCategories,
                                                      categories,
                                                      excludedLotIDs,
                                                      hintEntries)
            if tierList:
                # if we still have a tier list, pick one
                pick = rng.choice(tierList)
                # add the picked entry to the hint entry list for this lot
                hintEntries.append(pick)
                # update the count of hints this item has had
                pick["hintCount"] += 1

        # if there are entries for this hint, add it
        if hintEntries:
            rng.shuffle(hintEntries)
            allHintEntries.append({
                "lotID": lotID,
                "hintEntries": hintEntries
            })
            count += 1
    return count
