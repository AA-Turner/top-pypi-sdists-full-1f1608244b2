#
# Copyright 2023 Splunk Inc.
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
#
from abc import abstractmethod


class Collection:
    """
    A Collection metaclass that specifies what functions a collection in the
    Splunk SPL Wrapper framework must implement.
    """

    def __call__(self):
        return list(self.items())

    def __len__(self):
        return len(list(self.items()))

    def __iter__(self):
        yield from list(self.items())

    @abstractmethod
    def items(self):
        """
        Return a collection of all the contained objects. It is up to the
        subclass to decide whether this collection is a list, map or of any
        other kind.

        @return: A collection of all the items contained.
        """
        pass

    @abstractmethod
    def __contains__(self, item):
        """
        Return boolean whether item is contained in Collection.

        @param item: The item which is checked if contained.
        """
        pass
