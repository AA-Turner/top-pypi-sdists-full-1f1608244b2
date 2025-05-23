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


class CalendarDependency(object):
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
        'calendars': 'list[str]',
        'dependency_type': 'str'
    }

    attribute_map = {
        'calendars': 'calendars',
        'dependency_type': 'dependencyType'
    }

    required_map = {
        'calendars': 'required',
        'dependency_type': 'required'
    }

    def __init__(self, calendars=None, dependency_type=None, local_vars_configuration=None):  # noqa: E501
        """CalendarDependency - a model defined in OpenAPI"
        
        :param calendars:  The Codes of the calendars that are depended upon. (required)
        :type calendars: list[str]
        :param dependency_type:  The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency (required)
        :type dependency_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._calendars = None
        self._dependency_type = None
        self.discriminator = None

        self.calendars = calendars
        self.dependency_type = dependency_type

    @property
    def calendars(self):
        """Gets the calendars of this CalendarDependency.  # noqa: E501

        The Codes of the calendars that are depended upon.  # noqa: E501

        :return: The calendars of this CalendarDependency.  # noqa: E501
        :rtype: list[str]
        """
        return self._calendars

    @calendars.setter
    def calendars(self, calendars):
        """Sets the calendars of this CalendarDependency.

        The Codes of the calendars that are depended upon.  # noqa: E501

        :param calendars: The calendars of this CalendarDependency.  # noqa: E501
        :type calendars: list[str]
        """
        if self.local_vars_configuration.client_side_validation and calendars is None:  # noqa: E501
            raise ValueError("Invalid value for `calendars`, must not be `None`")  # noqa: E501

        self._calendars = calendars

    @property
    def dependency_type(self):
        """Gets the dependency_type of this CalendarDependency.  # noqa: E501

        The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency  # noqa: E501

        :return: The dependency_type of this CalendarDependency.  # noqa: E501
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this CalendarDependency.

        The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency  # noqa: E501

        :param dependency_type: The dependency_type of this CalendarDependency.  # noqa: E501
        :type dependency_type: str
        """
        if self.local_vars_configuration.client_side_validation and dependency_type is None:  # noqa: E501
            raise ValueError("Invalid value for `dependency_type`, must not be `None`")  # noqa: E501
        allowed_values = ["OpaqueDependency", "CashDependency", "DiscountingDependency", "EquityCurveDependency", "EquityVolDependency", "FxDependency", "FxForwardsDependency", "FxVolDependency", "IndexProjectionDependency", "IrVolDependency", "QuoteDependency", "Vendor", "CalendarDependency", "InflationFixingDependency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dependency_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dependency_type, allowed_values)
            )

        self._dependency_type = dependency_type

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
        if not isinstance(other, CalendarDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalendarDependency):
            return True

        return self.to_dict() != other.to_dict()
