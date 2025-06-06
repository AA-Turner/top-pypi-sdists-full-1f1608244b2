# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module to use to extract archives. No business logic."""

import bz2
import concurrent.futures
import contextlib
import gzip
import multiprocessing
import os
import tarfile
import typing
from typing import Iterator, Tuple, Union
import uuid
import zipfile

from absl import logging
from etils import epath
import promise
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


@utils.memoize()
def get_extractor(*args, **kwargs):
  return _Extractor(*args, **kwargs)


class ExtractError(Exception):
  """There was an error while extracting the archive."""


class UnsafeArchiveError(Exception):
  """The archive is unsafe to unpack, e.g. absolute path."""


class _Extractor(object):
  """Singleton (use `get_extractor()` module fct) to extract archives."""

  def __init__(self, max_workers=None):
    max_workers = max_workers or multiprocessing.cpu_count()
    self._executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers * 4
    )
    self._pbar_path = None

  @contextlib.contextmanager
  def tqdm(self):
    """Add a progression bar for the current extraction."""
    with utils.async_tqdm(
        total=0, desc='Extraction completed...', unit=' file', mininterval=1.0
    ) as pbar_path:
      self._pbar_path = pbar_path
      yield

  def extract(
      self,
      path: epath.PathLike,
      extract_method: resource_lib.ExtractMethod,
      to_path: epath.PathLike,
  ) -> promise.Promise:
    """Returns `promise.Promise` => to_path."""
    path = epath.Path(path)
    to_path = epath.Path(to_path)
    if extract_method not in _EXTRACT_METHODS:
      raise ValueError('Unknown extraction method "%s".' % extract_method)
    future = self._executor.submit(
        self._extract, from_path=path, method=extract_method, to_path=to_path
    )
    return promise.Promise.resolve(future)

  def _extract(
      self,
      from_path: epath.Path,
      method: resource_lib.ExtractMethod,
      to_path: epath.Path,
  ) -> epath.Path:
    """Returns `to_path` once resource has been extracted there."""
    tmp_file_name = '%s%s_%s' % (
        constants.INCOMPLETE_PREFIX,
        uuid.uuid4().hex,
        to_path.name,
    )
    to_path_tmp = os.fspath(to_path.parent / tmp_file_name)
    max_length_dst_path = 0
    futures = []
    if self._pbar_path is None:
      raise ValueError("'_pbar_path' is not initialized")
    try:
      for path, handle in iter_archive(from_path, method):
        path = tf.compat.as_text(path)
        dst_path = path and os.path.join(to_path_tmp, path) or to_path_tmp
        max_length_dst_path = max(max_length_dst_path, len(dst_path))
        file_utils.makedirs_cached(os.path.dirname(dst_path))
        future = self._executor.submit(_copy, handle.read(), dst_path)
        futures.append(future)
        self._pbar_path.update_total(1)

      # Wait until all copies have completed.
      for future in concurrent.futures.as_completed(futures):
        future.result()
        self._pbar_path.update(1)
    except BaseException as err:
      msg = f'Error while extracting {from_path} to {to_path}: {err}'
      # Check if running on windows
      if os.name == 'nt' and max_length_dst_path > 250:
        msg += (
            '\nOn windows, path lengths greater than 260 characters may result'
            ' in an error. See the doc to remove the limitation: '
            'https://docs.python.org/3/using/windows.html#removing-the-max-path-limitation'
        )
      raise ExtractError(msg) from err

    # `tf.io.gfile.Rename(overwrite=True)` doesn't work for non empty
    # directories, so delete destination first, if it already exists.
    to_path = epath.Path(to_path)
    if to_path.exists():
      # `rename` is atomic, but not `rmtree`.
      # When 2 builder scripts (for each config) extract the same file, one can
      # `rename` while the other is still running `rmtree`, leading to corrupted
      # archive dir.
      path_to_delete = epath.Path(to_path_tmp + '.todelete')
      to_path.rename(path_to_delete)
      path_to_delete.rmtree()
    epath.Path(to_path_tmp).rename(to_path)
    return to_path


def _copy(src_data, dest_path):
  """Copy data read from src data to new file in dest_path."""
  with tf.io.gfile.GFile(dest_path, 'wb') as dest_file:
    dest_file.write(src_data)


def _normpath(path):
  path = os.path.normpath(path)
  if (
      path.startswith('.')
      or os.path.isabs(path)
      or path.endswith('~')
      or os.path.basename(path).startswith('.')
  ):
    return None
  return path


@contextlib.contextmanager
def _open_or_pass(path_or_fobj):
  if isinstance(path_or_fobj, epath.PathLikeCls):
    with tf.io.gfile.GFile(path_or_fobj, 'rb') as f_obj:
      yield f_obj
  else:
    yield path_or_fobj


def iter_tar(arch_f, stream=False):
  """Iter over tar archive, yielding (path, object-like) tuples.

  Args:
    arch_f: File object of the archive to iterate.
    stream: If True, open the archive in stream mode which allows for faster
      processing and less temporary disk consumption, but random access to the
      file is not allowed.

  Yields:
    (filepath, extracted_fobj) for each file in the archive.
  """
  read_type = 'r' + ('|' if stream else ':') + '*'

  with _open_or_pass(arch_f) as fobj:
    tar = tarfile.open(mode=read_type, fileobj=fobj)
    for member in tar:
      if stream and (member.islnk() or member.issym()):
        # Links cannot be dereferenced in stream mode.
        logging.warning('Skipping link during extraction: %s', member.name)
        continue

      try:
        extract_file = tar.extractfile(member)
      except KeyError:
        if not (member.islnk() or member.issym()):
          raise  # Forward exception non-link files which couldn't be extracted
        # The link could not be extracted, which likely indicates a corrupted
        # archive.
        logging.warning(
            'Skipping extraction of invalid link: %s -> %s',
            member.name,
            member.linkname,
        )
        continue

      if extract_file:  # File with data (not directory):
        path = _normpath(member.path)  # pytype: disable=attribute-error
        if not path:
          continue
        yield (path, extract_file)


def iter_tar_stream(arch_f):
  return iter_tar(arch_f, stream=True)


def iter_gzip(arch_f):
  with _open_or_pass(arch_f) as fobj:
    gzip_ = gzip.GzipFile(fileobj=fobj)
    yield ('', gzip_)  # No inner file.


def iter_bzip2(arch_f):
  with _open_or_pass(arch_f) as fobj:
    bz2_ = bz2.BZ2File(filename=fobj)
    yield ('', bz2_)  # No inner file.


def iter_zip(arch_f):
  """Iterate over zip archive."""
  with _open_or_pass(arch_f) as fobj:
    z = zipfile.ZipFile(fobj)
    for member in z.infolist():
      if member.is_dir():  # Filter directories  # pytype: disable=attribute-error
        continue
      extract_file = z.open(member)
      path = _normpath(member.filename)
      if not path:
        continue
      yield (path, extract_file)


_EXTRACT_METHODS = {
    resource_lib.ExtractMethod.BZIP2: iter_bzip2,
    resource_lib.ExtractMethod.GZIP: iter_gzip,
    resource_lib.ExtractMethod.TAR: iter_tar,
    resource_lib.ExtractMethod.TAR_GZ: iter_tar,
    resource_lib.ExtractMethod.TAR_GZ_STREAM: iter_tar_stream,
    resource_lib.ExtractMethod.TAR_STREAM: iter_tar_stream,
    resource_lib.ExtractMethod.ZIP: iter_zip,
}


def iter_archive(
    path: Union[epath.PathLike, typing.BinaryIO],
    method: resource_lib.ExtractMethod,
) -> Iterator[Tuple[str, typing.BinaryIO]]:
  """Iterate over an archive.

  Args:
    path: `str`, archive path
    method: `tfds.download.ExtractMethod`, extraction method

  Returns:
    An iterator of `(path_in_archive, f_obj)`
  """
  if method == resource_lib.ExtractMethod.NO_EXTRACT:
    raise ValueError(
        f'Cannot `iter_archive` over {path}. Invalid or unrecognised archive.'
    )
  return _EXTRACT_METHODS[method](path)  # pytype: disable=bad-return-type
