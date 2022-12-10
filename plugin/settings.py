# -*- coding: utf-8 -*-


import os
from pathlib import Path

from dotenv import load_dotenv

setting_pyfile = Path(__file__).resolve()
pludir = setting_pyfile.parent
basedir = pludir.parent

dotenv_path = basedir / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)


# The default value can work, if no user config.
CONFIG = os.getenv("CONFIG", "default config")
LOCAL = os.getenv("local", "en")


# the information of package
__app_name__ = "DevToys Launcher"
__package_name__ = "Flow.Launcher.Plugin.DevToysLauncher"
__version__ = "1.0.0"
__short_description__ = "Launch DevToys tools"
GITHUB_USERNAME = "umi-uyura"


readme_path = basedir / "README.md"
try:
    __long_description__ = open(readme_path, "r").read()
except:
    __long_description__ = __short_description__


# extensions
TRANSLATIONS_PATH = basedir / "plugin/translations"

# plugin.json
PLUGIN_ID = "14b986ef-45ec-44c1-be66-cab460a771f7"  # could generate via python `uuid` official package
ICON_PATH = "assets/300x300.png"
PLUGIN_AUTHOR = "Umi Uyura"
PLUGIN_ACTION_KEYWORD = "dtoys"
PLUGIN_PROGRAM_LANG = "python"
PLUGIN_EXECUTE_FILENAME = "main.py"
PLUGIN_ZIP_NAME = f"{__package_name__}-{__version__}.zip"
PLUGIN_URL = f"https://github.com/{GITHUB_USERNAME}/{__package_name__}"
PLUGIN_URL_SOURCE_CODE = f"https://github.com/{GITHUB_USERNAME}/{__package_name__}"
PLUGIN_URL_DOWNLOAD = (
    f"{PLUGIN_URL_SOURCE_CODE}/releases/download/v{__version__}/{PLUGIN_ZIP_NAME}"
)
