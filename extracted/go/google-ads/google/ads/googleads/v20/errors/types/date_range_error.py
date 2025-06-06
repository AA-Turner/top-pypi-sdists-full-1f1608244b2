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
    package="google.ads.googleads.v20.errors",
    marshal="google.ads.googleads.v20",
    manifest={
        "DateRangeErrorEnum",
    },
)


class DateRangeErrorEnum(proto.Message):
    r"""Container for enum describing possible date range errors."""

    class DateRangeError(proto.Enum):
        r"""Enum describing possible date range errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            INVALID_DATE (2):
                Invalid date.
            START_DATE_AFTER_END_DATE (3):
                The start date was after the end date.
            CANNOT_SET_DATE_TO_PAST (4):
                Cannot set date to past time
            AFTER_MAXIMUM_ALLOWABLE_DATE (5):
                A date was used that is past the system
                "last" date.
            CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED (6):
                Trying to change start date on a resource
                that has started.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_DATE = 2
        START_DATE_AFTER_END_DATE = 3
        CANNOT_SET_DATE_TO_PAST = 4
        AFTER_MAXIMUM_ALLOWABLE_DATE = 5
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
