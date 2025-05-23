"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  The OpenAPI Specification in YAML format is available on [www](https://www.agilicus.com/www/api/agilicus-openapi.yaml) for importing to other tools.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2025.05.20
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.api_client import ApiClient, Endpoint as _Endpoint
from agilicus_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from agilicus_api.model.mfa_challenge_answer import MFAChallengeAnswer
from agilicus_api.model.mfa_challenge_question import MFAChallengeQuestion
from agilicus_api.model.mfa_enrollment_answer import MFAEnrollmentAnswer
from agilicus_api.model.mfa_enrollment_question import MFAEnrollmentQuestion
from agilicus_api.model.map_attributes_answer import MapAttributesAnswer
from agilicus_api.model.map_attributes_question import MapAttributesQuestion


class PolicyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_challenge_decision(
            self,
            mfa_challenge_question,
            **kwargs
        ):
            """evaluate a policy challenge decision  # noqa: E501

            Evaluate a policy challenge decision to determine if the user should be forced to answer a challenge  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_challenge_decision(mfa_challenge_question, async_req=True)
            >>> result = thread.get()

            Args:
                mfa_challenge_question (MFAChallengeQuestion): The MFA Challenge Question to ask

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MFAChallengeAnswer
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['mfa_challenge_question'] = \
                mfa_challenge_question
            return self.call_with_http_info(**kwargs)

        if self.get_challenge_decision is None:
            self.get_challenge_decision = _Endpoint(
                settings={
                    'response_type': (MFAChallengeAnswer,),
                    'auth': [],
                    'endpoint_path': '/v1/data/authentication/mfa_policy/allow',
                    'operation_id': 'get_challenge_decision',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'mfa_challenge_question',
                    ],
                    'required': [
                        'mfa_challenge_question',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'mfa_challenge_question':
                            (MFAChallengeQuestion,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'mfa_challenge_question': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__get_challenge_decision
            )

        def __get_enrollment_decision(
            self,
            mfa_enrollment_question,
            **kwargs
        ):
            """evaluate a policy enrollment decision  # noqa: E501

            Evaluate a policy enrollment decision to determine if the user should be forced to enroll  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_enrollment_decision(mfa_enrollment_question, async_req=True)
            >>> result = thread.get()

            Args:
                mfa_enrollment_question (MFAEnrollmentQuestion): The MFA Enrollment Question to ask

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MFAEnrollmentAnswer
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['mfa_enrollment_question'] = \
                mfa_enrollment_question
            return self.call_with_http_info(**kwargs)

        if self.get_enrollment_decision is None:
            self.get_enrollment_decision = _Endpoint(
                settings={
                    'response_type': (MFAEnrollmentAnswer,),
                    'auth': [],
                    'endpoint_path': '/v1/data/authentication/enrollment/allow',
                    'operation_id': 'get_enrollment_decision',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'mfa_enrollment_question',
                    ],
                    'required': [
                        'mfa_enrollment_question',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'mfa_enrollment_question':
                            (MFAEnrollmentQuestion,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'mfa_enrollment_question': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__get_enrollment_decision
            )

        def __map_attributes(
            self,
            map_attributes_question,
            **kwargs
        ):
            """map attributes of a user  # noqa: E501

            map attributes of a user  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.map_attributes(map_attributes_question, async_req=True)
            >>> result = thread.get()

            Args:
                map_attributes_question (MapAttributesQuestion): The attributes to map and information used to gather them

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MapAttributesAnswer
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['map_attributes_question'] = \
                map_attributes_question
            return self.call_with_http_info(**kwargs)

        if self.map_attributes is None:
            self.map_attributes = _Endpoint(
                settings={
                    'response_type': (MapAttributesAnswer,),
                    'auth': [],
                    'endpoint_path': '/v1/data/authentication/attribute_mapping/map_attributes',
                    'operation_id': 'map_attributes',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'map_attributes_question',
                    ],
                    'required': [
                        'map_attributes_question',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'map_attributes_question':
                            (MapAttributesQuestion,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'map_attributes_question': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__map_attributes
            )

    get_challenge_decision = None 
    get_enrollment_decision = None 
    map_attributes = None 
