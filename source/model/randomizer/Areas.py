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

# Parse MapName.txt and annotations.txt to get map IDs for area descriptions
# in spoilers.txt


class Areas:
    def __init__(self, mapNamesLines, annotationsLines):
        self.areasByMapID = dict()
        self.mapIDsByArea = dict()
        self.loadAreas(mapNamesLines, annotationsLines)

    def loadAreas(self, mapNamesLines, annotationsLines):
        self.areasByMapID = dict()
        self.mapIDsByArea = dict()
        areaText = ""
        lineIter = iter(mapNamesLines)
        while True:
            line = next(lineIter, None)
            if line is None:
                break
            line = line[:-1]  # remove newline
            # left side is map ID, right side is area name
            split = line.split(" ", 1)
            self.areasByMapID[split[0]] = [split[1]]
            self.mapIDsByArea[split[1]] = [split[0]]
        reading = False
        lineIter = iter(annotationsLines)
        while True:
            line = next(lineIter, None)
            if line is None:
                break
            line = line[:-1]  # remove newline
            # skip everything not in the Areas part of the file
            if line.startswith("Areas:"):
                reading = True
                continue
            if not reading:
                continue
            # stop reading after all the areas are read
            if line.startswith("PlacementRestrictions:"):
                if areaText:
                    if areaText in self.mapIDsByArea:
                        storedAreaMaps = self.mapIDsByArea[areaText]
                        for areaMap in areaMaps:
                            if areaMap not in storedAreaMaps:
                                storedAreaMaps.append(areaMap)
                        self.mapIDsByArea[areaText] = storedAreaMaps
                    else:
                        self.mapIDsByArea[areaText] = areaMaps
                break

            # start line of each area entry
            if line.startswith("- Name: "):
                # store previous line results
                if areaText:
                    if areaText in self.mapIDsByArea:
                        storedAreaMaps = self.mapIDsByArea[areaText]
                        for areaMap in areaMaps:
                            if areaMap not in storedAreaMaps:
                                storedAreaMaps.append(areaMap)
                    else:
                        self.mapIDsByArea[areaText] = areaMaps
                areaText = ""
                areaMaps = []

            # the area name used in spoilers.txt
            if line.startswith("  Text: "):
                areaText = line[8:]

            # the list of map IDs for the area
            if line.startswith("  Maps: "):
                areaMaps = line[8:].split(" ")
