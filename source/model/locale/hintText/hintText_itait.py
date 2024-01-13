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
# Importazioni specifiche italiane:


def hintText_itait(components, localeData):

    # Restituisce una versione localizzata del testo passatogli dal localeData
    # specificato oppure, se non ne esiste uno, restituisce semplicemente il
    # testo.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # Assembla il nome dell'elemento suggerimento che appare negli elenchi
    # dell'inventario.
    # Se viene fornito un componente "hintName", dovrebbe essere tradotto
    # direttamente.
    # Componenti <components>:
    # "noteName": la parola inglese per l'oggetto oggetto stesso.
    # "ownerName": la parola inglese che descrive il precedente proprietario
    # dell'articolo.
    # "ownerAdjective": un aggettivo inglese opzionale che descrive il
    # proprietario.
    # Utilizza questi componenti per assemblare un nome randomizzato e
    # grammaticalmente corretto.
    def hintObjectName():
        # se è già fornito un nome completo, tradurlo direttamente
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} di {owner}",
            "La {noteName} del {owner}",
            "{noteName} da un {owner}",
            "{noteName} del {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assembla la descrizione dell'oggetto suggerimento che appare nelle
    # descrizioni dell'inventario.
    # Se viene fornito un componente "hintDescription", dovrebbe essere
    # tradotto direttamente.
    # <hintName> è il nome completamente tradotto dell'elemento suggerimento e
    # dovrebbe prefissare la descrizione assemblata come una riga separata.
    # Componenti <components>:
    # "noteName": la parola inglese per l'oggetto suggerimento stesso.
    # "noteAdjectives": due aggettivi inglesi che descrivono l'oggetto
    # suggerimento.
    # Utilizza questi componenti per assemblare una descrizione
    # grammaticalmente corretta.
    def hintObjectDescription(hintName):
        # se è già fornita una descrizione completa, tradutela direttamente
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

    # Assembla il testo di una singola voce di suggerimento del portale della
    # nebbia.
    # Componenti <hintEntry>:
    # "area": il nome inglese dell'area di partenza.
    # "destArea": il nome inglese dell'area di destinazione.
    # "gate": il nome inglese per la porta della nebbia o curvatura
    # "pathAreas": i nomi inglesi delle aree attraversate, se presenti.
    # Usa questi componenti per assemblare un suggerimento per il cancello
    # della nebbia grammaticalmente corretto.
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
                "{gate} conduce alla {dest} attraverso {path}"
            ]
        else:
            variants = [
                "{gate} conduce alla {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # se non è presente alcun hintRegion nella voce, non utilizzare il
        # testo dell'area iniziale
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "A " + area + ", " + kwargs["gate"]
        # se il percorso è lungo, utilizzare la forma più breve per evitare
        # potenziali troncamenti
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Assembla il testo di una singola voce di suggerimento di rilascio casuale.
    # Componenti <hintEntry>:
    # "item": il nome inglese dell'articolo.
    # "enemy": il nome inglese del nemico che lascia cadere l'oggetto.
    # "chance": il nome inglese per la frequenza del calo. Può essere "always",
    # "often", "sometimes", "rarely", "very rarely" o "".
    # "quantity": la quantità dell'oggetto abbandonato, se è più di uno.
    # Utilizza questi componenti per assemblare un suggerimento di rilascio
    # casuale grammaticalmente corretto.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} {chance}rilasciano {item}"
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

    # Assemblare il testo di una singola voce di suggerimento del libro.
    # Componenti <hintEntry>:
    # "item": il nome inglese dell'articolo.
    # "book": il nome inglese dell'articolo contenitore.
    # "parentEntry": la voce del suggerimento per l'elemento contenitore.
    # Dovrebbe essere passata a hintString con l'opzione isParent abilitata per
    # incorporare un suggerimento sulla posizione per l'elemento contenitore.
    # Usa questi componenti per assemblare un suggerimento per il libro
    # grammaticalmente corretto.
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
                "che si trova nella {book}{parentHint}"
            ]
        else:
            variants = [
                "{item} è nella {book}{parentHint}"
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

    # Assembla il testo di una singola voce di suggerimento per un oggetto NPC.
    # Componenti <hintEntry>:
    # "item": il nome inglese dell'articolo.
    # "NPC": il nome inglese dell'NPC che possiede l'oggetto.
    # "npcLocation": il nome inglese della posizione in cui si trova l'NPC. Non
    # fornito se l'NPC si sposta da un posto all'altro.
    # "foe": il nome inglese del nemico che deve essere sconfitto per ottenere
    # l'oggetto, se richiesto.
    # "foeLocation": il nome inglese della posizione in cui si trova il nemico.
    # "foeDirections": la voce delle indicazioni stradali per il nemico.
    # Dovrebbe essere passato a directionsString per fornire indicazioni
    # localizzate.
    # "isShop": questo componente esiste se l'oggetto si trova in un negozio
    # NPC.
    # Usa questi componenti per assemblare un suggerimento per l'oggetto NPC
    # grammaticalmente corretto.
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
                "che {ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}"
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "possiede",
            "ownedBy": "è di proprietà del",
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "vende"
            kwargs["ownedBy"] = "viene venduto dal"
        if npcLocation:
            kwargs["npc"] += " in " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "dopo aver sconfitto {foe} a {location}",
                "dopo aver sconfitto {foe} {directions}",
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

    # Assembla il testo di una singola voce di suggerimento per il rilascio di
    # un nemico unico.
    # Componenti <hintEntry>:
    # "item": il nome inglese dell'articolo.
    # "enemy": il nome inglese del nemico che deve essere sconfitto per
    # ottenere l'oggetto.
    # "directions": la voce delle direzioni per il nemico. Dovrebbe essere
    # passato a directionsString per fornire indicazioni localizzate.
    # Usa questi componenti per assemblare un suggerimento per la caduta del
    # nemico unico e grammaticalmente corretto.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "che è di proprietà di {enemy} {directions}"
            ]
        else:
            variants = [
                "{enemy} possiede {item} {directions}"
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

    # Metti insieme il testo di una singola voce di suggerimento del tesoro.
    # Componenti <hintEntry>:
    # "item": il nome inglese dell'articolo.
    # "directions": la voce delle indicazioni stradali per l'elemento. Dovrebbe
    # essere passato a directionsString per fornire indicazioni localizzate.
    # Usa questi componenti per assemblare un suggerimento sul tesoro
    # grammaticalmente corretto.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "che si trova {directions}",
            ]
        else:
            variants = [
                "{item} è {directions}"
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

    # Questo metodo chiama i vari metodi di assemblaggio dei suggerimenti a
    # seconda dei componenti della voce del suggerimento.
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

    # Assemblare il testo di un unico insieme di indicazioni.
    # Componenti <directions>:
    # "location": il nome inglese dell'area.
    # "landmark": il nome inglese del punto di riferimento utilizzato come
    # punto di riferimento. Se non è presente alcun punto di riferimento, è
    # necessario localizzare solo la posizione.
    # "angle": le parole inglesi per indicare la direzione della bussola dal
    # punto di riferimento. Non ci sarà alcun angolo se la distanza è vicina al
    # punto di riferimento.
    # "height": le parole inglesi per indicare se l'elemento è sopra o sotto il
    # punto di riferimento. Può essere "far above", "above", "below",
    # "far below" o "".
    # "distance": le parole inglesi per indicare la distanza dal punto di
    # riferimento dell'oggetto. Può essere "near", "far" o "".
    # Usa questi componenti per assemblare indicazioni grammaticalmente
    # corrette.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "nel " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " della " + landmark + " nel " + location
        if height:
            directionsHint = height + " e " + directionsHint
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
