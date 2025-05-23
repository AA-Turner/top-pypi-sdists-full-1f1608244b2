"""
Main interface for shield service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_shield/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_shield import (
        Client,
        ListAttacksPaginator,
        ListProtectionsPaginator,
        ShieldClient,
    )

    session = get_session()
    async with session.create_client("shield") as client:
        client: ShieldClient
        ...


    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
    ```
"""

from .client import ShieldClient
from .paginator import ListAttacksPaginator, ListProtectionsPaginator

Client = ShieldClient

__all__ = ("Client", "ListAttacksPaginator", "ListProtectionsPaginator", "ShieldClient")
