# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreateUtilityPlatformMeter(Model):
    """CreateUtilityPlatformMeter.

    All required parameters must be populated in order to send to Azure.

    :param meter_code: Required. The meter code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type meter_code: str
    """

    _validation = {
        'meter_code': {'required': True, 'max_length': 32, 'min_length': 0},
    }

    _attribute_map = {
        'meter_code': {'key': 'meterCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CreateUtilityPlatformMeter, self).__init__(**kwargs)
        self.meter_code = kwargs.get('meter_code', None)
