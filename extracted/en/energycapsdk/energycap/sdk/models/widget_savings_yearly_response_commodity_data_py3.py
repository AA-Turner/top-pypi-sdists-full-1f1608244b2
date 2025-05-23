# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WidgetSavingsYearlyResponseCommodityData(Model):
    """WidgetSavingsYearlyResponseCommodityData.

    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param all_time_batcc_use: Program to Date BATCC (Baseline Adjusted to
     Current Conditions) Use
    :type all_time_batcc_use: float
    :param all_time_use: Program to Date Native Use
    :type all_time_use: float
    :param all_time_savings_use: Program to Date Savings Use = allTimeBATCCUse
     - allTimeUse
    :type all_time_savings_use: float
    :param all_time_batcc_total_cost: Program to Date BATCC (Baseline Adjusted
     to Current Conditions) Total Cost
    :type all_time_batcc_total_cost: float
    :param all_time_total_cost: Program to Date Total Cost
    :type all_time_total_cost: float
    :param all_time_savings_total_cost: Program to Date Savings Total Cost =
     allTimeBATCCTotalCost - allTimeTotalCost
    :type all_time_savings_total_cost: float
    :param results: An array of yearly data
    :type results:
     list[~energycap.sdk.models.WidgetSavingsYearlyResponseResults]
    """

    _attribute_map = {
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'all_time_batcc_use': {'key': 'allTimeBATCCUse', 'type': 'float'},
        'all_time_use': {'key': 'allTimeUse', 'type': 'float'},
        'all_time_savings_use': {'key': 'allTimeSavingsUse', 'type': 'float'},
        'all_time_batcc_total_cost': {'key': 'allTimeBATCCTotalCost', 'type': 'float'},
        'all_time_total_cost': {'key': 'allTimeTotalCost', 'type': 'float'},
        'all_time_savings_total_cost': {'key': 'allTimeSavingsTotalCost', 'type': 'float'},
        'results': {'key': 'results', 'type': '[WidgetSavingsYearlyResponseResults]'},
    }

    def __init__(self, *, commodity=None, all_time_batcc_use: float=None, all_time_use: float=None, all_time_savings_use: float=None, all_time_batcc_total_cost: float=None, all_time_total_cost: float=None, all_time_savings_total_cost: float=None, results=None, **kwargs) -> None:
        super(WidgetSavingsYearlyResponseCommodityData, self).__init__(**kwargs)
        self.commodity = commodity
        self.all_time_batcc_use = all_time_batcc_use
        self.all_time_use = all_time_use
        self.all_time_savings_use = all_time_savings_use
        self.all_time_batcc_total_cost = all_time_batcc_total_cost
        self.all_time_total_cost = all_time_total_cost
        self.all_time_savings_total_cost = all_time_savings_total_cost
        self.results = results
