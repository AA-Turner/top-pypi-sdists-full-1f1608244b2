# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdminSettingsResponse(Model):
    """AdminSettingsResponse.

    :param field_name: The setting field
    :type field_name: str
    :param value: The setting value
    :type value: str
    :param data_type:
    :type data_type: ~energycap.sdk.models.DataTypeResponse
    """

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'DataTypeResponse'},
    }

    def __init__(self, *, field_name: str=None, value: str=None, data_type=None, **kwargs) -> None:
        super(AdminSettingsResponse, self).__init__(**kwargs)
        self.field_name = field_name
        self.value = value
        self.data_type = data_type
