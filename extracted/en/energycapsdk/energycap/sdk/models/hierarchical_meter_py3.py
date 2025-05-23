# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HierarchicalMeter(Model):
    """HierarchicalMeter.

    :param has_wattics_data_point: Indicates if the meter has a Smart
     Analytics (Wattics) Data Point link
    :type has_wattics_data_point: bool
    :param has_emission_source: Indicates if the meter has an Emission Source
     link
    :type has_emission_source: bool
    :param meter_id: The meter identifier
    :type meter_id: int
    :param meter_code: The meter code
    :type meter_code: str
    :param meter_info: The meter info
    :type meter_info: str
    :param meter_type:
    :type meter_type: ~energycap.sdk.models.MeterTypeChild
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param active: Indicates whether the Meter is Active
    :type active: bool
    :param is_calculated_meter: Indicates whether the meter is a calculated
     meter
    :type is_calculated_meter: bool
    :param is_split_parent_meter: Indicates whether the meter is a parent of a
     split
    :type is_split_parent_meter: bool
    :param is_split_child_meter: Indicates whether the meter is a child of a
     split
    :type is_split_child_meter: bool
    :param serial_number: The meter's current serial number
    :type serial_number: str
    """

    _attribute_map = {
        'has_wattics_data_point': {'key': 'hasWatticsDataPoint', 'type': 'bool'},
        'has_emission_source': {'key': 'hasEmissionSource', 'type': 'bool'},
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'meter_type': {'key': 'meterType', 'type': 'MeterTypeChild'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'active': {'key': 'active', 'type': 'bool'},
        'is_calculated_meter': {'key': 'isCalculatedMeter', 'type': 'bool'},
        'is_split_parent_meter': {'key': 'isSplitParentMeter', 'type': 'bool'},
        'is_split_child_meter': {'key': 'isSplitChildMeter', 'type': 'bool'},
        'serial_number': {'key': 'serialNumber', 'type': 'str'},
    }

    def __init__(self, *, has_wattics_data_point: bool=None, has_emission_source: bool=None, meter_id: int=None, meter_code: str=None, meter_info: str=None, meter_type=None, commodity=None, active: bool=None, is_calculated_meter: bool=None, is_split_parent_meter: bool=None, is_split_child_meter: bool=None, serial_number: str=None, **kwargs) -> None:
        super(HierarchicalMeter, self).__init__(**kwargs)
        self.has_wattics_data_point = has_wattics_data_point
        self.has_emission_source = has_emission_source
        self.meter_id = meter_id
        self.meter_code = meter_code
        self.meter_info = meter_info
        self.meter_type = meter_type
        self.commodity = commodity
        self.active = active
        self.is_calculated_meter = is_calculated_meter
        self.is_split_parent_meter = is_split_parent_meter
        self.is_split_child_meter = is_split_child_meter
        self.serial_number = serial_number
