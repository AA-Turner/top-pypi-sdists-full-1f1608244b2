# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cudo_compute
from cudo_compute.api.search_api import SearchApi  # noqa: E501
from cudo_compute.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = cudo_compute.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_regions(self):
        """Test case for list_regions

        Regions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
