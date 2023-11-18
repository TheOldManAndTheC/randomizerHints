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
from copy import deepcopy
from source.utils.entryMatch import entryMatch
from source.data.model.randomizerData.containerFixes import containerFixes
from source.data.model.randomizerData.notRandomized import notRandomized
import source.data.model.randomizerData.loadSpoilers.directionFixes as dF


namesWithColons = [
    "Ash of War",
    "Note",
    "Aspects of the Crucible",
    "Map"
]


# Parses the item and enemy randomizer spoilers text file and creates the
# spoiler structure of item entries, along with the boss and enemy replacement
# structures. Returns all three of these and the random seed from the spoiler
# file.
def loadSpoilers(spoilerLines):
    spoilers = dict()
    bossDict = dict()
    enemyDict = dict()
    directionFixes = deepcopy(dF.directionFixes)
    regularEnemyPlacements = False
    lineIter = iter(spoilerLines)
    nextLine = next(lineIter)[:-1]  # remove newline
    # get the seed to prime the rng so randomly generated item hints will
    # be consistent
    seed = int(nextLine.split("seed:", 2)[2].split(" ", 1)[0])
    previousFix = dict()
    while True:
        line = nextLine
        if line is None:
            break
        nextLine = next(lineIter, None)
        if nextLine is not None:
            nextLine = nextLine[:-1]  # remove newline

        # skip items that aren't randomized
        skip = False
        for prefix in notRandomized:
            if line.startswith(prefix):
                skip = True
                break
        if skip:
            continue

        # switch from boss enemy placements to regular enemy placements
        if line.startswith("-- Basic placements"):
            regularEnemyPlacements = True
            continue

        # Boss and enemy placements
        if line.startswith("Replacing "):
            splitLine = line.split(" (#", 1)
            replacedEnemy = splitLine[0][10:]  # skip "Replacing "
            line = splitLine[1]
            splitLine = line.split(") in ", 1)
            replacedID = splitLine[0]
            line = splitLine[1]
            splitLine = line.split(": ", 1)
            enemyRegion = splitLine[0]
            line = splitLine[1]
            splitLine = line.split(" (#", 1)
            newEnemy = splitLine[0]
            line = splitLine[1]
            splitLine = line.split(") from ")
            newID = splitLine[0]
            if regularEnemyPlacements:
                resultsDict = enemyDict
            else:
                resultsDict = bossDict
            if replacedEnemy not in resultsDict:
                resultsDict[replacedEnemy] = dict()
            enemyEntry = resultsDict[replacedEnemy]
            if replacedID in enemyEntry:
                warn("Parse error, duplicate enemy ID: " + replacedID,
                     SyntaxWarning)
            else:
                enemyEntry[replacedID] = {
                    "replacedEnemy": replacedEnemy,
                    "replacedID": replacedID,
                    "newEnemy": newEnemy,
                    "newID": newID,
                    "enemyRegion": enemyRegion
                }
        if ". Replaces " not in line:  # Not an item entry
            continue

        itemEntry = dict()
        # get the vanilla item this item replaces
        splitLine = line.split(". Replaces ", 1)
        line = splitLine[0]
        itemEntry["replaces"] = splitLine[1][:-1]  # remove the .
        # account for the extra ':' in some items
        extraColon = False
        for prefix in namesWithColons:
            if line.startswith(prefix):
                splitLine = line.split(": ", 2)
                splitLine[0] = splitLine[0] + ": " + splitLine[1]
                splitLine[1] = splitLine[2]
                extraColon = True
                break
        if not extraColon:
            splitLine = line.split(": ", 1)
        item = splitLine[0]
        line = splitLine[1]

        splitLine = item.split(" in ", 1)
        item = splitLine[0]
        # get quantity from the end of the item name if any
        if item[-1] == "x" and item[-2].isdigit():
            if item[-3].isdigit():
                itemEntry["quantity"] = item[-3:-1]
                item = item[:-4]
            else:
                itemEntry["quantity"] = item[-2:-1]
                item = item[:-3]
        itemEntry["newItem"] = item
        # it's an item with a region (not necessarily accurate)
        if len(splitLine) > 1:
            itemEntry["region"] = splitLine[1]

        # has a container name and possibly directions, not a custom
        # description
        # since some custom description lines actually start with
        # "From" filter them
        if line.startswith("From") and not line.startswith("From a ") and \
                not line.startswith("From an ") and \
                not line.startswith("From the "):
            splitLine = line.split(". ", 1)
            itemEntry["container"] = splitLine[0][5:]  # skip the "From"
            if len(splitLine) > 1:
                line = splitLine[1]
            else:
                line = ""
            # get the container ID if there is one
            splitLine = itemEntry["container"].split(" (#", 1)
            if len(splitLine) > 1:
                itemEntry["container"] = splitLine[0]
                itemEntry["containerID"] = splitLine[1][:-1]  # skip )
            # if it's directions, it's the rest of the line
            if line.startswith("Near "):
                itemEntry["directions"] = line
                line = ""
            # fix container names that cause a problem with searching the
            # item slots (currently only Kenneth Haight)
            if itemEntry["container"] in containerFixes:
                itemEntry["container"] = \
                    containerFixes[itemEntry["container"]]

        # if it's a random drop save the drop chance and set drop and
        # enemy entries
        if nextLine.startswith("  Drop chance for "):
            chance = float(nextLine.split(": ")[1][:-1])  # skip %
            itemEntry["dropChance"] = chance
            itemEntry["enemy"] = itemEntry["container"]

        # anything else is text description
        itemEntry["text"] = line
        # set empty directions for later comparisons
        if "directions" not in itemEntry:
            itemEntry["directions"] = ""

        # special case fixes for items with no directions
        fixed = False
        for directionFix in directionFixes:
            # certain fixes are only done once, this is so we can have
            # sequential fixes for certain items that have identical
            # matches in different locations.  however, there may be
            # multiple items stacked in the same location, and they will
            # come directly after each other, so we save the previous fix
            # to allow the same unique fix to be used for every item in
            # that location
            if "done" in directionFix and \
                    not directionFix == previousFix:
                continue
            if entryMatch(itemEntry, directionFix["conditions"]):
                for fix in directionFix["fixes"]:
                    itemEntry[fix] = directionFix["fixes"][fix]
                fixed = True
                # if it's a one time fix, mark it as having been done but
                # save the fix to allow piggyback items
                if "one_time" in directionFix:
                    directionFix["done"] = True
                    previousFix = directionFix
                # clear the saved fix if it's not a one time fix
                else:
                    previousFix = dict()
                break
        # clear saved fix if there was no fix needed for this item,
        # as there will be no piggybacking
        if not fixed:
            previousFix = dict()

        # add the item entry to the database
        if item in spoilers:
            spoilers[item].append(itemEntry)
        else:
            spoilers[item] = [itemEntry]
    return seed, spoilers, bossDict, enemyDict
