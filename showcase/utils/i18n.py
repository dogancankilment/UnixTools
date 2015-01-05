import os
import locale
import gettext


APP_NAME = "internationalization"

BASE_DIR = os.path.dirname(os.path.abspath(APP_NAME))

LOCALE_DIR = os.path.join(BASE_DIR, 'i18n')

mo_location = LOCALE_DIR

DEFAULT_LANGUAGES = os.environ.get('LANG', '').split(':')
DEFAULT_LANGUAGES += ['en_US']

language_code, encoding_type = locale.getdefaultlocale()

if language_code:
    languages = [language_code]

languages += DEFAULT_LANGUAGES

gettext.install(True, localedir=None, unicode=1)

gettext.find(APP_NAME, mo_location)

gettext.textdomain(APP_NAME)

gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")

language = gettext.translation(APP_NAME, mo_location, languages=languages, fallback=True)