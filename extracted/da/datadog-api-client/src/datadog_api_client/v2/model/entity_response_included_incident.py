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
    from datadog_api_client.v2.model.entity_response_included_related_incident_attributes import (
        EntityResponseIncludedRelatedIncidentAttributes,
    )
    from datadog_api_client.v2.model.entity_response_included_incident_type import EntityResponseIncludedIncidentType


class EntityResponseIncludedIncident(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_included_related_incident_attributes import (
            EntityResponseIncludedRelatedIncidentAttributes,
        )
        from datadog_api_client.v2.model.entity_response_included_incident_type import (
            EntityResponseIncludedIncidentType,
        )

        return {
            "attributes": (EntityResponseIncludedRelatedIncidentAttributes,),
            "id": (str,),
            "type": (EntityResponseIncludedIncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[EntityResponseIncludedRelatedIncidentAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[EntityResponseIncludedIncidentType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included incident.

        :param attributes: Incident attributes.
        :type attributes: EntityResponseIncludedRelatedIncidentAttributes, optional

        :param id: Incident ID.
        :type id: str, optional

        :param type: Incident description.
        :type type: EntityResponseIncludedIncidentType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
