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

from warnings import warn
from source.utils.rng import rng
from source.utils.capitalize import capitalize
# English specific imports:
from source.model.locale.hintText.hintTextUtils_engus import articleOf
from source.model.locale.hintText.hintTextUtils_engus import randomText
from source.model.locale.hintText.hintTextUtils_engus import makePlural
from source.data.locale.hintText.engus.noArticles_engus \
    import noArticles
from source.data.locale.hintText.engus.hintTextData_engus \
    import enemyPlurals
from source.data.locale.hintText.engus.hintTextData_engus \
    import itemPlurals


def hintText_engus(components, localeData):

    # Returns a localized version of the text passed to it from the given
    # localeData, or if one does not exist just returns the text.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # debug code to check for missing translations
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # Assemble the name of the hint item that appears in inventory lists.
    # If a "hintName" component is provided, it should be directly translated.
    # Components <components>:
    #   "noteName": The English word for the item object itself.
    #   "ownerName": The English word describing the previous owner of the item.
    #   "ownerAdjective": An optional English adjective describing the owner.
    # Use these components to assemble a randomized and grammatically correct
    # name.
    def hintObjectName():
        # if a complete name is provided already, translate it directly
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{article} {owner}'s {noteName}",
            "The {owner}'s {noteName}",
            "{owner}'s {noteName}",
            "{noteName} from {article} {owner}",
            "{noteName} from the {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
            "article": articleOf(ownerName, noArticles),
        }
        # for English, just put the owner adjective in front of the owner name
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemble the description of the hint item that appears in inventory
    # descriptions.
    # If a "hintDescription" component is provided, it should be directly
    # translated.
    # <hintName> is the fully translated name of the hint item, and should
    # prefix the assembled description as a separate line.
    # Components <components>:
    #   "noteName": The English word for the hint item object itself.
    #   "noteAdjectives": Two English adjectives that describe the hint item
    #   object.
    # Use these components to assemble a grammatically correct description.
    def hintObjectDescription(hintName):
        # if a complete description is provided already, translate it directly
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\n{adj1} {noteName}",
            "{hintName}.\n{adj1} {adj2} {noteName}",
        ]
        kwargs = {
            "adj1": capitalize(articleOf(adjective1, noArticles)) + " "
                    + adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Assemble the text of a single fog gate hint entry.
    # Components <hintEntry>:
    #   "area": The English name for the starting area.
    #   "destArea: The English name for the destination area.
    #   "gate": The English name for the fog gate or warp
    #   "pathAreas": The English names for areas that are passed through, if
    #   any exist.
    # Use these components to assemble a grammatically correct fog gate hint.
    def fogHint(hintEntry):
        area = localize(hintEntry["area"])
        destArea = localize(hintEntry["destArea"])
        gate = localize(hintEntry["gate"])
        path = ""
        if "pathAreas" in hintEntry:
            for pathArea in hintEntry["pathAreas"]:
                path += localize(pathArea) + ", "
            path = path[:-2]
        if path:
            variants = [
                "{areaGate} {leadsTo} {dest} {passing} {path}",
                "{areaGate} {passes} {path} {leadingTo} {dest}",
                "{dest} {connectedTo} {gateArea} {passing} {path}",
            ]
        else:
            variants = [
                "{areaGate} {leadsTo} {dest}",
                "{dest} {connectedTo} {gateArea}",
            ]
        kwargs = {
            "area": "",
            "dest": destArea,
            "gate": gate,
            "leadsTo": randomText("leads to"),
            "leadingTo": randomText("leading to"),
            "connectedTo": randomText("is connected to"),
            "passing": randomText("passing through"),
            "passes": randomText("passes through"),
            "path": path,
        }
        # if there is no hintRegion in the entry, don't use the starting area
        # text
        if "hintRegion" in hintEntry:
            kwargs["area"] = "in " + area
        # if the path is long, use the shortest form to avoid potential
        # truncating
        if len(kwargs["path"]) > 90:
            kwargs["areaGate"] = gate
            if kwargs["area"]:
                kwargs["areaGate"] += " " + kwargs["area"]
            kwargs["leadsTo"] = "leads to"
            kwargs["passing"] = "via"
            return capitalize(variants[0].format(**kwargs))
        if rng.randint(0, 1):
            kwargs["gate"] = "the " + kwargs["gate"]
        kwargs["areaGate"] = kwargs["gate"]
        kwargs["gateArea"] = kwargs["gate"]
        if kwargs["area"]:
            # gateArea must be ordered, but areaGate can be ordered either way
            kwargs["gateArea"] += " " + kwargs["area"]
            if rng.randint(0, 1):
                kwargs["areaGate"] = kwargs["area"] + ", " + kwargs["gate"]
            else:
                kwargs["areaGate"] = kwargs["gateArea"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemble the text of a single random drop hint entry.
    # Components <hintEntry>:
    #   "item": The English name for the item.
    #   "enemy": The English name for the enemy that drops the item.
    #   "chance": The English name for the frequency of the drop. Can be
    #   "always", "often", "sometimes", "rarely", "very rarely", or "".
    #   "quantity": The quantity of the dropped item, if it is more than one.
    # Use these components to assemble a grammatically correct random drop hint.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{item} {chance}are {isDrop} {enemy}",
            "{item} are {chance}{isDrop} {enemy}",
            "{enemy} {chance}will {drop} {item}",
            "{enemy} will {chance}{drop} {item}",
            "{enemy} {chance}{drop} {item}",
            "{chance}{item} are {isDrop} {enemy}",
            "{chance}{enemy} will {drop} {item}",
            "{chance}{enemy} {drop} {item}",
        ]
        kwargs = {
            "item": makePlural(item, itemPlurals),
            "enemy": makePlural(enemy, enemyPlurals),
            "chance": chance,
            "drop": randomText("drop"),
            "isDrop": randomText("dropped by")
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if kwargs["chance"]:
            kwargs["chance"] += " "
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemble the text of a single book hint entry.
    # Components <hintEntry>:
    #   "item": The English name for the item.
    #   "book": The English name for the container item.
    #   "parentEntry": The hint entry for the container item. It should be
    #   passed to hintString with the isParent option enabled to embed a
    #   location hint for the container item.
    # Use these components to assemble a grammatically correct book hint.
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        parentHint = hintString(hintEntry["parentEntry"], isParent=True)
        if isParent:
            variants = [
                "which is {in} the {book}, {parentHint}",
                "and the {book} {contains} one, {parentHint}",
                "and one is {in} the {book}, {parentHint}",
            ]
        else:
            variants = [
                "{in} the {book} {verb} {item}, {parentHint}",
                "the {book} {contains} {item}, {parentHint}",
                "{item} {verb} {in} the {book}, {parentHint}",
            ]
        parts = itemParts(hintEntry)
        kwargs = {
            "book": book,
            "parentHint": parentHint,
            "item": parts["itemHint"],
            "verb": parts["verb"],
            "in": randomText("within"),
            "contains": randomText("contains"),
        }
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemble the text of a single NPC item hint entry.
    # Components <hintEntry>:
    #   "item": The English name for the item.
    #   "NPC": The English name for the NPC that owns the item.
    #   "npcLocation": The English name for the location the NPC is in. Not
    #   provided if the NPC moves from place to place.
    #   "foe": The English name of the enemy that must be defeated to obtain
    #   the item, if that is required.
    #   "foeLocation": The English name for the location the enemy is in.
    #   "foeDirections": The directions entry for the enemy. It should be
    #   passed to directionsString to provide localized directions.
    #   "isShop": This component exists if the item is in an NPC shop.
    # Use these components to assemble a grammatically correct NPC item hint.
    def npcHint(hintEntry, isParent=False):
        npc = localize(hintEntry["NPC"])
        npcLocation = localize(hintEntry["npcLocation"])
        foe = foeLocation = foeDirections = ""
        if "foe" in hintEntry:
            foe = localize(hintEntry["foe"])
            article = articleOf(foe, noArticles)
            if article:
                foe = article + " " + foe
            foeLocation = localize(hintEntry["foeLocation"])
            foeDirections = directionsString(hintEntry["foeDirections"])
        if isParent:
            variants = [
                "which {verb} {isOwned} {npcRegion}",
                "and {npc} {owns} one{spaceRegion}",
                "{andOneInRegion}which {npc} {owns}",
                "and{spaceRegionComma} one {verb} {isOwned} {npc}",
            ]
        else:
            variants = [
                "{item} {verb} {isOwned} {npcRegion}",
                "{npc} {owns} {itemRegion}",
                "{regionNPC} {owns} {item}",
                "{regionItem} {verb} {isOwned} {npc}",
            ]
        parts = itemParts(hintEntry)
        article = articleOf(npc, noArticles)
        if article:
            npc = article + " " + npc
        kwargs = {
            "verb": parts["verb"],
            "isOwned": randomText("owned by"),
            "owns": randomText("owns"),
            "item": parts["itemHint"],
            "npc": npc,
            "npcRegion": npc,
            "regionNPC": npc,
            "itemRegion": parts["itemHint"],
            "regionItem": parts["itemHint"],
            "spaceRegion": "",
            "spaceRegionComma": "",
            "andOneInRegion": "",
        }
        if "isShop" in hintEntry:
            kwargs["isOwned"] = randomText("sold by")
            kwargs["owns"] = randomText("sells")
        if npcLocation:
            region = "in " + npcLocation
            kwargs["spaceRegion"] = " " + region
            kwargs["spaceRegionComma"] = kwargs["spaceRegion"] + ","
            kwargs["andOneInRegion"] = "and one is " + region + ", "
            kwargs["npcRegion"] += " " + region
            kwargs["itemRegion"] += " " + region
            kwargs["regionNPC"] = region + ", " + kwargs["npc"]
            kwargs["regionItem"] = region + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "{after} {killing} {foe} in {location}",
                "{after} {killing} {foe} {directions}",
            ]
            kwargs = {
                "after": randomText("after"),
                "killing": randomText("killing"),
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            if not isParent and rng.randint(0, 1):
                hint = questHint + ", " + hint
            else:
                hint += " " + questHint
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemble the text of a single unique enemy drop hint entry.
    # Components <hintEntry>:
    #   "item": The English name for the item.
    #   "enemy": The English name of the enemy that must be defeated to obtain
    #   the item.
    #   "directions": The directions entry for the enemy. It should be passed
    #   to directionsString to provide localized directions.
    # Use these components to assemble a grammatically correct unique enemy
    # drop hint.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        if isParent:
            variants = [
                "and {enemy} {owns} one {directions}",
                "which {verb} {isOwned} {enemy} {directions}",
                "and {directions} {enemy} {owns} one",
                "and {directions} one {verb} {isOwned} {enemy}",
                "and {enemy} {directions} {owns} one",
                "and one {directions} {verb} {isOwned} {enemy}",
            ]
        else:
            variants = [
                "{enemy} {owns} {item} {directions}",
                "{item} {verb} {isOwned} {enemy} {directions}",
                "{directions} {enemy} {owns} {item}",
                "{directions} {item} {verb} {isOwned} {enemy}",
                "{enemy} {directions} {owns} {item}",
                "{item} {directions} {verb} {isOwned} {enemy}",
            ]
        parts = itemParts(hintEntry)
        article = articleOf(enemy, noArticles)
        if article:
            enemy = article + " " + enemy
        kwargs = {
            "item": parts["itemHint"],
            "enemy": enemy,
            "owns": randomText("owns"),
            "directions": directionsString(hintEntry["directions"]),
            "verb": parts["verb"],
            "isOwned": randomText("owned by")
        }
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemble the text of a single treasure hint entry.
    # Components <hintEntry>:
    #   "item": The English name for the item.
    #   "directions": The directions entry for the item. It should be passed to
    #   directionsString to provide localized directions.
    # Use these components to assemble a grammatically correct treasure hint.
    def treasureHint(hintEntry, isParent=False):
        parts = itemParts(hintEntry)
        if isParent:
            variants = [
                "which {verb} {directions}",
            ]
        else:
            variants = [
                "{item} {verb} {directions}",
                "{directions} {verb} {item}",
            ]
        kwargs = {
            "item": parts["itemHint"],
            "verb": parts["verb"],
            "directions": directionsString(hintEntry["directions"])
        }
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # This method calls the various hint assembling methods depending on the
    # hint entry's components.
    def hintString(hintEntry, isParent=False):
        if "chance" in hintEntry:
            return randomDropHint(hintEntry)
        elif "book" in hintEntry:
            return bookHint(hintEntry, isParent)
        elif "NPC" in hintEntry:
            return npcHint(hintEntry, isParent)
        elif "enemy" in hintEntry:
            return enemyHint(hintEntry, isParent)
        else:
            return treasureHint(hintEntry, isParent)

    # Assemble the text of a single set of directions.
    # Components <directions>:
    #   "location": The English name for the area.
    #   "landmark": The English name for the landmark used as a reference
    #   point. If there is no landmark, only the location should be localized.
    #   "angle": The English words for the compass direction from the landmark.
    #   There will be no angle if the distance is near the landmark.
    #   "height": The English words for whether the item is above or below the
    #   landmark. Can be "far above", "above", "below", "far below" or "".
    #   "distance":  The English words for how far from the landmark the item
    #   is. Can be "near", "far", or "".
    # Use these components to assemble grammatically correct directions.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return randomText("in") + " " + location
        if distance:
            distanceHint = randomText(distance)
            if angle:
                distanceHint += " " + angle + " of"
        else:
            distanceHint = angle + " of"
        if height:
            if rng.randint(0, 1):
                directionsHint = \
                    distanceHint + " and " + height + " " + landmark
            else:
                directionsHint = \
                    height + " and " + distanceHint + " " + landmark
        else:
            directionsHint = distanceHint + " " + landmark
        if rng.randint(0, 1):
            return "in " + location + " " + directionsHint
        return directionsHint + " in " + location

    # English specific method to get the article and plural form of the entry's
    # item name and the correct verb.
    def itemParts(hintEntry):
        item = localize(hintEntry["item"])
        parts = {"verb": "are"}
        if hintEntry["quantity"]:
            parts["itemHint"] = hintEntry["quantity"] + " " \
                                + makePlural(item, itemPlurals)
        elif item in itemPlurals and item == itemPlurals[item]:
            parts["itemHint"] = "some " + item
        else:
            parts["verb"] = "is"
            article = articleOf(item, noArticles)
            if article:
                parts["itemHint"] = article + " " + item
            else:
                parts["itemHint"] = item
        return parts

    hint = dict()
    # Create the name of the hint object
    hint["name"] = hintObjectName()
    # Create the description of the hint object
    hint["description"] = hintObjectDescription(hint["name"])
    # Create the text body of the hint object
    text = ""
    for entry in components["hintEntries"]:
        if not components["isItem"]:
            text += fogHint(entry) + "\n\n"
            continue
        text += hintString(entry) + "\n\n"
    hint["text"] = text
    if "FIXME" in text:
        warn(text, RuntimeWarning)
    return hint
