# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterSearchRequest(Model):
    """Parameters to use for performing a utility platform meter search.

    :param search_type: Type of input to use for meter search <span
     class='property-internal'>One of Address, SerialNumber </span>
    :type search_type: str
    :param addresses: List of premise ids to search for <span
     class='property-internal'>Required when SearchType is set to
     Address</span><span class='property-internal'>List cannot be empty</span>
    :type addresses: list[str]
    :param serial_numbers: List of serial numbers to search for <span
     class='property-internal'>Required when SearchType is set to
     SerialNumber</span><span class='property-internal'>List cannot be
     empty</span>
    :type serial_numbers: list[str]
    """

    _attribute_map = {
        'search_type': {'key': 'searchType', 'type': 'str'},
        'addresses': {'key': 'addresses', 'type': '[str]'},
        'serial_numbers': {'key': 'serialNumbers', 'type': '[str]'},
    }

    def __init__(self, *, search_type: str=None, addresses=None, serial_numbers=None, **kwargs) -> None:
        super(MeterSearchRequest, self).__init__(**kwargs)
        self.search_type = search_type
        self.addresses = addresses
        self.serial_numbers = serial_numbers
