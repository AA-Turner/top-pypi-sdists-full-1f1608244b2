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

class NotificationConfigurationsApi(object):
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

    def delete_notification_configuration(self, **kwargs):
        """
        Delete a notification configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_notification_configuration(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID of the notifiable item (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_notification_configuration_with_http_info(**kwargs)
        else:
            (data) = self.delete_notification_configuration_with_http_info(**kwargs)
            return data

    def delete_notification_configuration_with_http_info(self, **kwargs):
        """
        Delete a notification configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_notification_configuration_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID of the notifiable item (required)
        :return: StatusMessageBase
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StatusMessageBase
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
                    " to method delete_notification_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_notification_configuration`")


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

        return self.api_client.call_api('/notification-configurations/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'StatusMessageBase'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_notification_configuration(self, **kwargs):
        """
        Get a notification configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notification_configuration(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID of the notifiable item (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_notification_configuration_with_http_info(**kwargs)
        else:
            (data) = self.get_notification_configuration_with_http_info(**kwargs)
            return data

    def get_notification_configuration_with_http_info(self, **kwargs):
        """
        Get a notification configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notification_configuration_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID of the notifiable item (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
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
                    " to method get_notification_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification_configuration`")


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

        return self.api_client.call_api('/notification-configurations/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'NotificationConfigurationOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_notification_configuration_for_condition_monitor(self, **kwargs):
        """
        Create or update a notification configuration on a condition monitor
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_notification_configuration_for_condition_monitor(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConditionMonitorNotificationConfigurationInputV1 body: (required)
        :param str id: The Seeq ID of the condition monitor (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_notification_configuration_for_condition_monitor_with_http_info(**kwargs)
        else:
            (data) = self.set_notification_configuration_for_condition_monitor_with_http_info(**kwargs)
            return data

    def set_notification_configuration_for_condition_monitor_with_http_info(self, **kwargs):
        """
        Create or update a notification configuration on a condition monitor
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_notification_configuration_for_condition_monitor_with_http_info(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConditionMonitorNotificationConfigurationInputV1 body: (required)
        :param str id: The Seeq ID of the condition monitor (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
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
                    " to method set_notification_configuration_for_condition_monitor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_notification_configuration_for_condition_monitor`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_notification_configuration_for_condition_monitor`")


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

        return self.api_client.call_api('/notification-configurations/condition-monitors/{id}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'NotificationConfigurationOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_notification_configuration_for_report(self, **kwargs):
        """
        Create or update a notification configuration on a report
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_notification_configuration_for_report(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportNotificationConfigurationInputV1 body: (required)
        :param str id: The Seeq ID of the report (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_notification_configuration_for_report_with_http_info(**kwargs)
        else:
            (data) = self.set_notification_configuration_for_report_with_http_info(**kwargs)
            return data

    def set_notification_configuration_for_report_with_http_info(self, **kwargs):
        """
        Create or update a notification configuration on a report
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_notification_configuration_for_report_with_http_info(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportNotificationConfigurationInputV1 body: (required)
        :param str id: The Seeq ID of the report (required)
        :return: NotificationConfigurationOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationConfigurationOutputV1
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
                    " to method set_notification_configuration_for_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_notification_configuration_for_report`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `set_notification_configuration_for_report`")


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

        return self.api_client.call_api('/notification-configurations/reports/{id}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'NotificationConfigurationOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def unsubscribe_from_item(self, **kwargs):
        """
        Unsubscribe the current user from the notification on the specified item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unsubscribe_from_item(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the item to unsubscribe from (required)
        :return: UnsubscribeOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UnsubscribeOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.unsubscribe_from_item_with_http_info(**kwargs)
        else:
            (data) = self.unsubscribe_from_item_with_http_info(**kwargs)
            return data

    def unsubscribe_from_item_with_http_info(self, **kwargs):
        """
        Unsubscribe the current user from the notification on the specified item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unsubscribe_from_item_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The ID of the item to unsubscribe from (required)
        :return: UnsubscribeOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UnsubscribeOutputV1
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
                    " to method unsubscribe_from_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `unsubscribe_from_item`")


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

        return self.api_client.call_api('/notification-configurations/unsubscribe/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'UnsubscribeOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
