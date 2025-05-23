# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EmissionSourceResponse(Model):
    """EmissionSourceResponse.

    :param emission_source_id: The emission source identifier
    :type emission_source_id: int
    :param emission_source_code: The emission source code
    :type emission_source_code: str
    :param emission_source_info: The emission source info
    :type emission_source_info: str
    :param collection:
    :type collection: ~energycap.sdk.models.CollectionChild
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param default_scope_category:
    :type default_scope_category: ~energycap.sdk.models.GHGScopeCategoryChild
    :param default_emission_factor:
    :type default_emission_factor: ~energycap.sdk.models.GHGFactorChild
    :param address:
    :type address: ~energycap.sdk.models.AddressChild
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The date and time the emission source was created
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification of
     the emission source
    :type modified_date: datetime
    :param note: The emission source description
    :type note: str
    :param active: Indicates whether the emission source is active
    :type active: bool
    :param meter:
    :type meter: ~energycap.sdk.models.MeterLink
    """

    _attribute_map = {
        'emission_source_id': {'key': 'emissionSourceId', 'type': 'int'},
        'emission_source_code': {'key': 'emissionSourceCode', 'type': 'str'},
        'emission_source_info': {'key': 'emissionSourceInfo', 'type': 'str'},
        'collection': {'key': 'collection', 'type': 'CollectionChild'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'default_scope_category': {'key': 'defaultScopeCategory', 'type': 'GHGScopeCategoryChild'},
        'default_emission_factor': {'key': 'defaultEmissionFactor', 'type': 'GHGFactorChild'},
        'address': {'key': 'address', 'type': 'AddressChild'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'note': {'key': 'note', 'type': 'str'},
        'active': {'key': 'active', 'type': 'bool'},
        'meter': {'key': 'meter', 'type': 'MeterLink'},
    }

    def __init__(self, *, emission_source_id: int=None, emission_source_code: str=None, emission_source_info: str=None, collection=None, commodity=None, default_scope_category=None, default_emission_factor=None, address=None, created_by=None, created_date=None, modified_by=None, modified_date=None, note: str=None, active: bool=None, meter=None, **kwargs) -> None:
        super(EmissionSourceResponse, self).__init__(**kwargs)
        self.emission_source_id = emission_source_id
        self.emission_source_code = emission_source_code
        self.emission_source_info = emission_source_info
        self.collection = collection
        self.commodity = commodity
        self.default_scope_category = default_scope_category
        self.default_emission_factor = default_emission_factor
        self.address = address
        self.created_by = created_by
        self.created_date = created_date
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.note = note
        self.active = active
        self.meter = meter
