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
    "packPadx": 10,
    "packPady": 10,
    "packExpand": True,
    "packFill": tk.BOTH,
    "packSide": tk.LEFT
}


class MissableItemsPane(mtk.Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.uiText = self._valueFromController("uiText")
        filterOptions = {
            "filterLabel": self.uiText["filterLabel"],
            "filterTooltip": self.uiText["filterTooltip"],
            "filterButton": self.uiText["filterButton"],
            "filterButtonTooltip": self.uiText["filterButtonTooltip"]
        }
        self.selector = mtk.ListSelector(self,
                                         controller=self._controller,
                                         name="missableItemsSelector",
                                         label=self.uiText["missableLabel"],
                                         tooltip=self.uiText["selectorTooltip"],
                                         allowReorder=False,
                                         selectmode=tk.BROWSE,
                                         **(filterOptions | packOptions))
        frame = mtk.Frame(self, **packOptions)
        mtk.Label(frame, text=self.uiText["spoilersLabel"],
                  tooltip=self.uiText["spoilersTooltip"], packFill=tk.X)
        self.spoilers = mtk.Text(frame, wrap=tk.WORD, enableEdit=False,
                                 packAnchor=tk.NW)
        mtk.HelpIcon(frame, tooltip=self.uiText["helpIcon"], packAnchor=tk.SW)

    def setValue(self, value, key=None):
        self.spoilers.setValue(value)

    def refresh(self):
        self.selector.refresh()

    def reset(self):
        self.selector.reset()
        self.setValue(None)
