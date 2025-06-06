# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillAccountMeterStatisticsResponse(Model):
    """BillAccountMeterStatisticsResponse.

    :param use_per_day:
    :type use_per_day: ~energycap.sdk.models.StatisticsResponse
    :param cost_per_day:
    :type cost_per_day: ~energycap.sdk.models.StatisticsResponse
    :param demand_per_day:
    :type demand_per_day: ~energycap.sdk.models.StatisticsResponse
    :param bill_id: The bill identifier
    :type bill_id: int
    :param billing_period: The bill's billing period
    :type billing_period: int
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param days: The number of days the bill covers
    :type days: int
    :param account:
    :type account: ~energycap.sdk.models.AccountChild
    :param meter:
    :type meter: ~energycap.sdk.models.MeterChild
    """

    _attribute_map = {
        'use_per_day': {'key': 'usePerDay', 'type': 'StatisticsResponse'},
        'cost_per_day': {'key': 'costPerDay', 'type': 'StatisticsResponse'},
        'demand_per_day': {'key': 'demandPerDay', 'type': 'StatisticsResponse'},
        'bill_id': {'key': 'billId', 'type': 'int'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'days': {'key': 'days', 'type': 'int'},
        'account': {'key': 'account', 'type': 'AccountChild'},
        'meter': {'key': 'meter', 'type': 'MeterChild'},
    }

    def __init__(self, *, use_per_day=None, cost_per_day=None, demand_per_day=None, bill_id: int=None, billing_period: int=None, begin_date=None, end_date=None, days: int=None, account=None, meter=None, **kwargs) -> None:
        super(BillAccountMeterStatisticsResponse, self).__init__(**kwargs)
        self.use_per_day = use_per_day
        self.cost_per_day = cost_per_day
        self.demand_per_day = demand_per_day
        self.bill_id = bill_id
        self.billing_period = billing_period
        self.begin_date = begin_date
        self.end_date = end_date
        self.days = days
        self.account = account
        self.meter = meter
