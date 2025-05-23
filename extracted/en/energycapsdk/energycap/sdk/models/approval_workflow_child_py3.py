# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApprovalWorkflowChild(Model):
    """Bill approval settings.

    :param approval_mode_enabled: Whether or not Approval Mode is enabled
    :type approval_mode_enabled: bool
    :param confirm_edit_delete: Whether or not edit / delete should be
     confirmed
    :type confirm_edit_delete: bool
    """

    _attribute_map = {
        'approval_mode_enabled': {'key': 'approvalModeEnabled', 'type': 'bool'},
        'confirm_edit_delete': {'key': 'confirmEditDelete', 'type': 'bool'},
    }

    def __init__(self, *, approval_mode_enabled: bool=None, confirm_edit_delete: bool=None, **kwargs) -> None:
        super(ApprovalWorkflowChild, self).__init__(**kwargs)
        self.approval_mode_enabled = approval_mode_enabled
        self.confirm_edit_delete = confirm_edit_delete
