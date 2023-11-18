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
# 日本固有の輸入品:


def hintText_jpnjp(components, localeData):

    # 指定された localeData から渡されたテキストのローカライズされたバージョンを返します。
    # 存在しない場合はテキストを返します。
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # インベントリリストに表示されるヒントアイテムの名前を組み立てます。
    # 「hintName」コンポーネントが提供されている場合は、それを直接翻訳する必要があります。
    # コンポーネント <components>:
    # "noteName": item オブジェクト自体を表す英語の単語。
    # "ownerName": アイテムの前の所有者を表す英語の単語。
    # "ownerAdjective": 所有者を説明する英語の形容詞 (オプション)。
    # これらのコンポーネントを使用して、ランダム化された文法的に正しい名前を組み立てます。
    def hintObjectName():
        # 完全な名前がすでに指定されている場合は、それを直接翻訳します
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{owner}の{noteName}",
            "{owner}からの{noteName}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + "な" + kwargs["owner"]
        return rng.choice(variants).format(**kwargs)

    # インベントリの説明に表示されるヒントアイテムの説明を組み立てます。
    # 「hintDescription」コンポーネントが提供されている場合は、
    # それを直接翻訳する必要があります。
    # <hintName> は、ヒント項目の完全に翻訳された名前であり、
    # 別の行として組み立てられた説明の前に付ける必要があります。
    # コンポーネント <components>:
    # "noteName": ヒント項目オブジェクト自体を表す英語の単語。
    # "noteAdjectives": ヒント項目オブジェクトを説明する 2 つの英語の形容詞。
    # これらのコンポーネントを使用して、文法的に正しい説明を組み立てます。
    def hintObjectDescription(hintName):
        # 完全な説明がすでに提供されている場合は、それを直接翻訳してください
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}。\n{adj1}の{noteName}",
            "{hintName}。\n{adj1}の{adj2}の{noteName}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # 単一のフォグ ゲート ヒント エントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "area": 開始エリアの英語名。
    # "destArea": 宛先エリアの英語名。
    # "gate"：霧のゲートまたはワープの英語名
    # "pathAreas": 通過する領域が存在する場合、その英語名。
    # これらのコンポーネントを使用して、文法的に正しいフォグ ゲート ヒントを組み立てます。
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
                "{gate}が{path}を経由して{dest}に通じています"
            ]
        else:
            variants = [
                "{gate}が{dest}につながる"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # エントリにhintRegionがない場合は、開始領域のテキストを使用しないでください。
        if "hintRegion" in hintEntry:
            kwargs["gate"] = area + "では" + kwargs["gate"]
        # パスが長い場合は、切り捨てられる可能性を避けるために最短の形式を使用します。
        if len(kwargs["path"]) > 90:
            return variants[0].format(**kwargs)
        return rng.choice(variants).format(**kwargs)

    # 単一のランダムなドロップ ヒント エントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "item": アイテムの英語名。
    # "enemy"：アイテムをドロップする敵の英語名。
    # "chance": ドロップの頻度の英語名。 「always」、「often」、「sometimes」、
    # 「rarely」、「very rarely」、「」のいずれかになります。
    # "quantity": ドロップされたアイテムの数量 (複数の場合)。
    # これらのコンポーネントを使用して、
    # 文法的に正しいランダム ドロップ ヒントを組み立てます。
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy}が{chance}{item}落とす",
        ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "chance": chance,
        }
        if quantity:
            kwargs["item"] = quantity + kwargs["item"]
        if chance:
            kwargs["chance"] += "が"
        return rng.choice(variants).format(**kwargs)

    # 単一の本のヒント エントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "item": アイテムの英語名。
    # "book": コンテナ アイテムの英語名。
    # "parentEntry": コンテナ アイテムのヒント エントリ。
    # コンテナ アイテムの位置ヒントを埋め込むには、
    # isParent オプションを有効にしてhintString に渡す必要があります。
    # これらのコンポーネントを使用して、文法的に正しい本のヒントを組み立てます。
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        parentHint = hintString(hintEntry["parentEntry"], isParent=True)
        if isParent:
            variants = [
                "それは{book}に中にあります、{parentHint}",
            ]
        else:
            variants = [
                "{item}は{book}に中にあります、{parentHint}",
            ]
        kwargs = {
            "book": book,
            "parentHint": parentHint,
            "item": item,
        }
        if quantity:
            kwargs["item"] = quantity + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # 単一の NPC アイテム ヒント エントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "item": アイテムの英語名。
    # "NPC": アイテムを所有する NPC の英語名。
    # "npcLocation": NPC がいる場所の英語名。
    # NPC が場所から場所へと移動する場合は提供されません。
    # "foe": アイテムを入手するために倒さなければならない敵の英語名 (必要な場合)。
    # "foeLocation": 敵がいる場所の英語名。
    # "foeDirections": 敵への方向エントリ。ローカライズされたルートを提供するには、
    # directionsString に渡す必要があります。
    # "isShop": このコンポーネントは、アイテムが NPC ショップにある場合に存在します。
    # これらのコンポーネントを使用して、文法的に正しい NPC アイテム ヒントを組み立てます。
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
                "{npc}が{owns}もの",
            ]
        else:
            variants = [
                "{npc}は{item}{owns}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "所有る",
        }
        if quantity:
            kwargs["item"] = quantity + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "販売る"
        if npcLocation:
            kwargs["npc"] = npcLocation + "で" + kwargs["npc"]
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "{location}で{foe}を倒した後",
                "{directions}の{foe}を倒した後",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint = questHint + "、" + hint
        return hint

    # 単一の固有の敵ドロップヒントエントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "item": アイテムの英語名。
    # "enemy"：アイテムを入手するために倒す必要がある敵の英語名。
    # "directions": 敵への指示エントリ。ローカライズされたルートを提供するには、
    # directionsString に渡す必要があります。
    # これらのコンポーネントを使用して、文法的に正しい固有の敵ドロップ ヒントを組み立てます。
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "{directions}の{enemy}が所有している",
            ]
        else:
            variants = [
                "{directions}の{enemy}は{item}を所有しています",
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] = quantity + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # 単一の宝のヒント エントリのテキストを組み立てます。
    # コンポーネント <hintEntry>:
    # "item": アイテムの英語名。
    # "directions": アイテムの指示エントリ。ローカライズされたルートを提供するには、
    # directionsString に渡す必要があります。
    # これらのコンポーネントを使用して、文法的に正しい宝のヒントを組み立てます。
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "ここは{directions}にあります",
            ]
        else:
            variants = [
                "{item}は{directions}にあります",
            ]
        kwargs = {
            "item": item,
            "directions": directionsString(hintEntry["directions"])
        }
        if quantity:
            kwargs["item"] = quantity + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # このメソッドは、ヒント エントリのコンポーネントに応じて、
    # さまざまなヒント アセンブル メソッドを呼び出します。
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

    # 単一の指示セットのテキストを組み立てます。
    # コンポーネント <directions>:
    # "location": エリアの英語名。
    # "landmark": 基準点として使用されるランドマークの英語名。ランドマークがない場合は、
    # 位置のみを特定する必要があります。
    # "angle"：ランドマークからのコンパスの方向を表す英語。距離がランドマークに近い場合、
    # 角度はありません。
    # "height": 物品がランドマークの上にあるのか、下にあるのかを表す英語。
    # 「far above」、「above」、「below」、「far below」、
    # または「」のいずれかになります。
    # "distance": アイテムがランドマークからどれだけ離れているかを表す英語。 「near」、
    # 「far」、「」のいずれかになります。
    # これらのコンポーネントを使用して、文法的に正しい指示を組み立てます。
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
        directionsHint = location + "の" + landmark + "の"
        if distance:
            directionsHint += distance
            if angle:
                directionsHint += angle
        else:
            directionsHint += angle
        if height:
            directionsHint += "と" + height
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
