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

itemFixes = [
    # these were fixed by better NPC naming in itemSlots.txt in 0.5.7
    # {
    #     "conditions": {
    #         "container": "Albinauric Lookout",
    #         "mapList": ["m60_35_50_00"]
    #     },
    #     "fixes": {
    #         "NPC": "Pidia"
    #     }
    # },
    # {
    #     "conditions": {
    #         "container": "Albinauric Lookout"
    #     },
    #     "fixes": {
    #         "NPC": "Old Albus"
    #     }
    # },
    # {
    #     # D's brother only has the Inseparable Sword
    #     "conditions": {
    #         "container": "D, Hunter of the Dead",
    #         "replaces": "Inseparable Sword"
    #     },
    #     "fixes": {
    #         "container": "D, Beholder of Death",
    #         "NPC": "D, Beholder of Death"
    #     }
    # },
    # {
    #     # separate Alexander's drops from other living jars
    #     "conditions": {
    #         "container": "Living Jar Warrior",
    #         "replaces": "Exalted Flesh"
    #     },
    #     "fixes": {
    #         "NPC": "Alexander, Warrior Jar"
    #     }
    # },
    # {
    #     "conditions": {
    #         "container": "Living Jar Warrior",
    #         "replaces": "Exalted Flesh 3x"
    #     },
    #     "fixes": {
    #         "NPC": "Alexander, Warrior Jar"
    #     }
    # },
    # {
    #     "conditions": {
    #         "container": "Living Jar Warrior",
    #         "replaces": "Jar"
    #     },
    #     "fixes": {
    #         "NPC": "Alexander, Warrior Jar"
    #     }
    # },
    # {
    #     "conditions": {
    #         "container": "Living Jar Warrior",
    #         "replaces": "Warrior Jar Shard"
    #     },
    #     "fixes": {
    #         "NPC": "Alexander, Warrior Jar"
    #     }
    # },
    {
        # Irina only has her letter
        "conditions": {
            "container": "Lightseeker Hyetta",
            "replaces": "Irina's Letter"
        },
        "fixes": {
            "container": "Irina of Morne"
        }
    },
    # certain enemies have a name mismatch between their item entries and their
    # enemy entries
    {
        "conditions": {
            "container": "Abductor Virgin (Swinging Sickle)",
            "containerIDs": ["16000860"],
        },
        "fixes": {
            "container": "Abductor Virgin Duo",
        }
    },
    {
        "conditions": {
            "container": "Ancient Hero of Zamor",
            "containerIDs": ["1042330800"],
        },
        "fixes": {
            "container": "Ancient Hero of Zamor Boss",
        }
    },
    {
        "conditions": {
            "container": "Ancient Hero of Zamor",
            "containerIDs": ["30080800"],
        },
        "fixes": {
            "container": "Ancient Hero of Zamor Boss",
        }
    },
    {
        "conditions": {
            "container": "Ancient Hero of Zamor",
            "containerIDs": ["30170800"],
        },
        "fixes": {
            "container": "Ancient Hero of Zamor Boss",
        }
    },
    {
        "conditions": {
            "container": "Astel",
            "containerIDs": ["12010401"],
        },
        "fixes": {
            "container": "Withered Astel",
        }
    },
    {
        "conditions": {
            "container": "Beastman of Farum Azula",
            "containerIDs": ["31030800"],
        },
        "fixes": {
            "container": "Beastman of Farum Azula Boss",
        }
    },
    {
        "conditions": {
            "container": "Beastman of Farum Azula (Cleaver)",
            "containerIDs": ["31100800"],
        },
        "fixes": {
            "container": "Beastman of Farum Azula Duo",
        }
    },
    {
        "conditions": {
            "container": "Black Knife Assassin",
            "containerIDs": ["1040520800"],
        },
        "fixes": {
            "container": "Black Knife Assassin Boss",
        }
    },
    {
        "conditions": {
            "container": "Black Knife Assassin",
            "containerIDs": ["30110800"],
        },
        "fixes": {
            "container": "Black Knife Assassin Boss",
        }
    },
    {
        "conditions": {
            "container": "Black Knife Assassin",
            "containerIDs": ["30050850"],
        },
        "fixes": {
            "container": "Black Knife Assassin Boss",
        }
    },
    {
        "conditions": {
            "container": "Black Knife Assassin",
            "containerIDs": ["31190800"],
        },
        "fixes": {
            "container": "Invisible Black Knife Assassin Boss",
        }
    },
    {
        "conditions": {
            "container": "Bloodhound Knight",
            "containerIDs": ["31050800"],
        },
        "fixes": {
            "container": "Bloodhound Knight Boss",
        }
    },
    {
        "conditions": {
            "container": "Cemetery Shade",
            "containerIDs": ["30050800"],
        },
        "fixes": {
            "container": "Cemetery Shade and Skeletons",
        }
    },
    {
        "conditions": {
            "container": "Cemetery Shade",
            "containerIDs": ["30000800"],
        },
        "fixes": {
            "container": "Cemetery Shade Boss",
        }
    },
    {
        "conditions": {
            "container": "Cemetery Shade",
            "containerIDs": ["30150800"],
        },
        "fixes": {
            "container": "Cemetery Shade Boss",
        }
    },
    {
        "conditions": {
            "container": "Cleanrot Knight (Spear)",
            "containerIDs": ["31200800"],
        },
        "fixes": {
            "container": "Cleanrot Knight Duo",
        }
    },
    {
        "conditions": {
            "container": "Cleanrot Knight",
            "containerIDs": ["31040800"],
        },
        "fixes": {
            "container": "Cleanrot Knight Boss",
        }
    },
    {
        "conditions": {
            "container": "Crucible Knight",
            "replaces": "Ruins Greatsword"
        },
        "fixes": {
            "container": "Crucible Misbegotten Duo",
            "containerID": "1051360800"
        }
    },
    {
        "conditions": {
            "container": "Crucible Knight",
            "containerIDs": ["1042370800"],
        },
        "fixes": {
            "container": "Crucible Knight Boss",
        }
    },
    {
        "conditions": {
            "container": "Crucible Knight Ordovis",
            "containerIDs": ["30100800"],
        },
        "fixes": {
            "container": "Crucible Knight Duo",
        }
    },
    {
        "conditions": {
            "container": "Crystalian",
            "containerIDs": ["32020800"],
        },
        "fixes": {
            "container": "Ringblade Crystalian Boss",
        }
    },
    {
        "conditions": {
            "container": "Crystalian (Ringblade)",
            "containerIDs": ["32050800"],
        },
        "fixes": {
            "container": "Crystalian Ringblade Spear Duo",
        }
    },
    {
        "conditions": {
            "container": "Crystalian (Staff)",
            "containerIDs": ["31060800"],
        },
        "fixes": {
            "container": "Crystalian Staff Spear Duo",
        }
    },
    {
        "conditions": {
            "container": "Demi-Human Chief",
            "containerIDs": ["31150800"],
        },
        "fixes": {
            "container": "Demi-Human Chief Duo",
        }
    },
    {
        "conditions": {
            "container": "Draconic Tree Sentinel",
            "containerIDs": ["1045520800"],
        },
        "fixes": {
            "container": "Draconic Tree Sentinel Boss",
        }
    },
    {
        "conditions": {
            "container": "Dragonkin Soldier",
            "containerIDs": ["12010850"],
        },
        "fixes": {
            "container": "Dragonkin Soldier Boss",
        }
    },
    {
        "conditions": {
            "container": "Dragonkin Soldier",
            "containerIDs": ["12020830"],
        },
        "fixes": {
            "container": "Dragonkin Soldier Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Avatar",
            "containerIDs": ["1038480800"],
        },
        "fixes": {
            "container": "Erdtree Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Avatar",
            "containerIDs": ["1033430800"],
        },
        "fixes": {
            "container": "Erdtree Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Avatar",
            "containerIDs": ["1043330800"],
        },
        "fixes": {
            "container": "Erdtree Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Avatar",
            "containerIDs": ["1052560800"],
        },
        "fixes": {
            "container": "Erdtree Avatar Duo",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Burial Watchdog",
            "containerIDs": ["30020800"],
        },
        "fixes": {
            "container": "Fire Erdtree Burial Watchdog Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Burial Watchdog",
            "containerIDs": ["30010800"],
        },
        "fixes": {
            "container": "Erdtree Burial Watchdog and Imps",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Burial Watchdog",
            "containerIDs": ["30070800"],
        },
        "fixes": {
            "container": "Lightning Erdtree Burial Watchdog Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Burial Watchdog",
            "containerIDs": ["30060800"],
        },
        "fixes": {
            "container": "Scepter Erdtree Burial Watchdog Boss",
        }
    },
    {
        "conditions": {
            "container": "Erdtree Burial Watchdog (Sword)",
            "containerIDs": ["30140800"],
        },
        "fixes": {
            "container": "Erdtree Burial Watchdog Duo",
        }
    },
    {
        "conditions": {
            "container": "Fallingstar Beast",
            "containerIDs": ["32080800"],
        },
        "fixes": {
            "container": "Regular Fallingstar Beast",
        }
    },
    {
        "conditions": {
            "container": "Fallingstar Beast",
            "containerIDs": ["1041500800"],
        },
        "fixes": {
            "container": "Regular Fallingstar Beast",
        }
    },
    {
        "conditions": {
            "container": "Fell Twin",
            "containerIDs": ["34140850"],
        },
        "fixes": {
            "container": "Fell Twin Duo",
        }
    },
    {
        "conditions": {
            "container": "Fire Giant"
        },
        "fixes": {
            "container": "Fire Giant 2"
        }
    },
    {
        "conditions": {
            "container": "Godfrey, First Elden Lord",
            "replaces": "Remembrance of Hoarah Loux"
        },
        "fixes": {
            "container": "Hoarah Loux, Warrior"
        }
    },
    {
        "conditions": {
            "container": "Godfrey, First Elden Lord",
            "replaces": "Talisman Pouch"
        },
        "fixes": {
            "container": "Goldfrey, First Elden Lord"
        }
    },
    {
        "conditions": {
            "container": "Godskin Noble",
            "containerIDs": ["16000850"],
        },
        "fixes": {
            "container": "Godskin Noble Boss"
        }
    },
    {
        "conditions": {
            "container": "Grafted Scion",
            "containerIDs": ["10010800"],
        },
        "fixes": {
            "container": "Grafted Scion Boss"
        }
    },
    {
        "conditions": {
            "container": "Grave Warden Duelist",
            "containerIDs": ["30040800"],
        },
        "fixes": {
            "container": "Grave Warden Duelist Boss"
        }
    },
    {
        "conditions": {
            "container": "Grave Warden Duelist",
            "containerIDs": ["30130800"],
        },
        "fixes": {
            "container": "Grave Warden Duelist Boss"
        }
    },
    {
        "conditions": {
            "container": "Guardian Golem",
            "containerIDs": ["31170800"],
        },
        "fixes": {
            "container": "Guardian Golem Boss"
        }
    },
    {
        "conditions": {
            "container": "Kindred of Rot",
            "containerIDs": ["31070800"],
        },
        "fixes": {
            "container": "Kindred of Rot Duo"
        }
    },
    {
        "conditions": {
            "container": "Leonine Misbegotten",
            "containerIDs": ["1043300800"],
        },
        "fixes": {
            "container": "Leonine Misbegotten Boss",
        }
    },
    {
        "conditions": {
            "container": "Magma Wyrm",
            "containerIDs": ["1035530800"],
        },
        "fixes": {
            "container": "Magma Wyrm Boss",
        }
    },
    {
        "conditions": {
            "container": "Magma Wyrm",
            "containerIDs": ["32070800"],
        },
        "fixes": {
            "container": "Magma Wyrm Boss",
        }
    },
    # {
    #     "conditions": {
    #         "container": "Margit"
    #     },
    #     "fixes": {
    #         # this needs to have "The" capitalized to properly match up with
    #         # randomized enemy replacement in the spoilers file.  the Margit
    #         # in Stormveil has a lowercase t, the one in the Capital Outskirts
    #         # has an uppercase T, and in itemSlots.txt, "Margit" as a full
    #         # container name is the one in the Capital Outskirts
    #         "container": "Margit, The Fell Omen"
    #     }
    # },
    {
        "conditions": {
            "container": "Miranda Blossom",
            "containerIDs": ["31020800"],
        },
        "fixes": {
            "container": "Miranda Blossom and Sprouts",
        }
    },
    {
        "conditions": {
            "container": "Miranda the Blighted Bloom",
            "containerIDs": ["31180800"],
        },
        "fixes": {
            "container": "Miranda Omenkiller Duo",
        }
    },
    {
        "conditions": {
            "container": "Misbegotten Warrior",
            "containerIDs": ["30120800"],
        },
        "fixes": {
            "container": "Misbegotten Perfumer Duo",
        }
    },
    {
        "conditions": {
            "container": "Morgott",
            "containerIDs": ["1043520701"],
        },
        "fixes": {
            "container": "Capital Outskirts Margit",
        }
    },
    {
        "conditions": {
            "container": "Night's Cavalry (Glaive)"
        },
        "fixes": {
            "container": "Night's Cavalry",
        }
    },
    {
        "conditions": {
            "container": "Nox Monk",
            "replaces": "Nox Flowing Sword"
        },
        "fixes": {
            "container": "Nox Duo",
            "containerID": "1049390800"
        }
    },
    {
        "conditions": {
            "container": "Omenkiller",
            "containerIDs": ["1035420800"],
        },
        "fixes": {
            "container": "Omenkiller Boss",
        }
    },
    {
        "conditions": {
            "container": "Onyx Lord",
            "containerIDs": ["34120800"],
        },
        "fixes": {
            "container": "Onyx Lord Boss",
        }
    },
    {
        "conditions": {
            "container": "Onyx Lord",
            "containerIDs": ["1036500800"],
        },
        "fixes": {
            "container": "Onyx Lord Boss",
        }
    },
    {
        "conditions": {
            "container": "Putrid Avatar",
            "containerIDs": ["1047400800"],
        },
        "fixes": {
            "container": "Putrid Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Putrid Avatar",
            "containerIDs": ["1050570850"],
        },
        "fixes": {
            "container": "Putrid Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Putrid Avatar",
            "containerIDs": ["1051400800"],
        },
        "fixes": {
            "container": "Putrid Avatar Boss",
        }
    },
    {
        "conditions": {
            "container": "Putrid Crystalian (Spear)",
            "containerIDs": ["31110800"],
        },
        "fixes": {
            "container": "Putrid Crystalian Trio",
        }
    },
    {
        "conditions": {
            "container": "Putrid Tree Spirit",
            "containerIDs": ["30160800"],
        },
        "fixes": {
            "container": "Putrid Tree Spirit Boss",
        }
    },
    {
        "conditions": {
            "container": "Rennala, Queen of the Full Moon"
        },
        "fixes": {
            "container": "Rennala 1"
        }
    },
    {
        "conditions": {
            "container": "Runebear",
            "containerIDs": ["31010800"],
        },
        "fixes": {
            "container": "Runebear Boss",
        }
    },
    {
        "conditions": {
            "container": "Scaly Misbegotten",
            "containerIDs": ["32000800"],
        },
        "fixes": {
            "container": "Scaly Misbegotten Boss",
        }
    },
    {
        "conditions": {
            "container": "Spiritcaller Snail",
            "containerIDs": ["30030800"],
        },
        "fixes": {
            "container": "Crucible Spiritcaller Snail",
        }
    },
    {
        "conditions": {
            "container": "Spiritcaller Snail",
            "containerIDs": ["31220800"],
        },
        "fixes": {
            "container": "Godskin Spiritcaller Snail",
        }
    },
    {
        "conditions": {
            "container": "Tibia Mariner",
            "containerIDs": ["1039440800"],
        },
        "fixes": {
            "container": "Tibia Mariner Boss",
        }
    },
    {
        "conditions": {
            "container": "Tibia Mariner",
            "containerIDs": ["1045390800"],
        },
        "fixes": {
            "container": "Tibia Mariner Boss",
        }
    },
    {
        "conditions": {
            "container": "Tibia Mariner",
            "containerIDs": ["1038520340"],
        },
        "fixes": {
            "container": "Tibia Mariner Boss",
        }
    },
    {
        "conditions": {
            "container": "Ulcerated Tree Spirit",
            "containerIDs": ["18000800"],
        },
        "fixes": {
            "container": "Ulcerated Tree Spirit Boss",
        }
    },
    {
        "conditions": {
            "container": "Ulcerated Tree Spirit",
            "containerIDs": ["1037540810"],
        },
        "fixes": {
            "container": "Ulcerated Tree Spirit Boss",
        }
    },
    {
        "conditions": {
            "container": "Ulcerated Tree Spirit",
            "containerIDs": ["30180800"],
        },
        "fixes": {
            "container": "Ulcerated Tree Spirit Boss",
        }
    },
    {
        "conditions": {
            "container": "Valiant Gargoyle",
            "containerIDs": ["12020800"],
        },
        "fixes": {
            "container": "Valiant Gargoyles",
        }
    },
    {
        "conditions": {
            "container": "Wormface",
            "containerIDs": ["1041530800"],
        },
        "fixes": {
            "container": "Wormface Boss",
        }
    },
    {
        # containerID mismatch between item and enemy
        "conditions": {
            "container": "Fia's Champion",
            "region": "Deeproot Depths",
            "replaces": "Fia's Mist"
        },
        "fixes": {
            "container": "Fia's Champions",
            # "containerID": "12030814"
            "containerID": "12030800"
        }
    },
    {
        # containerID mismatch between item and enemy
        "conditions": {
            "container": "Horned Remains",
            "replaces": "Ancestral Follower Ashes"
        },
        "fixes": {
            "container": "Ancestor Spirit",
            "containerID": "12080800"
        }
    },
    {
        # containerID mismatch between item and enemy
        "conditions": {
            "container": "Horned Remains",
            "replaces": "Remembrance of the Regal Ancestor"
        },
        "fixes": {
            "container": "Regal Ancestor Spirit",
            "containerID": "12090800"
        }
    },
    {
        # enemy missing container ID
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Northeast Giants' Gravepost",
            "directions": "Near Giants' Gravepost (Site of Grace) - 225.32 "
                          "away in 4 o'clock direction, 128.59 height offset"
        },
        "fixes": {
            "containerID": "2821661"
        }
    },
    {
        # enemy missing container ID
        "conditions": {
            "container": "Fingercreeper",
            "region": "Mountaintops of the Giants - East Zamor Ruins; "
                      "Flame Peak - Giant-Conquering Hero's Grave Entrance",
            "directions": "Near Giants' Mountaintop Catacombs (Site of Grace) "
                          "- 83.09 away in 4 o'clock direction, 76.56 height "
                          "offset"
        },
        "fixes": {
            "containerID": "2821239"
        }
    },
    {
        # enemy missing container ID
        "conditions": {
            "container": "Living Jar Warrior",
            "region": "Volcano Manor",
            "directions": "Near Prison Town Church (Site of Grace) - 49.78 "
                          "away in 10 o'clock direction, -44.50 height offset"
        },
        "fixes": {
            "containerID": "2801435"
        }
    },
    {
        # enemy missing container ID
        "conditions": {
            "container": "Flame Chariot",
            "region": "Mt. Gelmir - Seethewater Terminus",
            "directions": "Near Fort Laiedd (Fort) - 58.18 away in 5 o'clock "
                          "direction, -11.98 height offset"
        },
        "fixes": {
            "containerID": "2802800"
        }
    },
    {
        # Jarburg pots aren't randomized
        "conditions": {
            "container": "Living Jar Warrior",
            "containerID": "1039440730"
        },
        "fixes": {
            "newEnemy": "Living Jar Warrior",
        }
    },
    {
        # Jarburg pots aren't randomized
        "conditions": {
            "container": "Living Jar Warrior",
            "containerID": "1039440731"
        },
        "fixes": {
            "newEnemy": "Living Jar Warrior",
        }
    },
    # some enemies don't have a containerID in the item entry to match up
    # with the randomized enemy ID.
    # this is the noble with the treasure box just above the spiritspring
    # south of the bridge leading to Mt. Gelmir
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Altus Plateau - Mirage Rise; Mt. Gelmir - Bridge of "
                      "Iniquity",
            "replaces": "Golden Rune [10]",
            "directions": "Near Mirage Rise (Rise) - 88.41 away in 10 o'clock "
                          "direction, 44.34 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2810609"
        }
    },
    # These two are in the rock with the three fingercreepers just north of
    # Church of Repose, narrowed them down to these two IDs, one is on the north
    # side of the rock, the other on the south side where it meets the cliff
    # both of them are embedded in the base near the surface
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Southwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Church of Repose (Site of Grace) - 141.36 away "
                          "in 12 o'clock direction, -13.54 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821485"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Southwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Church of Repose (Site of Grace) - 155.40 away "
                          "in 12 o'clock direction, -9.49 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821484"
        }
    },
    # this one is also in the same rock, but seems to be embedded fairly deep
    # into it and up higher, may want to add to missable list
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Southwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Church of Repose (Site of Grace) - 148.66 away "
                          "in 12 o'clock direction, -2.58 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821483",
        }
    },
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Consecrated Snowfield - Northeast Foggy Area, Inner "
                      "Consecrated Snowfield",
            "replaces": "Golden Rune [13]",
            "directions": "Near Inner Consecrated Snowfield (Site of Grace) - "
                          "117.35 away in 5 o'clock direction, 25.58 height "
                          "offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821059"
        }
    },
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Consecrated Snowfield - Northeast Foggy Area, Inner "
                      "Consecrated Snowfield",
            "replaces": "Golden Rune [13]",
            "directions": "Near Consecrated Snowfield Catacombs (Site of Grace)"
                          " - 123.21 away in 9 o'clock direction, -35.86 "
                          "height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821054"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Northwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Church of Repose (Site of Grace) - 233.29 away "
                          "in 12 o'clock direction, -103.00 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821516"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Northwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Giants' Gravepost (Site of Grace) - 205.16 away"
                          " in 8 o'clock direction, 18.51 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821515"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Northwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Giants' Gravepost (Site of Grace) - 145.53 away"
                          " in 8 o'clock direction, -3.36 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821518"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Flame Peak - Northwest Giants' Gravepost",
            "replaces": "Somber Smithing Stone [7]",
            "directions": "Near Giants' Gravepost (Site of Grace) - 158.30 away"
                          " in 8 o'clock direction, 7.79 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821517"
        }
    },
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Capital Outskirts - Southeast Outer Wall Battleground",
            "replaces": "Golden Rune [12]",
            "directions": "Near Outer Wall Battleground (Site of Grace) - "
                          "190.53 away in 5 o'clock direction, -22.77 height "
                          "offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2812955"
        }
    },
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Altus Plateau - Road of Iniquity Side Path",
            "replaces": "Golden Rune [10]",
            "directions": "Near West Windmill Pasture (Pasture) - 76.33 away in"
                          " 6 o'clock direction, -45.91 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2810981"
        }
    },
    {
        "conditions": {
            "container": "Runebear",
            "region": "Deeproot Depths",
            "replaces": "Prince of Death's Cyst",
            "directions": "Near Across the Roots (Site of Grace) - 102.33 away "
                          "in 6 o'clock direction, -55.87 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2801067"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - Caria Manor",
            "replaces": "Somber Smithing Stone [2]",
            "directions": "Near Main Caria Manor Gate (Site of Grace) - 70.03 "
                          "away in 2 o'clock direction, 0.68 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802722"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - Caria Manor",
            "replaces": "Somber Smithing Stone [2]",
            "directions": "Near Caria Manor (Marker) - 31.73 away in 7 o'clock "
                          "direction, 2.99 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802726"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - Caria Manor",
            "replaces": "Somber Smithing Stone [2]",
            "directions": "Near Manor Lower Level (Site of Grace) - 55.13 away"
                          " in 12 o'clock direction, -12.26 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802723"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - Caria Manor",
            "replaces": "Somber Smithing Stone [2]",
            "directions": "Near Caria Manor (Marker) - 76.74 away in 4 o'clock "
                          "direction, -2.19 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802724"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - Caria Manor",
            "replaces": "Somber Smithing Stone [2]",
            "directions": "Near Main Caria Manor Gate (Site of Grace) - 37.89 "
                          "away in 3 o'clock direction, 6.66 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802725"
        }
    },
    {
        "conditions": {
            "container": "Guilty",
            "region": "Liurnia of the Lakes - Artist's Shack, Eastern Liurnia "
                      "Lake Shore",
            "replaces": "Briars of Sin",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2803945"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Fort Gael, Caelid Waypoint Ruins, Gaol Cave "
                      "Entrance",
            "replaces": "Fire Blossom 3x",
            "directions": "Near Fort Gael (Fort) - 14.89 away in 5 o'clock "
                          "direction, -10.68 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820258"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Fort Gael, Caelid Waypoint Ruins, Gaol Cave "
                      "Entrance",
            "replaces": "Fire Blossom 3x",
            "directions": "Near Fort Gael (Fort) - 15.96 away in 3 o'clock "
                          "direction, -10.68 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820257"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Greyoll's Dragonbarrow - Fort Faroth",
            "replaces": "Golden Rune [9]",
            "directions": "Near Fort Faroth (Site of Grace) - 47.16 away in 3 "
                          "o'clock direction, 7.98 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821387"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Greyoll's Dragonbarrow - Fort Faroth",
            "replaces": "Golden Rune [9]",
            "directions": "Near Fort Faroth (Site of Grace) - 35.88 away in 3 "
                          "o'clock direction, 8.16 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821386"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Greyoll's Dragonbarrow - Fort Faroth",
            "replaces": "Golden Rune [9]",
            "directions": "Near Fort Faroth (Site of Grace) - 27.33 away in 3 "
                          "o'clock direction, 7.96 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821388"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Gowry's Shack",
            "replaces": "Golden Rune [9]",
            "directions": "Near Gowry's Shack (Shack) - 55.71 away in 5 "
                          "o'clock direction, 40.04 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821151"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Gowry's Shack",
            "replaces": "Golden Rune [9]",
            "directions": "Near Gowry's Shack (Shack) - 70.00 away in 4 "
                          "o'clock direction, 38.72 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821152"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Gowry's Shack",
            "replaces": "Golden Rune [9]",
            "directions": "Near Gowry's Shack (Shack) - 40.57 away in 4 "
                          "o'clock direction, 40.04 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821153"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Gowry's Shack",
            "replaces": "Golden Rune [9]",
            "directions": "Near Gowry's Shack (Shack) - 53.50 away in 1 "
                          "o'clock direction, 40.99 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821154"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Gowry's Shack",
            "replaces": "Golden Rune [9]",
            "directions": "Near Gowry's Shack (Shack) - 55.25 away in 1 "
                          "o'clock direction, 41.14 height offset",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821155"
        }
    },
    {
        "conditions": {
            "container": "Wandering Noble",
            "region": "Limgrave - Waypoint Ruins",
            "replaces": "Glintstone Staff",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2813342"
        }
    },
    {
        "conditions": {
            "container": "Grave Warden Duelist",
            "region": "Consecrated Snowfield - Ordina, Liturgical Town",
            "replaces": "Rotten Duelist Greaves",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820816"
        }
    },
    {
        "conditions": {
            "container": "Grave Warden Duelist",
            "region": "Consecrated Snowfield - Southwest Foggy Area",
            "replaces": "Rotten Battle Hammer",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820734"
        }
    },
    {
        "conditions": {
            "container": "Ancestral Follower",
            "region": "Lake of Rot",
            "replaces": "Immunizing Horn Charm +1",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2800173"
        }
    },
    {
        "conditions": {
            "container": "Giant Ball",
            "region": "Nokron, Eternal City",
            "replaces": "Larval Tear",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2800393"
        }
    },
    {
        "conditions": {
            "container": "Omenkiller",
            "region": "Volcano Manor",
            "replaces": "Great Omenkiller Cleaver",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2801447"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Caelem Ruins, Forsaken Ruins, Minor Erdtree, "
                      "Minor Erdtree Catacombs Entrance",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820349"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Bellum Highway - Church of Inhibition, Southwest of "
                      "Grand Lift of Dectus",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2803541"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Deep Siofra Well; Greyoll's Dragonbarrow - "
                      "Dragonbarrow West",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820662"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Fort Gael North",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820312"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Liurnia of the Lakes - Eastern Tableland, Ainsel River "
                      "Well",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2803984"
        }
    },
    {
        "conditions": {
            "container": "Flame Chariot",
            "region": "Caelid - Smoldering Wall, Abandoned Cave Entrance",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2820596"
        }
    },
    {
        "conditions": {
            "container": "Fingercreeper",
            "region": "Liurnia of the Lakes - South of Caria Manor, West of "
                      "Ravine Entrance",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2802698"
        }
    },
    {
        "conditions": {
            "container": "Leyndell Knight",
            "region": "Liurnia of the Lakes - North of Gate Town Bridge",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2803884"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Weeping Peninsula - Castle Morne Approach Northwest "
                      "Cliffside",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2812395"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Caelid - Redmane Castle South Cliffside",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2821327"
        }
    },
    {
        "conditions": {
            "container": "Operatic Bat",
            "region": "Liurnia of the Lakes - Cuckoo's Evergaol, West of "
                      "Meeting Place",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2801862"
        }
    },
    {
        "conditions": {
            "container": "Battlemage",
            "region": "Altus Plateau - West Windmill Pasture",
            "replaces": "Haima Glintstone Crown",
            "containerIDs": []
        },
        "fixes": {
            "containerID": "2811049"
        }
    },
    {
        # Ancient Dragon Lansseax appears in two places, but we want the
        # Rampartside Path location
        "conditions": {
            "container": "Ancient Dragon Lansseax",
            "region": "Altus Plateau",
            "replaces": "Lansseax's Glaive"
        },
        "fixes": {
            "containerID": "1041520800"
        }
    },
    # items dropped by NPCs that show up as generic Shiny Items
    {
        "conditions": {
            "replaces": "Latenna the Albinauric"
        },
        "fixes": {
            "container": "Latenna the Albinauric"
        }
    },
    {
        "conditions": {
            "replaces": "Blue Silver Mail Hood"
        },
        "fixes": {
            "container": "Latenna the Albinauric"
        }
    },
    {
        "conditions": {
            "replaces": "Shard of Alexander"
        },
        "fixes": {
            "container": "Alexander, Warrior Jar"
        }
    },
    {
        "conditions": {
            "replaces": "Goldmask's Rags"
        },
        "fixes": {
            "container": "The Noble Goldmask"
        }
    },
    {
        "conditions": {
            "replaces": "Mending Rune of Perfect Order"
        },
        "fixes": {
            "container": "The Noble Goldmask"
        }
    },
    {
        "conditions": {
            "replaces": "Royal Remains Helm"
        },
        "fixes": {
            "container": "Ensha of the Royal Remains"
        }
    },
    {
        "conditions": {
            "replaces": "Thops's Barrier"
        },
        "fixes": {
            "container": "Sorcerer Thops"
        }
    },
    {
        "conditions": {
            "replaces": "Iji's Mirrorhelm"
        },
        "fixes": {
            "container": "Smithing Master Iji"
        }
    },
    {
        "conditions": {
            "replaces": "Rogier's Letter"
        },
        "fixes": {
            "container": "Sorcerer Rogier"
        }
    },
    {
        "conditions": {
            "replaces": "Fia's Hood"
        },
        "fixes": {
            "container": "Fia, Deathbed Companion"
        }
    },
    {
        "conditions": {
            "replaces": "Mending Rune of the Death-Prince"
        },
        "fixes": {
            "container": "Fia, Deathbed Companion"
        }
    },
    {
        "conditions": {
            "replaces": "Frenzied Flame Seal"
        },
        "fixes": {
            "container": "Lightseeker Hyetta"
        }
    },
    {
        "conditions": {
            "replaces": "Consort's Mask"
        },
        "fixes": {
            "container": "Tanith, Volcano Manor Proprietress"
        }
    },
    {
        "conditions": {
            "replaces": "Zorayas's Letter"
        },
        "fixes": {
            "container": "Rya the Scout"
        }
    },
    {
        "conditions": {
            "replaces": "Mending Rune of the Fell Curse"
        },
        "fixes": {
            "container": "Dung Eater"
        }
    },
    {
        "conditions": {
            "replaces": "Dark Moon Greatsword"
        },
        "fixes": {
            "container": "Ranni the Witch"
        }
    },
    {
        "conditions": {
            "replaces": "Seedbed Curse",
            "container": "Shiny Item",
            "region": "Capital Outskirts - South of Minor Erdtree"
        },
        "fixes": {
            "container": "Blackguard"
        }
    },
    {
        "conditions": {
            "replaces": "Companion Jar"
        },
        "fixes": {
            "container": "Jar-Bairn"
        }
    },
    {
        "conditions": {
            "replaces": "Rotten Winged Sword Insignia"
        },
        "fixes": {
            "container": "Millicent"
        }
    },
    {
        "conditions": {
            "replaces": "Flock's Canvas Talisman"
        },
        "fixes": {
            "container": "Sage Gowry"
        }
    },
]
