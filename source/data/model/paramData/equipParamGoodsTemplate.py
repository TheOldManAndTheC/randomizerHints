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
equipParamGoodsTemplate = {
    "ID": "0",  # set to Row ID of the item
    "Name": "HINT NOTE",  # set to name used in yapped
    "disableParam_NT": "1",
    "disableParamReserve1": "0",
    "disableParamReserve2": "[0|0|0]",
    "refId_default": "-1",
    "sfxVariationId": "-1",
    "weight": "0",
    "basicPrice": "0",
    "sellValue": "-1",
    "behaviorId": "0",
    "replaceItemId": "-1",
    "sortId": "452000",  # increment from 452000, use 999999 for shop version
    "appearanceReplaceItemId": "-1",
    "yesNoDialogMessageId": "-1",
    "useEnableSpEffectType": "0",
    "potGroupId": "-1",
    "pad": "0",
    # All usable icons:
    # 261: Map: Limgrave, West
    # 262: Map: Weeping Peninsula
    # 263: Map: Limgrave, East
    # 264: Map: Liurnia, West
    # 265: Map: Liurnia, North
    # 266: Map: Liurnia, East
    # 267: Map: Mt. Gelmir
    # 268: Map: Altus Plateau
    # 269: Map: Leyndell, Royal Capital
    # 270: Map: Dragonbarrow
    # 271: Map: Caelid
    # 272: Map: Consecrated Snowfield
    # 273: Map: Mountaintops of the Giants, West
    # 274: Map: Lake of Rot
    # 275: Map: Ainsel River
    # 276: Map: Siofra River
    # 277: Map: Mohgwyn Palace
    # 278: Map: Deeproot Depths
    # 279: Map: Mountaintops of the Giants, East

    # 288: Note - cyan and black feather
    # 289: Note - white feather
    # 290: Note - black feather
    # 291: Note - grey and white feather
    # 292: Note - red and yellow feather
    # 293: Note - blue feather
    # 294: Note - yellow feather
    # 295: Note - red feather
    # 296: Note - green feather
    # 297: Note - purple feather
    # 298: Note - red, black, yellow, green feathers
    # 299: Book - tear on cover tied with string and blue feathers
    # 300: Book - very tattered, tied with blue string with a branch and a fang
    # attached
    # 301: Book - red cover with brass fittings, cameo locket necklace, lots
    # of rips on cover and loose pages
    # 302: Book - cloth book tied with cloth, tattered, knotted strings holding
    # yellowish stones hanging from binding
    # 303: Book - wood cover wrapped in very tattered blue cloth, tied with
    # string holding glowing light blue stones hanging from binding
    # 304: Book - blue cover with shield design, tied with red and blue twine
    # with metal medallions strung on it, loose pages
    # 305: Book - torn grey cover, loose pages, tied with strings of beads
    # with Pattering Pate lookin things strung on it
    # 306: Book - ornate cover with a plant design, loose pages, tied with
    # brocade rope and small pouches tied to it
    # 307: Book - patchwork cover of different types of cloth roughly stitched
    # together, loose page, tied with patchwork string and small orange beads
    # 308: Book - dark green cover with brass fittings and elaborate design,
    # loose pages, tied with brocade string with a golden amulet with a red
    # stone threaded on it and a long quill tucked in
    # 309: Book - ornate cover with lots of gemstones and a string of beads
    # with very loose pages
    # 310: Scroll - Conspectus/Academy Scroll
    # 311: Scroll - Royal House Scroll
    # 312: Scroll - pale blue with frost coming off it
    # 313: Scroll - dark blue with mist coming off it
    # 314: Scroll - red with snake head biting page and flames coming off it
    # 315: Book - Fire Monks' Prayerbook
    # 316: Book - Giant's Prayerbook
    # 317: Book - Godskin Prayerbook
    # 318: Book - Two Fingers' Prayerbook
    # 319: Book - Assassin's Prayerbook
    # 320: Book - Erdtree Prayerbook - gold book with embossed Erdtree Seal
    # 321: Book - Erdtree Codex - Book with central circular design, some
    # flames, glowing
    # 322: Book - Golden Order Principia
    # 323: Book - Golden Order Principles - gold book with embossed Golden
    # Order Seal
    # 324: Book - Dragon Cult Prayerbook
    # 325: Book - Ancient Dragon Prayerbook

    # 3055: Note - Letter from Volcano Manor
    # 3059: Note - Irina's Letter
    # 3061: Note - Red Letter
    # 3071: Scroll - Seluvis's Introduction
    # 3084: Map - Mirage Riddle (anywhere)
    # 3089: Scroll - frayed, rolled up and tied with string and cyan and white
    # feathers
    # 3091: Scroll - pale blue with frost coming off it (less mist than 312)
    # 3101: Note - Same as Letter from Volcano Manor but opened
    # 3107: Note - Same as Letter from Volcano Manor but opened (copy, don't
    # use)

    # 3119: Book - Nomadic Warrior's Cookbook
    # 3120: Book - Armorer's Cookbook
    # 3121: Book - Glintstone Craftsman's Cookbook
    # 3122: Book - Missionary's Cookbook
    # 3123: Book - Perfumer's Cookbook
    # 3124: Book - Ancient Dragon Apostle's Cookbook
    # 3125: Book - Fevor's Cookbook
    # 3126: Book - Frenzied's Cookbook

    # 3226: Scroll - Iji's Confession
    # 3234: Note - Sellia's Secret
    # 3277: Map - Meeting Place Map (great lake)
    # 3280: Map - Knifeprint Clue (anywhere)
    # 3281: Note - Rogier's/Zorayas's Letter
    # 3286: Map - Weathered Map (anywhere)
    # 3287: Scroll - frayed, rolled up and tied with string

    # 81 usable icons
    # 58 without map icons
    # 30 books
    # 23 maps
    # 18 notes
    # 10 scrolls
    "iconId": "288",  # note icons: 288-292, 294, 298. use 0 for shop version
    "modelId": "0",
    "shopLv": "-1",
    "compTrophySedId": "-1",
    "trophySeqId": "-1",
    "maxNum": "1",
    "consumeHeroPoint": "0",
    "overDexterity": "50",
    "goodsType": "12",  # 12 - Info Item for hint, 0 - Normal Item for shop ver
    "refCategory": "0",
    "spEffectCategory": "0",
    "pad3": "0",
    "goodsUseAnim": "0",
    "opmeMenuType": "0",
    "useLimitCategory": "0",
    "replaceCategory": "0",
    "reserve4": "[0|0]",
    "enable_live": "0",
    "enable_gray": "0",
    "enable_white": "0",
    "enable_black": "0",
    "enable_multi": "0",
    "disable_offline": "0",
    "isEquip": "0",
    "isConsume": "0",
    "isAutoEquip": "0",
    "isEstablishment": "0",
    "isOnlyOne": "0",
    "isDiscard": "1",  # allow hints to be discarded
    "isDeposit": "1",  # allow hints to be stored in chest
    "isDisableHand": "0",
    "isRemoveItem_forGameClear": "1",  # remove in NG+
    "isSuppleItem": "0",
    "isFullSuppleItem": "0",
    "isEnhance": "0",
    "isFixItem": "0",
    "disableMultiDropShare": "0",
    "disableUseAtColiseum": "0",
    "disableUseAtOutOfColiseum": "0",
    "isEnableFastUseItem": "0",
    "isApplySpecialEffect": "0",
    "syncNumVaryId": "0",
    "refId_1": "-1",
    "refVirtualWepId": "-1",
    "vagrantItemLotId": "-1",
    "vagrantBonusEneDropItemLotId": "-1",
    "vagrantItemEneDropItemLotId": "-1",
    "castSfxId": "-1",
    "fireSfxId": "-1",
    "effectSfxId": "-1",
    "enable_ActiveBigRune": "1",
    "isBonfireWarpItem": "0",
    "enable_Ladder": "0",
    "isUseMultiPlayPreparation": "0",
    "canMultiUse": "0",
    "isShieldEnchant": "0",
    "isWarpProhibited": "0",
    "isUseMultiPenaltyOnly": "0",
    "suppleType": "0",
    "autoReplenishType": "0",
    "isDrop": "1",  # allow hints to be dropped
    "showLogCondType": "1",
    "isSummonHorse": "0",
    "showDialogCondType": "2",
    "isSleepCollectionItem": "0",
    "enableRiding": "1",
    "disableRiding": "0",
    "maxRepositoryNum": "1",
    "sortGroupId": "5",  # 5 for our hints, 10 for info, 255 for shop version
    "isUseNoAttackRegion": "1",
    "pad1": "0",
    "saleValue": "0",
    "rarity": "2",  # 2 - Rare for hint, 0 - Default for shop version
    "useLimitSummonBuddy": "0",
    "useLimitSpEffectType": "0",
    "aiUseJudgeId": "-1",
    "consumeMP": "0",
    "consumeHP": "-1",
    "reinforceGoodsId": "-1",
    "reinforceMaterialId": "-1",
    "reinforcePrice": "0",
    "useLevel_vowType0": "0",
    "useLevel_vowType1": "0",
    "useLevel_vowType2": "0",
    "useLevel_vowType3": "0",
    "useLevel_vowType4": "0",
    "useLevel_vowType5": "0",
    "useLevel_vowType6": "0",
    "useLevel_vowType7": "0",
    "useLevel_vowType8": "0",
    "useLevel_vowType9": "0",
    "useLevel_vowType10": "0",
    "useLevel_vowType11": "0",
    "useLevel_vowType12": "0",
    "useLevel_vowType13": "0",
    "useLevel_vowType14": "0",
    "useLevel_vowType15": "0",
    "useLevel": "0",
    "reserve5": "[0|0]",
    "itemGetTutorialFlagId": "0",
    "reserve3": "[0|0|0|0|0|0|0|0]",
}
