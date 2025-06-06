# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SearchResponse(Model):
    """SearchResponse.

    :param cost_centers: The collection of cost centers
    :type cost_centers: list[~energycap.sdk.models.SearchCostCenterChild]
    :param accounts: The collection of accounts
    :type accounts: list[~energycap.sdk.models.SearchAccountChild]
    :param places: The collection of places
    :type places: list[~energycap.sdk.models.SearchPlaceChild]
    :param meters: The collection of meters
    :type meters: list[~energycap.sdk.models.SearchMeterChild]
    :param place_groups: The collection of place groups
    :type place_groups: list[~energycap.sdk.models.SearchPlaceGroup]
    :param collections: The collection of CarbonHub collections
    :type collections: list[~energycap.sdk.models.SearchCollectionChild]
    :param emission_sources: The collection of CarbonHub emissions sources
    :type emission_sources:
     list[~energycap.sdk.models.SearchEmissionSourceChild]
    """

    _attribute_map = {
        'cost_centers': {'key': 'costCenters', 'type': '[SearchCostCenterChild]'},
        'accounts': {'key': 'accounts', 'type': '[SearchAccountChild]'},
        'places': {'key': 'places', 'type': '[SearchPlaceChild]'},
        'meters': {'key': 'meters', 'type': '[SearchMeterChild]'},
        'place_groups': {'key': 'placeGroups', 'type': '[SearchPlaceGroup]'},
        'collections': {'key': 'collections', 'type': '[SearchCollectionChild]'},
        'emission_sources': {'key': 'emissionSources', 'type': '[SearchEmissionSourceChild]'},
    }

    def __init__(self, *, cost_centers=None, accounts=None, places=None, meters=None, place_groups=None, collections=None, emission_sources=None, **kwargs) -> None:
        super(SearchResponse, self).__init__(**kwargs)
        self.cost_centers = cost_centers
        self.accounts = accounts
        self.places = places
        self.meters = meters
        self.place_groups = place_groups
        self.collections = collections
        self.emission_sources = emission_sources
