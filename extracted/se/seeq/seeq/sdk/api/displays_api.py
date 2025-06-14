# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.26.0-v202506111109-CD
    
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

class DisplaysApi(object):
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

    def archive_display(self, **kwargs):
        """
        Archive a display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_display(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the display item to archive. (required)
        :return: ArchiveOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ArchiveOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.archive_display_with_http_info(**kwargs)
        else:
            (data) = self.archive_display_with_http_info(**kwargs)
            return data

    def archive_display_with_http_info(self, **kwargs):
        """
        Archive a display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_display_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the display item to archive. (required)
        :return: ArchiveOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ArchiveOutputV1
        """

        all_params = ['id']
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
                    " to method archive_display" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `archive_display`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/displays/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ArchiveOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_display(self, **kwargs):
        """
        Create a new display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_display(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DisplayInputV1 body: (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_display_with_http_info(**kwargs)
        else:
            (data) = self.create_display_with_http_info(**kwargs)
            return data

    def create_display_with_http_info(self, **kwargs):
        """
        Create a new display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_display_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DisplayInputV1 body: (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
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
                    " to method create_display" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_display`")


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

        return self.api_client.call_api('/displays', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DisplayOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_display(self, **kwargs):
        """
        Get a display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_display(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID for the display (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_display_with_http_info(**kwargs)
        else:
            (data) = self.get_display_with_http_info(**kwargs)
            return data

    def get_display_with_http_info(self, **kwargs):
        """
        Get a display item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_display_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID for the display (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
        """

        all_params = ['id']
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
                    " to method get_display" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_display`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/displays/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DisplayOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_displays(self, **kwargs):
        """
        Get a list of display items
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_displays(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: The pagination offset, the index of the first display item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of display items that will be returned in this page of results
        :return: DisplayOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputListV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_displays_with_http_info(**kwargs)
        else:
            (data) = self.get_displays_with_http_info(**kwargs)
            return data

    def get_displays_with_http_info(self, **kwargs):
        """
        Get a list of display items
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_displays_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: The pagination offset, the index of the first display item that will be returned in this page of results
        :param int limit: The pagination limit, the total number of display items that will be returned in this page of results
        :return: DisplayOutputListV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputListV1
        """

        all_params = ['offset', 'limit']
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
                    " to method get_displays" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

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

        return self.api_client.call_api('/displays', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DisplayOutputListV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_display(self, **kwargs):
        """
        Update a display
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_display(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DisplayInputV1 body: (required)
        :param str id: The Seeq ID for the display (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_display_with_http_info(**kwargs)
        else:
            (data) = self.update_display_with_http_info(**kwargs)
            return data

    def update_display_with_http_info(self, **kwargs):
        """
        Update a display
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_display_with_http_info(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DisplayInputV1 body: (required)
        :param str id: The Seeq ID for the display (required)
        :return: DisplayOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisplayOutputV1
        """

        all_params = ['body', 'id']
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
                    " to method update_display" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_display`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_display`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/displays/{id}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'DisplayOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
