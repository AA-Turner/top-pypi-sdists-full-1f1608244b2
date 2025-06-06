# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillViewAddressChild(Model):
    """BillViewAddressChild.

    :param address_type_id: The address type identifier
    :type address_type_id: int
    :param line1: The line 1 of the address
    :type line1: str
    :param line2: The line 2 of the address
    :type line2: str
    :param line3: The line 2 of the address
    :type line3: str
    :param city: The city of the address
    :type city: str
    :param state: The state of the address
    :type state: str
    :param country: The country of the address
    :type country: str
    :param postal_code: The postal code of the address
    :type postal_code: str
    """

    _attribute_map = {
        'address_type_id': {'key': 'addressTypeId', 'type': 'int'},
        'line1': {'key': 'line1', 'type': 'str'},
        'line2': {'key': 'line2', 'type': 'str'},
        'line3': {'key': 'line3', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
    }

    def __init__(self, *, address_type_id: int=None, line1: str=None, line2: str=None, line3: str=None, city: str=None, state: str=None, country: str=None, postal_code: str=None, **kwargs) -> None:
        super(BillViewAddressChild, self).__init__(**kwargs)
        self.address_type_id = address_type_id
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
