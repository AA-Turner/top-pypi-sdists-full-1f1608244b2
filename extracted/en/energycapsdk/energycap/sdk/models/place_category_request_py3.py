# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceCategoryRequest(Model):
    """PlaceCategoryRequest.

    All required parameters must be populated in order to send to Azure.

    :param place_group_category_info: Required. The place category info <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type place_group_category_info: str
    :param place_group_category_code: Required. The place category code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type place_group_category_code: str
    """

    _validation = {
        'place_group_category_info': {'required': True, 'max_length': 32, 'min_length': 0},
        'place_group_category_code': {'required': True, 'max_length': 32, 'min_length': 0},
    }

    _attribute_map = {
        'place_group_category_info': {'key': 'placeGroupCategoryInfo', 'type': 'str'},
        'place_group_category_code': {'key': 'placeGroupCategoryCode', 'type': 'str'},
    }

    def __init__(self, *, place_group_category_info: str, place_group_category_code: str, **kwargs) -> None:
        super(PlaceCategoryRequest, self).__init__(**kwargs)
        self.place_group_category_info = place_group_category_info
        self.place_group_category_code = place_group_category_code
