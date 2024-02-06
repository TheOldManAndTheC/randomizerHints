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
# สินค้านำเข้าเฉพาะของไทย:


def hintText_thath(components, localeData):

    # ส่งคืนข้อความในเวอร์ชันท้องถิ่นที่ส่งผ่านจาก localeData ที่กำหนด
    # หรือหากไม่มีอยู่ ให้ส่งคืนข้อความนั้น
    def localize(text):
        if not text:
            return text
        if text in localeData:
            return localeData[text]
        # outText = text.replace("\"", "\\\"").replace("\n", "\\n")
        # with open("missingLocalizations.txt", "a", encoding="utf8") as fd:
        #     fd.write("    \"{}\": \"{}\",\n".format(outText, outText))
        return text

    # รวบรวมชื่อของรายการคำใบ้ที่ปรากฏในรายการสินค้าคงคลัง
    # หากมีการระบุองค์ประกอบ "hintName" ก็ควรแปลโดยตรง
    # ส่วนประกอบ <components>:
    # "noteName": คำภาษาอังกฤษสำหรับออบเจ็กต์รายการ
    # "ownerName": คำภาษาอังกฤษที่อธิบายเจ้าของคนก่อนของรายการ
    # "ownerAdjective": คำคุณศัพท์ภาษาอังกฤษที่เป็นทางเลือกซึ่งอธิบายถึงเจ้าของ
    # ใช้ส่วนประกอบเหล่านี้เพื่อรวบรวมชื่อแบบสุ่มและถูกต้องตามหลักไวยากรณ์
    def hintObjectName():
        # หากมีการระบุชื่อเต็มไว้แล้ว ให้แปลโดยตรง
        if "hintName" in components:
            return localize(components["hintName"])
        ownerName = localize(components["ownerName"])
        ownerAdjective = ""
        if "ownerAdjective" in components:
            ownerAdjective = localize(components["ownerAdjective"])
        noteName = localize(components["noteName"])
        variants = [
            "{noteName}ของ{owner}",
        ]
        kwargs = {
            "owner": ownerName,
            "noteName": noteName,
        }
        if ownerAdjective:
            kwargs["owner"] += ownerAdjective
        return rng.choice(variants).format(**kwargs)

    # ประกอบคำอธิบายของรายการคำใบ้ที่ปรากฏในคำอธิบายสินค้าคงคลัง
    # หากมีการระบุองค์ประกอบ "hintDescription" ก็ควรแปลโดยตรง
    # <hintName> เป็นชื่อที่แปลโดยสมบูรณ์ของรายการคำใบ้
    # และควรนำหน้าคำอธิบายที่ประกอบเป็นบรรทัดแยกต่างหาก
    # ส่วนประกอบ <components>:
    # "noteName": คำภาษาอังกฤษสำหรับออบเจ็กต์รายการคำใบ้
    # "noteAdjectives": คำคุณศัพท์ภาษาอังกฤษสองคำที่อธิบายวัตถุรายการคำใบ้
    # ใช้ส่วนประกอบเหล่านี้เพื่อประกอบคำอธิบายที่ถูกต้องตามหลักไวยากรณ์
    def hintObjectDescription(hintName):
        # หากมีคำอธิบายที่สมบูรณ์อยู่แล้ว ให้แปลโดยตรง
        if "hintDescription" in components:
            return localize(components["hintDescription"])
        noteName = localize(components["noteName"])
        adjective1 = localize(components["noteAdjectives"][0])
        adjective2 = localize(components["noteAdjectives"][1])
        variants = [
            "{hintName}.\n{noteName}{adj1}",
            "{hintName}.\n{noteName}{adj1}{adj2}",
        ]
        kwargs = {
            "adj1": adjective1,
            "adj2": adjective2,
            "noteName": noteName,
            "hintName": hintName,
        }
        return rng.choice(variants).format(**kwargs)

    # ประกอบข้อความของรายการคำใบ้ประตูหมอกเดียว
    # ส่วนประกอบ <hintEntry>:
    # "area": ชื่อภาษาอังกฤษของพื้นที่เริ่มต้น
    # "destArea": ชื่อภาษาอังกฤษของพื้นที่ปลายทาง
    # "gate": ชื่อภาษาอังกฤษของประตูหมอกหรือวาร์ป
    # "pathAreas": ชื่อภาษาอังกฤษของพื้นที่ที่ผ่าน ถ้ามี
    # ใช้ส่วนประกอบเหล่านี้เพื่อประกอบคำใบ้ประตูหมอกที่ถูกต้องตามหลักไวยากรณ์
    def fogHint(hintEntry):
        area = localize(hintEntry["area"])
        destArea = localize(hintEntry["destArea"])
        gate = localize(hintEntry["gate"])
        path = ""
        if "pathAreas" in hintEntry:
            for pathArea in hintEntry["pathAreas"]:
                path += localize(pathArea) + " "
            path = path[:-2]
        if path:
            variants = [
                "{gate}นำไปสู่{dest}ผ่าน{path}"
            ]
        else:
            variants = [
                "{gate}นำไปสู่{dest}"
            ]
        kwargs = {
            "dest": destArea,
            "gate": gate,
            "path": path,
        }
        # หากไม่มี hintRegion ในรายการ อย่าใช้ข้อความพื้นที่เริ่มต้น
        if "hintRegion" in hintEntry:
            kwargs["gate"] = "ใน" + area + kwargs["gate"]
        # หากเส้นทางยาว
        # ให้ใช้รูปแบบที่สั้นที่สุดเพื่อหลีกเลี่ยงการตัดทอนที่อาจเกิดขึ้น
        if len(kwargs["path"]) > 90:
            return variants[0].format(**kwargs)
        return rng.choice(variants).format(**kwargs)

    # รวบรวมข้อความของรายการคำใบ้การดรอปแบบสุ่มรายการเดียว
    # ส่วนประกอบ <hintEntry>:
    # "item": ชื่อภาษาอังกฤษของรายการ
    # "enemy": ชื่อภาษาอังกฤษของศัตรูที่ดรอปไอเท็ม
    # "chance": ชื่อภาษาอังกฤษของความถี่ของการดรอป อาจเป็น "always", "often",
    # "sometimes", "rarely", "very rarely" หรือ ""
    # "quantity": ปริมาณของรายการที่ทิ้ง หากมีมากกว่าหนึ่งรายการ
    # ใช้ส่วนประกอบเหล่านี้เพื่อประกอบคำใบ้การดรอปแบบสุ่มที่ถูกต้องตามหลักไวยากรณ์
    def randomDropHint(hintEntry):
        chance = localize(hintEntry["chance"])
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        variants = [
            "{enemy}ทำหล่น{chance}{item}",
        ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "chance": chance,
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # รวบรวมข้อความของรายการคำใบ้หนังสือเล่มเดียว
    # ส่วนประกอบ <hintEntry>:
    # "item": ชื่อภาษาอังกฤษของรายการ
    # "book": ชื่อภาษาอังกฤษสำหรับรายการคอนเทนเนอร์
    # "parentEntry": รายการคำใบ้สำหรับรายการคอนเทนเนอร์ ควรส่งผ่านไปยัง
    # hintString โดยเปิดใช้งานตัวเลือก isParent
    # เพื่อฝังคำใบ้ตำแหน่งสำหรับรายการคอนเทนเนอร์
    # ใช้ส่วนประกอบเหล่านี้เพื่อรวบรวมคำใบ้หนังสือที่ถูกต้องตามหลักไวยากรณ์
    def bookHint(hintEntry, isParent=False):
        book = localize(hintEntry["book"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if "parentEntry" in hintEntry:
            parentHint = hintString(hintEntry["parentEntry"], isParent=True)
        else:
            parentHint = ""
        if isParent:
            variants = [
                "ซึ่งอยู่ใน{book}{parentHint}",
            ]
        else:
            variants = [
                "{item}อยู่ใน{book}{parentHint}",
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

    # รวบรวมข้อความของรายการคำใบ้รายการ NPC รายการเดียว
    # ส่วนประกอบ <hintEntry>:
    # "item": ชื่อภาษาอังกฤษของรายการ
    # "NPC": ชื่อภาษาอังกฤษของ NPC ที่เป็นเจ้าของไอเท็ม
    # "npcLocation": ชื่อภาษาอังกฤษของสถานที่ที่ NPC อยู่ จะไม่ระบุหาก NPC
    # ย้ายจากที่หนึ่งไปยังอีกที่หนึ่ง
    # "foe": ชื่อภาษาอังกฤษของศัตรูที่ต้องพ่ายแพ้เพื่อให้ได้ไอเท็ม หากจำเป็น
    # "foeLocation": ชื่อภาษาอังกฤษของสถานที่ที่ศัตรูอยู่
    # "foeDirections": การเข้าสู่ทิศทางของศัตรู ควรส่งผ่านไปยัง directionsString
    # เพื่อจัดเตรียมทิศทางที่แปลเป็นภาษาท้องถิ่น
    # "isShop": องค์ประกอบนี้มีอยู่หากสินค้าอยู่ในร้านค้า NPC
    # ใช้ส่วนประกอบเหล่านี้เพื่อประกอบคำใบ้รายการ NPC ที่ถูกต้องตามหลักไวยากรณ์
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
                    "ซึ่งขายโดย{npc}",
                ]
            else:
                variants = [
                    "ซึ่ง{npc}เป็นเจ้าของ",
                ]
        else:
            variants = [
                "{npc}{owns}{item}",
            ]
        kwargs = {
            "item": item,
            "npc": npc,
            "owns": "เป็นเจ้าของ",
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        if "isShop" in hintEntry:
            kwargs["owns"] = "ขาย"
        if npcLocation:
            kwargs["npc"] += "ใน" + npcLocation
        hint = rng.choice(variants).format(**kwargs)
        if foe:
            variants = [
                "หลังจากเอาชนะ{foe}ใน{location}",
                "หลังจากเอาชนะ{foe}{directions}",
            ]
            kwargs = {
                "foe": foe,
                "location": foeLocation,
                "directions": foeDirections,
            }
            questHint = rng.choice(variants).format(**kwargs)
            hint += questHint
        return hint

    # รวบรวมข้อความรายการคำใบ้ดรอปของศัตรูที่ไม่ซ้ำใคร
    # ส่วนประกอบ <hintEntry>:
    # "item": ชื่อภาษาอังกฤษของรายการ
    # "enemy": ชื่อภาษาอังกฤษของศัตรูที่ต้องพ่ายแพ้เพื่อรับไอเทม
    # "directions": การเข้าสู่ทิศทางของศัตรู ควรส่งผ่านไปยัง directionsString
    # เพื่อจัดเตรียมทิศทางที่แปลเป็นภาษาท้องถิ่น
    # ใช้ส่วนประกอบเหล่านี้เพื่อรวบรวมคำใบ้การดรอปของศัตรูที่เป็นเอกลักษณ์ตามหลักไวยากรณ์
    def enemyHint(hintEntry, isParent=False):
        enemy = localize(hintEntry["enemy"])
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "หลังจากเอาชนะ{enemy}{directions}",
            ]
        else:
            variants = [
                "{enemy}เป็นเจ้าของ{item}{directions}",
            ]
        kwargs = {
            "item": item,
            "enemy": enemy,
            "directions": directionsString(hintEntry["directions"]),
        }
        if quantity:
            kwargs["item"] = " " + quantity + " " + kwargs["item"]
        return rng.choice(variants).format(**kwargs)

    # รวบรวมข้อความของรายการคำใบ้สมบัติรายการเดียว
    # ส่วนประกอบ <hintEntry>:
    # "item": ชื่อภาษาอังกฤษของรายการ
    # "directions": รายการเส้นทางสำหรับรายการ ควรส่งผ่านไปยัง directionsString
    # เพื่อจัดเตรียมทิศทางที่แปลเป็นภาษาท้องถิ่น
    # ใช้ส่วนประกอบเหล่านี้เพื่อรวบรวมคำใบ้สมบัติที่ถูกต้องตามหลักไวยากรณ์
    def treasureHint(hintEntry, isParent=False):
        item = localize(hintEntry["item"])
        quantity = hintEntry["quantity"]
        if isParent:
            variants = [
                "ซึ่งอยู่{directions}",
            ]
        else:
            variants = [
                "{item}นอยู่{directions}",
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

    # เมธอดนี้เรียกวิธีการประกอบคำใบ้ต่างๆ ขึ้นอยู่กับส่วนประกอบของรายการคำใบ้
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

    # ประกอบข้อความชุดคำสั่งชุดเดียว
    # ส่วนประกอบ <directions>:
    # "location": ชื่อภาษาอังกฤษของพื้นที่
    # "landmark": ชื่อภาษาอังกฤษของจุดสังเกตที่ใช้เป็นจุดอ้างอิง
    # หากไม่มีจุดสังเกต ควรแปลเฉพาะตำแหน่งเท่านั้น
    # "angle": คำภาษาอังกฤษสำหรับบอกทิศทางของเข็มทิศจากจุดสังเกต
    # จะไม่มีมุมหากระยะห่างใกล้จุดสังเกต
    # "height": คำภาษาอังกฤษว่ารายการนั้นอยู่ด้านบนหรือด้านล่างจุดสังเกต อาจเป็น
    # "far above", "above", "below", "far below" หรือ ""
    # "distance": คำภาษาอังกฤษที่หมายถึงระยะห่างจากจุดสังเกตของรายการนั้น
    # อาจเป็น
    # "near" "far" หรือ ""
    # ใช้ส่วนประกอบเหล่านี้เพื่อประกอบคำแนะนำที่ถูกต้องตามหลักไวยากรณ์
    def directionsString(directions):
        location = localize(directions["location"])
        landmark = localize(directions["landmark"])
        angle = localize(directions["angle"])
        height = localize(directions["height"])
        distance = localize(directions["distance"])
        if not location:
            return ""
        if not landmark:
            return "ใน" + location
        if distance:
            directionsHint = distance
            if angle:
                directionsHint = angle + directionsHint
        else:
            directionsHint = angle
        directionsHint += "ของ" + landmark + "ใน" + location
        if height:
            directionsHint = height + "และ" + directionsHint
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
