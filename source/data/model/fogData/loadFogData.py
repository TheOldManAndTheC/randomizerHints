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

fogSubKeys = {
    "- Name: ": {
        "indent": 2,
        "validKeys": []
    },
    "- Area: ": {
        "indent": 2,
        "validKeys": []
    },
    "To:": {
        "indent": 0,
        "key": "to",
        "validKeys": ["- Area: "]
    },
    "ASide:": {
        "indent": 2,
        "key": "aSide",
        "validKeys": []
    },
    "BSide:": {
        "indent": 2,
        "key": "bSide",
        "validKeys": []
    },
    "DebugInfos:": {
        "indent": 0,
        "key": "debugInfos",
        "isList": True,
        "validKeys": []
    },
    "Areas:": {
        "indent": 0,
        "key": "areas",
        "isRoot": True,
        "validKeys": []
    },
    "Warps:": {
        "indent": 0,
        "key": "warps",
        "isRoot": True,
        "validKeys": []
    },
    "Entrances:": {
        "indent": 0,
        "key": "entrances",
        "isRoot": True,
        "validKeys": []
    },
    "ConfigVars:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True,
    },
    "KeyItems:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True,
    },
    "RetryPoints:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True,
    },
    "OpenBonfires:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True
    },
    "DungeonItems:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True
    },
    "CustomBonfires:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True
    },
    "CustomBarriers:": {
        "indent": 0,
        "isRoot": True,
        "ignore": True
    }
}

fogBasicLines = {
    "Text: ": "text",
    "Maps: ": "maps",
    "DebugInfo: ": "debugInfo",
    "DefeatFlag: ": "defeatFlag",
    "BossTrigger: ": "bossTrigger",
    "TrapFlag: ": "trapFlag",
    "Tags: ": "tags",
    "Comment: ": "comment",
    "ID: ": "id",
    "Area: ": "area",
    "Silo: ": "silo",
    "Cond: ": "cond",
    "DestinationMap: ": "destinationMap",
    "WarpBonfire: ": "warpBonfire",
    "WarpBonfireFlag: ": "warpBonfireFlag",
    "AdjustHeight: ": "adjustHeight",
    "BossDefeatName: ": "bossDefeatName",
    "BossTriggerName: ": "bossTriggerName",
    "MainMaps: ": "mainMaps",
    "OpenArea: ": "openArea",
    "StakeRadius: ": "stakeRadius",
    "FullArea: ": "fullArea",
    "DoorName: ": "doorName",
    "BossTrapName: ": "bossTrapName",
    "AlternateOf: ": "alternateOf",
    "SplitFrom: ": "splitFrom",
    "MakeFrom: ": "makeFrom",
    "Strafe: ": "strafe",
    "StakeAsset: ": "stakeAsset",
    "DoorCond: ": "doorCond",
    "BossTriggerArea: ": "bossTriggerArea",
    "Raise: ": "raise",
    "TrimRegion: ": "trimRegion",
    "StakeRegions: ": "stakeRegions",
    "BeforeWarpFlag: ": "beforeWarpFlag",
    "AltBossTriggerArea: ": "altBossTriggerArea",
    "ReturnWarp: ": "returnWarp",
    "PairWith: ": "pairWith",
    "StakeAssetDepth: ": "stakeAssetDepth",
    "RemoveDest: ": "removeDest",
    "SpecialText: ": "specialText",
    "StakeRespawn: ": "stakeRespawn",
}
