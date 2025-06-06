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


class OrganizationPublicIdentifier(object):
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
        'public_identifier': 'str'
    }

    attribute_map = {
        'public_identifier': 'public_identifier'
    }

    def __init__(self, public_identifier=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationPublicIdentifier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._public_identifier = None
        self.discriminator = None

        self.public_identifier = public_identifier

    @property
    def public_identifier(self):
        """Gets the public_identifier of this OrganizationPublicIdentifier.  # noqa: E501


        :return: The public_identifier of this OrganizationPublicIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._public_identifier

    @public_identifier.setter
    def public_identifier(self, public_identifier):
        """Sets the public_identifier of this OrganizationPublicIdentifier.


        :param public_identifier: The public_identifier of this OrganizationPublicIdentifier.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `public_identifier`, must not be `None`")  # noqa: E501

        self._public_identifier = public_identifier

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
        if not isinstance(other, OrganizationPublicIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationPublicIdentifier):
            return True

        return self.to_dict() != other.to_dict()
