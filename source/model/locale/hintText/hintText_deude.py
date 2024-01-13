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
# Deutsche spezifische Importe:


def hintText_deude(components, localeData):

    # Gibt eine lokalisierte Version des Textes zurück, der von den angegebenen
    # localeData an ihn übergeben wurde, oder gibt einfach den Text zurück,
    # wenn keine vorhanden ist.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # Stellen Sie den Namen des Hinweiselements zusammen, das in Inventarlisten
    # erscheint.
    # Wenn eine „hintName"-Komponente bereitgestellt wird, sollte diese direkt
    # übersetzt werden.
    # Komponenten <components>:
    # „noteName": Das englische Wort für das Item-Objekt selbst.
    # „ownerName": Das englische Wort, das den Vorbesitzer des Artikels
    # beschreibt.
    # „ownerAdjective": Ein optionales englisches Adjektiv, das den Eigentümer
    # beschreibt.
    # Verwenden Sie diese Komponenten, um einen zufälligen und grammatikalisch
    # korrekten Namen zusammenzustellen.
    def hintObjectName():
        # Wenn bereits ein vollständiger Name angegeben ist, übersetzen Sie
        # ihn direkt
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} des {owner}",
            "Die {noteName} des {owner}",
            "{noteName} eines {owner}",
            "{noteName} vom {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Stellen Sie die Beschreibung des Hinweiselements zusammen, das in den
    # Inventarbeschreibungen erscheint.
    # Wenn eine „hintDescription"-Komponente bereitgestellt wird, sollte diese
    # direkt übersetzt werden.
    # <hintName> ist der vollständig übersetzte Name des Hinweiselements und
    # sollte der zusammengesetzten Beschreibung als separate Zeile
    # vorangestellt werden.
    # Komponenten <components>:
    # „noteName": Das englische Wort für das Hinweiselementobjekt selbst.
    # „noteAdjectives": Zwei englische Adjektive, die das Hinweiselementobjekt
    # beschreiben.
    # Verwenden Sie diese Komponenten, um eine grammatikalisch korrekte
    # Beschreibung zusammenzustellen.
    def hintObjectDescription(hintName):
        # Wenn bereits eine vollständige Beschreibung vorliegt, übersetzen Sie
        # diese direkt
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\nEine {adj1} {noteName}",
            "{hintName}.\nEine {adj1} {adj2} {noteName}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Stellen Sie den Text eines einzelnen Nebeltor-Hinweiseintrags zusammen.
    # Komponenten <hintEntry>:
    # „area": Der englische Name für das Startgebiet.
    # „destArea": Der englische Name für das Zielgebiet.
    # „gate": Der englische Name für das Nebeltor oder Warp
    # „pathAreas": Die englischen Namen für Bereiche, die durchlaufen werden,
    # sofern vorhanden.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten
    # Fog-Gate-Hinweis zusammenzustellen.
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
                "{gate} über {path} zum {dest}"
            ]
        else:
            variants = [
                "{gate} zum {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": "führt " + gate,
            "path": path,
        }
        # Wenn der Eintrag keine hintRegion enthält, verwenden Sie nicht den
        # Startbereichstext
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "in " + area + " " + kwargs["gate"]
        # Wenn der Pfad lang ist, verwenden Sie die kürzeste Form, um eine
        # mögliche Verkürzung zu vermeiden
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Stellen Sie den Text eines einzelnen zufälligen Drop-Hinweis-Eintrags
    # zusammen.
    # Komponenten <hintEntry>:
    # „item": Der englische Name für den Artikel.
    # „enemy": Der englische Name für den Feind, der den Gegenstand fallen
    # lässt.
    # „chance": Die englische Bezeichnung für die Häufigkeit des Abfalls. Kann
    # „always", „often", „sometimes", „rarely", „very rarely" oder „" sein.
    # „quantity": Die Menge des fallengelassenen Artikels, wenn es mehr als
    # eins ist.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten
    # Random-Drop-Hinweis zusammenzustellen.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} lassen {chance}{item} fallen"
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

    # Stellen Sie den Text eines einzelnen Buchhinweiseintrags zusammen.
    # Komponenten <hintEntry>:
    # „item": Der englische Name für den Artikel.
    # „book": Der englische Name für das Containerelement.
    # „parentEntry": Der Hinweiseintrag für das Containerelement. Er sollte mit
    # aktivierter isParent-Option an hintString übergeben werden, um einen
    # Standorthinweis für das Containerelement einzubetten.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten
    # Buchhinweis zusammenzustellen.
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
                "welches sich in der {book} befindet{parentHint}"
            ]
        else:
            variants = [
                "{item} befindet sich in der {book}{parentHint}"
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

    # Stellen Sie den Text eines einzelnen NPC-Gegenstandshinweiseintrags
    # zusammen.
    # Komponenten <hintEntry>:
    # „item": Der englische Name für den Artikel.
    # „NPC": Der englische Name für den NPC, dem der Gegenstand gehört.
    # „npcLocation": Der englische Name für den Ort, an dem sich der NPC
    # befindet. Wird nicht angegeben, wenn der NPC von Ort zu Ort zieht.
    # „foe": Der englische Name des Feindes, der besiegt werden muss, um den
    # Gegenstand zu erhalten, falls dies erforderlich ist.
    # „foeLocation": Der englische Name für den Ort, an dem sich der Feind
    # befindet.
    # „foeDirections": Der Richtungseintrag für den Feind. Es sollte an
    # directionsString übergeben werden, um lokalisierte Wegbeschreibungen
    # bereitzustellen.
    # „isShop": Diese Komponente existiert, wenn sich der Artikel in einem
    # NPC-Shop befindet.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten
    # NPC-Gegenstandshinweis zusammenzustellen.
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
            if "isShop" in hintEntry:
                variants = [
                    "welches von {npc} {ownedBy}",
                ]
            else:
                variants = [
                    "welches {npc} {ownedBy}",
                ]
        else:
            variants = [
                "{npc} {owns} {item}"
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "besitzt",
            "ownedBy": "gehört",
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "verkauft"
            kwargs["ownedBy"] = "verkauft wird"
        if npcLocation:
            kwargs["npc"] += " in " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "nach dem sieg über {foe} in {location}",
                "nach dem sieg über {foe} {directions}",
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

    # Stellen Sie den Text eines einzelnen, eindeutigen
    # Feindeintrags-Hinweiseintrags zusammen.
    # Komponenten <hintEntry>:
    # „item": Der englische Name für den Artikel.
    # „enemy": Der englische Name des Feindes, der besiegt werden muss, um den
    # Gegenstand zu erhalten.
    # „directions": Der Richtungseintrag für den Feind. Es sollte an
    # directionsString übergeben werden, um lokalisierte Wegbeschreibungen
    # bereitzustellen.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten,
    # eindeutigen Hinweis zum Ablegen des Feindes zusammenzustellen.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "das einem {enemy} {directions} gehört"
            ]
        else:
            variants = [
                "{enemy} besitzt {item} {directions}"
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

    # Stellen Sie den Text eines einzelnen Schatzhinweiseintrags zusammen.
    # Komponenten <hintEntry>:
    # „item": Der englische Name für den Artikel.
    # „directions": Der Wegbeschreibungseintrag für den Artikel. Es sollte an
    # directionsString übergeben werden, um lokalisierte Wegbeschreibungen
    # bereitzustellen.
    # Verwenden Sie diese Komponenten, um einen grammatikalisch korrekten
    # Schatzhinweis zusammenzustellen.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "das liegt {directions}",
            ]
        else:
            variants = [
                "{item} befindet sich {directions}"
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

    # Diese Methode ruft abhängig von den Komponenten des Hinweiseintrags die
    # verschiedenen Methoden zum Zusammenstellen von Hinweisen auf.
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

    # Stellen Sie den Text einer einzigen Reihe von Anweisungen zusammen.
    # Komponenten <directions>:
    # „location": Der englische Name für das Gebiet.
    # „landmark": Der englische Name für das Wahrzeichen, das als Referenzpunkt
    # verwendet wird. Wenn kein Orientierungspunkt vorhanden ist, sollte nur
    # der Standort lokalisiert werden.
    # „angle": Die englischen Wörter für die Himmelsrichtung vom
    # Orientierungspunkt. Es gibt keinen Winkel, wenn die Entfernung in der
    # Nähe des Orientierungspunkts liegt.
    # „height": Die englischen Wörter dafür, ob sich das Objekt über oder unter
    # dem Orientierungspunkt befindet. Kann „far above", „above", „below",
    # „far below" oder „" lauten.
    # „distance": Die englischen Wörter, die angeben, wie weit das Objekt vom
    # Orientierungspunkt entfernt ist. Kann „near", „far" oder „" sein.
    # Verwenden Sie diese Komponenten, um grammatikalisch korrekte Richtungen
    # zusammenzustellen.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "in " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " von " + landmark + " in " + location
        if height:
            directionsHint = height + " und " + directionsHint
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
