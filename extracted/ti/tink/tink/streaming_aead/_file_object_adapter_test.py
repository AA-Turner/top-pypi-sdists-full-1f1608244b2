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
"""Tests for tink.python.tink.util._file_object_adapter."""

import io

from absl.testing import absltest
from absl.testing.absltest import mock

from tink.streaming_aead import _file_object_adapter


class FileObjectAdapterTest(absltest.TestCase):

  def test_basic_write(self):
    file_object = io.BytesIO()
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(9, adapter.write(b'something'))
    self.assertEqual(b'something', file_object.getvalue())
    adapter.close()

  def test_multiple_write(self):
    file_object = io.BytesIO()
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(9, adapter.write(b'something'))
    self.assertEqual(3, adapter.write(b'123'))
    self.assertEqual(3, adapter.write(b'456'))
    self.assertEqual(b'something123456', file_object.getvalue())

  def test_write_after_close(self):
    file_object = io.BytesIO()
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    adapter.close()
    with self.assertRaises(ValueError):
      adapter.write(b'something')

  def test_write_returns_none_written_is_zero(self):
    file_object = mock.Mock()
    file_object.write = mock.Mock(return_value=None)
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(0, adapter.write(b''))

  def test_write_returns_negative_number_raises_error(self):
    file_object = mock.Mock()
    file_object.write = mock.Mock(return_value=-1)
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    with self.assertRaises(ValueError):
      adapter.write(b'something')

  def test_write_returns_too_large_number_raises_error(self):
    data = b'something'
    file_object = mock.Mock()
    file_object.write = mock.Mock(return_value=len(data) + 1)
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    with self.assertRaises(ValueError):
      adapter.write(b'something')

  def test_write_raises_blocking_error_returns_characters_written_success(self):
    file_object = mock.Mock()
    file_object.write = mock.Mock(side_effect=io.BlockingIOError(None, None, 5))
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(5, adapter.write(b'something'))

  def test_write_raises_invalid_blocking_error_raises_error(self):
    file_object = mock.Mock()
    file_object.write = mock.Mock(
        side_effect=io.BlockingIOError(None, None, 42)
    )
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    with self.assertRaises(ValueError):
      adapter.write(b'something')

  def test_partial_write(self):
    file_object = mock.Mock()
    file_object.write = mock.Mock(wraps=lambda data: len(data) - 1)
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(8, adapter.write(b'something'))

  def test_basic_read(self):
    file_object = io.BytesIO(b'something')
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(adapter.read(9), b'something')

  def test_multiple_read(self):
    file_object = io.BytesIO(b'something')
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(adapter.read(3), b'som')
    self.assertEqual(adapter.read(3), b'eth')
    self.assertEqual(adapter.read(3), b'ing')

  def test_read_returns_none(self):
    file_object = mock.Mock()
    file_object.read = mock.Mock(return_value=None)
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(adapter.read(10), b'')

  def test_read_eof(self):
    file_object = mock.Mock()
    file_object.read = mock.Mock(return_value=b'')
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    with self.assertRaises(EOFError):
      adapter.read(10)

  def test_read_size_0(self):
    file_object = io.BytesIO(b'something')
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(adapter.read(0), b'')

  def test_read_negative_size_fails(self):
    file_object = io.BytesIO(b'something')
    adapter = _file_object_adapter.FileObjectAdapter(file_object)
    with self.assertRaises(ValueError):
      adapter.read(-1)

  def test_read_raises_blocking_error(self):
    file_object = mock.Mock()
    file_object.read = mock.Mock(side_effect=io.BlockingIOError(None, None))
    adapter = _file_object_adapter.FileObjectAdapter(file_object)

    self.assertEqual(adapter.read(10), b'')


if __name__ == '__main__':
  absltest.main()
