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


class SettlementCycle(object):
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
        'business_day_offset': 'int',
        'calendars': 'list[ResourceId]'
    }

    attribute_map = {
        'business_day_offset': 'businessDayOffset',
        'calendars': 'calendars'
    }

    required_map = {
        'business_day_offset': 'required',
        'calendars': 'required'
    }

    def __init__(self, business_day_offset=None, calendars=None, local_vars_configuration=None):  # noqa: E501
        """SettlementCycle - a model defined in OpenAPI"
        
        :param business_day_offset:  (required)
        :type business_day_offset: int
        :param calendars:  (required)
        :type calendars: list[lusid.ResourceId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._business_day_offset = None
        self._calendars = None
        self.discriminator = None

        self.business_day_offset = business_day_offset
        self.calendars = calendars

    @property
    def business_day_offset(self):
        """Gets the business_day_offset of this SettlementCycle.  # noqa: E501


        :return: The business_day_offset of this SettlementCycle.  # noqa: E501
        :rtype: int
        """
        return self._business_day_offset

    @business_day_offset.setter
    def business_day_offset(self, business_day_offset):
        """Sets the business_day_offset of this SettlementCycle.


        :param business_day_offset: The business_day_offset of this SettlementCycle.  # noqa: E501
        :type business_day_offset: int
        """
        if self.local_vars_configuration.client_side_validation and business_day_offset is None:  # noqa: E501
            raise ValueError("Invalid value for `business_day_offset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                business_day_offset is not None and business_day_offset > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `business_day_offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                business_day_offset is not None and business_day_offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `business_day_offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._business_day_offset = business_day_offset

    @property
    def calendars(self):
        """Gets the calendars of this SettlementCycle.  # noqa: E501


        :return: The calendars of this SettlementCycle.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._calendars

    @calendars.setter
    def calendars(self, calendars):
        """Sets the calendars of this SettlementCycle.


        :param calendars: The calendars of this SettlementCycle.  # noqa: E501
        :type calendars: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and calendars is None:  # noqa: E501
            raise ValueError("Invalid value for `calendars`, must not be `None`")  # noqa: E501

        self._calendars = calendars

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
        if not isinstance(other, SettlementCycle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettlementCycle):
            return True

        return self.to_dict() != other.to_dict()
