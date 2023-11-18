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

# Parse the itemslots.txt file from the randomizer and build a usable data
# structure indexed by item name
from warnings import warn

from source.model.randomizer.directionUtils import parseDirections
from source.model.randomizer.directionUtils import scriptDirections
from source.data.model.randomizerData.loadItemSlotsData import books
from source.data.model.randomizerData.loadItemSlotsData import containerTypes
from source.data.model.randomizerData.loadItemSlotsData import duplicateMaps
from source.data.model.randomizerData.loadItemSlotsData import goods
from source.data.model.randomizerData.loadItemSlotsData \
    import itemSlotsBasicLines
from source.data.model.randomizerData.loadItemSlotsData \
    import itemSlotsSkipLines
from source.data.model.randomizerData.loadItemSlotsData import landmarkTypes
from source.data.model.randomizerData.loadItemSlotsData import lotAppends
from source.data.model.randomizerData.loadItemSlotsData import lotTypes
from source.data.model.randomizerData.loadItemSlotsData import otherBooks
from source.data.model.randomizerData.killQuests import killQuests


def loadItemSlots(itemSlotsLines):
    # Generate the itemSlots data structure from the randomizer's itemslots.txt
    # file
    itemSlots = dict()
    key = ""
    lineIter = iter(itemSlotsLines)
    while True:
        line = next(lineIter, None)
        if line is None:
            # when we get here with a key already set, we need to add
            # everything for the previous key entry
            if key != "":
                for itemEntry in itemList:
                    itemEntry.update(keyEntry)
                    item = itemEntry["item"]
                    if item not in itemSlots:
                        itemSlots[item] = [itemEntry]
                    else:
                        itemSlotList = itemSlots[item]
                        itemSlotList.append(itemEntry)
            break
        line = line[:-1]  # remove newline
        # unneeded lines that have a similar format to item lines
        skip = False
        for skipLine in itemSlotsSkipLines:
            if line.startswith(skipLine):
                skip = True
                break
        if skip:
            continue

        # handle basic info lines that don't require parsing
        skip = False
        for basicLineKey in itemSlotsBasicLines:
            if line.startswith(basicLineKey):
                keyEntry[itemSlotsBasicLines[basicLineKey]] = \
                    line[len(basicLineKey):]
                skip = True
                break
        if skip:
            continue

        # key line
        if line.startswith("- Key: '"):
            # when we get here with a key already set, we need to add
            # everything for the previous key entry
            if key != "":
                for itemEntry in itemList:
                    itemEntry.update(keyEntry)
                    item = itemEntry["item"]
                    if item not in itemSlots:
                        itemSlots[item] = [itemEntry]
                    else:
                        itemSlotList = itemSlots[item]
                        itemSlotList.append(itemEntry)
            key = line[8:-1]  # skip final '
            keyEntry = {
                "directionsList": [],
                "rawDirectionsList": [],
                "key": key
            }
            itemList = []
            continue

        if not key:
            continue

        # ignore lines without this format
        if not line.startswith("  - "):
            continue

        # trim line for further processing
        line = line[4:]  # remove left margin
        if line[0] == "'" or line[0] == "\"":  # remove quotes if there
            line = line[1:-1]

        # directions line
        if line.startswith("By "):
            # preserve the original line
            if line not in keyEntry["rawDirectionsList"]:
                keyEntry["rawDirectionsList"].append(line)
            # modify line to match the format in the spoilers file
            strings = parseDirections(line)
            # not doing a float cast here because of rounding issues
            angleComponents = strings["angle"].split(".")
            angle = int(angleComponents[0])
            fraction = int(angleComponents[1])
            # this doesn't seem to be properly reflected in spoilers, so a
            # jitter fix will be done in matchingSlot
            if fraction >= 50:
                angle += 1
            if angle == 0:
                angle = 12
            strings["angle"] = str(angle)
            if strings["type"] not in landmarkTypes:
                strings["type"] = "Site of Grace"
            directions = scriptDirections(strings)
            if directions not in keyEntry["directionsList"]:
                keyEntry["directionsList"].append(directions)
            continue

        # item line
        # some item lines have escaped quotes, remove them
        line = line.replace("\\\"", "\"")

        # Parse the line.  The format is:
        # <item name> - <item lot list>
        itemEntry = {
            "item": ""
        }

        # get item name
        index = line.find(" - ")
        itemEntry["item"] = line[:index]
        line = line[index + 3:]  # cut the separator string too

        # Parse list of lots.  The format is: (comma separated)
        # <lot type> <lot ID>[<container list>]
        # |<item name>|Good <good id>*|Equip <equip id>*|Weapon <weapon id>|
        # (Good <good id>)|, <quantity>x| for <price>
        lotList = []
        quantity = ""
        containerNamesList = []
        containerIDsList = []
        mapList = []
        regionsList = []
        while True:
            lotEntry = dict()
            # lot type
            found = False
            for lotType in lotTypes:
                if line.startswith(lotType):
                    lotEntry["type"] = lotType
                    line = line[len(lotType) + 1:]  # also skip space
                    found = True
                    break
            if not found:
                warn("Parse error, unknown lot type: " + line, SyntaxWarning)

            # lot ID
            index = line.find("[")
            lotEntry["lotID"] = line[:index]
            line = line[index:]

            # lot (container list)
            index = line.find("]")
            lot = line[1:index]
            line = line[index + 2:]  # also remove the space after the lot

            # Process the container list.  Format is: (comma separated)
            # <container type>| <container ref>| in <map ID> (<location>)|
            # (<container>) in <map ID> (<location>)|
            containerList = []
            while True:
                containerEntry = dict()
                found = False
                for containerType in containerTypes:
                    if lot.startswith(containerType):
                        containerEntry["type"] = containerType
                        lot = lot[len(containerType):]
                        found = True
                        break
                if not found:
                    warn("Parse error, unknown container type: " + lot,
                         SyntaxWarning)
                if not lot:
                    containerList.append(containerEntry)
                    break
                while lot[0] == " ":  # remove space
                    lot = lot[1:]

                # get the container ref, may end here
                index = 0
                while index < len(lot) and " ,]".find(lot[index]) == -1:
                    index += 1
                containerEntry["containerRef"] = lot[:index]
                lot = lot[index:]
                if not lot:
                    containerList.append(containerEntry)
                    break
                while lot[0] == " ":  # skip space
                    lot = lot[1:]

                # has a container name
                if lot[0] == "(":
                    index = lot.find(")")
                    # some enemies have parentheses in their names
                    if index < len(lot) - 1 and lot[index + 1] == ">" and \
                            lot[index + 2] == ")":
                        index += 2
                    containerEntry["container"] = lot[1:index]  # skip (
                    lot = lot[index + 1:]  # skip )
                # if there's no container name but the type is Melina
                elif containerEntry["type"] == "Melina":
                    containerEntry["container"] = containerEntry["type"]
                while lot[0] == " ":  # skip space
                    lot = lot[1:]

                # there may be a container ID
                if "container" in containerEntry:
                    if containerEntry["container"].find(" - id ") != -1:
                        splitLine = \
                            containerEntry["container"].split(" - id ", 1)
                        containerEntry["containerName"] = splitLine[0]
                        containerEntry["containerID"] = \
                            splitLine[1].split(" - ", 1)[0]
                        if containerEntry["containerID"] \
                                not in containerIDsList:
                            containerIDsList.append(
                                containerEntry["containerID"])
                        # <> contains a more complete name
                        if splitLine[1].find("<") != -1:
                            containerEntry["rawContainerName"] = \
                                containerEntry["containerName"]
                            containerEntry["containerName"] = \
                                splitLine[1].split("<")[1].split(">")[0]
                    # or there may be just a group ID, don't need it
                    elif containerEntry["container"].find(" - group ") \
                            != -1:
                        splitLine = \
                            containerEntry["container"].split(" - group ",
                                                              1)
                        containerEntry["containerName"] = splitLine[0]
                    else:  # just the name
                        containerEntry["containerName"] = \
                            containerEntry["container"]
                    if containerEntry["containerName"] \
                            not in containerNamesList:
                        containerNamesList.append(
                            containerEntry["containerName"])

                # map ID and location
                if lot.startswith("in "):
                    lot = lot[3:]
                    if lot.startswith("common"):
                        containerEntry["mapID"] = "common"
                        lot = lot[6:]
                    elif lot[0] == "m":
                        index = 12  # length of a map ID
                        containerEntry["mapID"] = lot[:index]
                        if containerEntry["mapID"] not in mapList:
                            mapList.append(containerEntry["mapID"])

                        lot = lot[index:]
                        if not lot:
                            containerList.append(containerEntry)
                            break
                        while lot[0] == " ":  # skip space
                            lot = lot[1:]
                        if lot[0] == "(":
                            index = lot.find(")")
                            if index < len(lot) - 1 and \
                                    lot[index + 1] == ")":
                                index += 1
                            containerEntry["region"] = lot[1:index]
                            if containerEntry["region"] not in regionsList:
                                regionsList.append(containerEntry["region"])
                            lot = lot[index + 1:]  # skip )
                        else:
                            warn("Parse error, unknown location format: " + lot,
                                 SyntaxWarning)
                    else:
                        warn("Parse error, unknown map ID format: " + lot,
                             SyntaxWarning)
                    if not lot:
                        containerList.append(containerEntry)
                        break
                elif lot[0] == ",":  # end of lot
                    pass
                else:
                    warn("Parse error, unknown container format: " + lot,
                         SyntaxWarning)
                if not lot:
                    containerList.append(containerEntry)
                    break
                if lot.startswith(", "):
                    lot = lot[2:]
                    containerList.append(containerEntry)
                else:
                    warn("Parse error, bad end of lot: " + lot, SyntaxWarning)
            lotEntry["containers"] = containerList

            # resume parsing line after container list
            # if the item name appears again, skip it
            if line.startswith(itemEntry["item"]):
                line = line.replace(itemEntry["item"], "", 1)
            if not line:
                lotList.append(lotEntry)
                break

            # possible appends
            for lotAppendKey in lotAppends:
                lotAppend = lotAppends[lotAppendKey]
                if line.startswith(lotAppendKey):
                    if "delimiter" in lotAppend:
                        index = line.find(lotAppend["delimiter"])
                        lotEntry[lotAppend["key"]] = \
                            line[len(lotAppendKey):index]
                        line = line[index + 1:]
                    else:  # no delimiter character
                        index = len(lotAppendKey)
                        while index < len(line) and line[index].isdigit():
                            index += 1
                        lotEntry[lotAppend["key"]] = \
                            line[len(lotAppendKey):index]
                        line = line[index:]
                    break
            if not line:
                lotList.append(lotEntry)
                break

            # check for quantity
            if line[0] == "," and line[2].isdigit():  # might be after a ','
                line = line[2:]
            if line[0].isdigit():  # it's a quantity
                index = line.find("x") + 1
                lotEntry["quantity"] = line[:index]
                # keep the final quantity for adding to the item name
                quantity = lotEntry["quantity"]
                line = line[index:]
            if not line:
                lotList.append(lotEntry)
                break
            if line[0] == " ":  # remove space if there
                line = line[1:]

            # price or recipe, may have ,'s
            if line.startswith("for "):
                line = line[4:]
                index = 0
                while index < len(line):
                    index = line.find(",", index)
                    if index == -1:
                        index = len(line)
                        conditions = line
                        break
                    if line[index:].startswith(", lot ") or \
                            line[index:].startswith(", shop") or \
                            line.startswith(", enemy lot "):
                        conditions = line[:index]
                        break
                    index += 1
                line = line[index:]
                splitLine = conditions.split(" - ")
                for clause in splitLine:
                    if clause == splitLine[0]:
                        lotEntry["price"] = clause
                    elif clause.startswith("qwc"):
                        lotEntry["qwc"] = clause
                    elif clause.startswith("flag"):
                        lotEntry["flag"] = clause
                    else:
                        lotEntry["condition"] = clause
                if "condition" in lotEntry:
                    if lotEntry["condition"].startswith("after giving "):
                        book = lotEntry["condition"][13:]
                        # spelling error in the file
                        if book == "Fire Monk's Prayerbook":
                            book = "Fire Monks' Prayerbook"
                        if book in books:
                            if "book" in itemEntry and \
                                    book != itemEntry["book"]:
                                warn("Parse error, multiple books for entry: "
                                     + str(itemEntry), SyntaxWarning)
                            itemEntry["book"] = book
                    if lotEntry["condition"].startswith("after defeating"):
                        killQuestKey = lotEntry["condition"][16:]
                        if killQuestKey in killQuests:
                            itemEntry["killQuest"] = \
                                killQuests[killQuestKey]

                if not line:
                    lotList.append(lotEntry)
                    break

            # validity check for next lot in list
            if line.startswith(", lot ") or line.startswith(", shop") or \
                    line.startswith(", enemy lot "):
                lotList.append(lotEntry)
                line = line[2:]
                continue
            warn("Parse error, unknown lot format: " + line, SyntaxWarning)

        itemEntry["containerNames"] = containerNamesList
        itemEntry["containerIDs"] = containerIDsList
        itemEntry["regions"] = regionsList
        # fixes
        # name correction based on good ID
        for lotEntry in lotList:
            if "good" in lotEntry and lotEntry["good"] in goods:
                itemEntry["item"] = goods[lotEntry["good"]]
                break
        # remove irrelevant maps
        # if the roundtable hold map isn't the only one it's a shop
        if len(mapList) > 1 and "m11_10_00_00" in mapList:
            mapList.remove("m11_10_00_00")
        if len(mapList) == 2:
            # check for duplicates from the known list
            for duplicateList in duplicateMaps:
                if mapList[0] in duplicateList and \
                        mapList[1] in duplicateList:
                    mapList = [duplicateList[1]]
                    break
        itemEntry["mapList"] = mapList
        # treat items in paintings and remembrances as if they were in books
        if itemEntry["item"] in otherBooks:
            itemEntry["book"] = otherBooks[itemEntry["item"]]

        if quantity and quantity != "1x":
            itemEntry["item"] = itemEntry["item"] + " " + quantity
        itemEntry["lotList"] = lotList

        # for the purposes of lot categorization later, store a flag for
        # shops and the item's lot ID for easier access
        if lotList[0]["type"] == "shop":
            itemEntry["isShop"] = True
        # the first lot entry is fine, any differences in subsequent
        # entries are typically after an NPC has died or left and their
        # items appear in shops.
        itemEntry["lotID"] = itemEntry["lotList"][0]["lotID"]

        itemList.append(itemEntry)

    return itemSlots
