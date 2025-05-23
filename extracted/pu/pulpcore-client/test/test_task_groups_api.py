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

from pulpcore.client.pulpcore.api.task_groups_api import TaskGroupsApi


class TestTaskGroupsApi(unittest.TestCase):
    """TaskGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TaskGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_list(self) -> None:
        """Test case for list

        List task groups
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a task group
        """
        pass

    def test_task_groups_cancel(self) -> None:
        """Test case for task_groups_cancel

        Cancel a task group
        """
        pass


if __name__ == '__main__':
    unittest.main()
