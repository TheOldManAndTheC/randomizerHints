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

from copy import deepcopy
from xml.sax.saxutils import escape
from source.model.hint.hintComponents import hintComponents
from source.model.hint.hintText import hintText
from source.model.params.freeRange import freeRange
from source.data.model.paramData.equipParamGoodsTemplate \
    import equipParamGoodsTemplate
from source.data.model.paramData.itemLotParam_mapTemplate \
    import itemLotParam_mapTemplate
from source.data.model.paramData.shopLineupParamTemplate \
    import shopLineupParamTemplate

xmlEntry = "<text id=\"{}\">{}</text>\n"
shopText = "Further details are available only to paying customers."


# Take the list of all generated hints and create the hint items that contain
# them and create their new CSV and XML entries
def scriptHints(allHintEntries, xmlFiles, params, itemInfo, localeData,
                useFogAreas, useAllDirections):
    if "newItemLotParam_map" in params:
        newItemLotParam_map = params["newItemLotParam_map"]
    else:
        newItemLotParam_map = dict()
    if "newEquipParamGoods" in params:
        newEquipParamGoods = params["newEquipParamGoods"]
    else:
        newEquipParamGoods = dict()
    if "newShopLineupParam" in params:
        newShopLineupParam = params["newShopLineupParam"]
    else:
        newShopLineupParam = dict()
    # sort IDs that will keep all the hint items in their own categories at the
    # top of the info item inventory page
    if "freeSortID" in params:
        freeSortID = params["freeSortID"]
    else:
        freeSortID = 452000
    if "fogFreeSortID" in params:
        fogFreeSortID = params["fogFreeSortID"]
    else:
        fogFreeSortID = 456000
    if "hintItemID" in params:
        hintItemID = params["hintItemID"]
    else:
        hintItemID = 300000
    # Process all the hint entries
    for hintEntryDict in allHintEntries:
        shopValue = None
        csvDict = params["ItemLotParam_map"]
        # if it's a shop lot, use the ShopLineupParams
        if "shopValue" in hintEntryDict:
            shopValue = hintEntryDict["shopValue"]
            csvDict = params["ShopLineupParam"]
        hintRange = freeRange(hintEntryDict["lotID"], csvDict)
        # if there's no room in this lot, we can't place a hint, skip
        if not hintRange:
            continue
        hintLotID = hintRange["freeLotID"]
        if "lotFlag" in hintRange:
            hintLotFlag = hintRange["lotFlag"]
        else:
            hintLotFlag = None

        components = hintComponents(hintEntryDict, itemInfo, useFogAreas,
                                    useAllDirections)
        for language in localeData:
            if language not in xmlFiles:
                continue
            hint = hintText(components, localeData, language)
            # add the note to the XML files in item.msgbnd, use XML character
            # escapes
            xmlFiles[language]["nameXML"].insert(
                -2,
                xmlEntry.format(hintItemID, escape(hint["name"]))
            )
            xmlFiles[language]["infoXML"].insert(
                -2,
                xmlEntry.format(hintItemID, escape(hint["description"]))
            )
            xmlFiles[language]["captionXML"].insert(
                -2,
                xmlEntry.format(hintItemID, escape(hint["text"]))
            )
            # if it's a shop item, we also need to create the shop inventory
            # object
            if shopValue is not None:
                # add the note to the XML files in item.msgbnd, use XML
                # character escapes
                xmlFiles[language]["nameXML"].insert(
                    -2,
                    xmlEntry.format(hintItemID + 1, escape(hint["name"]))
                )
                xmlFiles[language]["infoXML"].insert(
                    -2,
                    xmlEntry.format(hintItemID + 1, escape(hint["description"]))
                )
                # only hide the contents if it isn't free of charge
                if shopValue == "0":
                    xmlFiles[language]["captionXML"].insert(
                        -2,
                        xmlEntry.format(hintItemID + 1, escape(hint["text"]))
                    )
                else:
                    xmlFiles[language]["captionXML"].insert(
                        -2,
                        xmlEntry.format(hintItemID + 1,
                                        escape(localeData[language][shopText]))
                    )
        # create an entry in EquipParamGoods for the note
        newHint = deepcopy(equipParamGoodsTemplate)
        newHint["ID"] = hintItemID
        newHint["iconId"] = components["iconID"]
        newHint["Name"] = components["label"]
        if components["isItem"]:
            newHint["sortId"] = freeSortID
        else:
            newHint["sortId"] = fogFreeSortID
            # put fog hints in a separate group above item hints
            newHint["sortGroupId"] = "3"
        newEquipParamGoods[newHint["ID"]] = newHint
        # if it's a shop item, we also need to create the shop inventory object
        if shopValue is not None:
            # create an entry in EquipParamGoods for the shop inventory version
            newHint = deepcopy(equipParamGoodsTemplate)
            newHint["ID"] = hintItemID + 1
            newHint["iconId"] = components["iconID"]
            newHint["sortId"] = "999999"
            newHint["goodsType"] = "0"
            newHint["sortGroupId"] = "255"
            newHint["rarity"] = "0"
            newHint["Name"] = components["label"]
            newEquipParamGoods[newHint["ID"]] = newHint
            # add an entry for the note to the new lot in the new
            # ShopLineupParam
            newLot = deepcopy(shopLineupParamTemplate)
            newLot["ID"] = hintLotID
            newLot["equipId"] = hintItemID
            newLot["value"] = shopValue
            if hintLotFlag:
                newLot["eventFlag_forRelease"] = hintLotFlag
            # set the ID of the shop inventory version
            newLot["nameMsgId"] = hintItemID + 1
            newLot["Name"] = components["label"]
            newShopLineupParam[hintLotID] = newLot
            # Also add it to the existing ShopLineupParam to make sure that
            # hints don't overwrite each other
            params["ShopLineupParam"][hintLotID] = newLot
            # extra increment for the shop inventory version
            hintItemID += 1
        else:
            # add an entry for the note to the new lot in the new
            # ItemLotParam_map
            newLot = deepcopy(itemLotParam_mapTemplate)
            newLot["ID"] = hintLotID
            newLot["lotItemId01"] = hintItemID
            if hintLotFlag:
                newLot["getItemFlagId"] = hintLotFlag
            newLot["Name"] = components["label"]
            newItemLotParam_map[hintLotID] = newLot
            # Also add it to the existing ItemLotParam_map to make sure that
            # hints don't overwrite each other
            params["ItemLotParam_map"][hintLotID] = newLot
        hintItemID += 1
        if components["isItem"]:
            freeSortID += 1
        else:
            fogFreeSortID += 1
    params["newItemLotParam_map"] = newItemLotParam_map
    params["newEquipParamGoods"] = newEquipParamGoods
    params["newShopLineupParam"] = newShopLineupParam
    params["hintItemID"] = hintItemID
    params["freeSortID"] = freeSortID
    params["fogFreeSortID"] = fogFreeSortID
