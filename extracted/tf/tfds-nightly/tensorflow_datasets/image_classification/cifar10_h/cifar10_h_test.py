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

"""cifar10_h dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification.cifar10_h import cifar10_h


class Cifar10HTest(testing.DatasetBuilderTestCase):
  """Tests for cifar10_n dataset."""

  DATASET_CLASS = cifar10_h.Cifar10H
  SPLITS = {
      'train': 10,  # Number of fake train example
      'test': 2,  # Number of fake test example
  }


if __name__ == '__main__':
  testing.test_main()
