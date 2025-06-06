# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v18.errors",
    marshal="google.ads.googleads.v18",
    manifest={
        "FeedAttributeReferenceErrorEnum",
    },
)


class FeedAttributeReferenceErrorEnum(proto.Message):
    r"""Container for enum describing possible feed attribute
    reference errors.

    """

    class FeedAttributeReferenceError(proto.Enum):
        r"""Enum describing possible feed attribute reference errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            CANNOT_REFERENCE_REMOVED_FEED (2):
                A feed referenced by ID has been removed.
            INVALID_FEED_NAME (3):
                There is no enabled feed with the given name.
            INVALID_FEED_ATTRIBUTE_NAME (4):
                There is no feed attribute in an enabled feed
                with the given name.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_REFERENCE_REMOVED_FEED = 2
        INVALID_FEED_NAME = 3
        INVALID_FEED_ATTRIBUTE_NAME = 4


__all__ = tuple(sorted(__protobuf__.manifest))
