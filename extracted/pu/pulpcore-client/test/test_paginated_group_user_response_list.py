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

from pulpcore.client.pulpcore.models.paginated_group_user_response_list import PaginatedGroupUserResponseList

class TestPaginatedGroupUserResponseList(unittest.TestCase):
    """PaginatedGroupUserResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGroupUserResponseList:
        """Test PaginatedGroupUserResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGroupUserResponseList`
        """
        model = PaginatedGroupUserResponseList()
        if include_optional:
            return PaginatedGroupUserResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                        username = '', 
                        pulp_href = '', 
                        prn = '', )
                    ]
            )
        else:
            return PaginatedGroupUserResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                        username = '', 
                        pulp_href = '', 
                        prn = '', )
                    ],
        )
        """

    def testPaginatedGroupUserResponseList(self):
        """Test PaginatedGroupUserResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
