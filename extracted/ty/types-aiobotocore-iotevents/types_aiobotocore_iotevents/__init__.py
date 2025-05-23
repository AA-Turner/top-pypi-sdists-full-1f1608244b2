"""
Main interface for iotevents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_iotevents import (
        Client,
        IoTEventsClient,
    )

    session = get_session()
    async with session.create_client("iotevents") as client:
        client: IoTEventsClient
        ...

    ```
"""

from .client import IoTEventsClient

Client = IoTEventsClient


__all__ = ("Client", "IoTEventsClient")
