"""
Main interface for guardduty service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_guardduty/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_guardduty import (
        Client,
        DescribeMalwareScansPaginator,
        GuardDutyClient,
        ListCoveragePaginator,
        ListDetectorsPaginator,
        ListFiltersPaginator,
        ListFindingsPaginator,
        ListIPSetsPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListThreatIntelSetsPaginator,
    )

    session = get_session()
    async with session.create_client("guardduty") as client:
        client: GuardDutyClient
        ...


    describe_malware_scans_paginator: DescribeMalwareScansPaginator = client.get_paginator("describe_malware_scans")
    list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
    list_detectors_paginator: ListDetectorsPaginator = client.get_paginator("list_detectors")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_threat_intel_sets_paginator: ListThreatIntelSetsPaginator = client.get_paginator("list_threat_intel_sets")
    ```
"""

from .client import GuardDutyClient
from .paginator import (
    DescribeMalwareScansPaginator,
    ListCoveragePaginator,
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatIntelSetsPaginator,
)

Client = GuardDutyClient

__all__ = (
    "Client",
    "DescribeMalwareScansPaginator",
    "GuardDutyClient",
    "ListCoveragePaginator",
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListThreatIntelSetsPaginator",
)
