# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListActionAccrualExclusion(Model):
    """ListActionAccrualExclusion.

    All required parameters must be populated in order to send to Azure.

    :param exclude: Required. Whether or not the bill ids should be excluded
     from accruals, or included again <span
     class='property-internal'>Required</span>
    :type exclude: bool
    """

    _validation = {
        'exclude': {'required': True},
    }

    _attribute_map = {
        'exclude': {'key': 'exclude', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ListActionAccrualExclusion, self).__init__(**kwargs)
        self.exclude = kwargs.get('exclude', None)
