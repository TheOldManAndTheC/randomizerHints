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
from source.utils.rng import rng


# Returns a random number in a range of 0 to length -1  where the odds get
# worse for later numbers in the range using to a triangular distribution
def triangularRandom(length):
    odds = int(length * (length + 1) / 2)
    if odds == 1:
        return 0
    pick = rng.randint(1, odds)
    result = length - int(round(math.sqrt(pick * 2)))
    return result


# Returns a random number from 1 to maxCount with heavy bias towards higher
# numbers for hint entry generation. Value returned will never be more than 4.
def hintCountRandom(maxCount=4):
    pick = rng.randint(1, 100)
    if maxCount >= 4 and pick <= 50:
        return 4
    if maxCount >= 3 and pick <= 80:
        return 3
    if maxCount >= 2 and pick <= 95:
        return 2
    return 1
