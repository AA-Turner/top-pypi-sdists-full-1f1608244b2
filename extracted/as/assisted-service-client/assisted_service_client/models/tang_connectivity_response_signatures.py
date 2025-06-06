# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TangConnectivityResponseSignatures(object):
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
        'protected': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'protected': 'protected',
        'signature': 'signature'
    }

    def __init__(self, protected=None, signature=None):  # noqa: E501
        """TangConnectivityResponseSignatures - a model defined in Swagger"""  # noqa: E501

        self._protected = None
        self._signature = None
        self.discriminator = None

        if protected is not None:
            self.protected = protected
        if signature is not None:
            self.signature = signature

    @property
    def protected(self):
        """Gets the protected of this TangConnectivityResponseSignatures.  # noqa: E501


        :return: The protected of this TangConnectivityResponseSignatures.  # noqa: E501
        :rtype: str
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this TangConnectivityResponseSignatures.


        :param protected: The protected of this TangConnectivityResponseSignatures.  # noqa: E501
        :type: str
        """

        self._protected = protected

    @property
    def signature(self):
        """Gets the signature of this TangConnectivityResponseSignatures.  # noqa: E501


        :return: The signature of this TangConnectivityResponseSignatures.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this TangConnectivityResponseSignatures.


        :param signature: The signature of this TangConnectivityResponseSignatures.  # noqa: E501
        :type: str
        """

        self._signature = signature

    def to_dict(self):
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
        if issubclass(TangConnectivityResponseSignatures, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TangConnectivityResponseSignatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
