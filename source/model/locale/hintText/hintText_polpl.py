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
# Polski import specyficzny:


def hintText_polpl(components, localeData):

    # Zwraca zlokalizowaną wersję tekstu przekazanego mu z podanych ustawień
    # localeData lub, jeśli taki nie istnieje, po prostu zwraca tekst.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # Ułóż nazwę podpowiedzi, która pojawia się na listach ekwipunku.
    # Jeśli dostarczony jest komponent „hintName", należy go bezpośrednio
    # przetłumaczyć.
    # Komponenty <components>:
    # „noteName": angielskie słowo określające sam obiekt elementu.
    # „ownerName": angielskie słowo opisujące poprzedniego właściciela
    # przedmiotu.
    # „ownerAdjective": opcjonalny przymiotnik w języku angielskim opisującym
    # właściciela.
    # Użyj tych komponentów, aby ułożyć losową i poprawną gramatycznie nazwę.
    def hintObjectName():
        # jeśli podano już pełną nazwę, przetłumacz ją bezpośrednio
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} {owner}",
            "{noteName} od {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Złóż opis przedmiotu podpowiedzi, który pojawia się w opisach ekwipunku.
    # Jeśli dostarczony jest komponent „hintDescription", należy go
    # bezpośrednio przetłumaczyć.
    # <Nazwa podpowiedzi> jest w pełni przetłumaczoną nazwą elementu
    # podpowiedzi i powinna poprzedzać złożony opis w osobnej linii.
    # Komponenty <components>:
    # „noteName": angielskie słowo określające sam obiekt podpowiedzi.
    # „noteAdjectives": dwa angielskie przymiotniki opisujące obiekt
    # podpowiedzi.
    # Użyj tych elementów, aby utworzyć poprawny gramatycznie opis.
    def hintObjectDescription(hintName):
        # jeśli pełny opis został już podany, przetłumacz go bezpośrednio
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
            "adj1": capitalize(adjective1),
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Złóż tekst pojedynczego wpisu podpowiedzi dotyczącego bramy mgłowej.
    # Komponenty <hintEntry>:
    # „area": angielska nazwa obszaru początkowego.
    # „destArea": angielska nazwa obszaru docelowego.
    # „gate": angielska nazwa bramy mgłowej lub osnowy
    # „pathAreas": angielskie nazwy obszarów, przez które przechodzi się, jeśli
    # takie istnieją.
    # Użyj tych elementów, aby ułożyć poprawną gramatycznie wskazówkę dotyczącą
    # bramy mgłowej.
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
                "{gate} prowadzi do {dest} przez {path} "
            ]
        else:
            variants = [
                "{gate} prowadzi do {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # jeśli we wpisie nie ma hintRegion, nie używaj tekstu obszaru
        # początkowego
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "w " + area + ", " + kwargs["gate"]
        # jeśli ścieżka jest długa, użyj najkrótszej formy, aby uniknąć
        # potencjalnego obcięcia
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Złóż tekst pojedynczego losowego wpisu podpowiedzi.
    # Komponenty <hintEntry>:
    # „item": angielska nazwa przedmiotu.
    # „enemy": angielska nazwa wroga, który upuszcza przedmiot.
    # „chance": angielska nazwa częstotliwości zrzutu. Może brzmieć „always",
    # „often", „sometimes", „rarely", „very rarely" lub „".
    # „quantity": ilość upuszczonego przedmiotu, jeśli jest ich więcej niż
    # jeden.
    # Użyj tych komponentów, aby ułożyć poprawną gramatycznie wskazówkę
    # dotyczącą losowego upuszczenia.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} {chance}upuszczają {item}",
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

    # Złóż tekst pojedynczego wpisu podpowiedzi do książki.
    # Komponenty <hintEntry>:
    # „item": angielska nazwa przedmiotu.
    # „book": angielska nazwa elementu kontenera.
    # "parentEntry": Wpis podpowiedzi dla elementu kontenera. Należy go
    # przekazać do hintString z włączoną opcją isParent, aby osadzić wskazówkę
    # dotyczącą lokalizacji elementu kontenera.
    # Użyj tych elementów, aby ułożyć poprawną gramatycznie wskazówkę do
    # książki.
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
                "który znajduje się w {book}{parentHint}",
            ]
        else:
            variants = [
                "W {book} znajdują się {item}{parentHint}",
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

    # Złóż tekst pojedynczego wpisu podpowiedzi dotyczącego przedmiotu NPC.
    # Komponenty <hintEntry>:
    # „item": angielska nazwa przedmiotu.
    # „NPC": Angielska nazwa NPC będącego właścicielem przedmiotu.
    # „npcLocation": Angielska nazwa lokalizacji, w której znajduje się NPC.
    # Nie jest podawana, jeśli NPC przemieszcza się z miejsca na miejsce.
    # „foe": angielska nazwa wroga, którego należy pokonać, aby otrzymać
    # przedmiot, jeśli jest to wymagane.
    # „foeLocation": angielska nazwa lokalizacji, w której znajduje się wróg.
    # „foeDirections": Wprowadzanie wskazówek dla wroga. Należy go przekazać do
    # directionsString, aby zapewnić zlokalizowane wskazówki.
    # „isShop": Ten komponent istnieje, jeśli przedmiot znajduje się w sklepie
    # NPC.
    # Użyj tych komponentów, aby ułożyć poprawną gramatycznie wskazówkę
    # dotyczącą przedmiotu NPC.
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
                "{ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "posiada",
            "ownedBy": "którego właścicielem jest",
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "sprzedaje"
            kwargs["isOwned"] = "który jest sprzedawany przez"
        if npcLocation:
            kwargs["npc"] += " w " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "po pokonaniu {foe} {location}",
                "po pokonaniu {foe} {directions}",
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

    # Zbierz tekst pojedynczego, unikalnego wpisu wskazówki o zrzuceniu wroga.
    # Komponenty <hintEntry>:
    # „item": angielska nazwa przedmiotu.
    # „enemy": angielska nazwa wroga, którego należy pokonać, aby otrzymać
    # przedmiot.
    # „directions": Wprowadzanie wskazówek dla wroga. Należy go przekazać do
    # directionsString, aby zapewnić zlokalizowane wskazówki.
    # Użyj tych komponentów, aby stworzyć poprawną gramatycznie, unikalną
    # wskazówkę dotyczącą upuszczenia wroga.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "który jest własnością {enemy} {directions}",
            ]
        else:
            variants = [
                "{enemy} posiada {item} {directions}",
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

    # Złóż tekst pojedynczego wpisu wskazówki dotyczącego skarbu.
    # Komponenty <hintEntry>:
    # „item": angielska nazwa przedmiotu.
    # „directions": wpis dotyczący wskazówek dotyczących przedmiotu. Należy go
    # przekazać do directionsString, aby zapewnić zlokalizowane wskazówki.
    # Użyj tych elementów, aby ułożyć poprawną gramatycznie wskazówkę dotyczącą
    # skarbu.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "który jest na {directions}",
            ]
        else:
            variants = [
                "{item} znajdują się na {directions}",
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

    # Ta metoda wywołuje różne metody składania podpowiedzi w zależności od
    # komponentów wpisu podpowiedzi.
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

    # Złóż tekst jednego zestawu wskazówek.
    # Komponenty <directions>:
    # „location": angielska nazwa obszaru.
    # „landmark": angielska nazwa punktu orientacyjnego używanego jako punkt
    # odniesienia. Jeżeli nie ma punktu orientacyjnego, należy zlokalizować
    # jedynie lokalizację.
    # „angle": angielskie słowa oznaczające kierunek kompasu od punktu
    # orientacyjnego. Nie będzie żadnego kąta, jeśli odległość będzie blisko
    # punktu orientacyjnego.
    # „height": angielskie słowa określające, czy przedmiot znajduje się
    # powyżej, czy poniżej punktu orientacyjnego. Może być „far above",
    # „above", „below", „far below" lub „".
    # „distance": angielskie słowa określające odległość od punktu
    # orientacyjnego, w którym znajduje się przedmiot. Może być „near", „far"
    # lub „".
    # Użyj tych komponentów, aby złożyć poprawne gramatycznie wskazówki.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "w " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " od " + landmark + " w " + location
        if height:
            directionsHint = height + " i " + directionsHint
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
