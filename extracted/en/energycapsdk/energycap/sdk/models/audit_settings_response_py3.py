# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuditSettingsResponse(Model):
    """AuditSettingsResponse.

    All required parameters must be populated in order to send to Azure.

    :param bill_contains_line_item_descriptions:
    :type bill_contains_line_item_descriptions:
     ~energycap.sdk.models.BillContainsLineItemDescriptionsSettingResponse
    :param bill_contains_line_item_types:
    :type bill_contains_line_item_types:
     ~energycap.sdk.models.BillContainsLineItemTypesSettingResponse
    :param total_bill_cost_does_not_match_line_item_types:
    :type total_bill_cost_does_not_match_line_item_types:
     ~energycap.sdk.models.TotalBillCostDoesNotMatchLineItemTypesSettingResponse
    :param billing_period_outside_start_end_dates:
    :type billing_period_outside_start_end_dates:
     ~energycap.sdk.models.AuditSettingResponse
    :param bill_overlaps_with_other_account_bill:
    :type bill_overlaps_with_other_account_bill:
     ~energycap.sdk.models.AuditSettingResponse
    :param gap_between_bill_and_previous_bill_on_account:
    :type gap_between_bill_and_previous_bill_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param bill_ends_in_future:
    :type bill_ends_in_future: ~energycap.sdk.models.AuditSettingResponse
    :param account_has_multiple_bills_in_billing_period:
    :type account_has_multiple_bills_in_billing_period:
     ~energycap.sdk.models.AuditSettingResponse
    :param statement_date_before_end_date:
    :type statement_date_before_end_date:
     ~energycap.sdk.models.AuditSettingResponse
    :param due_date_before_end_date:
    :type due_date_before_end_date: ~energycap.sdk.models.AuditSettingResponse
    :param bill_significantly_shorter_or_longer_than_previous:
    :type bill_significantly_shorter_or_longer_than_previous:
     ~energycap.sdk.models.BillSignificantlyShorterOrLongerThanPreviousSettingResponse
    :param too_many_consecutive_estimated_bills:
    :type too_many_consecutive_estimated_bills:
     ~energycap.sdk.models.TooManyConsecutiveEstimatedBillsSettingResponse
    :param due_date_too_long_after_bill_end: Required.
    :type due_date_too_long_after_bill_end:
     ~energycap.sdk.models.DueDateTooLongAfterBillEndSettingResponse
    :param statement_date_too_long_after_bill_end: Required.
    :type statement_date_too_long_after_bill_end:
     ~energycap.sdk.models.StatementDateTooLongAfterBillEndSettingResponse
    :param invoice_number_is_repeated_on_account:
    :type invoice_number_is_repeated_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param likely_duplicate_bill_on_account:
    :type likely_duplicate_bill_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param total_meter_cost_is_percentage_higher_than_past_year:
    :type total_meter_cost_is_percentage_higher_than_past_year:
     ~energycap.sdk.models.AuditSettingResponse
    :param total_meter_use_is_percentage_higher_than_past_year:
    :type total_meter_use_is_percentage_higher_than_past_year:
     ~energycap.sdk.models.AuditSettingResponse
    :param serial_number_does_not_match_import_file:
    :type serial_number_does_not_match_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param rate_code_does_not_match_import_file:
    :type rate_code_does_not_match_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param import_file_start_date_adjusted_to_prevent_gaps:
    :type import_file_start_date_adjusted_to_prevent_gaps:
     ~energycap.sdk.models.AuditSettingResponse
    :param account_alert_exists_on_account_in_import_file:
    :type account_alert_exists_on_account_in_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param abnormal_bill_cost_with_outlier_analysis:
    :type abnormal_bill_cost_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillCostWithOutlierAnalysisSettingResponse
    :param abnormal_bill_use_with_outlier_analysis: Required.
    :type abnormal_bill_use_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillUseWithOutlierAnalysisSettingResponse
    :param abnormal_bill_demand_with_outlier_analysis: Required.
    :type abnormal_bill_demand_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillDemandWithOutlierAnalysisSettingResponse
    """

    _validation = {
        'due_date_too_long_after_bill_end': {'required': True},
        'statement_date_too_long_after_bill_end': {'required': True},
        'abnormal_bill_use_with_outlier_analysis': {'required': True},
        'abnormal_bill_demand_with_outlier_analysis': {'required': True},
    }

    _attribute_map = {
        'bill_contains_line_item_descriptions': {'key': 'billContainsLineItemDescriptions', 'type': 'BillContainsLineItemDescriptionsSettingResponse'},
        'bill_contains_line_item_types': {'key': 'billContainsLineItemTypes', 'type': 'BillContainsLineItemTypesSettingResponse'},
        'total_bill_cost_does_not_match_line_item_types': {'key': 'totalBillCostDoesNotMatchLineItemTypes', 'type': 'TotalBillCostDoesNotMatchLineItemTypesSettingResponse'},
        'billing_period_outside_start_end_dates': {'key': 'billingPeriodOutsideStartEndDates', 'type': 'AuditSettingResponse'},
        'bill_overlaps_with_other_account_bill': {'key': 'billOverlapsWithOtherAccountBill', 'type': 'AuditSettingResponse'},
        'gap_between_bill_and_previous_bill_on_account': {'key': 'gapBetweenBillAndPreviousBillOnAccount', 'type': 'AuditSettingResponse'},
        'bill_ends_in_future': {'key': 'billEndsInFuture', 'type': 'AuditSettingResponse'},
        'account_has_multiple_bills_in_billing_period': {'key': 'accountHasMultipleBillsInBillingPeriod', 'type': 'AuditSettingResponse'},
        'statement_date_before_end_date': {'key': 'statementDateBeforeEndDate', 'type': 'AuditSettingResponse'},
        'due_date_before_end_date': {'key': 'dueDateBeforeEndDate', 'type': 'AuditSettingResponse'},
        'bill_significantly_shorter_or_longer_than_previous': {'key': 'billSignificantlyShorterOrLongerThanPrevious', 'type': 'BillSignificantlyShorterOrLongerThanPreviousSettingResponse'},
        'too_many_consecutive_estimated_bills': {'key': 'tooManyConsecutiveEstimatedBills', 'type': 'TooManyConsecutiveEstimatedBillsSettingResponse'},
        'due_date_too_long_after_bill_end': {'key': 'dueDateTooLongAfterBillEnd', 'type': 'DueDateTooLongAfterBillEndSettingResponse'},
        'statement_date_too_long_after_bill_end': {'key': 'statementDateTooLongAfterBillEnd', 'type': 'StatementDateTooLongAfterBillEndSettingResponse'},
        'invoice_number_is_repeated_on_account': {'key': 'invoiceNumberIsRepeatedOnAccount', 'type': 'AuditSettingResponse'},
        'likely_duplicate_bill_on_account': {'key': 'likelyDuplicateBillOnAccount', 'type': 'AuditSettingResponse'},
        'total_meter_cost_is_percentage_higher_than_past_year': {'key': 'totalMeterCostIsPercentageHigherThanPastYear', 'type': 'AuditSettingResponse'},
        'total_meter_use_is_percentage_higher_than_past_year': {'key': 'totalMeterUseIsPercentageHigherThanPastYear', 'type': 'AuditSettingResponse'},
        'serial_number_does_not_match_import_file': {'key': 'serialNumberDoesNotMatchImportFile', 'type': 'AuditSettingResponse'},
        'rate_code_does_not_match_import_file': {'key': 'rateCodeDoesNotMatchImportFile', 'type': 'AuditSettingResponse'},
        'import_file_start_date_adjusted_to_prevent_gaps': {'key': 'importFileStartDateAdjustedToPreventGaps', 'type': 'AuditSettingResponse'},
        'account_alert_exists_on_account_in_import_file': {'key': 'accountAlertExistsOnAccountInImportFile', 'type': 'AuditSettingResponse'},
        'abnormal_bill_cost_with_outlier_analysis': {'key': 'abnormalBillCostWithOutlierAnalysis', 'type': 'AbnormalBillCostWithOutlierAnalysisSettingResponse'},
        'abnormal_bill_use_with_outlier_analysis': {'key': 'abnormalBillUseWithOutlierAnalysis', 'type': 'AbnormalBillUseWithOutlierAnalysisSettingResponse'},
        'abnormal_bill_demand_with_outlier_analysis': {'key': 'abnormalBillDemandWithOutlierAnalysis', 'type': 'AbnormalBillDemandWithOutlierAnalysisSettingResponse'},
    }

    def __init__(self, *, due_date_too_long_after_bill_end, statement_date_too_long_after_bill_end, abnormal_bill_use_with_outlier_analysis, abnormal_bill_demand_with_outlier_analysis, bill_contains_line_item_descriptions=None, bill_contains_line_item_types=None, total_bill_cost_does_not_match_line_item_types=None, billing_period_outside_start_end_dates=None, bill_overlaps_with_other_account_bill=None, gap_between_bill_and_previous_bill_on_account=None, bill_ends_in_future=None, account_has_multiple_bills_in_billing_period=None, statement_date_before_end_date=None, due_date_before_end_date=None, bill_significantly_shorter_or_longer_than_previous=None, too_many_consecutive_estimated_bills=None, invoice_number_is_repeated_on_account=None, likely_duplicate_bill_on_account=None, total_meter_cost_is_percentage_higher_than_past_year=None, total_meter_use_is_percentage_higher_than_past_year=None, serial_number_does_not_match_import_file=None, rate_code_does_not_match_import_file=None, import_file_start_date_adjusted_to_prevent_gaps=None, account_alert_exists_on_account_in_import_file=None, abnormal_bill_cost_with_outlier_analysis=None, **kwargs) -> None:
        super(AuditSettingsResponse, self).__init__(**kwargs)
        self.bill_contains_line_item_descriptions = bill_contains_line_item_descriptions
        self.bill_contains_line_item_types = bill_contains_line_item_types
        self.total_bill_cost_does_not_match_line_item_types = total_bill_cost_does_not_match_line_item_types
        self.billing_period_outside_start_end_dates = billing_period_outside_start_end_dates
        self.bill_overlaps_with_other_account_bill = bill_overlaps_with_other_account_bill
        self.gap_between_bill_and_previous_bill_on_account = gap_between_bill_and_previous_bill_on_account
        self.bill_ends_in_future = bill_ends_in_future
        self.account_has_multiple_bills_in_billing_period = account_has_multiple_bills_in_billing_period
        self.statement_date_before_end_date = statement_date_before_end_date
        self.due_date_before_end_date = due_date_before_end_date
        self.bill_significantly_shorter_or_longer_than_previous = bill_significantly_shorter_or_longer_than_previous
        self.too_many_consecutive_estimated_bills = too_many_consecutive_estimated_bills
        self.due_date_too_long_after_bill_end = due_date_too_long_after_bill_end
        self.statement_date_too_long_after_bill_end = statement_date_too_long_after_bill_end
        self.invoice_number_is_repeated_on_account = invoice_number_is_repeated_on_account
        self.likely_duplicate_bill_on_account = likely_duplicate_bill_on_account
        self.total_meter_cost_is_percentage_higher_than_past_year = total_meter_cost_is_percentage_higher_than_past_year
        self.total_meter_use_is_percentage_higher_than_past_year = total_meter_use_is_percentage_higher_than_past_year
        self.serial_number_does_not_match_import_file = serial_number_does_not_match_import_file
        self.rate_code_does_not_match_import_file = rate_code_does_not_match_import_file
        self.import_file_start_date_adjusted_to_prevent_gaps = import_file_start_date_adjusted_to_prevent_gaps
        self.account_alert_exists_on_account_in_import_file = account_alert_exists_on_account_in_import_file
        self.abnormal_bill_cost_with_outlier_analysis = abnormal_bill_cost_with_outlier_analysis
        self.abnormal_bill_use_with_outlier_analysis = abnormal_bill_use_with_outlier_analysis
        self.abnormal_bill_demand_with_outlier_analysis = abnormal_bill_demand_with_outlier_analysis
