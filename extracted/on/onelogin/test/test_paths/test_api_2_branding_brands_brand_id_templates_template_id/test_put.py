# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import onelogin
from onelogin.paths.api_2_branding_brands_brand_id_templates_template_id import put  # noqa: E501
from onelogin import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2BrandingBrandsBrandIdTemplatesTemplateId(ApiTestMixin, unittest.TestCase):
    """
    Api2BrandingBrandsBrandIdTemplatesTemplateId unit test stubs
        Update Message Template  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
