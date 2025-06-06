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


class RedisUserHistory(object):
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
        'path': 'str',
        'version': 'str',
        'visited_dt': 'datetime'
    }

    attribute_map = {
        'path': 'path',
        'version': 'version',
        'visited_dt': 'visited_dt'
    }

    def __init__(self, path=None, version=None, visited_dt=None, local_vars_configuration=None):  # noqa: E501
        """RedisUserHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._version = None
        self._visited_dt = None
        self.discriminator = None

        self.path = path
        self.version = version
        self.visited_dt = visited_dt

    @property
    def path(self):
        """Gets the path of this RedisUserHistory.  # noqa: E501


        :return: The path of this RedisUserHistory.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RedisUserHistory.


        :param path: The path of this RedisUserHistory.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def version(self):
        """Gets the version of this RedisUserHistory.  # noqa: E501


        :return: The version of this RedisUserHistory.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RedisUserHistory.


        :param version: The version of this RedisUserHistory.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def visited_dt(self):
        """Gets the visited_dt of this RedisUserHistory.  # noqa: E501


        :return: The visited_dt of this RedisUserHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._visited_dt

    @visited_dt.setter
    def visited_dt(self, visited_dt):
        """Sets the visited_dt of this RedisUserHistory.


        :param visited_dt: The visited_dt of this RedisUserHistory.  # noqa: E501
        :type visited_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and visited_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `visited_dt`, must not be `None`")  # noqa: E501

        self._visited_dt = visited_dt

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
        if not isinstance(other, RedisUserHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedisUserHistory):
            return True

        return self.to_dict() != other.to_dict()
