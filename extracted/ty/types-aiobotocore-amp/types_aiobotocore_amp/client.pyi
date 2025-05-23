"""
Type annotations for amp service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_amp.client import PrometheusServiceClient

    session = get_session()
    async with session.create_client("amp") as client:
        client: PrometheusServiceClient
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
    ListRuleGroupsNamespacesPaginator,
    ListScrapersPaginator,
    ListWorkspacesPaginator,
)
from .type_defs import (
    CreateAlertManagerDefinitionRequestTypeDef,
    CreateAlertManagerDefinitionResponseTypeDef,
    CreateLoggingConfigurationRequestTypeDef,
    CreateLoggingConfigurationResponseTypeDef,
    CreateRuleGroupsNamespaceRequestTypeDef,
    CreateRuleGroupsNamespaceResponseTypeDef,
    CreateScraperRequestTypeDef,
    CreateScraperResponseTypeDef,
    CreateWorkspaceRequestTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteAlertManagerDefinitionRequestTypeDef,
    DeleteLoggingConfigurationRequestTypeDef,
    DeleteRuleGroupsNamespaceRequestTypeDef,
    DeleteScraperRequestTypeDef,
    DeleteScraperResponseTypeDef,
    DeleteWorkspaceRequestTypeDef,
    DescribeAlertManagerDefinitionRequestTypeDef,
    DescribeAlertManagerDefinitionResponseTypeDef,
    DescribeLoggingConfigurationRequestTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeRuleGroupsNamespaceRequestTypeDef,
    DescribeRuleGroupsNamespaceResponseTypeDef,
    DescribeScraperRequestTypeDef,
    DescribeScraperResponseTypeDef,
    DescribeWorkspaceRequestTypeDef,
    DescribeWorkspaceResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDefaultScraperConfigurationResponseTypeDef,
    ListRuleGroupsNamespacesRequestTypeDef,
    ListRuleGroupsNamespacesResponseTypeDef,
    ListScrapersRequestTypeDef,
    ListScrapersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspacesRequestTypeDef,
    ListWorkspacesResponseTypeDef,
    PutAlertManagerDefinitionRequestTypeDef,
    PutAlertManagerDefinitionResponseTypeDef,
    PutRuleGroupsNamespaceRequestTypeDef,
    PutRuleGroupsNamespaceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLoggingConfigurationRequestTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateScraperRequestTypeDef,
    UpdateScraperResponseTypeDef,
    UpdateWorkspaceAliasRequestTypeDef,
)
from .waiter import (
    ScraperActiveWaiter,
    ScraperDeletedWaiter,
    WorkspaceActiveWaiter,
    WorkspaceDeletedWaiter,
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

__all__ = ("PrometheusServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PrometheusServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrometheusServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#generate_presigned_url)
        """

    async def create_alert_manager_definition(
        self, **kwargs: Unpack[CreateAlertManagerDefinitionRequestTypeDef]
    ) -> CreateAlertManagerDefinitionResponseTypeDef:
        """
        The <code>CreateAlertManagerDefinition</code> operation creates the alert
        manager definition in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/create_alert_manager_definition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_alert_manager_definition)
        """

    async def create_logging_configuration(
        self, **kwargs: Unpack[CreateLoggingConfigurationRequestTypeDef]
    ) -> CreateLoggingConfigurationResponseTypeDef:
        """
        The <code>CreateLoggingConfiguration</code> operation creates a logging
        configuration for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/create_logging_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_logging_configuration)
        """

    async def create_rule_groups_namespace(
        self, **kwargs: Unpack[CreateRuleGroupsNamespaceRequestTypeDef]
    ) -> CreateRuleGroupsNamespaceResponseTypeDef:
        """
        The <code>CreateRuleGroupsNamespace</code> operation creates a rule groups
        namespace within a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/create_rule_groups_namespace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_rule_groups_namespace)
        """

    async def create_scraper(
        self, **kwargs: Unpack[CreateScraperRequestTypeDef]
    ) -> CreateScraperResponseTypeDef:
        """
        The <code>CreateScraper</code> operation creates a scraper to collect metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/create_scraper.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_scraper)
        """

    async def create_workspace(
        self, **kwargs: Unpack[CreateWorkspaceRequestTypeDef]
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a Prometheus workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/create_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_workspace)
        """

    async def delete_alert_manager_definition(
        self, **kwargs: Unpack[DeleteAlertManagerDefinitionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the alert manager definition from a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/delete_alert_manager_definition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_alert_manager_definition)
        """

    async def delete_logging_configuration(
        self, **kwargs: Unpack[DeleteLoggingConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the logging configuration for a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/delete_logging_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_logging_configuration)
        """

    async def delete_rule_groups_namespace(
        self, **kwargs: Unpack[DeleteRuleGroupsNamespaceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes one rule groups namespace and its associated rule groups definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/delete_rule_groups_namespace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_rule_groups_namespace)
        """

    async def delete_scraper(
        self, **kwargs: Unpack[DeleteScraperRequestTypeDef]
    ) -> DeleteScraperResponseTypeDef:
        """
        The <code>DeleteScraper</code> operation deletes one scraper, and stops any
        metrics collection that the scraper performs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/delete_scraper.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_scraper)
        """

    async def delete_workspace(
        self, **kwargs: Unpack[DeleteWorkspaceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/delete_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_workspace)
        """

    async def describe_alert_manager_definition(
        self, **kwargs: Unpack[DescribeAlertManagerDefinitionRequestTypeDef]
    ) -> DescribeAlertManagerDefinitionResponseTypeDef:
        """
        Retrieves the full information about the alert manager definition for a
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/describe_alert_manager_definition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_alert_manager_definition)
        """

    async def describe_logging_configuration(
        self, **kwargs: Unpack[DescribeLoggingConfigurationRequestTypeDef]
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Returns complete information about the current logging configuration of the
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/describe_logging_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_logging_configuration)
        """

    async def describe_rule_groups_namespace(
        self, **kwargs: Unpack[DescribeRuleGroupsNamespaceRequestTypeDef]
    ) -> DescribeRuleGroupsNamespaceResponseTypeDef:
        """
        Returns complete information about one rule groups namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/describe_rule_groups_namespace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_rule_groups_namespace)
        """

    async def describe_scraper(
        self, **kwargs: Unpack[DescribeScraperRequestTypeDef]
    ) -> DescribeScraperResponseTypeDef:
        """
        The <code>DescribeScraper</code> operation displays information about an
        existing scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/describe_scraper.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_scraper)
        """

    async def describe_workspace(
        self, **kwargs: Unpack[DescribeWorkspaceRequestTypeDef]
    ) -> DescribeWorkspaceResponseTypeDef:
        """
        Returns information about an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/describe_workspace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_workspace)
        """

    async def get_default_scraper_configuration(
        self,
    ) -> GetDefaultScraperConfigurationResponseTypeDef:
        """
        The <code>GetDefaultScraperConfiguration</code> operation returns the default
        scraper configuration used when Amazon EKS creates a scraper for you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_default_scraper_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_default_scraper_configuration)
        """

    async def list_rule_groups_namespaces(
        self, **kwargs: Unpack[ListRuleGroupsNamespacesRequestTypeDef]
    ) -> ListRuleGroupsNamespacesResponseTypeDef:
        """
        Returns a list of rule groups namespaces in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/list_rule_groups_namespaces.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_rule_groups_namespaces)
        """

    async def list_scrapers(
        self, **kwargs: Unpack[ListScrapersRequestTypeDef]
    ) -> ListScrapersResponseTypeDef:
        """
        The <code>ListScrapers</code> operation lists all of the scrapers in your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/list_scrapers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_scrapers)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        The <code>ListTagsForResource</code> operation returns the tags that are
        associated with an Amazon Managed Service for Prometheus resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_tags_for_resource)
        """

    async def list_workspaces(
        self, **kwargs: Unpack[ListWorkspacesRequestTypeDef]
    ) -> ListWorkspacesResponseTypeDef:
        """
        Lists all of the Amazon Managed Service for Prometheus workspaces in your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/list_workspaces.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_workspaces)
        """

    async def put_alert_manager_definition(
        self, **kwargs: Unpack[PutAlertManagerDefinitionRequestTypeDef]
    ) -> PutAlertManagerDefinitionResponseTypeDef:
        """
        Updates an existing alert manager definition in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/put_alert_manager_definition.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#put_alert_manager_definition)
        """

    async def put_rule_groups_namespace(
        self, **kwargs: Unpack[PutRuleGroupsNamespaceRequestTypeDef]
    ) -> PutRuleGroupsNamespaceResponseTypeDef:
        """
        Updates an existing rule groups namespace within a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/put_rule_groups_namespace.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#put_rule_groups_namespace)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        The <code>TagResource</code> operation associates tags with an Amazon Managed
        Service for Prometheus resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from an Amazon Managed Service for Prometheus
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#untag_resource)
        """

    async def update_logging_configuration(
        self, **kwargs: Unpack[UpdateLoggingConfigurationRequestTypeDef]
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Updates the log group ARN or the workspace ID of the current logging
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/update_logging_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#update_logging_configuration)
        """

    async def update_scraper(
        self, **kwargs: Unpack[UpdateScraperRequestTypeDef]
    ) -> UpdateScraperResponseTypeDef:
        """
        Updates an existing scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/update_scraper.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#update_scraper)
        """

    async def update_workspace_alias(
        self, **kwargs: Unpack[UpdateWorkspaceAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the alias of an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/update_workspace_alias.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#update_workspace_alias)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rule_groups_namespaces"]
    ) -> ListRuleGroupsNamespacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scrapers"]
    ) -> ListScrapersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workspaces"]
    ) -> ListWorkspacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["scraper_active"]
    ) -> ScraperActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["scraper_deleted"]
    ) -> ScraperDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["workspace_active"]
    ) -> WorkspaceActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["workspace_deleted"]
    ) -> WorkspaceDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
        """
