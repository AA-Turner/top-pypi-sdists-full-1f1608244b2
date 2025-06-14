"""
Main interface for iotdeviceadvisor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotdeviceadvisor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_iotdeviceadvisor import (
        Client,
        IoTDeviceAdvisorClient,
    )

    session = get_session()
    async with session.create_client("iotdeviceadvisor") as client:
        client: IoTDeviceAdvisorClient
        ...

    ```
"""

from .client import IoTDeviceAdvisorClient

Client = IoTDeviceAdvisorClient

__all__ = ("Client", "IoTDeviceAdvisorClient")
