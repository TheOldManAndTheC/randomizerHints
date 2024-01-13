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
from source.data.model.fogData.fogGateLots import fogGateLots
from source.data.model.hintData.buildNearbyHintsData import nearbyHints


def buildNearbyHints(allNearbyHintEntries, randomized, params):
    count = 0
    for hintEntryDict in nearbyHints:
        # get the lotIDs for the entry from the entry itself or from the
        # associated fog gate lots
        if "lotIDs" in hintEntryDict:
            lotIDs = hintEntryDict["lotIDs"]
        else:
            areaName = hintEntryDict["areaName"]
            gateText = hintEntryDict["gateText"]
            lotIDs = fogGateLots[areaName][gateText]["lotIDs"]
        # process the list to contain only lots with room
        freeLotIDs = []
        for lotID in lotIDs:
            if freeRange(lotID, params["ItemLotParam_map"]):
                freeLotIDs.append(lotID)
        # if there are no free lots, can't place a hint, skip
        if not freeLotIDs:
            continue
        # pick a random lot from the free lots
        hintEntryDict["lotID"] = rng.choice(freeLotIDs)
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
            if itemName not in randomized:
                continue
            for itemEntry in randomized[itemName]:
                itemEntries.append(itemEntry)
            # generate the given number of hints
            for i in range(hintNumber):
                # stop if we've run out of entries or generated the maximum
                if not itemEntries or len(hintEntries) == 4:
                    break
                itemEntry = rng.choice(itemEntries)
                # remove the entry from the unpicked list
                itemEntries.remove(itemEntry)
                # add the entry to the hintEntries
                hintEntries.append(itemEntry)
        # finish generating the hint and add it to the master list
        if not hintEntries:
            continue
        hintEntryDict["hintEntries"] = hintEntries
        allNearbyHintEntries.append(hintEntryDict)
        count += 1
    return count
