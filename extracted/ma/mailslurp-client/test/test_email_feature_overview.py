# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.email_feature_overview import EmailFeatureOverview  # noqa: E501
from mailslurp_client.rest import ApiException

class TestEmailFeatureOverview(unittest.TestCase):
    """EmailFeatureOverview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailFeatureOverview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.email_feature_overview.EmailFeatureOverview()  # noqa: E501
        if include_optional :
            return EmailFeatureOverview(
                feature = 'amp', 
                title = '0', 
                description = '0', 
                category = 'css', 
                notes = '0', 
                notes_numbers = {
                    'key' : '0'
                    }, 
                feature_statistics = [
                    mailslurp_client.models.email_feature_family_statistics.EmailFeatureFamilyStatistics(
                        feature = 'amp', 
                        family = 'aol', 
                        platforms = [
                            mailslurp_client.models.email_feature_platform_statistics.EmailFeaturePlatformStatistics(
                                platform = 'android', 
                                versions = [
                                    mailslurp_client.models.email_feature_version_statistics.EmailFeatureVersionStatistics(
                                        version = '0', 
                                        support_flags = mailslurp_client.models.email_feature_support_flags.EmailFeatureSupportFlags(
                                            status = 'SUPPORTED', 
                                            notes = [
                                                '0'
                                                ], ), )
                                    ], )
                            ], )
                    ], 
                statuses = [
                    'SUPPORTED'
                    ]
            )
        else :
            return EmailFeatureOverview(
                feature = 'amp',
                statuses = [
                    'SUPPORTED'
                    ],
        )

    def testEmailFeatureOverview(self):
        """Test EmailFeatureOverview"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
