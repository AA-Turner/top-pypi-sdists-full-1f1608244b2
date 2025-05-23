#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""Output formatters for JSON."""

import argparse
import collections.abc
import json
import typing as ty

from cliff import columns
from cliff.formatters import base


class JSONFormatter(base.ListFormatter, base.SingleFormatter):
    def add_argument_group(self, parser: argparse.ArgumentParser) -> None:
        group = parser.add_argument_group(title='json formatter')
        group.add_argument(
            '--noindent',
            action='store_true',
            dest='noindent',
            help='whether to disable indenting the JSON',
        )

    def emit_list(
        self,
        column_names: collections.abc.Sequence[str],
        data: collections.abc.Iterable[collections.abc.Sequence[ty.Any]],
        stdout: ty.TextIO,
        parsed_args: argparse.Namespace,
    ) -> None:
        items = []
        for item in data:
            items.append(
                {
                    n: (
                        i.machine_readable()
                        if isinstance(i, columns.FormattableColumn)
                        else i
                    )
                    for n, i in zip(column_names, item)
                }
            )
        indent = None if parsed_args.noindent else 2
        json.dump(items, stdout, indent=indent)
        stdout.write('\n')

    def emit_one(
        self,
        column_names: collections.abc.Sequence[str],
        data: collections.abc.Sequence[ty.Any],
        stdout: ty.TextIO,
        parsed_args: argparse.Namespace,
    ) -> None:
        one = {
            n: (
                i.machine_readable()
                if isinstance(i, columns.FormattableColumn)
                else i
            )
            for n, i in zip(column_names, data)
        }
        indent = None if parsed_args.noindent else 2
        json.dump(one, stdout, indent=indent)
        stdout.write('\n')
