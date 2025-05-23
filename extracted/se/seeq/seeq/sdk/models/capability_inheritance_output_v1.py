# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class CapabilityInheritanceOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'capability': 'str',
        'inherited_from': 'IdentityPreviewV1'
    }

    attribute_map = {
        'capability': 'capability',
        'inherited_from': 'inheritedFrom'
    }

    def __init__(self, capability=None, inherited_from=None):
        """
        CapabilityInheritanceOutputV1 - a model defined in Swagger
        """

        self._capability = None
        self._inherited_from = None

        if capability is not None:
          self.capability = capability
        if inherited_from is not None:
          self.inherited_from = inherited_from

    @property
    def capability(self):
        """
        Gets the capability of this CapabilityInheritanceOutputV1.
        Name of the Capability

        :return: The capability of this CapabilityInheritanceOutputV1.
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """
        Sets the capability of this CapabilityInheritanceOutputV1.
        Name of the Capability

        :param capability: The capability of this CapabilityInheritanceOutputV1.
        :type: str
        """
        allowed_values = ["Admins", "AnalyticsAdministrationCapability", "AuditTrailCapability", "UserAdministrationCapability", "DatasourceAdministrationCapability", "LogViewerCapability", "ScalingTableCapability"]
        if capability not in allowed_values:
            raise ValueError(
                "Invalid value for `capability` ({0}), must be one of {1}"
                .format(capability, allowed_values)
            )

        self._capability = capability

    @property
    def inherited_from(self):
        """
        Gets the inherited_from of this CapabilityInheritanceOutputV1.

        :return: The inherited_from of this CapabilityInheritanceOutputV1.
        :rtype: IdentityPreviewV1
        """
        return self._inherited_from

    @inherited_from.setter
    def inherited_from(self, inherited_from):
        """
        Sets the inherited_from of this CapabilityInheritanceOutputV1.

        :param inherited_from: The inherited_from of this CapabilityInheritanceOutputV1.
        :type: IdentityPreviewV1
        """

        self._inherited_from = inherited_from

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CapabilityInheritanceOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
