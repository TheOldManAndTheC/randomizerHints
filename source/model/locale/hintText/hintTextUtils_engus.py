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

from source.utils.rng import rng


textVariants = {
    "near": "close to|close by|nearby|near to|near",
    "far": "a long way|a long distance|a fair way|a fair distance|far away|far",
    "owns": "carries|holds|has|possesses|keeps|owns",
    "owned by": "carried by|held by|possessed by|kept by|owned by",
    "drop": "drop|have|possess|hold|keep|own",
    # "dropAlt": "drops|has|possesses|holds|keeps|owns",
    "dropped by": "dropped by|held by|possessed by|kept by|owned by",
    "contains": "contains|has within it",
    "within": "inside|within|in|contained inside|contained within|contained in",
    "in": "in|within|somewhere in|somewhere within",
    "sells": "sells|offers|offers for sale|has for sale|offers for purchase|"
             "has for purchase",
    "sold by":
        "sold by|offered for sale by|offered for purchase by|available from|"
        "available for sale from|available for purchase from",
    "killing": "killing|slaying|defeating",
    "after": "after|upon",
    "leads to": "leads to|goes to|reaches|arrives in|connects to",
    "leading to": "leading to|going to|reaching|to|arriving in|connecting to",
    "is connected to": "is connected to|is reachable from|is accessible from|"
                       "can be reached from",
    "passes through": "passes through|goes through|travels through|" 
                      "goes by way of",
    "passing through": "passing through|via|by way of|going through|"
                       "traveling through",
}


def articleOf(text, noArticles=None):
    if noArticles and text in noArticles:
        return ""
    if text[0] in "aeiouAEIOU":
        if text.startswith("One") or text.startswith("one"):
            return "a"
        return "an"
    return "a"


# exceptions should be a dictionary of strings mapped to replacement strings
def makePlural(text, exceptions=None):
    if exceptions:
        for exception in exceptions:
            if exception in text:
                return text.replace(exception, exceptions[exception])
    index = text.find(" (")
    if index == -1:
        index = text.find(" [")
    if index == -1:
        if text[-1] != "s":
            text = text + "s"
    elif text[index - 1] != "s":
        text = text[:index] + "s" + text[index:]
    return text


def randomText(text, delimiter="|"):
    return rng.choice(textVariants[text].split(delimiter))
