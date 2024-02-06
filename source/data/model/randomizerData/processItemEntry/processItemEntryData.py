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

staticContainers = [
    "Book Imp",
    "Caravan Chest",
    "Chest",
    "Chest with Chain",
    "Corpse",
    "Corpse, Shiny Item",
    "Crystal Tear Basin",
    "Glowing Statue",
    "Golden Veil Corpse",
    "Greataxe Caravan Chest",
    "Great Rune",
    "Lidded Farum Azula Chest",
    "Lidded River Chest",
    "Open Coffin",
    "Painting",
    "Robed Corpse",
    "Robed Corpse, Shiny Item",
    "Shiny Item",
    "Smouldering Corpse",
    "Snowy Open Coffin",
    "Stone Chest"
]

duplicateLocationNames = [
    "Artist's Shack",
    "Hallowhorn Grounds",
    "Highway Lookout Tower",
    "Isolated Merchant's Shack",
    "the Minor Erdtree",
    "Uhl Palace Ruins"
]

npcNames = {
    "Abandoned Merchant": "Abandoned Merchant",
    "Albinauric Archer, Shiny Item": "Latenna the Albinauric",
    "Alexander, Warrior Jar": "Alexander, Warrior Jar",
    "Altar of Dragon Communion": "Altar of Dragon Communion",
    "Azur": "Primeval Sorcerer Azur",
    "Beast Clergyman": "Gurranq, Beast Clergyman",
    "Blackguard": "Blackguard",
    "Blackguard, Shiny Item": "Blackguard",
    "Blaidd": "Blaidd the Half-Wolf",
    "Blaidd the Half-Wolf": "Blaidd the Half-Wolf",
    "Boc the Seamster": "Boc the Seamster",
    "Brother Corhyn": "Brother Corhyn",
    "Castellan Jerren": "Castellan Jerren",
    "Cathedral of Dragon Communion": "Altar of Dragon Communion",
    "D, Beholder of Death": "D, Beholder of Death",
    # just the Inseperable Sword
    "D, Hunter of the Dead": "D, Hunter of the Dead",
    "Dung Eater": "Dung Eater",
    # Sacrificial Twig
    "Edgar": "Castellan Edgar",
    # Shabriri Grape
    "Edgar the Revenger": "Castellan Edgar",
    # Banished Knight's Halberd +8
    "Edgar, Shiny Item": "Castellan Edgar",
    "Ensha of the Royal Remains": "Ensha of the Royal Remains",
    "Fia, Deathbed Companion": "Fia, Deathbed Companion",
    "Finger Reader Enia": "Finger Reader Enia",
    "Gatekeeper Gostoc": "Gatekeeper Gostoc",
    "Hermit Merchant": "Hermit Merchant",
    "Imprisoned Merchant": "Imprisoned Merchant",
    "Irina of Morne": "Irina of Morne",
    "Isolated Merchant": "Isolated Merchant",
    "Jar-Bairn": "Jar-Bairn",
    "Kenneth Haight, Limgrave Heir": "Kenneth Haight, Limgrave Heir",
    # his armor and Warmaster's Shack shop inventory
    "Knight Bernahl": "Knight Bernahl",
    # Devourer's Scepter, Letter to Bernahl, and his Volcano Manor shop items
    "Knight Bernahl, Recusant Bernahl": "Knight Bernahl",
    # Gelmir's Fury
    "Knight Bernahl, Recusant Bernahl, Shiny Item": "Knight Bernahl",
    "Knight Diallos": "Knight Diallos",
    "Greatjar": "The Great-Jar",
    "Latenna the Albinauric": "Latenna the Albinauric",
    "Lightseeker Hyetta": "Lightseeker Hyetta",
    "Lusat": "Master Lusat",
    "Man-Serpent, Rya the Scout": "Rya the Scout",
    "Melina": "Melina",
    # only entry in spoilers seems to be Kale replacing glowstone, which isn't
    # there?
    "Merchant": "Merchant",
    "Merchant Kalé": "Merchant Kalé",
    "Millicent": "Millicent",
    "Miriel, Pastor of Vows": "Miriel, Pastor of Vows",
    "Nepheli Loux, Warrior": "Nepheli Loux, Warrior",
    "Nomadic Merchant": "Nomadic Merchant",
    "Old Albus": "Old Albus",
    "Patches": "Patches",
    "Pidia, Carian Servant": "Pidia, Carian Servant",
    "Preceptor Seluvis": "Preceptor Seluvis",
    # Carian Inverted Statue, Dark Moon Greatsword
    "Ranni the Witch": "Ranni the Witch",
    # Blasphemous Claw
    "Recusant Bernahl": "Knight Bernahl",
    # Lone Wolf Ashes
    "Renna the Witch": "Ranni the Witch",
    "Roderika, Spirit Tuner": "Roderika, Spirit Tuner",
    # Zorayas's Letter
    "Rya the Scout": "Rya the Scout",
    # Daedicar's Woe
    "Rya the Scout, Shiny Item": "Rya the Scout",
    "Sage Gowry": "Sage Gowry",
    # Ronin set
    "Shabriri": "Yura, Hunter of Bloody Fingers",
    # Smithing Stone [5] reward for helping with invasion
    "Shabriri, Yura, Hunter of Bloody Fingers":
        "Yura, Hunter of Bloody Fingers",
    # rewards for Volcano Manor assignments
    "Shiny Item, Tanith": "Tanith, Volcano Manor Proprietress",
    # Festering Bloody Finger 6x, Varré's Bouquet
    "Shiny Item, White Mask Varre": "White Mask Varré",
    # Nagakiba
    "Shiny Item, Yura, Hunter of Bloody Fingers":
        "Yura, Hunter of Bloody Fingers",
    "Sir Gideon Ofnir, the All-Knowing": "Sir Gideon Ofnir, the All-Knowing",
    "Smithing Master Iji": "Smithing Master Iji",
    "Sorcerer Rogier": "Sorcerer Rogier",
    "Sorcerer Thops": "Sorcerer Thops",
    "Sorceress Sellen": "Sorceress Sellen",
    # Tonic of Forgetfulness, Consort's Mask, Drawing-Room Key
    "Tanith, Volcano Manor Proprietress": "Tanith, Volcano Manor Proprietress",
    "The Noble Goldmask": "The Noble Goldmask",
    "Twin Maiden Husks": "Twin Maiden Husks",
    # Bloody Finger, Pureblood Knight's Medal, Festering Bloody Finger 5x
    "White Mask Varre": "White Mask Varré",
    # Lord of Blood's Favor
    "White Mask Varré": "White Mask Varré"
}

duplicateContainerNames = {
    "Abandoned Merchant": "Abandoned Merchant",
    "Blackguard": "Blackguard",
    "Boc the Seamster": "Boc the Seamster",
    "Brother Corhyn": "Brother Corhyn",
    "Castellan Jerren": "Castellan Jerren",
    "Cathedral of Dragon Communion": "Altar of Dragon Communion",
    "D, Beholder of Death": "D, Beholder of Death",
    "D, Hunter of the Dead": "D, Hunter of the Dead",
    "Dung Eater": "Dung Eater",
    "Edgar the Revenger": "Edgar the Revenger",
    "Finger Reader Enia": "Finger Reader Enia",
    "Gatekeeper Gostoc": "Gatekeeper Gostoc",
    "Hermit Merchant": "Hermit Merchant",
    "Imprisoned Merchant": "Imprisoned Merchant",
    "Isolated Merchant": "Isolated Merchant",
    "Knight Bernahl": "Knight Bernahl",
    "Knight Diallos": "Knight Diallos",
    "Lightseeker Hyetta": "Lightseeker Hyetta",
    # Kale also shows up in the container list for items sold by Isolated
    # Merchant and Nomadic Merchant as well, but they come first, so normal
    # processing should get the correct order in all cases
    "Merchant Kalé": "Merchant Kalé",
    "Merchant KalÃ©": "Merchant Kalé",  # because Windows is garbage
    "Millicent": "Millicent",
    "Miriel, Pastor of Vows": "Miriel, Pastor of Vows",
    "Nomadic Merchant": "Nomadic Merchant",
    "Patches": "Patches",
    "Pidia, Carian Servant": "Pidia, Carian Servant",
    "Preceptor Seluvis": "Preceptor Seluvis",
    "Renna the Witch": "Renna the Witch",
    # special case in Mohgwyn Palace where the Golden Seed  is listed as having
    # multiple containers. there are actually two locations for the Golden Seed,
    # one under a gold tree in the blood swamp and one on a corpse on a ledge in
    # the Mohgwyn Dynasty Mausoleum, for our purposes we're only going to hint
    # at the swamp location since it's more visible
    "Robed Corpse": "Shiny Item",
    "Roderika, Spirit Tuner": "Roderika, Spirit Tuner",
    "Sage Gowry": "Sage Gowry",
    "Sir Gideon Ofnir, the All-Knowing": "Sir Gideon Ofnir, the All-Knowing",
    "Smithing Master Iji": "Smithing Master Iji",
    "Sorcerer Rogier": "Sorcerer Rogier",
    "Sorcerer Thops": "Sorcerer Thops",
    "Sorceress Sellen": "Sorceress Sellen",
    "Tanith, Volcano Manor Proprietress": "Tanith, Volcano Manor Proprietress",
}
