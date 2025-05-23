# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EmissionRecordResponse(Model):
    """EmissionRecordResponse.

    :param emission_record_id: The record identifier
    :type emission_record_id: int
    :param bill_id: The bill identifier, if this record originated from a bill
     in UtilityManagement
    :type bill_id: int
    :param emission_source:
    :type emission_source: ~energycap.sdk.models.EmissionSourceChild
    :param vendor:
    :type vendor: ~energycap.sdk.models.VendorChild
    :param start_date: The start date for the record
    :type start_date: datetime
    :param end_date: The end date for the record
    :type end_date: datetime
    :param billing_period: The bill's billing period, if this record
     originated from a bill in UtilityManagement
    :type billing_period: int
    :param emission_record_type:
    :type emission_record_type: ~energycap.sdk.models.EmissionRecordType
    :param scope_category:
    :type scope_category: ~energycap.sdk.models.GHGScopeCategoryChild
    :param factor:
    :type factor: ~energycap.sdk.models.GHGFactorChild
    :param quantity:
    :type quantity: ~energycap.sdk.models.ValueWithUnit
    :param cost:
    :type cost: ~energycap.sdk.models.ValueWithUnit
    :param total_emissions: The total GHG emissions for this record in kgCO2e.
    :type total_emissions: float
    :param emission_values: The GHG emissions for this record, split by
     greenhouse gas type
    :type emission_values: list[~energycap.sdk.models.GHGGroupEmissions]
    :param note: The note for this record
    :type note: str
    :param attachment: The attachment for this record
    :type attachment: str
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The date this record was created
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date this record was last modified
    :type modified_date: datetime
    :param creation_method: The emission record creation method
    :type creation_method: str
    """

    _attribute_map = {
        'emission_record_id': {'key': 'emissionRecordId', 'type': 'int'},
        'bill_id': {'key': 'billId', 'type': 'int'},
        'emission_source': {'key': 'emissionSource', 'type': 'EmissionSourceChild'},
        'vendor': {'key': 'vendor', 'type': 'VendorChild'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'emission_record_type': {'key': 'emissionRecordType', 'type': 'EmissionRecordType'},
        'scope_category': {'key': 'scopeCategory', 'type': 'GHGScopeCategoryChild'},
        'factor': {'key': 'factor', 'type': 'GHGFactorChild'},
        'quantity': {'key': 'quantity', 'type': 'ValueWithUnit'},
        'cost': {'key': 'cost', 'type': 'ValueWithUnit'},
        'total_emissions': {'key': 'totalEmissions', 'type': 'float'},
        'emission_values': {'key': 'emissionValues', 'type': '[GHGGroupEmissions]'},
        'note': {'key': 'note', 'type': 'str'},
        'attachment': {'key': 'attachment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'creation_method': {'key': 'creationMethod', 'type': 'str'},
    }

    def __init__(self, *, emission_record_id: int=None, bill_id: int=None, emission_source=None, vendor=None, start_date=None, end_date=None, billing_period: int=None, emission_record_type=None, scope_category=None, factor=None, quantity=None, cost=None, total_emissions: float=None, emission_values=None, note: str=None, attachment: str=None, created_by=None, created_date=None, modified_by=None, modified_date=None, creation_method: str=None, **kwargs) -> None:
        super(EmissionRecordResponse, self).__init__(**kwargs)
        self.emission_record_id = emission_record_id
        self.bill_id = bill_id
        self.emission_source = emission_source
        self.vendor = vendor
        self.start_date = start_date
        self.end_date = end_date
        self.billing_period = billing_period
        self.emission_record_type = emission_record_type
        self.scope_category = scope_category
        self.factor = factor
        self.quantity = quantity
        self.cost = cost
        self.total_emissions = total_emissions
        self.emission_values = emission_values
        self.note = note
        self.attachment = attachment
        self.created_by = created_by
        self.created_date = created_date
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.creation_method = creation_method
