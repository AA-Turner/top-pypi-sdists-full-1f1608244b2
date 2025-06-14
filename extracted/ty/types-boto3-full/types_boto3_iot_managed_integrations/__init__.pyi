"""
Main interface for iot-managed-integrations service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iot_managed_integrations/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_iot_managed_integrations import (
        Client,
        ListCredentialLockersPaginator,
        ListDestinationsPaginator,
        ListEventLogConfigurationsPaginator,
        ListManagedThingSchemasPaginator,
        ListManagedThingsPaginator,
        ListNotificationConfigurationsPaginator,
        ListOtaTaskConfigurationsPaginator,
        ListOtaTaskExecutionsPaginator,
        ListOtaTasksPaginator,
        ListProvisioningProfilesPaginator,
        ListSchemaVersionsPaginator,
        ManagedintegrationsforIoTDeviceManagementClient,
    )

    session = Session()
    client: ManagedintegrationsforIoTDeviceManagementClient = session.client("iot-managed-integrations")

    list_credential_lockers_paginator: ListCredentialLockersPaginator = client.get_paginator("list_credential_lockers")
    list_destinations_paginator: ListDestinationsPaginator = client.get_paginator("list_destinations")
    list_event_log_configurations_paginator: ListEventLogConfigurationsPaginator = client.get_paginator("list_event_log_configurations")
    list_managed_thing_schemas_paginator: ListManagedThingSchemasPaginator = client.get_paginator("list_managed_thing_schemas")
    list_managed_things_paginator: ListManagedThingsPaginator = client.get_paginator("list_managed_things")
    list_notification_configurations_paginator: ListNotificationConfigurationsPaginator = client.get_paginator("list_notification_configurations")
    list_ota_task_configurations_paginator: ListOtaTaskConfigurationsPaginator = client.get_paginator("list_ota_task_configurations")
    list_ota_task_executions_paginator: ListOtaTaskExecutionsPaginator = client.get_paginator("list_ota_task_executions")
    list_ota_tasks_paginator: ListOtaTasksPaginator = client.get_paginator("list_ota_tasks")
    list_provisioning_profiles_paginator: ListProvisioningProfilesPaginator = client.get_paginator("list_provisioning_profiles")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    ```
"""

from .client import ManagedintegrationsforIoTDeviceManagementClient
from .paginator import (
    ListCredentialLockersPaginator,
    ListDestinationsPaginator,
    ListEventLogConfigurationsPaginator,
    ListManagedThingSchemasPaginator,
    ListManagedThingsPaginator,
    ListNotificationConfigurationsPaginator,
    ListOtaTaskConfigurationsPaginator,
    ListOtaTaskExecutionsPaginator,
    ListOtaTasksPaginator,
    ListProvisioningProfilesPaginator,
    ListSchemaVersionsPaginator,
)

Client = ManagedintegrationsforIoTDeviceManagementClient

__all__ = (
    "Client",
    "ListCredentialLockersPaginator",
    "ListDestinationsPaginator",
    "ListEventLogConfigurationsPaginator",
    "ListManagedThingSchemasPaginator",
    "ListManagedThingsPaginator",
    "ListNotificationConfigurationsPaginator",
    "ListOtaTaskConfigurationsPaginator",
    "ListOtaTaskExecutionsPaginator",
    "ListOtaTasksPaginator",
    "ListProvisioningProfilesPaginator",
    "ListSchemaVersionsPaginator",
    "ManagedintegrationsforIoTDeviceManagementClient",
)
