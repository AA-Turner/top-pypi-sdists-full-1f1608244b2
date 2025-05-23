"""
Main interface for codestar-notifications service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_codestar_notifications import (
        Client,
        CodeStarNotificationsClient,
        ListEventTypesPaginator,
        ListNotificationRulesPaginator,
        ListTargetsPaginator,
    )

    session = Session()
    client: CodeStarNotificationsClient = session.client("codestar-notifications")

    list_event_types_paginator: ListEventTypesPaginator = client.get_paginator("list_event_types")
    list_notification_rules_paginator: ListNotificationRulesPaginator = client.get_paginator("list_notification_rules")
    list_targets_paginator: ListTargetsPaginator = client.get_paginator("list_targets")
    ```
"""

from .client import CodeStarNotificationsClient
from .paginator import ListEventTypesPaginator, ListNotificationRulesPaginator, ListTargetsPaginator

Client = CodeStarNotificationsClient


__all__ = (
    "Client",
    "CodeStarNotificationsClient",
    "ListEventTypesPaginator",
    "ListNotificationRulesPaginator",
    "ListTargetsPaginator",
)
