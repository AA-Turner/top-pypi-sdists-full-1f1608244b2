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
        "PlacementTypeEnum",
    },
)


class PlacementTypeEnum(proto.Message):
    r"""Container for enum describing possible placement types."""

    class PlacementType(proto.Enum):
        r"""Possible placement types for a feed mapping.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            WEBSITE (2):
                Websites(for example,
                'www.flowers4sale.com').
            MOBILE_APP_CATEGORY (3):
                Mobile application categories(for example,
                'Games').
            MOBILE_APPLICATION (4):
                mobile applications(for example,
                'mobileapp::2-com.whatsthewordanswers').
            YOUTUBE_VIDEO (5):
                YouTube videos(for example,
                'youtube.com/video/wtLJPvx7-ys').
            YOUTUBE_CHANNEL (6):
                YouTube channels(for example,
                'youtube.com::L8ZULXASCc1I_oaOT0NaOQ').
            GOOGLE_PRODUCTS (7):
                Surfaces owned and operated by Google(for
                example, 'tv.google.com').
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBSITE = 2
        MOBILE_APP_CATEGORY = 3
        MOBILE_APPLICATION = 4
        YOUTUBE_VIDEO = 5
        YOUTUBE_CHANNEL = 6
        GOOGLE_PRODUCTS = 7


__all__ = tuple(sorted(__protobuf__.manifest))
