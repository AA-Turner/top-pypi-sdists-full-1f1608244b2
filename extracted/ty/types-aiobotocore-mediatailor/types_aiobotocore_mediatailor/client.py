"""
Type annotations for mediatailor service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_mediatailor.client import MediaTailorClient

    session = get_session()
    async with session.create_client("mediatailor") as client:
        client: MediaTailorClient
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
    GetChannelSchedulePaginator,
    ListAlertsPaginator,
    ListChannelsPaginator,
    ListLiveSourcesPaginator,
    ListPlaybackConfigurationsPaginator,
    ListPrefetchSchedulesPaginator,
    ListSourceLocationsPaginator,
    ListVodSourcesPaginator,
)
from .type_defs import (
    ConfigureLogsForChannelRequestTypeDef,
    ConfigureLogsForChannelResponseTypeDef,
    ConfigureLogsForPlaybackConfigurationRequestTypeDef,
    ConfigureLogsForPlaybackConfigurationResponseTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateLiveSourceRequestTypeDef,
    CreateLiveSourceResponseTypeDef,
    CreatePrefetchScheduleRequestTypeDef,
    CreatePrefetchScheduleResponseTypeDef,
    CreateProgramRequestTypeDef,
    CreateProgramResponseTypeDef,
    CreateSourceLocationRequestTypeDef,
    CreateSourceLocationResponseTypeDef,
    CreateVodSourceRequestTypeDef,
    CreateVodSourceResponseTypeDef,
    DeleteChannelPolicyRequestTypeDef,
    DeleteChannelRequestTypeDef,
    DeleteLiveSourceRequestTypeDef,
    DeletePlaybackConfigurationRequestTypeDef,
    DeletePrefetchScheduleRequestTypeDef,
    DeleteProgramRequestTypeDef,
    DeleteSourceLocationRequestTypeDef,
    DeleteVodSourceRequestTypeDef,
    DescribeChannelRequestTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeLiveSourceRequestTypeDef,
    DescribeLiveSourceResponseTypeDef,
    DescribeProgramRequestTypeDef,
    DescribeProgramResponseTypeDef,
    DescribeSourceLocationRequestTypeDef,
    DescribeSourceLocationResponseTypeDef,
    DescribeVodSourceRequestTypeDef,
    DescribeVodSourceResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChannelPolicyRequestTypeDef,
    GetChannelPolicyResponseTypeDef,
    GetChannelScheduleRequestTypeDef,
    GetChannelScheduleResponseTypeDef,
    GetPlaybackConfigurationRequestTypeDef,
    GetPlaybackConfigurationResponseTypeDef,
    GetPrefetchScheduleRequestTypeDef,
    GetPrefetchScheduleResponseTypeDef,
    ListAlertsRequestTypeDef,
    ListAlertsResponseTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListLiveSourcesRequestTypeDef,
    ListLiveSourcesResponseTypeDef,
    ListPlaybackConfigurationsRequestTypeDef,
    ListPlaybackConfigurationsResponseTypeDef,
    ListPrefetchSchedulesRequestTypeDef,
    ListPrefetchSchedulesResponseTypeDef,
    ListSourceLocationsRequestTypeDef,
    ListSourceLocationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVodSourcesRequestTypeDef,
    ListVodSourcesResponseTypeDef,
    PutChannelPolicyRequestTypeDef,
    PutPlaybackConfigurationRequestTypeDef,
    PutPlaybackConfigurationResponseTypeDef,
    StartChannelRequestTypeDef,
    StopChannelRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateLiveSourceRequestTypeDef,
    UpdateLiveSourceResponseTypeDef,
    UpdateProgramRequestTypeDef,
    UpdateProgramResponseTypeDef,
    UpdateSourceLocationRequestTypeDef,
    UpdateSourceLocationResponseTypeDef,
    UpdateVodSourceRequestTypeDef,
    UpdateVodSourceResponseTypeDef,
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


__all__ = ("MediaTailorClient",)


class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]


class MediaTailorClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaTailorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#generate_presigned_url)
        """

    async def configure_logs_for_channel(
        self, **kwargs: Unpack[ConfigureLogsForChannelRequestTypeDef]
    ) -> ConfigureLogsForChannelResponseTypeDef:
        """
        Configures Amazon CloudWatch log settings for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/configure_logs_for_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#configure_logs_for_channel)
        """

    async def configure_logs_for_playback_configuration(
        self, **kwargs: Unpack[ConfigureLogsForPlaybackConfigurationRequestTypeDef]
    ) -> ConfigureLogsForPlaybackConfigurationResponseTypeDef:
        """
        Defines where AWS Elemental MediaTailor sends logs for the playback
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/configure_logs_for_playback_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#configure_logs_for_playback_configuration)
        """

    async def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_channel)
        """

    async def create_live_source(
        self, **kwargs: Unpack[CreateLiveSourceRequestTypeDef]
    ) -> CreateLiveSourceResponseTypeDef:
        """
        The live source configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_live_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_live_source)
        """

    async def create_prefetch_schedule(
        self, **kwargs: Unpack[CreatePrefetchScheduleRequestTypeDef]
    ) -> CreatePrefetchScheduleResponseTypeDef:
        """
        Creates a prefetch schedule for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_prefetch_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_prefetch_schedule)
        """

    async def create_program(
        self, **kwargs: Unpack[CreateProgramRequestTypeDef]
    ) -> CreateProgramResponseTypeDef:
        """
        Creates a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_program)
        """

    async def create_source_location(
        self, **kwargs: Unpack[CreateSourceLocationRequestTypeDef]
    ) -> CreateSourceLocationResponseTypeDef:
        """
        Creates a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_source_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_source_location)
        """

    async def create_vod_source(
        self, **kwargs: Unpack[CreateVodSourceRequestTypeDef]
    ) -> CreateVodSourceResponseTypeDef:
        """
        The VOD source configuration parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/create_vod_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#create_vod_source)
        """

    async def delete_channel(self, **kwargs: Unpack[DeleteChannelRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_channel)
        """

    async def delete_channel_policy(
        self, **kwargs: Unpack[DeleteChannelPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The channel policy to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_channel_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_channel_policy)
        """

    async def delete_live_source(
        self, **kwargs: Unpack[DeleteLiveSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The live source to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_live_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_live_source)
        """

    async def delete_playback_configuration(
        self, **kwargs: Unpack[DeletePlaybackConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_playback_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_playback_configuration)
        """

    async def delete_prefetch_schedule(
        self, **kwargs: Unpack[DeletePrefetchScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a prefetch schedule for a specific playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_prefetch_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_prefetch_schedule)
        """

    async def delete_program(self, **kwargs: Unpack[DeleteProgramRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_program)
        """

    async def delete_source_location(
        self, **kwargs: Unpack[DeleteSourceLocationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_source_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_source_location)
        """

    async def delete_vod_source(
        self, **kwargs: Unpack[DeleteVodSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The video on demand (VOD) source to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/delete_vod_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#delete_vod_source)
        """

    async def describe_channel(
        self, **kwargs: Unpack[DescribeChannelRequestTypeDef]
    ) -> DescribeChannelResponseTypeDef:
        """
        Describes a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/describe_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#describe_channel)
        """

    async def describe_live_source(
        self, **kwargs: Unpack[DescribeLiveSourceRequestTypeDef]
    ) -> DescribeLiveSourceResponseTypeDef:
        """
        The live source to describe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/describe_live_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#describe_live_source)
        """

    async def describe_program(
        self, **kwargs: Unpack[DescribeProgramRequestTypeDef]
    ) -> DescribeProgramResponseTypeDef:
        """
        Describes a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/describe_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#describe_program)
        """

    async def describe_source_location(
        self, **kwargs: Unpack[DescribeSourceLocationRequestTypeDef]
    ) -> DescribeSourceLocationResponseTypeDef:
        """
        Describes a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/describe_source_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#describe_source_location)
        """

    async def describe_vod_source(
        self, **kwargs: Unpack[DescribeVodSourceRequestTypeDef]
    ) -> DescribeVodSourceResponseTypeDef:
        """
        Provides details about a specific video on demand (VOD) source in a specific
        source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/describe_vod_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#describe_vod_source)
        """

    async def get_channel_policy(
        self, **kwargs: Unpack[GetChannelPolicyRequestTypeDef]
    ) -> GetChannelPolicyResponseTypeDef:
        """
        Returns the channel's IAM policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_channel_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_channel_policy)
        """

    async def get_channel_schedule(
        self, **kwargs: Unpack[GetChannelScheduleRequestTypeDef]
    ) -> GetChannelScheduleResponseTypeDef:
        """
        Retrieves information about your channel's schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_channel_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_channel_schedule)
        """

    async def get_playback_configuration(
        self, **kwargs: Unpack[GetPlaybackConfigurationRequestTypeDef]
    ) -> GetPlaybackConfigurationResponseTypeDef:
        """
        Retrieves a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_playback_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_playback_configuration)
        """

    async def get_prefetch_schedule(
        self, **kwargs: Unpack[GetPrefetchScheduleRequestTypeDef]
    ) -> GetPrefetchScheduleResponseTypeDef:
        """
        Retrieves a prefetch schedule for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_prefetch_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_prefetch_schedule)
        """

    async def list_alerts(
        self, **kwargs: Unpack[ListAlertsRequestTypeDef]
    ) -> ListAlertsResponseTypeDef:
        """
        Lists the alerts that are associated with a MediaTailor channel assembly
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_alerts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_alerts)
        """

    async def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves information about the channels that are associated with the current
        AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_channels.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_channels)
        """

    async def list_live_sources(
        self, **kwargs: Unpack[ListLiveSourcesRequestTypeDef]
    ) -> ListLiveSourcesResponseTypeDef:
        """
        Lists the live sources contained in a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_live_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_live_sources)
        """

    async def list_playback_configurations(
        self, **kwargs: Unpack[ListPlaybackConfigurationsRequestTypeDef]
    ) -> ListPlaybackConfigurationsResponseTypeDef:
        """
        Retrieves existing playback configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_playback_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_playback_configurations)
        """

    async def list_prefetch_schedules(
        self, **kwargs: Unpack[ListPrefetchSchedulesRequestTypeDef]
    ) -> ListPrefetchSchedulesResponseTypeDef:
        """
        Lists the prefetch schedules for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_prefetch_schedules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_prefetch_schedules)
        """

    async def list_source_locations(
        self, **kwargs: Unpack[ListSourceLocationsRequestTypeDef]
    ) -> ListSourceLocationsResponseTypeDef:
        """
        Lists the source locations for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_source_locations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_source_locations)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        A list of tags that are associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_tags_for_resource)
        """

    async def list_vod_sources(
        self, **kwargs: Unpack[ListVodSourcesRequestTypeDef]
    ) -> ListVodSourcesResponseTypeDef:
        """
        Lists the VOD sources contained in a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/list_vod_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#list_vod_sources)
        """

    async def put_channel_policy(
        self, **kwargs: Unpack[PutChannelPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates an IAM policy for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/put_channel_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#put_channel_policy)
        """

    async def put_playback_configuration(
        self, **kwargs: Unpack[PutPlaybackConfigurationRequestTypeDef]
    ) -> PutPlaybackConfigurationResponseTypeDef:
        """
        Creates a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/put_playback_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#put_playback_configuration)
        """

    async def start_channel(self, **kwargs: Unpack[StartChannelRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/start_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#start_channel)
        """

    async def stop_channel(self, **kwargs: Unpack[StopChannelRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/stop_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#stop_channel)
        """

    async def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The resource to tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#tag_resource)
        """

    async def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The resource to untag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#untag_resource)
        """

    async def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/update_channel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#update_channel)
        """

    async def update_live_source(
        self, **kwargs: Unpack[UpdateLiveSourceRequestTypeDef]
    ) -> UpdateLiveSourceResponseTypeDef:
        """
        Updates a live source's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/update_live_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#update_live_source)
        """

    async def update_program(
        self, **kwargs: Unpack[UpdateProgramRequestTypeDef]
    ) -> UpdateProgramResponseTypeDef:
        """
        Updates a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/update_program.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#update_program)
        """

    async def update_source_location(
        self, **kwargs: Unpack[UpdateSourceLocationRequestTypeDef]
    ) -> UpdateSourceLocationResponseTypeDef:
        """
        Updates a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/update_source_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#update_source_location)
        """

    async def update_vod_source(
        self, **kwargs: Unpack[UpdateVodSourceRequestTypeDef]
    ) -> UpdateVodSourceResponseTypeDef:
        """
        Updates a VOD source's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/update_vod_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#update_vod_source)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_channel_schedule"]
    ) -> GetChannelSchedulePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_alerts"]
    ) -> ListAlertsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_live_sources"]
    ) -> ListLiveSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_playback_configurations"]
    ) -> ListPlaybackConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_prefetch_schedules"]
    ) -> ListPrefetchSchedulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_locations"]
    ) -> ListSourceLocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vod_sources"]
    ) -> ListVodSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/client/)
        """
