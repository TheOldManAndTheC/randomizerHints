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

nearbyHints = [
    {
        "areaName": "mountaintops_start",
        "gateText": "using the Rold Medallion at Forbidden Lands",
        "hintItems": ["Rold Medallion", "Haligtree Secret Medallion (Left)",
                      "Haligtree Secret Medallion (Right)"],
        "hintName": "Engineer's Draft",
        "hintDescription": "Engineer's Draft.\nLift operation information from "
                           "a lift engineer.",
        "hintIconTypes": ["map", "book"]
    },
    {
        "areaName": "flamepeak|mountaintops|mountaintops_sol",
        "gateText": "using the Rold Medallion at Mountaintops of the Giants",
        "hintItems": ["Rold Medallion"],
        "hintName": "Hero's Tragedy",
        "hintDescription": "Hero's Tragedy.\nTale of a hero who reached the "
                           "mountaintops but perished.",
        "hintIconTypes": ["book", "scroll"]
    },
    {
        "areaName": "bellum|liurnia|liurnia_manor",
        "gateText": "using the Dectus Medallion in Bellum Highway",
        "hintItems": ["Dectus Medallion (Left)", "Dectus Medallion (Right)"],
        "hintName": "Priest's Catechism",
        "hintDescription": "Priest's Catechism.\nInstructions for the pious "
                           "to properly make pilgrimage to the Erdtree.",
        "hintIconTypes": ["book"]
    },
    {
        "areaName": "altus|altus_shaded|gelmir|outskirts",
        "gateText": "using the Dectus Medallion in Altus Plateau",
        "hintItems": ["Dectus Medallion (Left)", "Dectus Medallion (Right)"],
        "hintName": "Noble's Letter",
        "hintDescription": "Noble's Letter.\nMissive penned by a noble of "
                           "Leyndell wishing to visit the lowlands.",
        "hintIconTypes": ["note"]
    },
    {
        "areaName": "bellum|liurnia|liurnia_manor",
        "gateText": "using South Raya Lucaria Gate",
        "hintItems": ["Academy Glintstone Key"],
        "hintName": "Burgher's Document",
        "hintDescription": "Burgher's Document.\nInformation about a key to "
                           "the Academy prepared for a town official.",
        "hintIconTypes": ["book", "map", "scroll"]
    },
    {
        "areaName": "bellum|liurnia|liurnia_manor",
        "gateText": "using East Raya Lucaria Gate",
        "hintItems": ["Academy Glintstone Key"],
        "hintName": "Lucaria Messenger's Charge",
        "hintDescription": "Lucaria Messenger's Charge.\nThe location of a "
                           "key Academy messengers used on the Bellum Highway.",
        "hintIconTypes": ["note", "map", "scroll"]
    },
    {
        "areaName": "academy_entrance",
        "gateText": "using South-facing gate at Raya Lucaria Main Entrance",
        "hintItems": ["Academy Glintstone Key"],
        "hintName": "Magi's Note",
        "hintDescription": "Magi's Note.\nNote concerning the location of a "
                           "Glinstone Key.",
        "hintIconTypes": ["note", "map", "scroll"]
    },
    {
        "lotIDs": [
            "10000500",  # trap room chest
            "10000975",  # trap room
            "10000200",  # in hole in wall
            "10000210",  # exploding barrel corridor
            "10000240",  # platform below trap room door
            "10000190",  # next to locked door
            "10000180",  # NW corner of bottom room
            "10000170",  # catwalk outside turret
            "10000100",  # exterior stair landing
        ],
        "hintItems": ["Rusty Key"],
        "hintName": "The Castellan's Orders",
        "hintDescription": "The Castellan's Orders.\nA sternly worded "
                           "directive from the castellan to a lax gatekeeper.",
        "hintIconTypes": ["note"]
    },
    {
        "lotIDs": [
            "34110700",  # Study Hall invader
            "34110010",  # W of Carian Study Hall
            "34110060",  # upper gallery E of Carian Study Hall
            "34110080",  # rafter W and above Carian Study Hall
            "34110200",  # S of Carian Study Hall
        ],
        "hintItems": ["Carian Inverted Statue"],
        "hintName": "Professor's Secret",
        "hintDescription": "Professor's Secret.\nA magic teacher's hidden "
                           "relic, revealed only to accomplished pupils.",
        "hintIconTypes": ["scroll"]
    },
    # only available lot on the basin side is the boss
    {
        "lotIDs": ["10080"],
        "hintItems": ["Dark Moon Ring"],
        "hintName": "Voidfarer's Journal",
        "hintDescription": "Voidfarer's Journal.\nAccount of a void denizen, "
                           "trapped in the deepest pit by sorcery of the moon.",
        "hintIconTypes": ["note", "map"]
    },
    # use the lots in the cathedral for the altar side
    {
        "lotIDs": [
            "1035420100",
            "1035420110",
            "1035420120",
            "1035420130",
            "1035420140",
            "1035420150",
            "1035420160",
            "1035420170",
            "1035420180",
            "1035420190",
            # "1035420200",
        ],
        "hintItems": ["Dark Moon Ring"],
        "hintName": "Moon Priestess's Scripture",
        "hintDescription": "Moon Priestess's Scripture.\nScripture about the "
                           "seal of the Dark Moon.",
        "hintIconTypes": ["scroll", "book"]
    },
    # put all the key hints in the chest at the top
    {
        "lotIDs": ["1033470020"],
        "hintItems": ["Imbued Sword Key"],
        "hintNumber": 3,
        "hintName": "The Fargate Wright's Addenda",
        "hintDescription": "The Fargate Wright's Addenda.\nNotations about "
                           "the keys to the belfry gates.",
        "hintIconTypes": ["scroll"]
    }
]
