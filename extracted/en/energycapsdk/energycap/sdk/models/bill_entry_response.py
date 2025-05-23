# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillEntryResponse(Model):
    """BillEntryResponse.

    :param bill_id: The bill identifier
    :type bill_id: int
    :param account_id: The account identifier
    :type account_id: int
    :param vendor_id: The vendor identifier
    :type vendor_id: int
    :param needs_to_open_batch: Indicates if a new bill batch needs to be
     opened to place this bill in
    :type needs_to_open_batch: bool
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param billing_period: The bill's billing period
    :type billing_period: int
    :param days: The bill's number of days
    :type days: int
    :param total_cost: The bill's total cost
    :type total_cost: float
    :param due_date:
    :type due_date: ~energycap.sdk.models.BillHeaderChild
    :param statement_date:
    :type statement_date: ~energycap.sdk.models.BillHeaderChild
    :param invoice_number:
    :type invoice_number: ~energycap.sdk.models.BillHeaderChild
    :param control_code:
    :type control_code: ~energycap.sdk.models.BillHeaderChild
    :param next_reading:
    :type next_reading: ~energycap.sdk.models.BillHeaderChild
    :param account_period_name:
    :type account_period_name: ~energycap.sdk.models.BillHeaderChild
    :param account_period_number:
    :type account_period_number: ~energycap.sdk.models.BillHeaderChild
    :param account_period_year:
    :type account_period_year: ~energycap.sdk.models.BillHeaderChild
    :param estimated:
    :type estimated: ~energycap.sdk.models.BillHeaderChild
    :param bill_note: The bill's note
    :type bill_note: str
    :param void: Indicates if the bill has been voided
    :type void: bool
    :param from_vendor: Indicates if the bill is from a vendor
    :type from_vendor: bool
    :param observation_method:
    :type observation_method: ~energycap.sdk.models.ObservationMethodChild
    :param approved: Indicates if the bill has been approved
    :type approved: bool
    :param has_been_split: Indicates if the bill has been split
    :type has_been_split: bool
    :param export_hold: Indicates if the bill is being withheld from bill
     exports
    :type export_hold: bool
    :param ap_exported: Indicates if the bill has been ap exported
    :type ap_exported: bool
    :param gl_exported: Indicates if the bill has been gl exported
    :type gl_exported: bool
    :param accrual: Indicates if the bill is an accrual bill
    :type accrual: bool
    :param check_number: The number of the check that the bill was paid with
    :type check_number: str
    :param check_date: The date and time of the check
    :type check_date: datetime
    :param pay_status: The payment status of the bill
    :type pay_status: str
    :param cleared_date: The date and time that the check cleared
    :type cleared_date: datetime
    :param bill_image_url: The fully qualified url to the bill image
    :type bill_image_url: str
    :param general_ledger_code: The general ledger code of the bill's
     account-level details ("Mixed" if there is more than one)
    :type general_ledger_code: str
    :param meters: The billing account's meters
    :type meters: list[~energycap.sdk.models.BillEntryMeterChild]
    :param account_body_lines: The bill's account-level details
    :type account_body_lines: list[~energycap.sdk.models.BillEntryBodyLine]
    :param vendor_body_lines: The bill's vendor template details
    :type vendor_body_lines: list[~energycap.sdk.models.BillEntryBodyLine]
    :param batch:
    :type batch: ~energycap.sdk.models.BatchChild
    """

    _attribute_map = {
        'bill_id': {'key': 'billId', 'type': 'int'},
        'account_id': {'key': 'accountId', 'type': 'int'},
        'vendor_id': {'key': 'vendorId', 'type': 'int'},
        'needs_to_open_batch': {'key': 'needsToOpenBatch', 'type': 'bool'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'days': {'key': 'days', 'type': 'int'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'due_date': {'key': 'dueDate', 'type': 'BillHeaderChild'},
        'statement_date': {'key': 'statementDate', 'type': 'BillHeaderChild'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'BillHeaderChild'},
        'control_code': {'key': 'controlCode', 'type': 'BillHeaderChild'},
        'next_reading': {'key': 'nextReading', 'type': 'BillHeaderChild'},
        'account_period_name': {'key': 'accountPeriodName', 'type': 'BillHeaderChild'},
        'account_period_number': {'key': 'accountPeriodNumber', 'type': 'BillHeaderChild'},
        'account_period_year': {'key': 'accountPeriodYear', 'type': 'BillHeaderChild'},
        'estimated': {'key': 'estimated', 'type': 'BillHeaderChild'},
        'bill_note': {'key': 'billNote', 'type': 'str'},
        'void': {'key': 'void', 'type': 'bool'},
        'from_vendor': {'key': 'fromVendor', 'type': 'bool'},
        'observation_method': {'key': 'observationMethod', 'type': 'ObservationMethodChild'},
        'approved': {'key': 'approved', 'type': 'bool'},
        'has_been_split': {'key': 'hasBeenSplit', 'type': 'bool'},
        'export_hold': {'key': 'exportHold', 'type': 'bool'},
        'ap_exported': {'key': 'apExported', 'type': 'bool'},
        'gl_exported': {'key': 'glExported', 'type': 'bool'},
        'accrual': {'key': 'accrual', 'type': 'bool'},
        'check_number': {'key': 'checkNumber', 'type': 'str'},
        'check_date': {'key': 'checkDate', 'type': 'iso-8601'},
        'pay_status': {'key': 'payStatus', 'type': 'str'},
        'cleared_date': {'key': 'clearedDate', 'type': 'iso-8601'},
        'bill_image_url': {'key': 'billImageUrl', 'type': 'str'},
        'general_ledger_code': {'key': 'generalLedgerCode', 'type': 'str'},
        'meters': {'key': 'meters', 'type': '[BillEntryMeterChild]'},
        'account_body_lines': {'key': 'accountBodyLines', 'type': '[BillEntryBodyLine]'},
        'vendor_body_lines': {'key': 'vendorBodyLines', 'type': '[BillEntryBodyLine]'},
        'batch': {'key': 'batch', 'type': 'BatchChild'},
    }

    def __init__(self, **kwargs):
        super(BillEntryResponse, self).__init__(**kwargs)
        self.bill_id = kwargs.get('bill_id', None)
        self.account_id = kwargs.get('account_id', None)
        self.vendor_id = kwargs.get('vendor_id', None)
        self.needs_to_open_batch = kwargs.get('needs_to_open_batch', None)
        self.begin_date = kwargs.get('begin_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.billing_period = kwargs.get('billing_period', None)
        self.days = kwargs.get('days', None)
        self.total_cost = kwargs.get('total_cost', None)
        self.due_date = kwargs.get('due_date', None)
        self.statement_date = kwargs.get('statement_date', None)
        self.invoice_number = kwargs.get('invoice_number', None)
        self.control_code = kwargs.get('control_code', None)
        self.next_reading = kwargs.get('next_reading', None)
        self.account_period_name = kwargs.get('account_period_name', None)
        self.account_period_number = kwargs.get('account_period_number', None)
        self.account_period_year = kwargs.get('account_period_year', None)
        self.estimated = kwargs.get('estimated', None)
        self.bill_note = kwargs.get('bill_note', None)
        self.void = kwargs.get('void', None)
        self.from_vendor = kwargs.get('from_vendor', None)
        self.observation_method = kwargs.get('observation_method', None)
        self.approved = kwargs.get('approved', None)
        self.has_been_split = kwargs.get('has_been_split', None)
        self.export_hold = kwargs.get('export_hold', None)
        self.ap_exported = kwargs.get('ap_exported', None)
        self.gl_exported = kwargs.get('gl_exported', None)
        self.accrual = kwargs.get('accrual', None)
        self.check_number = kwargs.get('check_number', None)
        self.check_date = kwargs.get('check_date', None)
        self.pay_status = kwargs.get('pay_status', None)
        self.cleared_date = kwargs.get('cleared_date', None)
        self.bill_image_url = kwargs.get('bill_image_url', None)
        self.general_ledger_code = kwargs.get('general_ledger_code', None)
        self.meters = kwargs.get('meters', None)
        self.account_body_lines = kwargs.get('account_body_lines', None)
        self.vendor_body_lines = kwargs.get('vendor_body_lines', None)
        self.batch = kwargs.get('batch', None)
