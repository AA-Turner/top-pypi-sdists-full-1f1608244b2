# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SharedBillListsClassPermission(Model):
    """SharedBillListsClassPermission.

    :param view:
    :type view: bool
    :param create:
    :type create: bool
    :param edit:
    :type edit: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'create': {'key': 'create', 'type': 'bool'},
        'edit': {'key': 'edit', 'type': 'bool'},
    }

    def __init__(self, *, view: bool=None, create: bool=None, edit: bool=None, **kwargs) -> None:
        super(SharedBillListsClassPermission, self).__init__(**kwargs)
        self.view = view
        self.create = create
        self.edit = edit
