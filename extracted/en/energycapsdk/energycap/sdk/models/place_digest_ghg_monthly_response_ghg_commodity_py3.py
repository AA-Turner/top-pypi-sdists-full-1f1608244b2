# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestGHGMonthlyResponseGHGCommodity(Model):
    """PlaceDigestGHGMonthlyResponseGHGCommodity.

    :param commodity_id: Commodity Id
    :type commodity_id: int
    :param commodity_code: Commodity Code
    :type commodity_code: str
    :param commodity_info: Commodity info
    :type commodity_info: str
    :param target_comparison:
    :type target_comparison:
     ~energycap.sdk.models.PlaceDigestGHGMonthlyResponseTargetComparison
    :param results: An array of monthly data
    :type results:
     list[~energycap.sdk.models.PlaceDigestGHGMonthlyResponseResults]
    """

    _attribute_map = {
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'commodity_code': {'key': 'commodityCode', 'type': 'str'},
        'commodity_info': {'key': 'commodityInfo', 'type': 'str'},
        'target_comparison': {'key': 'targetComparison', 'type': 'PlaceDigestGHGMonthlyResponseTargetComparison'},
        'results': {'key': 'results', 'type': '[PlaceDigestGHGMonthlyResponseResults]'},
    }

    def __init__(self, *, commodity_id: int=None, commodity_code: str=None, commodity_info: str=None, target_comparison=None, results=None, **kwargs) -> None:
        super(PlaceDigestGHGMonthlyResponseGHGCommodity, self).__init__(**kwargs)
        self.commodity_id = commodity_id
        self.commodity_code = commodity_code
        self.commodity_info = commodity_info
        self.target_comparison = target_comparison
        self.results = results
