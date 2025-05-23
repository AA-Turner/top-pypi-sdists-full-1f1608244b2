# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceGroupDigestChild(Model):
    """PlaceGroupDigestChild.

    :param place_id:
    :type place_id: int
    :param place_code:
    :type place_code: str
    :param place_info:
    :type place_info: str
    :param place_display:
    :type place_display: str
    :param include_in_charts:
    :type include_in_charts: bool
    """

    _attribute_map = {
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
        'place_display': {'key': 'placeDisplay', 'type': 'str'},
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PlaceGroupDigestChild, self).__init__(**kwargs)
        self.place_id = kwargs.get('place_id', None)
        self.place_code = kwargs.get('place_code', None)
        self.place_info = kwargs.get('place_info', None)
        self.place_display = kwargs.get('place_display', None)
        self.include_in_charts = kwargs.get('include_in_charts', None)
