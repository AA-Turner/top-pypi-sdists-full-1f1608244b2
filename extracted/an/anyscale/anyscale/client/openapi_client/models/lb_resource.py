# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class LBResource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'is_terminated': 'bool'
    }

    attribute_map = {
        'is_terminated': 'is_terminated'
    }

    def __init__(self, is_terminated=None, local_vars_configuration=None):  # noqa: E501
        """LBResource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_terminated = None
        self.discriminator = None

        self.is_terminated = is_terminated

    @property
    def is_terminated(self):
        """Gets the is_terminated of this LBResource.  # noqa: E501

        Flag if the Load balancer resources are terminated  # noqa: E501

        :return: The is_terminated of this LBResource.  # noqa: E501
        :rtype: bool
        """
        return self._is_terminated

    @is_terminated.setter
    def is_terminated(self, is_terminated):
        """Sets the is_terminated of this LBResource.

        Flag if the Load balancer resources are terminated  # noqa: E501

        :param is_terminated: The is_terminated of this LBResource.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_terminated is None:  # noqa: E501
            raise ValueError("Invalid value for `is_terminated`, must not be `None`")  # noqa: E501

        self._is_terminated = is_terminated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LBResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LBResource):
            return True

        return self.to_dict() != other.to_dict()
