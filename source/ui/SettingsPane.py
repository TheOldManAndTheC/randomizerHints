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
from tkinter import font
from tkinter import ttk
import source.pkg.mvcTkinter as mtk
# from source.mvcTkinter.Frame import Frame

buildButtonPath = "mainFrame.settingsFrame.settingsButtonsFrame.buildHints"
settingsFramePath = "mainFrame.settingsFrame"

packTop = {"packAnchor": tk.NW, "packSide": tk.TOP}
packBottom = {"packAnchor": tk.SW, "packSide": tk.BOTTOM}
packLeft = {"packAnchor": tk.W, "packSide": tk.LEFT}
packRight = {"packAnchor": tk.E, "packSide": tk.RIGHT}
padY2 = {"packPady": 2}
padX5 = {"packPadx": 5}
indent = {"packPadx": 30}
indent2 = {"packPadx": 60}
fillX = {"packFill": tk.X}
fillBoth = {"packFill": tk.BOTH}
expand = {"packExpand": True}
ridge = {"relief": "ridge", "borderwidth": 2}


class SettingsPane(mtk.Frame):
    def __init__(self, parent=None, **options):
        super().__init__(parent, **options)
        self.uiText = self._valueFromController("uiText")

        bigFont = font.Font(size=18)
        bigButton = ttk.Style()
        bigButton.configure("bigButton.TButton", font=bigFont)

        languages = self._valueFromController("languages")
        languageMenu = {"menuData": {"config": {"tearoff": False},
                                     "items": []}}
        for language in languages:
            languageMenu["menuData"]["items"].append(
                {"type": "radiobutton", "config": {"label": language}}
            )

        register = {"controller": self.controller()}
        fileSelectorOptions = register | packTop | padX5 | padY2 | fillX | {
            "className": "FileSelector",
            "fileDialog": "Choose File",
            "dirDialog": "Choose Directory",
        }
        checkbuttonOptions = \
            register | {"className": "Checkbutton", "defaultValue": True}
        buttonOptions = register | {"className": "Button"}
        percentSetterOptions = register | packLeft | {
            "className": "LabelSetter",
            "labelType": "float",
            "buttonText": self.uiText["changePercentButton"],
            "dialogTitle": self.uiText["getPercentTitle"],
            "dialogPrompt": self.uiText["getPercentPrompt"],
            "minvalue": 0.0,
            "maxvalue": 100.0,
        }
        labeledEntryOptions = register | {"className": "LabeledEntry"}

        fileSelectors = [
            fileSelectorOptions | {
                "name": "gameExe",
                "labelText": self.uiText["gameLabel"],
                "buttonText": self.uiText["gameButton"],
                "fileTypes": [(self.uiText["gameFileType"], "eldenring.exe")],
                "tooltip": self.uiText["gameTooltip"],
            },
            fileSelectorOptions | {
                "name": "randomizerExe",
                "labelText": self.uiText["randomizerLabel"],
                "buttonText": self.uiText["randomizerButton"],
                "fileTypes": [(self.uiText["randomizerFileType"],
                               "EldenRingRandomizer.exe")],
                "tooltip": self.uiText["randomizerTooltip"],
            },
            fileSelectorOptions | {
                "name": "fogRandomizerExe",
                "labelText": self.uiText["fogLabel"],
                "buttonText": self.uiText["fogButton"],
                "fileTypes": [(self.uiText["fogFileType"], "FogMod.exe")],
                "tooltip": self.uiText["fogTooltip"],
            },
            fileSelectorOptions | {
                "name": "yabberExe",
                "labelText": self.uiText["yabberLabel"],
                "buttonText": self.uiText["yabberButton"],
                "fileTypes": [(self.uiText["yabberFileType"], "Yabber.exe"),
                              (self.uiText["witchyBNDFileType"],
                               "WitchyBND.exe")],
                "tooltip": self.uiText["yabberTooltip"],
            },
            fileSelectorOptions | {
                "name": "dsmsPortableExe",
                "labelText": self.uiText["dsmspLabel"],
                "buttonText": self.uiText["dsmspButton"],
                "fileTypes": [(self.uiText["dsmspFileType"],
                               "DSMSPortable.exe")],
                "tooltip": self.uiText["dsmspTooltip"],
            },
        ]
        settings = [
            packTop | padY2 | {
                "className": "Frame",
                "name": "languageFrame",
                "tooltip": self.uiText["languageTooltip"],
                "subWidgets": [
                    packLeft | {
                        "className": "Label",
                        "name": "languageLabel",
                        "text": self.uiText["languageText"] + " (A⬌词):",
                    },
                    packLeft | languageMenu | {
                        "className": "Menubutton",
                        "controller": self.controller(),
                        "name": "language",
                    },
                ],
            },
            checkbuttonOptions | packTop | padY2 | {
                "name": "useRandomizer",
                "text": self.uiText["useRandomizerText"],
                "tooltip": self.uiText["useRandomizerTooltip"],
            },
            labeledEntryOptions | packTop | padY2 | indent | {
                "name": "customSeed",
                "tags": ["randomizer"],
                "preText": self.uiText["seedLabel"],
                "tooltip": self.uiText["seedTooltip"],
            },
            checkbuttonOptions | packTop | padY2 | indent | {
                "name": "useQuestHints",
                "tags": ["randomizer"],
                "text": self.uiText["useQuestHintsText"],
                "tooltip": self.uiText["useQuestHintsTooltip"],
            },
            checkbuttonOptions | packTop | padY2 | indent | {
                "name": "useCategoryHints",
                "tags": ["randomizer"],
                "text": self.uiText["useCategoryHintsText"],
                "tooltip": self.uiText["useCategoryHintsTooltip"],
            },
            checkbuttonOptions | packTop | padY2 | indent2 | {
                "name": "useNeighboringBias",
                "tags": ["randomizer"],
                "text": self.uiText["useNeighboringBiasText"],
                "tooltip": self.uiText["useNeighboringBiasTooltip"],
            },
            packTop | padY2 | indent | {
                "className": "Frame",
                "name": "useChestHintsFrame",
                "tags": ["randomizer"],
                "tooltip": self.uiText["useChestHintsTooltip"],
                "subWidgets": [
                    checkbuttonOptions | packLeft | {
                        "name": "useChestHints",
                        "text": self.uiText["percentHintsText"],
                    },
                    percentSetterOptions | {
                        "name": "chestHintsPercent",
                        "postText": self.uiText["chestHintsPercentText"],
                    }
                ],
            },
            packTop | padY2 | indent | {
                "className": "Frame",
                "tags": ["randomizer"],
                "tooltip": self.uiText["useBossHintsTooltip"],
                "name": "useBossHintsFrame",
                "subWidgets": [
                    checkbuttonOptions | packLeft | {
                        "name": "useBossHints",
                        "text": self.uiText["percentHintsText"]
                    },
                    percentSetterOptions | {
                        "name": "bossHintsPercent",
                        "postText": self.uiText["bossHintsPercentText"],
                    }
                ],
            },
            checkbuttonOptions | packTop | padY2 | indent | {
                "name": "useNearbyHints",
                "tags": ["randomizer"],
                "text": self.uiText["useNearbyHintsText"],
                "tooltip": self.uiText["useNearbyHintsTooltip"],
            },
            checkbuttonOptions | packTop | padY2 | indent | {
                "name": "useAllDirections",
                "tags": ["randomizer"],
                "text": self.uiText["useAllDirectionsText"],
                "tooltip": self.uiText["useAllDirectionsTooltip"],
                "defaultValue": False,
            },
            checkbuttonOptions | packTop | padY2 | {
                "name": "useFogRandomizer",
                "text": self.uiText["useFogText"],
                "tooltip": self.uiText["useFogTooltip"],
                "defaultValue": False,
            },
            labeledEntryOptions | packTop | padY2 | indent | {
                "name": "customFogSeed",
                "tags": ["fog"],
                "preText": self.uiText["fogSeedLabel"],
                "tooltip": self.uiText["fogSeedTooltip"],
            },
            checkbuttonOptions | packTop | padY2 | indent | {
                "name": "useNearbyFogHints",
                "tags": ["fog"],
                "text": self.uiText["useNearbyFogHintsText"],
                "tooltip": self.uiText["useNearbyFogHintsTooltip"],
            },
            packTop | padY2 | indent | {
                "className": "Frame",
                "name": "useChestFogHintsFrame",
                "tags": ["fog"],
                "tooltip": self.uiText["useChestFogHintsTooltip"],
                "subWidgets": [
                    checkbuttonOptions | packLeft | {
                        "name": "useChestFogHints",
                        "text": self.uiText["percentFogHintsText"]
                    },
                    percentSetterOptions | {
                        "name": "chestFogHintsPercent",
                        "postText": self.uiText["chestHintsPercentText"],
                    }
                ],
            },
            packTop | padY2 | indent | {
                "className": "Frame",
                "name": "useBossFogHintsFrame",
                "tags": ["fog"],
                "tooltip": self.uiText["useBossFogHintsTooltip"],
                "subWidgets": [
                    checkbuttonOptions | packLeft | {
                        "name": "useBossFogHints",
                        "text": self.uiText["percentFogHintsText"]
                    },
                    percentSetterOptions | {
                        "name": "bossFogHintsPercent",
                        "postText": self.uiText["bossHintsPercentText"],
                    }
                ],
            },
            checkbuttonOptions | packTop | padY2 | {
                "name": "useFingerMaidenItems",
                "text": self.uiText["useMaidenItemsText"],
                "tags": ["starting"],
                "tooltip": self.uiText["useMaidenItemsTooltip"],
                "defaultValue": False,
            },
            checkbuttonOptions | packTop | padY2 | {
                "name": "useShopInventory",
                "text": self.uiText["useShopText"],
                "tags": ["starting"],
                "tooltip": self.uiText["useShopTooltip"],
                "defaultValue": False,
            },
            packBottom | fillX | {
                "className": "Frame",
                "name": "settingsButtonsFrame",
                "subWidgets": [
                    buttonOptions | packLeft | padX5 | {
                        "name": "loadSettings",
                        "text": self.uiText["loadSettingsButton"],
                        "tooltip": self.uiText["loadSettingsTooltip"],
                    },
                    buttonOptions | packLeft | padX5 | {
                        "name": "saveSettings",
                        "text": self.uiText["saveSettingsButton"],
                        "tooltip": self.uiText["loadSettingsTooltip"],
                    },
                    buttonOptions | packLeft | padX5 | {
                        "name": "importSettings",
                        "text": self.uiText["importSettingsButton"],
                        "tooltip": self.uiText["importSettingsTooltip"],
                    },
                    buttonOptions | packLeft | padX5 | {
                        "name": "exportSettings",
                        "text": self.uiText["exportSettingsButton"],
                        "tooltip": self.uiText["exportSettingsTooltip"],
                    },
                    buttonOptions | packRight | indent | {
                        "name": "buildHints",
                        "text": self.uiText["buildButton"],
                        "tooltip": self.uiText["buildTooltip"],
                        "style": "bigButton.TButton",
                        "state": "disable",
                    },
                    packRight | indent | {
                        "className": "HelpIcon",
                        "tooltip": self.uiText["helpIcon"],
                    },
                ],
            },
        ]

        console = [
            packTop | padY2 | fillX | {
                "className": "Frame",
                "subWidgets": [
                    packLeft | fillX | expand | {
                        "className": "Label",
                        "text": self.uiText["consoleLabel"],
                        "tooltip": self.uiText["consoleTooltip"],
                    },
                    buttonOptions | packRight | {
                        "name": "copyConsole",
                        "text": self.uiText["consoleCopyButton"],
                        "tooltip": self.uiText["consoleCopyTooltip"],
                    },
                    buttonOptions | packRight | padX5 | {
                        "name": "clearConsole",
                        "text": self.uiText["consoleClearButton"],
                        "tooltip": self.uiText["consoleClearTooltip"],
                    },
                ]
            },
            packTop | padY2 | fillBoth | expand | {
                "className": "Frame",
                "subWidgets": [
                    packLeft | fillBoth | expand | {
                        "className": "ConsoleText",
                        "controller": self.controller(),
                        "name": "console",
                        "autoStart": True,
                    },
                ],
            },
        ]

        mtk.Frame(self, name="pathsFrame", subWidgets=fileSelectors,
                  **(packTop | padX5 | padY2 | ridge | fillBoth))
        frame = mtk.Frame(self, name="mainFrame",
                          **(packTop | padX5 | padY2 | fillBoth | expand))
        mtk.Frame(frame, name="settingsFrame", subWidgets=settings,
                  **(packLeft | fillBoth | expand))
        mtk.Frame(frame, name="consoleFrame", subWidgets=console, packPady=10,
                  **(packRight | fillBoth | expand))

    def setState(self, state, key=None):
        settingsFrame = self.getSubWidget(settingsFramePath)
        match key:
            case "build":
                self.getSubWidget("pathsFrame").setState(state, key)
                settingsFrame.setState(state, key)
            case "ready":
                self.getSubWidget(buildButtonPath).setState(state, key)
            case "fog" | "randomizer" | "starting":
                for widget in settingsFrame.widgets.values():
                    if key in widget.tags:
                        widget.setState(state, key)
            case _:
                super().setState(state, key)
