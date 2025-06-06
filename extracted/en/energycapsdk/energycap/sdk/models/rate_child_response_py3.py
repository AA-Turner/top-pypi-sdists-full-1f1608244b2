# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RateChildResponse(Model):
    """RateChildResponse.

    :param rate_id:
    :type rate_id: int
    :param name:
    :type name: str
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    """

    _attribute_map = {
        'rate_id': {'key': 'rateId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
    }

    def __init__(self, *, rate_id: int=None, name: str=None, commodity=None, **kwargs) -> None:
        super(RateChildResponse, self).__init__(**kwargs)
        self.rate_id = rate_id
        self.name = name
        self.commodity = commodity
