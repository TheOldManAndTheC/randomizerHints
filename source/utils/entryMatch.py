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

# Checks a dictionary entry against a matching dictionary.  If all the keys and
# values in the matching dictionary that are not in the ignore list are the
# same in the entry dictionary, it's a match.
def entryMatch(entry, match, ignore=None):
    if ignore is None:
        ignore = []
    matches = True
    for key in match:
        if key in ignore:
            continue
        matches = key in entry and match[key] == entry[key]
        if not matches:
            break
    return matches
