"""
Type annotations for resource-groups service client paginators.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_resource_groups.client import ResourceGroupsClient
    from types_aiobotocore_resource_groups.paginator import (
        ListGroupResourcesPaginator,
        ListGroupingStatusesPaginator,
        ListGroupsPaginator,
        ListTagSyncTasksPaginator,
        SearchResourcesPaginator,
    )

    session = get_session()
    with session.create_client("resource-groups") as client:
        client: ResourceGroupsClient

        list_group_resources_paginator: ListGroupResourcesPaginator = client.get_paginator("list_group_resources")
        list_grouping_statuses_paginator: ListGroupingStatusesPaginator = client.get_paginator("list_grouping_statuses")
        list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
        list_tag_sync_tasks_paginator: ListTagSyncTasksPaginator = client.get_paginator("list_tag_sync_tasks")
        search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from aiobotocore.paginate import AioPageIterator, AioPaginator

from .type_defs import (
    ListGroupingStatusesInputPaginateTypeDef,
    ListGroupingStatusesOutputTypeDef,
    ListGroupResourcesInputPaginateTypeDef,
    ListGroupResourcesOutputTypeDef,
    ListGroupsInputPaginateTypeDef,
    ListGroupsOutputTypeDef,
    ListTagSyncTasksInputPaginateTypeDef,
    ListTagSyncTasksOutputTypeDef,
    SearchResourcesInputPaginateTypeDef,
    SearchResourcesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListGroupResourcesPaginator",
    "ListGroupingStatusesPaginator",
    "ListGroupsPaginator",
    "ListTagSyncTasksPaginator",
    "SearchResourcesPaginator",
)


if TYPE_CHECKING:
    _ListGroupResourcesPaginatorBase = AioPaginator[ListGroupResourcesOutputTypeDef]
else:
    _ListGroupResourcesPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListGroupResourcesPaginator(_ListGroupResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroupResources.html#ResourceGroups.Paginator.ListGroupResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupresourcespaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupResourcesInputPaginateTypeDef]
    ) -> AioPageIterator[ListGroupResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroupResources.html#ResourceGroups.Paginator.ListGroupResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupresourcespaginator)
        """


if TYPE_CHECKING:
    _ListGroupingStatusesPaginatorBase = AioPaginator[ListGroupingStatusesOutputTypeDef]
else:
    _ListGroupingStatusesPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListGroupingStatusesPaginator(_ListGroupingStatusesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroupingStatuses.html#ResourceGroups.Paginator.ListGroupingStatuses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupingstatusespaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupingStatusesInputPaginateTypeDef]
    ) -> AioPageIterator[ListGroupingStatusesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroupingStatuses.html#ResourceGroups.Paginator.ListGroupingStatuses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupingstatusespaginator)
        """


if TYPE_CHECKING:
    _ListGroupsPaginatorBase = AioPaginator[ListGroupsOutputTypeDef]
else:
    _ListGroupsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroups.html#ResourceGroups.Paginator.ListGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsInputPaginateTypeDef]
    ) -> AioPageIterator[ListGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListGroups.html#ResourceGroups.Paginator.ListGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listgroupspaginator)
        """


if TYPE_CHECKING:
    _ListTagSyncTasksPaginatorBase = AioPaginator[ListTagSyncTasksOutputTypeDef]
else:
    _ListTagSyncTasksPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListTagSyncTasksPaginator(_ListTagSyncTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListTagSyncTasks.html#ResourceGroups.Paginator.ListTagSyncTasks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listtagsynctaskspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagSyncTasksInputPaginateTypeDef]
    ) -> AioPageIterator[ListTagSyncTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/ListTagSyncTasks.html#ResourceGroups.Paginator.ListTagSyncTasks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#listtagsynctaskspaginator)
        """


if TYPE_CHECKING:
    _SearchResourcesPaginatorBase = AioPaginator[SearchResourcesOutputTypeDef]
else:
    _SearchResourcesPaginatorBase = AioPaginator  # type: ignore[assignment]


class SearchResourcesPaginator(_SearchResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/SearchResources.html#ResourceGroups.Paginator.SearchResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#searchresourcespaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchResourcesInputPaginateTypeDef]
    ) -> AioPageIterator[SearchResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups/paginator/SearchResources.html#ResourceGroups.Paginator.SearchResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resource_groups/paginators/#searchresourcespaginator)
        """
