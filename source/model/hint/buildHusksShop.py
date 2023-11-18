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


def addMasseditEntry(massedit, param, paramID, field, value):
    entry = {
        "param": param,
        "id": paramID,
        "field": field,
        "value": value
    }
    massedit.append(entry)


def buildHusksShop(params, newShop):
    count = 0
    massedit = params["massedit"]
    for lotID in newShop:
        changed = False
        newShopEntry = newShop[lotID]
        newEquipId = newShopEntry["equipId"]
        newValue = int(newShopEntry["value"])
        match newShopEntry["equipType"]:
            case "0":
                param = "EquipParamWeapon"
            case "1":
                param = "EquipParamProtector"
            case "2":
                param = "EquipParamAccessory"
            case "3":
                param = "EquipParamGoods"
            case _:
                param = "EquipParamGem"
        sellValue = int(params[param][newEquipId]["sellValue"])

        shopEntry = params["ShopLineupParam"][lotID]
        if newEquipId != shopEntry["equipId"]:
            addMasseditEntry(massedit, "ShopLineupParam", lotID, "equipId",
                             newEquipId)
            addMasseditEntry(massedit, "ShopLineupParam", lotID, "equipType",
                             newShopEntry["equipType"])
            # addMasseditEntry(massedit, "ShopLineupParam", lotID,
            #                  "eventFlag_forStock", "0")
            addMasseditEntry(massedit, "ShopLineupParam", lotID,
                             "sellQuantity", "-1")
            changed = True
        if str(newValue) != shopEntry["value"]:
            addMasseditEntry(massedit, "ShopLineupParam", lotID, "value",
                             newShopEntry["value"])
            changed = True
        if sellValue > newValue:
            addMasseditEntry(massedit, param, newEquipId, "sellValue",
                             str(math.floor(newValue / 10)))
        if changed:
            count += 1
    return count
