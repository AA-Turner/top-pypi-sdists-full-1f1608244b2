# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType(ModelSimple):
    """
    Indicates that a predefined library pattern is used.

    :param value: If omitted defaults to "library". Must be one of ["library"].
    :type value: str
    """

    allowed_values = {
        "library",
    }
    LIBRARY: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType.LIBRARY = (
    ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType("library")
)
