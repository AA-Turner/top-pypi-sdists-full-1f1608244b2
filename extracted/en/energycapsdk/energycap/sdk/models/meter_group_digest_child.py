# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterGroupDigestChild(Model):
    """MeterGroupDigestChild.

    :param meter_id:
    :type meter_id: int
    :param meter_code:
    :type meter_code: str
    :param meter_info:
    :type meter_info: str
    :param meter_display:
    :type meter_display: str
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param include_in_charts:
    :type include_in_charts: bool
    :param active: Indicates whether the Meter is Active
    :type active: bool
    :param is_calculated_meter: Indicates whether the Meter is a calculated
     meter
    :type is_calculated_meter: bool
    :param is_split_parent_meter: Indicates whether the Meter is a parent of a
     split
    :type is_split_parent_meter: bool
    :param is_split_child_meter: Indicates whether the Meter is a child of a
     split
    :type is_split_child_meter: bool
    """

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'meter_display': {'key': 'meterDisplay', 'type': 'str'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
        'active': {'key': 'active', 'type': 'bool'},
        'is_calculated_meter': {'key': 'isCalculatedMeter', 'type': 'bool'},
        'is_split_parent_meter': {'key': 'isSplitParentMeter', 'type': 'bool'},
        'is_split_child_meter': {'key': 'isSplitChildMeter', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(MeterGroupDigestChild, self).__init__(**kwargs)
        self.meter_id = kwargs.get('meter_id', None)
        self.meter_code = kwargs.get('meter_code', None)
        self.meter_info = kwargs.get('meter_info', None)
        self.meter_display = kwargs.get('meter_display', None)
        self.commodity = kwargs.get('commodity', None)
        self.include_in_charts = kwargs.get('include_in_charts', None)
        self.active = kwargs.get('active', None)
        self.is_calculated_meter = kwargs.get('is_calculated_meter', None)
        self.is_split_parent_meter = kwargs.get('is_split_parent_meter', None)
        self.is_split_child_meter = kwargs.get('is_split_child_meter', None)
