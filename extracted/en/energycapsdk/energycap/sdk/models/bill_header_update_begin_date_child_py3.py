# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillHeaderUpdateBeginDateChild(Model):
    """Begin Date.

    All required parameters must be populated in order to send to Azure.

    :param begin_date:  <span class='property-internal'>Required when Update
     is set to True</span> <span class='property-internal'>Must be between
     12/31/1899 and 1/1/3000</span>
    :type begin_date: datetime
    :param update: Required. Indicates whether or not the header value is
     being updated <span class='property-internal'>Required</span>
    :type update: bool
    """

    _validation = {
        'update': {'required': True},
    }

    _attribute_map = {
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'update': {'key': 'update', 'type': 'bool'},
    }

    def __init__(self, *, update: bool, begin_date=None, **kwargs) -> None:
        super(BillHeaderUpdateBeginDateChild, self).__init__(**kwargs)
        self.begin_date = begin_date
        self.update = update
