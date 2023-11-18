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

# generic template for the ItemLotParam_map entries.  make a deep copy of this
# when creating a new entry with deepcopy()
itemLotParam_mapTemplate = {
    "ID": "0",  # set to Row ID of the lot
    "Name": "",  # set to name used in yapped
    "lotItemId01": "0",  # set to EquipParam* ID of item
    "lotItemId02": "0",
    "lotItemId03": "0",
    "lotItemId04": "0",
    "lotItemId05": "0",
    "lotItemId06": "0",
    "lotItemId07": "0",
    "lotItemId08": "0",
    # set lotItemCategory01 to type of item:
    # 0 - None
    # 1 - Good
    # 2 - Weapon
    # 3 - Protector
    # 4 - Accessory
    # 5 - Ashes
    "lotItemCategory01": "1",  # 1 because all our notes are Goods
    "lotItemCategory02": "0",
    "lotItemCategory03": "0",
    "lotItemCategory04": "0",
    "lotItemCategory05": "0",
    "lotItemCategory06": "0",
    "lotItemCategory07": "0",
    "lotItemCategory08": "0",
    "lotItemBasePoint01": "1000",
    "lotItemBasePoint02": "0",
    "lotItemBasePoint03": "0",
    "lotItemBasePoint04": "0",
    "lotItemBasePoint05": "0",
    "lotItemBasePoint06": "0",
    "lotItemBasePoint07": "0",
    "lotItemBasePoint08": "0",
    "cumulateLotPoint01": "0",
    "cumulateLotPoint02": "0",
    "cumulateLotPoint03": "0",
    "cumulateLotPoint04": "0",
    "cumulateLotPoint05": "0",
    "cumulateLotPoint06": "0",
    "cumulateLotPoint07": "0",
    "cumulateLotPoint08": "0",
    "getItemFlagId01": "0",
    "getItemFlagId02": "0",
    "getItemFlagId03": "0",
    "getItemFlagId04": "0",
    "getItemFlagId05": "0",
    "getItemFlagId06": "0",
    "getItemFlagId07": "0",
    "getItemFlagId08": "0",
    "getItemFlagId": "0",  # set this to the same flag as the base lot
    "cumulateNumFlagId": "0",
    "cumulateNumMax": "0",
    "lotItem_Rarity": "-1",
    "lotItemNum01": "1",  # set this to the desired quantity of the item
    "lotItemNum02": "0",
    "lotItemNum03": "0",
    "lotItemNum04": "0",
    "lotItemNum05": "0",
    "lotItemNum06": "0",
    "lotItemNum07": "0",
    "lotItemNum08": "0",
    "enableLuck01": "0",
    "enableLuck02": "0",
    "enableLuck03": "0",
    "enableLuck04": "0",
    "enableLuck05": "0",
    "enableLuck06": "0",
    "enableLuck07": "0",
    "enableLuck08": "0",
    "cumulateReset01": "0",
    "cumulateReset02": "0",
    "cumulateReset03": "0",
    "cumulateReset04": "0",
    "cumulateReset05": "0",
    "cumulateReset06": "0",
    "cumulateReset07": "0",
    "cumulateReset08": "0",
    "GameClearOffset": "0",
    "canExecByFriendlyGhost": "0",
    "canExecByHostileGhost": "0",
    "PAD1": "0",
    "PAD2": "0"
}
