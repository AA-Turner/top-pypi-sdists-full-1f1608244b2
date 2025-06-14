"""
Main interface for dynamodb service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_dynamodb import (
        Client,
        DynamoDBClient,
        DynamoDBServiceResource,
        ListBackupsPaginator,
        ListTablesPaginator,
        ListTagsOfResourcePaginator,
        QueryPaginator,
        ScanPaginator,
        ServiceResource,
        TableExistsWaiter,
        TableNotExistsWaiter,
    )

    session = get_session()
    async with session.create_client("dynamodb") as client:
        client: DynamoDBClient
        ...


    table_exists_waiter: TableExistsWaiter = client.get_waiter("table_exists")
    table_not_exists_waiter: TableNotExistsWaiter = client.get_waiter("table_not_exists")

    list_backups_paginator: ListBackupsPaginator = client.get_paginator("list_backups")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_of_resource_paginator: ListTagsOfResourcePaginator = client.get_paginator("list_tags_of_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    scan_paginator: ScanPaginator = client.get_paginator("scan")
    ```
"""

from .client import DynamoDBClient
from .paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from .waiter import TableExistsWaiter, TableNotExistsWaiter

try:
    from .service_resource import DynamoDBServiceResource
except ImportError:
    from builtins import object as DynamoDBServiceResource  # type: ignore[assignment]

Client = DynamoDBClient

ServiceResource = DynamoDBServiceResource

__all__ = (
    "Client",
    "DynamoDBClient",
    "DynamoDBServiceResource",
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
    "ServiceResource",
    "TableExistsWaiter",
    "TableNotExistsWaiter",
)
