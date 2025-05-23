# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
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

class LogsApi(object):
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

    def download_logs(self, **kwargs):
        """
        Download the log files in zipped form.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_logs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str download_logs_cookie: The value to return as a cookie.
        :return: bytes
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytes
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.download_logs_with_http_info(**kwargs)
        else:
            (data) = self.download_logs_with_http_info(**kwargs)
            return data

    def download_logs_with_http_info(self, **kwargs):
        """
        Download the log files in zipped form.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_logs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str download_logs_cookie: The value to return as a cookie.
        :return: bytes
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytes
        """

        all_params = ['download_logs_cookie']
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
                    " to method download_logs" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'download_logs_cookie' in params:
            query_params.append(('downloadLogsCookie', params['download_logs_cookie']))

        header_params = {}

        for key, value in params.get('_custom_headers', {}).items():
            header_params[key] = value


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.seeq.v1+json', 'application/zip'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/logs/download', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'bytes'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_available_log_files(self, **kwargs):
        """
        Get a list of available log files.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_log_files(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[str]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_log_files_with_http_info(**kwargs)
        else:
            (data) = self.get_available_log_files_with_http_info(**kwargs)
            return data

    def get_available_log_files_with_http_info(self, **kwargs):
        """
        Get a list of available log files.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_log_files_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[str]
        """

        all_params = []
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
                    " to method get_available_log_files" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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

        return self.api_client.call_api('/logs', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'list[str]'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_logs(self, **kwargs):
        """
        Get a collection of log messages
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_logs(log=log_value, start_time=start_time_value, limit=limit_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str log: ID of the log to retrieve (required)
        :param str start_time: Starting time to filter log messages on. (required)
        :param str end_time: Ending time to filter log messages on. It will default to the current time if none is specified.
        :param int limit: The (soft) limit for the number of log messages to return. (required)
        :param str sorted: Whether log messages should be sorted in ascending order, 'ASC', by their time or descending order, 'DESC'.
        :param str level: The minimum log level to include.
        :param str source_contains: A substring that the source field of the log messages must contain to be returned.
        :param str message_contains: A substring that the message field of the log messages must contain to be returned.
        :return: list[LogMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[LogMessage]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_logs_with_http_info(**kwargs)
        else:
            (data) = self.get_logs_with_http_info(**kwargs)
            return data

    def get_logs_with_http_info(self, **kwargs):
        """
        Get a collection of log messages
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_logs_with_http_info(log=log_value, start_time=start_time_value, limit=limit_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str log: ID of the log to retrieve (required)
        :param str start_time: Starting time to filter log messages on. (required)
        :param str end_time: Ending time to filter log messages on. It will default to the current time if none is specified.
        :param int limit: The (soft) limit for the number of log messages to return. (required)
        :param str sorted: Whether log messages should be sorted in ascending order, 'ASC', by their time or descending order, 'DESC'.
        :param str level: The minimum log level to include.
        :param str source_contains: A substring that the source field of the log messages must contain to be returned.
        :param str message_contains: A substring that the message field of the log messages must contain to be returned.
        :return: list[LogMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[LogMessage]
        """

        all_params = ['log', 'start_time', 'end_time', 'limit', 'sorted', 'level', 'source_contains', 'message_contains']
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
                    " to method get_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'log' is set
        if ('log' not in params) or (params['log'] is None):
            raise ValueError("Missing the required parameter `log` when calling `get_logs`")
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_logs`")
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_logs`")


        collection_formats = {}

        path_params = {}
        if 'log' in params:
            path_params['log'] = params['log']

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'sorted' in params:
            query_params.append(('sorted', params['sorted']))
        if 'level' in params:
            query_params.append(('level', params['level']))
        if 'source_contains' in params:
            query_params.append(('sourceContains', params['source_contains']))
        if 'message_contains' in params:
            query_params.append(('messageContains', params['message_contains']))

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

        return self.api_client.call_api('/logs/{log}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'list[LogMessage]'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def send(self, **kwargs):
        """
        Send a support request along with the log files to Seeq.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SupportRequestInputV1 body: Support request information (required)
        :return: SupportRequestOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SupportRequestOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_with_http_info(**kwargs)
        else:
            (data) = self.send_with_http_info(**kwargs)
            return data

    def send_with_http_info(self, **kwargs):
        """
        Send a support request along with the log files to Seeq.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SupportRequestInputV1 body: Support request information (required)
        :return: SupportRequestOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SupportRequestOutputV1
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
                    " to method send" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send`")


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

        return self.api_client.call_api('/logs/send', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'SupportRequestOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
