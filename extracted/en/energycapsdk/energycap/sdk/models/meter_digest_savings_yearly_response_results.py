# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterDigestSavingsYearlyResponseResults(Model):
    """MeterDigestSavingsYearlyResponseResults.

    :param year: Year
    :type year: str
    :param batcc_total_cost: BATCC (Baseline Adjusted to Current Conditions)
     Total Cost
    :type batcc_total_cost: float
    :param total_cost: Total Cost
    :type total_cost: float
    :param savings_total_cost: Savings Total Cost = BATCCTotalCost - TotalCost
    :type savings_total_cost: float
    :param batcc_native_use: BATCC (Baseline Adjusted to Current Conditions)
     Native Use
    :type batcc_native_use: float
    :param native_use: Native Use
    :type native_use: float
    :param savings_native_use: Savings Native Use = BATCCNativeUse - NativeUse
    :type savings_native_use: float
    :param batcc_common_use: BATCC (Baseline Adjusted to Current Conditions)
     Common Use
    :type batcc_common_use: float
    :param common_use: Common Use
    :type common_use: float
    :param savings_common_use: Savings Common Use = BATCCCommonUse - CommonUse
    :type savings_common_use: float
    """

    _attribute_map = {
        'year': {'key': 'year', 'type': 'str'},
        'batcc_total_cost': {'key': 'batccTotalCost', 'type': 'float'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'savings_total_cost': {'key': 'savingsTotalCost', 'type': 'float'},
        'batcc_native_use': {'key': 'batccNativeUse', 'type': 'float'},
        'native_use': {'key': 'nativeUse', 'type': 'float'},
        'savings_native_use': {'key': 'savingsNativeUse', 'type': 'float'},
        'batcc_common_use': {'key': 'batccCommonUse', 'type': 'float'},
        'common_use': {'key': 'commonUse', 'type': 'float'},
        'savings_common_use': {'key': 'savingsCommonUse', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(MeterDigestSavingsYearlyResponseResults, self).__init__(**kwargs)
        self.year = kwargs.get('year', None)
        self.batcc_total_cost = kwargs.get('batcc_total_cost', None)
        self.total_cost = kwargs.get('total_cost', None)
        self.savings_total_cost = kwargs.get('savings_total_cost', None)
        self.batcc_native_use = kwargs.get('batcc_native_use', None)
        self.native_use = kwargs.get('native_use', None)
        self.savings_native_use = kwargs.get('savings_native_use', None)
        self.batcc_common_use = kwargs.get('batcc_common_use', None)
        self.common_use = kwargs.get('common_use', None)
        self.savings_common_use = kwargs.get('savings_common_use', None)
