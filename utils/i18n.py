# @DCK@
# i18n for internationalization (localization)
# If you want to use this i18n.py python script in your projects,
# you must add this lines your python files,
# import i18n
# _ = i18n.language.gettext

import os
import locale
import gettext

APP_NAME = "internationalization"

# returns project directory
BASE_DIR = os.path.dirname(os.path.abspath(APP_NAME))

# returns BASE_DIR/i18n/ directory
LOCALE_DIR = os.path.join(BASE_DIR, 'i18n')

# So .mo files will then be located in BASE_DIR/i18n/LANGUAGECODE/LC_MESSAGES/
mo_location = LOCALE_DIR

# We need to choose the language.
# LANG env variable, determines the locale category for native language.
# We will provide a list, and gettext will use the first translation available in the list.
DEFAULT_LANGUAGES = os.environ.get('LANG', '').split(':')
DEFAULT_LANGUAGES += ['en_US']

language_code, encoding_type = locale.getdefaultlocale()

if language_code:
    languages = [language_code]

else:
    languages = DEFAULT_LANGUAGES

# description for gettext function.
gettext.install(True, localedir=None, unicode=1)

gettext.find(APP_NAME, mo_location)

gettext.textdomain(APP_NAME)

gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")

language = gettext.translation(APP_NAME, mo_location, languages=languages, fallback=True)