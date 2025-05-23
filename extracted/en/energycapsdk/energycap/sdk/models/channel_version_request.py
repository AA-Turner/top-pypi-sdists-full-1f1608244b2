# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChannelVersionRequest(Model):
    """ChannelVersionRequest.

    All required parameters must be populated in order to send to Azure.

    :param multiplier: Required. The channel multiplier <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 999999999999999</span>
    :type multiplier: float
    :param unit_code: Required. The channel's unit of measure <span
     class='property-internal'>Required</span>
    :type unit_code: str
    :param observation_rule: Required. The channel's observation rule.
     Possible values include "Odometer" and "Trip" <span
     class='property-internal'>Required</span> <span
     class='property-internal'>One of Odometer, Trip </span>
    :type observation_rule: str
    :param maximum_reading: Required. The channel's max reading <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 999999999999999</span>
    :type maximum_reading: float
    :param udfs: List of user defined/custom fields and values for this
     version
     If the Udfs list is null or empty no values are assigned
     If a udf is omitted no value is assigned to that udf
     To remove a value from an existing Udf, pass in the UdfId and set the
     Value to null
    :type udfs: list[~energycap.sdk.models.UDFValue]
    """

    _validation = {
        'multiplier': {'required': True, 'maximum': 999999999999999, 'minimum': 0},
        'unit_code': {'required': True},
        'observation_rule': {'required': True},
        'maximum_reading': {'required': True, 'maximum': 999999999999999, 'minimum': 0},
    }

    _attribute_map = {
        'multiplier': {'key': 'multiplier', 'type': 'float'},
        'unit_code': {'key': 'unitCode', 'type': 'str'},
        'observation_rule': {'key': 'observationRule', 'type': 'str'},
        'maximum_reading': {'key': 'maximumReading', 'type': 'float'},
        'udfs': {'key': 'udfs', 'type': '[UDFValue]'},
    }

    def __init__(self, **kwargs):
        super(ChannelVersionRequest, self).__init__(**kwargs)
        self.multiplier = kwargs.get('multiplier', None)
        self.unit_code = kwargs.get('unit_code', None)
        self.observation_rule = kwargs.get('observation_rule', None)
        self.maximum_reading = kwargs.get('maximum_reading', None)
        self.udfs = kwargs.get('udfs', None)
