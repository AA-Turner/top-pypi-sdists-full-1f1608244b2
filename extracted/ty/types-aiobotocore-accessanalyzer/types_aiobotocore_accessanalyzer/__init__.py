"""
Main interface for accessanalyzer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_accessanalyzer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_accessanalyzer import (
        AccessAnalyzerClient,
        Client,
        GetFindingRecommendationPaginator,
        GetFindingV2Paginator,
        ListAccessPreviewFindingsPaginator,
        ListAccessPreviewsPaginator,
        ListAnalyzedResourcesPaginator,
        ListAnalyzersPaginator,
        ListArchiveRulesPaginator,
        ListFindingsPaginator,
        ListFindingsV2Paginator,
        ListPolicyGenerationsPaginator,
        ValidatePolicyPaginator,
    )

    session = get_session()
    async with session.create_client("accessanalyzer") as client:
        client: AccessAnalyzerClient
        ...


    get_finding_recommendation_paginator: GetFindingRecommendationPaginator = client.get_paginator("get_finding_recommendation")
    get_finding_v2_paginator: GetFindingV2Paginator = client.get_paginator("get_finding_v2")
    list_access_preview_findings_paginator: ListAccessPreviewFindingsPaginator = client.get_paginator("list_access_preview_findings")
    list_access_previews_paginator: ListAccessPreviewsPaginator = client.get_paginator("list_access_previews")
    list_analyzed_resources_paginator: ListAnalyzedResourcesPaginator = client.get_paginator("list_analyzed_resources")
    list_analyzers_paginator: ListAnalyzersPaginator = client.get_paginator("list_analyzers")
    list_archive_rules_paginator: ListArchiveRulesPaginator = client.get_paginator("list_archive_rules")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_findings_v2_paginator: ListFindingsV2Paginator = client.get_paginator("list_findings_v2")
    list_policy_generations_paginator: ListPolicyGenerationsPaginator = client.get_paginator("list_policy_generations")
    validate_policy_paginator: ValidatePolicyPaginator = client.get_paginator("validate_policy")
    ```
"""

from .client import AccessAnalyzerClient
from .paginator import (
    GetFindingRecommendationPaginator,
    GetFindingV2Paginator,
    ListAccessPreviewFindingsPaginator,
    ListAccessPreviewsPaginator,
    ListAnalyzedResourcesPaginator,
    ListAnalyzersPaginator,
    ListArchiveRulesPaginator,
    ListFindingsPaginator,
    ListFindingsV2Paginator,
    ListPolicyGenerationsPaginator,
    ValidatePolicyPaginator,
)

Client = AccessAnalyzerClient


__all__ = (
    "AccessAnalyzerClient",
    "Client",
    "GetFindingRecommendationPaginator",
    "GetFindingV2Paginator",
    "ListAccessPreviewFindingsPaginator",
    "ListAccessPreviewsPaginator",
    "ListAnalyzedResourcesPaginator",
    "ListAnalyzersPaginator",
    "ListArchiveRulesPaginator",
    "ListFindingsPaginator",
    "ListFindingsV2Paginator",
    "ListPolicyGenerationsPaginator",
    "ValidatePolicyPaginator",
)
