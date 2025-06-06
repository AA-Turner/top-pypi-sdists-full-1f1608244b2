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

"""Beans leaf dataset with images of diseased and health leaves."""

import os

import tensorflow_datasets.public_api as tfds

_TRAIN_URL = "https://storage.googleapis.com/ibeans/train.zip"
_VALIDATION_URL = "https://storage.googleapis.com/ibeans/validation.zip"
_TEST_URL = "https://storage.googleapis.com/ibeans/test.zip"

_IMAGE_SIZE = 500
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)

_LABELS = ["angular_leaf_spot", "bean_rust", "healthy"]


class Builder(tfds.core.GeneratorBasedBuilder):
  """Beans plant leaf images dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names=_LABELS),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/AI-Lab-Makerere/ibean/",
    )

  def _split_generators(self, dl_manager):
    train_path, val_path, test_path = dl_manager.download(
        [_TRAIN_URL, _VALIDATION_URL, _TEST_URL]
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"archive": dl_manager.iter_archive(train_path)},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"archive": dl_manager.iter_archive(val_path)},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"archive": dl_manager.iter_archive(test_path)},
        ),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    for fname, fobj in archive:
      if not fname.endswith(".jpg"):
        continue
      label = fname.split(os.path.sep)[-2]
      record = {
          "image": fobj,
          "label": label,
      }
      yield fname, record
