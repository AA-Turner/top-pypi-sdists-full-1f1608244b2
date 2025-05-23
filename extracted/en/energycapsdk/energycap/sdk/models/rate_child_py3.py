# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RateChild(Model):
    """RateChild.

    :param rate_id:
    :type rate_id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'rate_id': {'key': 'rateId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, rate_id: int=None, name: str=None, **kwargs) -> None:
        super(RateChild, self).__init__(**kwargs)
        self.rate_id = rate_id
        self.name = name
