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

class V1RefreshResponse(object):
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
        'token': 'str'
    }

    attribute_map = {
        'token': 'token'
    }

    def __init__(self, token: 'str' =None):  # noqa: E501
        """V1RefreshResponse - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self.discriminator = None
        if token is not None:
            self.token = token

    @property
    def token(self) -> 'str':
        """Gets the token of this V1RefreshResponse.  # noqa: E501


        :return: The token of this V1RefreshResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: 'str'):
        """Sets the token of this V1RefreshResponse.


        :param token: The token of this V1RefreshResponse.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(V1RefreshResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1RefreshResponse') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1RefreshResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1RefreshResponse') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
