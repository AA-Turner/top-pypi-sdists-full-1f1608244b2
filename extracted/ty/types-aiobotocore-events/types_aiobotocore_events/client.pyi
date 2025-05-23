"""
Type annotations for events service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_events.client import EventBridgeClient

    session = get_session()
    async with session.create_client("events") as client:
        client: EventBridgeClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListRuleNamesByTargetPaginator,
    ListRulesPaginator,
    ListTargetsByRulePaginator,
)
from .type_defs import (
    ActivateEventSourceRequestTypeDef,
    CancelReplayRequestTypeDef,
    CancelReplayResponseTypeDef,
    CreateApiDestinationRequestTypeDef,
    CreateApiDestinationResponseTypeDef,
    CreateArchiveRequestTypeDef,
    CreateArchiveResponseTypeDef,
    CreateConnectionRequestTypeDef,
    CreateConnectionResponseTypeDef,
    CreateEndpointRequestTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventBusRequestTypeDef,
    CreateEventBusResponseTypeDef,
    CreatePartnerEventSourceRequestTypeDef,
    CreatePartnerEventSourceResponseTypeDef,
    DeactivateEventSourceRequestTypeDef,
    DeauthorizeConnectionRequestTypeDef,
    DeauthorizeConnectionResponseTypeDef,
    DeleteApiDestinationRequestTypeDef,
    DeleteArchiveRequestTypeDef,
    DeleteConnectionRequestTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteEndpointRequestTypeDef,
    DeleteEventBusRequestTypeDef,
    DeletePartnerEventSourceRequestTypeDef,
    DeleteRuleRequestTypeDef,
    DescribeApiDestinationRequestTypeDef,
    DescribeApiDestinationResponseTypeDef,
    DescribeArchiveRequestTypeDef,
    DescribeArchiveResponseTypeDef,
    DescribeConnectionRequestTypeDef,
    DescribeConnectionResponseTypeDef,
    DescribeEndpointRequestTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEventBusRequestTypeDef,
    DescribeEventBusResponseTypeDef,
    DescribeEventSourceRequestTypeDef,
    DescribeEventSourceResponseTypeDef,
    DescribePartnerEventSourceRequestTypeDef,
    DescribePartnerEventSourceResponseTypeDef,
    DescribeReplayRequestTypeDef,
    DescribeReplayResponseTypeDef,
    DescribeRuleRequestTypeDef,
    DescribeRuleResponseTypeDef,
    DisableRuleRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableRuleRequestTypeDef,
    ListApiDestinationsRequestTypeDef,
    ListApiDestinationsResponseTypeDef,
    ListArchivesRequestTypeDef,
    ListArchivesResponseTypeDef,
    ListConnectionsRequestTypeDef,
    ListConnectionsResponseTypeDef,
    ListEndpointsRequestTypeDef,
    ListEndpointsResponseTypeDef,
    ListEventBusesRequestTypeDef,
    ListEventBusesResponseTypeDef,
    ListEventSourcesRequestTypeDef,
    ListEventSourcesResponseTypeDef,
    ListPartnerEventSourceAccountsRequestTypeDef,
    ListPartnerEventSourceAccountsResponseTypeDef,
    ListPartnerEventSourcesRequestTypeDef,
    ListPartnerEventSourcesResponseTypeDef,
    ListReplaysRequestTypeDef,
    ListReplaysResponseTypeDef,
    ListRuleNamesByTargetRequestTypeDef,
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesRequestTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsByRuleRequestTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PutEventsRequestTypeDef,
    PutEventsResponseTypeDef,
    PutPartnerEventsRequestTypeDef,
    PutPartnerEventsResponseTypeDef,
    PutPermissionRequestTypeDef,
    PutRuleRequestTypeDef,
    PutRuleResponseTypeDef,
    PutTargetsRequestTypeDef,
    PutTargetsResponseTypeDef,
    RemovePermissionRequestTypeDef,
    RemoveTargetsRequestTypeDef,
    RemoveTargetsResponseTypeDef,
    StartReplayRequestTypeDef,
    StartReplayResponseTypeDef,
    TagResourceRequestTypeDef,
    TestEventPatternRequestTypeDef,
    TestEventPatternResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApiDestinationRequestTypeDef,
    UpdateApiDestinationResponseTypeDef,
    UpdateArchiveRequestTypeDef,
    UpdateArchiveResponseTypeDef,
    UpdateConnectionRequestTypeDef,
    UpdateConnectionResponseTypeDef,
    UpdateEndpointRequestTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateEventBusRequestTypeDef,
    UpdateEventBusResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack

__all__ = ("EventBridgeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    IllegalStatusException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidEventPatternException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ManagedRuleException: Type[BotocoreClientError]
    OperationDisabledException: Type[BotocoreClientError]
    PolicyLengthExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class EventBridgeClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EventBridgeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#generate_presigned_url)
        """

    async def activate_event_source(
        self, **kwargs: Unpack[ActivateEventSourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Activates a partner event source that has been deactivated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/activate_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#activate_event_source)
        """

    async def cancel_replay(
        self, **kwargs: Unpack[CancelReplayRequestTypeDef]
    ) -> CancelReplayResponseTypeDef:
        """
        Cancels the specified replay.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/cancel_replay.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#cancel_replay)
        """

    async def create_api_destination(
        self, **kwargs: Unpack[CreateApiDestinationRequestTypeDef]
    ) -> CreateApiDestinationResponseTypeDef:
        """
        Creates an API destination, which is an HTTP invocation endpoint configured as
        a target for events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_api_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_api_destination)
        """

    async def create_archive(
        self, **kwargs: Unpack[CreateArchiveRequestTypeDef]
    ) -> CreateArchiveResponseTypeDef:
        """
        Creates an archive of events with the specified settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_archive)
        """

    async def create_connection(
        self, **kwargs: Unpack[CreateConnectionRequestTypeDef]
    ) -> CreateConnectionResponseTypeDef:
        """
        Creates a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_connection)
        """

    async def create_endpoint(
        self, **kwargs: Unpack[CreateEndpointRequestTypeDef]
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates a global endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_endpoint)
        """

    async def create_event_bus(
        self, **kwargs: Unpack[CreateEventBusRequestTypeDef]
    ) -> CreateEventBusResponseTypeDef:
        """
        Creates a new event bus within your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_event_bus.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_event_bus)
        """

    async def create_partner_event_source(
        self, **kwargs: Unpack[CreatePartnerEventSourceRequestTypeDef]
    ) -> CreatePartnerEventSourceResponseTypeDef:
        """
        Called by an SaaS partner to create a partner event source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/create_partner_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#create_partner_event_source)
        """

    async def deactivate_event_source(
        self, **kwargs: Unpack[DeactivateEventSourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        You can use this operation to temporarily stop receiving events from the
        specified partner event source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/deactivate_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#deactivate_event_source)
        """

    async def deauthorize_connection(
        self, **kwargs: Unpack[DeauthorizeConnectionRequestTypeDef]
    ) -> DeauthorizeConnectionResponseTypeDef:
        """
        Removes all authorization parameters from the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/deauthorize_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#deauthorize_connection)
        """

    async def delete_api_destination(
        self, **kwargs: Unpack[DeleteApiDestinationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified API destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_api_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_api_destination)
        """

    async def delete_archive(self, **kwargs: Unpack[DeleteArchiveRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_archive)
        """

    async def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionRequestTypeDef]
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_connection)
        """

    async def delete_endpoint(
        self, **kwargs: Unpack[DeleteEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete an existing global endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_endpoint)
        """

    async def delete_event_bus(
        self, **kwargs: Unpack[DeleteEventBusRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified custom event bus or partner event bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_event_bus.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_event_bus)
        """

    async def delete_partner_event_source(
        self, **kwargs: Unpack[DeletePartnerEventSourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is used by SaaS partners to delete a partner event source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_partner_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_partner_event_source)
        """

    async def delete_rule(
        self, **kwargs: Unpack[DeleteRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/delete_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#delete_rule)
        """

    async def describe_api_destination(
        self, **kwargs: Unpack[DescribeApiDestinationRequestTypeDef]
    ) -> DescribeApiDestinationResponseTypeDef:
        """
        Retrieves details about an API destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_api_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_api_destination)
        """

    async def describe_archive(
        self, **kwargs: Unpack[DescribeArchiveRequestTypeDef]
    ) -> DescribeArchiveResponseTypeDef:
        """
        Retrieves details about an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_archive)
        """

    async def describe_connection(
        self, **kwargs: Unpack[DescribeConnectionRequestTypeDef]
    ) -> DescribeConnectionResponseTypeDef:
        """
        Retrieves details about a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_connection)
        """

    async def describe_endpoint(
        self, **kwargs: Unpack[DescribeEndpointRequestTypeDef]
    ) -> DescribeEndpointResponseTypeDef:
        """
        Get the information about an existing global endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_endpoint)
        """

    async def describe_event_bus(
        self, **kwargs: Unpack[DescribeEventBusRequestTypeDef]
    ) -> DescribeEventBusResponseTypeDef:
        """
        Displays details about an event bus in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_event_bus.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_event_bus)
        """

    async def describe_event_source(
        self, **kwargs: Unpack[DescribeEventSourceRequestTypeDef]
    ) -> DescribeEventSourceResponseTypeDef:
        """
        This operation lists details about a partner event source that is shared with
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_event_source)
        """

    async def describe_partner_event_source(
        self, **kwargs: Unpack[DescribePartnerEventSourceRequestTypeDef]
    ) -> DescribePartnerEventSourceResponseTypeDef:
        """
        An SaaS partner can use this operation to list details about a partner event
        source that they have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_partner_event_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_partner_event_source)
        """

    async def describe_replay(
        self, **kwargs: Unpack[DescribeReplayRequestTypeDef]
    ) -> DescribeReplayResponseTypeDef:
        """
        Retrieves details about a replay.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_replay.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_replay)
        """

    async def describe_rule(
        self, **kwargs: Unpack[DescribeRuleRequestTypeDef]
    ) -> DescribeRuleResponseTypeDef:
        """
        Describes the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/describe_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#describe_rule)
        """

    async def disable_rule(
        self, **kwargs: Unpack[DisableRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/disable_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#disable_rule)
        """

    async def enable_rule(
        self, **kwargs: Unpack[EnableRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/enable_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#enable_rule)
        """

    async def list_api_destinations(
        self, **kwargs: Unpack[ListApiDestinationsRequestTypeDef]
    ) -> ListApiDestinationsResponseTypeDef:
        """
        Retrieves a list of API destination in the account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_api_destinations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_api_destinations)
        """

    async def list_archives(
        self, **kwargs: Unpack[ListArchivesRequestTypeDef]
    ) -> ListArchivesResponseTypeDef:
        """
        Lists your archives.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_archives.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_archives)
        """

    async def list_connections(
        self, **kwargs: Unpack[ListConnectionsRequestTypeDef]
    ) -> ListConnectionsResponseTypeDef:
        """
        Retrieves a list of connections from the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_connections.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_connections)
        """

    async def list_endpoints(
        self, **kwargs: Unpack[ListEndpointsRequestTypeDef]
    ) -> ListEndpointsResponseTypeDef:
        """
        List the global endpoints associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_endpoints.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_endpoints)
        """

    async def list_event_buses(
        self, **kwargs: Unpack[ListEventBusesRequestTypeDef]
    ) -> ListEventBusesResponseTypeDef:
        """
        Lists all the event buses in your account, including the default event bus,
        custom event buses, and partner event buses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_event_buses.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_event_buses)
        """

    async def list_event_sources(
        self, **kwargs: Unpack[ListEventSourcesRequestTypeDef]
    ) -> ListEventSourcesResponseTypeDef:
        """
        You can use this to see all the partner event sources that have been shared
        with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_event_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_event_sources)
        """

    async def list_partner_event_source_accounts(
        self, **kwargs: Unpack[ListPartnerEventSourceAccountsRequestTypeDef]
    ) -> ListPartnerEventSourceAccountsResponseTypeDef:
        """
        An SaaS partner can use this operation to display the Amazon Web Services
        account ID that a particular partner event source name is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_partner_event_source_accounts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_partner_event_source_accounts)
        """

    async def list_partner_event_sources(
        self, **kwargs: Unpack[ListPartnerEventSourcesRequestTypeDef]
    ) -> ListPartnerEventSourcesResponseTypeDef:
        """
        An SaaS partner can use this operation to list all the partner event source
        names that they have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_partner_event_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_partner_event_sources)
        """

    async def list_replays(
        self, **kwargs: Unpack[ListReplaysRequestTypeDef]
    ) -> ListReplaysResponseTypeDef:
        """
        Lists your replays.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_replays.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_replays)
        """

    async def list_rule_names_by_target(
        self, **kwargs: Unpack[ListRuleNamesByTargetRequestTypeDef]
    ) -> ListRuleNamesByTargetResponseTypeDef:
        """
        Lists the rules for the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_rule_names_by_target.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_rule_names_by_target)
        """

    async def list_rules(
        self, **kwargs: Unpack[ListRulesRequestTypeDef]
    ) -> ListRulesResponseTypeDef:
        """
        Lists your Amazon EventBridge rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_rules)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with an EventBridge resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_tags_for_resource)
        """

    async def list_targets_by_rule(
        self, **kwargs: Unpack[ListTargetsByRuleRequestTypeDef]
    ) -> ListTargetsByRuleResponseTypeDef:
        """
        Lists the targets assigned to the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/list_targets_by_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#list_targets_by_rule)
        """

    async def put_events(
        self, **kwargs: Unpack[PutEventsRequestTypeDef]
    ) -> PutEventsResponseTypeDef:
        """
        Sends custom events to Amazon EventBridge so that they can be matched to rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/put_events.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#put_events)
        """

    async def put_partner_events(
        self, **kwargs: Unpack[PutPartnerEventsRequestTypeDef]
    ) -> PutPartnerEventsResponseTypeDef:
        """
        This is used by SaaS partners to write events to a customer's partner event bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/put_partner_events.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#put_partner_events)
        """

    async def put_permission(
        self, **kwargs: Unpack[PutPermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Running <code>PutPermission</code> permits the specified Amazon Web Services
        account or Amazon Web Services organization to put events to the specified
        <i>event bus</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/put_permission.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#put_permission)
        """

    async def put_rule(self, **kwargs: Unpack[PutRuleRequestTypeDef]) -> PutRuleResponseTypeDef:
        """
        Creates or updates the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/put_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#put_rule)
        """

    async def put_targets(
        self, **kwargs: Unpack[PutTargetsRequestTypeDef]
    ) -> PutTargetsResponseTypeDef:
        """
        Adds the specified targets to the specified rule, or updates the targets if
        they are already associated with the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/put_targets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#put_targets)
        """

    async def remove_permission(
        self, **kwargs: Unpack[RemovePermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Revokes the permission of another Amazon Web Services account to be able to put
        events to the specified event bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/remove_permission.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#remove_permission)
        """

    async def remove_targets(
        self, **kwargs: Unpack[RemoveTargetsRequestTypeDef]
    ) -> RemoveTargetsResponseTypeDef:
        """
        Removes the specified targets from the specified rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/remove_targets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#remove_targets)
        """

    async def start_replay(
        self, **kwargs: Unpack[StartReplayRequestTypeDef]
    ) -> StartReplayResponseTypeDef:
        """
        Starts the specified replay.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/start_replay.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#start_replay)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified EventBridge
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#tag_resource)
        """

    async def test_event_pattern(
        self, **kwargs: Unpack[TestEventPatternRequestTypeDef]
    ) -> TestEventPatternResponseTypeDef:
        """
        Tests whether the specified event pattern matches the provided event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/test_event_pattern.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#test_event_pattern)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified EventBridge resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#untag_resource)
        """

    async def update_api_destination(
        self, **kwargs: Unpack[UpdateApiDestinationRequestTypeDef]
    ) -> UpdateApiDestinationResponseTypeDef:
        """
        Updates an API destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/update_api_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#update_api_destination)
        """

    async def update_archive(
        self, **kwargs: Unpack[UpdateArchiveRequestTypeDef]
    ) -> UpdateArchiveResponseTypeDef:
        """
        Updates the specified archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/update_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#update_archive)
        """

    async def update_connection(
        self, **kwargs: Unpack[UpdateConnectionRequestTypeDef]
    ) -> UpdateConnectionResponseTypeDef:
        """
        Updates settings for a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/update_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#update_connection)
        """

    async def update_endpoint(
        self, **kwargs: Unpack[UpdateEndpointRequestTypeDef]
    ) -> UpdateEndpointResponseTypeDef:
        """
        Update an existing endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/update_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#update_endpoint)
        """

    async def update_event_bus(
        self, **kwargs: Unpack[UpdateEventBusRequestTypeDef]
    ) -> UpdateEventBusResponseTypeDef:
        """
        Updates the specified event bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/update_event_bus.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#update_event_bus)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rule_names_by_target"]
    ) -> ListRuleNamesByTargetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_targets_by_rule"]
    ) -> ListTargetsByRulePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/client/)
        """
