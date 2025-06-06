# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillActionHistoricalExport(Model):
    """BillActionHistoricalExport.

    :param ids:  <span class='property-internal'>Cannot be Empty</span>
    :type ids: list[int]
    :param vpr:  <span class='property-internal'>One of , V, P, R </span>
    :type vpr: str
    """

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'vpr': {'key': 'vpr', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BillActionHistoricalExport, self).__init__(**kwargs)
        self.ids = kwargs.get('ids', None)
        self.vpr = kwargs.get('vpr', None)
