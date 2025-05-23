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


class CashElection(object):
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
        'election_key': 'str',
        'exchange_rate': 'float',
        'dividend_rate': 'float',
        'is_chosen': 'bool',
        'is_declared': 'bool',
        'is_default': 'bool',
        'dividend_currency': 'str'
    }

    attribute_map = {
        'election_key': 'electionKey',
        'exchange_rate': 'exchangeRate',
        'dividend_rate': 'dividendRate',
        'is_chosen': 'isChosen',
        'is_declared': 'isDeclared',
        'is_default': 'isDefault',
        'dividend_currency': 'dividendCurrency'
    }

    required_map = {
        'election_key': 'required',
        'exchange_rate': 'optional',
        'dividend_rate': 'optional',
        'is_chosen': 'optional',
        'is_declared': 'optional',
        'is_default': 'optional',
        'dividend_currency': 'required'
    }

    def __init__(self, election_key=None, exchange_rate=None, dividend_rate=None, is_chosen=None, is_declared=None, is_default=None, dividend_currency=None, local_vars_configuration=None):  # noqa: E501
        """CashElection - a model defined in OpenAPI"
        
        :param election_key:  Unique key used to identify this election. (required)
        :type election_key: str
        :param exchange_rate:  The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared.
        :type exchange_rate: float
        :param dividend_rate:  The payment rate for this CashElection.
        :type dividend_rate: float
        :param is_chosen:  Has this election been chosen.  Only one Election may be Chosen per Event.
        :type is_chosen: bool
        :param is_declared:  Is this the declared CashElection.  Only one Election may be Declared per Event.
        :type is_declared: bool
        :param is_default:  Is this election the default.  Only one Election may be Default per Event
        :type is_default: bool
        :param dividend_currency:  The payment currency for this CashElection. (required)
        :type dividend_currency: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._election_key = None
        self._exchange_rate = None
        self._dividend_rate = None
        self._is_chosen = None
        self._is_declared = None
        self._is_default = None
        self._dividend_currency = None
        self.discriminator = None

        self.election_key = election_key
        self.exchange_rate = exchange_rate
        self.dividend_rate = dividend_rate
        if is_chosen is not None:
            self.is_chosen = is_chosen
        if is_declared is not None:
            self.is_declared = is_declared
        if is_default is not None:
            self.is_default = is_default
        self.dividend_currency = dividend_currency

    @property
    def election_key(self):
        """Gets the election_key of this CashElection.  # noqa: E501

        Unique key used to identify this election.  # noqa: E501

        :return: The election_key of this CashElection.  # noqa: E501
        :rtype: str
        """
        return self._election_key

    @election_key.setter
    def election_key(self, election_key):
        """Sets the election_key of this CashElection.

        Unique key used to identify this election.  # noqa: E501

        :param election_key: The election_key of this CashElection.  # noqa: E501
        :type election_key: str
        """
        if self.local_vars_configuration.client_side_validation and election_key is None:  # noqa: E501
            raise ValueError("Invalid value for `election_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                election_key is not None and len(election_key) < 1):
            raise ValueError("Invalid value for `election_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._election_key = election_key

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this CashElection.  # noqa: E501

        The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared.  # noqa: E501

        :return: The exchange_rate of this CashElection.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this CashElection.

        The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared.  # noqa: E501

        :param exchange_rate: The exchange_rate of this CashElection.  # noqa: E501
        :type exchange_rate: float
        """

        self._exchange_rate = exchange_rate

    @property
    def dividend_rate(self):
        """Gets the dividend_rate of this CashElection.  # noqa: E501

        The payment rate for this CashElection.  # noqa: E501

        :return: The dividend_rate of this CashElection.  # noqa: E501
        :rtype: float
        """
        return self._dividend_rate

    @dividend_rate.setter
    def dividend_rate(self, dividend_rate):
        """Sets the dividend_rate of this CashElection.

        The payment rate for this CashElection.  # noqa: E501

        :param dividend_rate: The dividend_rate of this CashElection.  # noqa: E501
        :type dividend_rate: float
        """

        self._dividend_rate = dividend_rate

    @property
    def is_chosen(self):
        """Gets the is_chosen of this CashElection.  # noqa: E501

        Has this election been chosen.  Only one Election may be Chosen per Event.  # noqa: E501

        :return: The is_chosen of this CashElection.  # noqa: E501
        :rtype: bool
        """
        return self._is_chosen

    @is_chosen.setter
    def is_chosen(self, is_chosen):
        """Sets the is_chosen of this CashElection.

        Has this election been chosen.  Only one Election may be Chosen per Event.  # noqa: E501

        :param is_chosen: The is_chosen of this CashElection.  # noqa: E501
        :type is_chosen: bool
        """

        self._is_chosen = is_chosen

    @property
    def is_declared(self):
        """Gets the is_declared of this CashElection.  # noqa: E501

        Is this the declared CashElection.  Only one Election may be Declared per Event.  # noqa: E501

        :return: The is_declared of this CashElection.  # noqa: E501
        :rtype: bool
        """
        return self._is_declared

    @is_declared.setter
    def is_declared(self, is_declared):
        """Sets the is_declared of this CashElection.

        Is this the declared CashElection.  Only one Election may be Declared per Event.  # noqa: E501

        :param is_declared: The is_declared of this CashElection.  # noqa: E501
        :type is_declared: bool
        """

        self._is_declared = is_declared

    @property
    def is_default(self):
        """Gets the is_default of this CashElection.  # noqa: E501

        Is this election the default.  Only one Election may be Default per Event  # noqa: E501

        :return: The is_default of this CashElection.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CashElection.

        Is this election the default.  Only one Election may be Default per Event  # noqa: E501

        :param is_default: The is_default of this CashElection.  # noqa: E501
        :type is_default: bool
        """

        self._is_default = is_default

    @property
    def dividend_currency(self):
        """Gets the dividend_currency of this CashElection.  # noqa: E501

        The payment currency for this CashElection.  # noqa: E501

        :return: The dividend_currency of this CashElection.  # noqa: E501
        :rtype: str
        """
        return self._dividend_currency

    @dividend_currency.setter
    def dividend_currency(self, dividend_currency):
        """Sets the dividend_currency of this CashElection.

        The payment currency for this CashElection.  # noqa: E501

        :param dividend_currency: The dividend_currency of this CashElection.  # noqa: E501
        :type dividend_currency: str
        """
        if self.local_vars_configuration.client_side_validation and dividend_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `dividend_currency`, must not be `None`")  # noqa: E501

        self._dividend_currency = dividend_currency

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
        if not isinstance(other, CashElection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashElection):
            return True

        return self.to_dict() != other.to_dict()
