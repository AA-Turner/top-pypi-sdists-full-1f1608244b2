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

"""Annotated Enron Subject Line Corpus Dataset."""

import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://github.com/ryanzhumich/AESLC/archive/master.zip"

_DOCUMENT = "email_body"
_SUMMARY = "subject_line"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Annotated Enron Subject Line Corpus Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {_DOCUMENT: tfds.features.Text(), _SUMMARY: tfds.features.Text()}
        ),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/ryanzhumich/AESLC",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    input_path = os.path.join(dl_path, "AESLC-master", "enron_subject_line")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "pattern": os.path.join(input_path, "train", "*.subject")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "pattern": os.path.join(input_path, "dev", "*.subject")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "pattern": os.path.join(input_path, "test", "*.subject")
            },
        ),
    ]

  def _generate_examples(self, pattern=None):
    """Yields examples."""
    for filename in tf.io.gfile.glob(pattern):
      email_body, subject_line = _parse_email_file(filename)
      key = os.path.basename(filename).rstrip(".subject")
      yield key, {_DOCUMENT: email_body, _SUMMARY: subject_line}


def _parse_email_file(filename):
  """Parse email file text for email body and subject."""
  with epath.Path(filename).open() as f:
    email_body = ""
    for line in f:
      if line == "\n":
        break
      email_body += line
    line = next(f)
    subject = ""
    for line in f:
      if line == "\n":
        break
      subject += line
  return email_body, subject
