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
        "ThirdPartyAppAnalyticsLinkErrorEnum",
    },
)


class ThirdPartyAppAnalyticsLinkErrorEnum(proto.Message):
    r"""Container for enum describing possible third party app
    analytics link errors.

    """

    class ThirdPartyAppAnalyticsLinkError(proto.Enum):
        r"""Enum describing possible third party app analytics link
        errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            INVALID_ANALYTICS_PROVIDER_ID (2):
                The provided analytics provider ID is
                invalid.
            INVALID_MOBILE_APP_ID (3):
                The provided mobile app ID is invalid.
            MOBILE_APP_IS_NOT_ENABLED (4):
                The mobile app corresponding to the provided
                app ID is not active/enabled.
            CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK (5):
                Regenerating shareable link ID is only
                allowed on active links
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_ANALYTICS_PROVIDER_ID = 2
        INVALID_MOBILE_APP_ID = 3
        MOBILE_APP_IS_NOT_ENABLED = 4
        CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK = 5


__all__ = tuple(sorted(__protobuf__.manifest))
