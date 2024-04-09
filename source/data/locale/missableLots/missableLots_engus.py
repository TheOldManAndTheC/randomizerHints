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

missableLots_engus = {
    # Latenna's drop at her shack, can miss this if you fight Ensha before
    # showing her Albus's right half of the medallion
    # Might also be just picking up the left half?
    # Also sometimes doesn't get awarded even if she's there
    # Latenna the Albinauric
    "104100": "Given by Latenna after meeting her with the right half of the "
              "Haligtree Secret Medallion. Can be missed if you obtain the "
              "left half first.",
    # Latenna's reward for bringing her to Apostate Derelict
    # Somber Ancient Dragon Smithing Stone
    "104110": "Given by Latenna after bringing her to Apostate Derelict. Can "
              "be missed if she dies before you meet her in Slumbering Wolf's "
              "Shack.",
    # Blaidd's gift for beating Darriwil, can be missed if you start the
    # festival before you get it. With the fog randomizer just stumbling on the
    # Wailing Dunes will be enough
    # Somber Smithing Stone [2]
    "101500": "Given by Blaidd after defeating the boss in Forlorn Hound "
              "Evergaol. Can be missed if the Radahn festival begins before "
              "you meet him in Mistwood.",
    # Baleful Shadow drop, sometimes this won't drop
    # TODO: figure out conditions for why it won't drop
    # Discarded Palace Key
    "101590": "Given by Ranni after defeating the Baleful Shadow in Ainsel "
              "River Main. Sometimes this will not be awarded.",
    # Bloody Finger Ravenmount Assassin invasion drop
    # Ash of War: Raptor of the Mists
    "1035460700": "Reward for defeating Bloody Finger Ravenmount Assassin. Can "
                  "be missed if Yura dies before you can assist him.",
    # Yura's reward for helping him with Bloody Finger invasion
    # Smithing Stone [5]
    "101610": "Given by Yura after assisting him against Bloody Finger "
              "Ravenmount Assassin. Can be missed if Yura dies before you can "
              "assist him.",
    # these two are from the big Living Pots in Jarburg that aren't randomized
    # killing them can break Jar-Bairn's quest, these lots are from
    # ItemLotParam_enemy, not sure what the randomizer ItemLotParam_map
    # equivalents are or how to find them
    # It is possible to get these without breaking Jar-Bairn's quest by getting
    # absolution, but list them here anyway since they're NPCs
    # maybe add "norandom ignore" to their itemSlots.txt entries before running
    # randomizer
    # Living Jar Shard
    "449020001": "Drop from one of the Large Living Pots in Jarburg. Can be "
                 "missed if you don't wish to kill peaceful NPCs.",
    # Raw Meat Dumpling
    "449020002": "Drop from one of the Large Living Pots in Jarburg. Can be "
                 "missed if you don't wish to kill peaceful NPCs.",
    # Living Jar Shard
    "449020011": "Drop from one of the Large Living Pots in Jarburg. Can be "
                 "missed if you don't wish to kill peaceful NPCs.",
    # Raw Meat Dumpling
    "449020012": "Drop from one of the Large Living Pots in Jarburg. Can be "
                 "missed if you don't wish to kill peaceful NPCs.",
    # Sellen and Jerren's lots, can only get one or the other
    # Ancient Dragon Smithing Stone, Jerren gift after beating Sellen
    "104000": "Given by Jerren after helping him defeat Sellen. Can be missed "
              "if you side with Sellen.",
    # Eccentric's Hood, drop from beating Jerren
    "104010": "Reward for defeating Jerren. Can be missed if you side with "
              "him.",
    # "104011", # Eccentric's Armor
    # "104012", # Eccentric's Manchettes
    # "104013", # Eccentric's Breeches
    # Glintstone Kris, gift after talking to her
    "101010": "Given by Sellen after assisting her against Jerren. Can be "
              "missed if you side with Jerren.",
    # Sellen's reward for freeing Master Lusat could be softlocked by having
    # the Sellian Sealbreaker as the reward or as Lusat's gift
    # Starlight Shards
    "101030": "Given by Sellen for finding Lusat. Can be missed if the Sellian "
              "Sealbreaker is held by Lusat or is otherwise unobtainable.",
    # Witch's Glintstone Crown, if she never turns into a mass
    # there are three lot IDs in itemslots
    "101061": "Appears near Sellen after she transforms at the end of her "
              "quest. Can be missed if you side with Jerren or are unable to "
              "obtain her reward for finding Lusat.",
    "101070": "Appears near Sellen after she transforms at the end of her "
              "quest. Can be missed if you side with Jerren or are unable to "
              "obtain her reward for finding Lusat.",
    "111001": "Appears near Sellen after she transforms at the end of her "
              "quest. Can be missed if you side with Jerren or are unable to "
              "obtain her reward for finding Lusat.",
    # Corhyn/Goldmask quest items, can miss these if the Erdtree must be burned
    # to get Law of Regression
    # Mending Rune of Perfect Order
    "4900": "Drop from Goldmask at the end of his quest. Can be missed if the "
            "Law of Regression is unobtainable before burning the Erdtree.",
    # Goldmask's Rags
    "105000": "Drop from Goldmask at the end of his quest. Can be missed if "
              "the Law of Regression is unobtainable before burning the "
              "Erdtree.",
    # "105001",  # Gold Bracelets
    # "105002",  # Gold Waistwrap
    # Rogier's Letter drop doesn't always show up?
    # TODO: test to see if failing to get the Black Knifeprint affects this
    # Rogier's Letter
    "103582": "Drop from Rogier at the end of his quest. Sometimes this won't "
              "appear.",
    # Fia's gift for giving Rogier the Black Knifeprint, can be missed if the
    # knifeprint is behind Ranni questline gated areas
    # Sacrificial Twig
    "103320": "Given by Fia for giving Rogier the Black Knifeprint. Can be "
              "missed if joining Ranni is required to get it.",
    # Possibilities:
    # Cursemark of Death dropped by Lichdragon Fortissax would be a softlock
    # for Fia's quest
    # Mending Rune of the Death-Prince
    "103350": "Drop from Fia after defeating the boss in the Deathbed Dream. "
              "Can be missed if the Cursemark of Death is held by that boss or "
              "D, Beholder of Death.",
    # Inseparable Sword
    "103410": "Drop from D, Beholder of Death at the end of his quest. Can be "
              "missed if the Cursemark of Death is held by the boss of the "
              "Deathbed Dream or D, Beholder of Death.",
    # Thops's Erudition gesture is needed to get into the Converted Fringe Tower
    # and if his Academy Glintstone Key is in there, it and any other items in
    # the same lot will be softlocked, along with the gesture itself
    # Cannon of Haima
    "1039480100": "In a chest at the top of Converted Fringe Tower. Can be "
                  "missed if the Erudition gesture is unavailable.",
    # "1039480101", # Gavel of Haima
    # Bernahl's quest, can be softlocked if Letter to Bernahl (or Istvan or
    # Rilegh) are in Ashen Leyndell
    # Raging Wolf Helm, drop from the Vargram/Wilhelm fight
    "11001985": "Reward for defeating Vargram the Raging Wolf and Errant "
                "Sorcerer Wilhelm. Can be missed if the Letter to Bernahl is "
                "unable to be obtained before defeating the final boss of "
                "Volcano Manor.",
    # "11001986", # Raging Wolf Armor
    # "11001987", # Raging Wolf Gauntlets
    # "11001989", # Raging Wolf Greaves
    # Gelmir's Fury can be obtained from his invasion if you didn't get it
    # "102910", # Gelmir's Fury, Bernahl gift after winning the fight
    # Alexander's shard talismans can't both be obtained
    # Warrior Jar Shard
    "111700": "Drop from Alexander if you kill him before finishing his quest. "
              "Can be missed if you complete his quest.",
    # Shard of Alexander
    "101740": "Drop from Alexander after finishing his quest. Can be missed if "
              "you kill him before then.",
    # "101741",  # Alexander's Innards
    # Alexander's first gift for getting ustuck can be missed if the festival
    # starts before you can get to him in Stormhill
    "101700": "Given by Alexander after freeing him from the hole in "
              "Stormhill. Can be missed if you are unable to reach him before "
              "the festival starts.",
    # Alexander's second gift for getting unstuck can be softlocked if there is
    # no way to make oil pots before he appears in Mt. Gelmir or Farum Azula
    # Exalted Flesh
    "101710": "Given by Alexander after freeing him from the hole in Liurnia. "
              "Can be missed if you are unable to make Oil Pots before he "
              "appears in Mt. Gelmir.",
    # Kenneth drops a Golden Seed, if you kill him you softlock Nepheli and
    # Gostoc
    # Golden Seed
    "112200": "Drop from Kenneth if you kill him. Can be missed if you "
              "complete his quest.",
    # Diallos drops a Numen's Rune at the end of his quest, if you can't
    # complete the first two Volcano Manor quests before defeating Rykard, it
    # can be softlocked
    # Numen's Rune
    "104512": "Drop from Diallos at the end of his quest. Can be missed if you "
              "can't complete the Volcano Manor requests before defeating the "
              "final boss of Volcano Manor.",
    # Patches' only softlockable items involve his Volcano Manor quest
    # if you can't complete the first Volcano Manor quest before defeating
    # Rykard, Letter to Patches can't be gotten, and if you can't get Letter
    # to Patches before defeating Rykard you can't get the Magma Whip
    # Candlestick
    # Letter to Patches
    "101800": "Given by Patches after completing the first Volcano Manor "
              "request. Can be missed if you can't complete the request before "
              "defeating the final boss of Volcano Manor.",
    # Magma Whip Candlestick
    "101820": "Given by Patches after completing his invasion request. Can be "
              "missed if the Letter to Patches is unobtainable before "
              "defeating the final boss of Volcano Manor.",
    # Arsenal Charm
    "104200": "Given by Nepheli in Roundtable Hold after speaking to her in "
              "Stormveil Castle. Can be missed if defeating the boss of "
              "Stormveil Castle is required to reach Stormveil Castle.",
    # Nepheli's quest reward can be softlocked if The Stormhawk King isn't
    # available until after burning the Erdtree
    # Ancient Dragon Smithing Stone
    "104220": "Given by Nepheli at the end of her quest. Can me missed if The "
              "Stormhawk King can't be obtained before burning the Erdtree.",
    # Nepheli's drops can't be obtained if you finish her quest
    # Stormhawk Axe
    "114210": "Drop from Nepheli if you kill her. Can be missed if you "
              "complete her quest.",
    # "114211", # Stormhawk Axe
    # Hyetta's drop can't be obtained if you complete her quest
    # Frenzyflame Stone 3x, drop from killing her
    # the drop from killing her and the drop from finishing her quest here
    # appear to be the same in the spoiler file, so this is not missable
    # # this has two lot IDs in itemslots
    # "110810": "Drop from Hyetta if you kill her. Can be missed if you complete "
    #           "her quest.",
    # "100891": "Drop from Hyetta if you kill her. Can be missed if you complete "
    #           "her quest.",
    # Frenzied Flame Seal, quest reward
    "100890": "Drop from Hyetta at the end of her quest. Can be missed if you "
              "kill her before then.",
    # "100891", # Frenzyflame Stone 5x, quest reward
    # Tanith's rewards can all be softlocked depending on the Volcano Manor key
    # item locations
    # Magma Shot, Istvan quest reward
    "100760": "Given by Tanith after completing the first Volcano Manor "
              "request. Can be missed if the Drawing-Room Key or the Letter "
              "from Volcano Manor (Istvan) can't be obtained before defeating "
              "the final boss of Volcano Manor.",
    # Serpentbone Blade, Rileigh quest reward
    "100770": "Given by Tanith after completing the second Volcano Manor "
              "request. Can be missed if the first request can't be completed "
              "or the Letter from Volcano Manor (Rileigh) can't be obtained "
              "before defeating the final boss of Volcano Manor.",
    # Taker's Cameo, Juno quest reward
    "100780": "Given by Tanith after completing the third Volcano Manor "
              "request. Can be missed if the second request can't be completed "
              "or the Red Letter can't be obtained before defeating the final "
              "boss of Volcano Manor.",
    # Letter from Volcano Manor (Istvan)
    "100730": "On a table in Volcano Manor Drawing-Rooms. Can be missed if the "
              "Drawing-Room Key can't be obtained before defeating the final "
              "boss of Volcano Manor.",
    # Letter from Volcano Manor (Rileigh)
    "100740": "On a table in Volcano Manor Drawing-Rooms. Can be missed if the "
              "first Volcano Manor request can't be completed before defeating "
              "the final boss of Volcano Manor.",
    # Red Letter
    "100750": "On a table in Volcano Manor Drawing-Rooms. Can be missed if the "
              "second Volcano Manor request can't be completed before "
              "defeating the final boss of Volcano Manor.",
    # Tanith's Tonic of Forgetfulness can be softlocked if you can't complete
    # Rileigh's quest before killing Rykard
    # actually it's on her chair if this happens
    # "100700", # Tonic of Forgetfulness
    # Rya's Volcano Manor Invitiation can be softlocked if you have to join
    # Volcano Manor before obtaining Rya's Necklace
    # Volcano Manor Invitation
    "100900": "Given by Rya after returning Rya's Necklace to her. Can be "
              "missed if you must join Volcano Manor to obtain the necklace.",
    # Rya's quest items can be softlocked if you can't give her the Serpent's
    # Amnion before killing Rykard
    # Zorayas's Letter
    "100910": "Drop from Rya at the end of her quest. Can be missed if you "
              "can't obtain the Serpent's Amnion before defeating the final "
              "boss of Volcano Manor.",
    # "100911", # Daedicar's Woe
    # Grace Mimic
    "100500": "Given by Gostoc after confronting him when he follows you "
              "through the castle. Can be missed if defeating the boss of "
              "Stormveil Castle is required to reach Stormveil Castle.",
    # Ranni's quest can be softlocked if one of her later quest items is
    # required to get an earlier one
    # Carian Inverted Statue
    "103910": "Given by Ranni after giving her the Fingerslayer Blade. Can be "
              "missed if the Fingerslayer Blade is inside Renna's Rise or is "
              "dropped by Baleful Shadow, Blaidd, Seluvis, or Iji.",
    # Snow Witch Hat
    "1034510900": "In a chest inside Renna's Rise. Can be missed if the "
                  "Fingerslayer Blade is inside Renna's Rise or is dropped by "
                  "Baleful Shadow, Blaidd, Seluvis, or Iji.",
    # "1034510901",  # Snow Witch Robe
    # "1034510902",  # Snow Witch Skirt
    # Seluvis has several items that can be softlocked
    # Seluvis's Introduction
    "101430": "Given by Seluvis after speaking to Blaidd in Siofra River. Can "
              "be missed if the Radahn festival starts before you join Ranni.",
    # Magic Scorpion Charm
    "101410": "Given by Seluvis after giving him the Amber Starlight. Can be "
              "missed if it is unobtainable before giving Ranni the "
              "Fingerslayer Blade.",
    # Amber Draught
    "101450": "Given by Seluvis after giving him the Amber Starlight. Can be "
              "missed if it is unobtainable before giving Ranni the "
              "Fingerslayer Blade.",
    # # These two aren't listed in the spoilers file, so it seems the randomzier
    # # prevents these from being an issue
    # # Pidia drops one of two puppet ashes depending on whether Nepheli was
    # # given Seluvis's Potion
    # # Dolores the Sleeping Arrow Puppet
    # "101491": "Drop from Pidia after not giving Seluvis's Potion to Nepheli "
    #           "and giving Ranni the Fingerslayer Blade. Can be missed if you "
    #           "give Nepheli the potion or buy it from Seluvis.",
    # # Nepheli Loux Puppet
    # "101496": "Drop from Pidia after giving Seluvis's Potion to Nepheli and "
    #           "giving Ranni the Fingerslayer Blade. Can be missed if you "
    #           "don't give Nepheli the potion.",
    # Gowry can have his quest softlocked if either he or Millicent have items
    # needed in earlier stages of their quests
    # Unalloyed Gold Needle (fixed)
    "103100": "Given by Gowry after giving him the Unalloyed Gold Needle "
              "(Broken). Can be missed if it is held by Gowry, Millicent, or "
              "her sisters.",
    # Sellia's Secret
    "103110": "Given by Gowry after giving him the Unalloyed Gold Needle "
              "(Broken). Can be missed if it is held by Gowry, Millicent, or "
              "her sisters.",
    # Flock's Canvas Talisman
    "103120": "Drop from Gowry after killing him at the end of his quest. Can "
              "be missed if his quest can't be completed.",
    # Millicent can likewise be softlocked
    # Prosthesis-Wearer Heirloom
    "103200": "Given by Millicent after giving her the Unalloyed Gold Needle "
              "(Fixed). Can be missed if it is held by Gowry, Millicent, or "
              "her sisters.",
    # Unalloyed Gold Needle (Millicent)
    "103210": "Drop from Millicent after helping her defeat her sisters. Can "
              "be missed if you side with her sisters.",
    # Millicent's Prosthesis only appears once in the spoiler file even though
    # it has two lots
    # Millicent's Prosthesis, drop
    "103220": "Drop from Millicent after killing her after giving her the "
              "Valkyrie's Prosthesis. Can be missed if you complete her quest.",
    # Millicent's Prosthesis, drop
    "113200": "Reward for defeating Millicent by assisting her sisters. Can be "
              "missed if you side with Millicent.",
    # Rotten Winged Sword Insignia
    "104800": "Reward for defeating Millicent's sisters. Can be missed if you "
              "side with her sisters.",
    # Jar-Bairn's quest reward can be softlocked if Diallos's is
    # Companion Jar
    "104600": "Given by Jar-Bairn at the end of his quest. Can be missed if "
              "Diallos's quest can't be completed.",
    # The following enemy lots seem to follow their randomized enemy ID instead
    # of their original location. Unsure if it's possible that these enemies
    # are never assigned to a new location making the items unobtainable.
    # Also unsure what determines which new enemy assignment has the drop.
    # I've only had one example where the enemy was assigned twice and the drop
    # only happened in the first enemy location in the spoiler file.
    # This also seems to happen inconsistently, the Sellia Hideaway enemy had
    # this problem in one playthrough, but it was awarded properly in another.
    # If there turn out to be a lot of these, may want to set up another data
    # structure to track all enemy positions to be able to give accurate hints,
    # but at that point it would probably be less effort to rewrite the entire
    # mod to work from the data in the map files directly instead of parsing
    # the randomizer's data files. For now, just let the player know these
    # items are possibly missable.
    # Extra Large Scarab drop on bridge to Divine Tower of East Altus
    "34140720": "Drop from enemy on bridge between Leyndell and the Forbidden "
                "Lands. "
                "If enemies are randomized, this item may or may not be "
                "dropped by the original enemy in its new randomized "
                "location (if any), and may not match the contents of the "
                "spoiler file. The item may still be obtainable, but the "
                "hints to it may not be accurate.",
    # Royal Revenant drop in Sainted Hero's Grave, the one closest to the wall
    # of the two that are on each side of the item above and south of the
    # exit door
    "402030001": "Drop from enemy near and above heavy door in Sainted Hero's "
                 "Grave. "
                 "If enemies are randomized, this item may or may not be "
                 "dropped by the original enemy in its new randomized "
                 "location (if any), and may not match the contents of the "
                 "spoiler file. The item may still be obtainable, but the "
                 "hints to it may not be accurate.",
    # Royal Revenant drop in Sellia Hideaway, in the first pool below the
    # crystals in the first big open area
    "402040001": "Drop from enemy in the first pool of water below the "
                 "crystal bridges in Sellia Hideaway. "
                 "If enemies are randomized, this item may or may not be "
                 "dropped by the original enemy in its new randomized "
                 "location (if any), and may not match the contents of the "
                 "spoiler file. The item may still be obtainable, but the "
                 "hints to it may not be accurate.",
    # Enemies that are disguised in the vanilla game that drop Larval Tears
    "1044350100": "Drop from enemy east of Agheel Lake South. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    "1047370100": "Drop from enemy near coffins south of Caelid Highway South. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    "1035430100": "Drop from enemy south of Fallen Ruins of the Lake. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    "1043530100": "Drop from enemy in ruins north of Rampartside Path. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    "1036540100": "Drop from enemy east of Road of Iniquity. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    "1049550700": "Drop from enemy southeast of Inner Consecrated Snowfield. "
                  "If enemies are randomized, this item may or may not be "
                  "dropped by the original enemy in its new randomized "
                  "location (if any), and may not match the contents of the "
                  "spoiler file. The item may still be obtainable, but the "
                  "hints to it may not be accurate.",
    # Vargram the Raging Wolf invasion drop, currently broken by the
    # randomizer v0.5.7
    # Fixed in v0.6
    # "11001985",
    # Bernah's reward for helping him with Vargram, also not available as above
    # Fixed in v0.6
    # "102910",

    # Lots that simply don't appear in the game
    # Glowstone lot attributed to Merchant Kale but does not show up in game
    "100420": "This appears in the spoilers file as belonging to Merchant "
              "Kalé, but it does not actually appear in his shop and cannot be "
              "obtained.",
    # Fix these by adding "norandom ignore" to their lots in itemSlots.txt
    # Neutralizing Boluses 5x, Stanching Boluses, Noble Sorcerer Ashes in
    # lots 1037500000-1037500002 don't actually exist in the world
    # Fixed in v0.9
    # "1037500000": "This appears in the spoilers file as being near "
    #               "Ravine-Veiled Village, but it does not actually appear in"
    #               "the world and cannot be obtained.",
    # Golden Rune [1] in Ruin-Strewn Precipice, has the same directions as
    # a Rune Arc with lot 39200080 but does not appear there
    "39200000": "This appears in the spoilers file as being in the same "
                "location as another item near the base of the elevator next "
                "to Ruin-Strewn Precipice Overlook, but it does not actually "
                "appear in the world and cannot be obtained.",
}

missableShopLots_engus = {
    # Shard Spiral, in Sellen's Shop at the end of her questline
    "100056": "Available in Sellen's shop after assisting her against Jerren. "
              "Can be missed if you side with Jerren.",
    # Immutable Shield, Corhyn's shop after Radagon puzzle
    "100361": "Available in Corhyn's shop after unmasking Radagon's statue. "
              "Can be missed if the Law of Regression is unobtainable before "
              "burning the Erdtree.",
    # Gostoc's quest completion can be softlocked if Nepheli's is
    # Ancient Dragon Smithing Stone
    "100018": "Available in Gostoc's shop after completing Nepheli's quest. "
              "Can be missed if you are unable to complete Nepheli's quest.",
    # Dolores the Sleeping Arrow Puppet
    "100301": "Available in Seluvis's puppet shop after giving Seluvis's "
              "Potion to Nepheli. Can be missed if you don't give her the "
              "potion.",
    # Dung Eater Puppet
    "100310": "Available in Seluvis's puppet shop after giving Seluvis's "
              "Potion to Dung Eater. Can be missed if you don't give him the "
              "potion.",
    # Glintstone Stars
    "100177": "Available in Gowry's shop after giving Millicent the Unalloyed "
              "Gold Needle (Fixed). Can be missed if it is held by Gowry, "
              "Millicent, or her sisters.",
    # Night Shard
    "100175": "Available in Gowry's shop after giving Millicent the Unalloyed "
              "Gold Needle (Fixed). Can be missed if it is held by Gowry, "
              "Millicent, or her sisters.",
    # Night Maiden's Mist
    "100176": "Available in Gowry's shop after giving Millicent the Unalloyed "
              "Gold Needle (Fixed). Can be missed if it is held by Gowry, "
              "Millicent, or her sisters.",
    # Pest Threads
    "100185": "Available in Gowry's shop after giving Millicent the Valkyrie's "
              "Prosthesis. Can be missed if it is held by Gowry, Millicent, or "
              "her sisters.",
}
