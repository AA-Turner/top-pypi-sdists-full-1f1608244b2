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
    package="google.ads.googleads.v20.common",
    marshal="google.ads.googleads.v20",
    manifest={
        "ClickLocation",
    },
)


class ClickLocation(proto.Message):
    r"""Location criteria associated with a click.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        city (str):
            The city location criterion associated with
            the impression.

            This field is a member of `oneof`_ ``_city``.
        country (str):
            The country location criterion associated
            with the impression.

            This field is a member of `oneof`_ ``_country``.
        metro (str):
            The metro location criterion associated with
            the impression.

            This field is a member of `oneof`_ ``_metro``.
        most_specific (str):
            The most specific location criterion
            associated with the impression.

            This field is a member of `oneof`_ ``_most_specific``.
        region (str):
            The region location criterion associated with
            the impression.

            This field is a member of `oneof`_ ``_region``.
    """

    city: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    country: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    metro: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    most_specific: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    region: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
