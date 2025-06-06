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


class ComplexMarketDataId(object):
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
        'provider': 'str',
        'price_source': 'str',
        'lineage': 'str',
        'effective_at': 'str',
        'market_asset': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'price_source': 'priceSource',
        'lineage': 'lineage',
        'effective_at': 'effectiveAt',
        'market_asset': 'marketAsset'
    }

    required_map = {
        'provider': 'required',
        'price_source': 'optional',
        'lineage': 'optional',
        'effective_at': 'optional',
        'market_asset': 'required'
    }

    def __init__(self, provider=None, price_source=None, lineage=None, effective_at=None, market_asset=None, local_vars_configuration=None):  # noqa: E501
        """ComplexMarketDataId - a model defined in OpenAPI"
        
        :param provider:  The platform or vendor that provided the complex market data, e.g. 'DataScope', 'LUSID', etc. (required)
        :type provider: str
        :param price_source:  The source or originator of the complex market data, e.g. a bank or financial institution.
        :type price_source: str
        :param lineage:  This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class.
        :type lineage: str
        :param effective_at:  The effectiveAt or cut label that this item of complex market data is/was updated/inserted with.
        :type effective_at: str
        :param market_asset:  The name of the market entity that the document represents (required)
        :type market_asset: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._provider = None
        self._price_source = None
        self._lineage = None
        self._effective_at = None
        self._market_asset = None
        self.discriminator = None

        self.provider = provider
        self.price_source = price_source
        self.lineage = lineage
        self.effective_at = effective_at
        self.market_asset = market_asset

    @property
    def provider(self):
        """Gets the provider of this ComplexMarketDataId.  # noqa: E501

        The platform or vendor that provided the complex market data, e.g. 'DataScope', 'LUSID', etc.  # noqa: E501

        :return: The provider of this ComplexMarketDataId.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ComplexMarketDataId.

        The platform or vendor that provided the complex market data, e.g. 'DataScope', 'LUSID', etc.  # noqa: E501

        :param provider: The provider of this ComplexMarketDataId.  # noqa: E501
        :type provider: str
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                provider is not None and len(provider) > 32):
            raise ValueError("Invalid value for `provider`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                provider is not None and len(provider) < 0):
            raise ValueError("Invalid value for `provider`, length must be greater than or equal to `0`")  # noqa: E501

        self._provider = provider

    @property
    def price_source(self):
        """Gets the price_source of this ComplexMarketDataId.  # noqa: E501

        The source or originator of the complex market data, e.g. a bank or financial institution.  # noqa: E501

        :return: The price_source of this ComplexMarketDataId.  # noqa: E501
        :rtype: str
        """
        return self._price_source

    @price_source.setter
    def price_source(self, price_source):
        """Sets the price_source of this ComplexMarketDataId.

        The source or originator of the complex market data, e.g. a bank or financial institution.  # noqa: E501

        :param price_source: The price_source of this ComplexMarketDataId.  # noqa: E501
        :type price_source: str
        """
        if (self.local_vars_configuration.client_side_validation and
                price_source is not None and len(price_source) > 256):
            raise ValueError("Invalid value for `price_source`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                price_source is not None and len(price_source) < 0):
            raise ValueError("Invalid value for `price_source`, length must be greater than or equal to `0`")  # noqa: E501

        self._price_source = price_source

    @property
    def lineage(self):
        """Gets the lineage of this ComplexMarketDataId.  # noqa: E501

        This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class.  # noqa: E501

        :return: The lineage of this ComplexMarketDataId.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this ComplexMarketDataId.

        This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class.  # noqa: E501

        :param lineage: The lineage of this ComplexMarketDataId.  # noqa: E501
        :type lineage: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) > 1024):
            raise ValueError("Invalid value for `lineage`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) < 0):
            raise ValueError("Invalid value for `lineage`, length must be greater than or equal to `0`")  # noqa: E501

        self._lineage = lineage

    @property
    def effective_at(self):
        """Gets the effective_at of this ComplexMarketDataId.  # noqa: E501

        The effectiveAt or cut label that this item of complex market data is/was updated/inserted with.  # noqa: E501

        :return: The effective_at of this ComplexMarketDataId.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this ComplexMarketDataId.

        The effectiveAt or cut label that this item of complex market data is/was updated/inserted with.  # noqa: E501

        :param effective_at: The effective_at of this ComplexMarketDataId.  # noqa: E501
        :type effective_at: str
        """

        self._effective_at = effective_at

    @property
    def market_asset(self):
        """Gets the market_asset of this ComplexMarketDataId.  # noqa: E501

        The name of the market entity that the document represents  # noqa: E501

        :return: The market_asset of this ComplexMarketDataId.  # noqa: E501
        :rtype: str
        """
        return self._market_asset

    @market_asset.setter
    def market_asset(self, market_asset):
        """Sets the market_asset of this ComplexMarketDataId.

        The name of the market entity that the document represents  # noqa: E501

        :param market_asset: The market_asset of this ComplexMarketDataId.  # noqa: E501
        :type market_asset: str
        """
        if self.local_vars_configuration.client_side_validation and market_asset is None:  # noqa: E501
            raise ValueError("Invalid value for `market_asset`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                market_asset is not None and len(market_asset) > 256):
            raise ValueError("Invalid value for `market_asset`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                market_asset is not None and len(market_asset) < 0):
            raise ValueError("Invalid value for `market_asset`, length must be greater than or equal to `0`")  # noqa: E501

        self._market_asset = market_asset

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
        if not isinstance(other, ComplexMarketDataId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplexMarketDataId):
            return True

        return self.to_dict() != other.to_dict()
