"""
Type annotations for cloud9 service client paginators.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_cloud9.client import Cloud9Client
    from types_aiobotocore_cloud9.paginator import (
        DescribeEnvironmentMembershipsPaginator,
        ListEnvironmentsPaginator,
    )

    session = get_session()
    with session.create_client("cloud9") as client:
        client: Cloud9Client

        describe_environment_memberships_paginator: DescribeEnvironmentMembershipsPaginator = client.get_paginator("describe_environment_memberships")
        list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from aiobotocore.paginate import AioPageIterator, AioPaginator

from .type_defs import (
    DescribeEnvironmentMembershipsRequestPaginateTypeDef,
    DescribeEnvironmentMembershipsResultTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("DescribeEnvironmentMembershipsPaginator", "ListEnvironmentsPaginator")


if TYPE_CHECKING:
    _DescribeEnvironmentMembershipsPaginatorBase = AioPaginator[
        DescribeEnvironmentMembershipsResultTypeDef
    ]
else:
    _DescribeEnvironmentMembershipsPaginatorBase = AioPaginator  # type: ignore[assignment]


class DescribeEnvironmentMembershipsPaginator(_DescribeEnvironmentMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/DescribeEnvironmentMemberships.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/paginators/#describeenvironmentmembershipspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEnvironmentMembershipsRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeEnvironmentMembershipsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/DescribeEnvironmentMemberships.html#Cloud9.Paginator.DescribeEnvironmentMemberships.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/paginators/#describeenvironmentmembershipspaginator)
        """


if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = AioPaginator[ListEnvironmentsResultTypeDef]
else:
    _ListEnvironmentsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/ListEnvironments.html#Cloud9.Paginator.ListEnvironments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/paginators/#listenvironmentspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> AioPageIterator[ListEnvironmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9/paginator/ListEnvironments.html#Cloud9.Paginator.ListEnvironments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloud9/paginators/#listenvironmentspaginator)
        """
