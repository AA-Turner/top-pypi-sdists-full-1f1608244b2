# encoding: utf8

from __future__ import annotations

from typing_extensions import override

from pyinfra.api import FactBase

from .util.packaging import parse_packages

CARGO_REGEX = r"^([a-zA-Z0-9\-]+)\sv([0-9\.]+)"


class CargoPackages(FactBase):
    """
    Returns a dict of installed cargo packages globally:

    .. code:: python

        {
            "package_name": ["version"],
        }
    """

    default = dict

    @override
    def command(self) -> str:
        return "cargo install --list"

    @override
    def requires_command(self) -> str:
        return "cargo"

    @override
    def process(self, output):
        return parse_packages(CARGO_REGEX, output)
