# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountMeterResponse(Model):
    """AccountMeterResponse.

    :param account_meter_id: The account meter identifier <span
     class='property-internal'>Required (defined)</span>
    :type account_meter_id: int
    :param account:
    :type account: ~energycap.sdk.models.AccountChild
    :param meter:
    :type meter: ~energycap.sdk.models.MeterChild
    :param begin_date: The beginning date and time for this account meter
     relationship <span class='property-internal'>Required (defined)</span>
    :type begin_date: datetime
    :param end_date: The ending date and time for this account meter
     relationship <span class='property-internal'>Required (defined)</span>
    :type end_date: datetime
    :param general_ledger:
    :type general_ledger: ~energycap.sdk.models.GeneralLedgerChild
    :param vendor_type:
    :type vendor_type: ~energycap.sdk.models.VendorTypeChild
    :param deregulated: Indicates if the account meter is deregulated <span
     class='property-internal'>Required (defined)</span>
    :type deregulated: bool
    :param form_templates: The template assigned to this account meter <span
     class='property-internal'>Required (defined)</span>
    :type form_templates: list[~energycap.sdk.models.FormTemplateChild]
    :param rates: The rate assigned to this account meter <span
     class='property-internal'>Required (defined)</span>
    :type rates: list[~energycap.sdk.models.AccountRateChild]
    """

    _attribute_map = {
        'account_meter_id': {'key': 'accountMeterId', 'type': 'int'},
        'account': {'key': 'account', 'type': 'AccountChild'},
        'meter': {'key': 'meter', 'type': 'MeterChild'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'general_ledger': {'key': 'generalLedger', 'type': 'GeneralLedgerChild'},
        'vendor_type': {'key': 'vendorType', 'type': 'VendorTypeChild'},
        'deregulated': {'key': 'deregulated', 'type': 'bool'},
        'form_templates': {'key': 'formTemplates', 'type': '[FormTemplateChild]'},
        'rates': {'key': 'rates', 'type': '[AccountRateChild]'},
    }

    def __init__(self, *, account_meter_id: int=None, account=None, meter=None, begin_date=None, end_date=None, general_ledger=None, vendor_type=None, deregulated: bool=None, form_templates=None, rates=None, **kwargs) -> None:
        super(AccountMeterResponse, self).__init__(**kwargs)
        self.account_meter_id = account_meter_id
        self.account = account
        self.meter = meter
        self.begin_date = begin_date
        self.end_date = end_date
        self.general_ledger = general_ledger
        self.vendor_type = vendor_type
        self.deregulated = deregulated
        self.form_templates = form_templates
        self.rates = rates
