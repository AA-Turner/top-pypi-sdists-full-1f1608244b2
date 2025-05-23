# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterUDFResponse(Model):
    """MeterUDFResponse.

    :param meter_id: The meter identifier
    :type meter_id: int
    :param meter_code: The meter code
    :type meter_code: str
    :param meter_info: The meter info
    :type meter_info: str
    :param udfs: An array of user-defined fields (UDFs)
    :type udfs: list[~energycap.sdk.models.UDFFieldChild]
    """

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'udfs': {'key': 'udfs', 'type': '[UDFFieldChild]'},
    }

    def __init__(self, **kwargs):
        super(MeterUDFResponse, self).__init__(**kwargs)
        self.meter_id = kwargs.get('meter_id', None)
        self.meter_code = kwargs.get('meter_code', None)
        self.meter_info = kwargs.get('meter_info', None)
        self.udfs = kwargs.get('udfs', None)
