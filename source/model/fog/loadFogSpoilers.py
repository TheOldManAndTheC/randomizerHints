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

from source.data.model.fogData.fogData import fogTwoWayTransitions
from source.data.model.fogData.fogData import fogPreexistingTransitions


def loadFogSpoilers(fogSpoilerLines):
    lineIter = iter(fogSpoilerLines)
    fogSpoilers = dict()
    # get the options line
    line = next(lineIter)[:-1]  # remove newline
    options = line
    # skip everything before the area listings
    while not line.startswith("Chapel of Anticipation"):
        line = next(lineIter, None)
    # read until the end of the area listings
    while line:
        line = next(lineIter, None)
        # only interested in gate lines
        if not line or line[0] != " ":
            continue
        line = line[:-1]  # remove newline
        # split off the gate type from the line
        lineSplit = line.split(": ", 1)
        # gateType = lineSplit[0] # not used
        # split the line into from and to sections
        lineSplit = lineSplit[1].split(" --> ")
        fromLine = lineSplit[0]
        toLine = lineSplit[1]
        # get the from area name
        lineSplit = fromLine.split(" (", 1)
        fromAreaName = lineSplit[0]
        # get the from area gate if there is one
        fromAreaGate = None
        if len(lineSplit) > 1:
            fromAreaGate = lineSplit[1][:-1]  # remove trailing )
        # get the to area name
        lineSplit = toLine.split(" (", 1)
        toAreaName = lineSplit[0]
        # get the to area gate
        toAreaLine = lineSplit[1]
        lineSplit = toAreaLine.split(")")
        toAreaGate = lineSplit[0]
        # the rest of the line may have item requirements
        items = None
        if len(lineSplit) > 1 and lineSplit[1]:
            items = lineSplit[1].split(" from ", 1)[1].split("; ")
        # if the area names aren't in the dictionary yet, add them
        if fromAreaName not in fogSpoilers:
            fogSpoilers[fromAreaName] = dict()
        if toAreaName not in fogSpoilers:
            fogSpoilers[toAreaName] = dict()
        # if there was no from area gate, then it's either a preexisting
        # transition, or the gate name is the same in both areas
        if not fromAreaGate:
            # in either case, the from area gate should be the to area gate
            fromAreaGate = toAreaGate
            # if it's a preexisting transition
            if fromAreaGate in fogPreexistingTransitions:
                # and if it's not a two-way transition, it's one way, so there
                # shouldn't be a to area gate
                if fromAreaGate not in fogTwoWayTransitions:
                    toAreaGate = None
                # correct gate name if needed
                elif fogTwoWayTransitions[fromAreaGate]:
                    fromAreaGate = \
                        fogTwoWayTransitions[fromAreaGate][fromAreaName]
                    toAreaGate = fogTwoWayTransitions[fromAreaGate][toAreaName]
        # make a sub-dictionary linking the from area to the to area
        fromAreaDict = {"area": toAreaName}
        # if there is a to area gate make sure that's part of the link
        if toAreaGate:
            fromAreaDict["gate"] = toAreaGate
        # if there were item requirements, add them to the sub-dictionary
        if items:
            fromAreaDict["items"] = items
        # add the sub-dictionary to the from area entry
        if fromAreaGate in fogSpoilers[fromAreaName]:
            # unless an identical one is already there
            if fromAreaDict not in fogSpoilers[fromAreaName][fromAreaGate]:
                fogSpoilers[fromAreaName][fromAreaGate].append(fromAreaDict)
        else:
            fogSpoilers[fromAreaName][fromAreaGate] = [fromAreaDict]
        # if there's no to area gate, we're done
        if not toAreaGate:
            continue
        # make a sub-dictionary linking the to area to the from area
        toAreaDict = {"area": fromAreaName, "gate": fromAreaGate}
        # if it's a two-way transition add any item requirements as well
        if items and fromAreaGate in fogTwoWayTransitions:
            toAreaDict["items"] = items
        # add the sub-dictionary to the to area entry
        if toAreaGate in fogSpoilers[toAreaName]:
            # unless an identical one is already there
            if toAreaDict not in fogSpoilers[toAreaName][toAreaGate]:
                fogSpoilers[toAreaName][toAreaGate].append(toAreaDict)
        else:
            fogSpoilers[toAreaName][toAreaGate] = [toAreaDict]
    return fogSpoilers, options
