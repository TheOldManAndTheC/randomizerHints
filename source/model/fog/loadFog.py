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
from source.data.model.fogData.loadFogData import fogBasicLines
from source.data.model.fogData.loadFogData import fogSubKeys


# returns a key from the key list if the start of the line matches it
def getKey(line, keyList):
    if not line:
        return None
    for key in keyList:
        if line.startswith(key):
            return key
    return None


# tests if the current level of line indentation has ended
def indentEnded(line, indent):
    for index in range(indent):
        if line[index] != " ":
            return True
    return False


# recursively process the fog.txt file to build a structure of areas and gates
def parseSubEntry(lineIter, indent, validKeys=None, isRoot=False):
    # new dictionary for this nesting level
    entry = dict()
    line = None
    ignore = False
    while True:
        # if there is not already a line from the previous iteration, read one
        if line is None:
            line = next(lineIter, None)
            if line is not None:
                line = line[:-1]  # remove newline
        # if we're at the end of this indent level or EOF, stop iterating
        if line is None or indentEnded(line, indent):
            break
        subLine = line[indent:]  # remove leading spaces
        # check if the line starts another nesting level
        subKey = getKey(subLine, fogSubKeys)
        # only continue this level if the key is valid or all keys are valid
        if validKeys and subKey not in validKeys:
            break
        # if it is another nesting level
        if subKey:
            # get the metadata for this type of key
            subEntry = fogSubKeys[subKey]
            # if it's a root level key, and we're not in the root level, pop
            if not isRoot and "isRoot" in subEntry:
                break
            # if this key and its data are to be ignored set the flag
            if "ignore" in subEntry:
                ignore = True
            # otherwise if this is a root key that is not ignored, stop ignoring
            elif "isRoot" in subEntry:
                ignore = False
            # if we're currently in ignore mode
            if ignore:
                # clear the line so the next one will be read and skip
                line = None
                continue
            # get the key name at the end of the line
            key = subLine[len(subKey):]
            # if there is not there, the key is the line itself
            if not key:
                key = subEntry["key"]
            # if the key is for a list of lines
            if "isList" in subEntry:
                lineList = []
                listIndent = indent + subEntry["indent"]
                # read lines until this nesting level is over, EOF, or an
                # actual key line is found
                while True:
                    line = next(lineIter, None)
                    if line is None or indentEnded(line, listIndent):
                        break
                    line = line[:-1]  # remove newline
                    subLine = line[indent:]  # remove leading spaces
                    if getKey(subLine, fogSubKeys) or \
                            getKey(subLine, fogBasicLines):
                        break
                    lineList.append(line)
                # add the list to the entry
                entry[key] = lineList
            else:
                # otherwise recursively parse the next nesting level down
                newSubDict, line = parseSubEntry(lineIter,
                                                 indent + subEntry["indent"],
                                                 subEntry["validKeys"])
                # if this key is already taken
                if key in entry:
                    # get the old entry
                    oldSubObject = entry[key]
                    # if it's a dictionary, that was the first one, make it the
                    # first member of a new list
                    if isinstance(oldSubObject, dict):
                        oldSubObject = [oldSubObject]
                        entry[key] = oldSubObject
                    # add the new entry to the list of entries for this key
                    oldSubObject.append(newSubDict)
                else:
                    # otherwise it's a new key, just add it
                    entry[key] = newSubDict

            # start the next iteration with the line after the previous nesting
            # level
            continue
        # if we're currently in ignore mode
        if ignore:
            # clear the line so the next one will be read and skip
            line = None
            continue
        # check if the line is a basic key data line
        lineKey = getKey(subLine, fogBasicLines)
        # only continue this level if the key is valid or all keys are valid
        if validKeys and lineKey not in validKeys:
            break
        # if it was a valid key, add it and its data to the entry
        if lineKey:
            entry[fogBasicLines[lineKey]] = subLine[len(lineKey):]
            # clear the line so the next one will be read and skip
            line = None
            continue
        # if we got here, there's an unknown line key type or other syntax issue
        warn("Parse error, unknown line: " + line, SyntaxWarning)
        # clear the line so the next one will be read
        line = None
    # iteration complete, return this nesting level entry along with the line
    # that came after it
    return entry, line


def loadFog(fogLines):
    # load the area/gate structure from the fog.txt file
    fog, _ = parseSubEntry(iter(fogLines), 0, isRoot=True)
    return fog
