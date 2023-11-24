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

import tkinter as tk
import source.pkg.mvcTkinter as mtk

left = {"packSide": tk.LEFT}
top = {"packSide": tk.TOP}
fillX = {"packFill": tk.X}
fillBoth = {"packFill": tk.BOTH}
expand = {"packExpand": True}
padx10 = {"packPadx": 10}
padx5 = {"packPadx": 5}
pady5 = {"packPady": 5}


class StartingItemsPane(mtk.Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.uiText = self._valueFromController("uiText")
        self.selectedSlot = None
        self.itemList = []
        filterOptions = {
            "filterLabel": self.uiText["filterLabel"],
            "filterTooltip": self.uiText["filterTooltip"],
            "filterButton": self.uiText["filterButton"],
            "filterButtonTooltip": self.uiText["filterButtonTooltip"]
        }
        maidenBuilderSelector = filterOptions | {
            "name": "startingMaidenBuilderSelector",
            "label": self.uiText["maidenLabel"],
            "properties": {
                "drop": {
                    "tag": self.uiText["propertyDropTag"],
                    "propertyType": "bool",
                    "buttonText": self.uiText["propertyDropButton"],
                    "tooltip": self.uiText["propertyDropTooltip"]
                },
                "quantity": {
                    "tag": self.uiText["propertyQtyTag"],
                    "propertyType": "int",
                    "minvalue": 1,
                    "maxvalue": 255,
                    "buttonText": self.uiText["propertyQtyButton"],
                    "title": self.uiText["propertyQtyTitle"],
                    "prompt": self.uiText["propertyQtyPrompt"],
                    "tooltip": self.uiText["propertyQtyTooltip"]
                },
                "isItem": {
                    "tag": self.uiText["propertyItemTag"],
                    "propertyType": "bool",
                },
                "isItemHint": {
                    "tag": self.uiText["propertyHintTag"],
                    "propertyType": "bool",
                },
                "isCategory": {
                    "tag": self.uiText["propertyCategoryTag"],
                    "propertyType": "bool",
                }
            },
            "tooltip": self.uiText["maidenTooltip"]
        }
        maidenBuilderSources = [filterOptions | {
            "name": "startingMaidenItemList",
            "label": self.uiText["itemListLabel"],
            "tooltip": self.uiText["itemListTooltip"],
            "dataReturn": {"isItem": True},
        }, filterOptions | {
            "name": "startingMaidenHintList",
            "label": self.uiText["hintListLabel"],
            "tooltip": self.uiText["hintListTooltip"],
            "dataReturn": {"isItemHint": True},
        }, filterOptions | {
            "name": "startingMaidenCategoryList",
            "label": self.uiText["categoryListLabel"],
            "tooltip": self.uiText["categoryListTooltip"],
            "dataReturn": {"isCategory": True},
        }]
        maidenFrame = mtk.Frame(self, **(left | fillBoth | expand))
        self.maidenBuilder = \
            mtk.ListBuilder(maidenFrame,
                            controller=self.controller(),
                            name="startingMaidenBuilder",
                            builderButtonTooltip=\
                                self.uiText["builderButtonTooltip"],
                            selectorOptions=maidenBuilderSelector,
                            sourceOptions=maidenBuilderSources,
                            **(top | padx10 | pady5 | fillBoth | expand))
        self.maidenSpaceVar = mtk.StringVar(self)
        mtk.Label(maidenFrame, textvariable=self.maidenSpaceVar,
                  tooltip=self.uiText["maidenSpaceTooltip"],
                  **(top | padx10 | pady5))
        shopFrame = mtk.Frame(self, borderwidth=2, relief="ridge", packPady=2,
                              packPadx=20, **(left | fillBoth | expand))
        inventoryFrame = mtk.Frame(shopFrame,
                                   **(left | padx5 | fillBoth | expand))
        mtk.Label(inventoryFrame, text=self.uiText["shopLabel"],
                  justify=tk.CENTER, tooltip=self.uiText["shopTooltip"],
                  **(top | pady5 | padx5 | fillX))
        self.inventoryListVar = mtk.Variable(self, value=[])
        self.inventoryListBox = mtk.Listbox(inventoryFrame, height=21,
                                            listvariable=self.inventoryListVar,
                                            **(top | fillX))
        self.inventoryListBox.registerObserver(self)
        mtk.Scrollbar(inventoryFrame, axis=tk.X,
                      scrollWidget=self.inventoryListBox, **(top | fillX))
        frame = mtk.Frame(inventoryFrame, **(top | pady5 | fillX))
        self.slotVar = mtk.StringVar(self,
                                     value=self.uiText["slotLabel"] + " :")
        mtk.Label(frame, textvariable=self.slotVar, **(left | pady5))
        mtk.Button(
            frame, text="<-", tooltip=self.uiText["useItemTooltip"],
            command=lambda *_: self._notifyObservers(self, "replaceShopItem"),
            packSide=tk.RIGHT
        )
        self.itemVar = mtk.StringVar(self, value="")
        mtk.Label(inventoryFrame, textvariable=self.itemVar, **(top | fillX))
        frame = mtk.Frame(inventoryFrame, packPady=20, **(top | fillX))
        mtk.Button(
            frame, text=self.uiText["priceButton"],
            command=lambda *_: self._notifyObservers(self, "setItemPrice"),
            tooltip=self.uiText["priceTooltip"],
            **left
        )
        self.loadShopButton = mtk.Button(
            frame, text=self.uiText["loadButton"],
            command=lambda *_: self._notifyObservers(self, "loadShopInventory"),
            tooltip=self.uiText["loadTooltip"],
            packSide=tk.RIGHT
        )
        mtk.HelpIcon(inventoryFrame, tooltip=self.uiText["helpIcon"],
                     packSide=tk.BOTTOM)
        self.itemSelector = mtk.ListSelector(
            shopFrame,
            controller=self.controller(),
            name="startingShopItemList",
            label=self.uiText["itemListLabel"],
            tooltip=self.uiText["itemListTooltip"],
            allowReorder=False,
            **(filterOptions | left | pady5 | fillBoth | expand)
        )
        self.inventorySource = None

    def value(self, key=None):
        match key:
            case mtk.SELECTION | mtk.SELECTED_ITEMS:
                return self.inventoryListBox.value(key)
            case "selectedLotID":
                if self.selectedSlot is None:
                    return None
                return list(self.inventorySource.keys())[self.selectedSlot]
            case "selectedEntry":
                lotID = self.value("selectedLotID")
                if lotID is None:
                    return None
                return self.inventorySource[lotID]
        return None

    def setValue(self, value, key=None):
        match key:
            case mtk.SOURCE:
                if value is None:
                    value = dict()
                self.inventorySource = value
                self.setValue(None, mtk.SELECTION_CLEAR)
            case mtk.SELECTION_CLEAR:
                self.maidenBuilder.setValue(None, mtk.SELECTION_CLEAR)
                self.inventoryListBox.setValue(None, mtk.SELECTION_CLEAR)
                self.selectedSlot = None
            case "maidenSpace":
                self.maidenSpaceVar.set(value)

    def widgetUpdated(self, widget, event=None, key=None, **kwargs):
        if not self.inventoryListBox.value(mtk.SELECTION):
            return
        self.selectedSlot = self.inventoryListBox.value(mtk.SELECTION)[0]
        self._refreshItem()
        self._notifyObservers(self, "selectionChanged")

    def reset(self):
        self.maidenBuilder.reset()
        self.itemSelector.reset()
        self.setValue(self._valueFromController("source"), mtk.SOURCE)
        self.refresh()

    def refresh(self):
        self.maidenBuilder.refresh()
        itemList = []
        for lotID in self.inventorySource:
            itemEntry = self.inventorySource[lotID]
            itemList.append(itemEntry["displayName"] + " (" +
                            str(itemEntry["value"]) + ")")
        self.inventoryListVar.set(itemList)
        self._refreshItem()
        self.setValue(self._valueFromController("maidenSpace"), "maidenSpace")

    def _refreshItem(self):
        if self.selectedSlot is None:
            slotText = ""
            itemText = ""
        else:
            slotText = str(self.selectedSlot + 1)
            itemText = self.value("selectedEntry")["displayName"]
        self.slotVar.set(self.uiText["slotLabel"] + " " + slotText + ":")
        self.itemVar.set(itemText)

    def destroy(self) -> None:
        self.inventoryListBox.unregisterObserver(self)
        super().destroy()
