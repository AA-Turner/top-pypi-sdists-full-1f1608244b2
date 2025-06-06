# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WeatherImportResult(Model):
    """WeatherImportResult.

    :param begin_date: The begin date of the weather data that was imported
    :type begin_date: datetime
    :param end_date: The end date of the weather data that was imported
    :type end_date: datetime
    :param weather_station_summaries: List of weather stations and the number
     of readings that were imported for each
    :type weather_station_summaries:
     list[~energycap.sdk.models.WeatherStationSummary]
    """

    _attribute_map = {
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'weather_station_summaries': {'key': 'weatherStationSummaries', 'type': '[WeatherStationSummary]'},
    }

    def __init__(self, **kwargs):
        super(WeatherImportResult, self).__init__(**kwargs)
        self.begin_date = kwargs.get('begin_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.weather_station_summaries = kwargs.get('weather_station_summaries', None)
