"""
Type annotations for opensearch service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_opensearch.client import OpenSearchServiceClient

    session = get_session()
    async with session.create_client("opensearch") as client:
        client: OpenSearchServiceClient
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

from .paginator import ListApplicationsPaginator
from .type_defs import (
    AcceptInboundConnectionRequestTypeDef,
    AcceptInboundConnectionResponseTypeDef,
    AddDataSourceRequestTypeDef,
    AddDataSourceResponseTypeDef,
    AddDirectQueryDataSourceRequestTypeDef,
    AddDirectQueryDataSourceResponseTypeDef,
    AddTagsRequestTypeDef,
    AssociatePackageRequestTypeDef,
    AssociatePackageResponseTypeDef,
    AssociatePackagesRequestTypeDef,
    AssociatePackagesResponseTypeDef,
    AuthorizeVpcEndpointAccessRequestTypeDef,
    AuthorizeVpcEndpointAccessResponseTypeDef,
    CancelDomainConfigChangeRequestTypeDef,
    CancelDomainConfigChangeResponseTypeDef,
    CancelServiceSoftwareUpdateRequestTypeDef,
    CancelServiceSoftwareUpdateResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDomainRequestTypeDef,
    CreateDomainResponseTypeDef,
    CreateOutboundConnectionRequestTypeDef,
    CreateOutboundConnectionResponseTypeDef,
    CreatePackageRequestTypeDef,
    CreatePackageResponseTypeDef,
    CreateVpcEndpointRequestTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteDataSourceRequestTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteDirectQueryDataSourceRequestTypeDef,
    DeleteDomainRequestTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteInboundConnectionRequestTypeDef,
    DeleteInboundConnectionResponseTypeDef,
    DeleteOutboundConnectionRequestTypeDef,
    DeleteOutboundConnectionResponseTypeDef,
    DeletePackageRequestTypeDef,
    DeletePackageResponseTypeDef,
    DeleteVpcEndpointRequestTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    DescribeDomainAutoTunesRequestTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeDomainChangeProgressRequestTypeDef,
    DescribeDomainChangeProgressResponseTypeDef,
    DescribeDomainConfigRequestTypeDef,
    DescribeDomainConfigResponseTypeDef,
    DescribeDomainHealthRequestTypeDef,
    DescribeDomainHealthResponseTypeDef,
    DescribeDomainNodesRequestTypeDef,
    DescribeDomainNodesResponseTypeDef,
    DescribeDomainRequestTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeDomainsRequestTypeDef,
    DescribeDomainsResponseTypeDef,
    DescribeDryRunProgressRequestTypeDef,
    DescribeDryRunProgressResponseTypeDef,
    DescribeInboundConnectionsRequestTypeDef,
    DescribeInboundConnectionsResponseTypeDef,
    DescribeInstanceTypeLimitsRequestTypeDef,
    DescribeInstanceTypeLimitsResponseTypeDef,
    DescribeOutboundConnectionsRequestTypeDef,
    DescribeOutboundConnectionsResponseTypeDef,
    DescribePackagesRequestTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedInstanceOfferingsRequestTypeDef,
    DescribeReservedInstanceOfferingsResponseTypeDef,
    DescribeReservedInstancesRequestTypeDef,
    DescribeReservedInstancesResponseTypeDef,
    DescribeVpcEndpointsRequestTypeDef,
    DescribeVpcEndpointsResponseTypeDef,
    DissociatePackageRequestTypeDef,
    DissociatePackageResponseTypeDef,
    DissociatePackagesRequestTypeDef,
    DissociatePackagesResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetCompatibleVersionsRequestTypeDef,
    GetCompatibleVersionsResponseTypeDef,
    GetDataSourceRequestTypeDef,
    GetDataSourceResponseTypeDef,
    GetDirectQueryDataSourceRequestTypeDef,
    GetDirectQueryDataSourceResponseTypeDef,
    GetDomainMaintenanceStatusRequestTypeDef,
    GetDomainMaintenanceStatusResponseTypeDef,
    GetPackageVersionHistoryRequestTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryRequestTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusRequestTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListDataSourcesRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDirectQueryDataSourcesRequestTypeDef,
    ListDirectQueryDataSourcesResponseTypeDef,
    ListDomainMaintenancesRequestTypeDef,
    ListDomainMaintenancesResponseTypeDef,
    ListDomainNamesRequestTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageRequestTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListInstanceTypeDetailsRequestTypeDef,
    ListInstanceTypeDetailsResponseTypeDef,
    ListPackagesForDomainRequestTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListScheduledActionsRequestTypeDef,
    ListScheduledActionsResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsRequestTypeDef,
    ListVersionsResponseTypeDef,
    ListVpcEndpointAccessRequestTypeDef,
    ListVpcEndpointAccessResponseTypeDef,
    ListVpcEndpointsForDomainRequestTypeDef,
    ListVpcEndpointsForDomainResponseTypeDef,
    ListVpcEndpointsRequestTypeDef,
    ListVpcEndpointsResponseTypeDef,
    PurchaseReservedInstanceOfferingRequestTypeDef,
    PurchaseReservedInstanceOfferingResponseTypeDef,
    RejectInboundConnectionRequestTypeDef,
    RejectInboundConnectionResponseTypeDef,
    RemoveTagsRequestTypeDef,
    RevokeVpcEndpointAccessRequestTypeDef,
    StartDomainMaintenanceRequestTypeDef,
    StartDomainMaintenanceResponseTypeDef,
    StartServiceSoftwareUpdateRequestTypeDef,
    StartServiceSoftwareUpdateResponseTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateDataSourceRequestTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateDirectQueryDataSourceRequestTypeDef,
    UpdateDirectQueryDataSourceResponseTypeDef,
    UpdateDomainConfigRequestTypeDef,
    UpdateDomainConfigResponseTypeDef,
    UpdatePackageRequestTypeDef,
    UpdatePackageResponseTypeDef,
    UpdatePackageScopeRequestTypeDef,
    UpdatePackageScopeResponseTypeDef,
    UpdateScheduledActionRequestTypeDef,
    UpdateScheduledActionResponseTypeDef,
    UpdateVpcEndpointRequestTypeDef,
    UpdateVpcEndpointResponseTypeDef,
    UpgradeDomainRequestTypeDef,
    UpgradeDomainResponseTypeDef,
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

__all__ = ("OpenSearchServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailureException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    SlotNotAvailableException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#generate_presigned_url)
        """

    async def accept_inbound_connection(
        self, **kwargs: Unpack[AcceptInboundConnectionRequestTypeDef]
    ) -> AcceptInboundConnectionResponseTypeDef:
        """
        Allows the destination Amazon OpenSearch Service domain owner to accept an
        inbound cross-cluster search connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/accept_inbound_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#accept_inbound_connection)
        """

    async def add_data_source(
        self, **kwargs: Unpack[AddDataSourceRequestTypeDef]
    ) -> AddDataSourceResponseTypeDef:
        """
        Creates a new direct-query data source to the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/add_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#add_data_source)
        """

    async def add_direct_query_data_source(
        self, **kwargs: Unpack[AddDirectQueryDataSourceRequestTypeDef]
    ) -> AddDirectQueryDataSourceResponseTypeDef:
        """
        Adds a new data source in Amazon OpenSearch Service so that you can perform
        direct queries on external data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/add_direct_query_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#add_direct_query_data_source)
        """

    async def add_tags(
        self, **kwargs: Unpack[AddTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches tags to an existing Amazon OpenSearch Service domain, data source, or
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/add_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#add_tags)
        """

    async def associate_package(
        self, **kwargs: Unpack[AssociatePackageRequestTypeDef]
    ) -> AssociatePackageResponseTypeDef:
        """
        Associates a package with an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/associate_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#associate_package)
        """

    async def associate_packages(
        self, **kwargs: Unpack[AssociatePackagesRequestTypeDef]
    ) -> AssociatePackagesResponseTypeDef:
        """
        Operation in the Amazon OpenSearch Service API for associating multiple
        packages with a domain simultaneously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/associate_packages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#associate_packages)
        """

    async def authorize_vpc_endpoint_access(
        self, **kwargs: Unpack[AuthorizeVpcEndpointAccessRequestTypeDef]
    ) -> AuthorizeVpcEndpointAccessResponseTypeDef:
        """
        Provides access to an Amazon OpenSearch Service domain through the use of an
        interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/authorize_vpc_endpoint_access.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#authorize_vpc_endpoint_access)
        """

    async def cancel_domain_config_change(
        self, **kwargs: Unpack[CancelDomainConfigChangeRequestTypeDef]
    ) -> CancelDomainConfigChangeResponseTypeDef:
        """
        Cancels a pending configuration change on an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/cancel_domain_config_change.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#cancel_domain_config_change)
        """

    async def cancel_service_software_update(
        self, **kwargs: Unpack[CancelServiceSoftwareUpdateRequestTypeDef]
    ) -> CancelServiceSoftwareUpdateResponseTypeDef:
        """
        Cancels a scheduled service software update for an Amazon OpenSearch Service
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/cancel_service_software_update.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#cancel_service_software_update)
        """

    async def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an OpenSearch UI application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/create_application.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#create_application)
        """

    async def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> CreateDomainResponseTypeDef:
        """
        Creates an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/create_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#create_domain)
        """

    async def create_outbound_connection(
        self, **kwargs: Unpack[CreateOutboundConnectionRequestTypeDef]
    ) -> CreateOutboundConnectionResponseTypeDef:
        """
        Creates a new cross-cluster search connection from a source Amazon OpenSearch
        Service domain to a destination domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/create_outbound_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#create_outbound_connection)
        """

    async def create_package(
        self, **kwargs: Unpack[CreatePackageRequestTypeDef]
    ) -> CreatePackageResponseTypeDef:
        """
        Creates a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/create_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#create_package)
        """

    async def create_vpc_endpoint(
        self, **kwargs: Unpack[CreateVpcEndpointRequestTypeDef]
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an Amazon OpenSearch Service-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/create_vpc_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#create_vpc_endpoint)
        """

    async def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified OpenSearch application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_application.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_application)
        """

    async def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestTypeDef]
    ) -> DeleteDataSourceResponseTypeDef:
        """
        Deletes a direct-query data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_data_source)
        """

    async def delete_direct_query_data_source(
        self, **kwargs: Unpack[DeleteDirectQueryDataSourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a previously configured direct query data source from Amazon OpenSearch
        Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_direct_query_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_direct_query_data_source)
        """

    async def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestTypeDef]
    ) -> DeleteDomainResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_domain)
        """

    async def delete_inbound_connection(
        self, **kwargs: Unpack[DeleteInboundConnectionRequestTypeDef]
    ) -> DeleteInboundConnectionResponseTypeDef:
        """
        Allows the destination Amazon OpenSearch Service domain owner to delete an
        existing inbound cross-cluster search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_inbound_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_inbound_connection)
        """

    async def delete_outbound_connection(
        self, **kwargs: Unpack[DeleteOutboundConnectionRequestTypeDef]
    ) -> DeleteOutboundConnectionResponseTypeDef:
        """
        Allows the source Amazon OpenSearch Service domain owner to delete an existing
        outbound cross-cluster search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_outbound_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_outbound_connection)
        """

    async def delete_package(
        self, **kwargs: Unpack[DeletePackageRequestTypeDef]
    ) -> DeletePackageResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_package)
        """

    async def delete_vpc_endpoint(
        self, **kwargs: Unpack[DeleteVpcEndpointRequestTypeDef]
    ) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/delete_vpc_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#delete_vpc_endpoint)
        """

    async def describe_domain(
        self, **kwargs: Unpack[DescribeDomainRequestTypeDef]
    ) -> DescribeDomainResponseTypeDef:
        """
        Describes the domain configuration for the specified Amazon OpenSearch Service
        domain, including the domain ID, domain service endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain)
        """

    async def describe_domain_auto_tunes(
        self, **kwargs: Unpack[DescribeDomainAutoTunesRequestTypeDef]
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        Returns the list of optimizations that Auto-Tune has made to an Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain_auto_tunes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain_auto_tunes)
        """

    async def describe_domain_change_progress(
        self, **kwargs: Unpack[DescribeDomainChangeProgressRequestTypeDef]
    ) -> DescribeDomainChangeProgressResponseTypeDef:
        """
        Returns information about the current blue/green deployment happening on an
        Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain_change_progress.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain_change_progress)
        """

    async def describe_domain_config(
        self, **kwargs: Unpack[DescribeDomainConfigRequestTypeDef]
    ) -> DescribeDomainConfigResponseTypeDef:
        """
        Returns the configuration of an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain_config)
        """

    async def describe_domain_health(
        self, **kwargs: Unpack[DescribeDomainHealthRequestTypeDef]
    ) -> DescribeDomainHealthResponseTypeDef:
        """
        Returns information about domain and node health, the standby Availability
        Zone, number of nodes per Availability Zone, and shard count per node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain_health.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain_health)
        """

    async def describe_domain_nodes(
        self, **kwargs: Unpack[DescribeDomainNodesRequestTypeDef]
    ) -> DescribeDomainNodesResponseTypeDef:
        """
        Returns information about domain and nodes, including data nodes, master nodes,
        ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and
        node states.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domain_nodes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domain_nodes)
        """

    async def describe_domains(
        self, **kwargs: Unpack[DescribeDomainsRequestTypeDef]
    ) -> DescribeDomainsResponseTypeDef:
        """
        Returns domain configuration information about the specified Amazon OpenSearch
        Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_domains.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_domains)
        """

    async def describe_dry_run_progress(
        self, **kwargs: Unpack[DescribeDryRunProgressRequestTypeDef]
    ) -> DescribeDryRunProgressResponseTypeDef:
        """
        Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch
        Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_dry_run_progress.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_dry_run_progress)
        """

    async def describe_inbound_connections(
        self, **kwargs: Unpack[DescribeInboundConnectionsRequestTypeDef]
    ) -> DescribeInboundConnectionsResponseTypeDef:
        """
        Lists all the inbound cross-cluster search connections for a destination
        (remote) Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_inbound_connections.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_inbound_connections)
        """

    async def describe_instance_type_limits(
        self, **kwargs: Unpack[DescribeInstanceTypeLimitsRequestTypeDef]
    ) -> DescribeInstanceTypeLimitsResponseTypeDef:
        """
        Describes the instance count, storage, and master node limits for a given
        OpenSearch or Elasticsearch version and instance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_instance_type_limits.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_instance_type_limits)
        """

    async def describe_outbound_connections(
        self, **kwargs: Unpack[DescribeOutboundConnectionsRequestTypeDef]
    ) -> DescribeOutboundConnectionsResponseTypeDef:
        """
        Lists all the outbound cross-cluster connections for a local (source) Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_outbound_connections.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_outbound_connections)
        """

    async def describe_packages(
        self, **kwargs: Unpack[DescribePackagesRequestTypeDef]
    ) -> DescribePackagesResponseTypeDef:
        """
        Describes all packages available to OpenSearch Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_packages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_packages)
        """

    async def describe_reserved_instance_offerings(
        self, **kwargs: Unpack[DescribeReservedInstanceOfferingsRequestTypeDef]
    ) -> DescribeReservedInstanceOfferingsResponseTypeDef:
        """
        Describes the available Amazon OpenSearch Service Reserved Instance offerings
        for a given Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_reserved_instance_offerings.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_reserved_instance_offerings)
        """

    async def describe_reserved_instances(
        self, **kwargs: Unpack[DescribeReservedInstancesRequestTypeDef]
    ) -> DescribeReservedInstancesResponseTypeDef:
        """
        Describes the Amazon OpenSearch Service instances that you have reserved in a
        given Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_reserved_instances.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_reserved_instances)
        """

    async def describe_vpc_endpoints(
        self, **kwargs: Unpack[DescribeVpcEndpointsRequestTypeDef]
    ) -> DescribeVpcEndpointsResponseTypeDef:
        """
        Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/describe_vpc_endpoints.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#describe_vpc_endpoints)
        """

    async def dissociate_package(
        self, **kwargs: Unpack[DissociatePackageRequestTypeDef]
    ) -> DissociatePackageResponseTypeDef:
        """
        Removes a package from the specified Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/dissociate_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#dissociate_package)
        """

    async def dissociate_packages(
        self, **kwargs: Unpack[DissociatePackagesRequestTypeDef]
    ) -> DissociatePackagesResponseTypeDef:
        """
        Dissociates multiple packages from a domain simulatneously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/dissociate_packages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#dissociate_packages)
        """

    async def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Retrieves the configuration and status of an existing OpenSearch application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_application.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_application)
        """

    async def get_compatible_versions(
        self, **kwargs: Unpack[GetCompatibleVersionsRequestTypeDef]
    ) -> GetCompatibleVersionsResponseTypeDef:
        """
        Returns a map of OpenSearch or Elasticsearch versions and the versions you can
        upgrade them to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_compatible_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_compatible_versions)
        """

    async def get_data_source(
        self, **kwargs: Unpack[GetDataSourceRequestTypeDef]
    ) -> GetDataSourceResponseTypeDef:
        """
        Retrieves information about a direct query data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_data_source)
        """

    async def get_direct_query_data_source(
        self, **kwargs: Unpack[GetDirectQueryDataSourceRequestTypeDef]
    ) -> GetDirectQueryDataSourceResponseTypeDef:
        """
        Returns detailed configuration information for a specific direct query data
        source in Amazon OpenSearch Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_direct_query_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_direct_query_data_source)
        """

    async def get_domain_maintenance_status(
        self, **kwargs: Unpack[GetDomainMaintenanceStatusRequestTypeDef]
    ) -> GetDomainMaintenanceStatusResponseTypeDef:
        """
        The status of the maintenance action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_domain_maintenance_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_domain_maintenance_status)
        """

    async def get_package_version_history(
        self, **kwargs: Unpack[GetPackageVersionHistoryRequestTypeDef]
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        Returns a list of Amazon OpenSearch Service package versions, along with their
        creation time, commit message, and plugin properties (if the package is a zip
        plugin package).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_package_version_history.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_package_version_history)
        """

    async def get_upgrade_history(
        self, **kwargs: Unpack[GetUpgradeHistoryRequestTypeDef]
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        Retrieves the complete history of the last 10 upgrades performed on an Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_upgrade_history.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_upgrade_history)
        """

    async def get_upgrade_status(
        self, **kwargs: Unpack[GetUpgradeStatusRequestTypeDef]
    ) -> GetUpgradeStatusResponseTypeDef:
        """
        Returns the most recent status of the last upgrade or upgrade eligibility check
        performed on an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_upgrade_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_upgrade_status)
        """

    async def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists all OpenSearch applications under your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_applications.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_applications)
        """

    async def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists direct-query data sources for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_data_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_data_sources)
        """

    async def list_direct_query_data_sources(
        self, **kwargs: Unpack[ListDirectQueryDataSourcesRequestTypeDef]
    ) -> ListDirectQueryDataSourcesResponseTypeDef:
        """
        Lists an inventory of all the direct query data sources that you have
        configured within Amazon OpenSearch Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_direct_query_data_sources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_direct_query_data_sources)
        """

    async def list_domain_maintenances(
        self, **kwargs: Unpack[ListDomainMaintenancesRequestTypeDef]
    ) -> ListDomainMaintenancesResponseTypeDef:
        """
        A list of maintenance actions for the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_domain_maintenances.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_domain_maintenances)
        """

    async def list_domain_names(
        self, **kwargs: Unpack[ListDomainNamesRequestTypeDef]
    ) -> ListDomainNamesResponseTypeDef:
        """
        Returns the names of all Amazon OpenSearch Service domains owned by the current
        user in the active Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_domain_names.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_domain_names)
        """

    async def list_domains_for_package(
        self, **kwargs: Unpack[ListDomainsForPackageRequestTypeDef]
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        Lists all Amazon OpenSearch Service domains associated with a given package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_domains_for_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_domains_for_package)
        """

    async def list_instance_type_details(
        self, **kwargs: Unpack[ListInstanceTypeDetailsRequestTypeDef]
    ) -> ListInstanceTypeDetailsResponseTypeDef:
        """
        Lists all instance types and available features for a given OpenSearch or
        Elasticsearch version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_instance_type_details.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_instance_type_details)
        """

    async def list_packages_for_domain(
        self, **kwargs: Unpack[ListPackagesForDomainRequestTypeDef]
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        Lists all packages associated with an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_packages_for_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_packages_for_domain)
        """

    async def list_scheduled_actions(
        self, **kwargs: Unpack[ListScheduledActionsRequestTypeDef]
    ) -> ListScheduledActionsResponseTypeDef:
        """
        Retrieves a list of configuration changes that are scheduled for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_scheduled_actions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_scheduled_actions)
        """

    async def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Returns all resource tags for an Amazon OpenSearch Service domain, data source,
        or application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_tags)
        """

    async def list_versions(
        self, **kwargs: Unpack[ListVersionsRequestTypeDef]
    ) -> ListVersionsResponseTypeDef:
        """
        Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch
        Service supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_versions)
        """

    async def list_vpc_endpoint_access(
        self, **kwargs: Unpack[ListVpcEndpointAccessRequestTypeDef]
    ) -> ListVpcEndpointAccessResponseTypeDef:
        """
        Retrieves information about each Amazon Web Services principal that is allowed
        to access a given Amazon OpenSearch Service domain through the use of an
        interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_vpc_endpoint_access.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_vpc_endpoint_access)
        """

    async def list_vpc_endpoints(
        self, **kwargs: Unpack[ListVpcEndpointsRequestTypeDef]
    ) -> ListVpcEndpointsResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current
        Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_vpc_endpoints.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_vpc_endpoints)
        """

    async def list_vpc_endpoints_for_domain(
        self, **kwargs: Unpack[ListVpcEndpointsForDomainRequestTypeDef]
    ) -> ListVpcEndpointsForDomainResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a
        particular domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/list_vpc_endpoints_for_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#list_vpc_endpoints_for_domain)
        """

    async def purchase_reserved_instance_offering(
        self, **kwargs: Unpack[PurchaseReservedInstanceOfferingRequestTypeDef]
    ) -> PurchaseReservedInstanceOfferingResponseTypeDef:
        """
        Allows you to purchase Amazon OpenSearch Service Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/purchase_reserved_instance_offering.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#purchase_reserved_instance_offering)
        """

    async def reject_inbound_connection(
        self, **kwargs: Unpack[RejectInboundConnectionRequestTypeDef]
    ) -> RejectInboundConnectionResponseTypeDef:
        """
        Allows the remote Amazon OpenSearch Service domain owner to reject an inbound
        cross-cluster connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/reject_inbound_connection.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#reject_inbound_connection)
        """

    async def remove_tags(
        self, **kwargs: Unpack[RemoveTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified set of tags from an Amazon OpenSearch Service domain,
        data source, or application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/remove_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#remove_tags)
        """

    async def revoke_vpc_endpoint_access(
        self, **kwargs: Unpack[RevokeVpcEndpointAccessRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Revokes access to an Amazon OpenSearch Service domain that was provided through
        an interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/revoke_vpc_endpoint_access.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#revoke_vpc_endpoint_access)
        """

    async def start_domain_maintenance(
        self, **kwargs: Unpack[StartDomainMaintenanceRequestTypeDef]
    ) -> StartDomainMaintenanceResponseTypeDef:
        """
        Starts the node maintenance process on the data node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/start_domain_maintenance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#start_domain_maintenance)
        """

    async def start_service_software_update(
        self, **kwargs: Unpack[StartServiceSoftwareUpdateRequestTypeDef]
    ) -> StartServiceSoftwareUpdateResponseTypeDef:
        """
        Schedules a service software update for an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/start_service_software_update.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#start_service_software_update)
        """

    async def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates the configuration and settings of an existing OpenSearch application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_application.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_application)
        """

    async def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestTypeDef]
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a direct-query data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_data_source)
        """

    async def update_direct_query_data_source(
        self, **kwargs: Unpack[UpdateDirectQueryDataSourceRequestTypeDef]
    ) -> UpdateDirectQueryDataSourceResponseTypeDef:
        """
        Updates the configuration or properties of an existing direct query data source
        in Amazon OpenSearch Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_direct_query_data_source.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_direct_query_data_source)
        """

    async def update_domain_config(
        self, **kwargs: Unpack[UpdateDomainConfigRequestTypeDef]
    ) -> UpdateDomainConfigResponseTypeDef:
        """
        Modifies the cluster configuration of the specified Amazon OpenSearch Service
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_domain_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_domain_config)
        """

    async def update_package(
        self, **kwargs: Unpack[UpdatePackageRequestTypeDef]
    ) -> UpdatePackageResponseTypeDef:
        """
        Updates a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_package.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_package)
        """

    async def update_package_scope(
        self, **kwargs: Unpack[UpdatePackageScopeRequestTypeDef]
    ) -> UpdatePackageScopeResponseTypeDef:
        """
        Updates the scope of a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_package_scope.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_package_scope)
        """

    async def update_scheduled_action(
        self, **kwargs: Unpack[UpdateScheduledActionRequestTypeDef]
    ) -> UpdateScheduledActionResponseTypeDef:
        """
        Reschedules a planned domain configuration change for a later time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_scheduled_action.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_scheduled_action)
        """

    async def update_vpc_endpoint(
        self, **kwargs: Unpack[UpdateVpcEndpointRequestTypeDef]
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/update_vpc_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#update_vpc_endpoint)
        """

    async def upgrade_domain(
        self, **kwargs: Unpack[UpgradeDomainRequestTypeDef]
    ) -> UpgradeDomainResponseTypeDef:
        """
        Allows you to either upgrade your Amazon OpenSearch Service domain or perform
        an upgrade eligibility check to a compatible version of OpenSearch or
        Elasticsearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/upgrade_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#upgrade_domain)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client/)
        """
