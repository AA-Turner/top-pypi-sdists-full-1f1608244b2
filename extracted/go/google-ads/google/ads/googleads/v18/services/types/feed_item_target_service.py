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

from google.ads.googleads.v18.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v18.resources.types import (
    feed_item_target as gagr_feed_item_target,
)
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v18.services",
    marshal="google.ads.googleads.v18",
    manifest={
        "MutateFeedItemTargetsRequest",
        "FeedItemTargetOperation",
        "MutateFeedItemTargetsResponse",
        "MutateFeedItemTargetResult",
    },
)


class MutateFeedItemTargetsRequest(proto.Message):
    r"""Request message for
    [FeedItemTargetService.MutateFeedItemTargets][google.ads.googleads.v18.services.FeedItemTargetService.MutateFeedItemTargets].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose feed
            item targets are being modified.
        operations (MutableSequence[google.ads.googleads.v18.services.types.FeedItemTargetOperation]):
            Required. The list of operations to perform
            on individual feed item targets.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        response_content_type (google.ads.googleads.v18.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operations: MutableSequence["FeedItemTargetOperation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="FeedItemTargetOperation",
        )
    )
    partial_failure: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    response_content_type: (
        gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    ) = proto.Field(
        proto.ENUM,
        number=5,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class FeedItemTargetOperation(proto.Message):
    r"""A single operation (create, remove) on an feed item target.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create (google.ads.googleads.v18.resources.types.FeedItemTarget):
            Create operation: No resource name is
            expected for the new feed item target.

            This field is a member of `oneof`_ ``operation``.
        remove (str):
            Remove operation: A resource name for the removed feed item
            target is expected, in this format:

            ``customers/{customer_id}/feedItemTargets/{feed_id}~{feed_item_id}~{feed_item_target_type}~{feed_item_target_id}``

            This field is a member of `oneof`_ ``operation``.
    """

    create: gagr_feed_item_target.FeedItemTarget = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_feed_item_target.FeedItemTarget,
    )
    remove: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="operation",
    )


class MutateFeedItemTargetsResponse(proto.Message):
    r"""Response message for an feed item target mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (for example, auth errors), we return
            an RPC level error.
        results (MutableSequence[google.ads.googleads.v18.services.types.MutateFeedItemTargetResult]):
            All results for the mutate.
    """

    partial_failure_error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    results: MutableSequence["MutateFeedItemTargetResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="MutateFeedItemTargetResult",
        )
    )


class MutateFeedItemTargetResult(proto.Message):
    r"""The result for the feed item target mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
        feed_item_target (google.ads.googleads.v18.resources.types.FeedItemTarget):
            The mutated feed item target with only mutable fields after
            mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feed_item_target: gagr_feed_item_target.FeedItemTarget = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_feed_item_target.FeedItemTarget,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
