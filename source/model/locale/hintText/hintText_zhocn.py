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
# 中国特定进口：


def hintText_zhocn(components, localeData):

    # 返回从给定 localeData 传递给它的文本的本地化版本，或者如果不存在则仅返回文本。
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # 组合出现在库存列表中的提示项目的名称。
    # 如果提供了"hintName"组件，则应直接翻译它。
    # 组件<components>：
    # "noteName"：项目对象本身的英文单词。
    # "ownerName"：描述该物品的前任所有者的英文单词。
    # "ownerAdjective"：描述所有者的可选英语形容词。
    # 使用这些组件来组合一个随机且语法正确的名称。
    def hintObjectName():
        # 如果已经提供了完整名称，则直接翻译
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

    # 组装库存描述中出现的提示项目的描述。
    # 如果提供了"hintDescription"组件，则应直接翻译它。
    # <hintName> 是提示项的完整翻译名称，并且应作为单独的行作为组装描述的前缀。
    # 组件<components>：
    # "noteName"：提示项对象本身的英文单词。
    # "noteAdjectives"：两个描述提示项对象的英语形容词。
    # 使用这些组件来组合语法正确的描述。
    def hintObjectDescription(hintName):
        # 如果已经提供了完整的描述，请直接翻译
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

    # 组装单个雾门提示条目的文本。
    # 组件<hintEntry>：
    # "area"：起始区域的英文名称。
    # "destArea"：目的地区域的英文名称。
    # "gate"：雾门或扭曲的英文名称
    # "pathAreas"：经过的区域的英文名称（如果存在）。
    # 使用这些组件来组装语法正确的雾门提示。
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
                "{gate}通过{path}通往{dest}"
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
        # 如果条目中没有hintRegion，则不要使用起始区域文本
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "在" + area + "，" + kwargs["gate"]
        # 如果路径很长，请使用最短的形式以避免潜在的截断
        if len(kwargs["path"]) > 90:
            return variants[0].format(**kwargs)
        return rng.choice(variants).format(**kwargs)

    # 组合单个随机放置提示条目的文本。
    # 组件<hintEntry>：
    # "item"：项目的英文名称。
    # "enemy"：掉落物品的敌人的英文名称。
    # "chance"：掉落频率的英文名称。可以是"always"、"often"、"sometimes"、"rarely"、
    # "very rarely"或""。
    # "quantity"：掉落物品的数量（如果超过一件）。
    # 使用这些组件来组装语法正确的随机放置提示。
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

    # 组装单个书籍提示条目的文本。
    # 组件<hintEntry>：
    # "item"：项目的英文名称。
    # "book"：容器项目的英文名称。
    # "parentEntry"：容器项的提示条目。应将其传递给hintString，并启用isParent
    # 选项以嵌入容器项的位置提示。
    # 使用这些组件来组装语法正确的书籍提示。
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
                "这是在{book}中{parentHint}",
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

    # 组合单个 NPC 物品提示条目的文本。
    # 组件<hintEntry>：
    # "item"：项目的英文名称。
    # "NPC"：拥有该物品的NPC的英文名称。
    # "npcLocation"：NPC 所在位置的英文名称。如果 NPC 从一个地方移动到另一个地方，
    # 则不提供。
    # "foe"：如果需要的话，必须击败才能获得该物品的敌人的英文名称。
    # "foeLocation"：敌人所在位置的英文名称。
    # "foeDirections"：敌人的方向条目。应将其传递给 directionsString 以提供本地化方向。
    # "isShop"：如果物品位于 NPC 商店中，则该组件存在。
    # 使用这些组件来组装语法正确的 NPC 项目提示。
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
            "owns": "拥有",
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
                "在{location}击败{foe}后",
                "在{directions}击败{foe}后",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint = questHint + "，" + hint
        return hint

    # 组装单个独特敌人掉落提示条目的文本。
    # 组件<hintEntry>：
    # "item"：项目的英文名称。
    # "enemy"：必须击败才能获得该物品的敌人的英文名称。
    # "directions"：敌人的方向输入。应将其传递给 directionsString 以提供本地化方向。
    # 使用这些组件来组装语法正确的独特敌人掉落提示。
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "其所有者为在{directions}具{enemy}",
            ]
        else:
            variants = [
                "在{directions}{enemy}拥有{item}",
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # 组装单个宝藏提示条目的文本。
    # 组件<hintEntry>：
    # "item"：项目的英文名称。
    # "directions"：该项目的方向条目。应将其传递给 directionsString 以提供本地化方向。
    # 使用这些组件来组装语法正确的宝藏提示。
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "位于{directions}",
            ]
        else:
            variants = [
                "{item}位于{directions}",
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

    # 该方法根据提示条目的组件调用各种提示组装方法。
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

    # 组装一组说明的文本。
    # 组件<directions>：
    # "location"：该地区的英文名称。
    # "landmark"：用作参考点的地标的英文名称。如果没有地标，则只需定位位置。
    # "angle"：表示从地标开始的罗盘方向的英文单词。如果距离接近地标，则不会有角度。
    # "height"：表示该物品位于地标上方还是下方的英文单词。可以是"far above"、"above"、
    # "below"、"far below"或""。
    # "distance"：表示该项目距地标有多远的英文单词。可以是"near"、"far"或""。
    # 使用这些组件来组合语法正确的方向。
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
