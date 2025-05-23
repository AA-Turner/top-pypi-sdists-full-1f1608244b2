# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.convert_job_results_to_signals_attributes import (
        ConvertJobResultsToSignalsAttributes,
    )
    from datadog_api_client.v2.model.convert_job_results_to_signals_data_type import ConvertJobResultsToSignalsDataType


class ConvertJobResultsToSignalsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.convert_job_results_to_signals_attributes import (
            ConvertJobResultsToSignalsAttributes,
        )
        from datadog_api_client.v2.model.convert_job_results_to_signals_data_type import (
            ConvertJobResultsToSignalsDataType,
        )

        return {
            "attributes": (ConvertJobResultsToSignalsAttributes,),
            "type": (ConvertJobResultsToSignalsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ConvertJobResultsToSignalsAttributes, UnsetType] = unset,
        type: Union[ConvertJobResultsToSignalsDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for converting historical job results to signals.

        :param attributes: Attributes for converting historical job results to signals.
        :type attributes: ConvertJobResultsToSignalsAttributes, optional

        :param type: Type of payload.
        :type type: ConvertJobResultsToSignalsDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
