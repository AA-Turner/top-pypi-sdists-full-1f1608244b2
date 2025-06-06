# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceResponse(Model):
    """PlaceResponse.

    :param parent:
    :type parent: ~energycap.sdk.models.PlaceChild
    :param place_type:
    :type place_type: ~energycap.sdk.models.PlaceTypeResponse
    :param created_date: The date and time the place was created
    :type created_date: datetime
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification to
     the place
    :type modified_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param address:
    :type address: ~energycap.sdk.models.AddressChild
    :param build_date: The date and time the place was built
    :type build_date: datetime
    :param primary_use:
    :type primary_use: ~energycap.sdk.models.PrimaryUseChild
    :param weather_station:
    :type weather_station: ~energycap.sdk.models.WeatherStationChild
    :param size:
    :type size: ~energycap.sdk.models.PlaceSizeChild
    :param benchmark1:
    :type benchmark1: ~energycap.sdk.models.LatestBenchmarkValue
    :param benchmark2:
    :type benchmark2: ~energycap.sdk.models.LatestBenchmarkValue
    :param benchmark3:
    :type benchmark3: ~energycap.sdk.models.LatestBenchmarkValue
    :param energy_star_enabled: Tells whether energy star is enabled for the
     given place
    :type energy_star_enabled: bool
    :param energy_star_rating:
    :type energy_star_rating: ~energycap.sdk.models.EnergyStarRatingChild
    :param places: An array of child places. A child place is one directly
     beneath the current place on the buildings and meters tree
    :type places: list[~energycap.sdk.models.PlaceChild]
    :param meters: An array of child meters. A child meter is one directly
     beneath the current place on the buildings and meters tree
    :type meters: list[~energycap.sdk.models.MeterChild]
    :param contact:
    :type contact: ~energycap.sdk.models.ContactChild
    :param place_description: A description of the place
    :type place_description: str
    :param wattics_site:
    :type wattics_site: ~energycap.sdk.models.WatticsSite
    :param place_id: The place identifier
    :type place_id: int
    :param place_code: The place code
    :type place_code: str
    :param place_info: The place info
    :type place_info: str
    """

    _attribute_map = {
        'parent': {'key': 'parent', 'type': 'PlaceChild'},
        'place_type': {'key': 'placeType', 'type': 'PlaceTypeResponse'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'address': {'key': 'address', 'type': 'AddressChild'},
        'build_date': {'key': 'buildDate', 'type': 'iso-8601'},
        'primary_use': {'key': 'primaryUse', 'type': 'PrimaryUseChild'},
        'weather_station': {'key': 'weatherStation', 'type': 'WeatherStationChild'},
        'size': {'key': 'size', 'type': 'PlaceSizeChild'},
        'benchmark1': {'key': 'benchmark1', 'type': 'LatestBenchmarkValue'},
        'benchmark2': {'key': 'benchmark2', 'type': 'LatestBenchmarkValue'},
        'benchmark3': {'key': 'benchmark3', 'type': 'LatestBenchmarkValue'},
        'energy_star_enabled': {'key': 'energyStarEnabled', 'type': 'bool'},
        'energy_star_rating': {'key': 'energyStarRating', 'type': 'EnergyStarRatingChild'},
        'places': {'key': 'places', 'type': '[PlaceChild]'},
        'meters': {'key': 'meters', 'type': '[MeterChild]'},
        'contact': {'key': 'contact', 'type': 'ContactChild'},
        'place_description': {'key': 'placeDescription', 'type': 'str'},
        'wattics_site': {'key': 'watticsSite', 'type': 'WatticsSite'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PlaceResponse, self).__init__(**kwargs)
        self.parent = kwargs.get('parent', None)
        self.place_type = kwargs.get('place_type', None)
        self.created_date = kwargs.get('created_date', None)
        self.created_by = kwargs.get('created_by', None)
        self.modified_date = kwargs.get('modified_date', None)
        self.modified_by = kwargs.get('modified_by', None)
        self.address = kwargs.get('address', None)
        self.build_date = kwargs.get('build_date', None)
        self.primary_use = kwargs.get('primary_use', None)
        self.weather_station = kwargs.get('weather_station', None)
        self.size = kwargs.get('size', None)
        self.benchmark1 = kwargs.get('benchmark1', None)
        self.benchmark2 = kwargs.get('benchmark2', None)
        self.benchmark3 = kwargs.get('benchmark3', None)
        self.energy_star_enabled = kwargs.get('energy_star_enabled', None)
        self.energy_star_rating = kwargs.get('energy_star_rating', None)
        self.places = kwargs.get('places', None)
        self.meters = kwargs.get('meters', None)
        self.contact = kwargs.get('contact', None)
        self.place_description = kwargs.get('place_description', None)
        self.wattics_site = kwargs.get('wattics_site', None)
        self.place_id = kwargs.get('place_id', None)
        self.place_code = kwargs.get('place_code', None)
        self.place_info = kwargs.get('place_info', None)
