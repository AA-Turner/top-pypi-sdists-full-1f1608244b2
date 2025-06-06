"""
Type annotations for pca-connector-ad service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient

    session = get_session()
    async with session.create_client("pca-connector-ad") as client:
        client: PcaConnectorAdClient
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
    ListConnectorsPaginator,
    ListDirectoryRegistrationsPaginator,
    ListServicePrincipalNamesPaginator,
    ListTemplateGroupAccessControlEntriesPaginator,
    ListTemplatesPaginator,
)
from .type_defs import (
    CreateConnectorRequestTypeDef,
    CreateConnectorResponseTypeDef,
    CreateDirectoryRegistrationRequestTypeDef,
    CreateDirectoryRegistrationResponseTypeDef,
    CreateServicePrincipalNameRequestTypeDef,
    CreateTemplateGroupAccessControlEntryRequestTypeDef,
    CreateTemplateRequestTypeDef,
    CreateTemplateResponseTypeDef,
    DeleteConnectorRequestTypeDef,
    DeleteDirectoryRegistrationRequestTypeDef,
    DeleteServicePrincipalNameRequestTypeDef,
    DeleteTemplateGroupAccessControlEntryRequestTypeDef,
    DeleteTemplateRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetConnectorRequestTypeDef,
    GetConnectorResponseTypeDef,
    GetDirectoryRegistrationRequestTypeDef,
    GetDirectoryRegistrationResponseTypeDef,
    GetServicePrincipalNameRequestTypeDef,
    GetServicePrincipalNameResponseTypeDef,
    GetTemplateGroupAccessControlEntryRequestTypeDef,
    GetTemplateGroupAccessControlEntryResponseTypeDef,
    GetTemplateRequestTypeDef,
    GetTemplateResponseTypeDef,
    ListConnectorsRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListDirectoryRegistrationsRequestTypeDef,
    ListDirectoryRegistrationsResponseTypeDef,
    ListServicePrincipalNamesRequestTypeDef,
    ListServicePrincipalNamesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateGroupAccessControlEntriesRequestTypeDef,
    ListTemplateGroupAccessControlEntriesResponseTypeDef,
    ListTemplatesRequestTypeDef,
    ListTemplatesResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateTemplateGroupAccessControlEntryRequestTypeDef,
    UpdateTemplateRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("PcaConnectorAdClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class PcaConnectorAdClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PcaConnectorAdClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#generate_presigned_url)
        """

    async def create_connector(
        self, **kwargs: Unpack[CreateConnectorRequestTypeDef]
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a connector between Amazon Web Services Private CA and an Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/create_connector.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_connector)
        """

    async def create_directory_registration(
        self, **kwargs: Unpack[CreateDirectoryRegistrationRequestTypeDef]
    ) -> CreateDirectoryRegistrationResponseTypeDef:
        """
        Creates a directory registration that authorizes communication between Amazon
        Web Services Private CA and an Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/create_directory_registration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_directory_registration)
        """

    async def create_service_principal_name(
        self, **kwargs: Unpack[CreateServicePrincipalNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a service principal name (SPN) for the service account in Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/create_service_principal_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_service_principal_name)
        """

    async def create_template(
        self, **kwargs: Unpack[CreateTemplateRequestTypeDef]
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates an Active Directory compatible certificate template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/create_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_template)
        """

    async def create_template_group_access_control_entry(
        self, **kwargs: Unpack[CreateTemplateGroupAccessControlEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Create a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/create_template_group_access_control_entry.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_template_group_access_control_entry)
        """

    async def delete_connector(
        self, **kwargs: Unpack[DeleteConnectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a connector for Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/delete_connector.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_connector)
        """

    async def delete_directory_registration(
        self, **kwargs: Unpack[DeleteDirectoryRegistrationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/delete_directory_registration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_directory_registration)
        """

    async def delete_service_principal_name(
        self, **kwargs: Unpack[DeleteServicePrincipalNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the service principal name (SPN) used by a connector to authenticate
        with your Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/delete_service_principal_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_service_principal_name)
        """

    async def delete_template(
        self, **kwargs: Unpack[DeleteTemplateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/delete_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_template)
        """

    async def delete_template_group_access_control_entry(
        self, **kwargs: Unpack[DeleteTemplateGroupAccessControlEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/delete_template_group_access_control_entry.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_template_group_access_control_entry)
        """

    async def get_connector(
        self, **kwargs: Unpack[GetConnectorRequestTypeDef]
    ) -> GetConnectorResponseTypeDef:
        """
        Lists information about your connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_connector.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_connector)
        """

    async def get_directory_registration(
        self, **kwargs: Unpack[GetDirectoryRegistrationRequestTypeDef]
    ) -> GetDirectoryRegistrationResponseTypeDef:
        """
        A structure that contains information about your directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_directory_registration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_directory_registration)
        """

    async def get_service_principal_name(
        self, **kwargs: Unpack[GetServicePrincipalNameRequestTypeDef]
    ) -> GetServicePrincipalNameResponseTypeDef:
        """
        Lists the service principal name that the connector uses to authenticate with
        Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_service_principal_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_service_principal_name)
        """

    async def get_template(
        self, **kwargs: Unpack[GetTemplateRequestTypeDef]
    ) -> GetTemplateResponseTypeDef:
        """
        Retrieves a certificate template that the connector uses to issue certificates
        from a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_template)
        """

    async def get_template_group_access_control_entry(
        self, **kwargs: Unpack[GetTemplateGroupAccessControlEntryRequestTypeDef]
    ) -> GetTemplateGroupAccessControlEntryResponseTypeDef:
        """
        Retrieves the group access control entries for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_template_group_access_control_entry.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_template_group_access_control_entry)
        """

    async def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors that you created by using the <a
        href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector</a>
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_connectors.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_connectors)
        """

    async def list_directory_registrations(
        self, **kwargs: Unpack[ListDirectoryRegistrationsRequestTypeDef]
    ) -> ListDirectoryRegistrationsResponseTypeDef:
        """
        Lists the directory registrations that you created by using the <a
        href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration</a>
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_directory_registrations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_directory_registrations)
        """

    async def list_service_principal_names(
        self, **kwargs: Unpack[ListServicePrincipalNamesRequestTypeDef]
    ) -> ListServicePrincipalNamesResponseTypeDef:
        """
        Lists the service principal names that the connector uses to authenticate with
        Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_service_principal_names.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_service_principal_names)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags, if any, that are associated with your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_tags_for_resource)
        """

    async def list_template_group_access_control_entries(
        self, **kwargs: Unpack[ListTemplateGroupAccessControlEntriesRequestTypeDef]
    ) -> ListTemplateGroupAccessControlEntriesResponseTypeDef:
        """
        Lists group access control entries you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_template_group_access_control_entries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_template_group_access_control_entries)
        """

    async def list_templates(
        self, **kwargs: Unpack[ListTemplatesRequestTypeDef]
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists the templates, if any, that are associated with a connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/list_templates.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_templates)
        """

    async def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#tag_resource)
        """

    async def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#untag_resource)
        """

    async def update_template(
        self, **kwargs: Unpack[UpdateTemplateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update template configuration to define the information included in
        certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/update_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#update_template)
        """

    async def update_template_group_access_control_entry(
        self, **kwargs: Unpack[UpdateTemplateGroupAccessControlEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update a group access control entry you created using <a
        href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html">CreateTemplateGroupAccessControlEntry</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/update_template_group_access_control_entry.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#update_template_group_access_control_entry)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connectors"]
    ) -> ListConnectorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_directory_registrations"]
    ) -> ListDirectoryRegistrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_principal_names"]
    ) -> ListServicePrincipalNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_template_group_access_control_entries"]
    ) -> ListTemplateGroupAccessControlEntriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_templates"]
    ) -> ListTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
        """
