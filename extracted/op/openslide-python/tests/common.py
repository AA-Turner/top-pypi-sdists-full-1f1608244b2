#
# openslide-python - Python bindings for the OpenSlide library
#
# Copyright (c) 2016-2021 Benjamin Gilbert
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of version 2.1 of the GNU Lesser General Public License
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <https://www.gnu.org/licenses/>.
#

from __future__ import annotations

import os
from pathlib import Path

# Handle Windows-specific first-import logic here, so individual modules
# don't have to
if os.name == 'nt':
    # In application code, you probably shouldn't use an environment
    # variable for this, unless you're sure you can trust the contents of the
    # environment.
    _dll_path = os.getenv('OPENSLIDE_PATH')
    if _dll_path is not None:
        with os.add_dll_directory(_dll_path):  # type: ignore[attr-defined,unused-ignore]  # noqa: E501
            import openslide  # noqa: F401  module-imported-but-unused


def file_path(name: str) -> Path:
    return Path(__file__).parent / 'fixtures' / name
