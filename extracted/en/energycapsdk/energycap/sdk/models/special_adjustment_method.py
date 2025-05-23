# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SpecialAdjustmentMethod(Model):
    """SpecialAdjustmentMethod.

    :param label: Description of Special Adjustment method
    :type label: str
    :param special_adjustment_method_id: Special Adjustment Method ID
    :type special_adjustment_method_id: int
    :param electric_only: Indicates whether or not this method is for Electric
     meters only
    :type electric_only: bool
    :param symbol: The symbol for the Special Adjustment's input value
    :type symbol: str
    :param precision: The precision on the Special Adjustment's input value
    :type precision: int
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'special_adjustment_method_id': {'key': 'specialAdjustmentMethodId', 'type': 'int'},
        'electric_only': {'key': 'electricOnly', 'type': 'bool'},
        'symbol': {'key': 'symbol', 'type': 'str'},
        'precision': {'key': 'precision', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(SpecialAdjustmentMethod, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.special_adjustment_method_id = kwargs.get('special_adjustment_method_id', None)
        self.electric_only = kwargs.get('electric_only', None)
        self.symbol = kwargs.get('symbol', None)
        self.precision = kwargs.get('precision', None)
