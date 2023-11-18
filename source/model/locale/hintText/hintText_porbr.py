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
# Importações específicas portuguesas:


def hintText_porbr(components, localeData):

    # Retorna uma versão localizada do texto passado a ele a partir do
    # localeData fornecido ou, se não existir, apenas retorna o texto.
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        return text

    # Monte o nome do item de dica que aparece nas listas de inventário.
    # Se um componente "hintName" for fornecido, ele deverá ser traduzido
    # diretamente.
    # Componentes <components>:
    # "noteName": A palavra em inglês para o próprio objeto item.
    # "ownerName": A palavra em inglês que descreve o proprietário anterior do
    # item.
    # "ownerAdjective": Um adjetivo opcional em inglês que descreve o
    # proprietário.
    # Use esses componentes para montar um nome aleatório e gramaticalmente
    # correto.
    def hintObjectName():
        # se um nome completo já for fornecido, traduza-o diretamente
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName} do {owner}",
            "A {noteName} do {owner}",
            "{noteName} de um {owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] = ownerAdjective + " " + kwargs["owner"]
        return capitalize(rng.choice(variants).format(**kwargs))

    # Monte a descrição do item de dica que aparece nas descrições do
    # inventário.
    # Se um componente "hintDescription" for fornecido, ele deverá ser
    # traduzido diretamente.
    # <hintName> é o nome totalmente traduzido do item de dica e deve preceder
    # a descrição montada como uma linha separada.
    # Componentes <components>:
    # "noteName": A palavra em inglês para o próprio objeto de item de dica.
    # "noteAdjectives": Dois adjetivos em inglês que descrevem o objeto de
    # item de dica.
    # Use esses componentes para montar uma descrição gramaticalmente correta.
    def hintObjectDescription(hintName):
        # se uma descrição completa já for fornecida, traduza-a diretamente
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\nUm {noteName} {adj1}",
            "{hintName}.\nUm {noteName} {adj1} {adj2}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # Monte o texto de uma única entrada de dica do portão de neblina.
    # Componentes <hintEntry>:
    # "area": O nome em inglês da área inicial.
    # "destArea": O nome em inglês da área de destino.
    # "gate": O nome em inglês para o portão de neblina ou warp
    # "pathAreas": Os nomes em inglês das áreas por onde passam, se existirem.
    # Use esses componentes para montar uma dica de portão de neblina
    # gramaticalmente correta.
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
                "{gate} leva à {dest} através do {path}"
            ]
        else:
            variants = [
                "{gate} leva à {dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # se não houver hintRegion na entrada, não use o texto da área inicial
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "em " + area + ", a " + kwargs["gate"]
        # se o caminho for longo, use o formato mais curto para evitar
        # possíveis truncamentos
        if len(kwargs["path"]) > 90:
            return capitalize(variants[0].format(**kwargs))
        return capitalize(rng.choice(variants).format(**kwargs))

    # Monte o texto de uma única entrada de dica aleatória.
    # Componentes <hintEntry>:
    # "item": O nome em inglês do item.
    # "enemy": O nome em inglês do inimigo que derruba o item.
    # "chance": O nome em inglês para a frequência da queda. Pode ser "always",
    # "often", "sometimes", "rarely", "very rarely" ou "".
    # "quantity": A quantidade do item descartado, se for mais de um.
    # Use esses componentes para montar uma dica de queda aleatória
    # gramaticalmente correta.
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy} {chance}derrubam {item}",
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

    # Monte o texto de uma única entrada de dica de livro.
    # Componentes <hintEntry>:
    # "item": O nome em inglês do item.
    # "book": O nome em inglês do item do contêiner.
    # "parentEntry": a entrada de dica para o item do contêiner. Deve ser
    # passada para hintString com a opção isParent habilitada para incorporar
    # uma dica de localização para o item do contêiner.
    # Use esses componentes para montar uma dica de livro gramaticalmente
    # correta.
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        parentHint = hintString(hintEntry["parentEntry"], isParent=True)
        if isParent:
            variants = [
                "que está no {book}, {parentHint}",
            ]
        else:
            variants = [
                "{item} estão no {book}, {parentHint}",
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

    # Monte o texto de uma única entrada de dica de item NPC.
    # Componentes <hintEntry>:
    # "item": O nome em inglês do item.
    # "NPC": O nome em inglês do NPC que possui o item.
    # "npcLocation": O nome em inglês do local onde o NPC está. Não fornecido
    # se o NPC se mover de um lugar para outro.
    # "foe": O nome em inglês do inimigo que deve ser derrotado para obter o
    # item, se necessário.
    # "foeLocation": O nome em inglês do local onde o inimigo está.
    # "foeDirections": A entrada de direções para o inimigo. Deve ser passado
    # para directionsString para fornecer instruções localizadas.
    # "isShop": Este componente existe se o item estiver em uma loja NPC.
    # Use esses componentes para montar uma dica de item NPC gramaticalmente
    # correta.
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
                "que é {ownedBy} {npc}",
            ]
        else:
            variants = [
                "{npc} {owns} {item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "possui",
            "ownedBy": "propriedade de"
        }
        if quantity:
            kwargs["item"] = quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "vende"
            kwargs["ownedBy"] = "vendido por"
        if npcLocation:
            kwargs["npc"] += " em " + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "depois de derrotar {foe} em {location}",
                "depois de derrotar {foe} {directions}",
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

    # Monte o texto de uma única entrada exclusiva de dica de queda do inimigo.
    # Componentes <hintEntry>:
    # "item": O nome em inglês do item.
    # "enemy": O nome em inglês do inimigo que deve ser derrotado para obter o
    # item.
    # "directions": A entrada de direções para o inimigo. Deve ser passado para
    # directionsString para fornecer instruções localizadas.
    # Use esses componentes para montar uma dica única de lançamento do inimigo
    # gramaticalmente correta.
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "que pertence a um {enemy} {directions}",
            ]
        else:
            variants = [
                "Um {enemy} possui {item} {directions}",
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

    # Monte o texto de uma única entrada de dica de tesouro.
    # Componentes <hintEntry>:
    # "item": O nome em inglês do item.
    # "directions": A entrada de rotas para o item. Deve ser passado para
    # directionsString para fornecer instruções localizadas.
    # Use esses componentes para montar uma dica de tesouro gramaticalmente
    # correta.
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "que fica {directions}",
            ]
        else:
            variants = [
                "{item} estão {directions}",
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

    # Este método chama os vários métodos de montagem de dicas, dependendo dos
    # componentes da entrada da dica.
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

    # Monte o texto de um único conjunto de instruções.
    # Componentes <directions>:
    # "location": O nome em inglês da área.
    # "landmark": O nome em inglês do marco usado como ponto de referência.
    # Se não houver nenhum ponto de referência, apenas o local deverá ser
    # localizado.
    # "angle": As palavras em inglês para a direção da bússola a partir do
    # ponto de referência. Não haverá ângulo se a distância estiver próxima do
    # ponto de referência.
    # "height": As palavras em inglês que indicam se o item está acima ou
    # abaixo do ponto de referência. Pode ser "far above", "above", "below",
    # "far below" ou "".
    # "distance": as palavras em inglês que indicam a distância do ponto de
    # referência do item. Pode ser "near", "far" ou "".
    # Use esses componentes para montar instruções gramaticalmente corretas.
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "em " + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint += " " + angle
        else:
            directionsHint = angle
        directionsHint += " de " + landmark + " em " + location
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
