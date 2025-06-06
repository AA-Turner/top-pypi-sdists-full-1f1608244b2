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


class DividendOptionEvent(object):
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
        'announcement_date': 'datetime',
        'cash_elections': 'list[CashElection]',
        'ex_date': 'datetime',
        'payment_date': 'datetime',
        'record_date': 'datetime',
        'security_elections': 'list[SecurityElection]',
        'security_settlement_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'announcement_date': 'announcementDate',
        'cash_elections': 'cashElections',
        'ex_date': 'exDate',
        'payment_date': 'paymentDate',
        'record_date': 'recordDate',
        'security_elections': 'securityElections',
        'security_settlement_date': 'securitySettlementDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'announcement_date': 'optional',
        'cash_elections': 'required',
        'ex_date': 'required',
        'payment_date': 'required',
        'record_date': 'optional',
        'security_elections': 'required',
        'security_settlement_date': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, announcement_date=None, cash_elections=None, ex_date=None, payment_date=None, record_date=None, security_elections=None, security_settlement_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """DividendOptionEvent - a model defined in OpenAPI"
        
        :param announcement_date:  Date on which the dividend was announced / declared.
        :type announcement_date: datetime
        :param cash_elections:  CashElection for this DividendReinvestmentEvent (required)
        :type cash_elections: list[lusid.CashElection]
        :param ex_date:  The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. (required)
        :type ex_date: datetime
        :param payment_date:  The date the company pays out dividends to shareholders. (required)
        :type payment_date: datetime
        :param record_date:  Date you have to be the holder of record in order to participate in the tender.
        :type record_date: datetime
        :param security_elections:  SecurityElection for this DividendReinvestmentEvent (required)
        :type security_elections: list[lusid.SecurityElection]
        :param security_settlement_date:  The settlement date of the additional units.  Equal to the PaymentDate if not provided.
        :type security_settlement_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._announcement_date = None
        self._cash_elections = None
        self._ex_date = None
        self._payment_date = None
        self._record_date = None
        self._security_elections = None
        self._security_settlement_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.announcement_date = announcement_date
        self.cash_elections = cash_elections
        self.ex_date = ex_date
        self.payment_date = payment_date
        self.record_date = record_date
        self.security_elections = security_elections
        if security_settlement_date is not None:
            self.security_settlement_date = security_settlement_date
        self.instrument_event_type = instrument_event_type

    @property
    def announcement_date(self):
        """Gets the announcement_date of this DividendOptionEvent.  # noqa: E501

        Date on which the dividend was announced / declared.  # noqa: E501

        :return: The announcement_date of this DividendOptionEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this DividendOptionEvent.

        Date on which the dividend was announced / declared.  # noqa: E501

        :param announcement_date: The announcement_date of this DividendOptionEvent.  # noqa: E501
        :type announcement_date: datetime
        """

        self._announcement_date = announcement_date

    @property
    def cash_elections(self):
        """Gets the cash_elections of this DividendOptionEvent.  # noqa: E501

        CashElection for this DividendReinvestmentEvent  # noqa: E501

        :return: The cash_elections of this DividendOptionEvent.  # noqa: E501
        :rtype: list[lusid.CashElection]
        """
        return self._cash_elections

    @cash_elections.setter
    def cash_elections(self, cash_elections):
        """Sets the cash_elections of this DividendOptionEvent.

        CashElection for this DividendReinvestmentEvent  # noqa: E501

        :param cash_elections: The cash_elections of this DividendOptionEvent.  # noqa: E501
        :type cash_elections: list[lusid.CashElection]
        """
        if self.local_vars_configuration.client_side_validation and cash_elections is None:  # noqa: E501
            raise ValueError("Invalid value for `cash_elections`, must not be `None`")  # noqa: E501

        self._cash_elections = cash_elections

    @property
    def ex_date(self):
        """Gets the ex_date of this DividendOptionEvent.  # noqa: E501

        The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.  # noqa: E501

        :return: The ex_date of this DividendOptionEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._ex_date

    @ex_date.setter
    def ex_date(self, ex_date):
        """Sets the ex_date of this DividendOptionEvent.

        The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.  # noqa: E501

        :param ex_date: The ex_date of this DividendOptionEvent.  # noqa: E501
        :type ex_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and ex_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_date`, must not be `None`")  # noqa: E501

        self._ex_date = ex_date

    @property
    def payment_date(self):
        """Gets the payment_date of this DividendOptionEvent.  # noqa: E501

        The date the company pays out dividends to shareholders.  # noqa: E501

        :return: The payment_date of this DividendOptionEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this DividendOptionEvent.

        The date the company pays out dividends to shareholders.  # noqa: E501

        :param payment_date: The payment_date of this DividendOptionEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def record_date(self):
        """Gets the record_date of this DividendOptionEvent.  # noqa: E501

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :return: The record_date of this DividendOptionEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this DividendOptionEvent.

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :param record_date: The record_date of this DividendOptionEvent.  # noqa: E501
        :type record_date: datetime
        """

        self._record_date = record_date

    @property
    def security_elections(self):
        """Gets the security_elections of this DividendOptionEvent.  # noqa: E501

        SecurityElection for this DividendReinvestmentEvent  # noqa: E501

        :return: The security_elections of this DividendOptionEvent.  # noqa: E501
        :rtype: list[lusid.SecurityElection]
        """
        return self._security_elections

    @security_elections.setter
    def security_elections(self, security_elections):
        """Sets the security_elections of this DividendOptionEvent.

        SecurityElection for this DividendReinvestmentEvent  # noqa: E501

        :param security_elections: The security_elections of this DividendOptionEvent.  # noqa: E501
        :type security_elections: list[lusid.SecurityElection]
        """
        if self.local_vars_configuration.client_side_validation and security_elections is None:  # noqa: E501
            raise ValueError("Invalid value for `security_elections`, must not be `None`")  # noqa: E501

        self._security_elections = security_elections

    @property
    def security_settlement_date(self):
        """Gets the security_settlement_date of this DividendOptionEvent.  # noqa: E501

        The settlement date of the additional units.  Equal to the PaymentDate if not provided.  # noqa: E501

        :return: The security_settlement_date of this DividendOptionEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._security_settlement_date

    @security_settlement_date.setter
    def security_settlement_date(self, security_settlement_date):
        """Sets the security_settlement_date of this DividendOptionEvent.

        The settlement date of the additional units.  Equal to the PaymentDate if not provided.  # noqa: E501

        :param security_settlement_date: The security_settlement_date of this DividendOptionEvent.  # noqa: E501
        :type security_settlement_date: datetime
        """

        self._security_settlement_date = security_settlement_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this DividendOptionEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :return: The instrument_event_type of this DividendOptionEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this DividendOptionEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this DividendOptionEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent", "ExpiryEvent", "ScripDividendEvent", "StockDividendEvent", "ReverseStockSplitEvent", "CapitalDistributionEvent", "SpinOffEvent", "MergerEvent", "FutureExpiryEvent", "SwapCashFlowEvent", "SwapPrincipalEvent", "CreditPremiumCashFlowEvent", "CdsCreditEvent", "CdxCreditEvent", "MbsCouponEvent", "MbsPrincipalEvent", "BonusIssueEvent", "MbsPrincipalWriteOffEvent", "MbsInterestDeferralEvent", "MbsInterestShortfallEvent", "TenderEvent", "CallOnIntermediateSecuritiesEvent", "IntermediateSecuritiesDistributionEvent", "OptionExercisePhysicalEvent", "OptionExerciseCashEvent", "ProtectionPayoutCashFlowEvent", "TermDepositInterestEvent", "TermDepositPrincipalEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, DividendOptionEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DividendOptionEvent):
            return True

        return self.to_dict() != other.to_dict()
