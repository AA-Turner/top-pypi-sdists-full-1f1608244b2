"""
Type annotations for medialive service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_medialive.client import MediaLiveClient

    session = get_session()
    async with session.create_client("medialive") as client:
        client: MediaLiveClient
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
    DescribeSchedulePaginator,
    ListChannelPlacementGroupsPaginator,
    ListChannelsPaginator,
    ListCloudWatchAlarmTemplateGroupsPaginator,
    ListCloudWatchAlarmTemplatesPaginator,
    ListClustersPaginator,
    ListEventBridgeRuleTemplateGroupsPaginator,
    ListEventBridgeRuleTemplatesPaginator,
    ListInputDevicesPaginator,
    ListInputDeviceTransfersPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListNetworksPaginator,
    ListNodesPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
    ListSdiSourcesPaginator,
    ListSignalMapsPaginator,
)
from .type_defs import (
    AcceptInputDeviceTransferRequestTypeDef,
    BatchDeleteRequestTypeDef,
    BatchDeleteResponseTypeDef,
    BatchStartRequestTypeDef,
    BatchStartResponseTypeDef,
    BatchStopRequestTypeDef,
    BatchStopResponseTypeDef,
    BatchUpdateScheduleRequestTypeDef,
    BatchUpdateScheduleResponseTypeDef,
    CancelInputDeviceTransferRequestTypeDef,
    ClaimDeviceRequestTypeDef,
    CreateChannelPlacementGroupRequestTypeDef,
    CreateChannelPlacementGroupResponseTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateCloudWatchAlarmTemplateGroupRequestTypeDef,
    CreateCloudWatchAlarmTemplateGroupResponseTypeDef,
    CreateCloudWatchAlarmTemplateRequestTypeDef,
    CreateCloudWatchAlarmTemplateResponseTypeDef,
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateEventBridgeRuleTemplateGroupRequestTypeDef,
    CreateEventBridgeRuleTemplateGroupResponseTypeDef,
    CreateEventBridgeRuleTemplateRequestTypeDef,
    CreateEventBridgeRuleTemplateResponseTypeDef,
    CreateInputRequestTypeDef,
    CreateInputResponseTypeDef,
    CreateInputSecurityGroupRequestTypeDef,
    CreateInputSecurityGroupResponseTypeDef,
    CreateMultiplexProgramRequestTypeDef,
    CreateMultiplexProgramResponseTypeDef,
    CreateMultiplexRequestTypeDef,
    CreateMultiplexResponseTypeDef,
    CreateNetworkRequestTypeDef,
    CreateNetworkResponseTypeDef,
    CreateNodeRegistrationScriptRequestTypeDef,
    CreateNodeRegistrationScriptResponseTypeDef,
    CreateNodeRequestTypeDef,
    CreateNodeResponseTypeDef,
    CreatePartnerInputRequestTypeDef,
    CreatePartnerInputResponseTypeDef,
    CreateSdiSourceRequestTypeDef,
    CreateSdiSourceResponseTypeDef,
    CreateSignalMapRequestTypeDef,
    CreateSignalMapResponseTypeDef,
    CreateTagsRequestTypeDef,
    DeleteChannelPlacementGroupRequestTypeDef,
    DeleteChannelPlacementGroupResponseTypeDef,
    DeleteChannelRequestTypeDef,
    DeleteChannelResponseTypeDef,
    DeleteCloudWatchAlarmTemplateGroupRequestTypeDef,
    DeleteCloudWatchAlarmTemplateRequestTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteEventBridgeRuleTemplateGroupRequestTypeDef,
    DeleteEventBridgeRuleTemplateRequestTypeDef,
    DeleteInputRequestTypeDef,
    DeleteInputSecurityGroupRequestTypeDef,
    DeleteMultiplexProgramRequestTypeDef,
    DeleteMultiplexProgramResponseTypeDef,
    DeleteMultiplexRequestTypeDef,
    DeleteMultiplexResponseTypeDef,
    DeleteNetworkRequestTypeDef,
    DeleteNetworkResponseTypeDef,
    DeleteNodeRequestTypeDef,
    DeleteNodeResponseTypeDef,
    DeleteReservationRequestTypeDef,
    DeleteReservationResponseTypeDef,
    DeleteScheduleRequestTypeDef,
    DeleteSdiSourceRequestTypeDef,
    DeleteSdiSourceResponseTypeDef,
    DeleteSignalMapRequestTypeDef,
    DeleteTagsRequestTypeDef,
    DescribeAccountConfigurationResponseTypeDef,
    DescribeChannelPlacementGroupRequestTypeDef,
    DescribeChannelPlacementGroupResponseTypeDef,
    DescribeChannelRequestTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeClusterRequestTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeInputDeviceRequestTypeDef,
    DescribeInputDeviceResponseTypeDef,
    DescribeInputDeviceThumbnailRequestTypeDef,
    DescribeInputDeviceThumbnailResponseTypeDef,
    DescribeInputRequestTypeDef,
    DescribeInputResponseTypeDef,
    DescribeInputSecurityGroupRequestTypeDef,
    DescribeInputSecurityGroupResponseTypeDef,
    DescribeMultiplexProgramRequestTypeDef,
    DescribeMultiplexProgramResponseTypeDef,
    DescribeMultiplexRequestTypeDef,
    DescribeMultiplexResponseTypeDef,
    DescribeNetworkRequestTypeDef,
    DescribeNetworkResponseTypeDef,
    DescribeNodeRequestTypeDef,
    DescribeNodeResponseTypeDef,
    DescribeOfferingRequestTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationRequestTypeDef,
    DescribeReservationResponseTypeDef,
    DescribeScheduleRequestTypeDef,
    DescribeScheduleResponseTypeDef,
    DescribeSdiSourceRequestTypeDef,
    DescribeSdiSourceResponseTypeDef,
    DescribeThumbnailsRequestTypeDef,
    DescribeThumbnailsResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCloudWatchAlarmTemplateGroupRequestTypeDef,
    GetCloudWatchAlarmTemplateGroupResponseTypeDef,
    GetCloudWatchAlarmTemplateRequestTypeDef,
    GetCloudWatchAlarmTemplateResponseTypeDef,
    GetEventBridgeRuleTemplateGroupRequestTypeDef,
    GetEventBridgeRuleTemplateGroupResponseTypeDef,
    GetEventBridgeRuleTemplateRequestTypeDef,
    GetEventBridgeRuleTemplateResponseTypeDef,
    GetSignalMapRequestTypeDef,
    GetSignalMapResponseTypeDef,
    ListChannelPlacementGroupsRequestTypeDef,
    ListChannelPlacementGroupsResponseTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListCloudWatchAlarmTemplateGroupsRequestTypeDef,
    ListCloudWatchAlarmTemplateGroupsResponseTypeDef,
    ListCloudWatchAlarmTemplatesRequestTypeDef,
    ListCloudWatchAlarmTemplatesResponseTypeDef,
    ListClustersRequestTypeDef,
    ListClustersResponseTypeDef,
    ListEventBridgeRuleTemplateGroupsRequestTypeDef,
    ListEventBridgeRuleTemplateGroupsResponseTypeDef,
    ListEventBridgeRuleTemplatesRequestTypeDef,
    ListEventBridgeRuleTemplatesResponseTypeDef,
    ListInputDevicesRequestTypeDef,
    ListInputDevicesResponseTypeDef,
    ListInputDeviceTransfersRequestTypeDef,
    ListInputDeviceTransfersResponseTypeDef,
    ListInputSecurityGroupsRequestTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsRequestTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexesRequestTypeDef,
    ListMultiplexesResponseTypeDef,
    ListMultiplexProgramsRequestTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListNetworksRequestTypeDef,
    ListNetworksResponseTypeDef,
    ListNodesRequestTypeDef,
    ListNodesResponseTypeDef,
    ListOfferingsRequestTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsRequestTypeDef,
    ListReservationsResponseTypeDef,
    ListSdiSourcesRequestTypeDef,
    ListSdiSourcesResponseTypeDef,
    ListSignalMapsRequestTypeDef,
    ListSignalMapsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVersionsResponseTypeDef,
    PurchaseOfferingRequestTypeDef,
    PurchaseOfferingResponseTypeDef,
    RebootInputDeviceRequestTypeDef,
    RejectInputDeviceTransferRequestTypeDef,
    RestartChannelPipelinesRequestTypeDef,
    RestartChannelPipelinesResponseTypeDef,
    StartChannelRequestTypeDef,
    StartChannelResponseTypeDef,
    StartDeleteMonitorDeploymentRequestTypeDef,
    StartDeleteMonitorDeploymentResponseTypeDef,
    StartInputDeviceMaintenanceWindowRequestTypeDef,
    StartInputDeviceRequestTypeDef,
    StartMonitorDeploymentRequestTypeDef,
    StartMonitorDeploymentResponseTypeDef,
    StartMultiplexRequestTypeDef,
    StartMultiplexResponseTypeDef,
    StartUpdateSignalMapRequestTypeDef,
    StartUpdateSignalMapResponseTypeDef,
    StopChannelRequestTypeDef,
    StopChannelResponseTypeDef,
    StopInputDeviceRequestTypeDef,
    StopMultiplexRequestTypeDef,
    StopMultiplexResponseTypeDef,
    TransferInputDeviceRequestTypeDef,
    UpdateAccountConfigurationRequestTypeDef,
    UpdateAccountConfigurationResponseTypeDef,
    UpdateChannelClassRequestTypeDef,
    UpdateChannelClassResponseTypeDef,
    UpdateChannelPlacementGroupRequestTypeDef,
    UpdateChannelPlacementGroupResponseTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateCloudWatchAlarmTemplateGroupRequestTypeDef,
    UpdateCloudWatchAlarmTemplateGroupResponseTypeDef,
    UpdateCloudWatchAlarmTemplateRequestTypeDef,
    UpdateCloudWatchAlarmTemplateResponseTypeDef,
    UpdateClusterRequestTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateEventBridgeRuleTemplateGroupRequestTypeDef,
    UpdateEventBridgeRuleTemplateGroupResponseTypeDef,
    UpdateEventBridgeRuleTemplateRequestTypeDef,
    UpdateEventBridgeRuleTemplateResponseTypeDef,
    UpdateInputDeviceRequestTypeDef,
    UpdateInputDeviceResponseTypeDef,
    UpdateInputRequestTypeDef,
    UpdateInputResponseTypeDef,
    UpdateInputSecurityGroupRequestTypeDef,
    UpdateInputSecurityGroupResponseTypeDef,
    UpdateMultiplexProgramRequestTypeDef,
    UpdateMultiplexProgramResponseTypeDef,
    UpdateMultiplexRequestTypeDef,
    UpdateMultiplexResponseTypeDef,
    UpdateNetworkRequestTypeDef,
    UpdateNetworkResponseTypeDef,
    UpdateNodeRequestTypeDef,
    UpdateNodeResponseTypeDef,
    UpdateNodeStateRequestTypeDef,
    UpdateNodeStateResponseTypeDef,
    UpdateReservationRequestTypeDef,
    UpdateReservationResponseTypeDef,
    UpdateSdiSourceRequestTypeDef,
    UpdateSdiSourceResponseTypeDef,
)
from .waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    ChannelPlacementGroupAssignedWaiter,
    ChannelPlacementGroupDeletedWaiter,
    ChannelPlacementGroupUnassignedWaiter,
    ChannelRunningWaiter,
    ChannelStoppedWaiter,
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    InputAttachedWaiter,
    InputDeletedWaiter,
    InputDetachedWaiter,
    MultiplexCreatedWaiter,
    MultiplexDeletedWaiter,
    MultiplexRunningWaiter,
    MultiplexStoppedWaiter,
    NodeDeregisteredWaiter,
    NodeRegisteredWaiter,
    SignalMapCreatedWaiter,
    SignalMapMonitorDeletedWaiter,
    SignalMapMonitorDeployedWaiter,
    SignalMapUpdatedWaiter,
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


__all__ = ("MediaLiveClient",)


class Exceptions(BaseClientExceptions):
    BadGatewayException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GatewayTimeoutException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class MediaLiveClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaLiveClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#generate_presigned_url)
        """

    async def accept_input_device_transfer(
        self, **kwargs: Unpack[AcceptInputDeviceTransferRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Accept an incoming input device transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/accept_input_device_transfer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#accept_input_device_transfer)
        """

    async def batch_delete(
        self, **kwargs: Unpack[BatchDeleteRequestTypeDef]
    ) -> BatchDeleteResponseTypeDef:
        """
        Starts delete of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/batch_delete.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#batch_delete)
        """

    async def batch_start(
        self, **kwargs: Unpack[BatchStartRequestTypeDef]
    ) -> BatchStartResponseTypeDef:
        """
        Starts existing resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/batch_start.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#batch_start)
        """

    async def batch_stop(
        self, **kwargs: Unpack[BatchStopRequestTypeDef]
    ) -> BatchStopResponseTypeDef:
        """
        Stops running resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/batch_stop.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#batch_stop)
        """

    async def batch_update_schedule(
        self, **kwargs: Unpack[BatchUpdateScheduleRequestTypeDef]
    ) -> BatchUpdateScheduleResponseTypeDef:
        """
        Update a channel schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/batch_update_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#batch_update_schedule)
        """

    async def cancel_input_device_transfer(
        self, **kwargs: Unpack[CancelInputDeviceTransferRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancel an input device transfer that you have requested.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/cancel_input_device_transfer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#cancel_input_device_transfer)
        """

    async def claim_device(self, **kwargs: Unpack[ClaimDeviceRequestTypeDef]) -> Dict[str, Any]:
        """
        Send a request to claim an AWS Elemental device that you have purchased from a
        third-party vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/claim_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#claim_device)
        """

    async def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_channel)
        """

    async def create_input(
        self, **kwargs: Unpack[CreateInputRequestTypeDef]
    ) -> CreateInputResponseTypeDef:
        """
        Create an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_input.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_input)
        """

    async def create_input_security_group(
        self, **kwargs: Unpack[CreateInputSecurityGroupRequestTypeDef]
    ) -> CreateInputSecurityGroupResponseTypeDef:
        """
        Creates a Input Security Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_input_security_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_input_security_group)
        """

    async def create_multiplex(
        self, **kwargs: Unpack[CreateMultiplexRequestTypeDef]
    ) -> CreateMultiplexResponseTypeDef:
        """
        Create a new multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_multiplex)
        """

    async def create_multiplex_program(
        self, **kwargs: Unpack[CreateMultiplexProgramRequestTypeDef]
    ) -> CreateMultiplexProgramResponseTypeDef:
        """
        Create a new program in the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_multiplex_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_multiplex_program)
        """

    async def create_partner_input(
        self, **kwargs: Unpack[CreatePartnerInputRequestTypeDef]
    ) -> CreatePartnerInputResponseTypeDef:
        """
        Create a partner input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_partner_input.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_partner_input)
        """

    async def create_tags(
        self, **kwargs: Unpack[CreateTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Create tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_tags)
        """

    async def delete_channel(
        self, **kwargs: Unpack[DeleteChannelRequestTypeDef]
    ) -> DeleteChannelResponseTypeDef:
        """
        Starts deletion of channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_channel)
        """

    async def delete_input(self, **kwargs: Unpack[DeleteInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the input end point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_input.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_input)
        """

    async def delete_input_security_group(
        self, **kwargs: Unpack[DeleteInputSecurityGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Input Security Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_input_security_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_input_security_group)
        """

    async def delete_multiplex(
        self, **kwargs: Unpack[DeleteMultiplexRequestTypeDef]
    ) -> DeleteMultiplexResponseTypeDef:
        """
        Delete a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_multiplex)
        """

    async def delete_multiplex_program(
        self, **kwargs: Unpack[DeleteMultiplexProgramRequestTypeDef]
    ) -> DeleteMultiplexProgramResponseTypeDef:
        """
        Delete a program from a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_multiplex_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_multiplex_program)
        """

    async def delete_reservation(
        self, **kwargs: Unpack[DeleteReservationRequestTypeDef]
    ) -> DeleteReservationResponseTypeDef:
        """
        Delete an expired reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_reservation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_reservation)
        """

    async def delete_schedule(
        self, **kwargs: Unpack[DeleteScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete all schedule actions on a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_schedule)
        """

    async def delete_tags(
        self, **kwargs: Unpack[DeleteTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_tags)
        """

    async def describe_account_configuration(self) -> DescribeAccountConfigurationResponseTypeDef:
        """
        Describe account configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_account_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_account_configuration)
        """

    async def describe_channel(
        self, **kwargs: Unpack[DescribeChannelRequestTypeDef]
    ) -> DescribeChannelResponseTypeDef:
        """
        Gets details about a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_channel)
        """

    async def describe_input(
        self, **kwargs: Unpack[DescribeInputRequestTypeDef]
    ) -> DescribeInputResponseTypeDef:
        """
        Produces details about an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_input.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_input)
        """

    async def describe_input_device(
        self, **kwargs: Unpack[DescribeInputDeviceRequestTypeDef]
    ) -> DescribeInputDeviceResponseTypeDef:
        """
        Gets the details for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_input_device)
        """

    async def describe_input_device_thumbnail(
        self, **kwargs: Unpack[DescribeInputDeviceThumbnailRequestTypeDef]
    ) -> DescribeInputDeviceThumbnailResponseTypeDef:
        """
        Get the latest thumbnail data for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_input_device_thumbnail.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_input_device_thumbnail)
        """

    async def describe_input_security_group(
        self, **kwargs: Unpack[DescribeInputSecurityGroupRequestTypeDef]
    ) -> DescribeInputSecurityGroupResponseTypeDef:
        """
        Produces a summary of an Input Security Group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_input_security_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_input_security_group)
        """

    async def describe_multiplex(
        self, **kwargs: Unpack[DescribeMultiplexRequestTypeDef]
    ) -> DescribeMultiplexResponseTypeDef:
        """
        Gets details about a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_multiplex)
        """

    async def describe_multiplex_program(
        self, **kwargs: Unpack[DescribeMultiplexProgramRequestTypeDef]
    ) -> DescribeMultiplexProgramResponseTypeDef:
        """
        Get the details for a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_multiplex_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_multiplex_program)
        """

    async def describe_offering(
        self, **kwargs: Unpack[DescribeOfferingRequestTypeDef]
    ) -> DescribeOfferingResponseTypeDef:
        """
        Get details for an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_offering.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_offering)
        """

    async def describe_reservation(
        self, **kwargs: Unpack[DescribeReservationRequestTypeDef]
    ) -> DescribeReservationResponseTypeDef:
        """
        Get details for a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_reservation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_reservation)
        """

    async def describe_schedule(
        self, **kwargs: Unpack[DescribeScheduleRequestTypeDef]
    ) -> DescribeScheduleResponseTypeDef:
        """
        Get a channel schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_schedule)
        """

    async def describe_thumbnails(
        self, **kwargs: Unpack[DescribeThumbnailsRequestTypeDef]
    ) -> DescribeThumbnailsResponseTypeDef:
        """
        Describe the latest thumbnails data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_thumbnails.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_thumbnails)
        """

    async def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Produces list of channels that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_channels.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_channels)
        """

    async def list_input_device_transfers(
        self, **kwargs: Unpack[ListInputDeviceTransfersRequestTypeDef]
    ) -> ListInputDeviceTransfersResponseTypeDef:
        """
        List input devices that are currently being transferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_input_device_transfers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_input_device_transfers)
        """

    async def list_input_devices(
        self, **kwargs: Unpack[ListInputDevicesRequestTypeDef]
    ) -> ListInputDevicesResponseTypeDef:
        """
        List input devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_input_devices.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_input_devices)
        """

    async def list_input_security_groups(
        self, **kwargs: Unpack[ListInputSecurityGroupsRequestTypeDef]
    ) -> ListInputSecurityGroupsResponseTypeDef:
        """
        Produces a list of Input Security Groups for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_input_security_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_input_security_groups)
        """

    async def list_inputs(
        self, **kwargs: Unpack[ListInputsRequestTypeDef]
    ) -> ListInputsResponseTypeDef:
        """
        Produces list of inputs that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_inputs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_inputs)
        """

    async def list_multiplex_programs(
        self, **kwargs: Unpack[ListMultiplexProgramsRequestTypeDef]
    ) -> ListMultiplexProgramsResponseTypeDef:
        """
        List the programs that currently exist for a specific multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_multiplex_programs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_multiplex_programs)
        """

    async def list_multiplexes(
        self, **kwargs: Unpack[ListMultiplexesRequestTypeDef]
    ) -> ListMultiplexesResponseTypeDef:
        """
        Retrieve a list of the existing multiplexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_multiplexes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_multiplexes)
        """

    async def list_offerings(
        self, **kwargs: Unpack[ListOfferingsRequestTypeDef]
    ) -> ListOfferingsResponseTypeDef:
        """
        List offerings available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_offerings.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_offerings)
        """

    async def list_reservations(
        self, **kwargs: Unpack[ListReservationsRequestTypeDef]
    ) -> ListReservationsResponseTypeDef:
        """
        List purchased reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_reservations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_reservations)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Produces list of tags that have been created for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_tags_for_resource)
        """

    async def purchase_offering(
        self, **kwargs: Unpack[PurchaseOfferingRequestTypeDef]
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Purchase an offering and create a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/purchase_offering.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#purchase_offering)
        """

    async def reboot_input_device(
        self, **kwargs: Unpack[RebootInputDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Send a reboot command to the specified input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/reboot_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#reboot_input_device)
        """

    async def reject_input_device_transfer(
        self, **kwargs: Unpack[RejectInputDeviceTransferRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Reject the transfer of the specified input device to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/reject_input_device_transfer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#reject_input_device_transfer)
        """

    async def start_channel(
        self, **kwargs: Unpack[StartChannelRequestTypeDef]
    ) -> StartChannelResponseTypeDef:
        """
        Starts an existing channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_channel)
        """

    async def start_input_device(
        self, **kwargs: Unpack[StartInputDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Start an input device that is attached to a MediaConnect flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_input_device)
        """

    async def start_input_device_maintenance_window(
        self, **kwargs: Unpack[StartInputDeviceMaintenanceWindowRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Start a maintenance window for the specified input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_input_device_maintenance_window.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_input_device_maintenance_window)
        """

    async def start_multiplex(
        self, **kwargs: Unpack[StartMultiplexRequestTypeDef]
    ) -> StartMultiplexResponseTypeDef:
        """
        Start (run) the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_multiplex)
        """

    async def stop_channel(
        self, **kwargs: Unpack[StopChannelRequestTypeDef]
    ) -> StopChannelResponseTypeDef:
        """
        Stops a running channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/stop_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#stop_channel)
        """

    async def stop_input_device(
        self, **kwargs: Unpack[StopInputDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stop an input device that is attached to a MediaConnect flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/stop_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#stop_input_device)
        """

    async def stop_multiplex(
        self, **kwargs: Unpack[StopMultiplexRequestTypeDef]
    ) -> StopMultiplexResponseTypeDef:
        """
        Stops a running multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/stop_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#stop_multiplex)
        """

    async def transfer_input_device(
        self, **kwargs: Unpack[TransferInputDeviceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Start an input device transfer to another AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/transfer_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#transfer_input_device)
        """

    async def update_account_configuration(
        self, **kwargs: Unpack[UpdateAccountConfigurationRequestTypeDef]
    ) -> UpdateAccountConfigurationResponseTypeDef:
        """
        Update account configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_account_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_account_configuration)
        """

    async def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_channel)
        """

    async def update_channel_class(
        self, **kwargs: Unpack[UpdateChannelClassRequestTypeDef]
    ) -> UpdateChannelClassResponseTypeDef:
        """
        Changes the class of the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_channel_class.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_channel_class)
        """

    async def update_input(
        self, **kwargs: Unpack[UpdateInputRequestTypeDef]
    ) -> UpdateInputResponseTypeDef:
        """
        Updates an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_input.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_input)
        """

    async def update_input_device(
        self, **kwargs: Unpack[UpdateInputDeviceRequestTypeDef]
    ) -> UpdateInputDeviceResponseTypeDef:
        """
        Updates the parameters for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_input_device.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_input_device)
        """

    async def update_input_security_group(
        self, **kwargs: Unpack[UpdateInputSecurityGroupRequestTypeDef]
    ) -> UpdateInputSecurityGroupResponseTypeDef:
        """
        Update an Input Security Group's Whilelists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_input_security_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_input_security_group)
        """

    async def update_multiplex(
        self, **kwargs: Unpack[UpdateMultiplexRequestTypeDef]
    ) -> UpdateMultiplexResponseTypeDef:
        """
        Updates a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_multiplex.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_multiplex)
        """

    async def update_multiplex_program(
        self, **kwargs: Unpack[UpdateMultiplexProgramRequestTypeDef]
    ) -> UpdateMultiplexProgramResponseTypeDef:
        """
        Update a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_multiplex_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_multiplex_program)
        """

    async def update_reservation(
        self, **kwargs: Unpack[UpdateReservationRequestTypeDef]
    ) -> UpdateReservationResponseTypeDef:
        """
        Update reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_reservation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_reservation)
        """

    async def restart_channel_pipelines(
        self, **kwargs: Unpack[RestartChannelPipelinesRequestTypeDef]
    ) -> RestartChannelPipelinesResponseTypeDef:
        """
        Restart pipelines in one channel that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/restart_channel_pipelines.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#restart_channel_pipelines)
        """

    async def create_cloud_watch_alarm_template(
        self, **kwargs: Unpack[CreateCloudWatchAlarmTemplateRequestTypeDef]
    ) -> CreateCloudWatchAlarmTemplateResponseTypeDef:
        """
        Creates a cloudwatch alarm template to dynamically generate cloudwatch metric
        alarms on targeted resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_cloud_watch_alarm_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_cloud_watch_alarm_template)
        """

    async def create_cloud_watch_alarm_template_group(
        self, **kwargs: Unpack[CreateCloudWatchAlarmTemplateGroupRequestTypeDef]
    ) -> CreateCloudWatchAlarmTemplateGroupResponseTypeDef:
        """
        Creates a cloudwatch alarm template group to group your cloudwatch alarm
        templates and to attach to signal maps for dynamically creating alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_cloud_watch_alarm_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_cloud_watch_alarm_template_group)
        """

    async def create_event_bridge_rule_template(
        self, **kwargs: Unpack[CreateEventBridgeRuleTemplateRequestTypeDef]
    ) -> CreateEventBridgeRuleTemplateResponseTypeDef:
        """
        Creates an eventbridge rule template to monitor events and send notifications
        to your targeted resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_event_bridge_rule_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_event_bridge_rule_template)
        """

    async def create_event_bridge_rule_template_group(
        self, **kwargs: Unpack[CreateEventBridgeRuleTemplateGroupRequestTypeDef]
    ) -> CreateEventBridgeRuleTemplateGroupResponseTypeDef:
        """
        Creates an eventbridge rule template group to group your eventbridge rule
        templates and to attach to signal maps for dynamically creating notification
        rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_event_bridge_rule_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_event_bridge_rule_template_group)
        """

    async def create_signal_map(
        self, **kwargs: Unpack[CreateSignalMapRequestTypeDef]
    ) -> CreateSignalMapResponseTypeDef:
        """
        Initiates the creation of a new signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_signal_map.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_signal_map)
        """

    async def delete_cloud_watch_alarm_template(
        self, **kwargs: Unpack[DeleteCloudWatchAlarmTemplateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a cloudwatch alarm template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_cloud_watch_alarm_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_cloud_watch_alarm_template)
        """

    async def delete_cloud_watch_alarm_template_group(
        self, **kwargs: Unpack[DeleteCloudWatchAlarmTemplateGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a cloudwatch alarm template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_cloud_watch_alarm_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_cloud_watch_alarm_template_group)
        """

    async def delete_event_bridge_rule_template(
        self, **kwargs: Unpack[DeleteEventBridgeRuleTemplateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an eventbridge rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_event_bridge_rule_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_event_bridge_rule_template)
        """

    async def delete_event_bridge_rule_template_group(
        self, **kwargs: Unpack[DeleteEventBridgeRuleTemplateGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an eventbridge rule template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_event_bridge_rule_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_event_bridge_rule_template_group)
        """

    async def delete_signal_map(
        self, **kwargs: Unpack[DeleteSignalMapRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_signal_map.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_signal_map)
        """

    async def get_cloud_watch_alarm_template(
        self, **kwargs: Unpack[GetCloudWatchAlarmTemplateRequestTypeDef]
    ) -> GetCloudWatchAlarmTemplateResponseTypeDef:
        """
        Retrieves the specified cloudwatch alarm template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_cloud_watch_alarm_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_cloud_watch_alarm_template)
        """

    async def get_cloud_watch_alarm_template_group(
        self, **kwargs: Unpack[GetCloudWatchAlarmTemplateGroupRequestTypeDef]
    ) -> GetCloudWatchAlarmTemplateGroupResponseTypeDef:
        """
        Retrieves the specified cloudwatch alarm template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_cloud_watch_alarm_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_cloud_watch_alarm_template_group)
        """

    async def get_event_bridge_rule_template(
        self, **kwargs: Unpack[GetEventBridgeRuleTemplateRequestTypeDef]
    ) -> GetEventBridgeRuleTemplateResponseTypeDef:
        """
        Retrieves the specified eventbridge rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_event_bridge_rule_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_event_bridge_rule_template)
        """

    async def get_event_bridge_rule_template_group(
        self, **kwargs: Unpack[GetEventBridgeRuleTemplateGroupRequestTypeDef]
    ) -> GetEventBridgeRuleTemplateGroupResponseTypeDef:
        """
        Retrieves the specified eventbridge rule template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_event_bridge_rule_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_event_bridge_rule_template_group)
        """

    async def get_signal_map(
        self, **kwargs: Unpack[GetSignalMapRequestTypeDef]
    ) -> GetSignalMapResponseTypeDef:
        """
        Retrieves the specified signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_signal_map.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_signal_map)
        """

    async def list_cloud_watch_alarm_template_groups(
        self, **kwargs: Unpack[ListCloudWatchAlarmTemplateGroupsRequestTypeDef]
    ) -> ListCloudWatchAlarmTemplateGroupsResponseTypeDef:
        """
        Lists cloudwatch alarm template groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_cloud_watch_alarm_template_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_cloud_watch_alarm_template_groups)
        """

    async def list_cloud_watch_alarm_templates(
        self, **kwargs: Unpack[ListCloudWatchAlarmTemplatesRequestTypeDef]
    ) -> ListCloudWatchAlarmTemplatesResponseTypeDef:
        """
        Lists cloudwatch alarm templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_cloud_watch_alarm_templates.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_cloud_watch_alarm_templates)
        """

    async def list_event_bridge_rule_template_groups(
        self, **kwargs: Unpack[ListEventBridgeRuleTemplateGroupsRequestTypeDef]
    ) -> ListEventBridgeRuleTemplateGroupsResponseTypeDef:
        """
        Lists eventbridge rule template groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_event_bridge_rule_template_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_event_bridge_rule_template_groups)
        """

    async def list_event_bridge_rule_templates(
        self, **kwargs: Unpack[ListEventBridgeRuleTemplatesRequestTypeDef]
    ) -> ListEventBridgeRuleTemplatesResponseTypeDef:
        """
        Lists eventbridge rule templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_event_bridge_rule_templates.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_event_bridge_rule_templates)
        """

    async def list_signal_maps(
        self, **kwargs: Unpack[ListSignalMapsRequestTypeDef]
    ) -> ListSignalMapsResponseTypeDef:
        """
        Lists signal maps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_signal_maps.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_signal_maps)
        """

    async def start_delete_monitor_deployment(
        self, **kwargs: Unpack[StartDeleteMonitorDeploymentRequestTypeDef]
    ) -> StartDeleteMonitorDeploymentResponseTypeDef:
        """
        Initiates a deployment to delete the monitor of the specified signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_delete_monitor_deployment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_delete_monitor_deployment)
        """

    async def start_monitor_deployment(
        self, **kwargs: Unpack[StartMonitorDeploymentRequestTypeDef]
    ) -> StartMonitorDeploymentResponseTypeDef:
        """
        Initiates a deployment to deploy the latest monitor of the specified signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_monitor_deployment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_monitor_deployment)
        """

    async def start_update_signal_map(
        self, **kwargs: Unpack[StartUpdateSignalMapRequestTypeDef]
    ) -> StartUpdateSignalMapResponseTypeDef:
        """
        Initiates an update for the specified signal map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/start_update_signal_map.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#start_update_signal_map)
        """

    async def update_cloud_watch_alarm_template(
        self, **kwargs: Unpack[UpdateCloudWatchAlarmTemplateRequestTypeDef]
    ) -> UpdateCloudWatchAlarmTemplateResponseTypeDef:
        """
        Updates the specified cloudwatch alarm template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_cloud_watch_alarm_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_cloud_watch_alarm_template)
        """

    async def update_cloud_watch_alarm_template_group(
        self, **kwargs: Unpack[UpdateCloudWatchAlarmTemplateGroupRequestTypeDef]
    ) -> UpdateCloudWatchAlarmTemplateGroupResponseTypeDef:
        """
        Updates the specified cloudwatch alarm template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_cloud_watch_alarm_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_cloud_watch_alarm_template_group)
        """

    async def update_event_bridge_rule_template(
        self, **kwargs: Unpack[UpdateEventBridgeRuleTemplateRequestTypeDef]
    ) -> UpdateEventBridgeRuleTemplateResponseTypeDef:
        """
        Updates the specified eventbridge rule template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_event_bridge_rule_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_event_bridge_rule_template)
        """

    async def update_event_bridge_rule_template_group(
        self, **kwargs: Unpack[UpdateEventBridgeRuleTemplateGroupRequestTypeDef]
    ) -> UpdateEventBridgeRuleTemplateGroupResponseTypeDef:
        """
        Updates the specified eventbridge rule template group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_event_bridge_rule_template_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_event_bridge_rule_template_group)
        """

    async def create_channel_placement_group(
        self, **kwargs: Unpack[CreateChannelPlacementGroupRequestTypeDef]
    ) -> CreateChannelPlacementGroupResponseTypeDef:
        """
        Create a ChannelPlacementGroup in the specified Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_channel_placement_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_channel_placement_group)
        """

    async def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Create a new Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_cluster)
        """

    async def create_network(
        self, **kwargs: Unpack[CreateNetworkRequestTypeDef]
    ) -> CreateNetworkResponseTypeDef:
        """
        Create as many Networks as you need.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_network.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_network)
        """

    async def create_node(
        self, **kwargs: Unpack[CreateNodeRequestTypeDef]
    ) -> CreateNodeResponseTypeDef:
        """
        Create a Node in the specified Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_node.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_node)
        """

    async def create_node_registration_script(
        self, **kwargs: Unpack[CreateNodeRegistrationScriptRequestTypeDef]
    ) -> CreateNodeRegistrationScriptResponseTypeDef:
        """
        Create the Register Node script for all the nodes intended for a specific
        Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_node_registration_script.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_node_registration_script)
        """

    async def delete_channel_placement_group(
        self, **kwargs: Unpack[DeleteChannelPlacementGroupRequestTypeDef]
    ) -> DeleteChannelPlacementGroupResponseTypeDef:
        """
        Delete the specified ChannelPlacementGroup that exists in the specified Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_channel_placement_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_channel_placement_group)
        """

    async def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Delete a Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_cluster)
        """

    async def delete_network(
        self, **kwargs: Unpack[DeleteNetworkRequestTypeDef]
    ) -> DeleteNetworkResponseTypeDef:
        """
        Delete a Network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_network.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_network)
        """

    async def delete_node(
        self, **kwargs: Unpack[DeleteNodeRequestTypeDef]
    ) -> DeleteNodeResponseTypeDef:
        """
        Delete a Node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_node.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_node)
        """

    async def describe_channel_placement_group(
        self, **kwargs: Unpack[DescribeChannelPlacementGroupRequestTypeDef]
    ) -> DescribeChannelPlacementGroupResponseTypeDef:
        """
        Get details about a ChannelPlacementGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_channel_placement_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_channel_placement_group)
        """

    async def describe_cluster(
        self, **kwargs: Unpack[DescribeClusterRequestTypeDef]
    ) -> DescribeClusterResponseTypeDef:
        """
        Get details about a Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_cluster)
        """

    async def describe_network(
        self, **kwargs: Unpack[DescribeNetworkRequestTypeDef]
    ) -> DescribeNetworkResponseTypeDef:
        """
        Get details about a Network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_network.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_network)
        """

    async def describe_node(
        self, **kwargs: Unpack[DescribeNodeRequestTypeDef]
    ) -> DescribeNodeResponseTypeDef:
        """
        Get details about a Node in the specified Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_node.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_node)
        """

    async def list_channel_placement_groups(
        self, **kwargs: Unpack[ListChannelPlacementGroupsRequestTypeDef]
    ) -> ListChannelPlacementGroupsResponseTypeDef:
        """
        Retrieve the list of ChannelPlacementGroups in the specified Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_channel_placement_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_channel_placement_groups)
        """

    async def list_clusters(
        self, **kwargs: Unpack[ListClustersRequestTypeDef]
    ) -> ListClustersResponseTypeDef:
        """
        Retrieve the list of Clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_clusters.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_clusters)
        """

    async def list_networks(
        self, **kwargs: Unpack[ListNetworksRequestTypeDef]
    ) -> ListNetworksResponseTypeDef:
        """
        Retrieve the list of Networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_networks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_networks)
        """

    async def list_nodes(
        self, **kwargs: Unpack[ListNodesRequestTypeDef]
    ) -> ListNodesResponseTypeDef:
        """
        Retrieve the list of Nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_nodes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_nodes)
        """

    async def update_channel_placement_group(
        self, **kwargs: Unpack[UpdateChannelPlacementGroupRequestTypeDef]
    ) -> UpdateChannelPlacementGroupResponseTypeDef:
        """
        Change the settings for a ChannelPlacementGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_channel_placement_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_channel_placement_group)
        """

    async def update_cluster(
        self, **kwargs: Unpack[UpdateClusterRequestTypeDef]
    ) -> UpdateClusterResponseTypeDef:
        """
        Change the settings for a Cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_cluster)
        """

    async def update_network(
        self, **kwargs: Unpack[UpdateNetworkRequestTypeDef]
    ) -> UpdateNetworkResponseTypeDef:
        """
        Change the settings for a Network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_network.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_network)
        """

    async def update_node(
        self, **kwargs: Unpack[UpdateNodeRequestTypeDef]
    ) -> UpdateNodeResponseTypeDef:
        """
        Change the settings for a Node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_node.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_node)
        """

    async def update_node_state(
        self, **kwargs: Unpack[UpdateNodeStateRequestTypeDef]
    ) -> UpdateNodeStateResponseTypeDef:
        """
        Update the state of a node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_node_state.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_node_state)
        """

    async def list_versions(self) -> ListVersionsResponseTypeDef:
        """
        Retrieves an array of all the encoder engine versions that are available in
        this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_versions)
        """

    async def create_sdi_source(
        self, **kwargs: Unpack[CreateSdiSourceRequestTypeDef]
    ) -> CreateSdiSourceResponseTypeDef:
        """
        Create an SdiSource for each video source that uses the SDI protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/create_sdi_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#create_sdi_source)
        """

    async def delete_sdi_source(
        self, **kwargs: Unpack[DeleteSdiSourceRequestTypeDef]
    ) -> DeleteSdiSourceResponseTypeDef:
        """
        Delete an SdiSource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/delete_sdi_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#delete_sdi_source)
        """

    async def describe_sdi_source(
        self, **kwargs: Unpack[DescribeSdiSourceRequestTypeDef]
    ) -> DescribeSdiSourceResponseTypeDef:
        """
        Gets details about a SdiSource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/describe_sdi_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#describe_sdi_source)
        """

    async def list_sdi_sources(
        self, **kwargs: Unpack[ListSdiSourcesRequestTypeDef]
    ) -> ListSdiSourcesResponseTypeDef:
        """
        List all the SdiSources in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/list_sdi_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#list_sdi_sources)
        """

    async def update_sdi_source(
        self, **kwargs: Unpack[UpdateSdiSourceRequestTypeDef]
    ) -> UpdateSdiSourceResponseTypeDef:
        """
        Change some of the settings in an SdiSource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/update_sdi_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#update_sdi_source)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_schedule"]
    ) -> DescribeSchedulePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channel_placement_groups"]
    ) -> ListChannelPlacementGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_watch_alarm_template_groups"]
    ) -> ListCloudWatchAlarmTemplateGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_watch_alarm_templates"]
    ) -> ListCloudWatchAlarmTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_bridge_rule_template_groups"]
    ) -> ListEventBridgeRuleTemplateGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_bridge_rule_templates"]
    ) -> ListEventBridgeRuleTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_input_device_transfers"]
    ) -> ListInputDeviceTransfersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_input_devices"]
    ) -> ListInputDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_input_security_groups"]
    ) -> ListInputSecurityGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_inputs"]
    ) -> ListInputsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_multiplex_programs"]
    ) -> ListMultiplexProgramsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_multiplexes"]
    ) -> ListMultiplexesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_networks"]
    ) -> ListNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_nodes"]
    ) -> ListNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_offerings"]
    ) -> ListOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sdi_sources"]
    ) -> ListSdiSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signal_maps"]
    ) -> ListSignalMapsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_created"]
    ) -> ChannelCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_deleted"]
    ) -> ChannelDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_placement_group_assigned"]
    ) -> ChannelPlacementGroupAssignedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_placement_group_deleted"]
    ) -> ChannelPlacementGroupDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_placement_group_unassigned"]
    ) -> ChannelPlacementGroupUnassignedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_running"]
    ) -> ChannelRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["channel_stopped"]
    ) -> ChannelStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_created"]
    ) -> ClusterCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_deleted"]
    ) -> ClusterDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_attached"]
    ) -> InputAttachedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_deleted"]
    ) -> InputDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["input_detached"]
    ) -> InputDetachedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["multiplex_created"]
    ) -> MultiplexCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["multiplex_deleted"]
    ) -> MultiplexDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["multiplex_running"]
    ) -> MultiplexRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["multiplex_stopped"]
    ) -> MultiplexStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["node_deregistered"]
    ) -> NodeDeregisteredWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["node_registered"]
    ) -> NodeRegisteredWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["signal_map_created"]
    ) -> SignalMapCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["signal_map_monitor_deleted"]
    ) -> SignalMapMonitorDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["signal_map_monitor_deployed"]
    ) -> SignalMapMonitorDeployedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["signal_map_updated"]
    ) -> SignalMapUpdatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client/)
        """
