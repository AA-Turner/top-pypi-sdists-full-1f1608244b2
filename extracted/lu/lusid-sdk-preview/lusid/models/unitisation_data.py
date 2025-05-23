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


class UnitisationData(object):
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
        'shares_in_issue': 'float',
        'unit_price': 'float',
        'net_dealing_units': 'float'
    }

    attribute_map = {
        'shares_in_issue': 'sharesInIssue',
        'unit_price': 'unitPrice',
        'net_dealing_units': 'netDealingUnits'
    }

    required_map = {
        'shares_in_issue': 'required',
        'unit_price': 'required',
        'net_dealing_units': 'required'
    }

    def __init__(self, shares_in_issue=None, unit_price=None, net_dealing_units=None, local_vars_configuration=None):  # noqa: E501
        """UnitisationData - a model defined in OpenAPI"
        
        :param shares_in_issue:  The number of shares in issue at a valuation point. (required)
        :type shares_in_issue: float
        :param unit_price:  The price of one unit of the share class at a valuation point. (required)
        :type unit_price: float
        :param net_dealing_units:  The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). (required)
        :type net_dealing_units: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._shares_in_issue = None
        self._unit_price = None
        self._net_dealing_units = None
        self.discriminator = None

        self.shares_in_issue = shares_in_issue
        self.unit_price = unit_price
        self.net_dealing_units = net_dealing_units

    @property
    def shares_in_issue(self):
        """Gets the shares_in_issue of this UnitisationData.  # noqa: E501

        The number of shares in issue at a valuation point.  # noqa: E501

        :return: The shares_in_issue of this UnitisationData.  # noqa: E501
        :rtype: float
        """
        return self._shares_in_issue

    @shares_in_issue.setter
    def shares_in_issue(self, shares_in_issue):
        """Sets the shares_in_issue of this UnitisationData.

        The number of shares in issue at a valuation point.  # noqa: E501

        :param shares_in_issue: The shares_in_issue of this UnitisationData.  # noqa: E501
        :type shares_in_issue: float
        """
        if self.local_vars_configuration.client_side_validation and shares_in_issue is None:  # noqa: E501
            raise ValueError("Invalid value for `shares_in_issue`, must not be `None`")  # noqa: E501

        self._shares_in_issue = shares_in_issue

    @property
    def unit_price(self):
        """Gets the unit_price of this UnitisationData.  # noqa: E501

        The price of one unit of the share class at a valuation point.  # noqa: E501

        :return: The unit_price of this UnitisationData.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this UnitisationData.

        The price of one unit of the share class at a valuation point.  # noqa: E501

        :param unit_price: The unit_price of this UnitisationData.  # noqa: E501
        :type unit_price: float
        """
        if self.local_vars_configuration.client_side_validation and unit_price is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def net_dealing_units(self):
        """Gets the net_dealing_units of this UnitisationData.  # noqa: E501

        The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units).  # noqa: E501

        :return: The net_dealing_units of this UnitisationData.  # noqa: E501
        :rtype: float
        """
        return self._net_dealing_units

    @net_dealing_units.setter
    def net_dealing_units(self, net_dealing_units):
        """Sets the net_dealing_units of this UnitisationData.

        The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units).  # noqa: E501

        :param net_dealing_units: The net_dealing_units of this UnitisationData.  # noqa: E501
        :type net_dealing_units: float
        """
        if self.local_vars_configuration.client_side_validation and net_dealing_units is None:  # noqa: E501
            raise ValueError("Invalid value for `net_dealing_units`, must not be `None`")  # noqa: E501

        self._net_dealing_units = net_dealing_units

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
        if not isinstance(other, UnitisationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnitisationData):
            return True

        return self.to_dict() != other.to_dict()
