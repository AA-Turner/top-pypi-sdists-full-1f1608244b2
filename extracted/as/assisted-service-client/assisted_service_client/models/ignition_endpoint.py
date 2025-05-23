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


class IgnitionEndpoint(object):
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
        'url': 'str',
        'ca_certificate': 'str'
    }

    attribute_map = {
        'url': 'url',
        'ca_certificate': 'ca_certificate'
    }

    def __init__(self, url=None, ca_certificate=None):  # noqa: E501
        """IgnitionEndpoint - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._ca_certificate = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate

    @property
    def url(self):
        """Gets the url of this IgnitionEndpoint.  # noqa: E501

        The URL for the ignition endpoint.  # noqa: E501

        :return: The url of this IgnitionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IgnitionEndpoint.

        The URL for the ignition endpoint.  # noqa: E501

        :param url: The url of this IgnitionEndpoint.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def ca_certificate(self):
        """Gets the ca_certificate of this IgnitionEndpoint.  # noqa: E501

        base64 encoded CA certficate to be used when contacting the URL via https.  # noqa: E501

        :return: The ca_certificate of this IgnitionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """Sets the ca_certificate of this IgnitionEndpoint.

        base64 encoded CA certficate to be used when contacting the URL via https.  # noqa: E501

        :param ca_certificate: The ca_certificate of this IgnitionEndpoint.  # noqa: E501
        :type: str
        """

        self._ca_certificate = ca_certificate

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
        if issubclass(IgnitionEndpoint, dict):
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
        if not isinstance(other, IgnitionEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
