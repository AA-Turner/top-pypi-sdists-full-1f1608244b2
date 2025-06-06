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

"""Dataset definition for pg19.

DEPRECATED!
If you want to use the Pg19 dataset builder class, use:
tfds.builder_cls('pg19')
"""

from tensorflow_datasets.core import lazy_builder_import

Pg19 = lazy_builder_import.LazyBuilderImport('pg19')
