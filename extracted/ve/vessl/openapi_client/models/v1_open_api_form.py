# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class V1OpenAPIForm(object):
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
        'method': 'str',
        'path': 'str',
        'url': 'str'
    }

    attribute_map = {
        'method': 'method',
        'path': 'path',
        'url': 'url'
    }

    def __init__(self, method=None, path=None, url=None, local_vars_configuration=None):  # noqa: E501
        """V1OpenAPIForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._method = None
        self._path = None
        self._url = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url

    @property
    def method(self):
        """Gets the method of this V1OpenAPIForm.  # noqa: E501


        :return: The method of this V1OpenAPIForm.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this V1OpenAPIForm.


        :param method: The method of this V1OpenAPIForm.  # noqa: E501
        :type method: str
        """
        allowed_values = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def path(self):
        """Gets the path of this V1OpenAPIForm.  # noqa: E501


        :return: The path of this V1OpenAPIForm.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1OpenAPIForm.


        :param path: The path of this V1OpenAPIForm.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def url(self):
        """Gets the url of this V1OpenAPIForm.  # noqa: E501


        :return: The url of this V1OpenAPIForm.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1OpenAPIForm.


        :param url: The url of this V1OpenAPIForm.  # noqa: E501
        :type url: str
        """

        self._url = url

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1OpenAPIForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1OpenAPIForm):
            return True

        return self.to_dict() != other.to_dict()
