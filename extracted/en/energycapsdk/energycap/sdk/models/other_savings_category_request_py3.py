# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OtherSavingsCategoryRequest(Model):
    """OtherSavingsCategoryRequest.

    :param other_savings_category_info: Other savings category name
    :type other_savings_category_info: str
    """

    _attribute_map = {
        'other_savings_category_info': {'key': 'otherSavingsCategoryInfo', 'type': 'str'},
    }

    def __init__(self, *, other_savings_category_info: str=None, **kwargs) -> None:
        super(OtherSavingsCategoryRequest, self).__init__(**kwargs)
        self.other_savings_category_info = other_savings_category_info
