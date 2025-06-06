"""Utility functions for hoppr plug-ins."""

from __future__ import annotations

import urllib.parse

from shutil import which

from hoppr.result import Result


def dir_name_from_repo_url(repo: str) -> str:
    """Creates a directory name based on a repo url."""
    if not repo.endswith("://"):
        repo = repo.removesuffix("/")

    return urllib.parse.quote_plus(repo)


def repo_url_from_dir_name(dir_name: str) -> str:
    """Reconstitutes a repo url from a directory name generated by dir_name_from_repo_url."""
    return urllib.parse.unquote_plus(dir_name)


def get_missing_commands(cmd_list: list[str] | list[str | list[str]]) -> list[str]:
    """Determine which items from a list of required commands are unavailable."""
    flattened_cmd_list: list[str] = []

    for cmd in cmd_list:
        flattened_cmd_list.extend(cmd if isinstance(cmd, list) else [cmd])

    return [cmd for cmd in flattened_cmd_list if not which(cmd)]


def check_for_missing_commands(cmd_list: list[str] | list[str | list[str]]) -> Result:
    """Raise an exception if any of a list of required commands are unavailable."""
    return (
        Result.fail(
            f"The following required commands are unavailable: {', '.join(missing_cmds)}. Please install and try again."
        )
        if (missing_cmds := get_missing_commands(cmd_list))
        else Result.success()
    )
