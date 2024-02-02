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

from source.model.fog.loadFog import loadFog
from source.model.fog.loadFogSpoilers import loadFogSpoilers
from source.data.model.fogData.fogData import fogAreaFixes
from source.data.model.fogData.fogData import fogArrivalAreas
from source.data.model.fogData.fogData import fogBigAreaFixes
from source.data.model.fogData.fogData import fogBlockedConditions
from source.data.model.fogData.fogData import fogDropFixes
from source.data.model.fogData.fogData import fogIgnoreGates
from source.data.model.fogData.fogData import fogNewGateAreas
from source.data.model.fogData.fogData import fogNoNewGateArea
from source.data.model.fogData.fogData import fogReverseWarps
from source.data.model.fogData.fogData import fogReversibleWarps
from source.data.model.fogData.fogGateLots import fogGateLots


# find a big area list in a set of big area lists given an area name
def getBigAreaList(bigAreas, areaName):
    for bigAreaList in bigAreas:
        if areaName in bigAreaList:
            return bigAreaList
    return None


# return any custom arrival point area text
# gateKey is "text" in all fog.text and gate structure data, "gate" should only
# be used for the fog spoilers data
def getArrivalArea(areaName, gateEntry, gateKey="text"):
    if gateKey in gateEntry and areaName in fogArrivalAreas and \
            gateEntry[gateKey] in fogArrivalAreas[areaName]:
        return fogArrivalAreas[areaName][gateEntry[gateKey]]
    return None


# if there is custom area hint text for a given gate, add it to the gate entry
def setHintArea(gateEntry):
    areaName = gateEntry["area"]
    gateText = gateEntry["text"]
    if areaName in fogGateLots and gateText in fogGateLots[areaName] and \
            "hintArea" in fogGateLots[areaName][gateText]:
        gateEntry["hintArea"] = fogGateLots[areaName][gateText]["hintArea"]
        return
    # if the newgate option is off, and it's the big lands between area, check
    # fogGateLots for both big subareas
    if areaName == fogNoNewGateArea:
        for subArea in fogNewGateAreas:
            if subArea in fogGateLots and gateText in fogGateLots[subArea] and \
                    "hintArea" in fogGateLots[subArea][gateText]:
                gateEntry["hintArea"] = \
                    fogGateLots[subArea][gateText]["hintArea"]
                return


# read in the fog.txt and fog spoilers file and generate a traversable area
# network to be used for generating hints
def processFog(fogLines, fogSpoilerLines):
    # read fog.txt
    fog = loadFog(fogLines)
    # read spoiler file and get options
    fogSpoilers, fog["options"] = loadFogSpoilers(fogSpoilerLines)
    # get the seed from the options
    fog["fogSeed"] = fog["options"].split("seed:")[2].split(" ")[0]
    if fog["fogSeed"][-1] == "\n":
        fog["fogSeed"] = fog["fogSeed"][:-1]
    coupledMinor = "coupledminor" in fog["options"]
    coupledWarp = "coupledwarp" in fog["options"]
    # special case fixes:
    # if the new fog between liurnia and stormhill is not there, make them
    # contiguous
    if "newgate" not in fog["options"]:
        fog["areas"]["stormhill"]["to"]["liurnia"] = {}
        fog["areas"]["liurnia"]["to"]["stormhill"] = {}
    # add an "area" to be used for the Pureblood Knight's Medal warp, so it
    # isn't added to the network
    fog["areas"]["pureblood"] = {"text": "anywhere"}
    # alter the spoilers so that there is an entry for the area with the
    # medal warp
    fogSpoilers["anywhere"] = {
        "using the Pureblood Knight's Medal from anywhere": [
            fogSpoilers["Chapel of Anticipation"]["using the Pureblood Knight's"
                                                  " Medal from anywhere"][0]
        ]
    }
    # remove the entry from the Chapel of Anticipation spoilers
    fogSpoilers["Chapel of Anticipation"].pop("using the Pureblood Knight's "
                                              "Medal from anywhere")
    # change the warp's source area to point to our special area instead
    fog["warps"]["12052021"]["aSide"]["area"] = "pureblood"

    # process the areas to apply fixes and set preexisting transitions
    bigAreas = []
    # make a lookup dictionary for area names
    fog["areaNames"] = dict()
    for areaName in fog["areas"]:
        areaEntry = fog["areas"][areaName]
        # if there's no text key, or it's not in our area fixes, ignore it
        if "text" not in areaEntry or areaName not in fogAreaFixes:
            areaEntry["ignore"] = True
            continue
        # link the spoiler text to the area name in the lookup dictionary
        fog["areaNames"][areaEntry["text"]] = areaName
        # apply missing one way preexisting transition fixes
        if areaName in fogDropFixes:
            for toAreaName in fogDropFixes[areaName]:
                toEntry = fog["areas"][areaName]["to"][toAreaName]
                if "tags" in toEntry:
                    toEntry["tags"] += " drop"
                else:
                    toEntry["tags"] = "drop"
        # apply area fixes
        for key in fogAreaFixes[areaName]:
            areaEntry[key] = fogAreaFixes[areaName][key]
        # if the area is a node when the coupledwarp option is off, set it
        if "isCoupledWarpNode" in areaEntry and \
                "coupledwarp" not in fog["options"]:
            areaEntry["isNode"] = True
        # add a new dictionary to the area entry for gates
        areaEntry["gates"] = dict()
        # process preexisting two-way connections to find contiguous areas
        # see if there's a big area list with this area already in it
        bigAreaList = getBigAreaList(bigAreas, areaName)
        if bigAreaList is None:
            # if not, see if there is one in the fog big area fixes
            bigAreaList = getBigAreaList(fogBigAreaFixes, areaName)
            if bigAreaList is None:
                # otherwise, just make a new one
                bigAreaList = [areaName]
            bigAreas.append(bigAreaList)
        # if there are no preexisting transitions, we're done with this entry
        if "to" not in areaEntry:
            continue
        # process the preexisting connections for this area
        for toAreaName in areaEntry["to"]:
            # if the area is already in this big area list, skip
            if toAreaName in bigAreaList:
                continue
            toEntry = areaEntry["to"][toAreaName]
            # skip gates we want to ignore
            if "text" in toEntry and toEntry["text"] in fogIgnoreGates:
                continue
            if "tags" in toEntry:
                # if it's a crawl only entry, skip it
                if "crawlonly" in toEntry["tags"]:
                    continue
                # if it's a one way connection, add it as a gate
                if "drop" in toEntry["tags"]:
                    areaEntry["gates"][toEntry["text"]] = {
                        "area": toAreaName
                    }
                    # if there is custom text for the arrival point add it to
                    # the gate entry
                    hintArea = getArrivalArea(toAreaName, toEntry)
                    if hintArea:
                        areaEntry["gates"][toEntry["text"]]["hintArea"] = \
                            hintArea
                    continue
            # get the big area list for the connected area
            toAreaList = getBigAreaList(bigAreas, toAreaName)
            # if there isn't one, it hasn't been processed yet, skip it
            if toAreaList is None:
                continue
            # there is a separate area list so combine them
            for name in toAreaList:
                if name not in bigAreaList:
                    bigAreaList.append(name)
            bigAreas.remove(toAreaList)

    # create the combined area entries
    for bigAreaList in bigAreas:
        # singleton lists aren't combined areas
        if len(bigAreaList) <= 1:
            continue
        bigAreaList.sort()
        bigAreaEntry = {
            "subAreas": bigAreaList,
            "gates": {}
        }
        # create the combined area name
        bigAreaName = ""
        for bigAreaSubName in bigAreaList:
            bigAreaName += "|" + bigAreaSubName
        bigAreaName = bigAreaName[1:]
        # apply area fixes
        for key in fogAreaFixes[bigAreaName]:
            bigAreaEntry[key] = fogAreaFixes[bigAreaName][key]
        # if the area is a node when the coupledwarp option is off, set it
        if "isCoupledWarpNode" in bigAreaEntry and \
                "coupledwarp" not in fog["options"]:
            bigAreaEntry["isNode"] = True
        fog["areas"][bigAreaName] = bigAreaEntry
        # add the big area name to the sub area entries that are within it
        for subAreaName in bigAreaList:
            fog["areas"][subAreaName]["bigArea"] = bigAreaName
            # set the spoiler text for each sub area to point to the big area
            for areaText in fog["areaNames"]:
                if fog["areaNames"][areaText] == subAreaName:
                    fog["areaNames"][areaText] = bigAreaName
            # also add area name linkages to the big area name
            fog["areaNames"][subAreaName] = bigAreaName
            # copy any existing gate entries from the sub areas
            for gateName in fog["areas"][subAreaName]["gates"]:
                bigAreaEntry["gates"][gateName] = \
                    fog["areas"][subAreaName]["gates"][gateName]
    # do a pass through all the areas to make sure their gate entries have
    # big areas instead of subareas
    for areaName in fog["areas"]:
        if "gates" not in fog["areas"][areaName]:
            continue
        for gateName in fog["areas"][areaName]["gates"]:
            gateEntry = fog["areas"][areaName]["gates"][gateName]
            if gateEntry["area"] in fog["areaNames"]:
                gateEntry["area"] = fog["areaNames"][gateEntry["area"]]

    # build the area gates structures from the warps and entrances
    fog["gates"] = dict()

    # inline method to add a gate to the gates structure
    def addGate(areaName, gateText, gateEntry):
        # if there's no gate structure entry for this area, add one
        if areaName not in fog["gates"]:
            fog["gates"][areaName] = dict()
        # if there's no entries for this gate key, just add it
        if gateText not in fog["gates"][areaName]:
            fog["gates"][areaName][gateText] = {gateEntry["id"]: gateEntry}
            return
        # if there's already a gate with the same endpoints, skip this one
        for prevID in fog["gates"][areaName][gateText]:
            prevEntry = fog["gates"][areaName][gateText][prevID]
            if prevEntry["aSide"]["area"] == gateEntry["aSide"]["area"] and \
                    prevEntry["bSide"]["area"] == gateEntry["bSide"]["area"]:
                return
        # some gate targets will have multiple gates pointing to them, preserve
        # by unique id for now
        fog["gates"][areaName][gateText][gateEntry["id"]] = gateEntry

    # inline method to check gate entries for basic disqualifying data and
    # update them with big area keys
    def processGateEntry(gateEntry):
        # ignore gates tagged as remove, are crawl only, or are in the ignore
        # list
        if ("remove" in gateEntry["tags"] and
            "openremove" not in gateEntry["tags"]) \
                or "crawlonly" in gateEntry["tags"] \
                or gateEntry["text"] in fogIgnoreGates:
            return False
        # get the entries for both sides of the gate
        aSideEntry = gateEntry["aSide"]
        bSideEntry = gateEntry["bSide"]
        # there are some entries with no spoiler text, ignore
        if aSideEntry["text"] == "''" or bSideEntry["text"] == "''":
            return False
        # if the areas are part of a big area, update the entry
        if aSideEntry["area"] in fog["areaNames"]:
            aSideEntry["area"] = fog["areaNames"][aSideEntry["area"]]
        if bSideEntry["area"] in fog["areaNames"]:
            bSideEntry["area"] = fog["areaNames"][bSideEntry["area"]]
        # add both sides to the gate structure
        addGate(aSideEntry["area"], aSideEntry["text"], gateEntry)
        addGate(bSideEntry["area"], bSideEntry["text"], gateEntry)
        return True

    # process warps
    for warpID in fog["warps"]:
        warpEntry = fog["warps"][warpID]
        if not processGateEntry(warpEntry):
            continue
        # mark as a warp
        warpEntry["isWarp"] = True
        # if it's a reversible warp, add the key for the reverse warp
        if coupledWarp and "uniquegate" in warpEntry["tags"] or \
                (coupledMinor and "uniqueminor" in warpEntry["tags"]) or \
                "evergaol" in warpEntry["tags"] or \
                warpEntry["text"] in fogReversibleWarps:
            warpEntry["reverseWarp"] = fogReverseWarps[warpEntry["text"]]

    # process fog entrances
    for assetID in fog["entrances"]:
        assetList = fog["entrances"][assetID]
        # convert singleton entries to lists
        if isinstance(assetList, dict):
            assetList = [assetList]
        for entranceEntry in assetList:
            if not processGateEntry(entranceEntry):
                continue
            # get the entries for both sides of the gate
            aSideEntry = entranceEntry["aSide"]
            bSideEntry = entranceEntry["bSide"]
            # if there are conditions that can block movement into the area
            # when passing through into a side, mark the side as blocked
            if "cond" in aSideEntry and \
                    (aSideEntry["cond"] == aSideEntry["area"] or
                     aSideEntry["cond"] in fogBlockedConditions):
                aSideEntry["isBlocked"] = True
            if "cond" in bSideEntry and \
                    (bSideEntry["cond"] == bSideEntry["area"] or
                     bSideEntry["cond"] in fogBlockedConditions):
                bSideEntry["isBlocked"] = True

    # process spoilers and add their gate information to the areas structure

    # inline method to find a gate entry and key within an area that corresponds
    # to a given gate spoiler text
    # the spoiler text may be a warp arrival point for a reversible warp,
    # which requires using the reverseWarp entry to find the correct entrance
    # warp
    def matchingGate(areaName, gateText):
        # if there's no entries for the given area or gate spoiler text, ignore
        if areaName not in fog["gates"]:
            return None, None
        if gateText not in fog["gates"][areaName]:
            return None, None
        # since some gates have multiple entries, we need to check them all
        # the significant case is that of "arriving at South Raya Lucaria Gate"
        # which appears as the exit point for two warps, one of which can be
        # reversible
        matches = []
        for gateEntry in list(fog["gates"][areaName][gateText].values()):
            newGateEntry = gateEntry
            newGateText = gateText
            # if it's the arrival point of the warp
            if "isWarp" in newGateEntry and \
                    areaName == newGateEntry["bSide"]["area"] \
                    and newGateText == newGateEntry["bSide"]["text"]:
                # if there's no reverse warp, ignore
                if "reverseWarp" not in newGateEntry:
                    continue
                # use the reverse warp as the gate entry instead
                newGateText = newGateEntry["reverseWarp"]
                newGateEntry = \
                    list(fog["gates"][areaName][newGateText].values())[0]
            # add the matched gate entry and key
            matches.append((newGateEntry, newGateText))
        # if there are multiple matches they are normal/ashen transitions where
        # the aSide is the same but the bSide is different, for our purposes
        # either will do
        if matches:
            return matches[0]
        return None, None

    # go through the spoiler areas
    for areaText in fogSpoilers:
        # ignore areas that aren't part of the network
        if areaText not in fog["areaNames"]:
            continue
        areaName = fog["areaNames"][areaText]
        # ignore areas that don't have gates
        if areaName not in fog["gates"]:
            continue
        areaGates = fog["areas"][areaName]["gates"]
        # go through the arrival points for this area
        for gateText in fogSpoilers[areaText]:
            # if it's a map transition it's been handled in parsing fog.txt
            if gateText == "in map":
                continue
            # if the gate is already in the area's gate entries, skip it,
            # it's been handled
            if gateText in areaGates:
                continue
            gateEntry, gateSideText = matchingGate(areaName, gateText)
            if not gateEntry:
                continue
            # step through the spoiler entries for this arrival point
            for spoilerEntry in fogSpoilers[areaText][gateText]:
                # ignore areas that aren't part of the network
                if spoilerEntry["area"] not in fog["areaNames"]:
                    continue
                # get the area on the other side of the gate
                destAreaName = fog["areaNames"][spoilerEntry["area"]]
                # if there is gate text in the entry, get it
                destGateEntry = None
                destGateText = None
                if "gate" in spoilerEntry:
                    destGateEntry, destGateText = \
                        matchingGate(destAreaName, spoilerEntry["gate"])
                twoWay = "isWarp" not in gateEntry or "reverseWarp" in gateEntry
                # if it's a one way gate, just add the destination area with no
                # gate key
                if not destGateEntry or not twoWay:
                    areaGates[gateSideText] = {
                        "area": destAreaName
                    }
                    # if there is custom area text for the arrival point, add
                    # it to the gate entry
                    hintArea = getArrivalArea(destAreaName, spoilerEntry,
                                              "gate")
                    if hintArea:
                        areaGates[gateSideText]["hintArea"] = hintArea
                    continue
                destTwoWay = "isWarp" not in destGateEntry or \
                             "reverseWarp" in destGateEntry
                # if the directionality of the two gates does not match, as in
                # the case where "arriving at South Raya Lucaria Gate" is an
                # arrival point for both one way and two-way warps, do not add
                if twoWay != destTwoWay:
                    continue
                # get the correct side entry for the destination gate side text
                if destGateEntry["aSide"]["area"] == destAreaName and \
                        destGateEntry["aSide"]["text"] == destGateText:
                    destSideEntry = destGateEntry["aSide"]
                else:
                    destSideEntry = destGateEntry["bSide"]
                # if there is custom area text for the destination gate, add it
                setHintArea(destSideEntry)
                areaGates[gateSideText] = destSideEntry
    return fog
