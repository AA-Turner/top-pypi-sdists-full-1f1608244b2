"""
Main interface for mturk service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mturk import (
        Client,
        ListAssignmentsForHITPaginator,
        ListBonusPaymentsPaginator,
        ListHITsForQualificationTypePaginator,
        ListHITsPaginator,
        ListQualificationRequestsPaginator,
        ListQualificationTypesPaginator,
        ListReviewableHITsPaginator,
        ListWorkerBlocksPaginator,
        ListWorkersWithQualificationTypePaginator,
        MTurkClient,
    )

    session = Session()
    client: MTurkClient = session.client("mturk")

    list_assignments_for_hit_paginator: ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
    list_bonus_payments_paginator: ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
    list_hits_for_qualification_type_paginator: ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
    list_hits_paginator: ListHITsPaginator = client.get_paginator("list_hits")
    list_qualification_requests_paginator: ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
    list_qualification_types_paginator: ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
    list_reviewable_hits_paginator: ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
    list_worker_blocks_paginator: ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
    list_workers_with_qualification_type_paginator: ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
    ```
"""

from .client import MTurkClient
from .paginator import (
    ListAssignmentsForHITPaginator,
    ListBonusPaymentsPaginator,
    ListHITsForQualificationTypePaginator,
    ListHITsPaginator,
    ListQualificationRequestsPaginator,
    ListQualificationTypesPaginator,
    ListReviewableHITsPaginator,
    ListWorkerBlocksPaginator,
    ListWorkersWithQualificationTypePaginator,
)

Client = MTurkClient


__all__ = (
    "Client",
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListHITsPaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
    "MTurkClient",
)
