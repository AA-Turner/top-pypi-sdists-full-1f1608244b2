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


class ExpressionWithAlias(object):
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
        'expression': 'str',
        'alias': 'str',
        'flags': 'MappingFlags'
    }

    attribute_map = {
        'expression': 'expression',
        'alias': 'alias',
        'flags': 'flags'
    }

    required_map = {
        'expression': 'required',
        'alias': 'optional',
        'flags': 'optional'
    }

    def __init__(self, expression=None, alias=None, flags=None, local_vars_configuration=None):  # noqa: E501
        """ExpressionWithAlias - a model defined in OpenAPI"
        
        :param expression:  Expression (column name, constant, complex expression, etc.) (required)
        :type expression: str
        :param alias:  Column Alias for the expression
        :type alias: str
        :param flags: 
        :type flags: luminesce.MappingFlags

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._expression = None
        self._alias = None
        self._flags = None
        self.discriminator = None

        self.expression = expression
        self.alias = alias
        if flags is not None:
            self.flags = flags

    @property
    def expression(self):
        """Gets the expression of this ExpressionWithAlias.  # noqa: E501

        Expression (column name, constant, complex expression, etc.)  # noqa: E501

        :return: The expression of this ExpressionWithAlias.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ExpressionWithAlias.

        Expression (column name, constant, complex expression, etc.)  # noqa: E501

        :param expression: The expression of this ExpressionWithAlias.  # noqa: E501
        :type expression: str
        """
        if self.local_vars_configuration.client_side_validation and expression is None:  # noqa: E501
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                expression is not None and len(expression) < 1):
            raise ValueError("Invalid value for `expression`, length must be greater than or equal to `1`")  # noqa: E501

        self._expression = expression

    @property
    def alias(self):
        """Gets the alias of this ExpressionWithAlias.  # noqa: E501

        Column Alias for the expression  # noqa: E501

        :return: The alias of this ExpressionWithAlias.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ExpressionWithAlias.

        Column Alias for the expression  # noqa: E501

        :param alias: The alias of this ExpressionWithAlias.  # noqa: E501
        :type alias: str
        """

        self._alias = alias

    @property
    def flags(self):
        """Gets the flags of this ExpressionWithAlias.  # noqa: E501


        :return: The flags of this ExpressionWithAlias.  # noqa: E501
        :rtype: luminesce.MappingFlags
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this ExpressionWithAlias.


        :param flags: The flags of this ExpressionWithAlias.  # noqa: E501
        :type flags: luminesce.MappingFlags
        """

        self._flags = flags

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
        if not isinstance(other, ExpressionWithAlias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExpressionWithAlias):
            return True

        return self.to_dict() != other.to_dict()
