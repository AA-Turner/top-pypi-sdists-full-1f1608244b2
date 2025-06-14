"""
Main interface for evidently service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_evidently/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_evidently import (
        Client,
        CloudWatchEvidentlyClient,
        ListExperimentsPaginator,
        ListFeaturesPaginator,
        ListLaunchesPaginator,
        ListProjectsPaginator,
        ListSegmentReferencesPaginator,
        ListSegmentsPaginator,
    )

    session = get_session()
    async with session.create_client("evidently") as client:
        client: CloudWatchEvidentlyClient
        ...


    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_features_paginator: ListFeaturesPaginator = client.get_paginator("list_features")
    list_launches_paginator: ListLaunchesPaginator = client.get_paginator("list_launches")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_segment_references_paginator: ListSegmentReferencesPaginator = client.get_paginator("list_segment_references")
    list_segments_paginator: ListSegmentsPaginator = client.get_paginator("list_segments")
    ```
"""

from .client import CloudWatchEvidentlyClient
from .paginator import (
    ListExperimentsPaginator,
    ListFeaturesPaginator,
    ListLaunchesPaginator,
    ListProjectsPaginator,
    ListSegmentReferencesPaginator,
    ListSegmentsPaginator,
)

Client = CloudWatchEvidentlyClient

__all__ = (
    "Client",
    "CloudWatchEvidentlyClient",
    "ListExperimentsPaginator",
    "ListFeaturesPaginator",
    "ListLaunchesPaginator",
    "ListProjectsPaginator",
    "ListSegmentReferencesPaginator",
    "ListSegmentsPaginator",
)
