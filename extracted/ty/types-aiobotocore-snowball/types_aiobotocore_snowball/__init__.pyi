"""
Main interface for snowball service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_snowball/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_snowball import (
        Client,
        DescribeAddressesPaginator,
        ListClusterJobsPaginator,
        ListClustersPaginator,
        ListCompatibleImagesPaginator,
        ListJobsPaginator,
        ListLongTermPricingPaginator,
        SnowballClient,
    )

    session = get_session()
    async with session.create_client("snowball") as client:
        client: SnowballClient
        ...


    describe_addresses_paginator: DescribeAddressesPaginator = client.get_paginator("describe_addresses")
    list_cluster_jobs_paginator: ListClusterJobsPaginator = client.get_paginator("list_cluster_jobs")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compatible_images_paginator: ListCompatibleImagesPaginator = client.get_paginator("list_compatible_images")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_long_term_pricing_paginator: ListLongTermPricingPaginator = client.get_paginator("list_long_term_pricing")
    ```
"""

from .client import SnowballClient
from .paginator import (
    DescribeAddressesPaginator,
    ListClusterJobsPaginator,
    ListClustersPaginator,
    ListCompatibleImagesPaginator,
    ListJobsPaginator,
    ListLongTermPricingPaginator,
)

Client = SnowballClient

__all__ = (
    "Client",
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
    "ListLongTermPricingPaginator",
    "SnowballClient",
)
