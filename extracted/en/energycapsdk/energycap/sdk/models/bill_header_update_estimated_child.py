# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillHeaderUpdateEstimatedChild(Model):
    """Estimated.

    All required parameters must be populated in order to send to Azure.

    :param estimated:  <span class='property-internal'>Required when Update is
     set to True</span>
    :type estimated: bool
    :param update: Required. Indicates whether or not the header value is
     being updated <span class='property-internal'>Required</span>
    :type update: bool
    """

    _validation = {
        'update': {'required': True},
    }

    _attribute_map = {
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'update': {'key': 'update', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(BillHeaderUpdateEstimatedChild, self).__init__(**kwargs)
        self.estimated = kwargs.get('estimated', None)
        self.update = kwargs.get('update', None)
