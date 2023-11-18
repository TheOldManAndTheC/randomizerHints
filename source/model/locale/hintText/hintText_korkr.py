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
# 한국 특정 수입품:


def hintText_korkr(components, localeData):

    # 주어진 localeData에서 전달된 텍스트의 현지화된 버전을 반환하거나, 존재하지 않는 경우
    # 텍스트를 반환합니다.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # 인벤토리 목록에 나타나는 힌트 아이템의 이름을 모아보세요.
    # "hintName" 컴포넌트가 제공되면 직접 번역되어야 합니다.
    # 구성요소 <components>:
    # "noteName": 아이템 객체 자체에 대한 영어 단어입니다.
    # "ownerName": 해당 항목의 이전 소유자를 설명하는 영어 단어입니다.
    # "ownerAdjective": 소유자를 설명하는 선택적 영어 형용사입니다.
    # 이러한 구성요소를 사용하여 무작위이고 문법적으로 올바른 이름을 조합합니다.
    def hintObjectName():
        # 전체 이름이 이미 제공된 경우 직접 번역하세요.
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{owner}의 {noteName}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return rng.choice(variants).format(**kwargs)

    # 인벤토리 설명에 나타나는 힌트 아이템의 설명을 모아보세요.
    # "hintDescription" 구성 요소가 제공되면 직접 번역되어야 합니다.
    # <hintName>은 힌트 항목의 완전히 번역된 이름이며, 조립된 설명 앞에 별도의 줄을 추가해야
    # 합니다.
    # 구성요소 <components>:
    # "noteName": 힌트 항목 개체 자체에 대한 영어 단어입니다.
    # "noteAdjectives": 힌트 항목 개체를 설명하는 두 개의 영어 형용사입니다.
    # 이러한 구성요소를 사용하여 문법적으로 올바른 설명을 조합하세요.
    def hintObjectDescription(hintName):
        # 완전한 설명이 이미 제공된 경우 직접 번역하세요.
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
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # 단일 포그 게이트 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "area": 시작 지역의 영어 이름입니다.
    # "destArea": 목적지 지역의 영문 이름입니다.
    # "gate": 포그 게이트 또는 워프의 영어 이름
    # "pathAreas": 통과하는 영역이 있는 경우 해당 영역의 영어 이름입니다.
    # 이러한 구성요소를 사용하여 문법적으로 올바른 포그 게이트 힌트를 조합하세요.
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
                "{gate}은 {path} 통해 {dest} 연결됩니다."
            ]
        else:
            variants = [
                "{gate}은 {dest}을 연결됩니다"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # 항목에 HintRegion이 없으면 시작 영역 텍스트를 사용하지 마세요.
        if "hintRegion" in hintEntry:
            kwargs["gate"] = area + "에 " + kwargs["gate"]
        # 경로가 길면 잠재적인 잘림을 방지하기 위해 가장 짧은 형식을 사용하십시오.
        if len(kwargs["path"]) > 90:
            return variants[0].format(**kwargs)
        return rng.choice(variants).format(**kwargs)

    # 단일 무작위 드롭 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "item": 해당 항목의 영어 이름입니다.
    # "enemy" : 아이템을 떨어뜨린 적의 영어 이름입니다.
    # "chance": 드롭 빈도의 영어 이름입니다. "always", "often", "sometimes",
    # "rarely", "very rarely" 또는 ""일 수 있습니다.
    # "quantity": 드롭된 아이템의 수량입니다(두 개 이상인 경우).
    # 이러한 구성 요소를 사용하여 문법적으로 올바른 무작위 드롭 힌트를 조합하세요.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy}은 {item}을 {chance}떨어뜨립니다",
        ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "chance": chance,
        }
        if quantity:
            kwargs["item"] += " " + quantity + "개"
        if kwargs["chance"]:
            kwargs["chance"] += " "
        return rng.choice(variants).format(**kwargs)

    # 단일 도서 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "item": 해당 항목의 영어 이름입니다.
    # "book": 컨테이너 항목의 영어 이름입니다.
    # "parentEntry": 컨테이너 항목에 대한 힌트 항목입니다. 컨테이너 항목에 대한 위치 힌트를
    # 포함하려면 isParent 옵션을 활성화하여 hintString에 전달해야 합니다.
    # 이러한 구성 요소를 사용하여 문법적으로 올바른 책 힌트를 조합하세요.
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        parentHint = hintString(hintEntry["parentEntry"], isParent=True)
        if isParent:
            variants = [
                "에 있는, {parentHint}",
            ]
        else:
            variants = [
                "{item}은 {book}에 있고, {parentHint}",
            ]
        kwargs = {
            "book": book,
            "parentHint": parentHint,
            "item": item,
        }
        if quantity:
            kwargs["item"] += " " + quantity + "개"
        return rng.choice(variants).format(**kwargs)

    # 단일 NPC 항목 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "item": 해당 항목의 영어 이름입니다.
    # "NPC" : 해당 아이템을 소유한 NPC의 영문명입니다.
    # "npcLocation": NPC가 위치한 위치의 영문 이름. NPC가 이곳 저곳으로 이동하는 경우에는
    # 제공되지 않습니다.
    # "foe": 아이템을 획득하기 위해 반드시 쓰러뜨려야 하는 적의 영어 이름입니다(필요한 경우).
    # "foeLocation": 적이 위치한 위치의 영문명.
    # "foeDirections": 적에 대한 방향 항목입니다. 현지화된 길찾기를 제공하려면
    # directionsString 전달되어야 합니다.
    # "isShop": 아이템이 NPC 상점에 있는 경우 이 구성요소가 존재합니다.
    # 이러한 구성 요소를 사용하여 문법적으로 올바른 NPC 항목 힌트를 조합하세요.
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
                "{npc}이 {ownedBy} 것입니다",
            ]
        else:
            variants = [
                "{npc}이 {item}를 {owns}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "소유하고",
            "ownedBy": "소유한",
        }
        if quantity:
            kwargs["item"] += " " + quantity + "개"
        if "isShop" in hintEntry:
            kwargs["owns"] = "판매합니다"
            kwargs["ownedBy"] = "판매하는"
        if npcLocation:
            kwargs["npc"] = npcLocation + "에 " + kwargs["npc"]
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "{location}에서 {foe}을 물리친 후",
                "{directions} {foe}을 물리친 후",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint = questHint + ", " + hint
        return hint

    # 하나의 고유한 적 드롭 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "item": 해당 항목의 영어 이름입니다.
    # "enemy": 아이템을 획득하기 위해 반드시 쓰러뜨려야 할 적의 영어 이름입니다.
    # "directions": 적에 대한 방향 입력입니다. 현지화된 길찾기를 제공하려면
    # directionsString 전달되어야 합니다.
    # 이러한 구성 요소를 사용하여 문법적으로 올바른 고유한 적 드롭 힌트를 조합하세요.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "{directions}의 {enemy}이 소유하고 있는",
            ]
        else:
            variants = [
                "{enemy}은 {directions} {item}을 소유하고",
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] += " " + quantity + "개"
        return rng.choice(variants).format(**kwargs)

    # 단일 보물 힌트 항목의 텍스트를 조합합니다.
    # 구성요소 <hintEntry>:
    # "item": 해당 항목의 영어 이름입니다.
    # "directions": 항목에 대한 길찾기 항목입니다. 현지화된 길찾기를 제공하려면
    # directionsString 전달되어야 합니다.
    # 이러한 구성 요소를 사용하여 문법적으로 올바른 보물 힌트를 조합하세요.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "그곳은 {directions}",
            ]
        else:
            variants = [
                "{item}은 {directions} 있고",
            ]
        kwargs = {
            "item": item,
            "directions": directionsString(hintEntry["directions"])
        }
        if quantity:
            kwargs["item"] += " " + quantity + "개"
        return rng.choice(variants).format(**kwargs)

    # 이 메서드는 힌트 항목의 구성 요소에 따라 다양한 힌트 조립 메서드를 호출합니다.
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

    # 단일 방향 세트의 텍스트를 조합합니다.
    # 구성요소 <directions>:
    # "location": 해당 지역의 영어 이름입니다.
    # "landmark": 기준점으로 사용되는 랜드마크의 영문명. 랜드마크가 없는 경우 위치만
    # 현지화해야 합니다.
    # "angle": 랜드마크로부터 나침반 방향을 나타내는 영어 단어입니다. 거리가 랜드마크
    # 근처에 있으면 각도가 없습니다.
    # "height": 해당 항목이 랜드마크 위에 있는지 아래에 있는지를 나타내는 영어 단어입니다.
    # "far above", "above", "below", "far below" 또는 ""일 수 있습니다.
    # "distance": 아이템이 랜드마크로부터 얼마나 떨어져 있는지 나타내는 영어 단어입니다.
    # "near", "far" 또는 ""일 수 있습니다.
    # 이러한 구성요소를 사용하여 문법적으로 올바른 방향을 조립하세요.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return location + "에서"
        directionsHint = location + "의 " + landmark
        if distance:
            directionsHint += distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint += angle
        if height:
            directionsHint += " 및 " + height
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
