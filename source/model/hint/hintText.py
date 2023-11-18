#  Copyright (c) 2023 The Old Man and the C
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

from source.model.locale.hintText.hintText_engus import hintText_engus
from source.model.locale.hintText.hintText_deude import hintText_deude
from source.model.locale.hintText.hintText_frafr import hintText_frafr
from source.model.locale.hintText.hintText_itait import hintText_itait
from source.model.locale.hintText.hintText_jpnjp import hintText_jpnjp
from source.model.locale.hintText.hintText_korkr import hintText_korkr
from source.model.locale.hintText.hintText_polpl import hintText_polpl
from source.model.locale.hintText.hintText_porbr import hintText_porbr
from source.model.locale.hintText.hintText_rusru import hintText_rusru
from source.model.locale.hintText.hintText_spaar import hintText_spaar
from source.model.locale.hintText.hintText_spaes import hintText_spaes
from source.model.locale.hintText.hintText_thath import hintText_thath
from source.model.locale.hintText.hintText_zhocn import hintText_zhocn
from source.model.locale.hintText.hintText_zhotw import hintText_zhotw


def hintText(components, localeData, language):
    match language:
        case "engus":
            return hintText_engus(components, localeData[language])
        case "deude":
            return hintText_deude(components, localeData[language])
        case "frafr":
            return hintText_frafr(components, localeData[language])
        case "itait":
            return hintText_itait(components, localeData[language])
        case "jpnjp":
            return hintText_jpnjp(components, localeData[language])
        case "korkr":
            return hintText_korkr(components, localeData[language])
        case "polpl":
            return hintText_polpl(components, localeData[language])
        case "porbr":
            return hintText_porbr(components, localeData[language])
        case "rusru":
            return hintText_rusru(components, localeData[language])
        case "spaar":
            return hintText_spaar(components, localeData[language])
        case "spaes":
            return hintText_spaes(components, localeData[language])
        case "thath":
            return hintText_thath(components, localeData[language])
        case "zhocn":
            return hintText_zhocn(components, localeData[language])
        case "zhotw":
            return hintText_zhotw(components, localeData[language])
