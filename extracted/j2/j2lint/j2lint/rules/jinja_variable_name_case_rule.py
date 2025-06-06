# Copyright (c) 2021-2025 Arista Networks, Inc.
# Use of this source code is governed by the MIT license
# that can be found in the LICENSE file.
"""jinja_variable_name_case_rule.py - Rule class to check the variables use lower case."""

from __future__ import annotations

import re
from typing import Any

from j2lint.linter.error import LinterError
from j2lint.linter.rule import Rule
from j2lint.utils import get_jinja_expressions

# pylint: disable=duplicate-code


class JinjaVariableNameCaseRule(Rule):
    """Rule class to check the variables use lower case."""

    rule_id = "V1"
    description = "All variables should use lower case: '{{ variable }}'"
    short_description = "jinja-variable-lower-case"
    severity = "LOW"

    regex = re.compile(r"([a-zA-Z0-9-_\"']*[A-Z][a-zA-Z0-9-_\"']*)")

    def __init__(self, ignore: bool = False, warn: list[Any] | None = None) -> None:
        super().__init__(ignore=ignore, warn=warn)

    def checktext(self, filename: str, text: str) -> list[LinterError]:
        """Not Implemented for this rule."""
        raise NotImplementedError

    def checkline(self, filename: str, line: str, line_no: int) -> list[LinterError]:
        """Check if the given line matches the error regex, which matches variables with non lower case characters.

        Parameters
        ----------
        filename
            The filename to which the line belongs.
        line
            The content of the line to check.
        line_no:
            The line number.

        Returns
        -------
        list[LinterError]
            The list of LinterError generated by this rule.
        """
        variables = get_jinja_expressions(line, blank_literals=True)
        all_matches = []
        for var in variables:
            var_matches = re.findall(self.regex, var)
            var_matches = [match for match in var_matches if (match not in ["False", "True"]) and ("'" not in match) and ('"' not in match)]
            all_matches.extend(var_matches)

        return [LinterError(line_no, line, filename, self, f"{self.description}: {match}") for match in all_matches]
