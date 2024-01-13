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
# Российский специфический импорт:


def hintText_rusru(components, localeData):

    # Возвращает локализованную версию текста, переданного ему из заданного
    # localeData, или, если таковой не существует, просто возвращает текст.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # Соберите имя предмета-подсказки, который появляется в списках инвентаря.
    # Если указан компонент "hintName", его следует перевести напрямую.
    # Компоненты <components>:
    # <<noteName>>: английское слово, обозначающее сам объект элемента.
    # <<ownerName>>: английское слово, описывающее предыдущего владельца
    # предмета.
    # <<ownerAdjective>>: необязательное английское прилагательное, описывающее
    # владельца.
    # Используйте эти компоненты, чтобы составить рандомизированное и
    # грамматически правильное имя.
    def hintObjectName():
        # если полное имя уже указано, переведите его напрямую
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} {owner}",
            "{noteName} от {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Соберите описание предмета-подсказки, которое появляется в описаниях
    # инвентаря.
    # Если предоставлен компонент "hintDescription", его следует перевести
    # напрямую.
    # <hintName>  --  это полностью переведенное имя элемента подсказки,
    # которое должно быть добавлено к собранному описанию в виде отдельной
    # строки.
    # Компоненты <components>:
    # <<noteName>>: английское слово, обозначающее сам объект элемента
    # подсказки.
    # <<noteAdjectives>>: два английских прилагательных, описывающих объект
    # элемента подсказки.
    # Используйте эти компоненты, чтобы составить грамматически правильное
    # описание.
    def hintObjectDescription(hintName):
        # если полное описание уже предоставлено, переведите его напрямую
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

    # Соберите текст одной записи подсказки о туманных вратах.
    # Компоненты <hintEntry>:
    # <<area>>: английское название стартовой зоны.
    # <<destArea>>: английское название области назначения.
    # <<gate>>: английское название туманных ворот или варпа.
    # <<pathAreas>>: английские названия проходимых областей, если таковые
    # существуют.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # подсказку о туманных воротах.
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
                "{gate} ведет к {dest} через {path}"
            ]
        else:
            variants = [
                "{gate} ведет к {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # если в записи нет hintRegion, не используйте текст начальной области
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "В " + area + " " + kwargs["gate"]
        # если путь длинный, используйте самую короткую форму, чтобы избежать
        # потенциального усечения
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Соберите текст одной случайной записи подсказки.
    # Компоненты <hintEntry>:
    # <<item>>: английское название предмета.
    # <<enemy>>: английское название врага, из которого выпадает предмет.
    # <<chance>>: английское название частоты выпадения. Может быть <<always>>,
    # <<often>>, <<sometimes>>, <<rarely>>, <<very rarely>> или <<>>.
    # <<quantity>>: количество выпавшего предмета, если его больше одного.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # случайную подсказку.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "Из {enemy} {chance}падают {item}",
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

    # Соберите текст из одной записи-подсказки книги.
    # Компоненты <hintEntry>:
    # <<item>>: английское название предмета.
    # <<book>>: английское название предмета-контейнера.
    # <<parentEntry>>: запись подсказки для элемента контейнера. Ее следует
    # передать вhintString с включенной опцией isParent, чтобы встроить
    # подсказку о местоположении для элемента контейнера.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # книжную подсказку.
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
                "который находится в {book}{parentHint}",
            ]
        else:
            variants = [
                "{item} находится в {book}{parentHint}",
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

    # Соберите текст подсказки для одного предмета NPC.
    # Компоненты <hintEntry>:
    # <<item>>: английское название предмета.
    # <<NPC>>: английское название NPC, которому принадлежит предмет.
    # <<npcLocation>>: Английское название локации, в которой находится NPC.
    # Не указывается, если NPC перемещается с места на место.
    # <<foe>>: английское название врага, которого необходимо победить, чтобы
    # получить предмет, если это необходимо.
    # <<foeLocation>>: английское название локации, в которой находится враг.
    # <<foeDirections>>: ввод направлений для противника. Его следует передать
    # в directionsString, чтобы обеспечить локализованные маршруты.
    # <<isShop>>: этот компонент существует, если предмет находится в магазине
    # NPC.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # подсказку к предмету NPC.
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
                "который {ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "владеет",
            "ownedBy": "принадлежит",
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = kwargs["ownedBy"] = "продает"
        if npcLocation:
            kwargs["npc"] += "в " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "после победы над {foe} в {location}",
                "после победы над {foe} {directions}",
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

    # Соберите текст одной уникальной записи-подсказки о враге.
    # Компоненты <hintEntry>:
    # <<item>>: английское название предмета.
    # <<enemy>>: английское название врага, которого необходимо победить,
    # чтобы получить предмет.
    # <<directions>>: направления входа противника. Его следует передать в
    # directionsString, чтобы обеспечить локализованные маршруты.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # уникальную подсказку о выпадении противника.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "который принадлежит {enemy} {directions}",
            ]
        else:
            variants = [
                "{enemy} владеет {item} {directions}",
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

    # Соберите текст одной записи подсказки о сокровищах.
    # Компоненты <hintEntry>:
    # <<item>>: английское название предмета.
    # <<directions>>: запись направления для элемента. Его следует передать в
    # directionsString, чтобы обеспечить локализованные маршруты.
    # Используйте эти компоненты, чтобы составить грамматически правильную
    # подсказку о сокровищах.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "который находится {directions}",
            ]
        else:
            variants = [
                "{item} находятся {directions}",
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

    # Этот метод вызывает различные методы сборки подсказок в зависимости от
    # компонентов записи подсказки.
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

    # Соберите текст единого набора указаний.
    # Компоненты <направления>:
    # <<location>>: английское название области.
    # <<landmark>>: английское название ориентира, используемого в качестве
    # ориентира. Если ориентира нет, локализовать следует только местоположение.
    # <<angle>>: английские слова, обозначающие направление компаса от
    # ориентира. Никакого угла не будет, если расстояние близко к ориентиру.
    # <<height>>: английские слова, обозначающие, находится ли объект выше или
    # ниже ориентира. Может быть <<far above>>, <<above>>, <<below>>,
    # <<far below>> или <<>>.
    # <<height>>: английские слова, обозначающие, насколько далеко от ориентира
    # находится предмет. Может быть <<near>>, <<far>> или <<>>.
    # Используйте эти компоненты, чтобы составить грамматически правильные
    # указания.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "в " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " от " + landmark + " в " + location
        if height:
            directionsHint = height + " и " + directionsHint
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
