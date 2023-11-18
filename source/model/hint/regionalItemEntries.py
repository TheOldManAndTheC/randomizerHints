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

from source.data.model.hintData.neighboringRegions import neighboringRegions


# From a list of item entries find items in the same region as the source
# item entry.  If the neighboring flag is set, find entries from neighboring
# regions instead
def regionalItemEntries(entryList, sourceItemEntry, neighboring=False):
    regionalEntries = []
    if "hintRegion" not in sourceItemEntry:
        return regionalEntries
    if neighboring:
        regions = neighboringRegions[sourceItemEntry["hintRegion"]]
    else:
        regions = [sourceItemEntry["hintRegion"]]
    for itemEntry in entryList:
        if "hintRegion" in itemEntry and itemEntry["hintRegion"] in regions:
            regionalEntries.append(itemEntry)
    return regionalEntries
