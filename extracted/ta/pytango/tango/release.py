# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
This is an internal PyTango module.
"""

__all__ = ("Release",)

__docformat__ = "restructuredtext"


class Release:
    """Summarize release information as class attributes.

    Release information:
        - name: (str) package name
        - version_info: (tuple<int,int,int,str,int>) The five components
          of the version number: major, minor, micro, releaselevel, and
          serial.
        - version: (str) package version in format <major>.<minor>.<micro>
        - release: (str) pre-release, post-release or development release;
          it is empty for final releases.
        - version_long: (str) package version in format
          <major>.<minor>.<micro><releaselevel><serial>
        - version_description: (str) short description for the current
          version
        - version_number: (int) <major>*100 + <minor>*10 + <micro>
        - description : (str) package description
        - long_description: (str) longer package description
        - authors: (dict<str(last name), tuple<str(full name),str(email)>>)
          package authors
        - url: (str) package url
        - download_url: (str) package download url
        - platform: (seq<str>) list of available platforms
        - keywords: (seq<str>) list of keywords
        - license: (str) the license
    """

    name = "pytango"
    version_info = (10, 0, 2)
    version = ".".join(map(str, version_info[:3]))
    release = "".join(map(str, version_info[3:]))
    separator = "." if "dev" in release or "post" in release else ""
    version_long = version + separator + release

    version_description = "This version implements the C++ Tango 10.0 API."
    version_number = int(version.replace(".", ""))
    description = "A python binding for the Tango control system"
    long_description = "This module implements the Python Tango Device API mapping."
    license = "LGPL"
    authors = {"Coutinho": ("Tiago Coutinho", "coutinho@esrf.fr")}
    author_lines = "\n".join([f"{x[0]} <{x[1]}>" for x in authors.values()])
    url = "http://gitlab.com/tango-controls/pytango"
    download_url = "http://pypi.python.org/pypi/pytango"
    platform = ["Linux", "Windows", "macOS"]
    keywords = ["Tango", "CORBA", "binding"]
