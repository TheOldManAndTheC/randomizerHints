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

import math
from warnings import warn
from source.utils.rng import rng
from source.utils.randomExtras import triangularRandom
from source.data.model.hintData.hintComponents.hintIcons import hintIcons
from source.data.model.hintData.hintComponents.hintNames import hintNames
from source.data.model.hintData.hintComponents.enemyHints import enemyHints
from source.data.model.hintData.hintComponents.npcHints import npcHints
from source.data.model.hintData.hintComponents.hintComponentsData \
    import useDirections
from source.data.model.hintData.hintComponents.hintComponentsData \
    import movingNPCs
from source.data.model.hintData.hintComponents.hintComponentsData \
    import hintItemCorrections

iconTypes = ["map", "note", "scroll", "book"]
compass = {
    (0.0, 11.25): "north",
    (11.25, 33.75): "north-northeast",
    (33.75, 56.25): "northeast",
    (56.25, 78.75): "east-northeast",
    (78.75, 101.25): "east",
    (101.25, 123.75): "east-southeast",
    (123.75, 146.25): "southeast",
    (146.25, 168.75): "south-southeast",
    (168.75, 191.25): "south",
    (191.25, 213.75): "south-southwest",
    (213.75, 236.25): "southwest",
    (236.25, 258.75): "west-southwest",
    (258.75, 281.25): "west",
    (281.25, 303.75): "west-northwest",
    (303.75, 326.25): "northwest",
    (326.25, 348.75): "north-northwest",
    (348.75, 360.0): "north",
}


# Get a complete sorted list of unique adjective choices that apply to the icon
# with the given iconID, expanding all sublists from hintNames["adjectives"]
def getAdjectivesForIconID(iconID):
    adjectivesList = []
    iconAdjectives = hintIcons[iconID]["adjectives"]
    for adjective in iconAdjectives:
        if isinstance(adjective, list):
            # we can't sort a list with a sublist, so if there's a sublist,
            # just pick a random item from it to add since we'd need to do that
            # anyway if this element gets picked
            adjectivesList.append(rng.choice(adjective))
            continue
        if adjective in hintNames["adjectives"]:
            adjectivesList += hintNames["adjectives"][adjective]
            continue
        if adjective not in adjectivesList:
            adjectivesList.append(adjective)
    return adjectivesList


# Get a complete sorted list of unique owner names from the
# hintNames["ownerGroups"] group dictionary, expanding all subgroups
def getOwnersFromGroups(groupList):
    ownersSet = set()
    for key in groupList:
        if key not in hintNames["ownerGroups"]:
            ownersSet.add(key)
            continue
        ownersSet = ownersSet.union(
            set(getOwnersFromGroups(hintNames["ownerGroups"][key]))
        )
    ownersList = list(ownersSet)
    # need to sort the owner list since the sets it was created from
    # have undefined order, to keep from interfering with the seeded
    # random sequence
    ownersList.sort()
    return ownersList


def triangularHint(hintList, delimiter="|"):
    return \
        rng.choice(hintList[triangularRandom(len(hintList))].split(delimiter))


def getEnemyHint(itemEntry):
    enemy = itemEntry["newEnemy"]
    if enemy in enemyHints:
        enemyHintList = enemyHints[enemy]
    else:
        enemyHintList = ["enemy|foe"]
    enemyHint = triangularHint(enemyHintList)
    return enemyHint


def getDirections(itemEntry, useFogAreas, useAllDirections):
    directions = {
        "location": "",
        "landmark": "",
        "angle": "",
        "height": "",
        "distance": "",
    }
    if useFogAreas:
        directions["location"] = itemEntry["fogHintArea"]
    else:
        directions["location"] = itemEntry["hintLocation"]
    if (not useAllDirections and directions["location"] not in useDirections) \
            or "hintLandmark" not in itemEntry:
        return directions
    directions["landmark"] = itemEntry["hintLandmark"]
    height = float(itemEntry["rawDirections"]["vert"])
    distance = float(itemEntry["rawDirections"]["horiz"])
    heightAngle = math.atan2(height, distance)/math.pi * 180
    # ignore height differences if it's a gentle slope
    if math.fabs(heightAngle) > 15:
        if height < -60.0:
            directions["height"] = "far below"
        elif height < -10.0:
            directions["height"] = "below"
        elif height > 60.0:
            directions["height"] = "far above"
        elif height > 10.0:
            directions["height"] = "above"
    if distance < 40.0:
        directions["distance"] = "near"
    elif distance > 120.0:
        directions["distance"] = "far"
    if directions["distance"] != "near":
        angle = float(itemEntry["rawDirections"]["angle"]) * 30.0
        for (low, high) in compass:
            if low <= angle <= high:
                directions["angle"] = compass[(low, high)]
                break
    return directions


def generateComponentEntry(itemEntry, useFogAreas, useAllDirections):
    hintEntry = {
        "itemEntry": itemEntry,
        "quantity": "",
    }
    # make item name corrections
    if itemEntry["newItem"] in hintItemCorrections:
        hintEntry["item"] = hintItemCorrections[itemEntry["newItem"]]
    else:
        hintEntry["item"] = itemEntry["newItem"]
    # quantity if any
    if "quantity" in itemEntry:
        hintEntry["quantity"] = itemEntry["quantity"]
    # chance hints for random monster drops
    if "dropChance" in itemEntry:
        chance = itemEntry["dropChance"]
        if chance == 100.0:
            hintEntry["chance"] = "always"
        elif chance > 50.0:
            hintEntry["chance"] = "often"
        elif chance > 25.0:
            hintEntry["chance"] = ""
        elif chance > 10.0:
            hintEntry["chance"] = "sometimes"
        elif chance > 5.0:
            hintEntry["chance"] = "rarely"
        else:
            hintEntry["chance"] = "very rarely"
        hintEntry["enemy"] = itemEntry["enemy"]
        # use the first and most specific enemy hint name for random drops
        if hintEntry["enemy"] in enemyHints:
            hintEntry["enemy"] = enemyHints[hintEntry["enemy"]][0]
        # if it's a random drop entry, we're done
        return hintEntry
    # hints for items contained within books, paintings, or remembrances
    if "book" in itemEntry:
        hintEntry["book"] = itemEntry["book"]
        if "parentEntries" in itemEntry:
            parentEntries = itemEntry["parentEntries"]
            hintEntry["parentEntry"] = \
                generateComponentEntry(rng.choice(parentEntries), useFogAreas,
                                       useAllDirections)
    # get the region and directions for the item if any
    hintEntry["directions"] = \
        getDirections(itemEntry, useFogAreas, useAllDirections)
    # hints for NPC items
    if "NPC" in itemEntry:
        npc = itemEntry["NPC"]
        hintEntry["NPC"] = triangularHint(npcHints[npc])
        if "isShop" in itemEntry:
            hintEntry["isShop"] = itemEntry["isShop"]
        hintEntry["npcLocation"] = ""
        if npc not in movingNPCs:
            hintEntry["npcLocation"] = hintEntry["directions"]["location"]
        if "killQuest" in itemEntry:
            if "parentEntries" not in itemEntry:
                warn("Missing killQuest parents for: " + str(itemEntry),
                     SyntaxWarning)
            parentEntry = itemEntry["parentEntries"][0]
            if useFogAreas:
                hintEntry["foeLocation"] = parentEntry["fogHintArea"]
            else:
                hintEntry["foeLocation"] = parentEntry["hintLocation"]
            hintEntry["foeDirections"] = getDirections(parentEntry, useFogAreas,
                                                       useAllDirections)
            hintEntry["foe"] = getEnemyHint(parentEntry)
    if "newEnemy" in itemEntry:
        # use a random enemy hint name for unique enemy drops
        hintEntry["enemy"] = getEnemyHint(itemEntry)
    return hintEntry


# Given a hint entry dictionary, generate the components needed to script a hint
def hintComponents(hintEntryDict, itemInfo, useFogAreas, useAllDirections):
    hintEntries = hintEntryDict["hintEntries"]
    components = {"isItem": "newItem" in hintEntries[0]}
    if "hintName" in hintEntryDict:
        components["hintName"] = hintEntryDict["hintName"]
    if "hintDescription" in hintEntryDict:
        components["hintDescription"] = hintEntryDict["hintDescription"]

    # process the hint entries
    hintRegionList = []
    if components["isItem"]:
        ownerGroupChoices = []
        components["label"] = "HINTS: "
    else:
        ownerGroupChoices = ["GROUP_EXPLORER", "GROUP_MERCHANT",
                             "GROUP_ENTERTAINER", "GROUP_LORD"]
        components["label"] = "FOG HINTS: "
    newEntries = []
    for entry in hintEntries:
        if "hintRegion" in entry:
            hintRegionList.append(entry["hintRegion"])
        if "ownerGroups" in entry:
            ownerGroupChoices += entry["ownerGroups"]
        if not components["isItem"]:
            components["label"] += entry["area"] + "-" + entry["gate"] + "|"
            continue
        if entry["newItem"] in itemInfo:
            ownerGroupChoices += itemInfo[entry["newItem"]]["ownerGroups"]
        components["label"] += entry["newItem"] + "|"
        newEntries.append(generateComponentEntry(entry, useFogAreas,
                                                 useAllDirections))
    components["label"] = components["label"][:-1].replace(",", "")
    # if this is a fog hint, just need to pass on the original entries
    if not components["isItem"]:
        components["hintEntries"] = hintEntries
    else:
        components["hintEntries"] = newEntries

    # Pick an icon
    if "hintIconTypes" in hintEntryDict:
        hintIconTypes = hintEntryDict["hintIconTypes"]
    else:
        hintIconTypes = iconTypes
    iconIDs = []
    for iconID in hintIcons:
        if hintIcons[iconID]["type"] not in hintIconTypes:
            continue
        if "hintRegions" not in hintIcons[iconID]:
            iconIDs.append(iconID)
            continue
        # only allow region-based icons that match the regions of items in
        # the hint
        for hintRegion in hintIcons[iconID]["hintRegions"]:
            if hintRegion in hintRegionList:
                iconIDs.append(iconID)
                break
    components["iconID"] = rng.choice(iconIDs)
    components["noteName"] = \
        rng.choice(hintNames["type"][hintIcons[components["iconID"]]["type"]])

    # Pick an owner
    if "hintName" not in components:
        if not ownerGroupChoices:
            # use a generic owner name
            components["ownerName"] = \
                rng.choice(hintNames["ownerGroups"]["GENERIC_OWNER"])
            # since it's a generic owner, add a random adjective
            components["ownerAdjective"] = \
                rng.choice(hintNames["ownerGroups"]["GENERIC_OWNER_ADJECTIVE"])
        else:
            # only pick from the groups most represented in the hint
            highestGroupChoices = []
            highestGroupCount = 0
            for group in ownerGroupChoices:
                groupCount = ownerGroupChoices.count(group)
                if groupCount > highestGroupCount:
                    highestGroupChoices = [group]
                    highestGroupCount = groupCount
                elif groupCount == highestGroupCount and \
                        group not in highestGroupChoices:
                    highestGroupChoices.append(group)
            components["ownerName"] = \
                rng.choice(getOwnersFromGroups(highestGroupChoices))

    # Pick a pair of unique adjectives for the description
    if "hintDescription" not in components:
        adjectives = getAdjectivesForIconID(components["iconID"])
        adjective1 = rng.choice(adjectives)
        adjective2 = adjective1
        while adjective2 == adjective1:
            adjective2 = rng.choice(adjectives)
        if isinstance(adjective1, list):
            adjective1 = rng.choice(adjective1)
        if isinstance(adjective2, list):
            adjective2 = rng.choice(adjective2)
        components["noteAdjectives"] = [adjective1, adjective2]

    return components
