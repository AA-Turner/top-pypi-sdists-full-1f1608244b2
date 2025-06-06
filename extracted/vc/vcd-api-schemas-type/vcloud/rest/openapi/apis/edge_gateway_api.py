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


class EdgeGatewayApi(object):
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

    def delete_edge_gateway(self, gateway_id, **kwargs):
        """
        Deletes a specific Edge Gateway
        Deletes a specific Edge Gateway. Only NSX-T Edge Gateways can be deleted with this endpoint. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_edge_gateway(gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str gateway_id: (required)
        :param bool force: Value \"true\" means to forcefully delete the object that contains other objects even if those objects are in a state that does not allow removal. The default is \"false\"; therefore, objects are not removed if they are not in a state that normally allows removal. Force also implies recursive delete where other contained objects are removed. Errors may be ignored. Invalid value (not true or false) are ignored. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_edge_gateway_with_http_info(gateway_id, **kwargs)
        else:
            (data) = self.delete_edge_gateway_with_http_info(gateway_id, **kwargs)
            return data

    def delete_edge_gateway_with_http_info(self, gateway_id, **kwargs):
        """
        Deletes a specific Edge Gateway
        Deletes a specific Edge Gateway. Only NSX-T Edge Gateways can be deleted with this endpoint. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_edge_gateway_with_http_info(gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str gateway_id: (required)
        :param bool force: Value \"true\" means to forcefully delete the object that contains other objects even if those objects are in a state that does not allow removal. The default is \"false\"; therefore, objects are not removed if they are not in a state that normally allows removal. Force also implies recursive delete where other contained objects are removed. Errors may be ignored. Invalid value (not true or false) are ignored. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id', 'force']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_edge_gateway" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params) or (params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `delete_edge_gateway`")


        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gatewayId'] = params['gateway_id']

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/edgeGateways/{gatewayId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_edge_gateway(self, gateway_id, **kwargs):
        """
        Retrieves a specific Edge Gateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_edge_gateway(gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str gateway_id: (required)
        :return: EdgeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_edge_gateway_with_http_info(gateway_id, **kwargs)
        else:
            (data) = self.get_edge_gateway_with_http_info(gateway_id, **kwargs)
            return data

    def get_edge_gateway_with_http_info(self, gateway_id, **kwargs):
        """
        Retrieves a specific Edge Gateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_edge_gateway_with_http_info(gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str gateway_id: (required)
        :return: EdgeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edge_gateway" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params) or (params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `get_edge_gateway`")


        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gatewayId'] = params['gateway_id']

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

        return self.api_client.call_api('/1.0.0/edgeGateways/{gatewayId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EdgeGateway',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_used_ip_addresses(self, page, page_size, gateway_id, **kwargs):
        """
        Retrieve the list of IP addresses which are being used by the edge gateway.
        Get all the IP Addresses which are being used by the Edge Gateway such as the primary IP or an IP used by a given Edge Service, such as NAT. These IP addresses are a subset of the IPs allocated from the connected external networks. If the IP is  being consumed by any of the configured services on the edge gateway then name of service will be returned. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_used_ip_addresses(page, page_size, gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to fetch, zero offset. (required)
        :param int page_size: Results per page to fetch. (required)
        :param str gateway_id: (required)
        :param str filter: Filter for a query.  FIQL format.
        :param str sort_asc: Field to use for ascending sort
        :param str sort_desc: Field to use for descending sort
        :return: GatewayUsedIpAddresses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_used_ip_addresses_with_http_info(page, page_size, gateway_id, **kwargs)
        else:
            (data) = self.get_used_ip_addresses_with_http_info(page, page_size, gateway_id, **kwargs)
            return data

    def get_used_ip_addresses_with_http_info(self, page, page_size, gateway_id, **kwargs):
        """
        Retrieve the list of IP addresses which are being used by the edge gateway.
        Get all the IP Addresses which are being used by the Edge Gateway such as the primary IP or an IP used by a given Edge Service, such as NAT. These IP addresses are a subset of the IPs allocated from the connected external networks. If the IP is  being consumed by any of the configured services on the edge gateway then name of service will be returned. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_used_ip_addresses_with_http_info(page, page_size, gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to fetch, zero offset. (required)
        :param int page_size: Results per page to fetch. (required)
        :param str gateway_id: (required)
        :param str filter: Filter for a query.  FIQL format.
        :param str sort_asc: Field to use for ascending sort
        :param str sort_desc: Field to use for descending sort
        :return: GatewayUsedIpAddresses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'gateway_id', 'filter', 'sort_asc', 'sort_desc']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_used_ip_addresses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if ('page' not in params) or (params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_used_ip_addresses`")
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params) or (params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_used_ip_addresses`")
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params) or (params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `get_used_ip_addresses`")

        if 'page' in params and params['page'] < 1:
            raise ValueError("Invalid value for parameter `page` when calling `get_used_ip_addresses`, must be a value greater than or equal to `1`")
        if 'page_size' in params and params['page_size'] > 128:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_used_ip_addresses`, must be a value less than or equal to `128`")
        if 'page_size' in params and params['page_size'] < 0:
            raise ValueError("Invalid value for parameter `page_size` when calling `get_used_ip_addresses`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gatewayId'] = params['gateway_id']

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'sort_asc' in params:
            query_params.append(('sortAsc', params['sort_asc']))
        if 'sort_desc' in params:
            query_params.append(('sortDesc', params['sort_desc']))
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/edgeGateways/{gatewayId}/usedIpAddresses', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GatewayUsedIpAddresses',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_edge_gateway(self, gateway, gateway_id, **kwargs):
        """
        Updates a specific Edge Gateway
        Update a specific Edge Gateway. Only NSX-T Edge Gateways can be created with this endpoint. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_edge_gateway(gateway, gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EdgeGateway gateway: (required)
        :param str gateway_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_edge_gateway_with_http_info(gateway, gateway_id, **kwargs)
        else:
            (data) = self.update_edge_gateway_with_http_info(gateway, gateway_id, **kwargs)
            return data

    def update_edge_gateway_with_http_info(self, gateway, gateway_id, **kwargs):
        """
        Updates a specific Edge Gateway
        Update a specific Edge Gateway. Only NSX-T Edge Gateways can be created with this endpoint. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_edge_gateway_with_http_info(gateway, gateway_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EdgeGateway gateway: (required)
        :param str gateway_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway', 'gateway_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_edge_gateway" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway' is set
        if ('gateway' not in params) or (params['gateway'] is None):
            raise ValueError("Missing the required parameter `gateway` when calling `update_edge_gateway`")
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params) or (params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `update_edge_gateway`")


        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gatewayId'] = params['gateway_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gateway' in params:
            body_params = params['gateway']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/1.0.0/edgeGateways/{gatewayId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
