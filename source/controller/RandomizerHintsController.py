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

import importlib
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
import source.pkg.mvcTkinter as mtk
import source.pkg.mvcTkinter.core.fileIO as fileIO
from source.ui.RandomizerHintsView import RandomizerHintsView
from source.model.RandomizerHintsModel import RandomizerHintsModel

validDialogArgs = ["title", "prompt", "minvalue", "maxvalue", "initialvalue"]
validationSettings = ["gameExe", "randomizerExe", "yabberExe",
                      "dsmsPortableExe", "fogRandomizerExe", "useRandomizer",
                      "useFogRandomizer"]
categoryWidgets = ["selectionsPane", "startingPane", "editPane"]
iconPath = "source/pkg/scroll-paper/scroll-paper.ico"
uiTextModule = "source.data.locale.uiText."
languages = {
    "engus": "English",
    "deude": "Deutsch",
    "frafr": "Français",
    "itait": "Italiano",
    "jpnjp": "日本語",
    "korkr": "한국어",
    "polpl": "Polski",
    "porbr": "Português-Brasil",
    "rusru": "Русский",
    "spaar": "Español-Latinoamérica",
    "spaes": "Español-España",
    "thath": "ไทย",
    "zhocn": "简体中文",
    "zhotw": "繁體中文",
}


class RandomizerHintsController(mtk.Controller):
    def __init__(self, **options):
        super().__init__(**options)
        self._isResetting = False
        hasSettings = fileIO.readSettings()
        if self.option("modelOptions"):
            self.setModel(RandomizerHintsModel(**(self.option("modelOptions") |
                                                  {"controller": self})))
        if not hasSettings:
            self.model().update("defaultSettings")
        uiTextName = "uiText_" + self.settingValue("language")
        self._allUIText = \
            getattr(importlib.import_module(uiTextModule + uiTextName),
                    uiTextName)
        self._uiText = self._allUIText[self.name()]

        self.model().update("checkLocale")
        if self.option("viewOptions"):
            self.setView(RandomizerHintsView(**(self.option("viewOptions") |
                                                {"controller": self})))
            self._viewActivated()

    def setSetting(self, setting, value, write=True):
        super().setSetting(setting, value, write)
        match setting:
            case "shopItems":
                self.widgets["startingPane"].reset()
        if setting in validationSettings and self._viewActive and \
                not self._isResetting:
            self._validate()

    def output(self, key=None, *args):
        if key is None:
            print(*args)
            return
        print(self._uiText[key].format(*args))

    def _viewActivated(self):
        super()._viewActivated()
        self.view().update()
        self._validate()

    def _validate(self):
        self.model().update("validate")
        self.widgets["missableItemsSelector"].setValue(
            self.model().value("missable"),
            mtk.SOURCE
        )
        self._updateMaidenSpace()

    def _askYesNo(self, titleKey="", promptKey=""):
        return askyesno(parent=self.view().root, title=self._uiText[titleKey],
                        message=self._uiText[promptKey])

    def _showWarning(self, titleKey="", promptKey=""):
        showwarning(self._uiText[titleKey], self._uiText[promptKey])

    def _setUIState(self, group, enable):
        if enable:
            state = "normal"
        else:
            state = "disabled"
        self.widgets["settingsPane"].setState(state, group)
        if group == "ready" or group == "build":
            notebook = self.widgets["currentTab"]
            notebook.setState(state, range(1, notebook.index("end")))
        if self._viewActive:
            self.view().update_idletasks()

    def _refreshCategoryWidgets(self):
        for widgetName in categoryWidgets:
            self.widgets[widgetName].refresh()

    def _resetCategoryWidgets(self):
        self._isResetting = True
        for widgetName in categoryWidgets:
            self.widgets[widgetName].reset()
        self._isResetting = False

    def modelUpdated(self, key, **kwargs):
        match key:
            case "randomizer" | "fog" | "starting" | "ready" | "build":
                self._setUIState(key, kwargs["state"])
                return
            case "shopChanged":
                self._showWarning("shopChangedTitle", "shopChangedPrompt")
                return
        return super().modelUpdated(key, **kwargs)

    def valueForWidget(self, widget, key=None, **kwargs):
        match key:
            case mtk.SOURCE:
                return self._sourceForWidget(widget)
            case mtk.LIST_SELECTOR_PROPERTY_VALIDATE:
                match kwargs["propertyKey"]:
                    case "quantity":
                        if widget.name() == "startingMaidenBuilderSelector":
                            return self.model().value("checkMaidenSpace",
                                                      **kwargs)
                    case "drop":
                        entry = widget.value(mtk.SOURCE)[kwargs["selection"]]
                        if "isItem" in entry or "isCategory" in entry:
                            return False
                return True
            case mtk.LIST_BUILDER_VALIDATE_ADD:
                if widget.name() == "startingMaidenBuilder":
                    return self.model().value("checkMaidenSpace", **kwargs)
                return True
            case mtk.LIST_BUILDER_VALIDATE_REMOVE:
                return True
            case "uiText":
                if widget.name() in self._allUIText:
                    return self._allUIText["**COMMON**"] | \
                        self._allUIText[widget.name()]
                else:
                    return None
            case "maidenSpace":
                return self._maidenSpace()
            case "languages":
                return list(languages.values())
            case "iconPath":
                return fileIO.resourcePath(iconPath)
            case None:
                if widget.name() == "language":
                    return languages[self.settingValue(widget.name())]
                return self.settingValue(widget.name())
        return None

    def widgetUpdated(self, widget, event=None, key=None, **kwargs):
        match event:
            case mtk.SELECTION_CHANGED:
                self._selectionChanged(widget)
            case mtk.BUTTON_PRESSED:
                match widget.name():
                    case "loadSettings":
                        self._loadSettings()
                    case "saveSettings":
                        self._saveSettings()
                    case "importSettings":
                        self._importSettings()
                    case "exportSettings":
                        self._exportSettings()
                    case "copyConsole":
                        self.view().root.clipboard_clear()
                        self.view().root.clipboard_append(
                            self.widgets["console"].value()
                        )
                    case "clearConsole":
                        if self._askYesNo("clearConsoleTitle",
                                          "clearConsolePrompt"):
                            self.widgets["console"].setValue(None)
                    case "buildHints":
                        self.model().update(widget.name())
            case mtk.LIST_SELECTOR_PROPERTY_BUTTON_PRESSED | \
                 mtk.LIST_BUILDER_BUTTON_PRESSED:
                fileIO.writeSettings()
                if widget.name() == "startingMaidenBuilder" or \
                        widget.name() == "startingMaidenBuilderSelector":
                    self._updateMaidenSpace()
                    if key == "invalid" and kwargs:
                        match kwargs["propertyKey"]:
                            case "quantity":
                                self._showWarning("invalidMaidenTitle",
                                                  "fullMaidenPrompt")
                            case "drop":
                                self._showWarning("invalidPropertyTitle",
                                                  "invalidDropPrompt")
            case mtk.LIST_SELECTOR_REORDERED:
                self._refreshCategoryWidgets()
                fileIO.writeSettings()
            case "addCategory":
                self._addCategory()
            case "duplicateCategory":
                selectedItems = widget.value(mtk.SELECTED_ITEMS)
                if len(selectedItems) == 1:
                    self._addCategory(selectedItems[0])
            case "removeCategory" | "renameCategory":
                self._changeCategory(widget, event)
            case "reloadDefaultCategories" | "reloadDefaultActiveCategories":
                self._reloadDefaultCategories(event)
            case "loadShopInventory":
                if self._askYesNo("shopTitle", "shopPrompt"):
                    self.model().update(event)
            case "replaceShopItem":
                self._modifyShopItem(widget, "replace")
            case "setItemPrice":
                self._modifyShopItem(widget, "price")
            case "customSeed":
                self.setSetting("customSeed", widget.value("customSeed"))
            case "customFogSeed":
                self.setSetting("customFogSeed", widget.value("customFogSeed"))
            case _:
                if widget.name() == "language":
                    key = next(key for key, value in languages.items()
                               if value == widget.value())
                    if key != self.settingValue(widget.name()):
                        self._showWarning("changeLanguageTitle_" + key,
                                          "changeLanguagePrompt_" + key)
                    self.setSetting(widget.name(), key)
                    return
                self.setSetting(widget.name(), widget.value())

    def _sourceForWidget(self, widget):
        sourceKey = None
        match widget.name():
            case "editCategorySelector" | "startingMaidenCategoryList" | \
                 "selectionsGeneralCategories" | "selectionsChestCategories" | \
                 "selectionsBossCategories":
                sourceKey = "hintCategories"
            case "selectionsGeneralBuilderSelector":
                sourceKey = "generalCategories"
            case "selectionsChestBuilderSelector":
                sourceKey = "chestCategories"
            case "selectionsBossBuilderSelector":
                sourceKey = "bossCategories"
            case "startingMaidenHintList" | "startingShopItemList" | \
                 "editCategoryBuilderItemList" | "startingMaidenItemList":
                sourceKey = "itemInfo"
            case "startingMaidenBuilderSelector":
                sourceKey = "maidenItems"
            case "startingPane":
                sourceKey = "shopItems"
            case "missableItemsSelector":
                sourceKey = "missable"
        return self.model().value(sourceKey)

    def _selectionChanged(self, widget):
        match widget.name():
            case "editCategorySelector":
                if len(widget.value(mtk.SELECTION)) > 0:
                    self._setEditCategory(widget.value(mtk.SELECTED_ITEMS)[0])
            case "missableItemsSelector":
                missable = self.model().value("missable")
                if len(widget.value(mtk.SELECTION)) < 1 or not missable:
                    self.widgets["missablePane"].setValue(None)
                else:
                    self.widgets["missablePane"].setValue(
                        missable[widget.value(mtk.SELECTED_ITEMS)[0]]
                    )

    def _setEditCategory(self, category=""):
        if category:
            source = self.model().value("category", name=category)
            category += ":"
        else:
            source = None
        pane = self.widgets["editPane"]
        pane.setValue(category, mtk.LABEL)
        pane.setValue(source, mtk.SOURCE)

    def _maidenSpace(self):
        return self._uiText["maidenSpace"].format(
            *self.model().value("maidenItemsCount")
        )

    def _updateMaidenSpace(self):
        self.widgets["startingPane"].setValue(self._maidenSpace(),
                                              "maidenSpace")

    def _modifyShopItem(self, widget, mod):
        lotID = widget.value("selectedLotID")
        if lotID is None:
            return
        if mod == "replace":
            selectedItems = \
                self.widgets["startingShopItemList"].value(mtk.SELECTED_ITEMS)
            if not selectedItems:
                return
            self.model().update("modifyShopItem", lotID=lotID,
                                newName=selectedItems[0])
        elif mod == "price":
            value = sd.askinteger(parent=self.view().root,
                                  title=self._uiText["itemPriceTitle"],
                                  prompt=self._uiText["itemPricePrompt"],
                                  minvalue=1)
            if value is None:
                return
            self.model().update("modifyShopItem", lotID=lotID, value=value)
        fileIO.writeSettings()
        widget.refresh()

    def _addCategory(self, categoryToCopy=None):
        newName = sd.askstring(self._uiText["newTitle"],
                               self._uiText["newPrompt"],
                               parent=self.view().root)
        if newName is None or \
                not self.model().update("addCategory", newName=newName,
                                        categoryToCopy=categoryToCopy):
            return
        fileIO.writeSettings()
        self._refreshCategoryWidgets()
        widget = self.widgets["editCategorySelector"]
        widget.setValue(None, mtk.SELECTION_CLEAR)
        widget.setValue(tk.END, mtk.SELECTION_SET)
        widget.setValue(tk.END, mtk.SELECTION_ANCHOR)
        widget.see(tk.END)
        self._selectionChanged(widget)

    def _changeCategory(self, widget, event):
        selectedItems = widget.value(mtk.SELECTED_ITEMS)
        if len(selectedItems) < 1:
            return
        name = selectedItems[0]
        if event == "renameCategory":
            newName = sd.askstring(self._uiText["renameTitle"],
                                   self._uiText["renamePrompt"],
                                   parent=self.view().root)
            if newName is None or not self.model().update(event, name=name,
                                                          newName=newName):
                return
            self._setEditCategory(newName)
            self.widgets["editCategorySelector"].see(tk.END)
        elif event == "removeCategory":
            self.model().update(event, name=name)
            widget.refresh()
            selectedItems = widget.value(mtk.SELECTED_ITEMS)
            if len(selectedItems) < 1:
                self._setEditCategory()
            else:
                self._setEditCategory(selectedItems[0])
        fileIO.writeSettings()
        self._resetCategoryWidgets()

    def _reloadDefaultCategories(self, event):
        if event == "reloadDefaultCategories":
            prompt = "reloadPrompt"
            key = "defaultCategories"
        else:
            prompt = "reloadActivePrompt"
            key = "defaultActiveCategories"
        if self._askYesNo("reloadTitle", prompt):
            self.model().update(key)
        else:
            return
        self._resetCategoryWidgets()

    def _loadSettings(self):
        path = fd.askopenfilename(
            parent=self.view().root,
            title=self._uiText["loadSettingsTitle"],
            initialdir="settings",
            filetypes=[(self._uiText["settingsFileType"], "*.rhs")],
        )
        if not path:
            return
        self.output("loadSettingsText")
        fileIO.readSettings(path)
        self._isResetting = True
        self.view().reset()
        self._isResetting = False
        self._validate()

    def _saveSettings(self):
        path = fd.asksaveasfilename(
            parent=self.view().root,
            title=self._uiText["saveSettingsTitle"],
            initialdir="settings",
            filetypes=[(self._uiText["settingsFileType"], "*.rhs")],
            defaultextension=".rhs"
        )
        if not path:
            return
        fileIO.writeSettings(path)

    def _importSettings(self):
        path = fd.askopenfilename(
            parent=self.view().root,
            title=self._uiText["importSettingsTitle"],
            initialdir="settings",
            filetypes=[(self._uiText["exportSettingsFileType"], "*.rhe")],
        )
        if not path:
            return
        self.output("importSettingsText")
        fileIO.importSettings(path, self.model().value("exportKeys"))
        self._isResetting = True
        self.view().reset()
        self._isResetting = False
        self._validate()

    def _exportSettings(self):
        path = fd.asksaveasfilename(
            parent=self.view().root,
            title=self._uiText["exportSettingsTitle"],
            initialdir="settings",
            filetypes=[(self._uiText["exportSettingsFileType"], "*.rhe")],
            defaultextension=".rhe"
        )
        if not path:
            return
        fileIO.exportSettings(path, self.model().value("exportKeys"))
