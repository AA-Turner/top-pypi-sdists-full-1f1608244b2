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


class FloatingLegAllOf(object):
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
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'leg_definition': 'LegDefinition',
        'notional': 'float',
        'overrides': 'FixedLegAllOfOverrides',
        'cap_rate': 'float',
        'floor_rate': 'float',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'leg_definition': 'legDefinition',
        'notional': 'notional',
        'overrides': 'overrides',
        'cap_rate': 'capRate',
        'floor_rate': 'floorRate',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'leg_definition': 'required',
        'notional': 'required',
        'overrides': 'optional',
        'cap_rate': 'optional',
        'floor_rate': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, leg_definition=None, notional=None, overrides=None, cap_rate=None, floor_rate=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """FloatingLegAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param leg_definition:  (required)
        :type leg_definition: lusid.LegDefinition
        :param notional:  Scaling factor to apply to leg quantities. (required)
        :type notional: float
        :param overrides: 
        :type overrides: lusid.FixedLegAllOfOverrides
        :param cap_rate:  The maximum floating rate which a cashflow can accrue.
        :type cap_rate: float
        :param floor_rate:  The minimum floating rate which a cashflow can accrue.
        :type floor_rate: float
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._leg_definition = None
        self._notional = None
        self._overrides = None
        self._cap_rate = None
        self._floor_rate = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.leg_definition = leg_definition
        self.notional = notional
        self.overrides = overrides
        self.cap_rate = cap_rate
        self.floor_rate = floor_rate
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this FloatingLegAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this FloatingLegAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FloatingLegAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this FloatingLegAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this FloatingLegAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this FloatingLegAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this FloatingLegAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this FloatingLegAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def leg_definition(self):
        """Gets the leg_definition of this FloatingLegAllOf.  # noqa: E501


        :return: The leg_definition of this FloatingLegAllOf.  # noqa: E501
        :rtype: lusid.LegDefinition
        """
        return self._leg_definition

    @leg_definition.setter
    def leg_definition(self, leg_definition):
        """Sets the leg_definition of this FloatingLegAllOf.


        :param leg_definition: The leg_definition of this FloatingLegAllOf.  # noqa: E501
        :type leg_definition: lusid.LegDefinition
        """
        if self.local_vars_configuration.client_side_validation and leg_definition is None:  # noqa: E501
            raise ValueError("Invalid value for `leg_definition`, must not be `None`")  # noqa: E501

        self._leg_definition = leg_definition

    @property
    def notional(self):
        """Gets the notional of this FloatingLegAllOf.  # noqa: E501

        Scaling factor to apply to leg quantities.  # noqa: E501

        :return: The notional of this FloatingLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._notional

    @notional.setter
    def notional(self, notional):
        """Sets the notional of this FloatingLegAllOf.

        Scaling factor to apply to leg quantities.  # noqa: E501

        :param notional: The notional of this FloatingLegAllOf.  # noqa: E501
        :type notional: float
        """
        if self.local_vars_configuration.client_side_validation and notional is None:  # noqa: E501
            raise ValueError("Invalid value for `notional`, must not be `None`")  # noqa: E501

        self._notional = notional

    @property
    def overrides(self):
        """Gets the overrides of this FloatingLegAllOf.  # noqa: E501


        :return: The overrides of this FloatingLegAllOf.  # noqa: E501
        :rtype: lusid.FixedLegAllOfOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this FloatingLegAllOf.


        :param overrides: The overrides of this FloatingLegAllOf.  # noqa: E501
        :type overrides: lusid.FixedLegAllOfOverrides
        """

        self._overrides = overrides

    @property
    def cap_rate(self):
        """Gets the cap_rate of this FloatingLegAllOf.  # noqa: E501

        The maximum floating rate which a cashflow can accrue.  # noqa: E501

        :return: The cap_rate of this FloatingLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._cap_rate

    @cap_rate.setter
    def cap_rate(self, cap_rate):
        """Sets the cap_rate of this FloatingLegAllOf.

        The maximum floating rate which a cashflow can accrue.  # noqa: E501

        :param cap_rate: The cap_rate of this FloatingLegAllOf.  # noqa: E501
        :type cap_rate: float
        """

        self._cap_rate = cap_rate

    @property
    def floor_rate(self):
        """Gets the floor_rate of this FloatingLegAllOf.  # noqa: E501

        The minimum floating rate which a cashflow can accrue.  # noqa: E501

        :return: The floor_rate of this FloatingLegAllOf.  # noqa: E501
        :rtype: float
        """
        return self._floor_rate

    @floor_rate.setter
    def floor_rate(self, floor_rate):
        """Sets the floor_rate of this FloatingLegAllOf.

        The minimum floating rate which a cashflow can accrue.  # noqa: E501

        :param floor_rate: The floor_rate of this FloatingLegAllOf.  # noqa: E501
        :type floor_rate: float
        """

        self._floor_rate = floor_rate

    @property
    def instrument_type(self):
        """Gets the instrument_type of this FloatingLegAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :return: The instrument_type of this FloatingLegAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this FloatingLegAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :param instrument_type: The instrument_type of this FloatingLegAllOf.  # noqa: E501
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
        if not isinstance(other, FloatingLegAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FloatingLegAllOf):
            return True

        return self.to_dict() != other.to_dict()
