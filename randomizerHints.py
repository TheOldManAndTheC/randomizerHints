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

# Generate in-game hints for Elden Ring Item and Enemy Randomizer
import logging
import traceback

from source.controller.RandomizerHintsController \
    import RandomizerHintsController

options = {
    "name": "mainController",
    "modelOptions": {
        "name": "mainModel",
    },
    "viewOptions": {
        "name": "mainView",
        "title": "Elden Ring Randomizer Hints",
        "minWidth": 1600,
        "minHeight": 800,
        "packFill": "both",
        "packExpand": True,
    }
}

if __name__ == '__main__':
    try:
        controller = RandomizerHintsController(**options)
        controller.view().mainloop()
    except Exception as e:
        logging.basicConfig(filename="crash.log", level=logging.DEBUG)
        logging.debug(traceback.format_exc())
        raise
