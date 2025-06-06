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

import pprint
import re  # noqa: F401

from typing import TYPE_CHECKING

import six

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class V1ListCloudSpacesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cloudspaces': 'list[V1CloudSpace]',
        'next_page_token': 'str',
        'previous_page_token': 'str'
    }

    attribute_map = {
        'cloudspaces': 'cloudspaces',
        'next_page_token': 'nextPageToken',
        'previous_page_token': 'previousPageToken'
    }

    def __init__(self, cloudspaces: 'list[V1CloudSpace]' =None, next_page_token: 'str' =None, previous_page_token: 'str' =None):  # noqa: E501
        """V1ListCloudSpacesResponse - a model defined in Swagger"""  # noqa: E501
        self._cloudspaces = None
        self._next_page_token = None
        self._previous_page_token = None
        self.discriminator = None
        if cloudspaces is not None:
            self.cloudspaces = cloudspaces
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token

    @property
    def cloudspaces(self) -> 'list[V1CloudSpace]':
        """Gets the cloudspaces of this V1ListCloudSpacesResponse.  # noqa: E501


        :return: The cloudspaces of this V1ListCloudSpacesResponse.  # noqa: E501
        :rtype: list[V1CloudSpace]
        """
        return self._cloudspaces

    @cloudspaces.setter
    def cloudspaces(self, cloudspaces: 'list[V1CloudSpace]'):
        """Sets the cloudspaces of this V1ListCloudSpacesResponse.


        :param cloudspaces: The cloudspaces of this V1ListCloudSpacesResponse.  # noqa: E501
        :type: list[V1CloudSpace]
        """

        self._cloudspaces = cloudspaces

    @property
    def next_page_token(self) -> 'str':
        """Gets the next_page_token of this V1ListCloudSpacesResponse.  # noqa: E501


        :return: The next_page_token of this V1ListCloudSpacesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token: 'str'):
        """Sets the next_page_token of this V1ListCloudSpacesResponse.


        :param next_page_token: The next_page_token of this V1ListCloudSpacesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def previous_page_token(self) -> 'str':
        """Gets the previous_page_token of this V1ListCloudSpacesResponse.  # noqa: E501


        :return: The previous_page_token of this V1ListCloudSpacesResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token: 'str'):
        """Sets the previous_page_token of this V1ListCloudSpacesResponse.


        :param previous_page_token: The previous_page_token of this V1ListCloudSpacesResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1ListCloudSpacesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1ListCloudSpacesResponse') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ListCloudSpacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1ListCloudSpacesResponse') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
