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

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v20.resources.types import keyword_theme_constant


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.services",
    marshal="google.ads.googleads.v20",
    manifest={
        "SuggestKeywordThemeConstantsRequest",
        "SuggestKeywordThemeConstantsResponse",
    },
)


class SuggestKeywordThemeConstantsRequest(proto.Message):
    r"""Request message for
    [KeywordThemeConstantService.SuggestKeywordThemeConstants][google.ads.googleads.v20.services.KeywordThemeConstantService.SuggestKeywordThemeConstants].

    Attributes:
        query_text (str):
            The query text of a keyword theme that will
            be used to map to similar keyword themes. For
            example, "plumber" or "roofer".
        country_code (str):
            Upper-case, two-letter country code as
            defined by ISO-3166. This for refining the scope
            of the query, default to 'US' if not set.
        language_code (str):
            The two letter language code for get
            corresponding keyword theme for refining the
            scope of the query, default to 'en' if not set.
    """

    query_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SuggestKeywordThemeConstantsResponse(proto.Message):
    r"""Response message for
    [KeywordThemeConstantService.SuggestKeywordThemeConstants][google.ads.googleads.v20.services.KeywordThemeConstantService.SuggestKeywordThemeConstants].

    Attributes:
        keyword_theme_constants (MutableSequence[google.ads.googleads.v20.resources.types.KeywordThemeConstant]):
            Smart Campaign keyword theme suggestions.
    """

    keyword_theme_constants: MutableSequence[
        keyword_theme_constant.KeywordThemeConstant
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=keyword_theme_constant.KeywordThemeConstant,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
