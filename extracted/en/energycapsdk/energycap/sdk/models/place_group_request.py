# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceGroupRequest(Model):
    """PlaceGroupRequest.

    All required parameters must be populated in order to send to Azure.

    :param place_group_info: Required. The place group info <span
     class='property-internal'>Must be between 0 and 255 characters</span>
     <span class='property-internal'>Required</span>
    :type place_group_info: str
    :param place_group_category_id: Required. The place group category <span
     class='property-internal'>Required</span>
    :type place_group_category_id: int
    :param limit_members_by_topmost: Required. Should this group only return
     members within the current user's topmost <span
     class='property-internal'>Required</span>
    :type limit_members_by_topmost: bool
    :param automatic_group_filters: List of filters to add members to an
     automatic place group
     Either AutomaticGroupFilters or ManualGroupMembers, but not both, must be
     passed in <span class='property-internal'>Cannot be Empty</span> <span
     class='property-internal'>NULL Valid</span>
    :type automatic_group_filters: list[~energycap.sdk.models.FilterEdit]
    :param manual_group_members: List of members to add to the group
     Either AutomaticGroupFilters or ManualGroupMembers, but not both, must be
     passed in
     Members but be within the current user's topmost
     You can create an empty group by passing in an empty array
    :type manual_group_members: list[int]
    """

    _validation = {
        'place_group_info': {'required': True, 'max_length': 255, 'min_length': 0},
        'place_group_category_id': {'required': True},
        'limit_members_by_topmost': {'required': True},
    }

    _attribute_map = {
        'place_group_info': {'key': 'placeGroupInfo', 'type': 'str'},
        'place_group_category_id': {'key': 'placeGroupCategoryId', 'type': 'int'},
        'limit_members_by_topmost': {'key': 'limitMembersByTopmost', 'type': 'bool'},
        'automatic_group_filters': {'key': 'automaticGroupFilters', 'type': '[FilterEdit]'},
        'manual_group_members': {'key': 'manualGroupMembers', 'type': '[int]'},
    }

    def __init__(self, **kwargs):
        super(PlaceGroupRequest, self).__init__(**kwargs)
        self.place_group_info = kwargs.get('place_group_info', None)
        self.place_group_category_id = kwargs.get('place_group_category_id', None)
        self.limit_members_by_topmost = kwargs.get('limit_members_by_topmost', None)
        self.automatic_group_filters = kwargs.get('automatic_group_filters', None)
        self.manual_group_members = kwargs.get('manual_group_members', None)
