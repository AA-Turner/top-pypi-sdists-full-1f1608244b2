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
from assisted_service_client.api.events_api import EventsApi  # noqa: E501
from assisted_service_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = assisted_service_client.api.events_api.EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_list_events(self):
        """Test case for v2_list_events

        """
        pass

    def test_v2_trigger_event(self):
        """Test case for v2_trigger_event

        """
        pass


if __name__ == '__main__':
    unittest.main()
