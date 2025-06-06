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

from pulpcore.client.pulpcore.models.open_pgp_keyring import OpenPGPKeyring

class TestOpenPGPKeyring(unittest.TestCase):
    """OpenPGPKeyring unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenPGPKeyring:
        """Test OpenPGPKeyring
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenPGPKeyring`
        """
        model = OpenPGPKeyring()
        if include_optional:
            return OpenPGPKeyring(
                pulp_labels = {
                    'key' : ''
                    },
                name = '0',
                description = '0',
                retain_repo_versions = 1,
                remote = ''
            )
        else:
            return OpenPGPKeyring(
                name = '0',
        )
        """

    def testOpenPGPKeyring(self):
        """Test OpenPGPKeyring"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
