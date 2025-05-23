#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.

"""
This module provides a client class for NAT.
"""

import copy
import json
import logging
import uuid
import sys

from baidubce import bce_base_client
from baidubce.auth import bce_v1_signer
from baidubce.http import bce_http_client
from baidubce.http import handler
from baidubce.http import http_methods
from baidubce.services.vpc import nat_model
from baidubce import utils
from baidubce.utils import required
from baidubce import compat

if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf-8')

_logger = logging.getLogger(__name__)


default_billing_to_purchase_created = nat_model.Billing('Postpaid')
default_billing_to_purchase_reserved = nat_model.Billing()


class NatClient(bce_base_client.BceBaseClient):
    """
    NAT sdk client
    """
    version = b'/v1'

    def __init__(self, config=None):
        bce_base_client.BceBaseClient.__init__(self, config)

    def _merge_config(self, config=None):
        """
        :param config:
        :type config: baidubce.BceClientConfiguration
        """
        if config is None:
            return self.config
        else:
            new_config = copy.copy(self.config)
            new_config.merge_non_none_values(config)
            return new_config

    def _send_request(self, http_method, path,
                      body=None, headers=None, params=None,
                      config=None, body_parser=None):
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type':
                b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config, bce_v1_signer.sign, [handler.parse_error, body_parser],
            http_method, path, body, headers, params)

    @required(name=(bytes, str),
              vpc_id=(bytes, str))
    def create_nat(self, name, vpc_id, spec=None, billing=None, eips=None, dnat_eips=None, bind_eips=None,
                   client_token=None, config=None, cu_num=None, tags=None, resource_group_id=None, delete_protect=None):
        """
        Create a nat-gateway with the specified options.
        A nat gateway can bind only one public EIP,
        but can bind one or more EIPs in shared-bandwidth group

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if client token is provided.
        :type client_token: string

        :param name:
            The name of nat-gateway that will be created.
        :type name: string

        :param vpc_id:
            The id of VPC.
        :type vpc_id: string

        :param spec:
            The size of nat-gateway that needs to be created.
            It includes the following three types:
                small: support 5 public-IP-bindings at most,
                medium: support 10 public-IP-bindings at most,
                large: support 15 public-IP-bindings at most.
        :type spec: string

        :param cu_num:  The number of CU.
        :type cu_num: int

        :param billing:
            Billing information.
        :type billing: nat_model.Billing

        :param eips:
            A public EIP or one/more EIPs in shared-bandwidth group,
            which will be bound with nat-gateway.
        :type eips: list<String>

        :param dnat_eips:
        :type dnat_eips: list<String>

        :param bind_eips:
            A public EIP or one/more EIPs in shared-bandwidth group,
            which will be bound with nat-gateway, only for enhance nat.
        :type bind_eips: list<String>

        :param tags:
            The tags of nat-gateway that will be created.
        :type tags: list<String>

        :param resource_group_id:
            The resource group id of nat-gateway that will be created.
        :type resource_group_id: string

        :param delete_protect:
            The delete protect switch of nat-gateway that will be created.
        :type delete_protect: bool

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat')
        if client_token is None:
            client_token = generate_client_token()
        params = {b'clientToken': client_token}
        if billing is None:
            billing = default_billing_to_purchase_created
        body = {
            'name': compat.convert_to_string(name),
            'vpcId': compat.convert_to_string(vpc_id),
            'billing': billing.__dict__,
            'deleteProtect': delete_protect
        }
        if eips is not None:
            body['eips'] = eips
        if dnat_eips is not None:
            body['dnatEips'] = dnat_eips
        if bind_eips is not None:
            body['bindEips'] = bind_eips
        if cu_num is not None:
            body['cuNum'] = compat.convert_to_string(cu_num)
        if spec is not None:
            body['spec'] = compat.convert_to_string(spec)
        if tags is not None:
            tag_list = [tag.__dict__ for tag in tags]
            body['tags'] = tag_list
        if resource_group_id is not None:
            body['resourceGroupId'] = resource_group_id
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(vpc_id=(bytes, str))
    def list_nats(self, vpc_id=None, nat_id=None, name=None,
                  ip=None, marker=None, max_keys=None, config=None):
        """
        Return a list of nat-gateways, according to the ID,
        name or bound EIP of nat-gateways. If not specified,
        will return a full list of nat gateways in VPC.

        :param vpc_id:
            The id of VPC.
        :type vpc_id: string

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param name:
            The name of specified nat-gateway.
        :type name: string

        :param ip:
            The EIP associated with nat-gateway.
        :type ip: string

        :param marker:
            The optional parameter marker specified in the original
            request to specify where in the results to begin listing.
            Together with the marker, specifies the list result which
            listing should begin. If the marker is not specified,
            the list result will listing from the first one.
        :type marker: string

        :param max_keys:
            The optional parameter to specifies the max number of list
            result to return.
            The default value is 1000.
        :type max_keys: int

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat')
        params = {}
        if vpc_id is not None:
            params[b'vpcId'] = vpc_id
        if nat_id is not None:
            params[b'natId'] = nat_id
        if name is not None:
            params[b'name'] = name
        if ip is not None:
            params[b'ip'] = ip
        if marker is not None:
            params[b'marker'] = marker
        if max_keys is not None:
            params[b'maxKeys'] = max_keys
        return self._send_request(http_methods.GET, path,
                                  params=params, config=config)

    @required(nat_id=(bytes, str))
    def get_nat(self, nat_id, config=None):
        """
        Get the detail information of a specified nat-gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        return self._send_request(http_methods.GET, path, config=config)

    @required(nat_id=(bytes, str), name=(bytes, str))
    def update_nat(self, nat_id, name, client_token=None, config=None):
        """
        Update the name of a specified nat-gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param name:
            The new name of the nat-gateway
        :type name: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        body = {
            'name': compat.convert_to_string(name)
        }

        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), eips=list)
    def bind_eip(self, nat_id, eips, client_token=None, config=None):
        """
        Bind EIPs to a specified nat gateway.
        If a EIP is already bound to the nat gateway, unbind it first.
        If a shared_bandwidth EIP is bound to the nat gateway,
        one can bind more shared_bandwidth EIPs.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param eips:
            A public EIP or one/more EIPs in shared-bandwidth group,
            which will be bound with the nat-gateway.
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'bind': None,
            b'clientToken': client_token
        }
        body = {
            'eips': eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), eips=list)
    def unbind_eip(self, nat_id, eips, client_token=None, config=None):
        """
        Unbind EIPs of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param eips:
            EIP address list to be unbound
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'unbind': None,
            b'clientToken': client_token
        }
        body = {
            'eips': eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str))
    def delete_nat(self, nat_id, client_token=None, config=None):
        """
        Delete specified nat-gateway.
        If prepaid nat-gateway is not expired, it cannot be deleted.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        return self._send_request(http_methods.DELETE,
                                  path, params=params, config=config)

    @required(nat_id=(bytes, str))
    def purchase_reserved_nat(self, nat_id, billing, client_token=None,
                              config=None):
        """
        Renew specified nat-gateway. Postpaid NAT cannot be renewed

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param billing:
            Billing information.
        :type billing: nat_model.Billing

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'purchaseReserved': None,
            b'clientToken': client_token
        }
        if billing is None:
            billing = default_billing_to_purchase_reserved
        body = {
            'billing': billing.__dict__
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), cu_num=int)
    def resize_nat(self, nat_id, cu_num, client_token=None, config=None):
        """
        Resize a specified enhance nat-gateway.

        :param nat_id:
            The id of specified enhance nat-gateway.
        :type nat_id: string

        :param cu_num:
            The number of CU.
        :type cu_num: int

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'resize': None,
            b'clientToken': client_token
        }
        body = {
            'cuNum': compat.convert_to_string(cu_num)
        }

        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), delete_protect=bool)
    def update_delete_protect(self, nat_id, delete_protect, client_token=None, config=None):
        """
        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param delete_protect:
            Whether to enable deletion protection on the nat.
        :type delete_protect: bool

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'deleteProtect')
        params = {}
        if client_token is None:
            params[b'clientToken'] = generate_client_token()
        else:
            params[b'clientToken'] = client_token
        body = {
            "deleteProtect": delete_protect
        }

        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), eips=list)
    def bind_dnat_eip(self, nat_id, eips, client_token=None, config=None):
        """
        Bind Dnat EIPs to a specified nat gateway.
        If a EIP is already bound to nat gateway, need unbind it first.
        If a shared_bandwidth EIP is bound to the nat gateway,
        one can bind more shared_bandwidth EIPs.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param eips:
            Public EIPs or one/more EIPs in shared-bandwidth group,
            which will be bound with the nat-gateway.
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'bind': None,
            b'clientToken': client_token
        }
        body = {
            'dnatEips': eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)
    
    @required(nat_id=(bytes, str), eips=list)
    def unbind_dnat_eip(self, nat_id, eips, client_token=None, config=None):
        """
        Unbind Dnat EIPs of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param eips:
            EIP address list to be unbound
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'unbind': None,
            b'clientToken': client_token
        }
        body = {
            'dnatEips': eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), eips=list)
    def enhance_nat_bind_eip(self, nat_id, bind_eips, client_token=None, config=None):
        """
        Bind EIPs to a specified enhance nat gateway.

        :param nat_id:
            The id of specified enhance nat-gateway.
        :type nat_id: string

        :param bind_eips:
            Public EIPs or one/more EIPs in shared-bandwidth group,
            which will be bound with the nat-gateway.
        :type bind_eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'bind': None,
            b'clientToken': client_token
        }
        body = {
            'bindEips': bind_eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), eips=list)
    def enhance_nat_unbind_eip(self, nat_id, bind_eips, client_token=None, config=None):
        """
        Unbind EIPs of a specified enhance nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param bind_eips:
            EIP address list to be unbound
        :type bind_eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'unbind': None,
            b'clientToken': client_token
        }
        body = {
            'bindEips': bind_eips
        }
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str),
              rule_name=(bytes, str),
              source_cidr=(bytes, str),
              public_ip_address=list)
    def create_snat_rule(self, nat_id, rule_name, source_cidr, public_ip_address, client_token=None, config=None):
        """
        create snat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param rule_name:
            The name of snat rule.
        :type rule_name: string

        :param source_cidr:
            The source cidr of this snat rule.
        :type source_cidr: string

        :param public_ip_address:
            EIP address list to be bound
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'snatRule')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        body = {
            'ruleName': compat.convert_to_string(rule_name),
            'publicIpsAddress': public_ip_address,
            'sourceCIDR': compat.convert_to_string(source_cidr),
        }
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), snat_rules=list)
    def batch_create_snat_rule(self, nat_id, snat_rules, client_token=None, config=None):
        """
        batch create snat rules of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param snat_rules:
            Snat rules, every rule contains ruleName, sourceCIDR and publicIpsAddress.
        :type snat_rules: list<dict>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', 'snatRule', 'batchCreate')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        body = {
            "natId": compat.convert_to_string(nat_id),
            "snatRules": snat_rules
        }
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)
    
    @required(nat_id=(bytes, str), snat_rule_id=(bytes, str))
    def delete_snat_rule(self, nat_id, snat_rule_id, client_token=None, config=None):
        """
        delete snat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param snat_rule_id:
            The id of specified snat rule.
        :type snat_rule_id: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'snatRule', snat_rule_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        
        return self._send_request(http_methods.DELETE,
                                  path, params=params, config=config)
    
    @required(nat_id=(bytes, str), snat_rule_id=(bytes, str))
    def update_snat_rule(self, nat_id, snat_rule_id, rule_name=None, source_cidr=None,
                         public_ip_address=None, client_token=None, config=None):
        """
        update snat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param snat_rule_id:
            The id of specified snat rule.
        :type snat_rule_id: string

        :param rule_name:
            The name of snat rule.
        :type rule_name: string

        :param source_cidr:
            The source cidr of this snat rule.
        :type source_cidr: string

        :param public_ip_address:
            EIP address list to be update.
        :type eips: list<String>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'snatRule', snat_rule_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }

        body = {}
        if rule_name is not None:
            body['ruleName'] = compat.convert_to_string(rule_name)
        if public_ip_address is not None:
            body['publicIpsAddress'] = public_ip_address
        if source_cidr is not None:
            body['sourceCIDR'] = compat.convert_to_string(source_cidr)
        return self._send_request(http_methods.PUT,
                                  path, body=json.dumps(body),
                                  params=params, config=config)
        
    @required(nat_id=(bytes, str))
    def list_snat_rule(self, nat_id, marker=None, maxKeys=None, client_token=None, config=None):
        """
        list snat rules of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param marker:
            The optional parameter marker specified in the original
            request to specify where in the results to begin listing.
            Together with the marker, specifies the list result which
            listing should begin. If the marker is not specified,
            the list result will listing from the first one.
        :type marker: string

        :param max_keys:
            The optional parameter to specifies the max number of list
            result to return.
            The default value is 1000.
        :type max_keys: int
    
        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'snatRule')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        if marker is not None:
            params[b'marker'] = marker
        if maxKeys is not None:
            params[b'maxKeys'] = maxKeys
        
        return self._send_request(http_methods.GET,
                                  path, params=params, config=config)
    
    @required(nat_id=(bytes, str),
              public_ip_address=(bytes, str),
              private_ip_address=(bytes, str),
              protocol=(bytes, str))
    def create_dnat_rule(self, nat_id, public_ip_address, private_ip_address, protocol, rule_name=None, 
                         public_port=None, private_port=None, client_token=None, config=None):
        """
        create dnat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param rule_name:
            The name of this dnat rule.
        :type rule_name: string

        :param public_ip_address:
            The public ip address of this dnat rule.
        :type public_ip_address: string

        :param private_ip_address:
            The private ip address of this dnat rule.
        :type private_ip_address: string

        :param protocol:
            protocol, support TCP、UDP、all
        :type protocol: string

        :param public_port:
            public port
        :type public_port: string

        :param private_port:
            private port
        :type private_port: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'dnatRule')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        body = {
            'ruleName': compat.convert_to_string(rule_name),
            'publicIpAddress': compat.convert_to_string(public_ip_address),
            'privateIpAddress': compat.convert_to_string(private_ip_address),
            'protocol': compat.convert_to_string(protocol),
        }
        if public_port is not None:
            body['publicPort'] = compat.convert_to_string(public_port)
        if private_port is not None:
            body['privatePort'] = compat.convert_to_string(private_port)
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)

    @required(nat_id=(bytes, str), dnat_rules=list)
    def batch_create_dnat_rule(self, nat_id, dnat_rules, client_token=None, config=None):
        """
        batch create dnat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param dnat_rules:
            Dnat rules, every rule contains ruleName, publicIpAddress, privateIpAddress, protocol, privatePort, publicPort.
        :type snat_rules: list<dict>

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'dnatRule', 'batchCreate')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        body = {
            "rules": dnat_rules
        }
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)
    
    @required(nat_id=(bytes, str), snat_rule_id=(bytes, str))
    def delete_dnat_rule(self, nat_id, dnat_rule_id, client_token=None, config=None):
        """
        delete dnat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param dnat_rule_id:
            The id of specified snat rule.
        :type snat_rule_id: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'dnatRule', dnat_rule_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        
        return self._send_request(http_methods.DELETE,
                                  path, params=params, config=config)
    
    @required(nat_id=(bytes, str), rule_id=(bytes, str))
    def update_dnat_rule(self, nat_id, dnat_rule_id, 
                         public_ip_address=None, private_ip_address=None,
                         rule_name=None, protocol=None, public_port=None, 
                         private_port=None, client_token=None, config=None):
        """
        update dnat rule of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param rule_id:
            The id of specified dnat rule.
        :type rule_id: string

        :param rule_name:
            The name of dnat rule.
        :type rule_name: string

        :param public_ip_address:
            The public ip address of this dnat rule.
        :type public_ip_address: string

        :param private_ip_address:
            The private ip address of this dnat rule.
        :type private_ip_address: string

        :param protocol:
            protocol
        :type protocol: string

        :param public_port:
            public port
        :type public_port: string

        :param private_port:
            private port
        :type private_port: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'dnatRule', dnat_rule_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }

        body = {}
        if rule_name is not None:
            body[b'ruleName'] = compat.convert_to_string(rule_name)
        if protocol is not None:
            body[b'protocol'] = compat.convert_to_string(protocol)
        if public_ip_address is not None:
            body[b'publicIpAddress'] = compat.convert_to_string(public_ip_address)
        if private_ip_address is not None:
            body[b'privateIpAddress'] = compat.convert_to_string(private_ip_address)
        if public_port is not None:
            body[b'publicPort'] = compat.convert_to_string(public_port)
        if private_port is not None:
            body[b'privatePort'] = compat.convert_to_string(private_port)
        
        return self._send_request(http_methods.POST,
                                  path, body=json.dumps(body),
                                  params=params, config=config)
        
    @required(nat_id=(bytes, str))
    def list_dnat_rule(self, nat_id, marker=None, maxKeys=None, client_token=None, config=None):
        """
        list dnat rules of a specified nat gateway.

        :param nat_id:
            The id of specified nat-gateway.
        :type nat_id: string

        :param marker:
            The optional parameter marker specified in the original
            request to specify where in the results to begin listing.
            Together with the marker, specifies the list result which
            listing should begin. If the marker is not specified,
            the list result will listing from the first one.
        :type marker: string

        :param max_keys:
            The optional parameter to specifies the max number of list
            result to return.
            The default value is 1000.
        :type max_keys: int
    
        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by user,
            a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = utils.append_uri(self.version, 'nat', nat_id, 'dnatRule')
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        if marker is not None:
            params[b'marker'] = marker
        if maxKeys is not None:
            params[b'maxKeys'] = maxKeys
        
        return self._send_request(http_methods.GET,
                                  path, params=params, config=config)
def generate_client_token_by_uuid():
    """
    The default method to generate the random string for client_token
    if the optional parameter client_token is not specified by the user.

    :return:
    :rtype string
    """
    return str(uuid.uuid4())

generate_client_token = generate_client_token_by_uuid
