#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2022-2024 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import decomp_settings
from pathlib import Path

from .. import mapfile


def doSymbolSizesCsv(mapPath: Path, outputPath: Path|None, filterSection: str|None=None, sameFolder: bool=False, symbolsSummary: bool=False, allFiles: bool=False) -> int:
    if not mapPath.exists():
        print(f"Could not find mapfile at '{mapPath}'")
        return 1

    mapFile = mapfile.MapFile()
    mapFile.readMapFile(mapPath)

    if filterSection is not None:
        mapFile = mapFile.filterBySectionType(filterSection)

    if sameFolder:
        mapFile = mapFile.mixFolders()

    if symbolsSummary:
        output = mapFile.toCsvSymbols()
    else:
        output = mapFile.toCsv(printVram=not sameFolder, skipWithoutSymbols=not allFiles)

    if outputPath is None:
        print(output)
    else:
        outputPath.parent.mkdir(parents=True, exist_ok=True)
        outputPath.write_text(output)

    return 0

def processArguments(args: argparse.Namespace, decompConfig: decomp_settings.Config|None=None):
    if decompConfig is not None:
        version = decompConfig.get_version_by_name(args.version)
        assert version is not None, f"Invalid version '{args.version}' selected"

        mapPath = Path(version.paths.map)
    else:
        mapPath = args.mapfile

    outputPath: Path|None = Path(args.output) if args.output is not None else None
    filterSection: str|None = args.filter_section
    sameFolder: bool = args.same_folder
    symbolsSummary: bool = args.symbols
    allFiles: bool = args.all

    exit(doSymbolSizesCsv(mapPath, outputPath, filterSection, sameFolder, symbolsSummary, allFiles))

def addSubparser(subparser: argparse._SubParsersAction[argparse.ArgumentParser], decompConfig: decomp_settings.Config|None=None):
    parser = subparser.add_parser("symbol_sizes_csv", help="Produces a csv summarizing the files sizes by parsing a map file.")

    emitMapfile = True
    if decompConfig is not None:
        versions = []
        for version in decompConfig.versions:
            versions.append(version.name)

        if len(versions) > 0:
            parser.add_argument("-v", "--version", help="Version to process from the decomp.yaml file", type=str, choices=versions, default=versions[0])
            emitMapfile = False

    if emitMapfile:
        parser.add_argument("mapfile", help="Path to a map file.", type=Path)

    parser.add_argument("-o", "--output", help="Output path of for the generated csv. If omitted then stdout is used instead.")
    parser.add_argument("--same-folder", help="Mix files in the same folder.", action="store_true")
    parser.add_argument("--symbols", help="Prints the size of every symbol instead of a summary.", action="store_true")
    parser.add_argument("-a", "--all", help="Don't skip files without symbols.", action="store_true")
    parser.add_argument("-f", "--filter-section", help="Only print the symbols of the passed section. For example: .text")

    parser.set_defaults(func=processArguments)
