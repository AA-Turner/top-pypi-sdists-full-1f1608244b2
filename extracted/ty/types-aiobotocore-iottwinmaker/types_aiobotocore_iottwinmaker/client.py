"""
Type annotations for iottwinmaker service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_iottwinmaker.client import IoTTwinMakerClient

    session = get_session()
    async with session.create_client("iottwinmaker") as client:
        client: IoTTwinMakerClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchPutPropertyValuesRequestTypeDef,
    BatchPutPropertyValuesResponseTypeDef,
    CancelMetadataTransferJobRequestTypeDef,
    CancelMetadataTransferJobResponseTypeDef,
    CreateComponentTypeRequestTypeDef,
    CreateComponentTypeResponseTypeDef,
    CreateEntityRequestTypeDef,
    CreateEntityResponseTypeDef,
    CreateMetadataTransferJobRequestTypeDef,
    CreateMetadataTransferJobResponseTypeDef,
    CreateSceneRequestTypeDef,
    CreateSceneResponseTypeDef,
    CreateSyncJobRequestTypeDef,
    CreateSyncJobResponseTypeDef,
    CreateWorkspaceRequestTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteComponentTypeRequestTypeDef,
    DeleteComponentTypeResponseTypeDef,
    DeleteEntityRequestTypeDef,
    DeleteEntityResponseTypeDef,
    DeleteSceneRequestTypeDef,
    DeleteSyncJobRequestTypeDef,
    DeleteSyncJobResponseTypeDef,
    DeleteWorkspaceRequestTypeDef,
    DeleteWorkspaceResponseTypeDef,
    ExecuteQueryRequestTypeDef,
    ExecuteQueryResponseTypeDef,
    GetComponentTypeRequestTypeDef,
    GetComponentTypeResponseTypeDef,
    GetEntityRequestTypeDef,
    GetEntityResponseTypeDef,
    GetMetadataTransferJobRequestTypeDef,
    GetMetadataTransferJobResponseTypeDef,
    GetPricingPlanResponseTypeDef,
    GetPropertyValueHistoryRequestTypeDef,
    GetPropertyValueHistoryResponseTypeDef,
    GetPropertyValueRequestTypeDef,
    GetPropertyValueResponseTypeDef,
    GetSceneRequestTypeDef,
    GetSceneResponseTypeDef,
    GetSyncJobRequestTypeDef,
    GetSyncJobResponseTypeDef,
    GetWorkspaceRequestTypeDef,
    GetWorkspaceResponseTypeDef,
    ListComponentsRequestTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentTypesRequestTypeDef,
    ListComponentTypesResponseTypeDef,
    ListEntitiesRequestTypeDef,
    ListEntitiesResponseTypeDef,
    ListMetadataTransferJobsRequestTypeDef,
    ListMetadataTransferJobsResponseTypeDef,
    ListPropertiesRequestTypeDef,
    ListPropertiesResponseTypeDef,
    ListScenesRequestTypeDef,
    ListScenesResponseTypeDef,
    ListSyncJobsRequestTypeDef,
    ListSyncJobsResponseTypeDef,
    ListSyncResourcesRequestTypeDef,
    ListSyncResourcesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspacesRequestTypeDef,
    ListWorkspacesResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateComponentTypeRequestTypeDef,
    UpdateComponentTypeResponseTypeDef,
    UpdateEntityRequestTypeDef,
    UpdateEntityResponseTypeDef,
    UpdatePricingPlanRequestTypeDef,
    UpdatePricingPlanResponseTypeDef,
    UpdateSceneRequestTypeDef,
    UpdateSceneResponseTypeDef,
    UpdateWorkspaceRequestTypeDef,
    UpdateWorkspaceResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Self, Unpack
else:
    from typing_extensions import Self, Unpack


__all__ = ("IoTTwinMakerClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConnectorFailureException: Type[BotocoreClientError]
    ConnectorTimeoutException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    QueryTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTTwinMakerClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html#IoTTwinMaker.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTTwinMakerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html#IoTTwinMaker.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#generate_presigned_url)
        """

    async def batch_put_property_values(
        self, **kwargs: Unpack[BatchPutPropertyValuesRequestTypeDef]
    ) -> BatchPutPropertyValuesResponseTypeDef:
        """
        Sets values for multiple time series properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/batch_put_property_values.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#batch_put_property_values)
        """

    async def cancel_metadata_transfer_job(
        self, **kwargs: Unpack[CancelMetadataTransferJobRequestTypeDef]
    ) -> CancelMetadataTransferJobResponseTypeDef:
        """
        Cancels the metadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/cancel_metadata_transfer_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#cancel_metadata_transfer_job)
        """

    async def create_component_type(
        self, **kwargs: Unpack[CreateComponentTypeRequestTypeDef]
    ) -> CreateComponentTypeResponseTypeDef:
        """
        Creates a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_component_type.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_component_type)
        """

    async def create_entity(
        self, **kwargs: Unpack[CreateEntityRequestTypeDef]
    ) -> CreateEntityResponseTypeDef:
        """
        Creates an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_entity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_entity)
        """

    async def create_metadata_transfer_job(
        self, **kwargs: Unpack[CreateMetadataTransferJobRequestTypeDef]
    ) -> CreateMetadataTransferJobResponseTypeDef:
        """
        Creates a new metadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_metadata_transfer_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_metadata_transfer_job)
        """

    async def create_scene(
        self, **kwargs: Unpack[CreateSceneRequestTypeDef]
    ) -> CreateSceneResponseTypeDef:
        """
        Creates a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_scene.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_scene)
        """

    async def create_sync_job(
        self, **kwargs: Unpack[CreateSyncJobRequestTypeDef]
    ) -> CreateSyncJobResponseTypeDef:
        """
        This action creates a SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_sync_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_sync_job)
        """

    async def create_workspace(
        self, **kwargs: Unpack[CreateWorkspaceRequestTypeDef]
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a workplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/create_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#create_workspace)
        """

    async def delete_component_type(
        self, **kwargs: Unpack[DeleteComponentTypeRequestTypeDef]
    ) -> DeleteComponentTypeResponseTypeDef:
        """
        Deletes a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/delete_component_type.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#delete_component_type)
        """

    async def delete_entity(
        self, **kwargs: Unpack[DeleteEntityRequestTypeDef]
    ) -> DeleteEntityResponseTypeDef:
        """
        Deletes an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/delete_entity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#delete_entity)
        """

    async def delete_scene(self, **kwargs: Unpack[DeleteSceneRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/delete_scene.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#delete_scene)
        """

    async def delete_sync_job(
        self, **kwargs: Unpack[DeleteSyncJobRequestTypeDef]
    ) -> DeleteSyncJobResponseTypeDef:
        """
        Delete the SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/delete_sync_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#delete_sync_job)
        """

    async def delete_workspace(
        self, **kwargs: Unpack[DeleteWorkspaceRequestTypeDef]
    ) -> DeleteWorkspaceResponseTypeDef:
        """
        Deletes a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/delete_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#delete_workspace)
        """

    async def execute_query(
        self, **kwargs: Unpack[ExecuteQueryRequestTypeDef]
    ) -> ExecuteQueryResponseTypeDef:
        """
        Run queries to access information from your knowledge graph of entities within
        individual workspaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/execute_query.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#execute_query)
        """

    async def get_component_type(
        self, **kwargs: Unpack[GetComponentTypeRequestTypeDef]
    ) -> GetComponentTypeResponseTypeDef:
        """
        Retrieves information about a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_component_type.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_component_type)
        """

    async def get_entity(
        self, **kwargs: Unpack[GetEntityRequestTypeDef]
    ) -> GetEntityResponseTypeDef:
        """
        Retrieves information about an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_entity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_entity)
        """

    async def get_metadata_transfer_job(
        self, **kwargs: Unpack[GetMetadataTransferJobRequestTypeDef]
    ) -> GetMetadataTransferJobResponseTypeDef:
        """
        Gets a nmetadata transfer job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_metadata_transfer_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_metadata_transfer_job)
        """

    async def get_pricing_plan(self) -> GetPricingPlanResponseTypeDef:
        """
        Gets the pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_pricing_plan.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_pricing_plan)
        """

    async def get_property_value(
        self, **kwargs: Unpack[GetPropertyValueRequestTypeDef]
    ) -> GetPropertyValueResponseTypeDef:
        """
        Gets the property values for a component, component type, entity, or workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_property_value.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_property_value)
        """

    async def get_property_value_history(
        self, **kwargs: Unpack[GetPropertyValueHistoryRequestTypeDef]
    ) -> GetPropertyValueHistoryResponseTypeDef:
        """
        Retrieves information about the history of a time series property value for a
        component, component type, entity, or workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_property_value_history.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_property_value_history)
        """

    async def get_scene(self, **kwargs: Unpack[GetSceneRequestTypeDef]) -> GetSceneResponseTypeDef:
        """
        Retrieves information about a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_scene.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_scene)
        """

    async def get_sync_job(
        self, **kwargs: Unpack[GetSyncJobRequestTypeDef]
    ) -> GetSyncJobResponseTypeDef:
        """
        Gets the SyncJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_sync_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_sync_job)
        """

    async def get_workspace(
        self, **kwargs: Unpack[GetWorkspaceRequestTypeDef]
    ) -> GetWorkspaceResponseTypeDef:
        """
        Retrieves information about a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/get_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#get_workspace)
        """

    async def list_component_types(
        self, **kwargs: Unpack[ListComponentTypesRequestTypeDef]
    ) -> ListComponentTypesResponseTypeDef:
        """
        Lists all component types in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_component_types.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_component_types)
        """

    async def list_components(
        self, **kwargs: Unpack[ListComponentsRequestTypeDef]
    ) -> ListComponentsResponseTypeDef:
        """
        This API lists the components of an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_components.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_components)
        """

    async def list_entities(
        self, **kwargs: Unpack[ListEntitiesRequestTypeDef]
    ) -> ListEntitiesResponseTypeDef:
        """
        Lists all entities in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_entities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_entities)
        """

    async def list_metadata_transfer_jobs(
        self, **kwargs: Unpack[ListMetadataTransferJobsRequestTypeDef]
    ) -> ListMetadataTransferJobsResponseTypeDef:
        """
        Lists the metadata transfer jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_metadata_transfer_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_metadata_transfer_jobs)
        """

    async def list_properties(
        self, **kwargs: Unpack[ListPropertiesRequestTypeDef]
    ) -> ListPropertiesResponseTypeDef:
        """
        This API lists the properties of a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_properties.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_properties)
        """

    async def list_scenes(
        self, **kwargs: Unpack[ListScenesRequestTypeDef]
    ) -> ListScenesResponseTypeDef:
        """
        Lists all scenes in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_scenes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_scenes)
        """

    async def list_sync_jobs(
        self, **kwargs: Unpack[ListSyncJobsRequestTypeDef]
    ) -> ListSyncJobsResponseTypeDef:
        """
        List all SyncJobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_sync_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_sync_jobs)
        """

    async def list_sync_resources(
        self, **kwargs: Unpack[ListSyncResourcesRequestTypeDef]
    ) -> ListSyncResourcesResponseTypeDef:
        """
        Lists the sync resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_sync_resources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_sync_resources)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_tags_for_resource)
        """

    async def list_workspaces(
        self, **kwargs: Unpack[ListWorkspacesRequestTypeDef]
    ) -> ListWorkspacesResponseTypeDef:
        """
        Retrieves information about workspaces in the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/list_workspaces.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#list_workspaces)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#untag_resource)
        """

    async def update_component_type(
        self, **kwargs: Unpack[UpdateComponentTypeRequestTypeDef]
    ) -> UpdateComponentTypeResponseTypeDef:
        """
        Updates information in a component type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/update_component_type.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#update_component_type)
        """

    async def update_entity(
        self, **kwargs: Unpack[UpdateEntityRequestTypeDef]
    ) -> UpdateEntityResponseTypeDef:
        """
        Updates an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/update_entity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#update_entity)
        """

    async def update_pricing_plan(
        self, **kwargs: Unpack[UpdatePricingPlanRequestTypeDef]
    ) -> UpdatePricingPlanResponseTypeDef:
        """
        Update the pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/update_pricing_plan.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#update_pricing_plan)
        """

    async def update_scene(
        self, **kwargs: Unpack[UpdateSceneRequestTypeDef]
    ) -> UpdateSceneResponseTypeDef:
        """
        Updates a scene.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/update_scene.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#update_scene)
        """

    async def update_workspace(
        self, **kwargs: Unpack[UpdateWorkspaceRequestTypeDef]
    ) -> UpdateWorkspaceResponseTypeDef:
        """
        Updates a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker/client/update_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/#update_workspace)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html#IoTTwinMaker.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html#IoTTwinMaker.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/client/)
        """
