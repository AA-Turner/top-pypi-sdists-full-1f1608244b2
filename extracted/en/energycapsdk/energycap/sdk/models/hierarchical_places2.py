# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HierarchicalPlaces2(Model):
    """HierarchicalPlaces2.

    :param parent_id:
    :type parent_id: int
    :param place_id:
    :type place_id: int
    :param place_info:
    :type place_info: str
    :param place_code:
    :type place_code: str
    :param place_type_id:
    :type place_type_id: int
    :param has_children:
    :type has_children: bool
    :param has_place_children:
    :type has_place_children: bool
    :param has_meter_children:
    :type has_meter_children: bool
    :param has_active_children:
    :type has_active_children: bool
    :param has_active_meter_children:
    :type has_active_meter_children: bool
    :param meter_children:
    :type meter_children: list[~energycap.sdk.models.HierarchicalMeter]
    :param place_children:
    :type place_children: list[~energycap.sdk.models.HierarchicalPlaces]
    """

    _attribute_map = {
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_type_id': {'key': 'placeTypeId', 'type': 'int'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'has_place_children': {'key': 'hasPlaceChildren', 'type': 'bool'},
        'has_meter_children': {'key': 'hasMeterChildren', 'type': 'bool'},
        'has_active_children': {'key': 'hasActiveChildren', 'type': 'bool'},
        'has_active_meter_children': {'key': 'hasActiveMeterChildren', 'type': 'bool'},
        'meter_children': {'key': 'meterChildren', 'type': '[HierarchicalMeter]'},
        'place_children': {'key': 'placeChildren', 'type': '[HierarchicalPlaces]'},
    }

    def __init__(self, **kwargs):
        super(HierarchicalPlaces2, self).__init__(**kwargs)
        self.parent_id = kwargs.get('parent_id', None)
        self.place_id = kwargs.get('place_id', None)
        self.place_info = kwargs.get('place_info', None)
        self.place_code = kwargs.get('place_code', None)
        self.place_type_id = kwargs.get('place_type_id', None)
        self.has_children = kwargs.get('has_children', None)
        self.has_place_children = kwargs.get('has_place_children', None)
        self.has_meter_children = kwargs.get('has_meter_children', None)
        self.has_active_children = kwargs.get('has_active_children', None)
        self.has_active_meter_children = kwargs.get('has_active_meter_children', None)
        self.meter_children = kwargs.get('meter_children', None)
        self.place_children = kwargs.get('place_children', None)
