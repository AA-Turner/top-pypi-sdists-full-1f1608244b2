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

class ReportTemplatesApi(object):
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

    def archive_report_template(self, **kwargs):
        """
        Archive a report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_report_template(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the report template to archive. (required)
        :return: ArchiveOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ArchiveOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.archive_report_template_with_http_info(**kwargs)
        else:
            (data) = self.archive_report_template_with_http_info(**kwargs)
            return data

    def archive_report_template_with_http_info(self, **kwargs):
        """
        Archive a report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.archive_report_template_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the report template to archive. (required)
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
                    " to method archive_report_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `archive_report_template`")


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

        return self.api_client.call_api('/report-templates/{id}', 'DELETE',
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

    def create_report_template(self, **kwargs):
        """
        Create a new report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_report_template(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportTemplateInputV1 body: (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_report_template_with_http_info(**kwargs)
        else:
            (data) = self.create_report_template_with_http_info(**kwargs)
            return data

    def create_report_template_with_http_info(self, **kwargs):
        """
        Create a new report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_report_template_with_http_info(body=body_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportTemplateInputV1 body: (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
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
                    " to method create_report_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_report_template`")


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

        return self.api_client.call_api('/report-templates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ReportTemplateOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_report_template(self, **kwargs):
        """
        Get a report template item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_template(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID for the report template (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_report_template_with_http_info(**kwargs)
        else:
            (data) = self.get_report_template_with_http_info(**kwargs)
            return data

    def get_report_template_with_http_info(self, **kwargs):
        """
        Get a report template item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_template_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The Seeq ID for the report template (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
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
                    " to method get_report_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_report_template`")


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

        return self.api_client.call_api('/report-templates/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ReportTemplateOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_thumbnail(self, **kwargs):
        """
        Get the thumbnail for a report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_thumbnail(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the report template which you want the thumbnail of. (required)
        :return: bytes
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytes
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_thumbnail_with_http_info(**kwargs)
        else:
            (data) = self.get_thumbnail_with_http_info(**kwargs)
            return data

    def get_thumbnail_with_http_info(self, **kwargs):
        """
        Get the thumbnail for a report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_thumbnail_with_http_info(id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of the report template which you want the thumbnail of. (required)
        :return: bytes
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytes
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
                    " to method get_thumbnail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_thumbnail`")


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
            select_header_accept(['application/vnd.seeq.v1+json', 'image/png'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.seeq.v1+json', ])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/report-templates/thumbnail/{id}', 'GET',
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

    def update_report_template(self, **kwargs):
        """
        Update the given report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_report_template(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportTemplateInputV1 body: (required)
        :param str id: The Seeq ID for the report template (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_report_template_with_http_info(**kwargs)
        else:
            (data) = self.update_report_template_with_http_info(**kwargs)
            return data

    def update_report_template_with_http_info(self, **kwargs):
        """
        Update the given report template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_report_template_with_http_info(body=body_value, id=id_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportTemplateInputV1 body: (required)
        :param str id: The Seeq ID for the report template (required)
        :return: ReportTemplateOutputV1
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReportTemplateOutputV1
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
                    " to method update_report_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_report_template`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_report_template`")


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

        return self.api_client.call_api('/report-templates/{id}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=params.get('_response_type', 'ReportTemplateOutputV1'),
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
