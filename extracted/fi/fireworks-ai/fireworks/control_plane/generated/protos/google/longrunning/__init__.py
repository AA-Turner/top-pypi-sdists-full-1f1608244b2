# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: google/longrunning/operations.proto
# plugin: python-betterproto
# This file has been @generated

__all__ = (
    "Operation",
    "GetOperationRequest",
)


from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Operation(betterproto.Message):
    """
    This resource represents a long-running operation that is the result of a
    network API call.
    """

    name: str = betterproto.string_field(1)
    """
    The server-assigned name, which is only unique within the same service that
    originally returns it. If you use the default HTTP mapping, the
    `name` should be a resource name ending with `operations/{unique_id}`.
    """

    metadata: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    """
    Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.
    """

    done: bool = betterproto.bool_field(3)
    """
    If the value is `false`, it means the operation is still in progress.
    If `true`, the operation is completed, and either `error` or `response` is
    available.
    """

    error: "_rpc__.Status" = betterproto.message_field(4, group="result")
    """
    The error result of the operation in case of failure or cancellation.
    """

    response: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        5, group="result"
    )
    """
    The normal, successful response of the operation. If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx`
    is the original method name. For example, if the original method name
    is `TakeSnapshot()`, the inferred response type is
    `TakeSnapshotResponse`.
    """


@dataclass(eq=False, repr=False)
class GetOperationRequest(betterproto.Message):
    """The request message for GetOperation."""

    name: str = betterproto.string_field(1)
    """The name of the operation resource."""


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from .. import rpc as _rpc__
