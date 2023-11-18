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

# Find a free lot ID, how many consecutive free lots follow it, and a lot flag
# following the given row ID in the given param CSV dict
def freeRange(rowID, csvDict):
    if not rowID:
        return None
    index = int(rowID)
    # if the given lot is not in the randomized set, step backwards to find
    # the first extant lot in this range
    # if it's more than 8 lots before we find one then this lot doesn't exist
    # here, it's in ItemLotParam_enemy
    # testing shows that there are two specific lots, 449020002 and 449020012
    # that are the non-hostile large Living Jars in Jarburg that are always
    # handled in ItemLotParam_enemy, and every time I ran it no more than one
    # other random lot ended up handled this way.  considering the number of
    # lots available, I don't see a need to do a completely separate set of CSV
    # handling code just for a bare few lots, two of which are basically NPCs
    # that can break Jar-Bairn's quest so for now any lots not in
    # ItemLotParam_map gets treated as an unavailable lot.
    searched = 0
    while searched < 9 and index > 0 and str(index) not in csvDict:
        searched += 1
        index -= 1
    if searched >= 9:
        return None
    # if this CSV has a lot flag column (itemLotParam_*), make sure we have a
    # nonzero lot flag
    lotFlag = None
    if "getItemFlagId" in csvDict[str(index)]:
        # if the lot flag is 0 (random drops), then walk back through the
        # connected lots until we hit an entry with one
        lotFlag = csvDict[str(index)]["getItemFlagId"]
        # this loop doesn't seem to fail with an empty row lookup, so for now
        # we'll leave it like this, but there probably should be some checking
        # here
        while lotFlag == "0":
            index -= 1
            lotFlag = csvDict[str(index)]["getItemFlagId"]
    # step forward through the connected lots until we find a free space
    while str(index) in csvDict:
        # if it's a shop lot and there's a visibility flag, save it
        if "eventFlag_forRelease" in csvDict[str(index)] and \
                csvDict[str(index)]["eventFlag_forRelease"] != 0:
            lotFlag = csvDict[str(index)]["eventFlag_forRelease"]
        index += 1
    firstID = index
    # step through spaces until we hit another lot or get ten free spaces
    # upping this to 20 to allow for bigger lot ranges
    while str(index) not in csvDict and index < firstID + 21:
        index += 1
    # we want to make sure we don't use the space just before the next lot so
    # that we don't connect lots together and get erroneous pickups
    lastID = index - 2
    if lastID < firstID:
        return None
    returnDict = {
        "freeLotID": str(firstID),
        "freeLotLength": str(lastID - firstID + 1),
    }
    if lotFlag:
        returnDict["lotFlag"] = lotFlag
    return returnDict
