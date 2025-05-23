# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class HashiPayload(object):
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
        'import_as_json': 'bool',
        'namespaces': 'list[str]',
        'token': 'str',
        'url': 'str'
    }

    attribute_map = {
        'import_as_json': 'import_as_json',
        'namespaces': 'namespaces',
        'token': 'token',
        'url': 'url'
    }

    def __init__(self, import_as_json=None, namespaces=None, token=None, url=None, local_vars_configuration=None):  # noqa: E501
        """HashiPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._import_as_json = None
        self._namespaces = None
        self._token = None
        self._url = None
        self.discriminator = None

        if import_as_json is not None:
            self.import_as_json = import_as_json
        if namespaces is not None:
            self.namespaces = namespaces
        if token is not None:
            self.token = token
        if url is not None:
            self.url = url

    @property
    def import_as_json(self):
        """Gets the import_as_json of this HashiPayload.  # noqa: E501


        :return: The import_as_json of this HashiPayload.  # noqa: E501
        :rtype: bool
        """
        return self._import_as_json

    @import_as_json.setter
    def import_as_json(self, import_as_json):
        """Sets the import_as_json of this HashiPayload.


        :param import_as_json: The import_as_json of this HashiPayload.  # noqa: E501
        :type: bool
        """

        self._import_as_json = import_as_json

    @property
    def namespaces(self):
        """Gets the namespaces of this HashiPayload.  # noqa: E501


        :return: The namespaces of this HashiPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this HashiPayload.


        :param namespaces: The namespaces of this HashiPayload.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def token(self):
        """Gets the token of this HashiPayload.  # noqa: E501


        :return: The token of this HashiPayload.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this HashiPayload.


        :param token: The token of this HashiPayload.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def url(self):
        """Gets the url of this HashiPayload.  # noqa: E501


        :return: The url of this HashiPayload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HashiPayload.


        :param url: The url of this HashiPayload.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, HashiPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HashiPayload):
            return True

        return self.to_dict() != other.to_dict()
