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


class InterestRateSwap(object):
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
        'is_non_deliverable': 'bool',
        'legs': 'list[InstrumentLeg]',
        'settlement_ccy': 'str',
        'additional_payments': 'list[AdditionalPayment]',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'is_non_deliverable': 'isNonDeliverable',
        'legs': 'legs',
        'settlement_ccy': 'settlementCcy',
        'additional_payments': 'additionalPayments',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'is_non_deliverable': 'optional',
        'legs': 'required',
        'settlement_ccy': 'optional',
        'additional_payments': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, is_non_deliverable=None, legs=None, settlement_ccy=None, additional_payments=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """InterestRateSwap - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param is_non_deliverable:  Is the contract an IRS of \"Non-Deliverable\" type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates.
        :type is_non_deliverable: bool
        :param legs:  The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg. (required)
        :type legs: list[lusid.InstrumentLeg]
        :param settlement_ccy:  Settlement currency if IRS is non-deliverable.
        :type settlement_ccy: str
        :param additional_payments:  Optional additional payments at a given date e.g. to level off an uneven fixed-floating swap.  The dates must be distinct and either all payments are Pay or all payments are receive
        :type additional_payments: list[lusid.AdditionalPayment]
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._is_non_deliverable = None
        self._legs = None
        self._settlement_ccy = None
        self._additional_payments = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        if is_non_deliverable is not None:
            self.is_non_deliverable = is_non_deliverable
        self.legs = legs
        self.settlement_ccy = settlement_ccy
        self.additional_payments = additional_payments
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this InterestRateSwap.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this InterestRateSwap.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InterestRateSwap.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this InterestRateSwap.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this InterestRateSwap.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this InterestRateSwap.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this InterestRateSwap.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this InterestRateSwap.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def is_non_deliverable(self):
        """Gets the is_non_deliverable of this InterestRateSwap.  # noqa: E501

        Is the contract an IRS of \"Non-Deliverable\" type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates.  # noqa: E501

        :return: The is_non_deliverable of this InterestRateSwap.  # noqa: E501
        :rtype: bool
        """
        return self._is_non_deliverable

    @is_non_deliverable.setter
    def is_non_deliverable(self, is_non_deliverable):
        """Sets the is_non_deliverable of this InterestRateSwap.

        Is the contract an IRS of \"Non-Deliverable\" type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates.  # noqa: E501

        :param is_non_deliverable: The is_non_deliverable of this InterestRateSwap.  # noqa: E501
        :type is_non_deliverable: bool
        """

        self._is_non_deliverable = is_non_deliverable

    @property
    def legs(self):
        """Gets the legs of this InterestRateSwap.  # noqa: E501

        The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg.  # noqa: E501

        :return: The legs of this InterestRateSwap.  # noqa: E501
        :rtype: list[lusid.InstrumentLeg]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this InterestRateSwap.

        The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg.  # noqa: E501

        :param legs: The legs of this InterestRateSwap.  # noqa: E501
        :type legs: list[lusid.InstrumentLeg]
        """
        if self.local_vars_configuration.client_side_validation and legs is None:  # noqa: E501
            raise ValueError("Invalid value for `legs`, must not be `None`")  # noqa: E501

        self._legs = legs

    @property
    def settlement_ccy(self):
        """Gets the settlement_ccy of this InterestRateSwap.  # noqa: E501

        Settlement currency if IRS is non-deliverable.  # noqa: E501

        :return: The settlement_ccy of this InterestRateSwap.  # noqa: E501
        :rtype: str
        """
        return self._settlement_ccy

    @settlement_ccy.setter
    def settlement_ccy(self, settlement_ccy):
        """Sets the settlement_ccy of this InterestRateSwap.

        Settlement currency if IRS is non-deliverable.  # noqa: E501

        :param settlement_ccy: The settlement_ccy of this InterestRateSwap.  # noqa: E501
        :type settlement_ccy: str
        """

        self._settlement_ccy = settlement_ccy

    @property
    def additional_payments(self):
        """Gets the additional_payments of this InterestRateSwap.  # noqa: E501

        Optional additional payments at a given date e.g. to level off an uneven fixed-floating swap.  The dates must be distinct and either all payments are Pay or all payments are receive  # noqa: E501

        :return: The additional_payments of this InterestRateSwap.  # noqa: E501
        :rtype: list[lusid.AdditionalPayment]
        """
        return self._additional_payments

    @additional_payments.setter
    def additional_payments(self, additional_payments):
        """Sets the additional_payments of this InterestRateSwap.

        Optional additional payments at a given date e.g. to level off an uneven fixed-floating swap.  The dates must be distinct and either all payments are Pay or all payments are receive  # noqa: E501

        :param additional_payments: The additional_payments of this InterestRateSwap.  # noqa: E501
        :type additional_payments: list[lusid.AdditionalPayment]
        """

        self._additional_payments = additional_payments

    @property
    def instrument_type(self):
        """Gets the instrument_type of this InterestRateSwap.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :return: The instrument_type of this InterestRateSwap.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this InterestRateSwap.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility  # noqa: E501

        :param instrument_type: The instrument_type of this InterestRateSwap.  # noqa: E501
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
        if not isinstance(other, InterestRateSwap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InterestRateSwap):
            return True

        return self.to_dict() != other.to_dict()
