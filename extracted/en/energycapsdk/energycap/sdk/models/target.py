# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Target(Model):
    """Target.

    :param enable: Is the target setting enabled
    :type enable: bool
    :param multiplier: What multiplier to use for the target
    :type multiplier: float
    """

    _attribute_map = {
        'enable': {'key': 'enable', 'type': 'bool'},
        'multiplier': {'key': 'multiplier', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Target, self).__init__(**kwargs)
        self.enable = kwargs.get('enable', None)
        self.multiplier = kwargs.get('multiplier', None)
