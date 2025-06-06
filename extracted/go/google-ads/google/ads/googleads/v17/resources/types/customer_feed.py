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

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v17.common.types import (
    matching_function as gagc_matching_function,
)
from google.ads.googleads.v17.enums.types import feed_link_status
from google.ads.googleads.v17.enums.types import placeholder_type


__protobuf__ = proto.module(
    package="google.ads.googleads.v17.resources",
    marshal="google.ads.googleads.v17",
    manifest={
        "CustomerFeed",
    },
)


class CustomerFeed(proto.Message):
    r"""A customer feed.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Immutable. The resource name of the customer feed. Customer
            feed resource names have the form:

            ``customers/{customer_id}/customerFeeds/{feed_id}``
        feed (str):
            Immutable. The feed being linked to the
            customer.

            This field is a member of `oneof`_ ``_feed``.
        placeholder_types (MutableSequence[google.ads.googleads.v17.enums.types.PlaceholderTypeEnum.PlaceholderType]):
            Indicates which placeholder types the feed
            may populate under the connected customer.
            Required.
        matching_function (google.ads.googleads.v17.common.types.MatchingFunction):
            Matching function associated with the
            CustomerFeed. The matching function is used to
            filter the set of feed items selected. Required.
        status (google.ads.googleads.v17.enums.types.FeedLinkStatusEnum.FeedLinkStatus):
            Output only. Status of the customer feed.
            This field is read-only.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feed: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    placeholder_types: MutableSequence[
        placeholder_type.PlaceholderTypeEnum.PlaceholderType
    ] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=placeholder_type.PlaceholderTypeEnum.PlaceholderType,
    )
    matching_function: gagc_matching_function.MatchingFunction = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gagc_matching_function.MatchingFunction,
    )
    status: feed_link_status.FeedLinkStatusEnum.FeedLinkStatus = proto.Field(
        proto.ENUM,
        number=5,
        enum=feed_link_status.FeedLinkStatusEnum.FeedLinkStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
