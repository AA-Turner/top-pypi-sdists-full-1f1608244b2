"""
Type annotations for dax service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_dax.client import DAXClient

    session = get_session()
    async with session.create_client("dax") as client:
        client: DAXClient
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
    DescribeClustersPaginator,
    DescribeDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeSubnetGroupsPaginator,
    ListTagsPaginator,
)
from .type_defs import (
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateParameterGroupRequestTypeDef,
    CreateParameterGroupResponseTypeDef,
    CreateSubnetGroupRequestTypeDef,
    CreateSubnetGroupResponseTypeDef,
    DecreaseReplicationFactorRequestTypeDef,
    DecreaseReplicationFactorResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteParameterGroupRequestTypeDef,
    DeleteParameterGroupResponseTypeDef,
    DeleteSubnetGroupRequestTypeDef,
    DeleteSubnetGroupResponseTypeDef,
    DescribeClustersRequestTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersRequestTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsRequestTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsRequestTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsRequestTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    IncreaseReplicationFactorRequestTypeDef,
    IncreaseReplicationFactorResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    RebootNodeRequestTypeDef,
    RebootNodeResponseTypeDef,
    TagResourceRequestTypeDef,
    TagResourceResponseTypeDef,
    UntagResourceRequestTypeDef,
    UntagResourceResponseTypeDef,
    UpdateClusterRequestTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateParameterGroupRequestTypeDef,
    UpdateParameterGroupResponseTypeDef,
    UpdateSubnetGroupRequestTypeDef,
    UpdateSubnetGroupResponseTypeDef,
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

__all__ = ("DAXClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterQuotaForCustomerExceededFault: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InvalidARNFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterGroupStateFault: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    NodeNotFoundFault: Type[BotocoreClientError]
    NodeQuotaForClusterExceededFault: Type[BotocoreClientError]
    NodeQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ParameterGroupNotFoundFault: Type[BotocoreClientError]
    ParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ServiceLinkedRoleNotFoundFault: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    SubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    SubnetGroupInUseFault: Type[BotocoreClientError]
    SubnetGroupNotFoundFault: Type[BotocoreClientError]
    SubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetQuotaExceededFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]

class DAXClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DAXClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#generate_presigned_url)
        """

    async def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/create_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#create_cluster)
        """

    async def create_parameter_group(
        self, **kwargs: Unpack[CreateParameterGroupRequestTypeDef]
    ) -> CreateParameterGroupResponseTypeDef:
        """
        Creates a new parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/create_parameter_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#create_parameter_group)
        """

    async def create_subnet_group(
        self, **kwargs: Unpack[CreateSubnetGroupRequestTypeDef]
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        Creates a new subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/create_subnet_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#create_subnet_group)
        """

    async def decrease_replication_factor(
        self, **kwargs: Unpack[DecreaseReplicationFactorRequestTypeDef]
    ) -> DecreaseReplicationFactorResponseTypeDef:
        """
        Removes one or more nodes from a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/decrease_replication_factor.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#decrease_replication_factor)
        """

    async def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes a previously provisioned DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/delete_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#delete_cluster)
        """

    async def delete_parameter_group(
        self, **kwargs: Unpack[DeleteParameterGroupRequestTypeDef]
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        Deletes the specified parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/delete_parameter_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#delete_parameter_group)
        """

    async def delete_subnet_group(
        self, **kwargs: Unpack[DeleteSubnetGroupRequestTypeDef]
    ) -> DeleteSubnetGroupResponseTypeDef:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/delete_subnet_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#delete_subnet_group)
        """

    async def describe_clusters(
        self, **kwargs: Unpack[DescribeClustersRequestTypeDef]
    ) -> DescribeClustersResponseTypeDef:
        """
        Returns information about all provisioned DAX clusters if no cluster identifier
        is specified, or about a specific DAX cluster if a cluster identifier is
        supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_clusters.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_clusters)
        """

    async def describe_default_parameters(
        self, **kwargs: Unpack[DescribeDefaultParametersRequestTypeDef]
    ) -> DescribeDefaultParametersResponseTypeDef:
        """
        Returns the default system parameter information for the DAX caching software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_default_parameters.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_default_parameters)
        """

    async def describe_events(
        self, **kwargs: Unpack[DescribeEventsRequestTypeDef]
    ) -> DescribeEventsResponseTypeDef:
        """
        Returns events related to DAX clusters and parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_events.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_events)
        """

    async def describe_parameter_groups(
        self, **kwargs: Unpack[DescribeParameterGroupsRequestTypeDef]
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        Returns a list of parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_parameter_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_parameter_groups)
        """

    async def describe_parameters(
        self, **kwargs: Unpack[DescribeParametersRequestTypeDef]
    ) -> DescribeParametersResponseTypeDef:
        """
        Returns the detailed parameter list for a particular parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_parameters.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_parameters)
        """

    async def describe_subnet_groups(
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestTypeDef]
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        Returns a list of subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/describe_subnet_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#describe_subnet_groups)
        """

    async def increase_replication_factor(
        self, **kwargs: Unpack[IncreaseReplicationFactorRequestTypeDef]
    ) -> IncreaseReplicationFactorResponseTypeDef:
        """
        Adds one or more nodes to a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/increase_replication_factor.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#increase_replication_factor)
        """

    async def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        List all of the tags for a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/list_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#list_tags)
        """

    async def reboot_node(
        self, **kwargs: Unpack[RebootNodeRequestTypeDef]
    ) -> RebootNodeResponseTypeDef:
        """
        Reboots a single node of a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/reboot_node.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#reboot_node)
        """

    async def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> TagResourceResponseTypeDef:
        """
        Associates a set of tags with a DAX resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#tag_resource)
        """

    async def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> UntagResourceResponseTypeDef:
        """
        Removes the association of tags from a DAX resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#untag_resource)
        """

    async def update_cluster(
        self, **kwargs: Unpack[UpdateClusterRequestTypeDef]
    ) -> UpdateClusterResponseTypeDef:
        """
        Modifies the settings for a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/update_cluster.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#update_cluster)
        """

    async def update_parameter_group(
        self, **kwargs: Unpack[UpdateParameterGroupRequestTypeDef]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/update_parameter_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#update_parameter_group)
        """

    async def update_subnet_group(
        self, **kwargs: Unpack[UpdateSubnetGroupRequestTypeDef]
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        Modifies an existing subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/update_subnet_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#update_subnet_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_default_parameters"]
    ) -> DescribeDefaultParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> DescribeParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> DescribeSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags"]
    ) -> ListTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/client/)
        """
