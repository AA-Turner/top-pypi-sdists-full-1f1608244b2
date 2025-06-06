# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from airflow_client.client.models.asset_event_response import AssetEventResponse

class TestAssetEventResponse(unittest.TestCase):
    """AssetEventResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetEventResponse:
        """Test AssetEventResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetEventResponse`
        """
        model = AssetEventResponse()
        if include_optional:
            return AssetEventResponse(
                asset_id = 56,
                created_dagruns = [
                    airflow_client.client.models.dag_run_asset_reference.DagRunAssetReference(
                        dag_id = '', 
                        data_interval_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data_interval_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        logical_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        run_id = '', 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        state = '', )
                    ],
                extra = airflow_client.client.models.extra.extra(),
                group = '',
                id = 56,
                name = '',
                source_dag_id = '',
                source_map_index = 56,
                source_run_id = '',
                source_task_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                uri = ''
            )
        else:
            return AssetEventResponse(
                asset_id = 56,
                created_dagruns = [
                    airflow_client.client.models.dag_run_asset_reference.DagRunAssetReference(
                        dag_id = '', 
                        data_interval_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data_interval_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        logical_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        run_id = '', 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        state = '', )
                    ],
                id = 56,
                source_map_index = 56,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testAssetEventResponse(self):
        """Test AssetEventResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
