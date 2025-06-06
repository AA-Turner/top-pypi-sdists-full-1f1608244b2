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
        "AdCustomizerErrorEnum",
    },
)


class AdCustomizerErrorEnum(proto.Message):
    r"""Container for enum describing possible ad customizer errors."""

    class AdCustomizerError(proto.Enum):
        r"""Enum describing possible ad customizer errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            COUNTDOWN_INVALID_DATE_FORMAT (2):
                Invalid date argument in countdown function.
            COUNTDOWN_DATE_IN_PAST (3):
                Countdown end date is in the past.
            COUNTDOWN_INVALID_LOCALE (4):
                Invalid locale string in countdown function.
            COUNTDOWN_INVALID_START_DAYS_BEFORE (5):
                Days-before argument to countdown function is
                not positive.
            UNKNOWN_USER_LIST (6):
                A user list referenced in an IF function does
                not exist.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        COUNTDOWN_INVALID_DATE_FORMAT = 2
        COUNTDOWN_DATE_IN_PAST = 3
        COUNTDOWN_INVALID_LOCALE = 4
        COUNTDOWN_INVALID_START_DAYS_BEFORE = 5
        UNKNOWN_USER_LIST = 6


__all__ = tuple(sorted(__protobuf__.manifest))
