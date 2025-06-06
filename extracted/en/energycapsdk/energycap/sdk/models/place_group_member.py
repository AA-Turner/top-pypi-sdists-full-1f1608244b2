# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceGroupMember(Model):
    """PlaceGroupMember.

    :param place_group_id: The place group this place will belong to <span
     class='property-internal'>Required (defined)</span>
    :type place_group_id: int
    :param include_in_charts: Whether to include this place in the group's
     benchmark charts <span class='property-internal'>Required (defined)</span>
    :type include_in_charts: bool
    """

    _attribute_map = {
        'place_group_id': {'key': 'placeGroupId', 'type': 'int'},
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PlaceGroupMember, self).__init__(**kwargs)
        self.place_group_id = kwargs.get('place_group_id', None)
        self.include_in_charts = kwargs.get('include_in_charts', None)
