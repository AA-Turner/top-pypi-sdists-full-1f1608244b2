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
        "UserListLogicalRuleOperatorEnum",
    },
)


class UserListLogicalRuleOperatorEnum(proto.Message):
    r"""The logical operator of the rule."""

    class UserListLogicalRuleOperator(proto.Enum):
        r"""Enum describing possible user list logical rule operators.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            ALL (2):
                And - all of the operands.
            ANY (3):
                Or - at least one of the operands.
            NONE (4):
                Not - none of the operands.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL = 2
        ANY = 3
        NONE = 4


__all__ = tuple(sorted(__protobuf__.manifest))
