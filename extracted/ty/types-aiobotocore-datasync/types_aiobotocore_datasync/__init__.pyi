"""
Main interface for datasync service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_datasync import (
        Client,
        DataSyncClient,
        DescribeStorageSystemResourceMetricsPaginator,
        ListAgentsPaginator,
        ListDiscoveryJobsPaginator,
        ListLocationsPaginator,
        ListStorageSystemsPaginator,
        ListTagsForResourcePaginator,
        ListTaskExecutionsPaginator,
        ListTasksPaginator,
    )

    session = get_session()
    async with session.create_client("datasync") as client:
        client: DataSyncClient
        ...


    describe_storage_system_resource_metrics_paginator: DescribeStorageSystemResourceMetricsPaginator = client.get_paginator("describe_storage_system_resource_metrics")
    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_discovery_jobs_paginator: ListDiscoveryJobsPaginator = client.get_paginator("list_discovery_jobs")
    list_locations_paginator: ListLocationsPaginator = client.get_paginator("list_locations")
    list_storage_systems_paginator: ListStorageSystemsPaginator = client.get_paginator("list_storage_systems")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_task_executions_paginator: ListTaskExecutionsPaginator = client.get_paginator("list_task_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""

from .client import DataSyncClient
from .paginator import (
    DescribeStorageSystemResourceMetricsPaginator,
    ListAgentsPaginator,
    ListDiscoveryJobsPaginator,
    ListLocationsPaginator,
    ListStorageSystemsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)

Client = DataSyncClient

__all__ = (
    "Client",
    "DataSyncClient",
    "DescribeStorageSystemResourceMetricsPaginator",
    "ListAgentsPaginator",
    "ListDiscoveryJobsPaginator",
    "ListLocationsPaginator",
    "ListStorageSystemsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)
