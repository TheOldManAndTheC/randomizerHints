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

directionConnectors = {
    "keys": ["", "landmark", "type", "horiz", "angle", "vert"],
    "slots": ["By ", " (", ") - ", " away, ", " o'clock, ", " height offset"],
    "spoilers": ["Near ", " (", ") - ", " away in ", " o'clock direction, ",
                 " height offset"]
}


def parseDirections(directions):
    if directions.startswith(directionConnectors["slots"][0]):
        connectors = directionConnectors["slots"]
    else:
        connectors = directionConnectors["spoilers"]
    splitLine = directions
    strings = dict()
    index = 0
    for connector in connectors:
        splitLine = splitLine.split(connector)
        key = directionConnectors["keys"][index]
        if key:
            strings[key] = splitLine[0]
        splitLine = splitLine[1]
        index += 1
    return strings


def scriptDirections(strings, connect="spoilers"):
    directions = directionConnectors[connect][0]
    index = 1
    for key in strings:
        directions += strings[key]
        directions += directionConnectors[connect][index]
        index += 1
    return directions

