# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EmissionsSourcesModuleClassPermission(Model):
    """EmissionsSourcesModuleClassPermission.

    :param view:
    :type view: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(EmissionsSourcesModuleClassPermission, self).__init__(**kwargs)
        self.view = kwargs.get('view', None)
