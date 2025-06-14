# coding: utf-8

"""
    VMware Cloud Director OpenAPI

    VMware Cloud Director OpenAPI is a new API that is defined using the OpenAPI standards.<br/> This ReSTful API borrows some elements of the legacy VMware Cloud Director API and establishes new patterns for use as described below. <h4>Authentication</h4> Authentication and Authorization schemes are the same as those for the legacy APIs. You can authenticate using the JWT token via the <code>Authorization</code> header or specifying a session using <code>x-vcloud-authorization</code> (The latter form is deprecated). <h4>Operation Patterns</h4> This API follows the following general guidelines to establish a consistent CRUD pattern: <table> <tr>   <th>Operation</th><th>Description</th><th>Response Code</th><th>Response Content</th> </tr><tr>   <td>GET /items<td>Returns a paginated list of items<td>200<td>Response will include Navigational links to the items in the list. </tr><tr>   <td>POST /items<td>Returns newly created item<td>201<td>Content-Location header links to the newly created item </tr><tr>   <td>GET /items/urn<td>Returns an individual item<td>200<td>A single item using same data type as that included in list above </tr><tr>   <td>PUT /items/urn<td>Updates an individual item<td>200<td>Updated view of the item is returned </tr><tr>   <td>DELETE /items/urn<td>Deletes the item<td>204<td>No content is returned. </tr> </table> <h5>Asynchronous operations</h5> Asynchronous operations are determined by the server. In those cases, instead of responding as described above, the server responds with an HTTP Response code 202 and an empty body. The tracking task (which is the same task as all legacy API operations use) is linked via the URI provided in the <code>Location</code> header.<br/> All API calls can choose to service a request asynchronously or synchronously as determined by the server upon interpreting the request. Operations that choose to exhibit this dual behavior will have both options documented by specifying both response code(s) below. The caller must be prepared to handle responses to such API calls by inspecting the HTTP Response code. <h5>Error Conditions</h5> <b>All</b> operations report errors using the following error reporting rules: <ul>   <li>400: Bad Request - In event of bad request due to incorrect data or other user error</li>   <li>401: Bad Request - If user is unauthenticated or their session has expired</li>   <li>403: Forbidden - If the user is not authorized or the entity does not exist</li> </ul> <h4>OpenAPI Design Concepts and Principles</h4> <ul>   <li>IDs are full Uniform Resource Names (URNs).</li>   <li>OpenAPI's <code>Content-Type</code> is always <code>application/json</code></li>   <li>REST links are in the Link header.</li>   <ul>     <li>Multiple relationships for any link are represented by multiple values in a space-separated list.</li>     <li>Links have a custom VMware Cloud Director-specific &quot;model&quot; attribute that hints at the applicable data         type for the links.</li>     <li>title + rel + model attributes evaluates to a unique link.</li>     <li>Links follow Hypermedia as the Engine of Application State (HATEOAS) principles. Links are present if         certain operations are present and permitted for the user&quot;s current role and the state of the         referred entities.</li>   </ul>   <li>APIs follow a flat structure relying on cross-referencing other entities instead of the navigational style       used by the legacy VMware Cloud Director APIs.</li>   <li>Most endpoints that return a list support filtering and sorting similar to the query service in the legacy       VMware Cloud Director APIs.</li>   <li>Accept header must be included to specify the API version for the request similar to calls to existing legacy       VMware Cloud Director APIs.</li>   <li>Each feature has a version in the path element present in its URL.<br/>       <b>Note</b> API URL's without a version in their paths must be considered experimental.</li> </ul> 

    OpenAPI spec version: 36.0
    Contact: https://code.vmware.com/support
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CapabilitiesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_org_vdc_storage_policy_capabilities(self, id, **kwargs):
        """
        Retrieves capabilities of a specific organization VDC storage policy.
        Retrieves the current capabilities configured on a specific organization VDC storage policy. These cannot be edited. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_org_vdc_storage_policy_capabilities(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_org_vdc_storage_policy_capabilities_with_http_info(id, **kwargs)
        else:
            (data) = self.get_org_vdc_storage_policy_capabilities_with_http_info(id, **kwargs)
            return data

    def get_org_vdc_storage_policy_capabilities_with_http_info(self, id, **kwargs):
        """
        Retrieves capabilities of a specific organization VDC storage policy.
        Retrieves the current capabilities configured on a specific organization VDC storage policy. These cannot be edited. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_org_vdc_storage_policy_capabilities_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_org_vdc_storage_policy_capabilities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_org_vdc_storage_policy_capabilities`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/orgVdcStoragePolicies/{id}/capabilities', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Capabilities',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_pvdc_storage_policy_capabilities(self, id, **kwargs):
        """
        Retrieves capabilities of a specific provider VDC storage policy.
        Retrieves the current capabilities configured on a specific provider VDC storage policy. These cannot be edited. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pvdc_storage_policy_capabilities(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pvdc_storage_policy_capabilities_with_http_info(id, **kwargs)
        else:
            (data) = self.get_pvdc_storage_policy_capabilities_with_http_info(id, **kwargs)
            return data

    def get_pvdc_storage_policy_capabilities_with_http_info(self, id, **kwargs):
        """
        Retrieves capabilities of a specific provider VDC storage policy.
        Retrieves the current capabilities configured on a specific provider VDC storage policy. These cannot be edited. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pvdc_storage_policy_capabilities_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pvdc_storage_policy_capabilities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_pvdc_storage_policy_capabilities`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/pvdcStoragePolicies/{id}/capabilities', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Capabilities',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_quota_policy_capabilities(self, **kwargs):
        """
        Retrieves capabilities for quotaPolicy feature.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_quota_policy_capabilities(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_quota_policy_capabilities_with_http_info(**kwargs)
        else:
            (data) = self.get_quota_policy_capabilities_with_http_info(**kwargs)
            return data

    def get_quota_policy_capabilities_with_http_info(self, **kwargs):
        """
        Retrieves capabilities for quotaPolicy feature.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_quota_policy_capabilities_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota_policy_capabilities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/quotaPolicy/capabilities', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Capabilities',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_vdc_capabilities(self, org_vdc_id, **kwargs):
        """
        Retrieves capabilities for the given Organization vDC.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vdc_capabilities(org_vdc_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_vdc_id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_vdc_capabilities_with_http_info(org_vdc_id, **kwargs)
        else:
            (data) = self.get_vdc_capabilities_with_http_info(org_vdc_id, **kwargs)
            return data

    def get_vdc_capabilities_with_http_info(self, org_vdc_id, **kwargs):
        """
        Retrieves capabilities for the given Organization vDC.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vdc_capabilities_with_http_info(org_vdc_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_vdc_id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_vdc_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vdc_capabilities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_vdc_id' is set
        if ('org_vdc_id' not in params) or (params['org_vdc_id'] is None):
            raise ValueError("Missing the required parameter `org_vdc_id` when calling `get_vdc_capabilities`")


        collection_formats = {}

        path_params = {}
        if 'org_vdc_id' in params:
            path_params['orgVdcId'] = params['org_vdc_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/vdcs/{orgVdcId}/capabilities', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Capabilities',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_vdc_group_capabilities(self, vdc_group_id, **kwargs):
        """
        Retrieves the supported capabilities of the specified vDC Group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vdc_group_capabilities(vdc_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str vdc_group_id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_vdc_group_capabilities_with_http_info(vdc_group_id, **kwargs)
        else:
            (data) = self.get_vdc_group_capabilities_with_http_info(vdc_group_id, **kwargs)
            return data

    def get_vdc_group_capabilities_with_http_info(self, vdc_group_id, **kwargs):
        """
        Retrieves the supported capabilities of the specified vDC Group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vdc_group_capabilities_with_http_info(vdc_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str vdc_group_id: (required)
        :return: Capabilities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vdc_group_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vdc_group_capabilities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vdc_group_id' is set
        if ('vdc_group_id' not in params) or (params['vdc_group_id'] is None):
            raise ValueError("Missing the required parameter `vdc_group_id` when calling `get_vdc_group_capabilities`")


        collection_formats = {}

        path_params = {}
        if 'vdc_group_id' in params:
            path_params['vdcGroupId'] = params['vdc_group_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/vdcGroups/{vdcGroupId}/capabilities', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Capabilities',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
