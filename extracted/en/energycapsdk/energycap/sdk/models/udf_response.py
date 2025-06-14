# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UDFResponse(Model):
    """UDFResponse.

    :param udf_id: The identifier of the custom field. <span
     class='property-internal'>Required (defined)</span>
    :type udf_id: int
    :param name: The name of the custom field. <span
     class='property-internal'>Required (defined)</span>
    :type name: str
    :param description: The description for the custom field. <span
     class='property-internal'>Required (defined)</span>
    :type description: str
    :param udf_type: The type of the udf. Values include: Account, Meter,
     Vendor, Place, ChannelVersion, Rate, and Bill. <span
     class='property-internal'>Required (defined)</span>
    :type udf_type: str
    :param data_type:
    :type data_type: ~energycap.sdk.models.DataTypeResponse
    :param display_order: The display order of the custom field. <span
     class='property-internal'>Required (defined)</span>
    :type display_order: int
    :param udf_select_values: Select values of the custom field, if it is a
     select list (DataType = 12). <span class='property-internal'>Required
     (defined)</span>
    :type udf_select_values:
     list[~energycap.sdk.models.UDFSelectValueResponse]
    :param count: The number of times this custom field has been used. <span
     class='property-internal'>Required (defined)</span>
    :type count: int
    :param locked: If true, then this udf is a system custom field <span
     class='property-internal'>Required (defined)</span>
    :type locked: bool
    :param important: If true, this custom field is important. <span
     class='property-internal'>Required (defined)</span>
    :type important: bool
    """

    _attribute_map = {
        'udf_id': {'key': 'udfId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'udf_type': {'key': 'udfType', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'DataTypeResponse'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'udf_select_values': {'key': 'udfSelectValues', 'type': '[UDFSelectValueResponse]'},
        'count': {'key': 'count', 'type': 'int'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'important': {'key': 'important', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(UDFResponse, self).__init__(**kwargs)
        self.udf_id = kwargs.get('udf_id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.udf_type = kwargs.get('udf_type', None)
        self.data_type = kwargs.get('data_type', None)
        self.display_order = kwargs.get('display_order', None)
        self.udf_select_values = kwargs.get('udf_select_values', None)
        self.count = kwargs.get('count', None)
        self.locked = kwargs.get('locked', None)
        self.important = kwargs.get('important', None)
