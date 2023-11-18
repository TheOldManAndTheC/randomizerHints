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

containerFixes = {
    # the spoilers file just uses "Kenneth Height" but in itemSlots.txt the full
    # name is used
    "Kenneth Haight": "Kenneth Haight, Limgrave Heir",
    # itemSlots.txt has "Tanith's Knight" in <> after the "Crucible Knight" in
    # the container name, but the spoilers file does enemy replacement with the
    # "Crucible Knight" name
    "Tanith's Knight": "Crucible Knight",
    # # itemSlots.txt uses "Fia's Champion" as the container name, but the
    # # spoilers file does enemy replacement with the "Fia's Champions" name
    # "Fia's Champion": "Fia's Champions"
}
