# (c) 2025, NetApp, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" unit tests NetApp StorageGRID Org Container Ansible module: na_sg_org_container"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import json
import pytest
import sys

from ansible_collections.netapp.storagegrid.tests.unit.compat import unittest
from ansible_collections.netapp.storagegrid.tests.unit.compat.mock import patch
from ansible.module_utils import basic
from ansible.module_utils._text import to_bytes
from ansible_collections.netapp.storagegrid.plugins.modules.na_sg_grid_ilm_policy import (
    ILM_policy as grid_ilm_policy_module,
)

if sys.version_info < (3, 11):
    pytestmark = pytest.mark.skip("Skipping Unit Tests on 3.11")

# REST API canned responses when mocking send_request
SRR = {
    # common responses
    "empty_good": ({"data": []}, None),
    "end_of_sequence": (None, "Unexpected call to send_request"),
    "delete_good": (None, None),
    "version_114": ({"data": {"productVersion": "11.4.0-20200721.1338.d3969b3"}}, None),
    "api_response_creation_succeeded": (
        {
            "data": {
                "name": "1 Copy Per Site",
                "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                "rules": ["r12345678901234567890"],
                "defaultRule": "r12345678901234567890",
                "id": "c5b6b40e-4ed6-41a9-9d07-bd25a3618517",
                "active": False,
                "activatedBy": ["b9bd8000-696b-11e6-9981-56847afe2222"],
            }
        },
        None,
    ),
    "api_response_existing_ilm_policy": (
        {
            "data": [
                {
                    "name": "1 Copy Per Site",
                    "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                    "rules": ["r12345678901234567890"],
                    "defaultRule": "r12345678901234567890",
                    "id": "c5b6b40e-4ed6-41a9-9d07-bd25a3618517",
                    "active": False,
                    "activatedBy": ["b9bd8000-696b-11e6-9981-56847afe2222"],
                }
            ]
        },
        None,
    ),
    "api_response_existing_ilm_policy_updated": (
        {
            "data": {
                "name": "1 Copy Per Site",
                "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                "rules": ["r12345678901234567890", "r12345678901234567891"],
                "defaultRule": "r12345678901234567890",
                "id": "c5b6b40e-4ed6-41a9-9d07-bd25a3618517",
                "active": False,
                "activatedBy": ["b9bd8000-696b-11e6-9981-56847afe2222"],
            }
        },
        None,
    ),
}


def set_module_args(args):
    """prepare arguments so that they will be picked up during module creation"""
    args = json.dumps({"ANSIBLE_MODULE_ARGS": args})
    basic._ANSIBLE_ARGS = to_bytes(args)  # pylint: disable=protected-access


class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the test case"""

    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""

    pass


def exit_json(*args, **kwargs):  # pylint: disable=unused-argument
    """function to patch over exit_json; package return data into an exception"""
    if "changed" not in kwargs:
        kwargs["changed"] = False
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):  # pylint: disable=unused-argument
    """function to patch over fail_json; package return data into an exception"""
    kwargs["failed"] = True
    raise AnsibleFailJson(kwargs)


class TestMyModule(unittest.TestCase):
    """a group of related Unit Tests"""

    def setUp(self):
        self.mock_module_helper = patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)

    def set_default_args_fail_check(self):
        return dict(
            {
                "name": "1 Copy Per Site",
                "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                "default_rule": "r12345678901234567890",
                "api_url": "gmi.example.com",
                "auth_token": "01234567-5678-9abc-78de-9fgabc123def",
                "validate_certs": False,
            }
        )

    def set_default_args_pass_check(self):
        return dict(
            {
                "name": "1 Copy Per Site",
                "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                "rules": ["r12345678901234567890"],
                "default_rule": "r12345678901234567890",
                "api_url": "gmi.example.com",
                "auth_token": "01234567-5678-9abc-78de-9fgabc123def",
                "validate_certs": False,
            }
        )

    def set_args_create_na_sg_grid_ilm_policy(self):
        return dict(
            {
                "name": "1 Copy Per Site",
                "reason": "The 1 Copy Per Site policy places 1 replicated copy at each site",
                "rules": ["r12345678901234567890"],
                "default_rule": "r12345678901234567890",
                "api_url": "gmi.example.com",
                "auth_token": "01234567-5678-9abc-78de-9fgabc123def",
                "validate_certs": False,
            }
        )

    def set_args_delete_na_sg_grid_ilm_policy(self):
        return dict(
            {
                "state": "absent",
                "name": "1 Copy Per Site",
                "api_url": "gmi.example.com",
                "auth_token": "01234567-5678-9abc-78de-9fgabc123def",
                "validate_certs": False,
            }
        )

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_module_fail_when_required_args_missing(self, mock_request):
        """required arguments are reported as errors"""
        with pytest.raises(AnsibleFailJson) as exc:
            set_module_args(self.set_default_args_fail_check())
            grid_ilm_policy_module()
        print("Info: test_module_fail_when_required_args_missing: %s" % exc.value.args[0]["msg"])

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_module_succeed_when_required_args_present(self, mock_request):
        """required arguments are reported as errors"""
        mock_request.side_effect = [
            SRR["version_114"],
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            set_module_args(self.set_default_args_pass_check())
            grid_ilm_policy_module()
            exit_json(changed=True, msg="Induced arguments check")
        print("Info: test_module_fail_when_required_args_present: %s" % exc.value.args[0]["msg"])
        assert exc.value.args[0]["changed"]

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_create_na_sg_grid_ilm_policy_pass(self, mock_request):
        set_module_args(self.set_args_create_na_sg_grid_ilm_policy())
        mock_request.side_effect = [
            SRR["version_114"],
            SRR["empty_good"],  # get
            SRR["api_response_creation_succeeded"],  # post
            SRR["end_of_sequence"],
        ]
        my_obj = grid_ilm_policy_module()
        with pytest.raises(AnsibleExitJson) as exc:
            my_obj.apply()
        print("Info: test_create_na_sg_org_container_pass: %s" % repr(exc.value.args[0]))
        assert exc.value.args[0]["changed"]

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_idempotent_create_na_sg_grid_ilm_policy_pass(self, mock_request):
        set_module_args(self.set_args_create_na_sg_grid_ilm_policy())
        mock_request.side_effect = [
            SRR["version_114"],
            SRR["api_response_existing_ilm_policy"],  # get
            SRR["end_of_sequence"],
        ]
        my_obj = grid_ilm_policy_module()
        with pytest.raises(AnsibleExitJson) as exc:
            my_obj.apply()
        print("Info: test_idempotent_create_na_sg_grid_ilm_policy_pass: %s" % repr(exc.value.args[0]))
        assert not exc.value.args[0]["changed"]

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_update_na_sg_grid_ilm_policy_pass(self, mock_request):
        args = self.set_args_create_na_sg_grid_ilm_policy()
        args.update(
            {
                "rules": ["r12345678901234567890", "r12345678901234567891"],
            }
        )
        set_module_args(args)
        mock_request.side_effect = [
            SRR["version_114"],
            SRR["api_response_existing_ilm_policy"],  # get
            SRR["api_response_existing_ilm_policy_updated"],  # put
            SRR["end_of_sequence"],
        ]
        my_obj = grid_ilm_policy_module()
        with pytest.raises(AnsibleExitJson) as exc:
            my_obj.apply()
        print("Info: test_update_na_sg_org_container_pass: %s" % repr(exc.value.args[0]))
        assert exc.value.args[0]["changed"]

    @patch("ansible_collections.netapp.storagegrid.plugins.module_utils.netapp.SGRestAPI.send_request")
    def test_delete_na_sg_grid_ilm_policy_pass(self, mock_request):
        set_module_args(self.set_args_delete_na_sg_grid_ilm_policy())
        mock_request.side_effect = [
            SRR["version_114"],
            SRR["api_response_existing_ilm_policy"],  # get
            SRR["delete_good"],  # delete
            SRR["end_of_sequence"],
        ]
        my_obj = grid_ilm_policy_module()
        with pytest.raises(AnsibleExitJson) as exc:
            my_obj.apply()
        print("Info: test_delete_na_sg_grid_ilm_policy_pass: %s" % repr(exc.value.args[0]))
        assert exc.value.args[0]["changed"]
