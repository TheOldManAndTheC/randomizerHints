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
# 中國特定進口：


def hintText_zhotw(components, localeData):

    # 傳回從給定 localeData 傳遞給它的文字的本地化版本，或者如果不存在則僅傳回文字。
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # 組合出現在庫存清單中的提示項目的名稱。
    # 如果提供了"hintName"元件，則應直接翻譯它。
    # 組件<components>：
    # "noteName"：項目物件本身的英文單字。
    # "ownerName"：描述該物品的前所有者的英文單字。
    # "ownerAdjective"：描述所有者的可選英語形容詞。
    # 使用這些組件來組合一個隨機且語法正確的名稱。
    def hintObjectName():
        # 如果已經提供了完整名稱，則直接翻譯
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{owner}的{noteName}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + "的" + kwargs["owner"]
        return rng.choice(variants).format(**kwargs)

    # 組裝庫存描述中出現的提示項目的描述。
    # 如果提供了"hintDescription"元件，則應直接翻譯它。
    # <hintName> 是提示項目的完全翻譯名稱，並且應作為單獨的行作為組裝描述的前綴。
    # 組件<components>：
    # "noteName"：提示項物件本身的英文單字。
    # "noteAdjectives"：兩個描述提示項目物件的英文形容詞。
    # 使用這些組件來組合語法正確的描述。
    def hintObjectDescription(hintName):
        # 如果已經提供了完整的描述，請直接翻譯
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}。\n{adj1}的{noteName}",
            "{hintName}。\n{adj1}的{adj2}的{noteName}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # 組裝單一霧門提示條目的文字。
    # 組件<hintEntry>：
    # "area"：起始區域的英文名稱。
    # "destArea"：目的地區域的英文名稱。
    # "gate"：霧門或扭曲的英文名稱
    # "pathAreas"：經過的區域的英文名稱（如果存在）。
    # 使用這些組件來組裝語法正確的霧門提示。
    def fogHint(hintEntry):
        area = localize(hintEntry["area"])
        destArea = localize(hintEntry["destArea"])
        gate = localize(hintEntry["gate"])
        path = ""
        if "pathAreas" in hintEntry:
            for pathArea in hintEntry["pathAreas"]:
                path += localize(pathArea) + "、"
            path = path[:-2]
        if path:
            variants = [
                "{gate}透過{path}通往{dest}"
            ]
        else:
            variants = [
                "{gate}通往{dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # 如果條目中沒有hintRegion，則不要使用起始區域文本
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "在" + area + "，" + kwargs["gate"]
        # 如果路徑很長，請使用最短的形式以避免潛在的截斷
        if len(kwargs["path"]) > 90:
            return variants[0].format(**kwargs)
        return rng.choice(variants).format(**kwargs)

    # 組合單一隨機放置提示條目的文字。
    # 組件<hintEntry>：
    # "item"：項目的英文名稱。
    # "enemy"：掉落物品的敵人的英文名稱。
    # "chance"：掉落頻率的英文名稱。可以是「always」、「often」、「sometimes」、
    # 「rarely」、「very rarely」或「」。
    # "quantity"：掉落物品的數量（如果超過一件）。
    # 使用這些組件來組裝語法正確的隨機放置提示。
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy}{chance}掉落{item}",
        ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "chance": chance,
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # 組裝單一書籍提示條目的文字。
    # 組件<hintEntry>：
    # "item"：項目的英文名稱。
    # "book"：容器項目的英文名稱。
    # "parentEntry"：容器項目的提示條目。應將其傳遞到hintString，並啟用isParent
    # 選項以嵌入容器項目的位置提示。
    # 使用這些組件來組裝語法正確的書籍提示。
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if "parentEntry" in hintEntry:
            parentHint = \
                "，" + hintString(hintEntry["parentEntry"], isParent=True)
        else:
            parentHint = ""
        if isParent:
            variants = [
                "這是在{book}中{parentHint}",
            ]
        else:
            variants = [
                "{book}中有{item}{parentHint}",
            ]
        kwargs = {
            "book": book,
            "parentHint": parentHint,
            "item": item,
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if hint[0] == " ":
            hint = hint[1:]
        return hint

    # 組合單一 NPC 物品提示條目的文字。
    # 組件<hintEntry>：
    # "item"：項目的英文名稱。
    # "NPC"：擁有該物品的NPC的英文名稱。
    # "npcLocation"：NPC 所在位置的英文名稱。如果 NPC 從一個地方移動到另一個地方，
    # 則不提供。
    # "foe"：如果需要的話，必須擊敗才能獲得該物品的敵人的英文名稱。
    # "foeLocation"：敵人所在位置的英文名稱。
    # "foeDirections"：敵人的方向條目。應將其傳遞給 directionsString 以提供本地化方向。
    # "isShop"：如果物品位於 NPC 商店中，則該組件存在。
    # 使用這些組件來組裝語法正確的 NPC 項目提示。
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
                "由{npc}{owns}",
            ]
        else:
            variants = [
                "{npc}{owns}{item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "擁有",
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "出售"
        if npcLocation:
            kwargs["npc"] += "在" + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "在{location}擊敗{foe}後",
                "在{directions}擊敗{foe}後",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint = questHint + "，" + hint
        return hint

    # 組裝單一獨特敵人掉落提示條目的文字。
    # 組件<hintEntry>：
    # "item"：項目的英文名稱。
    # "enemy"：必須擊敗才能獲得該物品的敵人的英文名稱。
    # "directions"：敵人的方向輸入。應將其傳遞給 directionsString 以提供本地化方向。
    # 使用這些組件來組裝語法正確的獨特敵人掉落提示。
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "其所有者為在{directions}具{enemy}",
            ]
        else:
            variants = [
                "在{directions}{enemy}擁有{item}",
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # 組裝單一寶藏提示條目的文字。
    # 組件<hintEntry>：
    # "item"：項目的英文名稱。
    # "directions"：該項目的方向條目。應將其傳遞給 directionsString 以提供本地化方向。
    # 使用這些組件來組裝語法正確的寶藏提示。
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "位於{directions}",
            ]
        else:
            variants = [
                "{item}位於{directions}",
            ]
        kwargs = {
            "item": item,
            "directions": directionsString(hintEntry["directions"])
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        hint = rng.choice(variants).format(**kwargs)
        if hint[0] == " ":
            hint = hint[1:]
        return hint

    # 此方法根據提示條目的元件呼叫各種提示組裝方法。
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

    # 組裝一組說明的文字。
    # 組件<directions>：
    # "location"：該地區的英文名稱。
    # 「landmark」：用作參考點的地標的英文名稱。如果沒有地標，則只需定位位置。
    # 「angle」：表示從地標開始的羅盤方向的英文單字。如果距離接近地標，則不會有角度。
    # 「height」：表示該物品位於地標上方還是下方的英文單字。可以是「far above」、
    # 「above」、「below」、「far below」或「」。
    # 「distance」：表示該項目距地標有多遠的英文單字。可以是「near」、「far」或「」。
    # 使用這些組件來組合語法正確的方向。
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += angle
        else:
            directionsHint = angle
        if height:
            directionsHint += "和" + height
        directionsHint = location + "的" + landmark + directionsHint
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
