# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WidgetCreate(Model):
    """WidgetCreate.

    All required parameters must be populated in order to send to Azure.

    :param widget_id: Required. Widget identifier <span
     class='property-internal'>Required</span>
    :type widget_id: int
    :param row: Required. Dashboard row <span
     class='property-internal'>Required</span>
    :type row: int
    :param col: Required. Dashboard column <span
     class='property-internal'>Required</span>
    :type col: int
    :param height: Required. Widget height <span
     class='property-internal'>Required</span>
    :type height: int
    :param width: Required. Widget width <span
     class='property-internal'>Required</span>
    :type width: int
    :param title: Required. Personal Widget title <span
     class='property-internal'>Must be between 0 and 600 characters</span>
     <span class='property-internal'>Required</span>
    :type title: str
    :param user_widget_description: Personal Widget description <span
     class='property-internal'>Must be between 0 and 600 characters</span>
    :type user_widget_description: str
    :param filters: Widget filters
    :type filters: list[~energycap.sdk.models.FilterEdit]
    """

    _validation = {
        'widget_id': {'required': True},
        'row': {'required': True},
        'col': {'required': True},
        'height': {'required': True},
        'width': {'required': True},
        'title': {'required': True, 'max_length': 600, 'min_length': 0},
        'user_widget_description': {'max_length': 600, 'min_length': 0},
    }

    _attribute_map = {
        'widget_id': {'key': 'widgetId', 'type': 'int'},
        'row': {'key': 'row', 'type': 'int'},
        'col': {'key': 'col', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'width': {'key': 'width', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'},
        'user_widget_description': {'key': 'userWidgetDescription', 'type': 'str'},
        'filters': {'key': 'filters', 'type': '[FilterEdit]'},
    }

    def __init__(self, *, widget_id: int, row: int, col: int, height: int, width: int, title: str, user_widget_description: str=None, filters=None, **kwargs) -> None:
        super(WidgetCreate, self).__init__(**kwargs)
        self.widget_id = widget_id
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.title = title
        self.user_widget_description = user_widget_description
        self.filters = filters
