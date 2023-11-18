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

headerText = \
    "Item lots that can't be matched with their replaced " \
    "enemies/NPCs\n\n" \
    "If you don't know what this file is for, disregard it.\n\n" \
    "If it's an NPC, add the container name to npcNames with the " \
    "NPCs actual name as the value\n" \
    "If it's an enemy, find the name used in the spoilers file for " \
    "enemy replacement and its associated ID, then make an entry " \
    "in itemFixes that updates the container and containerID. You " \
    "might need to add qualifiers for replaces, region, and so on " \
    "depending on how large the list of possible candidates is.\n\n"
regionText = "Region: {}:\n"
replacesText = "    Replaces {} with {}\n"
directionsText = "    Directions: {}\n"
containerText = "  Container name: {}\n"
containerIDText = "    Container ID: {}\n"
containerIDsText = "    Container ID list: {}\n"
spoilerText = "    Spoiler text: {}\n"
candidatesText = "    Potential candidates:\n"


# TODO: ON UPDATE: check missing_enemies.txt
# creates af formatted file of item entries with missing enemy associations and
# possible candidates to be placed in itemFixes
def exportMissingEnemies(missingEnemies, bossDict, enemyDict):
    missing = dict()
    for itemEntry in missingEnemies:
        enemyName = itemEntry["enemy"]
        enemyRegion = itemEntry["region"]
        if enemyRegion not in missing:
            missing[enemyRegion] = dict()
        regionEntry = missing[enemyRegion]
        if enemyName not in regionEntry:
            regionEntry[enemyName] = {
                "itemEntries": [],
                "enemyEntries": []
            }
        regionEntry[enemyName]["itemEntries"].append(itemEntry)
        enemyEntries = regionEntry[enemyName]["enemyEntries"]
        if enemyName in enemyDict:
            for enemyEntry in enemyDict[enemyName].values():
                if enemyEntry["enemyRegion"] == enemyRegion and \
                        enemyEntry not in enemyEntries:
                    enemyEntries.append(enemyEntry)
        if enemyName in bossDict:
            for enemyEntry in bossDict[enemyName].values():
                if enemyEntry["enemyRegion"] == enemyRegion and \
                        enemyEntry not in enemyEntries:
                    enemyEntries.append(enemyEntry)
    missingText = headerText
    for region in missing:
        missingText += regionText.format(region)
        regionEntry = missing[region]
        for enemyName in regionEntry:
            missingText += containerText.format(enemyName)
            for itemEntry in regionEntry[enemyName]["itemEntries"]:
                missingText += replacesText.format(itemEntry["replaces"],
                                                   itemEntry["newItem"])
                missingText += directionsText.format(itemEntry["directions"])
                if "containerID" in itemEntry:
                    missingText += \
                        containerIDText.format(itemEntry["containerID"])
                if "containerIDs" in itemEntry:
                    missingText += \
                        containerIDsText.format(itemEntry["containerIDs"])
                if itemEntry["text"]:
                    missingText += spoilerText.format(itemEntry["text"])
            missingText += "\n"
            if regionEntry[enemyName]["enemyEntries"]:
                missingText += candidatesText
            for enemyEntry in regionEntry[enemyName]["enemyEntries"]:
                missingText += \
                    "{} ({}) > {}\n".format(enemyEntry["replacedEnemy"],
                                            enemyEntry["replacedID"],
                                            enemyEntry["newEnemy"])
            missingText += "\n"
        missingText += "\n"
    return missingText
