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

from pulpcore.client.pulpcore.api.orphans_api import OrphansApi


class TestOrphansApi(unittest.TestCase):
    """OrphansApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrphansApi()

    def tearDown(self) -> None:
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete orphans
        """
        pass


if __name__ == '__main__':
    unittest.main()
