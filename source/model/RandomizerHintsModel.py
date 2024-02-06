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

import math
import importlib
from copy import deepcopy
from os.path import dirname
import source.pkg.mvcTkinter as mtk
from source.utils.rng import rng
from source.data.model.paramData.hintMassedit import hintMassedit
from source.model.randomizer.processRandomized import processRandomized
from source.model.fog.processFog import processFog
from source.model.params.freeRange import freeRange
from source.model.hint.buildCategoryHints import buildCategoryHints
from source.model.hint.buildFingerMaidenItems import buildFingerMaidenItems
from source.model.hint.buildHusksShop import buildHusksShop
from source.model.hint.buildNearbyFogHints import buildNearbyFogHints
from source.model.hint.buildNearbyHints import buildNearbyHints
from source.model.hint.buildQuestHints import buildQuestHints
from source.model.hint.buildRandomFogLots import buildRandomFogLots
from source.model.hint.buildRandomLots import buildRandomLots
from source.model.hint.processItems import processItems
from source.model.hint.scriptHints import scriptHints
from source.model.hint.traverseFog import traverseFog
from source.data.model.RandomizerHintsModelData import *
from source.data.locale.bellOfReturnText import bellOfReturnText
from source.data.model.hintData.defaultLots import defaultLots
from source.data.model.defaultCategories.defaultCategories \
    import defaultCategories
from source.data.model.defaultCategories.defaultActiveCategories \
    import defaultActiveCategories
from source.data.model.defaultCategories.categoryLocalization \
    import categoryLocalizaiton


class RandomizerHintsModel(mtk.Model):
    def __init__(self, **options):
        super().__init__(**options)
        self._validated = False
        self._reportedInvalid = False
        self._randomized = None
        self._seed = None
        self._fogSeed = None
        self._missable = None
        self._params = None
        self._fog = None
        self._hintRegulationFile = self._currentDir() + "/regulation.bin"
        self._hintMsgDir = self._currentDir() + "/" + msgPath
        self._workingDir = self._currentDir() + "/working/"
        self._itemInfo = dict()
        self._localeData = dict()
        for language in languages:
            name = "itemInfo_" + language
            self._itemInfo[language] = \
                getattr(importlib.import_module(itemInfoModule + name), name)
            name = "localeData_" + language
            self._localeData[language] = \
                getattr(importlib.import_module(localeDataModule + name), name)
        self._language = self._settingValue("language")
        if self._language is None:
            self._language = "engus"

    def value(self, key, **kwargs):
        match key:
            case "missable":
                return self._missable
            case "hintCategories" | "maidenItems" | "shopItems":
                return self._settingValue(key)
            case "maidenItemsCount":
                return self._maidenItemsCount(self._settingValue("maidenItems"))
            case "checkMaidenSpace":
                return self._checkMaidenSpace(**kwargs)
            case "itemInfo":
                return self._itemInfo[self._language]
            case "category":
                if self._settingValue("hintCategories") is None:
                    self._validateCategorySettings()
                hintCategories = self._settingValue("hintCategories")
                if kwargs["name"] not in hintCategories:
                    return None
                return hintCategories[kwargs["name"]]
            case "generalCategories" | "chestCategories" | "bossCategories":
                if self._settingValue("activeCategories") is None:
                    self._validateCategorySettings()
                return self._settingValue("activeCategories")[key]
            case "exportKeys":
                return exportKeys
        return None

    def update(self, key, **kwargs):
        match key:
            case "defaultSettings":
                self._defaultSettings(defaultSettings)
                self._setSetting("language", self._language)
                self.update("defaultCategories")
                self.update("defaultActiveCategories")
                self._validateCategorySettings()
            case "defaultCategories":
                hintCategories = \
                    self._getLocalizedDefaultCategories(self._language)
                self._defaultSettings({"hintCategories": hintCategories})
                self._cleanCategories()
            case "defaultActiveCategories":
                activeCategories = \
                    self._getLocalizedDefaultActiveCategories(self._language)
                self._defaultSettings({"activeCategories": activeCategories})
                self._cleanCategories()
            case "validate":
                self._validate()
            case "loadShopInventory":
                self._loadShopInventory()
            case "modifyShopItem":
                self._modifyShopItem(**kwargs)
            case "buildHints":
                self._buildHints()
            case "addCategory":
                return self._addCategory(**kwargs)
            case "renameCategory":
                return self._cleanCategories(kwargs["name"], kwargs["newName"])
            case "removeCategory":
                return self._cleanCategories(kwargs["name"])
            case "cleanCategories":
                return self._cleanCategories()
            case "checkLocale":
                return self._checkLocale()
        return None

    def _getLocalizedCategoryName(self, name):
        for entry in categoryLocalizaiton.values():
            if name in entry.values():
                return entry[self._language]
        return None

    def _getLocalizedDefaultCategories(self, language):
        localizedCategories = dict()
        for category in defaultCategories:
            localizedCategory = categoryLocalizaiton[category][language]
            localizedCategories[localizedCategory] = dict()
            for item in defaultCategories[category]:
                localizedItem = self._localeData[language][item]
                if localizedItem in localizedCategories[localizedCategory]:
                    print(category, item, localizedCategory, localizedItem)
                localizedCategories[localizedCategory][localizedItem] = \
                    defaultCategories[category][item]
        return localizedCategories

    def _getLocalizedDefaultActiveCategories(self, language):
        localizedActiveCategories = dict()
        for key in defaultActiveCategories:
            localizedActiveCategories[key] = []
            for category in defaultActiveCategories[key]:
                localizedActiveCategories[key].append(
                    categoryLocalizaiton[category][language]
                )
        return localizedActiveCategories

    def _checkLocale(self):
        self._validateCategorySettings()
        itemInfo = self.value("itemInfo")
        changed = False
        newHintCategories = dict()
        hintCategories = self._settingValue("hintCategories")
        for categoryName in hintCategories:
            newCategoryName = self._getLocalizedCategoryName(categoryName)
            if newCategoryName is None:
                newCategoryName = categoryName
            elif newCategoryName != categoryName:
                changed = True
            category = hintCategories[categoryName]
            newCategory = dict()
            for itemName in category:
                itemEntry = category[itemName]
                if itemName not in itemInfo:
                    for altItemInfo in self._itemInfo.values():
                        if itemName in altItemInfo:
                            infoEntry = altItemInfo[itemName]
                            itemName = self._localeData[self._language][
                                infoEntry["name"]
                            ]
                            changed = True
                            break
                newCategory[itemName] = itemEntry
            newHintCategories[newCategoryName] = newCategory
        self._setSetting("hintCategories", newHintCategories, write=False)
        newActiveCategories = dict()
        activeCategories = self._settingValue("activeCategories")
        for key in activeCategories:
            newCategories = []
            for categoryName in activeCategories[key]:
                newCategoryName = self._getLocalizedCategoryName(categoryName)
                if newCategoryName is None:
                    newCategoryName = categoryName
                elif newCategoryName != categoryName:
                    changed = True
                newCategories.append(newCategoryName)
            newActiveCategories[key] = newCategories
        self._setSetting("activeCategories", newActiveCategories, write=False)
        if self._settingValue("shopItems") is not None:
            for itemEntry in self._settingValue("shopItems").values():
                if itemEntry["displayName"] not in itemInfo:
                    itemEntry["displayName"] = \
                        self._localeData[self._language][itemEntry["name"]]
                    changed = True
        newMaidenItems = dict()
        for name, entry in self._settingValue("maidenItems").items():
            if "isCategory" in entry:
                newCategoryName = self._getLocalizedCategoryName(name)
                if newCategoryName is None:
                    newCategoryName = name
                elif newCategoryName != name:
                    changed = True
                newMaidenItems[newCategoryName] = entry
                continue
            if name in itemInfo:
                newMaidenItems[name] = entry
                continue
            for altItemInfo in self._itemInfo.values():
                if name in altItemInfo:
                    infoEntry = altItemInfo[name]
                    itemName = \
                        self._localeData[self._language][infoEntry["name"]]
                    newMaidenItems[itemName] = entry
                    changed = True
                    break
        self._setSetting("maidenItems", newMaidenItems, write=False)
        if changed:
            self._cleanCategories()
        else:
            self._setSetting(None, None)
        return changed

    def _validate(self):
        self._modelUpdated("ready", state=False)
        self._validateCategorySettings()
        self._validated = self._validateSettings()
        useRandomizer = self._settingValue("useRandomizer")
        useFogRandomizer = self._settingValue("useFogRandomizer")
        self._modelUpdated("randomizer", state=useRandomizer)
        self._modelUpdated("fog", state=useFogRandomizer)
        self._modelUpdated("starting",
                           state=useRandomizer or useFogRandomizer)
        if not self._validated:
            self._invalidate()
            if not self._reportedInvalid:
                self._output("invalidPathsText")
                self._reportedInvalid = True
            return False
        self._reportedInvalid = False
        if useRandomizer:
            self._output("readSpoilersText")
            missableLotsName = "missableLots_" + self._language
            missableLots = getattr(importlib.import_module(missableLotsModule
                                                           + missableLotsName),
                                   missableLotsName)
            self._randomized, self._seed, missable, missingEnemiesText = \
                processRandomized(
                    self._readFile(self._itemSlotsFile, lines=True),
                    self._readFile(self._mapNamesFile, lines=True),
                    self._readFile(self._annotationsFile, lines=True),
                    self._readFile(self._latestFile(self._spoilerDir, "txt"),
                                   lines=True),
                    missableLots
                )
            if missingEnemiesText is not None:
                self._writeFile(missingEnemiesText, "missing_enemies.txt")
            self._missable = dict()
            for item in missable:
                localizedItem = self._localeData[self._language][item]
                self._missable[localizedItem] = missable[item]
            self._output("seedText", self._seed)
        else:
            self._randomized = None
            self._seed = None
            self._missable = None

        if useFogRandomizer:
            self._output("readFogText", self._seed)
            self._fog = processFog(
                self._readFile(self._fogFile, lines=True),
                self._readFile(self._latestFile(self._fogSpoilerDir, "txt"),
                               lines=True)
            )
            self._fogSeed = self._fog["fogSeed"]
            self._output("fogSeedText", self._fogSeed)
        else:
            self._fog = None
            self._fogSeed = None
        if not useRandomizer and not useFogRandomizer:
            self._invalidate()
            self._output("notBuildReadyText", self._seed)
            return False
        self._output("readRegulationText", self._seed)
        self._params = self._readParams()
        # we need to check the shop contents
        # get the current base shop and the user edited shop
        defaultShopItems = self._settingValue("defaultShopItems")
        currentShopItems = self._settingValue("shopItems")
        # load the shop from the new params
        self._loadShopInventory()
        newShopItems = self._settingValue("shopItems")
        # if the new base shop inventory is the same as the old, we'll
        # preserve the user's changes
        if newShopItems == defaultShopItems:
            self._setSetting("shopItems", currentShopItems)
        else:
            # otherwise set the new base shop default and notify the user
            # if they made changes
            self._setSetting("defaultShopItems", deepcopy(newShopItems))
            if currentShopItems != defaultShopItems:
                self._output("shopChangedText")
                self._modelUpdated("shopChanged")
        self._output("buildReadyText")
        self._modelUpdated("ready", state=True)
        return True

    def _invalidate(self):
        self._validated = False
        self._randomized = None
        self._seed = None
        self._missable = None
        self._params = None
        self._fog = None
        self._fogSeed = None
        self._modelUpdated("ready", state=False)

    def _defaultSettings(self, settings):
        for setting in settings:
            self._setSetting(setting, settings[setting], False)
        self._setSetting(None, None)

    def _validateCategorySettings(self):
        if self._settingValue("hintCategories") is None:
            self.update("defaultCategories")
        if self._settingValue("activeCategories") is None:
            self.update("defaultActiveCategories")

    def _validateSettings(self):
        if not self._pathExists(self._settingValue("gameExe")) or \
                not self._pathExists(self._settingValue("yabberExe")) or \
                not self._pathExists(self._settingValue("dsmsPortableExe")):
            return False
        # Generate the various paths
        self._gameDir = dirname(self._settingValue("gameExe"))
        # randomizer hints paths
        self._hintPatchesDir = self._workingDir + "hint_patches/"
        self._exportedCSVDir = self._workingDir + "export/"
        if not self._pathExists(self._workingDir):
            self._createDir(self._workingDir)
        if not self._pathExists(self._hintPatchesDir):
            self._createDir(self._hintPatchesDir)
        if not self._pathExists(self._exportedCSVDir):
            self._createDir(self._exportedCSVDir)
        result = self._validateRandomizerSettings() and \
                 self._validateFogSettings()
        return result

    def _validateRandomizerSettings(self):
        # disregard if we're not using item and enemy randomizer
        if not self._settingValue("useRandomizer"):
            return True
        if not self._pathExists(self._settingValue("randomizerExe")):
            return False
        # Generate the various paths
        self._randomizerDir = dirname(self._settingValue("randomizerExe")) + "/"
        self._spoilerDir = self._randomizerDir + "spoiler_logs/"
        randomizerDataDir = self._randomizerDir + "diste/"
        self._itemSlotsFile = randomizerDataDir + "Base/itemslots.txt"
        self._annotationsFile = randomizerDataDir + "Base/annotations.txt"
        self._mapNamesFile = randomizerDataDir + "Names/MapName.txt"
        # paths that will be overridden if fog gate randomizer is used
        self._sourceMsgDir = self._randomizerDir + msgPath
        self._sourceRegulationFile = self._randomizerDir + "regulation.bin"
        return True

    def _validateFogSettings(self):
        # disregard if we're not using fog gate randomizer
        if not self._settingValue("useFogRandomizer"):
            return True
        if not self._pathExists(self._settingValue("fogRandomizerExe")):
            return False
        # Generate the various paths
        self._fogRandomizerDir = \
            dirname(self._settingValue("fogRandomizerExe")) + "/"
        self._fogSpoilerDir = self._fogRandomizerDir + "spoiler_logs/"
        fogRandomizerDataDir = self._fogRandomizerDir + "eldendata/"
        self._fogFile = fogRandomizerDataDir + "Base/fog.txt"
        self._sourceFogMsgDir = self._fogRandomizerDir + msgPath
        # paths that override item and enemy randomizer paths
        self._sourceRegulationFile = self._fogRandomizerDir + "regulation.bin"
        return True

    def _spoilerFileIsCurrent(self):
        latestSpoilerFile = None
        if self._settingValue("useFogRandomizer"):
            latestSpoilerFile = self._latestFile(self._fogSpoilerDir, "txt")
        if self._settingValue("useRandomizer"):
            latestSpoilerFile = self._latestFile(self._spoilerDir, "txt")
        if self._settingValue("latestSpoilerFile") != latestSpoilerFile:
            self._setSetting("latestSpoilerFile", latestSpoilerFile)
            return False
        return True

    def _loadShopInventory(self):
        shopParams = self._params["ShopLineupParam"]
        shopItems = dict()
        for lotID in shopLots:
            for itemName in self.value("itemInfo"):
                itemEntry = self.value("itemInfo")[itemName]
                if itemEntry["equipId"] == shopParams[lotID]["equipId"]:
                    shopEntry = deepcopy(itemEntry)
                    shopEntry["displayName"] = itemName
                    shopEntry["value"] = shopParams[lotID]["value"]
                    shopItems[lotID] = shopEntry
                    break
        self._setSetting("shopItems", shopItems)

    def _modifyShopItem(self, lotID: str, newName=None, value=None):
        shopItems = self._settingValue("shopItems")
        shopEntry = shopItems[lotID]
        if value is None:
            value = shopEntry["value"]
        else:
            shopEntry["value"] = value
        if newName is not None:
            shopEntry = deepcopy(self.value("itemInfo")[newName])
            shopEntry["displayName"] = newName
            shopEntry["value"] = value
        shopItems[lotID] = shopEntry

    def _maidenItemsCount(self, maidenItems):
        if not self._validated:
            return 0, 0, 0
        itemCount = 0
        hintCount = 0
        for name in maidenItems:
            entry = maidenItems[name]
            if "isItem" in entry:
                itemCount += 1
            if "isItemHint" in entry or "isCategory" in entry:
                quantity = 1
                if "quantity" in entry:
                    quantity = entry["quantity"]
                hintCount += quantity
        hintItemCount = math.ceil(hintCount / 4.0)
        hintItemSpace = hintItemCount * 4 - hintCount
        lotRange = freeRange(fingerMaidenLotID,
                             self._params["ItemLotParam_map"])
        lotLength = int(lotRange["freeLotLength"])
        return itemCount + hintItemCount, lotLength, hintItemSpace

    def _checkMaidenSpace(self, selection, entry=None, value=0, **kwargs):
        maidenItems = self._settingValue("maidenItems")
        if entry is None:
            entry = maidenItems[selection]
        newEntry = deepcopy(entry)
        if value:
            newEntry["quantity"] = value
        newMaidenItems = deepcopy(maidenItems)
        newMaidenItems[selection] = newEntry
        itemCount, lotLength, _ = self._maidenItemsCount(newMaidenItems)
        if itemCount > lotLength:
            return False
        return True

    def _addCategory(self, newName, categoryToCopy=None):
        hintCategories = self._settingValue("hintCategories")
        if newName in hintCategories:
            return False
        if categoryToCopy is None:
            newCategory = dict()
        else:
            newCategory = deepcopy(hintCategories[categoryToCopy])
        hintCategories[newName] = newCategory
        return True

    def _cleanCategories(self, name=None, newName=None):
        hintCategories = self._settingValue("hintCategories")
        activeCategories = self._settingValue("activeCategories")
        if hintCategories is None or activeCategories is None:
            return
        maidenItems = self._settingValue("maidenItems")
        # if there is a category to be removed or renamed, do that first
        if name is not None:
            if newName is not None and newName not in hintCategories:
                hintCategories[newName] = hintCategories[name]
                for categoryList in activeCategories:
                    if name in activeCategories[categoryList]:
                        activeCategories[categoryList].append(newName)
                if name in maidenItems:
                    maidenItems[newName] = maidenItems[name]
            hintCategories.pop(name)
        # make sure the category selections and finger maiden items don't have
        # categories that don't exist anymore
        for categoryList in activeCategories:
            newCategoryList = []
            for categoryName in activeCategories[categoryList]:
                if categoryName in hintCategories:
                    newCategoryList.append(categoryName)
                    continue
                newCategoryName = self._getLocalizedCategoryName(categoryName)
                if newCategoryName in hintCategories:
                    newCategoryList.append(newCategoryName)
            activeCategories[categoryList] = newCategoryList
        newMaidenItems = dict()
        for name in maidenItems:
            if "isCategory" not in maidenItems[name] or name in hintCategories:
                newMaidenItems[name] = maidenItems[name]
                continue
            newCategoryName = self._getLocalizedCategoryName(name)
            if newCategoryName in hintCategories:
                newMaidenItems[newCategoryName] = maidenItems[name]
        self._setSetting("maidenItems", newMaidenItems)

    def _buildHints(self):
        useRandomizer = self._settingValue("useRandomizer")
        useFogRandomizer = self._settingValue("useFogRandomizer")
        useAllDirections = self._settingValue("useAllDirections")
        if not useRandomizer and not useFogRandomizer:
            self._output("noBuildText")
            return
        self._modelUpdated("build", state=False)
        self._output("readingFilesText")
        # make a copy of the params to work on
        params = deepcopy(self._params)
        # read the XML files in item.msgbnd.dcx
        xmlFiles = self._readXMLFiles()
        if xmlFiles is None:
            self._output("buildError")
            self._modelUpdated("build", state=True)
            return
        randomized = None
        hintCategories = None
        lots = defaultLots
        # build the list of hint entries
        allHintEntries = []
        nearbyHintEntries = []
        if useRandomizer:
            self._output("generatingHintsText")
            # set the random seed for item hint generation
            if self._settingValue("customSeed"):
                seed = self._settingValue("customSeed")
            else:
                seed = self._seed
            rng.seed(seed)
            self._output("usedSeedText", seed)
            # make copies of randomized and hintCategories to work on
            randomized = deepcopy(self._randomized)
            hintCategories = deepcopy(self._settingValue("hintCategories"))
            # process the items
            self._output("processingItemsText")
            localize = dict()
            for item in randomized:
                localize[item] = self._localeData[self._language][item]
            lots = processItems(randomized, hintCategories, params, localize)
            self._output("numLotsText", len(lots["lotsByID"]))
            if self._settingValue("useQuestHints"):
                self._output("useQuestHintsText")
                count = buildQuestHints(allHintEntries, randomized, params)
                self._output("numHintsText", count)
            activeCategories = self._settingValue("activeCategories")
            if self._settingValue("useCategoryHints"):
                self._output("useCategoryHintsText")
                count = buildCategoryHints(
                    lots["lotsByID"],
                    allHintEntries,
                    hintCategories,
                    activeCategories["generalCategories"],
                    self._settingValue("useNeighboringBias") and
                    not useFogRandomizer,
                    localize
                )
                self._output("numHintsText", count)
            # TODO: skew randomness towards certain categories
            if self._settingValue("useChestHints"):
                self._output("useChestHintsText")
                count = buildRandomLots(
                    lots["chestLots"],
                    allHintEntries,
                    hintCategories,
                    activeCategories["chestCategories"],
                    self._settingValue("chestHintsPercent")
                )
                self._output("numHintsText", count)
            if self._settingValue("useBossHints"):
                self._output("useBossHintsText")
                count = buildRandomLots(
                    lots["bossLots"],
                    allHintEntries,
                    hintCategories,
                    activeCategories["bossCategories"],
                    self._settingValue("bossHintsPercent")
                )
                self._output("numHintsText", count)
            # generate the hint items from the hint entries
            scriptHints(allHintEntries, xmlFiles, params,
                        self._itemInfo["engus"], self._localeData,
                        useFogRandomizer, useAllDirections)
            if self._settingValue("useNearbyHints"):
                self._output("useNearbyHintsText")
                count = buildNearbyHints(nearbyHintEntries, randomized, params)
                self._output("numHintsText", count)
            # generate the nearby hint items from the nearby hint entries
            scriptHints(nearbyHintEntries, xmlFiles, params,
                        self._itemInfo["engus"], self._localeData,
                        useFogRandomizer, useAllDirections)
        allFogHintEntries = []
        if useFogRandomizer:
            self._output("generatingFogHintsText")
            # set the random seed for fog gate hint generation
            if self._settingValue("customFogSeed"):
                seed = self._settingValue("customFogSeed")
            else:
                seed = self._fogSeed
            rng.seed(seed)
            self._output("usedSeedText", seed)
            fogHints = traverseFog(self._fog)
            if self._settingValue("useNearbyFogHints"):
                self._output("useNearbyFogHintsText")
                count = buildNearbyFogHints(self._fog, fogHints,
                                            allFogHintEntries, params)
                self._output("numHintsText", count)
            if self._settingValue("useChestFogHints"):
                self._output("useChestFogHintsText")
                count = buildRandomFogLots(
                    lots["chestLots"],
                    allFogHintEntries,
                    fogHints,
                    self._settingValue("chestFogHintsPercent")
                )
                self._output("numHintsText", count)
            if self._settingValue("useBossFogHints"):
                self._output("useBossFogHintsText")
                count = buildRandomFogLots(
                    lots["bossLots"],
                    allFogHintEntries,
                    fogHints,
                    self._settingValue("bossFogHintsPercent")
                )
                self._output("numHintsText", count)
            # generate the fog hint items from the fog hint entries
            scriptHints(allFogHintEntries, xmlFiles, params,
                        self._itemInfo["engus"], self._localeData,
                        useFogRandomizer, useAllDirections)
        maidenHintEntries = []
        if self._settingValue("useFingerMaidenItems"):
            self._output("useMaidenItemsText")
            count, itemCount = buildFingerMaidenItems(
                allHintEntries=maidenHintEntries,
                randomized=randomized,
                hintCategories=hintCategories,
                params=params,
                itemInfo=self.value("itemInfo"),
                maidenItems=self._settingValue("maidenItems"),
                useRandomizer=useRandomizer,
                useNeighboringBias=self._settingValue("useNeighboringBias") and
                    not useFogRandomizer
            )
            self._output("numItemsText", itemCount)
            self._output("numHintsText", count)
            # generate the maiden hint items from the maiden hint entries
            scriptHints(maidenHintEntries, xmlFiles, params,
                        self._itemInfo["engus"], self._localeData,
                        useFogRandomizer, useAllDirections)
        if self._settingValue("useShopInventory"):
            self._output("useShopText")
            count = buildHusksShop(params, self._settingValue("shopItems"))
            self._output("shopNumText", count)
        self._output("totalNumHintsText", len(allHintEntries) +
                     len(nearbyHintEntries) + len(maidenHintEntries) +
                     len(allFogHintEntries))
        self._output("writingFilesText")
        self._writeXMLFiles(xmlFiles)
        self._output("writingParamsText")
        self._writeParams(params)
        self._output("tomlText")
        self._createModEngineFile()
        self._output("buildDoneText")
        self._modelUpdated("build", state=True)

    # Run DSMSPortable to export params
    def _readParams(self):
        paramListText = ""
        for paramName in paramList:
            paramListText += paramName + " "
        command = \
            paramExportCommand.format(self._settingValue("dsmsPortableExe"),
                                      self._sourceRegulationFile,
                                      self._gameDir,
                                      paramListText,
                                      self._exportedCSVDir)
        self._shellCmd(command)
        # Read the params from the CSVs exported with DSMS Portable
        params = dict()
        for paramName in paramList:
            params[paramName] = \
                self._readCSV(self._exportedCSVDir + paramName + ".csv",
                              useDict=True)
        params["massedit"] = hintMassedit
        return params

    # Write the new params to CSVs and the massedit file to be used by
    # DSMSPortable
    def _writeParams(self, params):
        for paramName in paramList:
            csvFile = self._hintPatchesDir + paramName + ".csv"
            if self._pathExists(csvFile):
                self._deleteFile(csvFile)
            newParamName = paramList[paramName]
            if newParamName and newParamName in params and params[newParamName]:
                self._writeCSV(params[newParamName], csvFile)
        self._writeMassedit(params["massedit"])
        self._patchParams()

    # Create the massedit file for DSMSPortable
    def _writeMassedit(self, massedit):
        editText = "param {}: {}: {}: = {};\n"
        masseditText = ""
        for entry in massedit:
            param = entry["param"]
            field = entry["field"]
            value = entry["value"]
            if "id" in entry:
                idRange = "id " + entry["id"]
            else:
                idRange = "idrange " + entry["idStart"] + " " + entry["idEnd"]
            masseditText += editText.format(param, idRange, field, value)
        self._writeFile(masseditText, self._hintPatchesDir + "hint.massedit")

    # Run DSMSPortable to patch regulation.bin
    def _patchParams(self):
        csvText = ""
        for paramName in paramList:
            csvFile = self._hintPatchesDir + paramName + ".csv"
            if paramList[paramName] and self._pathExists(csvFile):
                csvText += "\"" + csvFile + "\" "
        if csvText:
            csvText = " -C " + csvText[:-1]
        command = \
            paramPatchCommand.format(self._settingValue("dsmsPortableExe"),
                                     self._sourceRegulationFile,
                                     self._gameDir,
                                     csvText,
                                     self._hintPatchesDir + "hint.massedit",
                                     self._hintRegulationFile)
        self._shellCmd(command)

    # Read the randomized goods XML files from item.msgbnd.dcx
    def _readXMLFiles(self):
        self._deleteDir(self._workingDir + msgPath)
        witchy = self._settingValue("yabberExe").endswith("WitchyBND.exe")
        sourcePaths = []
        if self._settingValue("useFogRandomizer"):
            sourcePaths.append(self._sourceFogMsgDir)
        if self._settingValue("useRandomizer"):
            sourcePaths.append(self._sourceMsgDir)
        sourcePaths.append(self._currentDir() + "/locale/" + msgPath)
        xmlDict = dict()
        for language in languages:
            sourceFile = None
            for sourcePath in sourcePaths:
                if self._pathExists(sourcePath + language + "/" + msgbndFile):
                    sourceFile = sourcePath + language + "/" + msgbndFile
                    break
            if sourceFile is None:
                continue
            self._output(None, sourceFile)
            workingDir = self._workingDir + msgPath + language + "/"
            if witchy:
                xmlDir = workingDir + witchyXMLPath
            else:
                xmlDir = workingDir + yabberXMLPath + language + "/"
            self._createDir(workingDir)
            self._copyFile(sourceFile, workingDir + msgbndFile)
            yabberPaths = [workingDir + msgbndFile]
            for xmlName in xmlList:
                yabberPaths.append(xmlDir + xmlName)
            self._yabber(yabberPaths)
            xmlDict[language] = dict()
            for xmlName in xmlList:
                xmlLines = self._readFile(xmlDir + xmlName + ".xml", lines=True)
                if xmlLines is None:
                    self._output("missingXMLFileError", xmlName, language)
                    if witchy:
                        self._output("witchyError")
                    else:
                        self._output("yabberError")
                    return None
                if self._settingValue("useFogRandomizer"):
                    found = False
                    for line in xmlLines:
                        if line.startswith(bellOfReturnXML.split("{")[0]):
                            found = True
                            break
                    if not found:
                        xmlLines.insert(-2, bellOfReturnXML.format(
                            bellOfReturnText[language][xmlList[xmlName]]
                        ))
                xmlDict[language][xmlList[xmlName]] = xmlLines
        return xmlDict

    # Write the randomized goods XML files back to item.msgbnd.dcx
    def _writeXMLFiles(self, xmlFiles):
        self._deleteDir(self._hintMsgDir)
        witchy = self._settingValue("yabberExe").endswith("WitchyBND.exe")
        for language in xmlFiles:
            workingDir = self._workingDir + msgPath + language + "/"
            hintMsgDir = self._hintMsgDir + language + "/"
            self._output(None, hintMsgDir + msgbndFile)
            if witchy:
                xmlDir = workingDir + witchyXMLPath
            else:
                xmlDir = workingDir + yabberXMLPath + language + "/"
            self._createDir(workingDir)
            self._createDir(hintMsgDir)
            yabberPaths = []
            for xmlName in xmlList:
                self._writeFile(xmlFiles[language][xmlList[xmlName]],
                                xmlDir + xmlName + ".xml", lines=True)
                yabberPaths.append(xmlDir + xmlName + ".xml")
            yabberPaths.append(workingDir + msgbndPath)
            self._yabber(yabberPaths)
            self._copyFile(workingDir + msgbndFile, hintMsgDir + msgbndFile)

    # Run Yabber or WitchyBND on the given paths
    def _yabber(self, paths):
        yabber = self._settingValue("yabberExe")
        witchy = yabber.endswith("WitchyBND.exe")
        arguments = ""
        for path in paths:
            arguments += " \"" + path + "\""
        # WitchyBND has a default 2 second delay after running unless the -p
        # option is used.
        witchyArgs = ""
        if witchy:
            witchyArgs = " -p"
        command = "\"" + yabber + "\"" + witchyArgs + arguments
        # WitchyBND throws an exception when both stdout and stderr are
        # redirected, and it doesn't play well with pyinstaller -noconsole,
        # so just suppress all output pipes
        if witchyArgs:
            result = self._shellCmd(command, output=False, stdout=None,
                                    stderr=None)
        else:
            result = self._shellCmd(command, output=False)
        # Yabber error catch
        if result[1].endswith("Press any key to exit.\n"):
            self._output(None, result[1])
        # TODO: witchy error catch

    # Create the toml file for Mod Engine 2
    def _createModEngineFile(self):
        # get the paths with all the path separators converted to \\ for
        # the toml format
        hintsDir = self._currentDir().replace("/", "\\").replace("\\", "\\\\")
        randomizerDir = None
        if self._settingValue("useRandomizer"):
            randomizerDir = \
                self._randomizerDir.replace("/", "\\").replace("\\", "\\\\")
        fogDir = None
        if self._settingValue("useFogRandomizer"):
            fogDir = \
                self._fogRandomizerDir.replace("/", "\\").replace("\\", "\\\\")
        tomlText = toml + tomlModEntry.format("randomizerhints", hintsDir)
        if fogDir:
            tomlText += tomlModEntry.format("fog", fogDir)
        if randomizerDir:
            tomlText += tomlModEntry.format("randomizer", randomizerDir)
        tomlText += tomlEnd
        self._writeFile(tomlText, self._currentDir() + tomlFile)
