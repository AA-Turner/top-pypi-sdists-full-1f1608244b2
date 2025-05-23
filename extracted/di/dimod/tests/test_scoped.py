# Copyright 2025 D-Wave
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unittest import mock

import dimod


class TestScopedClass(unittest.TestCase):
    def test_instantiation_base_class(self):
        with self.assertRaises(TypeError):
            dimod.Scoped()

    def test_context(self):
        class ScopedResource(dimod.Scoped):
            def close(self):
                pass

        with mock.patch.object(ScopedResource, 'close'):
            with ScopedResource() as scoped:
                pass

            scoped.close.assert_called_once()
