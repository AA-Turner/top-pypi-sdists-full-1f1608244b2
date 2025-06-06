# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.dag_warning_collection_response import DAGWarningCollectionResponse

class TestDAGWarningCollectionResponse(unittest.TestCase):
    """DAGWarningCollectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DAGWarningCollectionResponse:
        """Test DAGWarningCollectionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DAGWarningCollectionResponse`
        """
        model = DAGWarningCollectionResponse()
        if include_optional:
            return DAGWarningCollectionResponse(
                dag_warnings = [
                    airflow_client.client.models.dag_warning_response.DAGWarningResponse(
                        dag_id = '', 
                        message = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        warning_type = 'asset conflict', )
                    ],
                total_entries = 56
            )
        else:
            return DAGWarningCollectionResponse(
                dag_warnings = [
                    airflow_client.client.models.dag_warning_response.DAGWarningResponse(
                        dag_id = '', 
                        message = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        warning_type = 'asset conflict', )
                    ],
                total_entries = 56,
        )
        """

    def testDAGWarningCollectionResponse(self):
        """Test DAGWarningCollectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
