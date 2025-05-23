# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccrualProcessorRequest(Model):
    """AccrualProcessorRequest.

    All required parameters must be populated in order to send to Azure.

    :param batch_code: Required. The batch to create for accrual bills <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 255 characters</span>
    :type batch_code: str
    :param auc_safety_net: Required. Use a safety net for accrued cost
     calculation?
     - if we have usage and we are using an average unit cost safety net and
     the most recent unit cost does not vary more than the specified percentage
     from the historical average unit cost,
     accrued cost = accrued use * most recent unit cost
     - if we have usage and we are not using an average unit cost safety net or
     the most recent unit cost does vary more than the specified percentage
     from the historical average unit cost,
     accrued cost = accrued use * average historical unit cost
     - if we don't have usage,
     accrued cost = historical average cost per day * number of days in accrual
     period <span class='property-internal'>Required</span>
    :type auc_safety_net: bool
    :param auc_percent_variance_allowed: Percent of cost variance allowed when
     using average unit cost safety net <span
     class='property-internal'>Required when AucSafetyNet is set to True</span>
    :type auc_percent_variance_allowed: float
    :param accrual_period_end_date: Required. End date for accrual bills
     generated <span class='property-internal'>Required</span>
    :type accrual_period_end_date: datetime
    :param accrual_period_minimum_start_date: Required. Earliest bill end date
     to begin accruing from (end dates become begin dates for accrued bills)
     <span class='property-internal'>Required</span>
    :type accrual_period_minimum_start_date: datetime
    :param billing_period_calculation_method: Required. Billing period
     calculation method.  Valid values are "bill midpoint" and "manual". <span
     class='property-internal'>One of bill midpoint, manual </span> <span
     class='property-internal'>Required</span>
    :type billing_period_calculation_method: str
    :param manual_billing_period: Fixed billing period for accrual bills
     generated when billing period calculation method is manual. <span
     class='property-internal'>Required when BillingPeriodCalculationMethod is
     set to manual</span> <span class='property-internal'>Must be between
     190001 and 209912</span>
    :type manual_billing_period: int
    :param account_period_calculation_method: Required. Account period
     calculation method.  Valid values are "blank", "billing period" and
     "manual". <span class='property-internal'>One of blank, billing period,
     manual </span> <span class='property-internal'>Required</span>
    :type account_period_calculation_method: str
    :param manual_account_period: Fixed account period for accrual bills
     generated when account period calculation method is manual. <span
     class='property-internal'>Required when AccountPeriodCalculationMethod is
     set to manual</span> <span class='property-internal'>Must be between
     190001 and 209913</span>
    :type manual_account_period: int
    :param test_mode: Required. Generate accrual bills in test mode? Test mode
     bills are created as voided bills. <span
     class='property-internal'>Required</span>
    :type test_mode: bool
    """

    _validation = {
        'batch_code': {'required': True, 'max_length': 255, 'min_length': 0},
        'auc_safety_net': {'required': True},
        'accrual_period_end_date': {'required': True},
        'accrual_period_minimum_start_date': {'required': True},
        'billing_period_calculation_method': {'required': True},
        'manual_billing_period': {'maximum': 209912, 'minimum': 190001},
        'account_period_calculation_method': {'required': True},
        'manual_account_period': {'maximum': 209913, 'minimum': 190001},
        'test_mode': {'required': True},
    }

    _attribute_map = {
        'batch_code': {'key': 'batchCode', 'type': 'str'},
        'auc_safety_net': {'key': 'aucSafetyNet', 'type': 'bool'},
        'auc_percent_variance_allowed': {'key': 'aucPercentVarianceAllowed', 'type': 'float'},
        'accrual_period_end_date': {'key': 'accrualPeriodEndDate', 'type': 'iso-8601'},
        'accrual_period_minimum_start_date': {'key': 'accrualPeriodMinimumStartDate', 'type': 'iso-8601'},
        'billing_period_calculation_method': {'key': 'billingPeriodCalculationMethod', 'type': 'str'},
        'manual_billing_period': {'key': 'manualBillingPeriod', 'type': 'int'},
        'account_period_calculation_method': {'key': 'accountPeriodCalculationMethod', 'type': 'str'},
        'manual_account_period': {'key': 'manualAccountPeriod', 'type': 'int'},
        'test_mode': {'key': 'testMode', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AccrualProcessorRequest, self).__init__(**kwargs)
        self.batch_code = kwargs.get('batch_code', None)
        self.auc_safety_net = kwargs.get('auc_safety_net', None)
        self.auc_percent_variance_allowed = kwargs.get('auc_percent_variance_allowed', None)
        self.accrual_period_end_date = kwargs.get('accrual_period_end_date', None)
        self.accrual_period_minimum_start_date = kwargs.get('accrual_period_minimum_start_date', None)
        self.billing_period_calculation_method = kwargs.get('billing_period_calculation_method', None)
        self.manual_billing_period = kwargs.get('manual_billing_period', None)
        self.account_period_calculation_method = kwargs.get('account_period_calculation_method', None)
        self.manual_account_period = kwargs.get('manual_account_period', None)
        self.test_mode = kwargs.get('test_mode', None)
