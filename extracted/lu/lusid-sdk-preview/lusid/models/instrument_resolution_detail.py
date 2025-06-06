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


class InstrumentResolutionDetail(object):
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
        'instrument_identifiers': 'dict(str, str)',
        'lusid_instrument_id': 'str',
        'instrument_scope': 'str',
        'launch_price': 'float',
        'launch_date': 'datetime'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'lusid_instrument_id': 'lusidInstrumentId',
        'instrument_scope': 'instrumentScope',
        'launch_price': 'launchPrice',
        'launch_date': 'launchDate'
    }

    required_map = {
        'instrument_identifiers': 'required',
        'lusid_instrument_id': 'optional',
        'instrument_scope': 'optional',
        'launch_price': 'optional',
        'launch_date': 'optional'
    }

    def __init__(self, instrument_identifiers=None, lusid_instrument_id=None, instrument_scope=None, launch_price=None, launch_date=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentResolutionDetail - a model defined in OpenAPI"
        
        :param instrument_identifiers:  Unique instrument identifiers (required)
        :type instrument_identifiers: dict(str, str)
        :param lusid_instrument_id:  LUSID's internal unique instrument identifier, resolved from the instrument identifiers
        :type lusid_instrument_id: str
        :param instrument_scope:  The scope in which the instrument lies.
        :type instrument_scope: str
        :param launch_price:  The launch price set when a shareclass is added to the fund. Defaults to 1.
        :type launch_price: float
        :param launch_date:  The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date.
        :type launch_date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_identifiers = None
        self._lusid_instrument_id = None
        self._instrument_scope = None
        self._launch_price = None
        self._launch_date = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.lusid_instrument_id = lusid_instrument_id
        self.instrument_scope = instrument_scope
        self.launch_price = launch_price
        self.launch_date = launch_date

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this InstrumentResolutionDetail.  # noqa: E501

        Unique instrument identifiers  # noqa: E501

        :return: The instrument_identifiers of this InstrumentResolutionDetail.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this InstrumentResolutionDetail.

        Unique instrument identifiers  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this InstrumentResolutionDetail.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this InstrumentResolutionDetail.  # noqa: E501

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :return: The lusid_instrument_id of this InstrumentResolutionDetail.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this InstrumentResolutionDetail.

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this InstrumentResolutionDetail.  # noqa: E501
        :type lusid_instrument_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lusid_instrument_id is not None and len(lusid_instrument_id) > 64):
            raise ValueError("Invalid value for `lusid_instrument_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lusid_instrument_id is not None and len(lusid_instrument_id) < 1):
            raise ValueError("Invalid value for `lusid_instrument_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lusid_instrument_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', lusid_instrument_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `lusid_instrument_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this InstrumentResolutionDetail.  # noqa: E501

        The scope in which the instrument lies.  # noqa: E501

        :return: The instrument_scope of this InstrumentResolutionDetail.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this InstrumentResolutionDetail.

        The scope in which the instrument lies.  # noqa: E501

        :param instrument_scope: The instrument_scope of this InstrumentResolutionDetail.  # noqa: E501
        :type instrument_scope: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) > 64):
            raise ValueError("Invalid value for `instrument_scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) < 1):
            raise ValueError("Invalid value for `instrument_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', instrument_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `instrument_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._instrument_scope = instrument_scope

    @property
    def launch_price(self):
        """Gets the launch_price of this InstrumentResolutionDetail.  # noqa: E501

        The launch price set when a shareclass is added to the fund. Defaults to 1.  # noqa: E501

        :return: The launch_price of this InstrumentResolutionDetail.  # noqa: E501
        :rtype: float
        """
        return self._launch_price

    @launch_price.setter
    def launch_price(self, launch_price):
        """Sets the launch_price of this InstrumentResolutionDetail.

        The launch price set when a shareclass is added to the fund. Defaults to 1.  # noqa: E501

        :param launch_price: The launch_price of this InstrumentResolutionDetail.  # noqa: E501
        :type launch_price: float
        """

        self._launch_price = launch_price

    @property
    def launch_date(self):
        """Gets the launch_date of this InstrumentResolutionDetail.  # noqa: E501

        The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date.  # noqa: E501

        :return: The launch_date of this InstrumentResolutionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._launch_date

    @launch_date.setter
    def launch_date(self, launch_date):
        """Sets the launch_date of this InstrumentResolutionDetail.

        The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date.  # noqa: E501

        :param launch_date: The launch_date of this InstrumentResolutionDetail.  # noqa: E501
        :type launch_date: datetime
        """

        self._launch_date = launch_date

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
        if not isinstance(other, InstrumentResolutionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentResolutionDetail):
            return True

        return self.to_dict() != other.to_dict()
