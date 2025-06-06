# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.25.0-v202506042330-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import sys
import os
import re

from deprecated import deprecated
# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from ..models import *

class AuditApi(object):
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

    def create_version_history(self, **kwargs):
        """
        Version a Locked item and create a new Version History.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_version_history(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VersionInputV1 body: Input object containing id of item to version and notes (optional) (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_version_history_with_http_info(**kwargs)
        else:
            (data) = self.create_version_history_with_http_info(**kwargs)
            return data

    def create_version_history_with_http_info(self, **kwargs):
        """
        Version a Locked item and create a new Version History.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_version_history_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VersionInputV1 body: Input object containing id of item to version and notes (optional) (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')
        all_params.append('_custom_headers')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_version_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_version_history`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/audit/version', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'VersionHistoryOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_audit_entries(self, **kwargs):
        """
        Get a collection of Audit Trail entries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entries(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str start_time: The start time for the query, formatted as an ISO 8601 timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)
        :param str end_time: The end time for the query, formatted as an ISO 8601 timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)
        :param list[str] user_id: User ID(s) to filter on
        :param list[str] item_id: Item ID(s) to filter on
        :param list[str] item_type: Item type(s) to filter on
        :param list[str] change_type: Change type(s) to filter on (Create, Update, Delete)
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :param bool sort_asc: When true sorts by oldest entries first, when false sorts by newest entries first
        :param bool hide_system_entries: When true, entries created by system managed users will be hidden from the results
        :return: AuditOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuditOutputListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_entries_with_http_info(**kwargs)
        else:
            (data) = self.get_audit_entries_with_http_info(**kwargs)
            return data

    def get_audit_entries_with_http_info(self, **kwargs):
        """
        Get a collection of Audit Trail entries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entries_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str start_time: The start time for the query, formatted as an ISO 8601 timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)
        :param str end_time: The end time for the query, formatted as an ISO 8601 timestamp (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)
        :param list[str] user_id: User ID(s) to filter on
        :param list[str] item_id: Item ID(s) to filter on
        :param list[str] item_type: Item type(s) to filter on
        :param list[str] change_type: Change type(s) to filter on (Create, Update, Delete)
        :param int offset: The pagination offset, the index of the first collection item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of collection items that will be returned in this page of results
        :param bool sort_asc: When true sorts by oldest entries first, when false sorts by newest entries first
        :param bool hide_system_entries: When true, entries created by system managed users will be hidden from the results
        :return: AuditOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuditOutputListV1
        """

        all_params = ['start_time', 'end_time', 'user_id', 'item_id', 'item_type', 'change_type', 'offset', 'limit', 'sort_asc', 'hide_system_entries']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')
        all_params.append('_custom_headers')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_entries" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'user_id' in params:
            query_params.append(('userID', params['user_id']))
            collection_formats['userID'] = 'multi'
        if 'item_id' in params:
            query_params.append(('itemID', params['item_id']))
            collection_formats['itemID'] = 'multi'
        if 'item_type' in params:
            query_params.append(('itemType', params['item_type']))
            collection_formats['itemType'] = 'multi'
        if 'change_type' in params:
            query_params.append(('changeType', params['change_type']))
            collection_formats['changeType'] = 'multi'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'sort_asc' in params:
            query_params.append(('sortAsc', params['sort_asc']))
        if 'hide_system_entries' in params:
            query_params.append(('hideSystemEntries', params['hide_system_entries']))

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/audit', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'AuditOutputListV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_version_histories(self, **kwargs):
        """
        Get all the Version Histories this user has access to, or get all the Version Histories pertaining to an item that was created by cloning a versioned item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_histories(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str duplicate_item_id: The ID of a duplicate that was created by cloning a versioned item. If no ID is provided, all Version Histories will be returned.
        :return: VersionHistoryOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_version_histories_with_http_info(**kwargs)
        else:
            (data) = self.get_version_histories_with_http_info(**kwargs)
            return data

    def get_version_histories_with_http_info(self, **kwargs):
        """
        Get all the Version Histories this user has access to, or get all the Version Histories pertaining to an item that was created by cloning a versioned item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_histories_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str duplicate_item_id: The ID of a duplicate that was created by cloning a versioned item. If no ID is provided, all Version Histories will be returned.
        :return: VersionHistoryOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputListV1
        """

        all_params = ['duplicate_item_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')
        all_params.append('_custom_headers')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_histories" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'duplicate_item_id' in params:
            query_params.append(('duplicateItemId', params['duplicate_item_id']))

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/audit/version-histories', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'VersionHistoryOutputListV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_version_history(self, **kwargs):
        """
        Get a specific Version History that this user has access to
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_history(version_history_id=version_history_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version_history_id: (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_version_history_with_http_info(**kwargs)
        else:
            (data) = self.get_version_history_with_http_info(**kwargs)
            return data

    def get_version_history_with_http_info(self, **kwargs):
        """
        Get a specific Version History that this user has access to
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_history_with_http_info(version_history_id=version_history_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version_history_id: (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """

        all_params = ['version_history_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')
        all_params.append('_custom_headers')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_history_id' is set
        if ('version_history_id' not in params) or (params['version_history_id'] is None):
            raise ValueError("Missing the required parameter `version_history_id` when calling `get_version_history`")


        collection_formats = {}

        path_params = {}
        if 'version_history_id' in params:
            path_params['versionHistoryId'] = params['version_history_id']

        query_params = []

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/audit/version-history/{versionHistoryId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'VersionHistoryOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_version_history(self, **kwargs):
        """
        Version a Locked item and add it to an existing Version History.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_version_history(body=body_value, version_history_id=version_history_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VersionInputV1 body: Input object containing id of item to version and notes (required)
        :param str version_history_id: ID of the Version History to add this Version to. (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_version_history_with_http_info(**kwargs)
        else:
            (data) = self.update_version_history_with_http_info(**kwargs)
            return data

    def update_version_history_with_http_info(self, **kwargs):
        """
        Version a Locked item and add it to an existing Version History.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_version_history_with_http_info(body=body_value, version_history_id=version_history_id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VersionInputV1 body: Input object containing id of item to version and notes (required)
        :param str version_history_id: ID of the Version History to add this Version to. (required)
        :return: VersionHistoryOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VersionHistoryOutputV1
        """

        all_params = ['body', 'version_history_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_response_type')
        all_params.append('_custom_headers')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_version_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_version_history`")
        # verify the required parameter 'version_history_id' is set
        if ('version_history_id' not in params) or (params['version_history_id'] is None):
            raise ValueError("Missing the required parameter `version_history_id` when calling `update_version_history`")


        collection_formats = {}

        path_params = {}
        if 'version_history_id' in params:
            path_params['versionHistoryId'] = params['version_history_id']

        query_params = []

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/audit/version/{versionHistoryId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'VersionHistoryOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
