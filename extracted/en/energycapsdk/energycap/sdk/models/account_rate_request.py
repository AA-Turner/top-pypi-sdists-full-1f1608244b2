# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountRateRequest(Model):
    """AccountRateRequest.

    All required parameters must be populated in order to send to Azure.

    :param rate_id: Required. The identifier for the rate to assign to the
     accountMeter <span class='property-internal'>Required</span> <span
     class='property-internal'>Required</span>
    :type rate_id: int
    :param start_date: Required. The start date for the accountRate <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Required</span>
    :type start_date: datetime
    """

    _validation = {
        'rate_id': {'required': True},
        'start_date': {'required': True},
    }

    _attribute_map = {
        'rate_id': {'key': 'rateId', 'type': 'int'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AccountRateRequest, self).__init__(**kwargs)
        self.rate_id = kwargs.get('rate_id', None)
        self.start_date = kwargs.get('start_date', None)
