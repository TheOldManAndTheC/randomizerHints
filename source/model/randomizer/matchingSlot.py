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
from source.model.randomizer.directionUtils import parseDirections
from source.model.randomizer.directionUtils import scriptDirections

noMatchText = "Unable to find single matching item slot:\nitemEntry: {}\n"\
              "matchedTextSlots: {}\nmatchedDirectionsSlots: {}\n"\
              "matchedRegionSlots: {}\nmatchedContainerSlots: {}\n"


# given an item entry from the spoilers file, find a matching itemslots.txt
# entry
def matchingSlot(itemEntry, itemSlots, areas):
    # find the item slot that matches this entry
    slotList = itemSlots[itemEntry["replaces"]]
    if not slotList:
        warn("No item slots entry for: " + str(itemEntry), SyntaxWarning)
    if len(slotList) == 1:
        return slotList[0]
    # there's more than one item slot candidate for this item
    matchedTextSlots = []
    matchedDirectionsSlots = []
    matchedRegionSlots = []
    matchedContainerSlots = []
    for slotEntry in slotList:
        # find it based on the spoiler text
        # spoilers.txt is inconsistent about which periods are
        # preserved from the text descriptions
        if itemEntry["text"] == slotEntry["text"] or \
                itemEntry["text"] + "." == slotEntry["text"]:
            if slotEntry not in matchedTextSlots:
                matchedTextSlots.append(slotEntry)
        # find it based on the generic directions in spoilers.txt
        directionsList = slotEntry["directionsList"]
        if itemEntry["directions"] in directionsList:
            if slotEntry not in matchedDirectionsSlots:
                matchedDirectionsSlots.append(slotEntry)
        elif itemEntry["directions"]:
            strings = parseDirections(itemEntry["directions"])
            # try again with an adjusted angle to account for
            # rounding jitter
            angle = int(strings["angle"]) + 1
            if angle > 12:
                angle = 1
            strings["angle"] = str(angle)
            adjustedDirections = scriptDirections(strings)
            if adjustedDirections in directionsList:
                if slotEntry not in matchedDirectionsSlots:
                    matchedDirectionsSlots.append(slotEntry)
        # find it based on region
        for areaMap in areas.mapIDsByArea[itemEntry["region"]]:
            if areaMap in slotEntry["mapList"]:
                if slotEntry not in matchedRegionSlots:
                    matchedRegionSlots.append(slotEntry)
        # find it based on container
        if "container" in itemEntry and \
                len(slotEntry["containerNames"]) == 1 and \
                itemEntry["container"] == slotEntry["containerNames"][0]:
            if slotEntry not in matchedContainerSlots:
                matchedContainerSlots.append(slotEntry)

    # there should only be one matching directions slot
    if len(matchedDirectionsSlots) > 1:
        warn("Multiple directions match: " + str(matchedDirectionsSlots),
             SyntaxWarning)
    # if there was only one matching text slot, use that
    if len(matchedTextSlots) == 1:
        return matchedTextSlots.pop()
    # if there was only one matching directions slot, use that
    elif len(matchedDirectionsSlots) == 1:
        return matchedDirectionsSlots.pop()
    # if there was only one region match, use that
    elif len(matchedRegionSlots) == 1:
        return matchedRegionSlots.pop()
    # finally if there was only one container match use that
    # currently only Kenneth Haight's Golden Seed drop
    elif len(matchedContainerSlots) == 1:
        return matchedContainerSlots.pop()
    # new special cases that need to be fixed above
    warn(noMatchText.format(itemEntry, matchedTextSlots, matchedDirectionsSlots,
                            matchedRegionSlots, matchedContainerSlots),
         SyntaxWarning)
    return None
