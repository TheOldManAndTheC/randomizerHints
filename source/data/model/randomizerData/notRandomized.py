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

# items that aren't randomized and can be skipped.  need to check this after
# updates
notRandomized = [
    "Map: ",  # Map pieces aren't randomized
    "Flask of ",  # Flasks aren't randomized
    # The bloodied version of the Lord of Blood's Favor is not randomized
    "Lord of Blood's Favor in Bellum Highway: Acquired by using the Lord of "
    "Blood's Favor",
    # Special NPC equipment like Edgar's Halberd, Rogier's Rapier, and
    # Blackguard's Iron Ball, and other unknown goods that aren't
    # randomized.  Probably like this because they have Ashes of War
    # attached to them.
    # Rogier's Rapier +8, Banished Knight's Halberd +8, Nagakiba, Iron Ball are
    # all named and randomized as of randomizer 0.7.  The other items are
    # unknown
    "?ITEM?",
    "NPC Equipment",
    # NPC bell bearings aren't randomized
    "Abandoned Merchant's Bell Bearing",
    "Bernahl's Bell Bearing",
    "Blackguard's Bell Bearing",
    "Corhyn's Bell Bearing",
    "D's Bell Bearing",
    "Gostoc's Bell Bearing",
    "Gowry's Bell Bearing",
    "Hermit Merchant's Bell Bearing [1]",
    "Hermit Merchant's Bell Bearing [2]",
    "Hermit Merchant's Bell Bearing [3]",
    "Iji's Bell Bearing",
    "Imprisoned Merchant's Bell Bearing",
    "Isolated Merchant's Bell Bearing [1]",
    "Isolated Merchant's Bell Bearing [2]",
    "Isolated Merchant's Bell Bearing [3]",
    "Kalé's Bell Bearing",
    "Miriel's Bell Bearing",
    "Nomadic Merchant's Bell Bearing [1]",
    "Nomadic Merchant's Bell Bearing [10]",
    "Nomadic Merchant's Bell Bearing [2]",
    "Nomadic Merchant's Bell Bearing [3]",
    "Nomadic Merchant's Bell Bearing [4]",
    "Nomadic Merchant's Bell Bearing [5]",
    "Nomadic Merchant's Bell Bearing [6]",
    "Nomadic Merchant's Bell Bearing [7]",
    "Nomadic Merchant's Bell Bearing [8]",
    "Nomadic Merchant's Bell Bearing [9]",
    "Patches' Bell Bearing",
    "Pidia's Bell Bearing",
    "Rogier's Bell Bearing",
    "Sellen's Bell Bearing",
    "Seluvis's Bell Bearing",
    "Thops's Bell Bearing",
    # activated great runes aren't randomized:
    # need the extra text to differentiate them from the unactivated entries
    "Godrick's Great Rune in Divine Tower of Limgrave: Activating Godrick's "
    "Great Rune",
    "Malenia's Great Rune in Isolated Divine Tower: Activating Malenia's "
    "Great Rune",
    "Mohg's Great Rune in Divine Tower of East Altus: Activating Mohg's "
    "Great Rune",
    "Morgott's Great Rune in Divine Tower of East Altus: Activating Morgott's "
    "Great Rune",
    "Radahn's Great Rune in Divine Tower of Caelid: Activating Radahn's "
    "Great Rune",
    "Rykard's Great Rune in Divine Tower of West Altus: Activating Rykard's "
    "Great Rune",
    # other non-randomized items:
    "Crafting Kit",
    "Lantern",
    "Serpent-Hunter",
    "Radiant Baldachin's Blessing",
    "Spectral Steed Whistle",
    "Spirit Calling Bell",
    "Tarnished's Wizened Finger",
    "Whetstone Knife",
    # Some enemies that aren't randomized
    "Merciless Chariot",
    "Greyoll",
    "Balloon",
    "Ensha of the Royal Remains"
]
