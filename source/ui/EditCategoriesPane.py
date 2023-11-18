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

top = {"packSide": tk.TOP}
left = {"packSide": tk.LEFT}
fillX = {"packFill": tk.X}
fillBoth = {"packFill": tk.BOTH}
expand = {"packExpand": True}
padX10 = {"packPadx": 10}


class EditCategoriesPane(mtk.Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.uiText = self._valueFromController("uiText")
        filterOptions = {
            "filterLabel": self.uiText["filterLabel"],
            "filterTooltip": self.uiText["filterTooltip"],
            "filterButton": self.uiText["filterButton"],
            "filterButtonTooltip": self.uiText["filterButtonTooltip"]
        }
        categoriesFrame = mtk.Frame(self, **(top | fillBoth | expand))
        self.categorySelector = mtk.ListSelector(
            categoriesFrame,
            controller=self._controller,
            name="editCategorySelector",
            label=self.uiText["categoryLabel"],
            tooltip=self.uiText["categoryTooltip"],
            selectmode=tk.BROWSE,
            **(filterOptions | left | padX10 | fillBoth | expand)
        )
        categoryBuilderSelector = filterOptions | {
            "name": "editCategoryBuilderSelector",
            "properties": {
                "drop": {
                    "tag": self.uiText["propertyDropTag"],
                    "propertyType": "bool",
                    "buttonText": self.uiText["propertyDropButton"],
                    "tooltip": self.uiText["propertyDropTooltip"]
                }
            },
            "tooltip": self.uiText["builderTooltip"]
        }
        categoryBuilderSources = [filterOptions | {
            "name": "editCategoryBuilderItemList",
            "label": self.uiText["itemListLabel"],
            "tooltip": self.uiText["itemListTooltip"],
            "dataReturn": dict()
        }]
        self.categoryBuilder = mtk.ListBuilder(
            categoriesFrame,
            controller=self._controller,
            name="editCategoryBuilder",
            builderButtonTooltip=self.uiText["builderButtonTooltip"],
            selectorOptions=categoryBuilderSelector,
            sourceOptions=categoryBuilderSources,
            **(left | fillBoth | expand)
        )
        buttonsFrame = mtk.Frame(self, **(top | fillX))
        self.addButton = mtk.Button(
            buttonsFrame,
            text=self.uiText["addButton"],
            tooltip=self.uiText["addTooltip"],
            command=lambda *_: self._notifyObservers(self, "addCategory"),
            **(left | padX10)
        )
        self.duplicateButton = mtk.Button(
            buttonsFrame,
            text=self.uiText["duplicateButton"],
            tooltip=self.uiText["duplicateTooltip"],
            command=lambda *_: self._notifyObservers(self, "duplicateCategory"),
            **(left | padX10)
        )
        self.renameButton = mtk.Button(
            buttonsFrame,
            text=self.uiText["renameButton"],
            tooltip=self.uiText["renameTooltip"],
            command=lambda *_: self._notifyObservers(self, "renameCategory"),
            **(left | padX10)
        )
        self.removeButton = mtk.Button(
            buttonsFrame,
            text=self.uiText["removeButton"],
            tooltip=self.uiText["removeTooltip"],
            command=lambda *_: self._notifyObservers(self, "removeCategory"),
            **(left | padX10)
        )
        self.reloadButton = mtk.Button(
            buttonsFrame,
            text=self.uiText["reloadButton"],
            tooltip=self.uiText["reloadTooltip"],
            command=lambda *_: self._notifyObservers(self,
                                                     "reloadDefaultCategories"),
            packPadx=30,
            **left
        )
        mtk.HelpIcon(buttonsFrame, tooltip=self.uiText["helpIcon"],
                     packSide=tk.RIGHT)

    def value(self, key=None):
        return self.categorySelector.value(key)

    def setValue(self, value, key=None):
        match key:
            case mtk.SELECTION_CLEAR:
                self.categorySelector.setValue(None, key)
                self.setValue("", mtk.LABEL)
                self.setValue(None, mtk.SOURCE)
            case mtk.LABEL | mtk.SOURCE:
                self.categoryBuilder.selector.setValue(value, key)

    def refresh(self):
        self.categorySelector.refresh()
        self.categoryBuilder.refresh()

    def reset(self):
        self.categorySelector.reset()
        self.categoryBuilder.reset()
        self.setValue(None, mtk.SELECTION_CLEAR)
