# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergyStarPlaceMetricsRequest(Model):
    """EnergyStarPlaceMetricsRequest.

    All required parameters must be populated in order to send to Azure.

    :param begin_period: Required. The begin period for updating ENERGY STAR
     metrics <span class='property-internal'>Required</span>
    :type begin_period: int
    :param end_period: The end period for updating ENERGY STAR metrics
     If null, metrics will only be retrieved for the period specified in
     BeginPeriod
    :type end_period: int
    :param place_ids: Required. List of place identifiers to for which to
     update metrics <span class='property-internal'>Required</span> <span
     class='property-internal'>Cannot be Empty</span>
    :type place_ids: list[int]
    """

    _validation = {
        'begin_period': {'required': True},
        'place_ids': {'required': True},
    }

    _attribute_map = {
        'begin_period': {'key': 'beginPeriod', 'type': 'int'},
        'end_period': {'key': 'endPeriod', 'type': 'int'},
        'place_ids': {'key': 'placeIds', 'type': '[int]'},
    }

    def __init__(self, *, begin_period: int, place_ids, end_period: int=None, **kwargs) -> None:
        super(EnergyStarPlaceMetricsRequest, self).__init__(**kwargs)
        self.begin_period = begin_period
        self.end_period = end_period
        self.place_ids = place_ids
