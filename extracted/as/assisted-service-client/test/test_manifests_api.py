# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import assisted_service_client
from assisted_service_client.api.manifests_api import ManifestsApi  # noqa: E501
from assisted_service_client.rest import ApiException


class TestManifestsApi(unittest.TestCase):
    """ManifestsApi unit test stubs"""

    def setUp(self):
        self.api = assisted_service_client.api.manifests_api.ManifestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_create_cluster_manifest(self):
        """Test case for v2_create_cluster_manifest

        """
        pass

    def test_v2_delete_cluster_manifest(self):
        """Test case for v2_delete_cluster_manifest

        """
        pass

    def test_v2_download_cluster_manifest(self):
        """Test case for v2_download_cluster_manifest

        """
        pass

    def test_v2_list_cluster_manifests(self):
        """Test case for v2_list_cluster_manifests

        """
        pass

    def test_v2_update_cluster_manifest(self):
        """Test case for v2_update_cluster_manifest

        """
        pass


if __name__ == '__main__':
    unittest.main()
