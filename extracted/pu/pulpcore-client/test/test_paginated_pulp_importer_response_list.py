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

from pulpcore.client.pulpcore.models.paginated_pulp_importer_response_list import PaginatedPulpImporterResponseList

class TestPaginatedPulpImporterResponseList(unittest.TestCase):
    """PaginatedPulpImporterResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPulpImporterResponseList:
        """Test PaginatedPulpImporterResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPulpImporterResponseList`
        """
        model = PaginatedPulpImporterResponseList()
        if include_optional:
            return PaginatedPulpImporterResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulpcore.models.pulp_importer_response.PulpImporterResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        repo_mapping = {
                            'key' : ''
                            }, )
                    ]
            )
        else:
            return PaginatedPulpImporterResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.pulp_importer_response.PulpImporterResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        repo_mapping = {
                            'key' : ''
                            }, )
                    ],
        )
        """

    def testPaginatedPulpImporterResponseList(self):
        """Test PaginatedPulpImporterResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
