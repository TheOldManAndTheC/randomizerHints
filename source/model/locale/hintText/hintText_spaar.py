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
# Importaciones específicas españolas:


def hintText_spaar(components, localeData):

    # Devuelve una versión localizada del texto que se le pasa desde el
    # localeData dado o, si no existe, simplemente devuelve el texto.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # Reúna el nombre del elemento de pista que aparece en las listas de
    # inventario.
    # Si se proporciona un componente "hintName", debe traducirse directamente.
    # Componentes <components>:
    # "noteName": la palabra en inglés para el objeto del elemento en sí.
    # "ownerName": palabra inglesa que describe al propietario anterior del
    # artículo.
    # "ownerAdjective": un adjetivo inglés opcional que describe al propietario.
    # Utilice estos componentes para crear un nombre aleatorio y
    # gramaticalmente correcto.
    def hintObjectName():
        # Si ya se proporciona un nombre completo, tradúzcalo directamente.
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} del {owner}",
            "{noteName} de un {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Reúna la descripción del elemento de pista que aparece en las
    # descripciones del inventario.
    # Si se proporciona un componente "hintDescription", debe traducirse
    # directamente.
    # <hintName> es el nombre completamente traducido del elemento de
    # sugerencia y debe anteponer la descripción ensamblada como una línea
    # separada.
    # Componentes <components>:
    # "noteName": palabra inglesa para el objeto de elemento de sugerencia en
    # sí.
    # "noteAdjectives": dos adjetivos en inglés que describen el objeto del
    # elemento de sugerencia.
    # Utilice estos componentes para armar una descripción gramaticalmente
    # correcta.
    def hintObjectDescription(hintName):
        # Si ya se proporciona una descripción completa, tradúzcala
        # directamente.
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\nUna {noteName} {adj1}",
            "{hintName}.\nUna {noteName} {adj1} {adj2}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Reúna el texto de una sola entrada de sugerencia de puerta antiniebla.
    # Componentes <hintEntry>:
    # "area": El nombre en inglés del área de inicio.
    # "destArea": el nombre en inglés del área de destino.
    # "gate": El nombre en inglés de la puerta de niebla o warp.
    # "pathAreas": los nombres en inglés de las áreas por las que se pasa, si
    # existen.
    # Utilice estos componentes para crear una pista de puerta antiniebla
    # gramaticalmente correcta.
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
                "{gate} conduce a {dest} a través {path}"
            ]
        else:
            variants = [
                "{gate} conduce a {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # Si no hay hintRegion en la entrada, no utilice el texto del área
        # inicial.
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "En " + area + ", " + kwargs["gate"]
        # si el camino es largo, use la forma más corta para evitar posibles
        # truncamientos
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Reúna el texto de una única entrada de sugerencia aleatoria.
    # Componentes <hintEntry>:
    # "item": El nombre en inglés del artículo.
    # "enemy": El nombre en inglés del enemigo que arroja el objeto.
    # "chance": El nombre en inglés de la frecuencia de la caída. Puede ser
    # "always", "often", "sometimes", "rarely", "very rarely" o "".
    # "quantity": La cantidad del artículo descartado, si es más de uno.
    # Utilice estos componentes para crear una pista aleatoria gramaticalmente
    # correcta.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} {chance}dejan caer {item}",
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

    # Reúna el texto de una sola entrada de sugerencia de libro.
    # Componentes <hintEntry>:
    # "item": El nombre en inglés del artículo.
    # "book": El nombre en inglés del artículo contenedor.
    # "parentEntry": la entrada de sugerencia para el elemento contenedor. Se
    # debe pasar a hintString con la opción isParent habilitada para incrustar
    # una sugerencia de ubicación para el elemento contenedor.
    # Utilice estos componentes para crear una pista de libro gramaticalmente
    # correcta.
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
                "que está en {book}{parentHint}",
            ]
        else:
            variants = [
                "{item} está en {book}{parentHint}",
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

    # Reúna el texto de una única entrada de sugerencia de elemento NPC.
    # Componentes <hintEntry>:
    # "item": El nombre en inglés del artículo.
    # "NPC": El nombre en inglés del NPC propietario del artículo.
    # "npcLocation": el nombre en inglés de la ubicación en la que se encuentra
    # el NPC. No se proporciona si el NPC se mueve de un lugar a otro.
    # "foe": El nombre en inglés del enemigo que debe ser derrotado para
    # obtener el objeto, si es necesario.
    # "foeLocation": el nombre en inglés de la ubicación en la que se encuentra
    # el enemigo.
    # "foeDirections": La entrada de direcciones para el enemigo. Debe pasarse
    # a directionsString para proporcionar direcciones localizadas.
    # "isShop": este componente existe si el artículo está en una tienda de NPC.
    # Utilice estos componentes para crear una pista de elemento NPC
    # gramaticalmente correcta.
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
                "que es {ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "posee",
            "ownedBy": "propiedad de",
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "vende"
            kwargs["ownedBy"] = "vendido por"
        if npcLocation:
            kwargs["npc"] += "en " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "después de derrotar a {foe} en {location}",
                "después de derrotar a {foe} {directions}",
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

    # Reúna el texto de una única entrada de pista de caída de enemigo única.
    # Componentes <hintEntry>:
    # "item": El nombre en inglés del artículo.
    # "enemy": El nombre en inglés del enemigo que debe ser derrotado para
    # obtener el objeto.
    # "directions": La entrada de direcciones para el enemigo. Debe pasarse a
    # directionsString para proporcionar direcciones localizadas.
    # Utilice estos componentes para crear una pista de caída de enemigo única
    # y gramaticalmente correcta.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "que es propiedad de {enemy} {directions}",
            ]
        else:
            variants = [
                "{enemy} posee {item} {directions}",
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

    # Reúna el texto de una única entrada de pista de tesoro.
    # Componentes <hintEntry>:
    # "item": El nombre en inglés del artículo.
    # "directions": la entrada de direcciones para el elemento. Debe pasarse a
    # directionsString para proporcionar direcciones localizadas.
    # Utilice estos componentes para crear una pista del tesoro gramaticalmente
    # correcta.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "que está {directions}",
            ]
        else:
            variants = [
                "{item} está {directions}",
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

    # Este método llama a los distintos métodos de ensamblaje de sugerencias
    # según los componentes de la entrada de sugerencias.
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

    # Reúna el texto de un único conjunto de instrucciones.
    # Componentes <directions>:
    # "location": El nombre en inglés del área.
    # "landmark": el nombre en inglés del punto de referencia utilizado como
    # punto de referencia. Si no hay ningún punto de referencia, sólo se debe
    # localizar la ubicación.
    # "angle": Las palabras en inglés para la dirección de la brújula desde el
    # punto de referencia. No habrá ángulo si la distancia está cerca del punto
    # de referencia.
    # "height": palabras en inglés que indican si el elemento está por encima o
    # por debajo del punto de referencia. Puede ser "far above", "above",
    # "below", "far below" o "".
    # "distance": palabras en inglés que indican qué tan lejos del punto de
    # referencia se encuentra el elemento. Puede ser "near", "far" o "".
    # Utilice estos componentes para ensamblar instrucciones gramaticalmente
    # correctas.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "en " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " de " + landmark + " en " + location
        if height:
            directionsHint = height + " y " + directionsHint
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
