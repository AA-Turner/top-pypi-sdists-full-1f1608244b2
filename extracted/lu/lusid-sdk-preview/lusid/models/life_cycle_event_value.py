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


class LifeCycleEventValue(object):
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
        'effective_date': 'datetime',
        'event_values': 'ResultValueDictionary',
        'event_lineage': 'LifeCycleEventLineage',
        'result_value_type': 'str'
    }

    attribute_map = {
        'effective_date': 'effectiveDate',
        'event_values': 'eventValues',
        'event_lineage': 'eventLineage',
        'result_value_type': 'resultValueType'
    }

    required_map = {
        'effective_date': 'optional',
        'event_values': 'optional',
        'event_lineage': 'optional',
        'result_value_type': 'required'
    }

    def __init__(self, effective_date=None, event_values=None, event_lineage=None, result_value_type=None, local_vars_configuration=None):  # noqa: E501
        """LifeCycleEventValue - a model defined in OpenAPI"
        
        :param effective_date:  The effective date of the event
        :type effective_date: datetime
        :param event_values: 
        :type event_values: lusid.ResultValueDictionary
        :param event_lineage: 
        :type event_lineage: lusid.LifeCycleEventLineage
        :param result_value_type:  The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset (required)
        :type result_value_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_date = None
        self._event_values = None
        self._event_lineage = None
        self._result_value_type = None
        self.discriminator = None

        if effective_date is not None:
            self.effective_date = effective_date
        if event_values is not None:
            self.event_values = event_values
        if event_lineage is not None:
            self.event_lineage = event_lineage
        self.result_value_type = result_value_type

    @property
    def effective_date(self):
        """Gets the effective_date of this LifeCycleEventValue.  # noqa: E501

        The effective date of the event  # noqa: E501

        :return: The effective_date of this LifeCycleEventValue.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this LifeCycleEventValue.

        The effective date of the event  # noqa: E501

        :param effective_date: The effective_date of this LifeCycleEventValue.  # noqa: E501
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def event_values(self):
        """Gets the event_values of this LifeCycleEventValue.  # noqa: E501


        :return: The event_values of this LifeCycleEventValue.  # noqa: E501
        :rtype: lusid.ResultValueDictionary
        """
        return self._event_values

    @event_values.setter
    def event_values(self, event_values):
        """Sets the event_values of this LifeCycleEventValue.


        :param event_values: The event_values of this LifeCycleEventValue.  # noqa: E501
        :type event_values: lusid.ResultValueDictionary
        """

        self._event_values = event_values

    @property
    def event_lineage(self):
        """Gets the event_lineage of this LifeCycleEventValue.  # noqa: E501


        :return: The event_lineage of this LifeCycleEventValue.  # noqa: E501
        :rtype: lusid.LifeCycleEventLineage
        """
        return self._event_lineage

    @event_lineage.setter
    def event_lineage(self, event_lineage):
        """Sets the event_lineage of this LifeCycleEventValue.


        :param event_lineage: The event_lineage of this LifeCycleEventValue.  # noqa: E501
        :type event_lineage: lusid.LifeCycleEventLineage
        """

        self._event_lineage = event_lineage

    @property
    def result_value_type(self):
        """Gets the result_value_type of this LifeCycleEventValue.  # noqa: E501

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :return: The result_value_type of this LifeCycleEventValue.  # noqa: E501
        :rtype: str
        """
        return self._result_value_type

    @result_value_type.setter
    def result_value_type(self, result_value_type):
        """Sets the result_value_type of this LifeCycleEventValue.

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :param result_value_type: The result_value_type of this LifeCycleEventValue.  # noqa: E501
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
        if not isinstance(other, LifeCycleEventValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LifeCycleEventValue):
            return True

        return self.to_dict() != other.to_dict()
