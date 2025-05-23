# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class YearRange(Model):
    """General purpose year range DTO.

    :param start_year: The start year for the range
    :type start_year: int
    :param end_year: The end year for the range
    :type end_year: int
    """

    _attribute_map = {
        'start_year': {'key': 'startYear', 'type': 'int'},
        'end_year': {'key': 'endYear', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(YearRange, self).__init__(**kwargs)
        self.start_year = kwargs.get('start_year', None)
        self.end_year = kwargs.get('end_year', None)
