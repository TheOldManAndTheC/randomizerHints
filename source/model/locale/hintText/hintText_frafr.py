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

from source.utils.rng import rng
from source.utils.capitalize import capitalize
# Importations spécifiques françaises :


def hintText_frafr(components, localeData):

    # Renvoie une version localisée du texte qui lui est transmis à partir du
    # localeData donné, ou s'il n'en existe pas, renvoie simplement le texte.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # Assemblez le nom de l'élément d'indice qui apparaît dans les listes
    # d'inventaire.
    # Si un composant "hintName" est fourni, il doit être directement traduit.
    # Composants <components> :
    # "noteName" : le mot anglais désignant l'objet élément lui-même.
    # "ownerName" : mot anglais décrivant le précédent propriétaire de
    # l'élément.
    # "ownerAdjective" : un adjectif anglais facultatif décrivant le
    # propriétaire.
    # Utilisez ces composants pour assembler un nom aléatoire et
    # grammaticalement correct.
    def hintObjectName():
        # si un nom complet est déjà fourni, traduisez-le directement
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} du {owner}",
            "Le {noteName} du {owner}",
            "{noteName} du'n {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] += " " + ownerAdjective
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemblez la description de l'élément d'indice qui apparaît dans les
    # descriptions d'inventaire.
    # Si un composant "hintDescription" est fourni, il doit être directement
    # traduit.
    # <hintName> est le nom entièrement traduit de l'élément d'indice et doit
    # préfixer la description assemblée sur une ligne distincte.
    # Composants <components> :
    # "noteName" : le mot anglais désignant l'objet d'élément d'indice lui-même.
    # "noteAdjectives" : deux adjectifs anglais qui décrivent l'objet d'élément
    # d'indice.
    # Utilisez ces composants pour assembler une description grammaticalement
    # correcte.
    def hintObjectDescription(hintName):
        # si une description complète est déjà fournie, traduisez-la directement
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\nUne {noteName} {adj1}",
            "{hintName}.\nUne {noteName} {adj1} {adj2}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Assemblez le texte d'une seule entrée d'indice de porte de brouillard.
    # Composants <hintEntry> :
    # "area" : Le nom anglais de la zone de départ.
    # "destArea" : nom anglais de la zone de destination.
    # "gate" : Le nom anglais de la porte de brouillard ou chaîne
    # "pathAreas" : les noms anglais des zones traversées, le cas échéant.
    # Utilisez ces composants pour assembler un indice de porte de brouillard
    # grammaticalement correct.
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
                "{gate} mène à la tour {dest} via {path}"
            ]
        else:
            variants = [
                "{gate} mène à la tour {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # s'il n'y a pas d'hintRegion dans l'entrée, n'utilisez pas le texte de
        # la zone de départ
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "À " + area + ", " + kwargs["gate"]
        # si le chemin est long, utilisez la forme la plus courte pour éviter
        # une éventuelle troncature
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemblez le texte d'une seule entrée d'indice de dépôt aléatoire.
    # Composants <hintEntry> :
    # "item" : Le nom anglais de l'élément.
    # "enemy" : Le nom anglais de l'ennemi qui lâche l'objet.
    # "chance" : Le nom anglais de la fréquence de la chute. Peut être
    # << always >>, << often >>, << sometimes >>, << rarely >>,
    # << very rarely >> ou << >>.
    # "quantity" : La quantité de l'article déposé, s'il y en a plusieurs.
    # Utilisez ces composants pour assembler un indice de dépôt aléatoire
    # grammaticalement correct.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} lâchent {chance}{item}"
        ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "chance": chance,
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if kwargs["chance"]:
            kwargs["chance"] += " "
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assemblez le texte d'une seule entrée d'indice de livre.
    # Composants <hintEntry> :
    # "item" : Le nom anglais de l'élément.
    # "book" : le nom anglais de l'élément conteneur.
    # "parentEntry" : entrée d'indice pour l'élément conteneur. Elle doit être
    # transmise à hintString avec l'option isParent activée pour intégrer un
    # indice d'emplacement pour l'élément conteneur.
    # Utilisez ces composants pour assembler un indice de livre
    # grammaticalement correct.
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if "parentEntry" in hintEntry:
            parentHint = \
                ", " + hintString(hintEntry["parentEntry"], isParent=True)
        else:
            parentHint = ""
        if isParent:
            variants = [
                "qui se trouve dans {book}{parentHint}"
            ]
        else:
            variants = [
                "{item} sont dans {book}{parentHint}"
            ]
        kwargs = {
            "book": book,
            "parentHint": parentHint,
            "item": item,
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemblez le texte d'une seule entrée d'indice d'objet de PNJ.
    # Composants <hintEntry> :
    # "item" : Le nom anglais de l'élément.
    # "NPC" : Le nom anglais du PNJ qui possède l'objet.
    # "npcLocation" : Le nom anglais de l'emplacement dans lequel se trouve le
    # PNJ. Non fourni si le PNJ se déplace d'un endroit à l'autre.
    # "foe" : Le nom anglais de l'ennemi qui doit être vaincu pour obtenir
    # l'objet, si cela est nécessaire.
    # "foeLocation" : Le nom anglais de l'emplacement où se trouve l'ennemi.
    # "foeDirections" : L'entrée des directions pour l'ennemi. Il doit être
    # transmis à directionsString pour fournir des instructions localisées.
    # "isShop" : Ce composant existe si l'objet se trouve dans une boutique de
    # PNJ.
    # Utilisez ces composants pour assembler un indice d'objet PNJ
    # grammaticalement correct.
    def npcHint(hintEntry, isParent=False):
        npc = localize(hintEntry["NPC"])
        npcLocation = localize(hintEntry["npcLocation"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        foe = foeLocation = foeDirections = ""
        if "foe" in hintEntry:
            foe = localize(hintEntry["foe"])
            foeLocation = localize(hintEntry["foeLocation"])
            foeDirections = directionsString(hintEntry["foeDirections"])
        if isParent:
            variants = [
                "qui {ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}"
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "possède",
            "ownedBy": "appartient à"
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "vend"
            kwargs["ownedBy"] = "est vendu par"
        if npcLocation:
            kwargs["npc"] += " à " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "après avoir vaincu {foe} à {location}",
                "après avoir vaincu {foe} {directions}",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint += " " + questHint
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemblez le texte d'une seule entrée d'indice de chute d'ennemi unique.
    # Composants <hintEntry> :
    # "item" : Le nom anglais de l'élément.
    # "enemy" : Le nom anglais de l'ennemi qui doit être vaincu pour obtenir
    # l'objet.
    # "directions" : L'entrée des directions pour l'ennemi. Il doit être
    # transmis à directionsString pour fournir des instructions localisées.
    # Utilisez ces composants pour assembler un indice de chute d'ennemi unique
    # grammaticalement correct.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "qui appartient à un {enemy} {directions}"
            ]
        else:
            variants = [
                "Un {enemy} possède {item} {directions}"
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Assemblez le texte d'une seule entrée d'indice au trésor.
    # Composants <hintEntry> :
    # "item" : Le nom anglais de l'élément.
    # "directions" : l'entrée de direction pour l'élément. Il doit être
    # transmis à directionsString pour fournir des instructions localisées.
    # Utilisez ces composants pour assembler un indice de trésor
    # grammaticalement correct.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "qui se trouve au {directions}",
            ]
        else:
            variants = [
                "{item} se trouve {directions}"
            ]
        kwargs = {
            "item": item,
            "directions": directionsString(hintEntry["directions"])
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if not isParent:
            hint = capitalize(hint)
        return hint

    # Cette méthode appelle les différentes méthodes d'assemblage d'indices en
    # fonction des composants de l'entrée d'indice.
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

    # Assemblez le texte d'un seul ensemble d'instructions.
    # Composants <directions> :
    # "location" : Le nom anglais de la zone.
    # "landmark" : Le nom anglais du point de repère utilisé comme point de
    # référence. S'il n'y a pas de point de repère, seul l'emplacement doit
    # être localisé.
    # "angle" : les mots anglais désignant la direction de la boussole à partir
    # du point de repère. Il n'y aura aucun angle si la distance est proche du
    # point de repère.
    # "height" : les mots anglais indiquant si l'élément est au-dessus ou en
    # dessous du point de repère. Peut être << far above >>, << above >>,
    # << below >>, << far below >> ou << >>.
    # "distance" : les mots anglais indiquant à quelle distance du point de
    # repère se trouve l'élément. Peut être "near", "far" ou "".
    # Utilisez ces composants pour assembler des instructions grammaticalement
    # correctes.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "à " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += "de la " + landmark + " à " + location
        if height:
            directionsHint = height + " et " + directionsHint
        return directionsHint

    hint = dict()
    hint["name"] = hintObjectName()
    hint["description"] = hintObjectDescription(hint["name"])
    text = ""
    for entry in components["hintEntries"]:
        if not components["isItem"]:
            text += fogHint(entry) + "\n\n"
            continue
        text += hintString(entry) + "\n\n"
    hint["text"] = text
    return hint
