# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillResponse(Model):
    """BillResponse.

    :param bill_id: The bill identifier
    :type bill_id: int
    :param batch:
    :type batch: ~energycap.sdk.models.BatchChild
    :param account:
    :type account: ~energycap.sdk.models.AccountChild
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param billing_period: The bill's billing period
    :type billing_period: int
    :param account_period: The bill's accounting period
    :type account_period: int
    :param total_cost: The bill's total cost
    :type total_cost: float
    :param estimated: Indicates if the bill is estimated
    :type estimated: bool
    :param approved: Indicates if the bill has been approved
    :type approved: bool
    :param approve_date: The date and time the bill was approved
    :type approve_date: datetime
    :param approved_by:
    :type approved_by: ~energycap.sdk.models.UserChild
    :param exported: Indicates if the bill has been exported
    :type exported: bool
    :param export_date: The date and time the bill was exported
    :type export_date: datetime
    :param exported_by:
    :type exported_by: ~energycap.sdk.models.UserChild
    :param observation_method:
    :type observation_method: ~energycap.sdk.models.ObservationMethodChild
    :param statement_date: The date and time of the bill statement
    :type statement_date: datetime
    :param due_date: The date and time the bill is due
    :type due_date: datetime
    :param next_reading: The date and time of the next reading
    :type next_reading: datetime
    :param control_code: The bill's control code
    :type control_code: str
    :param invoice_number: The bill's invoice number
    :type invoice_number: str
    :param invoice_pages: The number of pages on the invoice
    :type invoice_pages: int
    :param check_number: The check number
    :type check_number: str
    :param check_date: The date and time of the check
    :type check_date: datetime
    :param pay_status: The pay status of the bill
    :type pay_status: str
    :param cleared_date: The cleared date
    :type cleared_date: datetime
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The date and time the bill was created
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification
    :type modified_date: datetime
    :param void: Indicates if the bill has been voided
    :type void: bool
    :param dirty: Indicates if the bill record has been cleaned. Cleaning is
     an internal EnergyCAP process
    :type dirty: bool
    :param import_verified: Indicates if the import has been verified
    :type import_verified: bool
    :param accrual: Indicates if the bill is an accrual
    :type accrual: bool
    :param accrual_reversed: Indicates if the bill is a reversed accrual
    :type accrual_reversed: bool
    :param accrual_reversed_date: The date and time the accrual was reversed
    :type accrual_reversed_date: datetime
    :param export_hold: Indicates if the bill is held for export
    :type export_hold: bool
    :param gl_exported: Indicates if the bill has been gl exported
    :type gl_exported: bool
    :param gl_exported_by:
    :type gl_exported_by: ~energycap.sdk.models.UserChild
    :param gl_export_date: The date and time the bill was exported to gl
    :type gl_export_date: datetime
    :param from_vendor: Indicates if the bill is from a vendor
    :type from_vendor: bool
    :param has_been_split: Indicates if the bill has been split
    :type has_been_split: bool
    :param was_split_date: The date and time the bill was split
    :type was_split_date: datetime
    :param trans_ref_num: The transaction reference number of the bill
    :type trans_ref_num: str
    :param payment_type: The payment type of the bill
    :type payment_type: str
    :param actual_amount_paid: The actual amount paid
    :type actual_amount_paid: float
    :param assigned_to:
    :type assigned_to: ~energycap.sdk.models.UserChild
    :param assigned_date: The date and time the bill was assigned to a user
    :type assigned_date: datetime
    :param pay_source: The bill's pay source
    :type pay_source: str
    :param pay_to: Indicates whom the bill paid
    :type pay_to: str
    :param previous_balance: The balance of the previous bill
    :type previous_balance: float
    :param balance_forward: The amount of balance that was forwarded
    :type balance_forward: float
    :param current_charges: The current charges
    :type current_charges: float
    :param bill_note: Bill note for this bill
    :type bill_note: str
    :param reversal_details:
    :type reversal_details: ~energycap.sdk.models.BillReversal
    :param excluded_from_accruals: Indicates whether this bill is excluded
     from accruals or not
    :type excluded_from_accruals: bool
    :param analyzing: Indicates whether this bill is currently being analyzed
    :type analyzing: bool
    """

    _attribute_map = {
        'bill_id': {'key': 'billId', 'type': 'int'},
        'batch': {'key': 'batch', 'type': 'BatchChild'},
        'account': {'key': 'account', 'type': 'AccountChild'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'account_period': {'key': 'accountPeriod', 'type': 'int'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'approved': {'key': 'approved', 'type': 'bool'},
        'approve_date': {'key': 'approveDate', 'type': 'iso-8601'},
        'approved_by': {'key': 'approvedBy', 'type': 'UserChild'},
        'exported': {'key': 'exported', 'type': 'bool'},
        'export_date': {'key': 'exportDate', 'type': 'iso-8601'},
        'exported_by': {'key': 'exportedBy', 'type': 'UserChild'},
        'observation_method': {'key': 'observationMethod', 'type': 'ObservationMethodChild'},
        'statement_date': {'key': 'statementDate', 'type': 'iso-8601'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'next_reading': {'key': 'nextReading', 'type': 'iso-8601'},
        'control_code': {'key': 'controlCode', 'type': 'str'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'invoice_pages': {'key': 'invoicePages', 'type': 'int'},
        'check_number': {'key': 'checkNumber', 'type': 'str'},
        'check_date': {'key': 'checkDate', 'type': 'iso-8601'},
        'pay_status': {'key': 'payStatus', 'type': 'str'},
        'cleared_date': {'key': 'clearedDate', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'void': {'key': 'void', 'type': 'bool'},
        'dirty': {'key': 'dirty', 'type': 'bool'},
        'import_verified': {'key': 'importVerified', 'type': 'bool'},
        'accrual': {'key': 'accrual', 'type': 'bool'},
        'accrual_reversed': {'key': 'accrualReversed', 'type': 'bool'},
        'accrual_reversed_date': {'key': 'accrualReversedDate', 'type': 'iso-8601'},
        'export_hold': {'key': 'exportHold', 'type': 'bool'},
        'gl_exported': {'key': 'glExported', 'type': 'bool'},
        'gl_exported_by': {'key': 'glExportedBy', 'type': 'UserChild'},
        'gl_export_date': {'key': 'glExportDate', 'type': 'iso-8601'},
        'from_vendor': {'key': 'fromVendor', 'type': 'bool'},
        'has_been_split': {'key': 'hasBeenSplit', 'type': 'bool'},
        'was_split_date': {'key': 'wasSplitDate', 'type': 'iso-8601'},
        'trans_ref_num': {'key': 'transRefNum', 'type': 'str'},
        'payment_type': {'key': 'paymentType', 'type': 'str'},
        'actual_amount_paid': {'key': 'actualAmountPaid', 'type': 'float'},
        'assigned_to': {'key': 'assignedTo', 'type': 'UserChild'},
        'assigned_date': {'key': 'assignedDate', 'type': 'iso-8601'},
        'pay_source': {'key': 'paySource', 'type': 'str'},
        'pay_to': {'key': 'payTo', 'type': 'str'},
        'previous_balance': {'key': 'previousBalance', 'type': 'float'},
        'balance_forward': {'key': 'balanceForward', 'type': 'float'},
        'current_charges': {'key': 'currentCharges', 'type': 'float'},
        'bill_note': {'key': 'billNote', 'type': 'str'},
        'reversal_details': {'key': 'reversalDetails', 'type': 'BillReversal'},
        'excluded_from_accruals': {'key': 'excludedFromAccruals', 'type': 'bool'},
        'analyzing': {'key': 'analyzing', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(BillResponse, self).__init__(**kwargs)
        self.bill_id = kwargs.get('bill_id', None)
        self.batch = kwargs.get('batch', None)
        self.account = kwargs.get('account', None)
        self.begin_date = kwargs.get('begin_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.billing_period = kwargs.get('billing_period', None)
        self.account_period = kwargs.get('account_period', None)
        self.total_cost = kwargs.get('total_cost', None)
        self.estimated = kwargs.get('estimated', None)
        self.approved = kwargs.get('approved', None)
        self.approve_date = kwargs.get('approve_date', None)
        self.approved_by = kwargs.get('approved_by', None)
        self.exported = kwargs.get('exported', None)
        self.export_date = kwargs.get('export_date', None)
        self.exported_by = kwargs.get('exported_by', None)
        self.observation_method = kwargs.get('observation_method', None)
        self.statement_date = kwargs.get('statement_date', None)
        self.due_date = kwargs.get('due_date', None)
        self.next_reading = kwargs.get('next_reading', None)
        self.control_code = kwargs.get('control_code', None)
        self.invoice_number = kwargs.get('invoice_number', None)
        self.invoice_pages = kwargs.get('invoice_pages', None)
        self.check_number = kwargs.get('check_number', None)
        self.check_date = kwargs.get('check_date', None)
        self.pay_status = kwargs.get('pay_status', None)
        self.cleared_date = kwargs.get('cleared_date', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_date = kwargs.get('created_date', None)
        self.modified_by = kwargs.get('modified_by', None)
        self.modified_date = kwargs.get('modified_date', None)
        self.void = kwargs.get('void', None)
        self.dirty = kwargs.get('dirty', None)
        self.import_verified = kwargs.get('import_verified', None)
        self.accrual = kwargs.get('accrual', None)
        self.accrual_reversed = kwargs.get('accrual_reversed', None)
        self.accrual_reversed_date = kwargs.get('accrual_reversed_date', None)
        self.export_hold = kwargs.get('export_hold', None)
        self.gl_exported = kwargs.get('gl_exported', None)
        self.gl_exported_by = kwargs.get('gl_exported_by', None)
        self.gl_export_date = kwargs.get('gl_export_date', None)
        self.from_vendor = kwargs.get('from_vendor', None)
        self.has_been_split = kwargs.get('has_been_split', None)
        self.was_split_date = kwargs.get('was_split_date', None)
        self.trans_ref_num = kwargs.get('trans_ref_num', None)
        self.payment_type = kwargs.get('payment_type', None)
        self.actual_amount_paid = kwargs.get('actual_amount_paid', None)
        self.assigned_to = kwargs.get('assigned_to', None)
        self.assigned_date = kwargs.get('assigned_date', None)
        self.pay_source = kwargs.get('pay_source', None)
        self.pay_to = kwargs.get('pay_to', None)
        self.previous_balance = kwargs.get('previous_balance', None)
        self.balance_forward = kwargs.get('balance_forward', None)
        self.current_charges = kwargs.get('current_charges', None)
        self.bill_note = kwargs.get('bill_note', None)
        self.reversal_details = kwargs.get('reversal_details', None)
        self.excluded_from_accruals = kwargs.get('excluded_from_accruals', None)
        self.analyzing = kwargs.get('analyzing', None)
