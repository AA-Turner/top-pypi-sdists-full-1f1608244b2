# coding: utf-8

"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

from __future__ import absolute_import

import re  # noqa: F401
from typing import TYPE_CHECKING, Any

# python 2 and python 3 compatibility library
import six

from lightning_cloud.openapi.api_client import ApiClient

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class ProfilerServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def profiler_service_create_profiler_capture(self, body: 'ProfilerCapturesBody', project_id: 'str', **kwargs) -> 'V1ProfilerCapture':  # noqa: E501
        """profiler_service_create_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_create_profiler_capture(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfilerCapturesBody body: (required)
        :param str project_id: (required)
        :return: V1ProfilerCapture
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_create_profiler_capture_with_http_info(body, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_create_profiler_capture_with_http_info(body, project_id, **kwargs)  # noqa: E501
            return data

    def profiler_service_create_profiler_capture_with_http_info(self, body: 'ProfilerCapturesBody', project_id: 'str', **kwargs) -> 'V1ProfilerCapture':  # noqa: E501
        """profiler_service_create_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_create_profiler_capture_with_http_info(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfilerCapturesBody body: (required)
        :param str project_id: (required)
        :return: V1ProfilerCapture
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_create_profiler_capture" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `profiler_service_create_profiler_capture`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_create_profiler_capture`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/captures', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ProfilerCapture',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiler_service_delete_profiler_capture(self, project_id: 'str', id: 'str', **kwargs) -> 'V1DeleteProfilerCaptureResponse':  # noqa: E501
        """profiler_service_delete_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_delete_profiler_capture(project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str id: (required)
        :return: V1DeleteProfilerCaptureResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_delete_profiler_capture_with_http_info(project_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_delete_profiler_capture_with_http_info(project_id, id, **kwargs)  # noqa: E501
            return data

    def profiler_service_delete_profiler_capture_with_http_info(self, project_id: 'str', id: 'str', **kwargs) -> 'V1DeleteProfilerCaptureResponse':  # noqa: E501
        """profiler_service_delete_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_delete_profiler_capture_with_http_info(project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str id: (required)
        :return: V1DeleteProfilerCaptureResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_delete_profiler_capture" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_delete_profiler_capture`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `profiler_service_delete_profiler_capture`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/captures/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DeleteProfilerCaptureResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiler_service_get_enable_profiler(self, project_id: 'str', **kwargs) -> 'V1ProfilerEnabledResponse':  # noqa: E501
        """profiler_service_get_enable_profiler  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_get_enable_profiler(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str cloud_space_instance_id:
        :return: V1ProfilerEnabledResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_get_enable_profiler_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_get_enable_profiler_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def profiler_service_get_enable_profiler_with_http_info(self, project_id: 'str', **kwargs) -> 'V1ProfilerEnabledResponse':  # noqa: E501
        """profiler_service_get_enable_profiler  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_get_enable_profiler_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str cloud_space_instance_id:
        :return: V1ProfilerEnabledResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'cloud_space_instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_get_enable_profiler" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_get_enable_profiler`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'cloud_space_instance_id' in params:
            query_params.append(('cloudSpaceInstanceId', params['cloud_space_instance_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/enabled', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ProfilerEnabledResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiler_service_list_profiler_captures(self, project_id: 'str', **kwargs) -> 'V1ListProfilerCapturesResponse':  # noqa: E501
        """profiler_service_list_profiler_captures  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_list_profiler_captures(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param list[str] cloudspace_ids:
        :return: V1ListProfilerCapturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_list_profiler_captures_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_list_profiler_captures_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def profiler_service_list_profiler_captures_with_http_info(self, project_id: 'str', **kwargs) -> 'V1ListProfilerCapturesResponse':  # noqa: E501
        """profiler_service_list_profiler_captures  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_list_profiler_captures_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param list[str] cloudspace_ids:
        :return: V1ListProfilerCapturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'cloudspace_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_list_profiler_captures" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_list_profiler_captures`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'cloudspace_ids' in params:
            query_params.append(('cloudspaceIds', params['cloudspace_ids']))  # noqa: E501
            collection_formats['cloudspaceIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/captures', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListProfilerCapturesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiler_service_update_profiler_capture(self, body: 'CapturesIdBody', project_id: 'str', id: 'str', **kwargs) -> 'V1ProfilerCapture':  # noqa: E501
        """profiler_service_update_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_update_profiler_capture(body, project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CapturesIdBody body: (required)
        :param str project_id: (required)
        :param str id: (required)
        :return: V1ProfilerCapture
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_update_profiler_capture_with_http_info(body, project_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_update_profiler_capture_with_http_info(body, project_id, id, **kwargs)  # noqa: E501
            return data

    def profiler_service_update_profiler_capture_with_http_info(self, body: 'CapturesIdBody', project_id: 'str', id: 'str', **kwargs) -> 'V1ProfilerCapture':  # noqa: E501
        """profiler_service_update_profiler_capture  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_update_profiler_capture_with_http_info(body, project_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CapturesIdBody body: (required)
        :param str project_id: (required)
        :param str id: (required)
        :return: V1ProfilerCapture
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_update_profiler_capture" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `profiler_service_update_profiler_capture`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_update_profiler_capture`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `profiler_service_update_profiler_capture`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/captures/{id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ProfilerCapture',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def profiler_service_update_profiler_enabled(self, body: 'ProfilerEnabledBody', project_id: 'str', **kwargs) -> 'V1ProfilerEnabledResponse':  # noqa: E501
        """profiler_service_update_profiler_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_update_profiler_enabled(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfilerEnabledBody body: (required)
        :param str project_id: (required)
        :return: V1ProfilerEnabledResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profiler_service_update_profiler_enabled_with_http_info(body, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.profiler_service_update_profiler_enabled_with_http_info(body, project_id, **kwargs)  # noqa: E501
            return data

    def profiler_service_update_profiler_enabled_with_http_info(self, body: 'ProfilerEnabledBody', project_id: 'str', **kwargs) -> 'V1ProfilerEnabledResponse':  # noqa: E501
        """profiler_service_update_profiler_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profiler_service_update_profiler_enabled_with_http_info(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfilerEnabledBody body: (required)
        :param str project_id: (required)
        :return: V1ProfilerEnabledResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method profiler_service_update_profiler_enabled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `profiler_service_update_profiler_enabled`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `profiler_service_update_profiler_enabled`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/profiler/enabled', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ProfilerEnabledResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
