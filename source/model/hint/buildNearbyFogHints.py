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
from source.data.model.fogData.fogData import fogPreexistingTransitions


def findNoLotDests(areaName, fog, fogHints, traversed):
    # make sure we haven't traversed this area already
    if areaName in traversed:
        return []
    traversed.append(areaName)
    # add all the gates in this area to the list
    hintEntries = list(fogHints[areaName].values())
    # shuffle the list
    rng.shuffle(hintEntries)
    # check each gate to see if they also point to nodes with no lots
    for hintEntry in hintEntries:
        # if this gate points to a node with no lots, add its gates too
        if "noLotDest" in hintEntry:
            hintEntries += findNoLotDests(hintEntry["noLotDest"], fog,
                                          fogHints, traversed)
    # check preexisting transitions as well as randomized gates
    for gateName in fog["areas"][areaName]["gates"]:
        if gateName not in fogPreexistingTransitions:
            continue
        destArea = fog["areas"][areaName]["gates"][gateName]["area"]
        # if this preexisting transition points to a node with no lots, add
        # its gates too
        if "isNode" in fog["areas"][destArea] and \
                "noLots" in fog["areas"][destArea]:
            hintEntries += findNoLotDests(destArea, fog, fogHints, traversed)
    return hintEntries


def buildNearbyFogHints(fog, fogHints, allFogHintEntries, params):
    count = 0
    # set up a structure to keep track of the lots we are using
    usedLots = dict()
    # go through all the fog hint entries
    for areaName in fogHints:
        # shuffle the gate order
        gateTexts = list(fogHints[areaName].keys())
        rng.shuffle(gateTexts)
        for gateText in gateTexts:
            hintEntry = fogHints[areaName][gateText]
            # if the entry does not have any lotIDs to use, skip it
            if "lotIDs" not in hintEntry:
                continue
            lotIDs = hintEntry["lotIDs"]
            hintEntries = [hintEntry]
            # as well as this entry, process entries from the other end if
            # they don't have lots to be placed in there
            if "noLotDest" in hintEntry:
                hintEntries += findNoLotDests(hintEntry["noLotDest"], fog,
                                              fogHints, [areaName])
            for hintEntry in hintEntries:
                # build a list of lotIDs that have room
                freeLots = []
                for lotID in lotIDs:
                    # if we've already used this lot, see if there's still room
                    if lotID in usedLots:
                        if usedLots[lotID]["fullCount"] \
                                < usedLots[lotID]["freeLotLength"]:
                            freeLots.append(lotID)
                        continue
                    # we haven't used this lot, so see if there's room
                    if freeRange(lotID, params["ItemLotParam_map"]):
                        freeLots.append(lotID)
                # if there are no lots with room, skip
                if not freeLots:
                    continue
                # pick a random lot from those available
                lotID = rng.choice(freeLots)
                # if it's not already in the used lots, add an entry for it
                # with the length of the free lot space, how many are already
                # full, and a partial count for hints within a single lot item
                if lotID not in usedLots:
                    freeLotRange = freeRange(lotID, params["ItemLotParam_map"])
                    usedLots[lotID] = {
                        "freeLotLength": int(freeLotRange["freeLotLength"]),
                        "fullCount": 0,
                        "partialCount": 0,
                        "hintEntries": []
                    }
                # add the hint entry to the list for this lot
                usedLots[lotID]["hintEntries"].append(hintEntry)
                # and update the count of how many hints are in this lot item
                usedLots[lotID]["partialCount"] += 1
                # if it reaches 3, it's a full item, update the counts
                if usedLots[lotID]["partialCount"] == 3:
                    usedLots[lotID]["fullCount"] += 1
                    usedLots[lotID]["partialCount"] = 0
    # go through all the lots in the used lots
    for lotID in usedLots:
        hintEntries = []
        # go through all the hint entries in this used lot
        for hintEntry in usedLots[lotID]["hintEntries"]:
            hintEntries.append(hintEntry)
            # if the hint object list has 3 items, it's full, create a hint
            # object entry and add it to the main list and start a new one
            if len(hintEntries) == 3:
                allFogHintEntries.append({
                    "lotID": lotID,
                    "hintEntries": hintEntries
                })
                hintEntries = []
                count += 1
        # add the final hint entry if there is one
        if hintEntries:
            allFogHintEntries.append({
                "lotID": lotID,
                "hintEntries": hintEntries
            })
            count += 1
    return count
