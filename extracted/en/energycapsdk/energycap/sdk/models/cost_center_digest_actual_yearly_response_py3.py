# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CostCenterDigestActualYearlyResponse(Model):
    """CostCenterDigestActualYearlyResponse.

    :param cost_center_code: The costCenter code
    :type cost_center_code: str
    :param cost_center_info: The costCenter info
    :type cost_center_info: str
    :param cost_center_id: The costCenter identifier
    :type cost_center_id: int
    :param global_use_unit:
    :type global_use_unit: ~energycap.sdk.models.UnitChild
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param updated: The date and time the data was updated
    :type updated: datetime
    :param results: An array of yearly data
    :type results:
     list[~energycap.sdk.models.CostCenterDigestActualYearlyResponseResults]
    :param commodities: An array of yearly data per commodity
    :type commodities:
     list[~energycap.sdk.models.CostCenterDigestActualYearlyResponseCommodityData]
    """

    _attribute_map = {
        'cost_center_code': {'key': 'costCenterCode', 'type': 'str'},
        'cost_center_info': {'key': 'costCenterInfo', 'type': 'str'},
        'cost_center_id': {'key': 'costCenterId', 'type': 'int'},
        'global_use_unit': {'key': 'globalUseUnit', 'type': 'UnitChild'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'results': {'key': 'results', 'type': '[CostCenterDigestActualYearlyResponseResults]'},
        'commodities': {'key': 'commodities', 'type': '[CostCenterDigestActualYearlyResponseCommodityData]'},
    }

    def __init__(self, *, cost_center_code: str=None, cost_center_info: str=None, cost_center_id: int=None, global_use_unit=None, cost_unit=None, updated=None, results=None, commodities=None, **kwargs) -> None:
        super(CostCenterDigestActualYearlyResponse, self).__init__(**kwargs)
        self.cost_center_code = cost_center_code
        self.cost_center_info = cost_center_info
        self.cost_center_id = cost_center_id
        self.global_use_unit = global_use_unit
        self.cost_unit = cost_unit
        self.updated = updated
        self.results = results
        self.commodities = commodities
