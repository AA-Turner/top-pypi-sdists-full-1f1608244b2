# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pulpcore.client.pulpcore.models.nested_open_pgp_public_subkey import NestedOpenPGPPublicSubkey

class TestNestedOpenPGPPublicSubkey(unittest.TestCase):
    """NestedOpenPGPPublicSubkey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NestedOpenPGPPublicSubkey:
        """Test NestedOpenPGPPublicSubkey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NestedOpenPGPPublicSubkey`
        """
        model = NestedOpenPGPPublicSubkey()
        if include_optional:
            return NestedOpenPGPPublicSubkey(
                fingerprint = '0',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return NestedOpenPGPPublicSubkey(
                fingerprint = '0',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testNestedOpenPGPPublicSubkey(self):
        """Test NestedOpenPGPPublicSubkey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
