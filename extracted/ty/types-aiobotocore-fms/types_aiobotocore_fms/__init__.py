"""
Main interface for fms service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fms/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_fms import (
        Client,
        FMSClient,
        ListAdminAccountsForOrganizationPaginator,
        ListAdminsManagingAccountPaginator,
        ListAppsListsPaginator,
        ListComplianceStatusPaginator,
        ListMemberAccountsPaginator,
        ListPoliciesPaginator,
        ListProtocolsListsPaginator,
        ListThirdPartyFirewallFirewallPoliciesPaginator,
    )

    session = get_session()
    async with session.create_client("fms") as client:
        client: FMSClient
        ...


    list_admin_accounts_for_organization_paginator: ListAdminAccountsForOrganizationPaginator = client.get_paginator("list_admin_accounts_for_organization")
    list_admins_managing_account_paginator: ListAdminsManagingAccountPaginator = client.get_paginator("list_admins_managing_account")
    list_apps_lists_paginator: ListAppsListsPaginator = client.get_paginator("list_apps_lists")
    list_compliance_status_paginator: ListComplianceStatusPaginator = client.get_paginator("list_compliance_status")
    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_protocols_lists_paginator: ListProtocolsListsPaginator = client.get_paginator("list_protocols_lists")
    list_third_party_firewall_firewall_policies_paginator: ListThirdPartyFirewallFirewallPoliciesPaginator = client.get_paginator("list_third_party_firewall_firewall_policies")
    ```
"""

from .client import FMSClient
from .paginator import (
    ListAdminAccountsForOrganizationPaginator,
    ListAdminsManagingAccountPaginator,
    ListAppsListsPaginator,
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
    ListProtocolsListsPaginator,
    ListThirdPartyFirewallFirewallPoliciesPaginator,
)

Client = FMSClient


__all__ = (
    "Client",
    "FMSClient",
    "ListAdminAccountsForOrganizationPaginator",
    "ListAdminsManagingAccountPaginator",
    "ListAppsListsPaginator",
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
    "ListProtocolsListsPaginator",
    "ListThirdPartyFirewallFirewallPoliciesPaginator",
)
