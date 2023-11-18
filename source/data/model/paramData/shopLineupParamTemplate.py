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

# generic template for the ShopLineupParam entries.  make a deep copy of this
# when creating a new entry with deepcopy()
shopLineupParamTemplate = {
    "ID": "0",  # set to Row ID of the shop lot
    "Name": "",  # set to name used in yapped
    "equipId": "0",  # set to the EquipParamGoods ID of the hint object
    "value": "0",  # set to shop price
    "mtrlId": "-1",
    # keep at 0 for infinite stock, using an existing flag will make other items
    # using that flag get used up
    "eventFlag_forStock": "0",
    # flag to determine when object is available in shop, set this according to
    # what comes back from freeRange
    "eventFlag_forRelease": "0",
    # we want a quantity of 1, but it gets overridden by not having an
    # eventFlag_forStock
    "sellQuantity": "1",
    "pad3": "0",
    # 0 - Weapon
    # 1 - Protector
    # 2 - Accessory
    # 3 - Good
    # 4 - Ashes
    "equipType": "3",  # EquipParamGoods is 3
    "costType": "0",  # 0 for runes as currency
    "pad1": "0",
    "setNum": "1",  # number allowed to purchase at once
    "value_Add": "0",
    "value_Magnification": "1",
    "iconId": "-1",
    "nameMsgId": "-1",  # set to EquipParamGoodsID of the shop only hint object
    "menuTitleMsgId": "-1",
    "menuIconId": "-1",
    "pad2": "[0|0]",
}
