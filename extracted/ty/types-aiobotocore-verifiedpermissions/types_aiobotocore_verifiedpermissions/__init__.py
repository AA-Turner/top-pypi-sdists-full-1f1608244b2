"""
Main interface for verifiedpermissions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_verifiedpermissions import (
        Client,
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
        VerifiedPermissionsClient,
    )

    session = get_session()
    async with session.create_client("verifiedpermissions") as client:
        client: VerifiedPermissionsClient
        ...


    list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_stores_paginator: ListPolicyStoresPaginator = client.get_paginator("list_policy_stores")
    list_policy_templates_paginator: ListPolicyTemplatesPaginator = client.get_paginator("list_policy_templates")
    ```
"""

from .client import VerifiedPermissionsClient
from .paginator import (
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyStoresPaginator,
    ListPolicyTemplatesPaginator,
)

Client = VerifiedPermissionsClient


__all__ = (
    "Client",
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyStoresPaginator",
    "ListPolicyTemplatesPaginator",
    "VerifiedPermissionsClient",
)
