# -*- coding: utf-8 -*-

import gettext

from plugin.settings import LOCAL, TRANSLATIONS_PATH

# localization
translation = gettext.translation(
    "messages",
    TRANSLATIONS_PATH,
    languages=[LOCAL],
)

_l = translation.gettext
