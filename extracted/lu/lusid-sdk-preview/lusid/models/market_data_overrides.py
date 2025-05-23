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


class MarketDataOverrides(object):
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
        'complex_market_data': 'list[EconomicDependencyWithComplexMarketData]',
        'quotes': 'list[EconomicDependencyWithQuote]'
    }

    attribute_map = {
        'complex_market_data': 'complexMarketData',
        'quotes': 'quotes'
    }

    required_map = {
        'complex_market_data': 'optional',
        'quotes': 'optional'
    }

    def __init__(self, complex_market_data=None, quotes=None, local_vars_configuration=None):  # noqa: E501
        """MarketDataOverrides - a model defined in OpenAPI"
        
        :param complex_market_data:  A list of EconomicDependency paired with quote data satisfying that economic dependency
        :type complex_market_data: list[lusid.EconomicDependencyWithComplexMarketData]
        :param quotes:  A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency
        :type quotes: list[lusid.EconomicDependencyWithQuote]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._complex_market_data = None
        self._quotes = None
        self.discriminator = None

        self.complex_market_data = complex_market_data
        self.quotes = quotes

    @property
    def complex_market_data(self):
        """Gets the complex_market_data of this MarketDataOverrides.  # noqa: E501

        A list of EconomicDependency paired with quote data satisfying that economic dependency  # noqa: E501

        :return: The complex_market_data of this MarketDataOverrides.  # noqa: E501
        :rtype: list[lusid.EconomicDependencyWithComplexMarketData]
        """
        return self._complex_market_data

    @complex_market_data.setter
    def complex_market_data(self, complex_market_data):
        """Sets the complex_market_data of this MarketDataOverrides.

        A list of EconomicDependency paired with quote data satisfying that economic dependency  # noqa: E501

        :param complex_market_data: The complex_market_data of this MarketDataOverrides.  # noqa: E501
        :type complex_market_data: list[lusid.EconomicDependencyWithComplexMarketData]
        """

        self._complex_market_data = complex_market_data

    @property
    def quotes(self):
        """Gets the quotes of this MarketDataOverrides.  # noqa: E501

        A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency  # noqa: E501

        :return: The quotes of this MarketDataOverrides.  # noqa: E501
        :rtype: list[lusid.EconomicDependencyWithQuote]
        """
        return self._quotes

    @quotes.setter
    def quotes(self, quotes):
        """Sets the quotes of this MarketDataOverrides.

        A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency  # noqa: E501

        :param quotes: The quotes of this MarketDataOverrides.  # noqa: E501
        :type quotes: list[lusid.EconomicDependencyWithQuote]
        """

        self._quotes = quotes

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
        if not isinstance(other, MarketDataOverrides):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketDataOverrides):
            return True

        return self.to_dict() != other.to_dict()
