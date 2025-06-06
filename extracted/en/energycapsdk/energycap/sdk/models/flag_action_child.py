# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FlagActionChild(Model):
    """FlagActionChild.

    :param flag_action_id: The flag action identifier
    :type flag_action_id: int
    :param flag_action_info: Flag action information
    :type flag_action_info: str
    """

    _attribute_map = {
        'flag_action_id': {'key': 'flagActionId', 'type': 'int'},
        'flag_action_info': {'key': 'flagActionInfo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FlagActionChild, self).__init__(**kwargs)
        self.flag_action_id = kwargs.get('flag_action_id', None)
        self.flag_action_info = kwargs.get('flag_action_info', None)
