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

from source.utils.entryMatch import entryMatch
from source.model.randomizer.directionUtils import parseDirections
from source.data.model.fogData.fogRegionHints import fogRegionHints
from source.data.model.fogData.fogRegionHints import fogShopRegionHints
from source.data.model.randomizerData.containerFixes import containerFixes
from source.data.model.randomizerData.notRandomized import notRandomized
from source.data.model.randomizerData.processItemEntry.itemFixes \
    import itemFixes
from source.data.model.randomizerData.processItemEntry.processItemEntryData \
    import duplicateContainerNames
from source.data.model.randomizerData.processItemEntry.processItemEntryData \
    import duplicateLocationNames
from source.data.model.randomizerData.processItemEntry.processItemEntryData \
    import npcNames
from source.data.model.randomizerData.processItemEntry.processItemEntryData \
    import staticContainers
from source.data.model.randomizerData.processItemEntry.regionHints \
    import regionHints


# given an item entry, process and add data to it to assist in generating hints
def processItemEntry(itemEntry, randomized, enemyDict, bossDict, areas):
    # if it's marked as ignore or norandom in itemslots.txt, skip it
    if "ignore" in itemEntry["tags"] or "norandom" in itemEntry["tags"]:
        return False
    if "replaces" not in itemEntry:
        itemEntry["replaces"] = itemEntry["item"]
    # TODO: ON UPDATE: this will need to be checked and any
    #   conflicting directions that aren't resolved with the first
    #   set of directions will need to be put in directionFixes
    # if there is a directions list, and we don't already have
    # directions, use the first one in the list
    if not itemEntry["directions"] and itemEntry["directionsList"]:
        itemEntry["directions"] = itemEntry["directionsList"][0]
    # if we do have directions, we need to find the raw version of them for
    # better compass accuracy
    if itemEntry["directions"] and itemEntry["rawDirectionsList"]:
        # if there's only one, use it
        if len(itemEntry["rawDirectionsList"]) == 1:
            itemEntry["rawDirections"] = \
                parseDirections(itemEntry["rawDirectionsList"][0])
        else:
            # need to find a matching raw direction string, so we can get
            # better accuracy on the compass
            strings = parseDirections(itemEntry["directions"])
            for rawDirections in itemEntry["rawDirectionsList"]:
                rawStrings = parseDirections(rawDirections)
                if rawStrings["landmark"] != strings["landmark"]:
                    continue
                if rawStrings["horiz"] != strings["horiz"]:
                    continue
                if rawStrings["vert"] != strings["vert"]:
                    continue
                # if all the non-angle strings match, it's almost certainly
                # the one
                itemEntry["rawDirections"] = rawStrings
    if "rawDirections" in itemEntry:
        itemEntry["hintLandmark"] = itemEntry["rawDirections"]["landmark"]
    # if it's a book or bell bearing, set the container and the parent
    # entry
    if "book" in itemEntry:
        itemEntry["container"] = itemEntry["book"]
        if itemEntry["book"] in randomized:
            itemEntry["parentEntries"] = randomized[itemEntry["book"]]
    # make sure there's a container
    if "container" not in itemEntry:
        containerNames = itemEntry["containerNames"]
        if not containerNames:
            warn("No container names: " + str(itemEntry), SyntaxWarning)
        # set correct container names for items with multiple containers
        if len(containerNames) > 1:
            for containerName in containerNames:
                if containerName in duplicateContainerNames:
                    itemEntry["container"] = \
                        duplicateContainerNames[containerName]
                    break
            # if there's none in the duplicate list, just use the first one
            if "container" not in itemEntry:
                itemEntry["container"] = containerNames[0]
        else:
            itemEntry["container"] = containerNames[0]
    # special case item fixes
    for itemFix in itemFixes:
        if entryMatch(itemEntry, itemFix["conditions"]):
            for fix in itemFix["fixes"]:
                itemEntry[fix] = itemFix["fixes"][fix]
            break
    # set static container/NPC states
    # special case for Gideon's boss fight, consider that entry as an enemy
    if itemEntry["container"] in npcNames and \
            itemEntry["replaces"] != "Scepter of the All-Knowing":
        itemEntry["NPC"] = npcNames[itemEntry["container"]]
    elif itemEntry["container"] in staticContainers:
        itemEntry["staticContainer"] = True
    elif "book" not in itemEntry:
        # if it's not an NPC item, in a static container, or in a book,
        # it's an enemy drop
        itemEntry["enemy"] = itemEntry["container"]
        # fix enemy names that cause a problem with finding their
        # randomized replacements
        if itemEntry["enemy"] in containerFixes:
            itemEntry["enemy"] = containerFixes[itemEntry["enemy"]]

    # # make adjustments to directions for non-NPC items
    # if "NPC" not in itemEntry and "book" not in itemEntry and \
    #         "rawDirections" in itemEntry:
    #     # break the raw directions strings down into numbers for the hints
    #     itemEntry["hintLandmark"] = itemEntry["rawDirections"]["landmark"]
    #     itemEntry["hintDistance"] = float(itemEntry["rawDirections"]["horiz"])
    #     # get the clock compass direction
    #     itemEntry["hintAngle"] = float(itemEntry["rawDirections"]["angle"])
    #     # get the vertical distance
    #     itemEntry["hintHeight"] = float(itemEntry["rawDirections"]["vert"])

    # set the randomized enemies for each item entry
    if "enemy" in itemEntry:
        if "newEnemy" not in itemEntry:
            enemyName = itemEntry["enemy"]
            newEnemyName = "an enemy"
            containerID = ""
            if "containerID" in itemEntry:
                containerID = itemEntry["containerID"]
            elif len(itemEntry["containerIDs"]) == 1:
                containerID = itemEntry["containerIDs"][0]
            if enemyName in enemyDict:
                enemyEntry = enemyDict[enemyName]
                if containerID in enemyEntry:
                    newEnemyName = enemyEntry[containerID]["newEnemy"]
            if enemyName in bossDict:
                enemyEntry = bossDict[enemyName]
                if containerID in enemyEntry:
                    newEnemyName = enemyEntry[containerID]["newEnemy"]
            if enemyName in notRandomized:
                newEnemyName = enemyName
            itemEntry["newEnemy"] = newEnemyName

    # set a proper region for the item
    hintRegion = itemEntry["region"]
    if itemEntry["mapList"]:
        hintRegion = areas.areasByMapID[itemEntry["mapList"][0]][0]
    hintArea = hintRegion
    graphRegion = None

    # search through regionHints for a region, select the first match.
    # this means hints should be ordered specific to general
    if hintRegion in regionHints:
        regionEntry = regionHints[hintRegion]
        hintRegion = regionEntry["hintRegion"]
        if "hintArea" in regionEntry:
            hintArea = regionEntry["hintArea"]
        else:
            hintArea = hintRegion
        if "graphRegion" in regionEntry:
            graphRegion = regionEntry["graphRegion"]
        if "exceptions" in regionEntry:
            for altEntry in regionEntry["exceptions"]:
                if entryMatch(itemEntry, altEntry,
                              ["hintRegion", "hintArea", "graphRegion"]):
                    hintRegion = altEntry["hintRegion"]
                    if "hintArea" in altEntry:
                        hintArea = altEntry["hintArea"]
                    else:
                        hintArea = hintRegion
                    if "graphRegion" in altEntry:
                        graphRegion = altEntry["graphRegion"]
                    break
    else:
        warn("Missing hintRegion: " + hintRegion + " for " +
             itemEntry["replaces"], SyntaxWarning)

    itemEntry["hintRegion"] = hintRegion
    itemEntry["hintArea"] = hintArea
    if graphRegion:
        itemEntry["graphRegion"] = graphRegion
        itemEntry["hintLocation"] = graphRegion
    elif hintArea in duplicateLocationNames:
        itemEntry["hintLocation"] = hintArea + " in " + hintRegion
    else:
        itemEntry["hintLocation"] = hintArea
    itemEntry["fogHintArea"] = itemEntry["hintLocation"]
    if "isShop" in itemEntry:
        if itemEntry["lotID"] in fogShopRegionHints:
            itemEntry["fogHintArea"] = \
                fogShopRegionHints[itemEntry["lotID"]]
    else:
        if itemEntry["lotID"] in fogRegionHints:
            itemEntry["fogHintArea"] = \
                fogRegionHints[itemEntry["lotID"]]
    return True
