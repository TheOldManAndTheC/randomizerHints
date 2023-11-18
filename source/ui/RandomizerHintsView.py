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
from source.ui.SettingsPane import SettingsPane
from source.ui.MissableItemsPane import MissableItemsPane
from source.ui.CategorySelectionsPane import CategorySelectionsPane
from source.ui.StartingItemsPane import StartingItemsPane
from source.ui.EditCategoriesPane import EditCategoriesPane

packOptions = {
    "packFill": tk.BOTH,
    "packExpand": True,
}
pad = {
    "packPadx": 10,
    "packPady": 10,
}


class RandomizerHintsView(mtk.View):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.root.iconbitmap(self._valueFromController("iconPath"))
        self.uiText = self._valueFromController("uiText")
        register = {"controller": self.controller()}
        self.notebook = mtk.Notebook(self, name="currentTab",
                                     **(register | packOptions))
        self.notebook.add(SettingsPane(self, name="settingsPane",
                                       **(register | packOptions | pad)),
                          text=self.uiText["settingsTab"])
        self.notebook.add(MissableItemsPane(self, name="missablePane",
                                            **(register | packOptions | pad)),
                          text=self.uiText["missableTab"])
        self.notebook.add(StartingItemsPane(self, name="startingPane",
                                            **(register | packOptions | pad)),
                          text=self.uiText["startingTab"])
        self.notebook.add(CategorySelectionsPane(self, name="selectionsPane",
                                                 **(register | packOptions |
                                                    pad)),
                          text=self.uiText["selectCategoriesTab"])
        self.notebook.add(EditCategoriesPane(self, name="editPane",
                                             **(register | packOptions | pad)),
                          text=self.uiText["editCategoriesTab"])
        # reset the notebook after adding all the panes to get the saved tab
        # back
        self.reset()
