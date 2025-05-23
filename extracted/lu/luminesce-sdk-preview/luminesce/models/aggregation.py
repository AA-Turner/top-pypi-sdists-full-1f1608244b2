# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from luminesce.configuration import Configuration


class Aggregation(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'type': 'AggregateFunction',
        'alias': 'str'
    }

    attribute_map = {
        'type': 'type',
        'alias': 'alias'
    }

    required_map = {
        'type': 'required',
        'alias': 'optional'
    }

    def __init__(self, type=None, alias=None, local_vars_configuration=None):  # noqa: E501
        """Aggregation - a model defined in OpenAPI"
        
        :param type:  (required)
        :type type: luminesce.AggregateFunction
        :param alias:  Alias, if any, for the Aggregate expression when selected
        :type alias: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._alias = None
        self.discriminator = None

        self.type = type
        self.alias = alias

    @property
    def type(self):
        """Gets the type of this Aggregation.  # noqa: E501


        :return: The type of this Aggregation.  # noqa: E501
        :rtype: luminesce.AggregateFunction
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Aggregation.


        :param type: The type of this Aggregation.  # noqa: E501
        :type type: luminesce.AggregateFunction
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def alias(self):
        """Gets the alias of this Aggregation.  # noqa: E501

        Alias, if any, for the Aggregate expression when selected  # noqa: E501

        :return: The alias of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Aggregation.

        Alias, if any, for the Aggregate expression when selected  # noqa: E501

        :param alias: The alias of this Aggregation.  # noqa: E501
        :type alias: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) > 256):
            raise ValueError("Invalid value for `alias`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) < 0):
            raise ValueError("Invalid value for `alias`, length must be greater than or equal to `0`")  # noqa: E501

        self._alias = alias

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
        if not isinstance(other, Aggregation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Aggregation):
            return True

        return self.to_dict() != other.to_dict()
