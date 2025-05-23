"""
Main interface for panorama service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_panorama/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_panorama import (
        Client,
        PanoramaClient,
    )

    session = Session()
    client: PanoramaClient = session.client("panorama")
    ```
"""

from .client import PanoramaClient

Client = PanoramaClient


__all__ = ("Client", "PanoramaClient")
