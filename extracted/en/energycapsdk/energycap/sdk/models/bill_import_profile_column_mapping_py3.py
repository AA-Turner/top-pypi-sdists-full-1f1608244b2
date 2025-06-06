# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillImportProfileColumnMapping(Model):
    """BillImportProfileColumnMapping.

    All required parameters must be populated in order to send to Azure.

    :param date_format: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>One of mm/dd/yyyy, Month dd yyyy, dd/mm/yyyy, dd
     Month yyyy, yyyymmdd </span>
    :type date_format: str
    :param account_code_column_index: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type account_code_column_index: int
    :param start_date_column_index: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type start_date_column_index: int
    :param end_date_column_index: Required.  <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type end_date_column_index: int
    :param vendor_code_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type vendor_code_column_index: int
    :param pay_amount_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type pay_amount_column_index: int
    :param billing_period_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type billing_period_column_index: int
    :param account_period_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type account_period_column_index: int
    :param statement_date_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type statement_date_column_index: int
    :param due_date_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type due_date_column_index: int
    :param control_code_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type control_code_column_index: int
    :param invoice_number_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type invoice_number_column_index: int
    :param meter_code_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type meter_code_column_index: int
    :param commodity_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type commodity_column_index: int
    :param service_charge_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type service_charge_column_index: int
    :param ace_flag_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type ace_flag_column_index: int
    :param vpr_flag_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type vpr_flag_column_index: int
    :param rate_column_index:  <span class='property-internal'>Must be between
     1 and 2147483647</span>
    :type rate_column_index: int
    :param serial_number_column_index:  <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type serial_number_column_index: int
    :param bill_note_column_index:  <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type bill_note_column_index: int
    :param observations:  <span class='property-internal'>Cannot be
     Empty</span>
    :type observations:
     list[~energycap.sdk.models.BillImportProfileObservation]
    """

    _validation = {
        'date_format': {'required': True},
        'account_code_column_index': {'required': True, 'maximum': 2147483647, 'minimum': 1},
        'start_date_column_index': {'required': True, 'maximum': 2147483647, 'minimum': 1},
        'end_date_column_index': {'required': True, 'maximum': 2147483647, 'minimum': 1},
        'vendor_code_column_index': {'maximum': 2147483647, 'minimum': 1},
        'pay_amount_column_index': {'maximum': 2147483647, 'minimum': 1},
        'billing_period_column_index': {'maximum': 2147483647, 'minimum': 1},
        'account_period_column_index': {'maximum': 2147483647, 'minimum': 1},
        'statement_date_column_index': {'maximum': 2147483647, 'minimum': 1},
        'due_date_column_index': {'maximum': 2147483647, 'minimum': 1},
        'control_code_column_index': {'maximum': 2147483647, 'minimum': 1},
        'invoice_number_column_index': {'maximum': 2147483647, 'minimum': 1},
        'meter_code_column_index': {'maximum': 2147483647, 'minimum': 1},
        'commodity_column_index': {'maximum': 2147483647, 'minimum': 1},
        'service_charge_column_index': {'maximum': 2147483647, 'minimum': 1},
        'ace_flag_column_index': {'maximum': 2147483647, 'minimum': 1},
        'vpr_flag_column_index': {'maximum': 2147483647, 'minimum': 1},
        'rate_column_index': {'maximum': 2147483647, 'minimum': 1},
        'serial_number_column_index': {'maximum': 2147483647, 'minimum': 1},
        'bill_note_column_index': {'maximum': 2147483647, 'minimum': 1},
    }

    _attribute_map = {
        'date_format': {'key': 'dateFormat', 'type': 'str'},
        'account_code_column_index': {'key': 'accountCodeColumnIndex', 'type': 'int'},
        'start_date_column_index': {'key': 'startDateColumnIndex', 'type': 'int'},
        'end_date_column_index': {'key': 'endDateColumnIndex', 'type': 'int'},
        'vendor_code_column_index': {'key': 'vendorCodeColumnIndex', 'type': 'int'},
        'pay_amount_column_index': {'key': 'payAmountColumnIndex', 'type': 'int'},
        'billing_period_column_index': {'key': 'billingPeriodColumnIndex', 'type': 'int'},
        'account_period_column_index': {'key': 'accountPeriodColumnIndex', 'type': 'int'},
        'statement_date_column_index': {'key': 'statementDateColumnIndex', 'type': 'int'},
        'due_date_column_index': {'key': 'dueDateColumnIndex', 'type': 'int'},
        'control_code_column_index': {'key': 'controlCodeColumnIndex', 'type': 'int'},
        'invoice_number_column_index': {'key': 'invoiceNumberColumnIndex', 'type': 'int'},
        'meter_code_column_index': {'key': 'meterCodeColumnIndex', 'type': 'int'},
        'commodity_column_index': {'key': 'commodityColumnIndex', 'type': 'int'},
        'service_charge_column_index': {'key': 'serviceChargeColumnIndex', 'type': 'int'},
        'ace_flag_column_index': {'key': 'aceFlagColumnIndex', 'type': 'int'},
        'vpr_flag_column_index': {'key': 'vprFlagColumnIndex', 'type': 'int'},
        'rate_column_index': {'key': 'rateColumnIndex', 'type': 'int'},
        'serial_number_column_index': {'key': 'serialNumberColumnIndex', 'type': 'int'},
        'bill_note_column_index': {'key': 'billNoteColumnIndex', 'type': 'int'},
        'observations': {'key': 'observations', 'type': '[BillImportProfileObservation]'},
    }

    def __init__(self, *, date_format: str, account_code_column_index: int, start_date_column_index: int, end_date_column_index: int, vendor_code_column_index: int=None, pay_amount_column_index: int=None, billing_period_column_index: int=None, account_period_column_index: int=None, statement_date_column_index: int=None, due_date_column_index: int=None, control_code_column_index: int=None, invoice_number_column_index: int=None, meter_code_column_index: int=None, commodity_column_index: int=None, service_charge_column_index: int=None, ace_flag_column_index: int=None, vpr_flag_column_index: int=None, rate_column_index: int=None, serial_number_column_index: int=None, bill_note_column_index: int=None, observations=None, **kwargs) -> None:
        super(BillImportProfileColumnMapping, self).__init__(**kwargs)
        self.date_format = date_format
        self.account_code_column_index = account_code_column_index
        self.start_date_column_index = start_date_column_index
        self.end_date_column_index = end_date_column_index
        self.vendor_code_column_index = vendor_code_column_index
        self.pay_amount_column_index = pay_amount_column_index
        self.billing_period_column_index = billing_period_column_index
        self.account_period_column_index = account_period_column_index
        self.statement_date_column_index = statement_date_column_index
        self.due_date_column_index = due_date_column_index
        self.control_code_column_index = control_code_column_index
        self.invoice_number_column_index = invoice_number_column_index
        self.meter_code_column_index = meter_code_column_index
        self.commodity_column_index = commodity_column_index
        self.service_charge_column_index = service_charge_column_index
        self.ace_flag_column_index = ace_flag_column_index
        self.vpr_flag_column_index = vpr_flag_column_index
        self.rate_column_index = rate_column_index
        self.serial_number_column_index = serial_number_column_index
        self.bill_note_column_index = bill_note_column_index
        self.observations = observations
