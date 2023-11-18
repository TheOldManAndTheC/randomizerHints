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

directionFixes = [
    {
        "conditions": {
            "replaces": "Golden Rune [6]",
            "region": "Siofra River",
            "container": "Robed Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Hallowhorn Grounds (Underground Ruins) - 35.82 "
                          "away in 10 o'clock direction, -20.01 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Golden Rune [9]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near West Capital Rampart (Site of Grace) - 13.65 "
                          "away in 11 o'clock direction, -7.20 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Golden Rune [10]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near East Capital Rampart (Site of Grace) - 75.49 "
                          "away in 6 o'clock direction, -11.57 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Golden Rune [11]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near West Capital Rampart (Site of Grace) - 21.00 "
                          "away in 11 o'clock direction, -0.03 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Nascent Butterfly 3x",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near East Capital Rampart (Site of Grace) - 120.27 "
                          "away in 4 o'clock direction, -35.58 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Smithing Stone [4]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near East Capital Rampart (Site of Grace) - 74.78 "
                          "away in 6 o'clock direction, -19.73 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Smithing Stone [5]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Royal Colosseum (Marker) - 116.39 away in 4 "
                          "o'clock direction, 1.47 height offset"
            # "directions": "Near Erdtree Sanctuary (Site of Grace) - 153.20 "
            #                "away in 8 o'clock direction, -1.09 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Somber Smithing Stone [6]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near East Capital Rampart (Site of Grace) - 89.71 "
                          "away in 3 o'clock direction, -44.41 height offset"
        }
    },
    {
        "conditions": {
            "replaces": "Rune Arc",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Leyndell, Royal Capital (Marker) - 54.67 away "
                          "in 10 o'clock direction, -10.98 height offset"
        }
    },
    {
        # has directions from both Underground Roadside and Leyndell Catacombs
        # sites of grace, and two container types, use the Underground Roadside
        # directions as they are closer
        "conditions": {
            "replaces": "Golden Rune [11]",
            "region": "Subterranean Shunning-Grounds",
            "container": "Corpse, Shiny Item",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Underground Roadside (Site of Grace) - 36.24 "
                          "away in 3 o'clock direction, -0.36 height offset",
            "container": "Shiny Item"
        }
    },
    {
        # Seedbed Curse is inside the manor but then is outside after the ash
        # falls, use the inside location
        "conditions": {
            "replaces": "Seedbed Curse",
            "region": "Leyndell, Royal Capital",
            "container": "Robed Corpse, Shiny Item",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Fortified Manor, First Floor (Site of Grace) - "
                          "46.62 away in 3 o'clock direction, 10.49 height "
                          "offset",
            "container": "Robed Corpse"
        }
    },
    {
        # the Whetstone Knife can be obtained from the Twin Maiden Husks after
        # getting two great runes, but its initial location is in Gatefront
        # Ruins
        "conditions": {
            "replaces": "Whetstone Knife",
            "region": "Limgrave",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Gatefront Ruins (Ruins) - 26.44 away in 6 "
                          "o'clock direction, -9.24 height offset"
        }
    },
    {
        # Lansseax appears near Erdtree-Gazing Hill but his main location is
        # near Rampartside Path
        "conditions": {
            "replaces": "Lansseax's Glaive",
            "region": "Altus Plateau",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Rampartside Path (Site of Grace) - 117.07 away "
                          "in 7 o'clock direction, 19.78 height offset"
        }
    },
    {
        # the Golden Seed in Mohgwyn Palace, the Dynasty Mausoleum Midpoint
        # directions are way off
        "conditions": {
            "replaces": "Golden Seed",
            "region": "Mohgwyn",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Palace Approach Ledge-Road (Site of Grace) - "
                          "99.59 away in 10 o'clock direction, -15.74 height "
                          "offset"
        }
    },
    {
        # these are the doubled up Golden Seeds in Capital Outskirts, since each
        # pair is so close together just one of the directions will do for both
        "conditions": {
            "text": "Under the Golden Seed tree at Outer Wall Phantom Tree"
        },
        "fixes": {
            "directions": "Near Outer Wall Phantom Tree (Site of Grace) - 3.63 "
                          "away in 1 o'clock direction, -0.23 height offset"
        }
    },
    {
        "conditions": {
            "text": "Under a Golden Seed tree found up the stairs from Outer "
                    "Wall Phantom Tree"
        },
        "fixes": {
            "directions": "Near Outer Wall Battleground (Site of Grace) - "
                          "223.03 away in 7 o'clock direction, -42.08 height "
                          "offset"
        }
    },
    {
        # there are two of each of these, but since the spoilers.txt file
        # matches the itemslots.txt file as far as order goes we can infer which
        # one is which, we just need to keep track of which one gets here first.
        "one_time": True,
        "conditions": {
            "replaces": "Furlcalling Finger Remedy",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near East Capital Rampart (Site of Grace) - 92.88 "
                          "away in 1 o'clock direction, -5.03 height offset"
        }
    },
    {
        "one_time": True,
        "conditions": {
            "replaces": "Furlcalling Finger Remedy",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near Royal Colosseum (Marker) - 37.51 away in 10 "
                          "o'clock direction, 0.18 height offset"
            # "directions": "Near Divine Bridge (Site of Grace) - 128.07 away "
            #                "in 5 o'clock direction, -0.49 height offset"
        }
    },
    {
        "one_time": True,
        "conditions": {
            "replaces": "Smithing Stone [6]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near West Capital Rampart (Site of Grace) - 31.23 "
                          "away in 6 o'clock direction, -12.73 height offset"
        }
    },
    {
        "one_time": True,
        "conditions": {
            "replaces": "Smithing Stone [6]",
            "region": "Leyndell, Royal Capital",
            "container": "Corpse",
            "directions": ""
        },
        "fixes": {
            "directions": "Near West Capital Rampart (Site of Grace) - 108.84 "
                          "away in 6 o'clock direction, -23.79 height offset"
        }
    }
]
