# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestNormalizedYearlyResponseTargetComparison(Model):
    """PlaceDigestNormalizedYearlyResponseTargetComparison.

    :param target_year: Target year
    :type target_year: int
    :param target_label: Target label
    :type target_label: str
    :param global_use: Total use for the target year
    :type global_use: float
    :param global_use_ytd: Total use for the target year up to the target
     period that corresponds to the current period
    :type global_use_ytd: float
    """

    _attribute_map = {
        'target_year': {'key': 'targetYear', 'type': 'int'},
        'target_label': {'key': 'targetLabel', 'type': 'str'},
        'global_use': {'key': 'globalUse', 'type': 'float'},
        'global_use_ytd': {'key': 'globalUseYtd', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(PlaceDigestNormalizedYearlyResponseTargetComparison, self).__init__(**kwargs)
        self.target_year = kwargs.get('target_year', None)
        self.target_label = kwargs.get('target_label', None)
        self.global_use = kwargs.get('global_use', None)
        self.global_use_ytd = kwargs.get('global_use_ytd', None)
