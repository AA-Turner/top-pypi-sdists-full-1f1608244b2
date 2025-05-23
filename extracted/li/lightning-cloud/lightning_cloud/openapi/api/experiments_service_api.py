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

class ExperimentsServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def experiments_service_assign_variant(self, body: 'ExperimentNameVariantNameBody', experiment_name: 'str', variant_name: 'str', **kwargs) -> 'V1AssignVariantResponse':  # noqa: E501
        """experiments_service_assign_variant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.experiments_service_assign_variant(body, experiment_name, variant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExperimentNameVariantNameBody body: (required)
        :param str experiment_name: (required)
        :param str variant_name: (required)
        :return: V1AssignVariantResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.experiments_service_assign_variant_with_http_info(body, experiment_name, variant_name, **kwargs)  # noqa: E501
        else:
            (data) = self.experiments_service_assign_variant_with_http_info(body, experiment_name, variant_name, **kwargs)  # noqa: E501
            return data

    def experiments_service_assign_variant_with_http_info(self, body: 'ExperimentNameVariantNameBody', experiment_name: 'str', variant_name: 'str', **kwargs) -> 'V1AssignVariantResponse':  # noqa: E501
        """experiments_service_assign_variant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.experiments_service_assign_variant_with_http_info(body, experiment_name, variant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExperimentNameVariantNameBody body: (required)
        :param str experiment_name: (required)
        :param str variant_name: (required)
        :return: V1AssignVariantResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'experiment_name', 'variant_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method experiments_service_assign_variant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `experiments_service_assign_variant`")  # noqa: E501
        # verify the required parameter 'experiment_name' is set
        if ('experiment_name' not in params or
                params['experiment_name'] is None):
            raise ValueError("Missing the required parameter `experiment_name` when calling `experiments_service_assign_variant`")  # noqa: E501
        # verify the required parameter 'variant_name' is set
        if ('variant_name' not in params or
                params['variant_name'] is None):
            raise ValueError("Missing the required parameter `variant_name` when calling `experiments_service_assign_variant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'experiment_name' in params:
            path_params['experimentName'] = params['experiment_name']  # noqa: E501
        if 'variant_name' in params:
            path_params['variantName'] = params['variant_name']  # noqa: E501

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
            '/v1/experiments/assign_variant/{experimentName}/{variantName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AssignVariantResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def experiments_service_list_experiments(self, **kwargs) -> 'V1ListExperimentsResponse':  # noqa: E501
        """experiments_service_list_experiments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.experiments_service_list_experiments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.experiments_service_list_experiments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.experiments_service_list_experiments_with_http_info(**kwargs)  # noqa: E501
            return data

    def experiments_service_list_experiments_with_http_info(self, **kwargs) -> 'V1ListExperimentsResponse':  # noqa: E501
        """experiments_service_list_experiments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.experiments_service_list_experiments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: V1ListExperimentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method experiments_service_list_experiments" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/experiments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListExperimentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
