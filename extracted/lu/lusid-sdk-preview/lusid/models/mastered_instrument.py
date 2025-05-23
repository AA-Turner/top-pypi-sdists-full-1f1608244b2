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


class MasteredInstrument(object):
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
        'identifiers': 'dict(str, str)',
        'mastered_dom_ccy': 'str',
        'mastered_instrument_type': 'str',
        'mastered_lusid_instrument_id': 'str',
        'mastered_name': 'str',
        'mastered_scope': 'str',
        'mastered_asset_class': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'identifiers': 'identifiers',
        'mastered_dom_ccy': 'masteredDomCcy',
        'mastered_instrument_type': 'masteredInstrumentType',
        'mastered_lusid_instrument_id': 'masteredLusidInstrumentId',
        'mastered_name': 'masteredName',
        'mastered_scope': 'masteredScope',
        'mastered_asset_class': 'masteredAssetClass',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'identifiers': 'required',
        'mastered_dom_ccy': 'optional',
        'mastered_instrument_type': 'optional',
        'mastered_lusid_instrument_id': 'optional',
        'mastered_name': 'optional',
        'mastered_scope': 'optional',
        'mastered_asset_class': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, identifiers=None, mastered_dom_ccy=None, mastered_instrument_type=None, mastered_lusid_instrument_id=None, mastered_name=None, mastered_scope=None, mastered_asset_class=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """MasteredInstrument - a model defined in OpenAPI"
        
        :param identifiers:  Dictionary of identifiers of the mastered instrument (required)
        :type identifiers: dict(str, str)
        :param mastered_dom_ccy:  DomCcy of the Instrument that Mastered Instrument points to - read only field
        :type mastered_dom_ccy: str
        :param mastered_instrument_type:  Type of the Instrument that Mastered Instrument points to - read only field
        :type mastered_instrument_type: str
        :param mastered_lusid_instrument_id:  Luid of the Instrument that Mastered Instrument points to - read only field
        :type mastered_lusid_instrument_id: str
        :param mastered_name:  Name of the Instrument that Mastered Instrument points to - read only field
        :type mastered_name: str
        :param mastered_scope:  Scope of the Instrument that Mastered Instrument points to - read only field
        :type mastered_scope: str
        :param mastered_asset_class:  Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].
        :type mastered_asset_class: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifiers = None
        self._mastered_dom_ccy = None
        self._mastered_instrument_type = None
        self._mastered_lusid_instrument_id = None
        self._mastered_name = None
        self._mastered_scope = None
        self._mastered_asset_class = None
        self._instrument_type = None
        self.discriminator = None

        self.identifiers = identifiers
        self.mastered_dom_ccy = mastered_dom_ccy
        self.mastered_instrument_type = mastered_instrument_type
        self.mastered_lusid_instrument_id = mastered_lusid_instrument_id
        self.mastered_name = mastered_name
        self.mastered_scope = mastered_scope
        self.mastered_asset_class = mastered_asset_class
        self.instrument_type = instrument_type

    @property
    def identifiers(self):
        """Gets the identifiers of this MasteredInstrument.  # noqa: E501

        Dictionary of identifiers of the mastered instrument  # noqa: E501

        :return: The identifiers of this MasteredInstrument.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this MasteredInstrument.

        Dictionary of identifiers of the mastered instrument  # noqa: E501

        :param identifiers: The identifiers of this MasteredInstrument.  # noqa: E501
        :type identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def mastered_dom_ccy(self):
        """Gets the mastered_dom_ccy of this MasteredInstrument.  # noqa: E501

        DomCcy of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :return: The mastered_dom_ccy of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_dom_ccy

    @mastered_dom_ccy.setter
    def mastered_dom_ccy(self, mastered_dom_ccy):
        """Sets the mastered_dom_ccy of this MasteredInstrument.

        DomCcy of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :param mastered_dom_ccy: The mastered_dom_ccy of this MasteredInstrument.  # noqa: E501
        :type mastered_dom_ccy: str
        """

        self._mastered_dom_ccy = mastered_dom_ccy

    @property
    def mastered_instrument_type(self):
        """Gets the mastered_instrument_type of this MasteredInstrument.  # noqa: E501

        Type of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :return: The mastered_instrument_type of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_instrument_type

    @mastered_instrument_type.setter
    def mastered_instrument_type(self, mastered_instrument_type):
        """Sets the mastered_instrument_type of this MasteredInstrument.

        Type of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :param mastered_instrument_type: The mastered_instrument_type of this MasteredInstrument.  # noqa: E501
        :type mastered_instrument_type: str
        """

        self._mastered_instrument_type = mastered_instrument_type

    @property
    def mastered_lusid_instrument_id(self):
        """Gets the mastered_lusid_instrument_id of this MasteredInstrument.  # noqa: E501

        Luid of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :return: The mastered_lusid_instrument_id of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_lusid_instrument_id

    @mastered_lusid_instrument_id.setter
    def mastered_lusid_instrument_id(self, mastered_lusid_instrument_id):
        """Sets the mastered_lusid_instrument_id of this MasteredInstrument.

        Luid of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :param mastered_lusid_instrument_id: The mastered_lusid_instrument_id of this MasteredInstrument.  # noqa: E501
        :type mastered_lusid_instrument_id: str
        """

        self._mastered_lusid_instrument_id = mastered_lusid_instrument_id

    @property
    def mastered_name(self):
        """Gets the mastered_name of this MasteredInstrument.  # noqa: E501

        Name of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :return: The mastered_name of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_name

    @mastered_name.setter
    def mastered_name(self, mastered_name):
        """Sets the mastered_name of this MasteredInstrument.

        Name of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :param mastered_name: The mastered_name of this MasteredInstrument.  # noqa: E501
        :type mastered_name: str
        """

        self._mastered_name = mastered_name

    @property
    def mastered_scope(self):
        """Gets the mastered_scope of this MasteredInstrument.  # noqa: E501

        Scope of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :return: The mastered_scope of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_scope

    @mastered_scope.setter
    def mastered_scope(self, mastered_scope):
        """Sets the mastered_scope of this MasteredInstrument.

        Scope of the Instrument that Mastered Instrument points to - read only field  # noqa: E501

        :param mastered_scope: The mastered_scope of this MasteredInstrument.  # noqa: E501
        :type mastered_scope: str
        """

        self._mastered_scope = mastered_scope

    @property
    def mastered_asset_class(self):
        """Gets the mastered_asset_class of this MasteredInstrument.  # noqa: E501

        Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  # noqa: E501

        :return: The mastered_asset_class of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._mastered_asset_class

    @mastered_asset_class.setter
    def mastered_asset_class(self, mastered_asset_class):
        """Sets the mastered_asset_class of this MasteredInstrument.

        Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  # noqa: E501

        :param mastered_asset_class: The mastered_asset_class of this MasteredInstrument.  # noqa: E501
        :type mastered_asset_class: str
        """

        self._mastered_asset_class = mastered_asset_class

    @property
    def instrument_type(self):
        """Gets the instrument_type of this MasteredInstrument.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :return: The instrument_type of this MasteredInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this MasteredInstrument.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :param instrument_type: The instrument_type of this MasteredInstrument.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan", "TotalReturnSwap", "InflationLeg", "FundShareClass", "FlexibleLoan", "UnsettledCash", "Cash", "MasteredInstrument", "LoanFacility"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, MasteredInstrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MasteredInstrument):
            return True

        return self.to_dict() != other.to_dict()
