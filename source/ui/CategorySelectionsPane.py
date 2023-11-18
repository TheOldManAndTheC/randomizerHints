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

packOptions = {
    "packSide": tk.TOP,
    "packFill": tk.BOTH,
    "packExpand": True,
    "packPadx": 10,
}


class CategorySelectionsPane(mtk.Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.uiText = self._valueFromController("uiText")
        filterOptions = {
            "filterLabel": self.uiText["filterLabel"],
            "filterTooltip": self.uiText["filterTooltip"],
            "filterButton": self.uiText["filterButton"],
            "filterButtonTooltip": self.uiText["filterButtonTooltip"]
        }
        generalBuilderSelector = filterOptions | {
            "name": "selectionsGeneralBuilderSelector",
            "label": self.uiText["generalLabel"],
            "tooltip": self.uiText["generalTooltip"]
        }
        generalCategorySources = [filterOptions | {
            "name": "selectionsGeneralCategories",
            "label": self.uiText["categoriesLabel"],
            "tooltip": self.uiText["categoriesTooltip"]
        }]
        chestBuilderSelector = filterOptions | {
            "name": "selectionsChestBuilderSelector",
            "label": self.uiText["chestLabel"],
            "tooltip": self.uiText["chestTooltip"]
        }
        chestCategorySources = [filterOptions | {
            "name": "selectionsChestCategories",
            "label": self.uiText["categoriesLabel"],
            "tooltip": self.uiText["categoriesTooltip"]
        }]
        bossBuilderSelector = filterOptions | {
            "name": "selectionsBossBuilderSelector",
            "label": self.uiText["bossLabel"],
            "tooltip": self.uiText["bossTooltip"]
        }
        bossCategorySources = [filterOptions | {
            "name": "selectionsBossCategories",
            "label": self.uiText["categoriesLabel"],
            "tooltip": self.uiText["categoriesTooltip"]
        }]
        self.generalBuilder = mtk.ListBuilder(
            self,
            controller=self._controller,
            name="selectionsGeneralBuilder",
            builderButtonTooltip=self.uiText["builderButtonTooltip"],
            selectorOptions=generalBuilderSelector,
            sourceOptions=generalCategorySources,
            **packOptions
        )
        self.chestBuilder = mtk.ListBuilder(
            self,
            controller=self._controller,
            name="selectionsChestBuilder",
            builderButtonTooltip=self.uiText["builderButtonTooltip"],
            selectorOptions=chestBuilderSelector,
            sourceOptions=chestCategorySources,
            **packOptions
        )
        self.bossBuilder = mtk.ListBuilder(
            self,
            controller=self._controller,
            name="selectionsBossBuilder",
            builderButtonTooltip=self.uiText["builderButtonTooltip"],
            selectorOptions=bossBuilderSelector,
            sourceOptions=bossCategorySources,
            **packOptions
        )
        buttonFrame = mtk.Frame(self, **packOptions)
        self.defaultButton = \
            mtk.Button(buttonFrame, text=self.uiText["defaultButton"],
                       command=lambda *_: self._notifyObservers(
                           self, "reloadDefaultActiveCategories"
                       ),
                       tooltip=self.uiText["defaultTooltip"],
                       packSide=tk.LEFT, packPadY=10)
        mtk.HelpIcon(buttonFrame, tooltip=self.uiText["helpIcon"],
                     packSide=tk.RIGHT)

    def reset(self):
        self.generalBuilder.reset()
        self.chestBuilder.reset()
        self.bossBuilder.reset()

    def refresh(self):
        self.generalBuilder.refresh()
        self.chestBuilder.refresh()
        self.bossBuilder.refresh()
