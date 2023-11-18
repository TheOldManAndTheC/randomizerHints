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
from source.utils.rng import rng
from source.utils.randomExtras import hintCountRandom


# Within the given categories, find the items that have the least number of
# previously generated hints
def unpickedFogHints(fogHints, excludedEntries):
    # calculate the minimum number of already generated fog hints
    minHints = sys.maxsize
    for areaName in fogHints:
        for gateText in fogHints[areaName]:
            if fogHints[areaName][gateText] in excludedEntries:
                continue
            if fogHints[areaName][gateText]["hintCount"] < minHints:
                minHints = fogHints[areaName][gateText]["hintCount"]
    # generate the list of hint entries that have had the least number of hints
    hintEntries = []
    for areaName in fogHints:
        for gateText in fogHints[areaName]:
            if fogHints[areaName][gateText] in excludedEntries:
                continue
            if fogHints[areaName][gateText]["hintCount"] == minHints:
                hintEntries.append(fogHints[areaName][gateText])
    return hintEntries


def buildRandomFogLots(lots, allFogHintEntries, fogHints, percent):
    limit = int(float(len(lots)) * percent / 100.0)
    if not limit:
        return 0
    lots.sort()
    rng.shuffle(lots)
    count = 0
    for lotID in lots:
        numberInLot = hintCountRandom(3)
        hintEntries = []
        for i in range(numberInLot):
            unpickedList = unpickedFogHints(fogHints, hintEntries)
            pick = rng.choice(unpickedList)
            # update the count of hints this item has had
            pick["hintCount"] += 1
            hintEntries.append(pick)
        allFogHintEntries.append({
            "lotID": lotID,
            "hintEntries": hintEntries
        })
        count += 1
        if count == limit:
            break
    return count
