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


class SecretOpenAICredentialsCreateAPIInput(object):
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
        'credential': 'V1OpenAICredential',
        'secret_name': 'str'
    }

    attribute_map = {
        'credential': 'credential',
        'secret_name': 'secret_name'
    }

    def __init__(self, credential=None, secret_name=None, local_vars_configuration=None):  # noqa: E501
        """SecretOpenAICredentialsCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._credential = None
        self._secret_name = None
        self.discriminator = None

        self.credential = credential
        self.secret_name = secret_name

    @property
    def credential(self):
        """Gets the credential of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501


        :return: The credential of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501
        :rtype: V1OpenAICredential
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this SecretOpenAICredentialsCreateAPIInput.


        :param credential: The credential of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501
        :type credential: V1OpenAICredential
        """
        if self.local_vars_configuration.client_side_validation and credential is None:  # noqa: E501
            raise ValueError("Invalid value for `credential`, must not be `None`")  # noqa: E501

        self._credential = credential

    @property
    def secret_name(self):
        """Gets the secret_name of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501


        :return: The secret_name of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this SecretOpenAICredentialsCreateAPIInput.


        :param secret_name: The secret_name of this SecretOpenAICredentialsCreateAPIInput.  # noqa: E501
        :type secret_name: str
        """
        if self.local_vars_configuration.client_side_validation and secret_name is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_name`, must not be `None`")  # noqa: E501

        self._secret_name = secret_name

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
        if not isinstance(other, SecretOpenAICredentialsCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecretOpenAICredentialsCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
