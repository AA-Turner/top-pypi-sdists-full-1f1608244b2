"""
Type annotations for codeartifact service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_codeartifact.client import CodeArtifactClient

    session = get_session()
    async with session.create_client("codeartifact") as client:
        client: CodeArtifactClient
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
    ListAllowedRepositoriesForGroupPaginator,
    ListAssociatedPackagesPaginator,
    ListDomainsPaginator,
    ListPackageGroupsPaginator,
    ListPackagesPaginator,
    ListPackageVersionAssetsPaginator,
    ListPackageVersionsPaginator,
    ListRepositoriesInDomainPaginator,
    ListRepositoriesPaginator,
    ListSubPackageGroupsPaginator,
)
from .type_defs import (
    AssociateExternalConnectionRequestTypeDef,
    AssociateExternalConnectionResultTypeDef,
    CopyPackageVersionsRequestTypeDef,
    CopyPackageVersionsResultTypeDef,
    CreateDomainRequestTypeDef,
    CreateDomainResultTypeDef,
    CreatePackageGroupRequestTypeDef,
    CreatePackageGroupResultTypeDef,
    CreateRepositoryRequestTypeDef,
    CreateRepositoryResultTypeDef,
    DeleteDomainPermissionsPolicyRequestTypeDef,
    DeleteDomainPermissionsPolicyResultTypeDef,
    DeleteDomainRequestTypeDef,
    DeleteDomainResultTypeDef,
    DeletePackageGroupRequestTypeDef,
    DeletePackageGroupResultTypeDef,
    DeletePackageRequestTypeDef,
    DeletePackageResultTypeDef,
    DeletePackageVersionsRequestTypeDef,
    DeletePackageVersionsResultTypeDef,
    DeleteRepositoryPermissionsPolicyRequestTypeDef,
    DeleteRepositoryPermissionsPolicyResultTypeDef,
    DeleteRepositoryRequestTypeDef,
    DeleteRepositoryResultTypeDef,
    DescribeDomainRequestTypeDef,
    DescribeDomainResultTypeDef,
    DescribePackageGroupRequestTypeDef,
    DescribePackageGroupResultTypeDef,
    DescribePackageRequestTypeDef,
    DescribePackageResultTypeDef,
    DescribePackageVersionRequestTypeDef,
    DescribePackageVersionResultTypeDef,
    DescribeRepositoryRequestTypeDef,
    DescribeRepositoryResultTypeDef,
    DisassociateExternalConnectionRequestTypeDef,
    DisassociateExternalConnectionResultTypeDef,
    DisposePackageVersionsRequestTypeDef,
    DisposePackageVersionsResultTypeDef,
    GetAssociatedPackageGroupRequestTypeDef,
    GetAssociatedPackageGroupResultTypeDef,
    GetAuthorizationTokenRequestTypeDef,
    GetAuthorizationTokenResultTypeDef,
    GetDomainPermissionsPolicyRequestTypeDef,
    GetDomainPermissionsPolicyResultTypeDef,
    GetPackageVersionAssetRequestTypeDef,
    GetPackageVersionAssetResultTypeDef,
    GetPackageVersionReadmeRequestTypeDef,
    GetPackageVersionReadmeResultTypeDef,
    GetRepositoryEndpointRequestTypeDef,
    GetRepositoryEndpointResultTypeDef,
    GetRepositoryPermissionsPolicyRequestTypeDef,
    GetRepositoryPermissionsPolicyResultTypeDef,
    ListAllowedRepositoriesForGroupRequestTypeDef,
    ListAllowedRepositoriesForGroupResultTypeDef,
    ListAssociatedPackagesRequestTypeDef,
    ListAssociatedPackagesResultTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResultTypeDef,
    ListPackageGroupsRequestTypeDef,
    ListPackageGroupsResultTypeDef,
    ListPackagesRequestTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsRequestTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionDependenciesRequestTypeDef,
    ListPackageVersionDependenciesResultTypeDef,
    ListPackageVersionsRequestTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainRequestTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesRequestTypeDef,
    ListRepositoriesResultTypeDef,
    ListSubPackageGroupsRequestTypeDef,
    ListSubPackageGroupsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PublishPackageVersionRequestTypeDef,
    PublishPackageVersionResultTypeDef,
    PutDomainPermissionsPolicyRequestTypeDef,
    PutDomainPermissionsPolicyResultTypeDef,
    PutPackageOriginConfigurationRequestTypeDef,
    PutPackageOriginConfigurationResultTypeDef,
    PutRepositoryPermissionsPolicyRequestTypeDef,
    PutRepositoryPermissionsPolicyResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePackageGroupOriginConfigurationRequestTypeDef,
    UpdatePackageGroupOriginConfigurationResultTypeDef,
    UpdatePackageGroupRequestTypeDef,
    UpdatePackageGroupResultTypeDef,
    UpdatePackageVersionsStatusRequestTypeDef,
    UpdatePackageVersionsStatusResultTypeDef,
    UpdateRepositoryRequestTypeDef,
    UpdateRepositoryResultTypeDef,
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


__all__ = ("CodeArtifactClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeArtifactClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeArtifactClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#generate_presigned_url)
        """

    async def associate_external_connection(
        self, **kwargs: Unpack[AssociateExternalConnectionRequestTypeDef]
    ) -> AssociateExternalConnectionResultTypeDef:
        """
        Adds an existing external connection to a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/associate_external_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#associate_external_connection)
        """

    async def copy_package_versions(
        self, **kwargs: Unpack[CopyPackageVersionsRequestTypeDef]
    ) -> CopyPackageVersionsResultTypeDef:
        """
        Copies package versions from one repository to another repository in the same
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/copy_package_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#copy_package_versions)
        """

    async def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> CreateDomainResultTypeDef:
        """
        Creates a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#create_domain)
        """

    async def create_package_group(
        self, **kwargs: Unpack[CreatePackageGroupRequestTypeDef]
    ) -> CreatePackageGroupResultTypeDef:
        """
        Creates a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_package_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#create_package_group)
        """

    async def create_repository(
        self, **kwargs: Unpack[CreateRepositoryRequestTypeDef]
    ) -> CreateRepositoryResultTypeDef:
        """
        Creates a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_repository.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#create_repository)
        """

    async def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestTypeDef]
    ) -> DeleteDomainResultTypeDef:
        """
        Deletes a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_domain)
        """

    async def delete_domain_permissions_policy(
        self, **kwargs: Unpack[DeleteDomainPermissionsPolicyRequestTypeDef]
    ) -> DeleteDomainPermissionsPolicyResultTypeDef:
        """
        Deletes the resource policy set on a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_domain_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_domain_permissions_policy)
        """

    async def delete_package(
        self, **kwargs: Unpack[DeletePackageRequestTypeDef]
    ) -> DeletePackageResultTypeDef:
        """
        Deletes a package and all associated package versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_package)
        """

    async def delete_package_group(
        self, **kwargs: Unpack[DeletePackageGroupRequestTypeDef]
    ) -> DeletePackageGroupResultTypeDef:
        """
        Deletes a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_package_group)
        """

    async def delete_package_versions(
        self, **kwargs: Unpack[DeletePackageVersionsRequestTypeDef]
    ) -> DeletePackageVersionsResultTypeDef:
        """
        Deletes one or more versions of a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_package_versions)
        """

    async def delete_repository(
        self, **kwargs: Unpack[DeleteRepositoryRequestTypeDef]
    ) -> DeleteRepositoryResultTypeDef:
        """
        Deletes a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_repository.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_repository)
        """

    async def delete_repository_permissions_policy(
        self, **kwargs: Unpack[DeleteRepositoryPermissionsPolicyRequestTypeDef]
    ) -> DeleteRepositoryPermissionsPolicyResultTypeDef:
        """
        Deletes the resource policy that is set on a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_repository_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#delete_repository_permissions_policy)
        """

    async def describe_domain(
        self, **kwargs: Unpack[DescribeDomainRequestTypeDef]
    ) -> DescribeDomainResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html">DomainDescription</a>
        object that contains information about the requested domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#describe_domain)
        """

    async def describe_package(
        self, **kwargs: Unpack[DescribePackageRequestTypeDef]
    ) -> DescribePackageResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html">PackageDescription</a>
        object that contains information about the requested package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#describe_package)
        """

    async def describe_package_group(
        self, **kwargs: Unpack[DescribePackageGroupRequestTypeDef]
    ) -> DescribePackageGroupResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html">PackageGroupDescription</a>
        object that contains information about the requested package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#describe_package_group)
        """

    async def describe_package_version(
        self, **kwargs: Unpack[DescribePackageVersionRequestTypeDef]
    ) -> DescribePackageVersionResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html">PackageVersionDescription</a>
        object that contains information about the requested package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#describe_package_version)
        """

    async def describe_repository(
        self, **kwargs: Unpack[DescribeRepositoryRequestTypeDef]
    ) -> DescribeRepositoryResultTypeDef:
        """
        Returns a <code>RepositoryDescription</code> object that contains detailed
        information about the requested repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_repository.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#describe_repository)
        """

    async def disassociate_external_connection(
        self, **kwargs: Unpack[DisassociateExternalConnectionRequestTypeDef]
    ) -> DisassociateExternalConnectionResultTypeDef:
        """
        Removes an existing external connection from a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/disassociate_external_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#disassociate_external_connection)
        """

    async def dispose_package_versions(
        self, **kwargs: Unpack[DisposePackageVersionsRequestTypeDef]
    ) -> DisposePackageVersionsResultTypeDef:
        """
        Deletes the assets in package versions and sets the package versions' status to
        <code>Disposed</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/dispose_package_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#dispose_package_versions)
        """

    async def get_associated_package_group(
        self, **kwargs: Unpack[GetAssociatedPackageGroupRequestTypeDef]
    ) -> GetAssociatedPackageGroupResultTypeDef:
        """
        Returns the most closely associated package group to the specified package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_associated_package_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_associated_package_group)
        """

    async def get_authorization_token(
        self, **kwargs: Unpack[GetAuthorizationTokenRequestTypeDef]
    ) -> GetAuthorizationTokenResultTypeDef:
        """
        Generates a temporary authorization token for accessing repositories in the
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_authorization_token.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_authorization_token)
        """

    async def get_domain_permissions_policy(
        self, **kwargs: Unpack[GetDomainPermissionsPolicyRequestTypeDef]
    ) -> GetDomainPermissionsPolicyResultTypeDef:
        """
        Returns the resource policy attached to the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_domain_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_domain_permissions_policy)
        """

    async def get_package_version_asset(
        self, **kwargs: Unpack[GetPackageVersionAssetRequestTypeDef]
    ) -> GetPackageVersionAssetResultTypeDef:
        """
        Returns an asset (or file) that is in a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_package_version_asset.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_package_version_asset)
        """

    async def get_package_version_readme(
        self, **kwargs: Unpack[GetPackageVersionReadmeRequestTypeDef]
    ) -> GetPackageVersionReadmeResultTypeDef:
        """
        Gets the readme file or descriptive text for a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_package_version_readme.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_package_version_readme)
        """

    async def get_repository_endpoint(
        self, **kwargs: Unpack[GetRepositoryEndpointRequestTypeDef]
    ) -> GetRepositoryEndpointResultTypeDef:
        """
        Returns the endpoint of a repository for a specific package format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_repository_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_repository_endpoint)
        """

    async def get_repository_permissions_policy(
        self, **kwargs: Unpack[GetRepositoryPermissionsPolicyRequestTypeDef]
    ) -> GetRepositoryPermissionsPolicyResultTypeDef:
        """
        Returns the resource policy that is set on a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_repository_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_repository_permissions_policy)
        """

    async def list_allowed_repositories_for_group(
        self, **kwargs: Unpack[ListAllowedRepositoriesForGroupRequestTypeDef]
    ) -> ListAllowedRepositoriesForGroupResultTypeDef:
        """
        Lists the repositories in the added repositories list of the specified
        restriction type for a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_allowed_repositories_for_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_allowed_repositories_for_group)
        """

    async def list_associated_packages(
        self, **kwargs: Unpack[ListAssociatedPackagesRequestTypeDef]
    ) -> ListAssociatedPackagesResultTypeDef:
        """
        Returns a list of packages associated with the requested package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_associated_packages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_associated_packages)
        """

    async def list_domains(
        self, **kwargs: Unpack[ListDomainsRequestTypeDef]
    ) -> ListDomainsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html">DomainSummary</a>
        objects for all domains owned by the Amazon Web Services account that makes
        this call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_domains.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_domains)
        """

    async def list_package_groups(
        self, **kwargs: Unpack[ListPackageGroupsRequestTypeDef]
    ) -> ListPackageGroupsResultTypeDef:
        """
        Returns a list of package groups in the requested domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_package_groups)
        """

    async def list_package_version_assets(
        self, **kwargs: Unpack[ListPackageVersionAssetsRequestTypeDef]
    ) -> ListPackageVersionAssetsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html">AssetSummary</a>
        objects for assets in a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_version_assets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_package_version_assets)
        """

    async def list_package_version_dependencies(
        self, **kwargs: Unpack[ListPackageVersionDependenciesRequestTypeDef]
    ) -> ListPackageVersionDependenciesResultTypeDef:
        """
        Returns the direct dependencies for a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_version_dependencies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_package_version_dependencies)
        """

    async def list_package_versions(
        self, **kwargs: Unpack[ListPackageVersionsRequestTypeDef]
    ) -> ListPackageVersionsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html">PackageVersionSummary</a>
        objects for package versions in a repository that match the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_package_versions)
        """

    async def list_packages(
        self, **kwargs: Unpack[ListPackagesRequestTypeDef]
    ) -> ListPackagesResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html">PackageSummary</a>
        objects for packages in a repository that match the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_packages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_packages)
        """

    async def list_repositories(
        self, **kwargs: Unpack[ListRepositoriesRequestTypeDef]
    ) -> ListRepositoriesResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html">RepositorySummary</a>
        objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_repositories.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_repositories)
        """

    async def list_repositories_in_domain(
        self, **kwargs: Unpack[ListRepositoriesInDomainRequestTypeDef]
    ) -> ListRepositoriesInDomainResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html">RepositorySummary</a>
        objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_repositories_in_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_repositories_in_domain)
        """

    async def list_sub_package_groups(
        self, **kwargs: Unpack[ListSubPackageGroupsRequestTypeDef]
    ) -> ListSubPackageGroupsResultTypeDef:
        """
        Returns a list of direct children of the specified package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_sub_package_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_sub_package_groups)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Gets information about Amazon Web Services tags for a specified Amazon Resource
        Name (ARN) in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#list_tags_for_resource)
        """

    async def publish_package_version(
        self, **kwargs: Unpack[PublishPackageVersionRequestTypeDef]
    ) -> PublishPackageVersionResultTypeDef:
        """
        Creates a new package version containing one or more assets (or files).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/publish_package_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#publish_package_version)
        """

    async def put_domain_permissions_policy(
        self, **kwargs: Unpack[PutDomainPermissionsPolicyRequestTypeDef]
    ) -> PutDomainPermissionsPolicyResultTypeDef:
        """
        Sets a resource policy on a domain that specifies permissions to access it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_domain_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#put_domain_permissions_policy)
        """

    async def put_package_origin_configuration(
        self, **kwargs: Unpack[PutPackageOriginConfigurationRequestTypeDef]
    ) -> PutPackageOriginConfigurationResultTypeDef:
        """
        Sets the package origin configuration for a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_package_origin_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#put_package_origin_configuration)
        """

    async def put_repository_permissions_policy(
        self, **kwargs: Unpack[PutRepositoryPermissionsPolicyRequestTypeDef]
    ) -> PutRepositoryPermissionsPolicyResultTypeDef:
        """
        Sets the resource policy on a repository that specifies permissions to access
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_repository_permissions_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#put_repository_permissions_policy)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a resource in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#untag_resource)
        """

    async def update_package_group(
        self, **kwargs: Unpack[UpdatePackageGroupRequestTypeDef]
    ) -> UpdatePackageGroupResultTypeDef:
        """
        Updates a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#update_package_group)
        """

    async def update_package_group_origin_configuration(
        self, **kwargs: Unpack[UpdatePackageGroupOriginConfigurationRequestTypeDef]
    ) -> UpdatePackageGroupOriginConfigurationResultTypeDef:
        """
        Updates the package origin configuration for a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_group_origin_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#update_package_group_origin_configuration)
        """

    async def update_package_versions_status(
        self, **kwargs: Unpack[UpdatePackageVersionsStatusRequestTypeDef]
    ) -> UpdatePackageVersionsStatusResultTypeDef:
        """
        Updates the status of one or more versions of a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_versions_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#update_package_versions_status)
        """

    async def update_repository(
        self, **kwargs: Unpack[UpdateRepositoryRequestTypeDef]
    ) -> UpdateRepositoryResultTypeDef:
        """
        Update the properties of a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_repository.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#update_repository)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_allowed_repositories_for_group"]
    ) -> ListAllowedRepositoriesForGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_packages"]
    ) -> ListAssociatedPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_groups"]
    ) -> ListPackageGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_version_assets"]
    ) -> ListPackageVersionAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_versions"]
    ) -> ListPackageVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_packages"]
    ) -> ListPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_repositories_in_domain"]
    ) -> ListRepositoriesInDomainPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sub_package_groups"]
    ) -> ListSubPackageGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/client/)
        """
