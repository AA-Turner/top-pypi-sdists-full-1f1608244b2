# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VendorTypeChild(Model):
    """VendorTypeChild.

    :param vendor_type_id: The vendor type identifier
    :type vendor_type_id: int
    :param vendor_type_code: The vendor type code
    :type vendor_type_code: str
    """

    _attribute_map = {
        'vendor_type_id': {'key': 'vendorTypeId', 'type': 'int'},
        'vendor_type_code': {'key': 'vendorTypeCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VendorTypeChild, self).__init__(**kwargs)
        self.vendor_type_id = kwargs.get('vendor_type_id', None)
        self.vendor_type_code = kwargs.get('vendor_type_code', None)
