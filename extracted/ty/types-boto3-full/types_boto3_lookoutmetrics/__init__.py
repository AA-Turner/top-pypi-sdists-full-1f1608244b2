"""
Main interface for lookoutmetrics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutmetrics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_lookoutmetrics import (
        Client,
        LookoutMetricsClient,
    )

    session = Session()
    client: LookoutMetricsClient = session.client("lookoutmetrics")
    ```
"""

from .client import LookoutMetricsClient

Client = LookoutMetricsClient


__all__ = ("Client", "LookoutMetricsClient")
