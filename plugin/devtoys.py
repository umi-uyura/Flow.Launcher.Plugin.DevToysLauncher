# -*- coding: utf-8 -*-

import subprocess
from plugin.extensions import _l

DEVTOYS_TOOLS = (
    {
        "tool": "base64",
        "name": _l("TOOLNAME_BASE64")
    },
    {
        "tool": "base64img",
        "name": _l("TOOLNAME_BASE64IMG")
    },
    {
        "tool": "gzip",
        "name": _l("TOOLNAME_GZIP")
    },
    {
        "tool": "hash",
        "name": _l("TOOLNAME_HASH")
    },
    {
        "tool": "uuid",
        "name": _l("TOOLNAME_UUID")
    },
    {
        "tool": "loremipsum",
        "name": _l("TOOLNAME_LOREMIPSUM")
    },
    {
        "tool": "checksum",
        "name": _l("TOOLNAME_CHECKSUM")
    },
    {
        "tool": "cronparser",
        "name": _l("TOOLNAME_CRONPARSER")
    },
    {
        "tool": "jsonformat",
        "name": _l("TOOLNAME_JSONFORMAT")
    },
    {
        "tool": "sqlformat",
        "name": _l("TOOLNAME_SQLFORMAT")
    },
    {
        "tool": "xmlformat",
        "name": _l("TOOLNAME_XMLFORMAT")
    },
    {
        "tool": "jsonyaml",
        "name": _l("TOOLNAME_JSONYAML")
    },
    {
        "tool": "jwt",
        "name": _l("TOOLNAME_JWT")
    },
    {
        "tool": "colorblind",
        "name": _l("TOOLNAME_COLORBLIND")
    },
    {
        "tool": "color",
        "name": _l("TOOLNAME_COLOR")
    },
    {
        "tool": "imgcomp",
        "name": _l("TOOLNAME_IMGCOMP")
    },
    {
        "tool": "imageconverter",
        "name": _l("TOOLNAME_IMAGECONVERTER")
    },
    {
        "tool": "markdown",
        "name": _l("TOOLNAME_MARKDOWN")
    },
    {
        "tool": "regex",
        "name": _l("TOOLNAME_REGEX")
    },
    {
        "tool": "time",
        "name": _l("TOOLNAME_TIME")
    },
    {
        "tool": "baseconverter",
        "name": _l("TOOLNAME_BASECONVERTER")
    },
    {
        "tool": "string",
        "name": _l("TOOLNAME_STRING")
    },
    {
        "tool": "url",
        "name": _l("TOOLNAME_URL")
    },
    {
        "tool": "html",
        "name": _l("TOOLNAME_HTML")
    },
    {
        "tool": "diff",
        "name": _l("TOOLNAME_DIFF")
    },
    {
        "tool": "xmlvalidator",
        "name": _l("TOOLNAME_XMLVALIDATOR")
    },
    {
        "tool": "escape",
        "name": _l("TOOLNAME_ESCAPE")
    },
    {
        "tool": "settings",
        "name": _l("TOOLNAME_SETTINGS")
    }
)

def startTool(tool):
    cmd=f"start devtoys:?tool={tool}".format(tool=tool)
    subprocess.run(cmd, shell=True)
