# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.257
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

from lusid.configuration import Configuration


class ResultValueDecimal(object):
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
        'value': 'float',
        'dimension': 'int',
        'result_value_type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'dimension': 'dimension',
        'result_value_type': 'resultValueType'
    }

    required_map = {
        'value': 'optional',
        'dimension': 'optional',
        'result_value_type': 'required'
    }

    def __init__(self, value=None, dimension=None, result_value_type=None, local_vars_configuration=None):  # noqa: E501
        """ResultValueDecimal - a model defined in OpenAPI"
        
        :param value:  The value itself
        :type value: float
        :param dimension:  The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion.
        :type dimension: int
        :param result_value_type:  The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset (required)
        :type result_value_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._dimension = None
        self._result_value_type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.dimension = dimension
        self.result_value_type = result_value_type

    @property
    def value(self):
        """Gets the value of this ResultValueDecimal.  # noqa: E501

        The value itself  # noqa: E501

        :return: The value of this ResultValueDecimal.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResultValueDecimal.

        The value itself  # noqa: E501

        :param value: The value of this ResultValueDecimal.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def dimension(self):
        """Gets the dimension of this ResultValueDecimal.  # noqa: E501

        The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion.  # noqa: E501

        :return: The dimension of this ResultValueDecimal.  # noqa: E501
        :rtype: int
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this ResultValueDecimal.

        The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion.  # noqa: E501

        :param dimension: The dimension of this ResultValueDecimal.  # noqa: E501
        :type dimension: int
        """

        self._dimension = dimension

    @property
    def result_value_type(self):
        """Gets the result_value_type of this ResultValueDecimal.  # noqa: E501

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :return: The result_value_type of this ResultValueDecimal.  # noqa: E501
        :rtype: str
        """
        return self._result_value_type

    @result_value_type.setter
    def result_value_type(self, result_value_type):
        """Sets the result_value_type of this ResultValueDecimal.

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :param result_value_type: The result_value_type of this ResultValueDecimal.  # noqa: E501
        :type result_value_type: str
        """
        if self.local_vars_configuration.client_side_validation and result_value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `result_value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ResultValue", "ResultValueDictionary", "ResultValue0D", "ResultValueDecimal", "ResultValueInt", "ResultValueString", "ResultValueBool", "ResultValueCurrency", "CashFlowValue", "CashFlowValueSet", "ResultValueLifeCycleEventValue", "ResultValueDateTimeOffset"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result_value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_value_type, allowed_values)
            )

        self._result_value_type = result_value_type

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
        if not isinstance(other, ResultValueDecimal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultValueDecimal):
            return True

        return self.to_dict() != other.to_dict()
