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

from warnings import warn
from source.data.model.fogData.fogData import fogNewGateAreas
from source.data.model.fogData.fogData import fogNoNewGateArea
from source.data.model.fogData.fogGateLots import fogGateLots


# traverse the area network to get the hint data
def traverseFog(fog):

    # inline recursive method to traverse corridor areas until a node or a dead
    # end is reached
    def traverseGates(areaName, areas, gateText=None, hintAreaText=None):
        # use custom area text if there is one
        if hintAreaText is None:
            hintAreaText = fog["areas"][areaName]["hintName"]
        # if we've visited this area already, stop
        if hintAreaText in areas:
            return None
        # mark the area as visited
        areas.append(hintAreaText)
        areaEntry = fog["areas"][areaName]
        # if we've reached a node, stop
        if "isNode" in areaEntry:
            # if there are no lots in the destination node, return its area
            # name to track it
            if "noLots" in areaEntry:
                return areaName
            return None
        # get a list of gates
        gates = []
        for exitGateText in areaEntry["gates"]:
            # don't count the gate we came in from
            if gateText == exitGateText:
                continue
            gates.append(areaEntry["gates"][exitGateText])
        # if there are no other gates, stop here
        if len(gates) == 0:
            return None
        # error if there is more than 1 other exit, if there is we need to add
        # a new node entry
        if len(gates) > 1:
            warn("Too many gates: {} {}".format(areaName, gates), SyntaxWarning)
            return None
        # get the exit area name
        exitAreaName = gates[0]["area"]
        # get any custom area hint text for the other side of the gate
        hintAreaText = None
        if "hintArea" in gates[0]:
            hintAreaText = gates[0]["hintArea"]
        # if the other side of the exit gate is blocked, add the next area and
        # stop
        if "isBlocked" in gates[0]:
            # if there is custom text use it, otherwise use the normal hintName
            if hintAreaText:
                areas.append(hintAreaText)
            else:
                areas.append(fog["areas"][exitAreaName]["hintName"])
            return None
        # get the exit gate spoiler text
        exitGateText = None
        if "text" in gates[0]:
            exitGateText = gates[0]["text"]
        # continue traversing with any possible custom area text
        return traverseGates(exitAreaName, areas, exitGateText, hintAreaText)
    fogHints = dict()
    # generate hint structures for each node gate
    # go through all the areas in the fog gate lots
    for lotAreaName in fogGateLots:
        areaName = lotAreaName
        # if Limgrave and Liurnia are not separated, we need to use the extended
        # area name
        if "newgate" not in fog["options"] and areaName in fogNewGateAreas:
            areaName = fogNoNewGateArea
        # if the area is actually only a node when the coupledwarp option is
        # disabled, and it's enabled, skip
        if "coupledwarp" in fog["options"] and \
                "isCoupledWarpNode" in fog[areaName]:
            continue
        if areaName not in fogHints:
            fogHints[areaName] = dict()
        # go through all the gates in the area
        for gateText in fogGateLots[lotAreaName]:
            hintAreas = []
            destName = None
            gateLotsEntry = fogGateLots[lotAreaName][gateText]
            # need to skip the gate between Limgrave and Liurnia if the option
            # to separate them isn't enabled
            if "newGate" in gateLotsEntry and "newgate" not in fog["options"]:
                continue
            # get the gate entry for the starting gate
            gateEntry = fog["areas"][areaName]["gates"][gateText]
            # get the area name for the area on the other side of the gate
            exitAreaName = gateEntry["area"]
            # get any custom area hint text for the other side of the gate
            hintAreaText = None
            if "hintArea" in gateEntry:
                hintAreaText = gateEntry["hintArea"]
            # if the gate is blocked on the far end, just add the destination
            # area and don't traverse further
            if "isBlocked" in gateEntry:
                # if there is custom text use it, otherwise use the normal
                # hintName
                if hintAreaText is None:
                    hintAreaText = fog["areas"][exitAreaName]["hintName"]
                hintAreas.append(hintAreaText)
            else:
                # get the gate text for the other side of the gate
                exitGateText = None
                if "text" in gateEntry:
                    exitGateText = gateEntry["text"]
                # traverse from the area on the other side of the gate
                destName = traverseGates(exitAreaName, hintAreas, exitGateText,
                                         hintAreaText)
            if gateText in fogHints[areaName]:
                warn("Duplicate hint: {}, {}".format(areaName, gateText),
                     SyntaxWarning)

            # build the hint entry
            if "hintArea" in gateLotsEntry:
                hintAreaName = gateLotsEntry["hintArea"]
            else:
                hintAreaName = fog["areas"][areaName]["hintName"]
            hintGateName = gateLotsEntry["hintName"]
            hintEntry = {
                "area": hintAreaName,
                "gate": hintGateName,
                # the last area in the list is the destination
                "destArea": hintAreas[-1],
                "hintCount": 0,
            }
            # if there is more than the destination area in the list, add them
            # as a list of path areas
            if len(hintAreas) > 1:
                hintEntry["pathAreas"] = hintAreas[:-1]
            if "lotIDs" in gateLotsEntry:
                hintEntry["lotIDs"] = gateLotsEntry["lotIDs"]
            if "ownerGroups" in gateLotsEntry:
                hintEntry["ownerGroups"] = gateLotsEntry["ownerGroups"]
            if "hintRegion" in gateLotsEntry:
                hintEntry["hintRegion"] = gateLotsEntry["hintRegion"]
            # if the destination is a node with no lots, save its name for
            # buildNearbyFogHints
            if destName is not None:
                hintEntry["noLotDest"] = destName
            fogHints[areaName][gateText] = hintEntry
    return fogHints
