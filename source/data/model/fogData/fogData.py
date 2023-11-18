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

# Note: drop tags mean any one way transition
fogDropFixes = {
    # drops
    "graveyard_cave_back": ["graveyard_cave"],
    "sewer_preflame": ["sewer_flame"],
    "volcano_temple": ["volcano_posttemple"],
    "leyndell2": ["leyndell2_sanctuaryside"],
    # one way doors
    "graveyard": ["graveyard_grave"],
    "stormveil_godrick": ["stormveil_throne"],
    "academy_entrance": ["academy"],
    "sewer_royal": ["sewer"],
    "snowfield_prehiddenpath": ["snowfield_hiddenpath"],
    "volcano_predoor": ["volcano"],
    "volcano_pretown": ["volcano_town"],
    "caelid_gaeltunnel": ["caelid_gaeltunnel_rear"],
    "volcano": ["volcano_drawingroom"],
    "liurnia_studyhall": ["liurnia_tower"],
    # "leyndell_erdtree": ["leyndell2_erdtree"],
    # "sewer_mohg": ["deeproot_start|sewer_flame|sewer_preflame"],
    # "leyndell2_erdtree": ["erdtree"],
    # one way door and locked elevator
    "volcano_posttemple": ["volcano_sendinggate",
                           "volcano_posttemple_elevator"],
    "leyndell": ["leyndell_pretower", "leyndell_divinebridge"],
    # locked elevator
    "precipice_postboss": ["altus"],
    # Deathbed Dream boss is not randomized, requires Cursemark of Death
    "deeproot_boss": ["deeproot_dream"],
}

fogBigAreaFixes = [
    ["deeproot_start", "sewer_flame", "sewer_preflame"],
    ["haligtree_elphael", "haligtree_postloretta"],
    ["snowfield_prehiddenpath", "snowfield_rold"],
    ["volcano_posttemple", "volcano_sendinggate"],
]

fogNewGateAreas = [
    "bellum|liurnia|liurnia_manor",
    "caelid|caelid_redmane|dragonbarrow|limgrave|peninsula|peninsula_morne|"
    "stormhill",
]

fogNoNewGateArea = "bellum|caelid|caelid_redmane|dragonbarrow|limgrave|liurnia"\
                "|liurnia_manor|peninsula|peninsula_morne|stormhill"

fogBlockedConditions = [
    "caelid_radahn"
]

fogIgnoreGates = [
    # to: transitions
    # effective duplicate of drop inside Caria Manor near Pidia
    "dropping down from the south edge of the Royal Grave",
    # Deathbed Dream is part of Fia's quest, no need to add to network
    "using Cursemark of Death with Fia, missable",
    # gates
    # any gate without a text description
    "''",
    # nonexistent elphael/postloretta gate
    "Before Elphael",
    # nonexistent gate between hidden Rold lift and the room before Hidden Path
    "Snowfield Rold destination",
    # renna gate (?)
]

fogArrivalAreas = {
    "altus|altus_shaded|gelmir|outskirts": {
        "arriving at the north side of the Forest-Spanning Greatbridge":
            "Altus Plateau",
        "arriving at the Grand Lift of Dectus in Altus Plateau":
            "Altus Plateau",
    },
    "caelid|caelid_redmane|dragonbarrow|limgrave|peninsula|peninsula_morne|"
    "stormhill": {
        "arriving at the east side of Impassable Greatbridge": "Caelid",
        "arriving at the west side of Impassable Greatbridge": "Caelid",
        "arriving outside Bestial Sanctum": "Bestial Sanctum",
        "arriving in the middle of Mistwood": "Mistwood",
        "arriving at the Redmane Castle sending gate": "Redmane Castle",
    },
    "bellum|liurnia|liurnia_manor": {
        "arriving by Northern Liurnia Lake Shore grace before Iji": "Liurnia",
        "arriving in Church of Vows": "Church of Vows",
        "arriving at East Raya Lucaria Gate": "Bellum Highway",
        "arriving at South Raya Lucaria Gate": "Academy Gate Town",
        "arriving at the Grand Lift of Dectus in Bellum Highway":
            "Bellum Highway",
    },
    "bellum|caelid|caelid_redmane|dragonbarrow|limgrave|liurnia|liurnia_manor"
    "|peninsula|peninsula_morne|stormhill": {
        "arriving at the east side of Impassable Greatbridge": "Caelid",
        "arriving at the west side of Impassable Greatbridge": "Caelid",
        "arriving outside Bestial Sanctum": "Bestial Sanctum",
        "arriving in the middle of Mistwood": "Mistwood",
        "arriving at the Redmane Castle sending gate": "Redmane Castle",
        "arriving by Northern Liurnia Lake Shore grace before Iji": "Liurnia",
        "arriving in Church of Vows": "Church of Vows",
        "arriving at East Raya Lucaria Gate": "Bellum Highway",
        "arriving at South Raya Lucaria Gate": "Academy Gate Town",
        "arriving at the Grand Lift of Dectus in Bellum Highway":
            "Bellum Highway",
    },
    # Gaol Cliff
    "limgrave": {
        "dropping down": "Limgrave",
    },
    # Inquisitor's Passage
    "gelmir": {
        "dropping down": "Mt. Gelmir",
    },
    # Precipice Lift
    "altus": {
        "taking the elevator up": "Altus Plateau",
    },
}

# reversible warps not dependent on options and not marked as evergaols
fogReversibleWarps = [
    "Fell Twins",
    "Fell Twins return",
    "Ordina Evergaol",
    "Ordina Evergaol return",
    "Auriza Side Tomb chest before the main hallway",
    "Auriza Side Tomb chest at the end of main hallway",
    "Auriza Side Tomb chest behind the main hallway illusory wall",
    "Auriza Side Tomb chest in the actual entrance",
    "Auriza Side Tomb chest in the main jail",
    "Auriza Side Tomb chest in the duplicate second floor",
    "Auriza Side Tomb chest in the duplicate jail",
    "Auriza Side Tomb chest at the end of the duplicate hallway",
    "Auriza side Tomb chest behind the duplicate hallway illusory wall",
    "Auriza Side Tomb chest in the main second floor",
    "Auriza Side Tomb chest up a ladder from the main second floor",
    "Auriza Side Tomb chest in the duplicate entrance area",
]

# This uses the unique text identifier for a warp to index to the spoiler text
# description of the aSide of the linked reverse warp. When trying to find the
# reverse warp of an arrival point listed in spoilers, first find the warp that
# arrival point belongs to from all warps, then use the reverseWarp entry to
# get the key for the arrival area's gate entry.
fogReverseWarps = {
    # evergaols
    "Ringleader's Evergaol": "finishing Ringleader's Evergaol",
    "Ringleader's Evergaol return": "entering Ringleader's Evergaol",
    "Cuckoo's Evergaol": "finishing Cuckoo's Evergaol",
    "Cuckoo's Evergaol return": "entering Cuckoo's Evergaol",
    "Royal Grave Evergaol": "finishing Royal Grave Evergaol",
    "Royal Grave Evergaol return": "entering Royal Grave Evergaol",
    "Malefactor's Evergaol": "finishing Malefactor's Evergaol",
    "Malefactor's Evergaol return": "entering Malefactor's Evergaol",
    "Golden Lineage Evergaol": "finishing Golden Lineage Evergaol",
    "Golden Lineage Evergaol return": "entering Golden Lineage Evergaol",
    "Weeping Evergaol": "finishing Weeping Evergaol",
    "Weeping Evergaol return": "entering Weeping Evergaol",
    "Stormhill Evergaol": "finishing Stormhill Evergaol",
    "Stormhill Evergaol return": "entering Stormhill Evergaol",
    "Forlorn Hound Evergaol": "finishing Forlorn Hound Evergaol",
    "Forlorn Hound Evergaol return": "entering Forlorn Hound Evergaol",
    "Sellia Evergaol": "finishing Sellia Evergaol",
    "Sellia Evergaol return": "entering Sellia Evergaol",
    "Lord Contender's Evergaol": "finishing Lord Contender's Evergaol",
    "Lord Contender's Evergaol return": "entering Lord Contender's Evergaol",
    # special evergaols
    "Ordina Evergaol": "finishing Ordina Evergaol",
    "Ordina Evergaol return": "entering Ordina Evergaol",
    "Fell Twins": "finishing the Fell Twins' arena fight",
    "Fell Twins return": "approaching the Divine Tower of East Altus gate, or "
                         "using the grace menu",
    # auriza side tomb chests
    "Auriza Side Tomb chest before the main hallway":
        "using the chest in the actual entrance",
    "Auriza Side Tomb chest in the actual entrance":
        "using the chest before the main hallway",
    "Auriza Side Tomb chest at the end of main hallway":
        "using the chest in the main jail",
    "Auriza Side Tomb chest in the main jail":
        "using the chest at the end of the main hallway",
    "Auriza Side Tomb chest behind the main hallway illusory wall":
        "using the chest overlooking the duplicate hallway",
    "Auriza Side Tomb chest in the duplicate second floor":
        "using the chest behind the illusory wall",
    "Auriza Side Tomb chest in the duplicate jail":
        "using the chest at the end of the duplicate hallway",
    "Auriza Side Tomb chest at the end of the duplicate hallway":
        "using the chest in the duplicate jail",
    "Auriza side Tomb chest behind the duplicate hallway illusory wall":
        "using the chest overlooking the main hallway",
    "Auriza Side Tomb chest in the main second floor":
        "using the chest behind the illusory wall",
    "Auriza Side Tomb chest up a ladder from the main second floor":
        "using the chest in the duplicate entrance area",
    "Auriza Side Tomb chest in the duplicate entrance area":
        "using the chest up the ladder from the main second floor",
    # coupledwarp
    "Rold to Mountaintops":
        "using the Rold Medallion at Mountaintops of the Giants",
    "Rold to Forbidden Lands": "using the Rold Medallion at Forbidden Lands",
    "Secret Rold to Consecrated Snowfield":
        "using the Haligtree secret medallions at Hidden Path to the Haligtree",
    "Secret Rold to Forbidden Lands":
        "using the Haligtree secret medallions at Forbidden Lands",
    "Dectus to Altus": "using the Dectus Medallion in Altus Plateau",
    "Dectus to Bellum Highway": "using the Dectus Medallion in Bellum Highway",
    "Raya Lucaria East to Main":
        "using East-facing gate at Raya Lucaria Main Entrance",
    "Raya Lucaria Main to East": "using East Raya Lucaria Gate",
    "Raya Lucaria South to Main":
        "using South-facing gate at Raya Lucaria Main Entrance",
    "Raya Lucaria Main to South": "using South Raya Lucaria Gate",
    # coupledminor
    "Sending gate from first island after Siofra River Bank grace to after "
    "Worshippers' Woods grace":
        "using the sending gate after the Worshippers' Woods grace",
    "Sending gate from after Worshippers' Woods grace to first island after "
    "Siofra River Bank grace":
        "using the sending gate after the Siofra River Bank grace",
    "Sending gates from Impassable Greatbridge into Redmane Castle":
        "using the sending gate in Redmane Castle",
    "Sending gate from Redmane Castle back to Impassable Greatbridge":
        "using either sending gate in Impassable Greatbridge",
}

fogTwoWayTransitions = {
    "in map": None,
    "at the Morgott the Grace-Given gate coming from Leyndell": {
        "Divine Tower of East Altus":
            "at the Morgott the Grace-Given gate coming from Forbidden Lands",
        "Divine Tower of East Altus Start":
            "at the Morgott the Grace-Given gate coming from Leyndell",
    },
    "at the Morgott the Grace-Given gate coming from Forbidden Lands": {
        "Divine Tower of East Altus":
            "at the Morgott the Grace-Given gate coming from Forbidden Lands",
        "Divine Tower of East Altus Start":
            "at the Morgott the Grace-Given gate coming from Leyndell",
    },
    "to Leyndell after acquiring enough Great Runes": {
        "Capital Outskirts - Capital Rampart":
            "to Capital Rampart after acquiring enough Great Runes",
        "Leyndell Start":
            "to Leyndell after acquiring enough Great Runes"
    },
    "to Capital Rampart after acquiring enough Great Runes": {
        "Capital Outskirts - Capital Rampart":
            "to Capital Rampart after acquiring enough Great Runes",
        "Leyndell Start":
            "to Leyndell after acquiring enough Great Runes"
    },
}

fogPreexistingTransitions = [
    "accessing an overworld grace",
    "after burning the Erdtree by defeating the boss in Maliketh's arena",
    "at entrance to Hidden Path to Haligtree dungeon",
    "at the Morgott the Grace-Given gate after Mohg the Omen's arena",
    "at the Morgott the Grace-Given gate before Frenzied Flame Proscription",
    "at the Morgott the Grace-Given gate coming from Leyndell",
    "at the Morgott the Grace-Given gate coming from Forbidden Lands",
    "at the start of Elphael",
    "completing the loop back to the Church of Cuckoo",
    "completing the path atop floating debris",
    "double-jumping off the bridge to the northwest pillar",
    "dropping back down to the courtyard at the start of rooftops section",
    "dropping down",
    "dropping down after Crumbling Beast Grave grace",
    "dropping down after climbing the ladder",
    "dropping down behind Castle Morne",
    "dropping down below the east-side bridge",
    "dropping down from the south edge of the Royal Grave",
    "dropping down in the southeast corner of the courtyard",
    "dropping down into the manor by Pidia",
    "dropping down past Aqueduct-Facing Cliffs grace",
    "dropping down past Jerren's platform",
    "dropping down past two illusory walls",
    "dropping down south of Deep Siofra Well",
    "dropping down south of the Ancestral Grounds grace",
    "dropping down the beams",
    "dropping down the small waterfall",
    "dropping down through the open sewer grate",
    "dropping down to the first Nokron grace",
    "dropping down to the north",
    "dropping down to the platform before the Dragon Temple grace",
    "dropping down to the right of the sanctuary entrance from the elevator",
    "dropping down, like near Bolt of Gransax",
    "dropping into the boss fight",
    "in map",
    "instead of entering the sanctuary, dropping down to the left",
    "instead of entering the sanctuary, dropping down to the right",
    "jumping into the lava behind the Sending Gate. this requires some vigor and flasks",
    "jumping over the balcony",
    "jumping to the stairs west of the Dragon Temple grace and dropping down again",
    "opening the door",
    "opening the door after the boss",
    "opening the doors to the Church of Cuckoo",
    "opening the first door into Volcano Manor",
    "opening the gate",
    "opening the heavy door",
    "opening the heavy door below East Capital Rampart",
    "opening the heavy doors",
    "opening the locked chest using the Discarded Palace Key",
    "opening the one-way door",
    "riding the elevator up and dropping down outside",
    "taking the elevator from Fortified Manor",
    "taking the elevator up",
    "to Capital Rampart after acquiring enough Great Runes",
    "to Leyndell after acquiring enough Great Runes",
    "touching the golden light",
    "traversing down the roots",
    "unlocking the elevator shortcut back to the temple",
    "using Carian Inverted Statue",
    "using Cursemark of Death with Fia, missable",
    "using Drawing-Room Key",
    "using a Stonesword Key and dropping down",
    "using a Stonesword Key, dropping down, and opening a door",
    "using two Stonesword Keys",
    "with Rusty Key or talking to Gostoc",
]

fogAreaFixes = {
    # added "area" for Pureblood Knight's Medal, so it's not part of the network
    "pureblood": {
        "hintName": "anywhere",
        "isNode": True,
    },
    "caelid|caelid_redmane|dragonbarrow|limgrave|peninsula|peninsula_morne|"
    "stormhill": {
        "hintName": "FIXME Limgrave group",
        "isNode": True,
    },
    "bellum|caelid|caelid_redmane|dragonbarrow|limgrave|liurnia|liurnia_manor|"
    "peninsula|peninsula_morne|stormhill": {
        "hintName": "FIXME Limgrave/Liurnia group",
        "isNode": True,
    },
    "bellum|liurnia|liurnia_manor": {
        "hintName": "FIXME Liurnia group",
        "isNode": True,
    },
    "deeproot_start|sewer_flame|sewer_preflame": {
        "hintName": "Frenzied Flame",
    },
    "stormveil|stormveil_start": {
        "hintName": "Stormveil Castle",
        "isNode": True,
    },
    "altus|altus_shaded|gelmir|outskirts": {
        "hintName": "FIXME Altus Plateau group",
        "isNode": True,
    },
    "volcano_posttemple|volcano_sendinggate": {
        "hintName": "Caldera Hall",
        "isNode": True,
    },
    "ainsel|lakeofrot": {
        "hintName": "Ainsel Main",
        "isNode": True,
    },
    "flamepeak|mountaintops|mountaintops_sol": {
        "hintName": "Mountaintops",
        "isNode": True,
    },
    # special case where having the coupledwarp option on makes it a corridor
    # but off makes it a node
    "snowfield_prehiddenpath|snowfield_rold": {
        "hintName": "Hidden Lift",
        "noLots": True,
        "isCoupledWarpNode": True,
    },
    "haligtree_elphael|haligtree_postloretta": {
        "hintName": "Elphael",
    },
    "chapel_start": {
        "hintName": "Chapel of Anticipation",
        "isNode": True,
    },
    "chapel_boss": {
        "hintName": "Chapel Courtyard",
    },
    "chapel_postboss": {
        "hintName": "Chapel Graveyard",
        "noLots": True,
    },
    "graveyard_cave": {
        "hintName": "Cave of Knowledge",
        "isNode": True,
        "noLots": True,
    },
    "graveyard_cave_boss": {
        "hintName": "Lair of Knowledge",
        "noLots": True,
    },
    "graveyard_cave_postboss": {
        "hintName": "Ledge of Knowledge",
        "noLots": True,
    },
    "graveyard_cave_back": {
        "hintName": "Passage of Knowledge",
    },
    "graveyard": {
        "hintName": "Stranded Graveyard",
        "isNode": True,
    },
    "graveyard_grave": {
        "hintName": "Fringefolk Grave",
    },
    "graveyard_grave_boss": {
        "hintName": "Fringefolk Tomb",
    },
    "limgrave": {
        "hintName": "FIXME Limgrave",
    },
    "limgrave_evergaol": {
        "hintName": "Hound Evergaol",
    },
    "limgrave_waypoint_boss": {
        "hintName": "Waypoint Chamber",
    },
    "limgrave_waypoint_sellen": {
        "hintName": "Waypoint Vault",
    },
    "stormhill": {
        "hintName": "FIXME Stormhill",
    },
    "stormhill_evergaol": {
        "hintName": "Stormhill Evergaol",
    },
    "roundtable": {
        "hintName": "Roundtable Hold",
        "isNode": True,
    },
    "roundtable_balcony": {
        "hintName": "Roundtable Hall",
    },
    "limgrave_coastalcave": {
        "hintName": "Coastal Cave",
    },
    "limgrave_coastalcave_boss": {
        "hintName": "Coastal Lair",
    },
    "limgrave_dragonchurch": {
        "hintName": "Dragon Church",
    },
    "stormveil_margit": {
        "hintName": "Stormveil Gate",
    },
    "stormveil_start": {
        "hintName": "FIXME Stormveil Castle start",
    },
    "stormveil": {
        "hintName": "FIXME Stormveil Castle",
    },
    "stormveil_godrick": {
        "hintName": "Stormveil Courtyard",
    },
    "stormveil_throne": {
        "hintName": "Stormveil Throne",
    },
    "limgrave_tower": {
        "hintName": "Stormveil Bridge",
    },
    "limgrave_tower2": {
        "hintName": "Limgrave Tower",
    },
    "peninsula": {
        "hintName": "FIXME Weeping Peninsula",
    },
    "peninsula_evergaol": {
        "hintName": "Weeping Evergaol",
    },
    "peninsula_morne": {
        "hintName": "FIXME Castle Morne",
    },
    "peninsula_postmorne": {
        "hintName": "Castle Morne",
    },
    "peninsula_leonine": {
        "hintName": "Morne Moangrave",
    },
    "liurnia": {
        "hintName": "FIXME Liurnia",
    },
    "liurnia_evergaol_adan": {
        "hintName": "Malefactor's Evergaol",
    },
    "liurnia_evergaol_bols": {
        "hintName": "Cuckoo's Evergaol",
    },
    "liurnia_kingsrealm_boss": {
        "hintName": "Kingsrealm Chamber",
    },
    "liurnia_kingsrealm_chest": {
        "hintName": "Kingsrealm Vault",
    },
    "liurnia_slumbering": {
        "hintName": "Wolf's Shack",
    },
    "bellum": {
        "hintName": "FIXME Bellum Highway",
    },
    "academy_entrance": {
        "hintName": "Academy Gate",
        "isNode": True,
    },
    "academy": {
        "hintName": "Lucaria Academy",
        "isNode": True,
    },
    "academy_redwolf": {
        "hintName": "Academy Parlor",
    },
    "academy_courtyard": {
        "hintName": "Academy Courtyard",
        "isNode": True,
    },
    "academy_rooftops": {
        "hintName": "Academy Rooftops",
        "isNode": True,
    },
    "academy_library": {
        "hintName": "Academy Library",
    },
    "academy_cavetower": {
        "hintName": "Academy Tower",
    },
    "siofra": {
        "hintName": "Siofra River",
        "isNode": True,
    },
    "siofra_dragonkin": {
        "hintName": "Upper Siofra",
    },
    "siofra_preboss": {
        "hintName": "Siofra Grotto",
        "noLots": True
    },
    "siofra_boss": {
        "hintName": "Siofra Lair",
    },
    "ainsel_start": {
        "hintName": "Ainsel River",
        "isNode": True,
    },
    "ainsel_abovestart": {
        "hintName": "Ainsel Ledge",
    },
    "ainsel_dragonkin": {
        "hintName": "Ainsel Falls",
    },
    "ainsel_postdragonkin": {
        "hintName": "Ainsel Vault",
    },
    "liurnia_studyhall": {
        "hintName": "Study Hall",
    },
    "caelid": {
        "hintName": "FIXME Caelid",
    },
    "caelid_crypt_boss": {
        "hintName": "Sellia Chair-Crypt",
    },
    "caelid_crypt_chest": {
        "hintName": "Sellia Vault",
    },
    "caelid_caelem_boss": {
        "hintName": "Caelem Chamber",
    },
    "caelid_caelem_chest": {
        "hintName": "Caelem Vault",
    },
    "caelid_greatjar": {
        "hintName": "Caelid Canyon",
        "isNode": True,
    },
    "dragonbarrow": {
        "hintName": "FIXME Dragonbarrow",
    },
    "dragonbarrow_evergaol": {
        "hintName": "Sellia Evergaol",
    },
    "precipice": {
        "hintName": "Ruin-Strewn Precipice",
    },
    "precipice_boss": {
        "hintName": "Precipice Lair",
    },
    "precipice_postboss": {
        "hintName": "Precipice Lift",
    },
    "altus": {
        "hintName": "FIXME Altus Plateau",
    },
    "altus_evergaol": {
        "hintName": "Golden Evergaol",
    },
    "altus_lux_boss": {
        "hintName": "Lux Chamber",
    },
    "altus_lux_chest": {
        "hintName": "Lux Vault",
    },
    "altus_writheblood_boss": {
        "hintName": "Writheblood Chamber",
    },
    "altus_writheblood_chest": {
        "hintName": "Writheblood Vault",
    },
    "altus_shaded": {
        "hintName": "FIXME Shaded Castle",
    },
    "altus_elemer": {
        "hintName": "Castellan's Hall",
    },
    "outskirts": {
        "hintName": "FIXME Capital Outskirts",
    },
    "outskirts_rampart": {
        "hintName": "Capital Rampart",
        "isNode": True,
        "noLots": True,
    },
    "leyndell_start": {
        "hintName": "Leyndell Lift",
    },
    "leyndell": {
        "hintName": "Leyndell",
        "isNode": True,
    },
    "leyndell_divinebridge": {
        "hintName": "Divine Bridge",
    },
    "leyndell_sanctuary": {
        "hintName": "Erdtree Sanctuary",
        "isNode": True,
    },
    "leyndell_sanctuaryfront": {
        "hintName": "Sanctuary Lift",
    },
    "leyndell_sanctuaryback": {
        "hintName": "Sanctuary Balcony",
        "isNode": True,
    },
    "leyndell_sanctuaryleft": {
        "hintName": "Sanctuary Alcove",
    },
    "leyndell_bedchamber": {
        "hintName": "Queen's Bedchamber",
        "isNode": True,
    },
    "leyndell_throne": {
        "hintName": "Elden Throne",
    },
    "leyndell_erdtree": {
        "hintName": "Erdtree",
        "noLots": True,
    },
    "leyndell_pretower": {
        "hintName": "Leyndell East",
    },
    "leyndell_tower_start": {
        "hintName": "Leyndell East Lift",
    },
    "leyndell_tower": {
        "hintName": "Leyndell Tower",
        "isNode": True,
    },
    "leyndell_tower_boss": {
        "hintName": "The Darkness",
    },
    "sewer": {
        "hintName": "Capital Sewer",
        "isNode": True,
    },
    "sewer_ashen": {
        "hintName": "Sewer Rafters",
    },
    "sewer_royal": {
        "hintName": "Sewer Entrance",
    },
    "sewer_mohg": {
        "hintName": "Forsaken Cathedral",
    },
    "sewer_preflame": {
        "hintName": "FIXME above Frenzied Flame",
    },
    "sewer_flame": {
        "hintName": "FIXME Frenzied Flame",
    },
    "sewer_catacombs": {
        "hintName": "Leyndell Catacombs",
    },
    "sewer_catacombs_boss": {
        "hintName": "Leyndell Tomb",
    },
    "deeproot_start": {
        "hintName": "FIXME Upper Deeproot",
    },
    "liurnia_loretta": {
        "hintName": "Moongazing Grounds",
    },
    "liurnia_manor": {
        "hintName": "FIXME Caria Manor",
    },
    "liurnia_postmanor": {
        "hintName": "Caria Estate",
        "isNode": True,
    },
    "liurnia_postmanor_evergaol": {
        "hintName": "Royal Evergaol",
    },
    "caelid_redmane": {
        "hintName": "FIXME Redmane Castle",
    },
    "caelid_redmane_boss": {
        "hintName": "Redmane Plaza",
    },
    "caelid_redmane_postboss": {
        "hintName": "Redmane Chapel",
        "isNode": True,
    },
    "caelid_preradahn": {
        "hintName": "Redmane Beach",
        "noLots": True,
    },
    "caelid_radahn": {
        "hintName": "Wailing Dunes",
    },
    "caelid_tower": {
        "hintName": "Caelid Tower",
        "isNode": True,
    },
    "caelid_tower_boss": {
        "hintName": "Caelid Tower Chamber",
    },
    "caelid_tower_postboss": {
        "hintName": "Caelid Tower Vault",
    },
    "caelid_tower_inner": {
        "hintName": "Caelid Tower Apex",
    },
    "siofrabank_prenokron": {
        "hintName": "Nokron Entrance",
    },
    "siofrabank_nokron": {
        "hintName": "Nokron",
    },
    "siofra_nokron_mimic": {
        "hintName": "Nokron Temple",
    },
    "siofra_nokron": {
        "hintName": "Nokron Woods",
        "isNode": True,
    },
    "siofra_nokron_grounds": {
        "hintName": "Night's Sacred Ground",
    },
    "siofra_nokron_aqueduct": {
        "hintName": "Siofra Aqueduct",
    },
    "siofra_nokron_aboveaqueduct": {
        "hintName": "Aqueduct Spill",
        "noLots": True
    },
    "siofra_nokron_gargoyles": {
        "hintName": "Waterfall Basin",
        "isNode": True,
    },
    "siofra_nokron_preboss": {
        "hintName": "Nokron Grotto",
        "noLots": True
    },
    "siofra_nokron_boss": {
        "hintName": "Nokron Lair",
    },
    "deeproot": {
        "hintName": "Deeproot Depths",
        "isNode": True,
    },
    "deeproot_boss": {
        "hintName": "Godwyn's Rest",
    },
    # ignore this area, it's a non-randomized part of Fia's quest
    # "deeproot_dream": {
    #     "hintName": "Deathbed Dream",
    # },
    "liurnia_tower": {
        "hintName": "Inverted Study Hall",
    },
    "liurnia_tower_inner": {
        "hintName": "Liurnia Tower",
    },
    "gelmir": {
        "hintName": "FIXME Mt. Gelmir",
    },
    "volcano_predoor": {
        "hintName": "Manor Entrance",
    },
    "volcano": {
        "hintName": "Volcano Manor",
    },
    "volcano_drawingroom": {
        "hintName": "Drawing Rooms",
    },
    "volcano_pretown": {
        "hintName": "Prison Church",
    },
    "volcano_town": {
        "hintName": "Prison Town",
        "isNode": True,
    },
    "volcano_temple": {
        "hintName": "Eiglay Temple",
        "isNode": True,
    },
    "volcano_posttemple": {
        "hintName": "FIXME Caldera Hall",
    },
    "volcano_posttemple_elevator": {
        "hintName": "Eiglay Lift",
    },
    "volcano_hallway": {
        "hintName": "Manor Attic",
        "isNode": True,
    },
    "volcano_sendinggate": {
        "hintName": "FIXME Caldera Hall throne room",
    },
    "volcano_pathway": {
        "hintName": "Audience Pathway",
        "noLots": True,
    },
    "volcano_rykard": {
        "hintName": "Serpent's Lair",
    },
    "volcano_abductors": {
        "hintName": "Inquisitor's Lair",
    },
    "volcano_postabductors": {
        "hintName": "Inquisitor's Passage",
        "noLots": True,
    },
    "outskirts_sealedtunnel": {
        "hintName": "Sealed Tunnel",
    },
    "outskirts_sealedtunnel_preboss": {
        "hintName": "Sealed Depths",
    },
    "outskirts_sealedtunnel_boss": {
        "hintName": "Sealed Lair",
    },
    "altus_tower": {
        "hintName": "Altus Tower",
    },
    "ainsel": {
        "hintName": "FIXME Ainsel Main",
    },
    "lakeofrot": {
        "hintName": "FIXME Lake of Rot",
    },
    "ainsel_preboss": {
        "hintName": "Ainsel Grotto",
        "noLots": True,
    },
    "ainsel_boss": {
        "hintName": "Ainsel Lair",
    },
    "ainsel_postboss": {
        "hintName": "Deep Ainsel Well",
        "noLots": True,
    },
    "moonlight": {
        "hintName": "Moonlight Altar",
    },
    "moonlight_evergaol": {
        "hintName": "Ringleader's Evergaol",
    },
    "mountaintops_start": {
        "hintName": "Forbidden Lands",
        "isNode": True
    },
    "mountaintops": {
        "hintName": "FIXME Mountaintops",
    },
    "mountaintops_evergaol": {
        "hintName": "Contender's Evergaol",
    },
    "mountaintops_sol": {
        "hintName": "FIXME Castle Sol",
    },
    "mountaintops_sol_boss": {
        "hintName": "Sol Rooftop",
    },
    "mountaintops_sol_postboss": {
        "hintName": "Sol Keep",
    },
    "flamepeak": {
        "hintName": "FIXME Flame Peak",
    },
    "flamepeak_firegiant": {
        "hintName": "Giants' Forge",
        "isNode": True
    },
    "farumazula_prestart": {
        "hintName": "Beast Grave",
    },
    "farumazula_start": {
        "hintName": "Beast Grave Depths",
    },
    "farumazula_temple": {
        "hintName": "Dragon Temple",
        "isNode": True,
    },
    "farumazula_transept": {
        "hintName": "Temple Transept",
        "noLots": True,
    },
    "farumazula_balcony": {
        "hintName": "Temple Balcony",
        "noLots": True,
    },
    "farumazula_godskinduo": {
        "hintName": "Temple Altar",
        "isNode": True,
    },
    "farumazula": {
        "hintName": "Farum Azula",
        "isNode": True,
    },
    "farumazula_lift": {
        "hintName": "Upper Azula",
    },
    "farumazula_maliketh": {
        "hintName": "Azula Rotunda",
    },
    "farumazula_placidusax": {
        "hintName": "Heart of the Tempest",
    },
    "farumazula_limited": {
        "hintName": "Azula Outskirts",
    },
    "siofra_limited": {
        "hintName": "Nokron Bridge",
    },
    "snowfield_hiddenpath": {
        "hintName": "Hidden Path",
        "isNode": True,
    },
    "snowfield_hiddenpath_boss": {
        "hintName": "Hidden Tomb",
    },
    "snowfield_rold": {
        "hintName": "FIXME Hidden Lift",
        "noLots": True,
    },
    "snowfield_prehiddenpath": {
        "hintName": "FIXME Hidden Lift door",
        "noLots": True,
    },
    "snowfield": {
        "hintName": "Snowfield",
        "isNode": True,
    },
    "snowfield_evergaol": {
        "hintName": "Ordina Evergaol",
    },
    "haligtree": {
        "hintName": "Haligtree",
    },
    "haligtree_loretta": {
        "hintName": "Haligtree Promenade",
    },
    "haligtree_postloretta": {
        "hintName": "FIXME Elphael entrance",
    },
    "haligtree_elphael": {
        "hintName": "FIXME Elphael",
    },
    "haligtree_malenia": {
        "hintName": "Haligtree Roots",
    },
    "isolated_tower": {
        "hintName": "Isolated Tower",
    },
    "mohgwyn": {
        "hintName": "Mohgwyn Palace",
    },
    "mohgwyn_boss": {
        "hintName": "Mohgwyn Throne",
        "isNode": True,
    },
    "mohgwyn_postboss": {
        "hintName": "Mohgwyn Balcony",
        "noLots": True,
    },
    "leyndell2": {
        "hintName": "Ashen Leyndell",
        "isNode": True,
    },
    "leyndell2_pretower": {
        "hintName": "Ashen Leyndell East",
    },
    "leyndell2_divinebridge": {
        "hintName": "Divine Bridge",
    },
    "leyndell2_sanctuaryside": {
        "hintName": "Ashen Portico",
        # "noLots": True,
    },
    "leyndell2_sanctuary": {
        "hintName": "Ashen Sanctuary",
        "isNode": True,
    },
    "leyndell2_sanctuaryback": {
        "hintName": "Ashen Balcony",
        "isNode": True,
    },
    "leyndell2_bedchamber": {
        "hintName": "Ashen Bedchamber",
        "isNode": True,
    },
    "leyndell2_throne": {
        "hintName": "Ashen Throne",
    },
    # ignore these areas, the burning the erdtree requirement is already
    # implied and the item hints for the great runes are sufficient
    # "leyndell2_erdtree": {
    #     "hintName": "Ashen Erdtree",
    #     "noLots": True,
    # },
    # "erdtree": {
    #     "hintName": "Erdtree's Core",
    # },
    "peninsula_tombswardcatacombs": {
        "hintName": "Tombsward Catacombs",
    },
    "peninsula_tombswardcatacombs_boss": {
        "hintName": "Tombsward Tomb",
    },
    "peninsula_impalerscatacombs": {
        "hintName": "Impaler's Catacombs",
    },
    "peninsula_impalerscatacombs_boss": {
        "hintName": "Impaler's Tomb",
    },
    "limgrave_stormfootcatacombs": {
        "hintName": "Stormfoot Catacombs",
    },
    "limgrave_stormfootcatacombs_boss": {
        "hintName": "Stormfoot Tomb",
    },
    "liurnia_roadsendcatacombs": {
        "hintName": "Road's End Catacombs",
    },
    "liurnia_roadsendcatacombs_boss": {
        "hintName": "Road's End Tomb",
    },
    "limgrave_murkwatercatacombs": {
        "hintName": "Murkwater Catacombs",
    },
    "limgrave_murkwatercatacombs_boss": {
        "hintName": "Murkwater Tomb",
    },
    "liurnia_blackknifecatacombs": {
        "hintName": "Black Knife Catacombs",
        "isNode": True,
    },
    "liurnia_blackknifecatacombs_boss": {
        "hintName": "Black Knife Tomb",
    },
    "liurnia_blackknifecatacombs_boss2": {
        "hintName": "Black Knife Chapel",
    },
    "liurnia_cliffbottomcatacombs": {
        "hintName": "Cliffbottom Catacombs",
    },
    "liurnia_cliffbottomcatacombs_boss": {
        "hintName": "Cliffbottom Tomb",
    },
    "gelmir_wyndhamcatacombs": {
        "hintName": "Wyndham Catacombs",
    },
    "gelmir_wyndhamcatacombs_boss": {
        "hintName": "Wyndham Tomb",
    },
    "altus_grave": {
        "hintName": "Sainted Grave",
    },
    "altus_grave_boss": {
        "hintName": "Sainted Tomb",
    },
    "gelmir_grave": {
        "hintName": "Gelmir Grave",
    },
    "gelmir_grave_boss": {
        "hintName": "Gelmir Tomb",
    },
    "outskirts_grave": {
        "hintName": "Auriza Grave",
    },
    "outskirts_grave_boss": {
        "hintName": "Auriza Tomb",
    },
    "stormhill_catacombs": {
        "hintName": "Deathtouched Catacombs",
    },
    "stormhill_catacombs_boss": {
        "hintName": "Deathtouched Tomb",
    },
    "altus_catacombs": {
        "hintName": "Unsightly Catacombs",
    },
    "altus_catacombs_boss": {
        "hintName": "Unsightly Tomb",
    },
    "outskirts_sidetomb": {
        "hintName": "Auriza Entrance",
        "isNode": True,
        "noLots": True,
    },
    "outskirts_sidetomb_hallway": {
        "hintName": "Auriza Hall",
        "isNode": True,
        "noLots": True,
    },
    "outskirts_sidetomb_upper": {
        "hintName": "Auriza Gallery",
        "isNode": True,
        "noLots": True,
    },
    "outskirts_sidetomb_jail": {
        "hintName": "Auriza Gaol",
    },
    "outskirts_sidetomb_dupeentrance": {
        "hintName": "Auriza Sham Entrance",
    },
    "outskirts_sidetomb_dupehallway": {
        "hintName": "Auriza Sham Hall",
        "isNode": True,
    },
    "outskirts_sidetomb_dupeupper": {
        "hintName": "Auriza Sham Gallery",
    },
    "outskirts_sidetomb_dupejail": {
        "hintName": "Auriza Sham Gaol",
    },
    "outskirts_sidetomb_boss": {
        "hintName": "Auriza Side Tomb",
    },
    "caelid_erdtreecatacombs": {
        "hintName": "Minor Erdtree Catacombs",
    },
    "caelid_erdtreecatacombs_boss": {
        "hintName": "Minor Erdtree Tomb",
    },
    "caelid_catacombs": {
        "hintName": "Caelid Catacombs",
    },
    "caelid_catacombs_boss": {
        "hintName": "Caelid Tomb",
    },
    "caelid_wardead": {
        "hintName": "War-Dead Catacombs",
    },
    "caelid_wardead_boss": {
        "hintName": "War-Dead Tomb",
    },
    "flamepeak_grave": {
        "hintName": "Conquering Grave",
    },
    "flamepeak_grave_boss": {
        "hintName": "Conquering Tomb",
    },
    "mountaintops_catacombs": {
        "hintName": "Giants' Catacombs",
    },
    "mountaintops_catacombs_boss": {
        "hintName": "Giants' Tomb",
    },
    "snowfield_catacombs": {
        "hintName": "Snowfield Catacombs",
    },
    "snowfield_catacombs_boss": {
        "hintName": "Snowfield Tomb",
    },
    "limgrave_murkwatercave": {
        "hintName": "Murkwater Cave",
    },
    "limgrave_murkwatercave_boss": {
        "hintName": "Murkwater Lair",
    },
    "peninsula_earthborecave": {
        "hintName": "Earthbore Cave",
    },
    "peninsula_earthborecave_boss": {
        "hintName": "Earthbore Lair",
    },
    "peninsula_tombswardcave": {
        "hintName": "Tombsward Cave",
    },
    "peninsula_tombswardcave_boss": {
        "hintName": "Tombsward Lair",
    },
    "limgrave_grovesidecave": {
        "hintName": "Groveside Cave",
    },
    "limgrave_grovesidecave_boss": {
        "hintName": "Groveside Lair",
    },
    "liurnia_stillwatercave": {
        "hintName": "Stillwater Cave",
    },
    "liurnia_stillwatercave_boss": {
        "hintName": "Stillwater Lair",
    },
    "liurnia_lakesidecave": {
        "hintName": "Lakeside Cave",
    },
    "liurnia_lakesidecave_boss": {
        "hintName": "Lakeside Lair",
    },
    "liurnia_academycave": {
        "hintName": "Academy Cave",
    },
    "liurnia_academycave_boss": {
        "hintName": "Academy Lair",
    },
    "gelmir_seethewatercave": {
        "hintName": "Seethewater Cave",
    },
    "gelmir_seethewatercave_boss": {
        "hintName": "Seethewater Lair",
    },
    "gelmir_volcanocave": {
        "hintName": "Volcano Cave",
    },
    "gelmir_volcanocave_boss": {
        "hintName": "Volcano Lair",
    },
    "dragonbarrow_cave": {
        "hintName": "Dragonbarrow Cave",
    },
    "dragonbarrow_cave_boss": {
        "hintName": "Dragonbarrow Lair",
    },
    "dragonbarrow_selliahideaway": {
        "hintName": "Sellia Hideaway",
    },
    "dragonbarrow_selliahideaway_boss": {
        "hintName": "Hideaway Lair",
    },
    "snowfield_cave": {
        "hintName": "Forlorn Cave",
    },
    "snowfield_cave_boss": {
        "hintName": "Forlorn Lair",
    },
    "limgrave_highroadcave": {
        "hintName": "Highroad Cave",
    },
    "limgrave_highroadcave_boss": {
        "hintName": "Highroad Lair",
    },
    "altus_grotto": {
        "hintName": "Perfumer's Grotto",
    },
    "altus_grotto_boss": {
        "hintName": "Perfumer's Lair",
    },
    "altus_sagescave": {
        "hintName": "Sage's Cave",
        "isNode": True,
    },
    "altus_sagescave_boss": {
        "hintName": "Sage's Lair",
    },
    "altus_sagescave_boss2": {
        "hintName": "Sage's Hidden Lair",
    },
    "caelid_abandonedcave_start": {
        "hintName": "Abandoned Passage",
        "noLots": True,
    },
    "caelid_abandonedcave": {
        "hintName": "Abandoned Cave",
    },
    "caelid_abandonedcave_boss": {
        "hintName": "Abandoned Lair",
    },
    "caelid_gaolcave": {
        "hintName": "Gaol Cave",
    },
    "caelid_gaolcave_preboss": {
        "hintName": "Gaol Shaft",
        "noLots": True,
    },
    "caelid_gaolcave_boss": {
        "hintName": "Gaol Lair",
    },
    "caelid_gaolcave_postboss": {
        "hintName": "Gaol Cliff",
    },
    "mountaintops_cave": {
        "hintName": "Spiritcaller Cave",
    },
    "mountaintops_cave_boss": {
        "hintName": "Spiritcaller Lair",
    },
    "peninsula_tunnel": {
        "hintName": "Morne Tunnel",
    },
    "peninsula_tunnel_boss": {
        "hintName": "Morne Lair",
    },
    "limgrave_tunnels": {
        "hintName": "Limgrave Tunnels",
    },
    "limgrave_tunnels_boss": {
        "hintName": "Limgrave Lair",
    },
    "liurnia_tunnel": {
        "hintName": "Lucaria Tunnel",
    },
    "liurnia_tunnel_boss": {
        "hintName": "Lucaria Lair",
    },
    "altus_oldtunnel": {
        "hintName": "Old Altus Tunnel",
    },
    "altus_oldtunnel_boss": {
        "hintName": "Old Altus Lair",
    },
    "altus_tunnel": {
        "hintName": "Altus Tunnel",
    },
    "altus_tunnel_boss": {
        "hintName": "Altus Lair",
    },
    "caelid_gaeltunnel_start": {
        "hintName": "Gael Shaft",
    },
    "caelid_gaeltunnel": {
        "hintName": "Gael Tunnel",
        "isNode": True,
    },
    "caelid_gaeltunnel_boss": {
        "hintName": "Gael Lair",
    },
    "caelid_gaeltunnel_rear": {
        "hintName": "Gael Tunnel Rear",
        "noLots": True,
    },
    "caelid_selliatunnel": {
        "hintName": "Sellia Tunnel",
        "isNode": True,
    },
    "caelid_selliatunnel_boss": {
        "hintName": "Sellia Lair",
    },
    "snowfield_tunnel": {
        "hintName": "Anix Tunnel",
    },
    "snowfield_tunnel_boss": {
        "hintName": "Anix Lair",
    },
}
