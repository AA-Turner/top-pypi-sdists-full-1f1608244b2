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

"""Historical phenological data for cherry tree flowering at Kyoto City."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.cherry_blossoms import cherry_blossoms


class CherryBlossomsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for cherry_blossoms dataset."""

  DATASET_CLASS = cherry_blossoms.CherryBlossoms
  SPLITS = {'train': 4}

  DL_EXTRACT_RESULT = 'cherry_blossoms.csv'


if __name__ == '__main__':
  tfds.testing.test_main()
