"""
Type annotations for codeconnections service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_codeconnections.client import CodeConnectionsClient

    session = get_session()
    async with session.create_client("codeconnections") as client:
        client: CodeConnectionsClient
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
    CreateConnectionInputTypeDef,
    CreateConnectionOutputTypeDef,
    CreateHostInputTypeDef,
    CreateHostOutputTypeDef,
    CreateRepositoryLinkInputTypeDef,
    CreateRepositoryLinkOutputTypeDef,
    CreateSyncConfigurationInputTypeDef,
    CreateSyncConfigurationOutputTypeDef,
    DeleteConnectionInputTypeDef,
    DeleteHostInputTypeDef,
    DeleteRepositoryLinkInputTypeDef,
    DeleteSyncConfigurationInputTypeDef,
    GetConnectionInputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostInputTypeDef,
    GetHostOutputTypeDef,
    GetRepositoryLinkInputTypeDef,
    GetRepositoryLinkOutputTypeDef,
    GetRepositorySyncStatusInputTypeDef,
    GetRepositorySyncStatusOutputTypeDef,
    GetResourceSyncStatusInputTypeDef,
    GetResourceSyncStatusOutputTypeDef,
    GetSyncBlockerSummaryInputTypeDef,
    GetSyncBlockerSummaryOutputTypeDef,
    GetSyncConfigurationInputTypeDef,
    GetSyncConfigurationOutputTypeDef,
    ListConnectionsInputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsInputTypeDef,
    ListHostsOutputTypeDef,
    ListRepositoryLinksInputTypeDef,
    ListRepositoryLinksOutputTypeDef,
    ListRepositorySyncDefinitionsInputTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListSyncConfigurationsInputTypeDef,
    ListSyncConfigurationsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateHostInputTypeDef,
    UpdateRepositoryLinkInputTypeDef,
    UpdateRepositoryLinkOutputTypeDef,
    UpdateSyncBlockerInputTypeDef,
    UpdateSyncBlockerOutputTypeDef,
    UpdateSyncConfigurationInputTypeDef,
    UpdateSyncConfigurationOutputTypeDef,
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

__all__ = ("CodeConnectionsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConditionalCheckFailedException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    RetryLatestCommitFailedException: Type[BotocoreClientError]
    SyncBlockerDoesNotExistException: Type[BotocoreClientError]
    SyncConfigurationStillExistsException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedProviderTypeException: Type[BotocoreClientError]
    UpdateOutOfSyncException: Type[BotocoreClientError]

class CodeConnectionsClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections.html#CodeConnections.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeConnectionsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections.html#CodeConnections.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#generate_presigned_url)
        """

    async def create_connection(
        self, **kwargs: Unpack[CreateConnectionInputTypeDef]
    ) -> CreateConnectionOutputTypeDef:
        """
        Creates a connection that can then be given to other Amazon Web Services
        services like CodePipeline so that it can access third-party code repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/create_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#create_connection)
        """

    async def create_host(
        self, **kwargs: Unpack[CreateHostInputTypeDef]
    ) -> CreateHostOutputTypeDef:
        """
        Creates a resource that represents the infrastructure where a third-party
        provider is installed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/create_host.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#create_host)
        """

    async def create_repository_link(
        self, **kwargs: Unpack[CreateRepositoryLinkInputTypeDef]
    ) -> CreateRepositoryLinkOutputTypeDef:
        """
        Creates a link to a specified external Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/create_repository_link.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#create_repository_link)
        """

    async def create_sync_configuration(
        self, **kwargs: Unpack[CreateSyncConfigurationInputTypeDef]
    ) -> CreateSyncConfigurationOutputTypeDef:
        """
        Creates a sync configuration which allows Amazon Web Services to sync content
        from a Git repository to update a specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/create_sync_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#create_sync_configuration)
        """

    async def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        The connection to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/delete_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#delete_connection)
        """

    async def delete_host(self, **kwargs: Unpack[DeleteHostInputTypeDef]) -> Dict[str, Any]:
        """
        The host to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/delete_host.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#delete_host)
        """

    async def delete_repository_link(
        self, **kwargs: Unpack[DeleteRepositoryLinkInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/delete_repository_link.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#delete_repository_link)
        """

    async def delete_sync_configuration(
        self, **kwargs: Unpack[DeleteSyncConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the sync configuration for a specified repository and connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/delete_sync_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#delete_sync_configuration)
        """

    async def get_connection(
        self, **kwargs: Unpack[GetConnectionInputTypeDef]
    ) -> GetConnectionOutputTypeDef:
        """
        Returns the connection ARN and details such as status, owner, and provider type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_connection)
        """

    async def get_host(self, **kwargs: Unpack[GetHostInputTypeDef]) -> GetHostOutputTypeDef:
        """
        Returns the host ARN and details such as status, provider type, endpoint, and,
        if applicable, the VPC configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_host.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_host)
        """

    async def get_repository_link(
        self, **kwargs: Unpack[GetRepositoryLinkInputTypeDef]
    ) -> GetRepositoryLinkOutputTypeDef:
        """
        Returns details about a repository link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_repository_link.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_repository_link)
        """

    async def get_repository_sync_status(
        self, **kwargs: Unpack[GetRepositorySyncStatusInputTypeDef]
    ) -> GetRepositorySyncStatusOutputTypeDef:
        """
        Returns details about the sync status for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_repository_sync_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_repository_sync_status)
        """

    async def get_resource_sync_status(
        self, **kwargs: Unpack[GetResourceSyncStatusInputTypeDef]
    ) -> GetResourceSyncStatusOutputTypeDef:
        """
        Returns the status of the sync with the Git repository for a specific Amazon
        Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_resource_sync_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_resource_sync_status)
        """

    async def get_sync_blocker_summary(
        self, **kwargs: Unpack[GetSyncBlockerSummaryInputTypeDef]
    ) -> GetSyncBlockerSummaryOutputTypeDef:
        """
        Returns a list of the most recent sync blockers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_sync_blocker_summary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_sync_blocker_summary)
        """

    async def get_sync_configuration(
        self, **kwargs: Unpack[GetSyncConfigurationInputTypeDef]
    ) -> GetSyncConfigurationOutputTypeDef:
        """
        Returns details about a sync configuration, including the sync type and
        resource name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/get_sync_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#get_sync_configuration)
        """

    async def list_connections(
        self, **kwargs: Unpack[ListConnectionsInputTypeDef]
    ) -> ListConnectionsOutputTypeDef:
        """
        Lists the connections associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_connections.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_connections)
        """

    async def list_hosts(self, **kwargs: Unpack[ListHostsInputTypeDef]) -> ListHostsOutputTypeDef:
        """
        Lists the hosts associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_hosts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_hosts)
        """

    async def list_repository_links(
        self, **kwargs: Unpack[ListRepositoryLinksInputTypeDef]
    ) -> ListRepositoryLinksOutputTypeDef:
        """
        Lists the repository links created for connections in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_repository_links.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_repository_links)
        """

    async def list_repository_sync_definitions(
        self, **kwargs: Unpack[ListRepositorySyncDefinitionsInputTypeDef]
    ) -> ListRepositorySyncDefinitionsOutputTypeDef:
        """
        Lists the repository sync definitions for repository links in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_repository_sync_definitions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_repository_sync_definitions)
        """

    async def list_sync_configurations(
        self, **kwargs: Unpack[ListSyncConfigurationsInputTypeDef]
    ) -> ListSyncConfigurationsOutputTypeDef:
        """
        Returns a list of sync configurations for a specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_sync_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_sync_configurations)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#list_tags_for_resource)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#untag_resource)
        """

    async def update_host(self, **kwargs: Unpack[UpdateHostInputTypeDef]) -> Dict[str, Any]:
        """
        Updates a specified host with the provided configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/update_host.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#update_host)
        """

    async def update_repository_link(
        self, **kwargs: Unpack[UpdateRepositoryLinkInputTypeDef]
    ) -> UpdateRepositoryLinkOutputTypeDef:
        """
        Updates the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/update_repository_link.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#update_repository_link)
        """

    async def update_sync_blocker(
        self, **kwargs: Unpack[UpdateSyncBlockerInputTypeDef]
    ) -> UpdateSyncBlockerOutputTypeDef:
        """
        Allows you to update the status of a sync blocker, resolving the blocker and
        allowing syncing to continue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/update_sync_blocker.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#update_sync_blocker)
        """

    async def update_sync_configuration(
        self, **kwargs: Unpack[UpdateSyncConfigurationInputTypeDef]
    ) -> UpdateSyncConfigurationOutputTypeDef:
        """
        Updates the sync configuration for your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections/client/update_sync_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/#update_sync_configuration)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections.html#CodeConnections.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeconnections.html#CodeConnections.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/client/)
        """
