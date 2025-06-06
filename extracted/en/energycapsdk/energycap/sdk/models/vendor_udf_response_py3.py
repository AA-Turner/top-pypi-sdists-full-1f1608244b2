# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VendorUDFResponse(Model):
    """VendorUDFResponse.

    :param vendor_id: The vendor identifier
    :type vendor_id: int
    :param vendor_code: The vendor code
    :type vendor_code: str
    :param vendor_info: The vendor info
    :type vendor_info: str
    :param udfs: An array of user-defined fields (UDFs)
    :type udfs: list[~energycap.sdk.models.UDFFieldChild]
    """

    _attribute_map = {
        'vendor_id': {'key': 'vendorId', 'type': 'int'},
        'vendor_code': {'key': 'vendorCode', 'type': 'str'},
        'vendor_info': {'key': 'vendorInfo', 'type': 'str'},
        'udfs': {'key': 'udfs', 'type': '[UDFFieldChild]'},
    }

    def __init__(self, *, vendor_id: int=None, vendor_code: str=None, vendor_info: str=None, udfs=None, **kwargs) -> None:
        super(VendorUDFResponse, self).__init__(**kwargs)
        self.vendor_id = vendor_id
        self.vendor_code = vendor_code
        self.vendor_info = vendor_info
        self.udfs = udfs
