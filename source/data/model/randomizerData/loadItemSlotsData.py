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

itemSlotsSkipLines = [
    "  - Unique location", "  - Shop item in"
]

itemSlotsBasicLines = {
    "  Area: ": "area",
    "  FullArea: ": "fullArea",
    "  Text: ": "text",
    "  Tags: ": "tags",
    "  QuestReqs: ": "questReqs",
    "  Comment: ": "comment",
    "  Event: ": "event",
    "  Until: ": "until"
}

lotTypes = [
    "shop", "lot", "enemy lot"
]

lotAppends = {
    " (Good ": {
        "key": "good",
        "delimiter": ")"
    },
    "Good ": {
        "key": "good",
        "delimiter": "*"
    },
    "Equip ": {
        "key": "equip",
        "delimiter": "*"
    },
    "Custom ": {
        "key": "equip"
    },
    "Weapon ": {
        "key": "weapon"
    }
}

containerTypes = [
    "event asset", "event enemy", "asset", "enemy", "event", "ESD",
    "unknown entity event", "Melina", "unused ESD", "unknown"
]

duplicateMaps = [
    # items that exist in both normal and ashen capital
    ["m11_05_00_00", "m11_00_00_00"],
    # some edge cases where two map IDs can point at the same place
    # Borealis the Freezing Fog
    ["m60_13_14_02", "m60_54_56_00"],
    # Lansseax (Rampartside Path)
    ["m60_37_51_00", "m60_41_52_00"],
    # snowfield Night's Cavalry
    ["m60_12_13_02", "m60_48_55_00"],
    # scarab south of Ordina
    ["m60_24_28_01", "m60_48_56_00"],
    # Limgrave troll cart (non-meteor map)
    ["m60_11_09_12", "m60_11_09_02"],
    # Draconic Tree Sentinel (non-ashen map)
    ["m60_45_52_10", "m60_45_52_00"]
]

# items with identical names with separate good IDs
goods = {
    "8174": "Academy Glintstone Key (Thops)",
    "8127": "Letter from Volcano Manor (Istvan)",
    "8132": "Letter from Volcano Manor (Rileigh)",
    "8975": "Unalloyed Gold Needle (Broken)",
    "8976": "Unalloyed Gold Needle (Fixed)",
    "8196": "Unalloyed Gold Needle (Milicent)",
    "8155": "Lord of Blood's Favor (Blooded)"
    # "191": "Godrick's Great Rune (Activated)",
    # "196": "Malenia's Great Rune (Activated)",
    # "195": "Mohg's Great Rune (Activated)",
    # "193": "Morgott's Great Rune (Activated)",
    # "192": "Radahn's Great Rune (Activated)",
    # "194": "Rykard's Great Rune (Activated)",
}

landmarkTypes = [
    "Church", "Divine Tower", "Erdtree", "Evergaol", "Fort",
    "Gate", "Grave", "Marker", "Other", "Pasture", "Red Mark",
    "Rise", "Ruins", "Shack", "Tower", "Underground",
    "Underground Ruins", "Well"
]

books = [
    # These are the only books/scrolls/bearings that are currently randomized
    "Academy Scroll",
    "Ancient Dragon Prayerbook",
    "Assassin's Prayerbook",
    "Bone Peddler's Bell Bearing",
    "Conspectus Scroll",
    "Dragon Cult Prayerbook",
    "Fire Monk's Prayerbook",
    "Fire Monks' Prayerbook",
    "Giant's Prayerbook",
    "Godskin Prayerbook",
    "Golden Order Principia",
    "Gravity Stone Peddler's Bell Bearing",
    "Meat Peddler's Bell Bearing",
    "Medicine Peddler's Bell Bearing",
    "Royal House Scroll",
    "Two Fingers' Prayerbook",
]

otherBooks = {
    # these items are either activated by their paintings, or available from
    # trading remembrances, so set them to be associated with those items like
    # a book
    "Warhawk Ashes": "\"Prophecy\" Painting",
    "Fire's Deadly Sin": "\"Flightless Bird\" Painting",
    "Juvenile Scholar Cap": "\"Resurrection\" Painting",
    "Harp Bow": "\"Champion's Song\" Painting",
    "Incantation Scarab": "\"Homing Instinct\" Painting",
    "Ash of War: Rain of Arrows": "\"Redmane\" Painting",
    "Greathood": "\"Sorcerer\" Painting",
    "Blasphemous Blade": "Remembrance of the Blasphemous",
    "Placidusax's Ruin": "Remembrance of the Dragonlord",
    "Fortissax's Lightning Spear": "Remembrance of the Lichdragon",
    "Dragon King's Cragblade": "Remembrance of the Dragonlord",
    "Morgott's Cursed Sword": "Remembrance of the Omen King",
    "Rennala's Full Moon": "Remembrance of the Full Moon Queen",
    "Carian Regal Scepter": "Remembrance of the Full Moon Queen",
    "Starscourge Greatsword": "Remembrance of the Starscourge",
    "Black Blade": "Remembrance of the Black Blade",
    "Rykard's Rancor": "Remembrance of the Blasphemous",
    "Marika's Hammer": "Elden Remembrance",
    "Bloodboon": "Remembrance of the Blood Lord",
    "Ash of War: Hoarah Loux's Earthshaker": "Remembrance of Hoarah Loux",
    "Hand of Malenia": "Remembrance of the Rot Goddess",
    "Mohgwyn's Sacred Spear": "Remembrance of the Blood Lord",
    "Giant's Red Braid": "Remembrance of the Fire Giant",
    "Scarlet Aeonia": "Remembrance of the Rot Goddess",
    "Sacred Relic Sword": "Elden Remembrance",
    "Maliketh's Black Blade": "Remembrance of the Black Blade",
    "Ash of War: Waves of Darkness": "Remembrance of the Naturalborn",
    "Death Lightning": "Remembrance of the Lichdragon",
    "Grafted Dragon": "Remembrance of the Grafted",
    "Burn, O Flame!": "Remembrance of the Fire Giant",
    "Ancestral Spirit's Horn": "Remembrance of the Regal Ancestor",
    "Bastard's Stars": "Remembrance of the Naturalborn",
    "Axe of Godfrey": "Remembrance of Hoarah Loux",
    "Axe of Godrick": "Remembrance of the Grafted",
    "Winged Greathorn": "Remembrance of the Regal Ancestor",
    "Lion Greatbow": "Remembrance of the Starscourge",
    "Regal Omen Bairn": "Remembrance of the Omen King"
}
