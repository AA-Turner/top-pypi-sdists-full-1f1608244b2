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
        "LanguageCodeErrorEnum",
    },
)


class LanguageCodeErrorEnum(proto.Message):
    r"""Container for enum describing language code errors."""

    class LanguageCodeError(proto.Enum):
        r"""Enum describing language code errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            LANGUAGE_CODE_NOT_FOUND (2):
                The input language code is not recognized.
            INVALID_LANGUAGE_CODE (3):
                The language code is not supported.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        LANGUAGE_CODE_NOT_FOUND = 2
        INVALID_LANGUAGE_CODE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
