# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
    package="google.ads.googleads.v20.enums",
    marshal="google.ads.googleads.v20",
    manifest={
        "CriterionSystemServingStatusEnum",
    },
)


class CriterionSystemServingStatusEnum(proto.Message):
    r"""Container for enum describing possible criterion system
    serving statuses.

    """

    class CriterionSystemServingStatus(proto.Enum):
        r"""Enumerates criterion system serving statuses.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                The value is unknown in this version.
            ELIGIBLE (2):
                Eligible.
            RARELY_SERVED (3):
                Low search volume.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        RARELY_SERVED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
