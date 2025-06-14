# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountAlertRequest(Model):
    """AccountAlertRequest.

    All required parameters must be populated in order to send to Azure.

    :param begin_date: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type begin_date: datetime
    :param end_date: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type end_date: datetime
    :param message: Required.  <span class='property-internal'>Required</span>
    :type message: str
    :param allow_bill_processing: Required.  <span
     class='property-internal'>Required</span>
    :type allow_bill_processing: bool
    """

    _validation = {
        'begin_date': {'required': True},
        'end_date': {'required': True},
        'message': {'required': True},
        'allow_bill_processing': {'required': True},
    }

    _attribute_map = {
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'allow_bill_processing': {'key': 'allowBillProcessing', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AccountAlertRequest, self).__init__(**kwargs)
        self.begin_date = kwargs.get('begin_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.message = kwargs.get('message', None)
        self.allow_bill_processing = kwargs.get('allow_bill_processing', None)
