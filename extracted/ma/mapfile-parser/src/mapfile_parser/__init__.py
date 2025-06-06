#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2022-2024 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

__version_info__ = (2, 9, 4)
__version__ = ".".join(map(str, __version_info__)) # + "-dev0"
__author__ = "Decompollaborate"

from . import utils as utils

from .mapfile import MapFile as MapFile
from .mapfile import Symbol as Symbol
from .mapfile import Section as Section
from .mapfile import Segment as Segment
from .mapfile import FoundSymbolInfo as FoundSymbolInfo
from .mapfile import SymbolComparisonInfo as SymbolComparisonInfo
from .mapfile import MapsComparisonInfo as MapsComparisonInfo
from .mapfile import ReportCategories as ReportCategories

from .progress_stats import ProgressStats as ProgressStats

from . import frontends as frontends

# Renamed types
from .mapfile import Section as File
