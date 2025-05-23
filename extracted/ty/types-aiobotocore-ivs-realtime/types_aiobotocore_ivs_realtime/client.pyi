"""
Type annotations for ivs-realtime service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient

    session = get_session()
    async with session.create_client("ivs-realtime") as client:
        client: IvsrealtimeClient
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

from .paginator import ListIngestConfigurationsPaginator, ListPublicKeysPaginator
from .type_defs import (
    CreateEncoderConfigurationRequestTypeDef,
    CreateEncoderConfigurationResponseTypeDef,
    CreateIngestConfigurationRequestTypeDef,
    CreateIngestConfigurationResponseTypeDef,
    CreateParticipantTokenRequestTypeDef,
    CreateParticipantTokenResponseTypeDef,
    CreateStageRequestTypeDef,
    CreateStageResponseTypeDef,
    CreateStorageConfigurationRequestTypeDef,
    CreateStorageConfigurationResponseTypeDef,
    DeleteEncoderConfigurationRequestTypeDef,
    DeleteIngestConfigurationRequestTypeDef,
    DeletePublicKeyRequestTypeDef,
    DeleteStageRequestTypeDef,
    DeleteStorageConfigurationRequestTypeDef,
    DisconnectParticipantRequestTypeDef,
    GetCompositionRequestTypeDef,
    GetCompositionResponseTypeDef,
    GetEncoderConfigurationRequestTypeDef,
    GetEncoderConfigurationResponseTypeDef,
    GetIngestConfigurationRequestTypeDef,
    GetIngestConfigurationResponseTypeDef,
    GetParticipantRequestTypeDef,
    GetParticipantResponseTypeDef,
    GetPublicKeyRequestTypeDef,
    GetPublicKeyResponseTypeDef,
    GetStageRequestTypeDef,
    GetStageResponseTypeDef,
    GetStageSessionRequestTypeDef,
    GetStageSessionResponseTypeDef,
    GetStorageConfigurationRequestTypeDef,
    GetStorageConfigurationResponseTypeDef,
    ImportPublicKeyRequestTypeDef,
    ImportPublicKeyResponseTypeDef,
    ListCompositionsRequestTypeDef,
    ListCompositionsResponseTypeDef,
    ListEncoderConfigurationsRequestTypeDef,
    ListEncoderConfigurationsResponseTypeDef,
    ListIngestConfigurationsRequestTypeDef,
    ListIngestConfigurationsResponseTypeDef,
    ListParticipantEventsRequestTypeDef,
    ListParticipantEventsResponseTypeDef,
    ListParticipantsRequestTypeDef,
    ListParticipantsResponseTypeDef,
    ListPublicKeysRequestTypeDef,
    ListPublicKeysResponseTypeDef,
    ListStageSessionsRequestTypeDef,
    ListStageSessionsResponseTypeDef,
    ListStagesRequestTypeDef,
    ListStagesResponseTypeDef,
    ListStorageConfigurationsRequestTypeDef,
    ListStorageConfigurationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartCompositionRequestTypeDef,
    StartCompositionResponseTypeDef,
    StopCompositionRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateIngestConfigurationRequestTypeDef,
    UpdateIngestConfigurationResponseTypeDef,
    UpdateStageRequestTypeDef,
    UpdateStageResponseTypeDef,
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

__all__ = ("IvsrealtimeClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IvsrealtimeClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime.html#Ivsrealtime.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IvsrealtimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime.html#Ivsrealtime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#generate_presigned_url)
        """

    async def create_encoder_configuration(
        self, **kwargs: Unpack[CreateEncoderConfigurationRequestTypeDef]
    ) -> CreateEncoderConfigurationResponseTypeDef:
        """
        Creates an EncoderConfiguration object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/create_encoder_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#create_encoder_configuration)
        """

    async def create_ingest_configuration(
        self, **kwargs: Unpack[CreateIngestConfigurationRequestTypeDef]
    ) -> CreateIngestConfigurationResponseTypeDef:
        """
        Creates a new IngestConfiguration resource, used to specify the ingest protocol
        for a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/create_ingest_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#create_ingest_configuration)
        """

    async def create_participant_token(
        self, **kwargs: Unpack[CreateParticipantTokenRequestTypeDef]
    ) -> CreateParticipantTokenResponseTypeDef:
        """
        Creates an additional token for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/create_participant_token.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#create_participant_token)
        """

    async def create_stage(
        self, **kwargs: Unpack[CreateStageRequestTypeDef]
    ) -> CreateStageResponseTypeDef:
        """
        Creates a new stage (and optionally participant tokens).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/create_stage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#create_stage)
        """

    async def create_storage_configuration(
        self, **kwargs: Unpack[CreateStorageConfigurationRequestTypeDef]
    ) -> CreateStorageConfigurationResponseTypeDef:
        """
        Creates a new storage configuration, used to enable recording to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/create_storage_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#create_storage_configuration)
        """

    async def delete_encoder_configuration(
        self, **kwargs: Unpack[DeleteEncoderConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/delete_encoder_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#delete_encoder_configuration)
        """

    async def delete_ingest_configuration(
        self, **kwargs: Unpack[DeleteIngestConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified IngestConfiguration, so it can no longer be used to
        broadcast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/delete_ingest_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#delete_ingest_configuration)
        """

    async def delete_public_key(
        self, **kwargs: Unpack[DeletePublicKeyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified public key used to sign stage participant tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/delete_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#delete_public_key)
        """

    async def delete_stage(self, **kwargs: Unpack[DeleteStageRequestTypeDef]) -> Dict[str, Any]:
        """
        Shuts down and deletes the specified stage (disconnecting all participants).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/delete_stage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#delete_stage)
        """

    async def delete_storage_configuration(
        self, **kwargs: Unpack[DeleteStorageConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/delete_storage_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#delete_storage_configuration)
        """

    async def disconnect_participant(
        self, **kwargs: Unpack[DisconnectParticipantRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disconnects a specified participant from a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/disconnect_participant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#disconnect_participant)
        """

    async def get_composition(
        self, **kwargs: Unpack[GetCompositionRequestTypeDef]
    ) -> GetCompositionResponseTypeDef:
        """
        Get information about the specified Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_composition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_composition)
        """

    async def get_encoder_configuration(
        self, **kwargs: Unpack[GetEncoderConfigurationRequestTypeDef]
    ) -> GetEncoderConfigurationResponseTypeDef:
        """
        Gets information about the specified EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_encoder_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_encoder_configuration)
        """

    async def get_ingest_configuration(
        self, **kwargs: Unpack[GetIngestConfigurationRequestTypeDef]
    ) -> GetIngestConfigurationResponseTypeDef:
        """
        Gets information about the specified IngestConfiguration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_ingest_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_ingest_configuration)
        """

    async def get_participant(
        self, **kwargs: Unpack[GetParticipantRequestTypeDef]
    ) -> GetParticipantResponseTypeDef:
        """
        Gets information about the specified participant token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_participant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_participant)
        """

    async def get_public_key(
        self, **kwargs: Unpack[GetPublicKeyRequestTypeDef]
    ) -> GetPublicKeyResponseTypeDef:
        """
        Gets information for the specified public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_public_key)
        """

    async def get_stage(self, **kwargs: Unpack[GetStageRequestTypeDef]) -> GetStageResponseTypeDef:
        """
        Gets information for the specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_stage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_stage)
        """

    async def get_stage_session(
        self, **kwargs: Unpack[GetStageSessionRequestTypeDef]
    ) -> GetStageSessionResponseTypeDef:
        """
        Gets information for the specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_stage_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_stage_session)
        """

    async def get_storage_configuration(
        self, **kwargs: Unpack[GetStorageConfigurationRequestTypeDef]
    ) -> GetStorageConfigurationResponseTypeDef:
        """
        Gets the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_storage_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_storage_configuration)
        """

    async def import_public_key(
        self, **kwargs: Unpack[ImportPublicKeyRequestTypeDef]
    ) -> ImportPublicKeyResponseTypeDef:
        """
        Import a public key to be used for signing stage participant tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/import_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#import_public_key)
        """

    async def list_compositions(
        self, **kwargs: Unpack[ListCompositionsRequestTypeDef]
    ) -> ListCompositionsResponseTypeDef:
        """
        Gets summary information about all Compositions in your account, in the AWS
        region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_compositions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_compositions)
        """

    async def list_encoder_configurations(
        self, **kwargs: Unpack[ListEncoderConfigurationsRequestTypeDef]
    ) -> ListEncoderConfigurationsResponseTypeDef:
        """
        Gets summary information about all EncoderConfigurations in your account, in
        the AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_encoder_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_encoder_configurations)
        """

    async def list_ingest_configurations(
        self, **kwargs: Unpack[ListIngestConfigurationsRequestTypeDef]
    ) -> ListIngestConfigurationsResponseTypeDef:
        """
        Lists all IngestConfigurations in your account, in the AWS region where the API
        request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_ingest_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_ingest_configurations)
        """

    async def list_participant_events(
        self, **kwargs: Unpack[ListParticipantEventsRequestTypeDef]
    ) -> ListParticipantEventsResponseTypeDef:
        """
        Lists events for a specified participant that occurred during a specified stage
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_participant_events.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_participant_events)
        """

    async def list_participants(
        self, **kwargs: Unpack[ListParticipantsRequestTypeDef]
    ) -> ListParticipantsResponseTypeDef:
        """
        Lists all participants in a specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_participants.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_participants)
        """

    async def list_public_keys(
        self, **kwargs: Unpack[ListPublicKeysRequestTypeDef]
    ) -> ListPublicKeysResponseTypeDef:
        """
        Gets summary information about all public keys in your account, in the AWS
        region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_public_keys.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_public_keys)
        """

    async def list_stage_sessions(
        self, **kwargs: Unpack[ListStageSessionsRequestTypeDef]
    ) -> ListStageSessionsResponseTypeDef:
        """
        Gets all sessions for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_stage_sessions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_stage_sessions)
        """

    async def list_stages(
        self, **kwargs: Unpack[ListStagesRequestTypeDef]
    ) -> ListStagesResponseTypeDef:
        """
        Gets summary information about all stages in your account, in the AWS region
        where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_stages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_stages)
        """

    async def list_storage_configurations(
        self, **kwargs: Unpack[ListStorageConfigurationsRequestTypeDef]
    ) -> ListStorageConfigurationsResponseTypeDef:
        """
        Gets summary information about all storage configurations in your account, in
        the AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_storage_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_storage_configurations)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#list_tags_for_resource)
        """

    async def start_composition(
        self, **kwargs: Unpack[StartCompositionRequestTypeDef]
    ) -> StartCompositionResponseTypeDef:
        """
        Starts a Composition from a stage based on the configuration provided in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/start_composition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#start_composition)
        """

    async def stop_composition(
        self, **kwargs: Unpack[StopCompositionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops and deletes a Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/stop_composition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#stop_composition)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for the AWS resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#untag_resource)
        """

    async def update_ingest_configuration(
        self, **kwargs: Unpack[UpdateIngestConfigurationRequestTypeDef]
    ) -> UpdateIngestConfigurationResponseTypeDef:
        """
        Updates a specified IngestConfiguration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/update_ingest_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#update_ingest_configuration)
        """

    async def update_stage(
        self, **kwargs: Unpack[UpdateStageRequestTypeDef]
    ) -> UpdateStageResponseTypeDef:
        """
        Updates a stage's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/update_stage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#update_stage)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ingest_configurations"]
    ) -> ListIngestConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_public_keys"]
    ) -> ListPublicKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime.html#Ivsrealtime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime.html#Ivsrealtime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/client/)
        """
