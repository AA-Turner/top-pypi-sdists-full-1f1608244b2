# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""FileObjectAdapter class.

Used in conjunction with PythonOutputStream/PythonInputStream to allow a C++
OutputStream/InputStream to interact with a Python file-like object.
"""

import io
from typing import BinaryIO

from tink.cc.pybind import tink_bindings


class FileObjectAdapter(tink_bindings.PythonFileObjectAdapter):
  """Adapts a Python file object for use in C++."""

  def __init__(self, file_object: BinaryIO):
    # Required to fix CLIF "Value invalidated due to capture by std::unique_ptr"
    super().__init__()
    self._file_object = file_object

  def write(self, data: bytes) -> int:
    """Writes to underlying file object and returns number of bytes written."""
    try:
      written = self._file_object.write(data)
      if written is None:
        return 0
      if written < 0 or written > len(data):
        raise ValueError('invalid value returned by write')
      return written
    except io.BlockingIOError as e:
      if e.characters_written is None:
        return 0
      if e.characters_written < 0 or e.characters_written > len(data):
        raise ValueError('invalid characters_written') from e
      return e.characters_written

  def close(self) -> None:
    self._file_object.close()

  def read(self, size: int) -> bytes:
    """Reads at most 'size' bytes from the underlying file object.

    Args:
      size: A non-negative integer, maximum number of bytes to read.

    Returns:
      Bytes that were read. An empty bytes object is returned if no bytes are
      available at the moment.

    Raises:
      EOFError if the file object is already at EOF.
    """
    if size < 0:
      raise ValueError('size must be non-negative')

    try:
      data = self._file_object.read(size)
      if data is None:
        return b''
      elif not data and size > 0:
        raise EOFError('EOF')
      return data
    except io.BlockingIOError:
      return b''
