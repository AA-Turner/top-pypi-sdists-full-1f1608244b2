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

from pulpcore.client.pulpcore.models.patched_composite_content_guard import PatchedCompositeContentGuard

class TestPatchedCompositeContentGuard(unittest.TestCase):
    """PatchedCompositeContentGuard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedCompositeContentGuard:
        """Test PatchedCompositeContentGuard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedCompositeContentGuard`
        """
        model = PatchedCompositeContentGuard()
        if include_optional:
            return PatchedCompositeContentGuard(
                name = '0',
                description = '0',
                guards = [
                    ''
                    ]
            )
        else:
            return PatchedCompositeContentGuard(
        )
        """

    def testPatchedCompositeContentGuard(self):
        """Test PatchedCompositeContentGuard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
