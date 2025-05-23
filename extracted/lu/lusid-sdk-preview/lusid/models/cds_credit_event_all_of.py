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


class CdsCreditEventAllOf(object):
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
        'effective_date': 'datetime',
        'auction_date': 'datetime',
        'recovery_rate': 'float',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'effective_date': 'effectiveDate',
        'auction_date': 'auctionDate',
        'recovery_rate': 'recoveryRate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'effective_date': 'required',
        'auction_date': 'optional',
        'recovery_rate': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, effective_date=None, auction_date=None, recovery_rate=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """CdsCreditEventAllOf - a model defined in OpenAPI"
        
        :param effective_date:  The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation. (required)
        :type effective_date: datetime
        :param auction_date:  The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined.
        :type auction_date: datetime
        :param recovery_rate:  The fraction of the defaulted debt that can be recovered.
        :type recovery_rate: float
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_date = None
        self._auction_date = None
        self._recovery_rate = None
        self._instrument_event_type = None
        self.discriminator = None

        self.effective_date = effective_date
        self.auction_date = auction_date
        self.recovery_rate = recovery_rate
        self.instrument_event_type = instrument_event_type

    @property
    def effective_date(self):
        """Gets the effective_date of this CdsCreditEventAllOf.  # noqa: E501

        The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation.  # noqa: E501

        :return: The effective_date of this CdsCreditEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CdsCreditEventAllOf.

        The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation.  # noqa: E501

        :param effective_date: The effective_date of this CdsCreditEventAllOf.  # noqa: E501
        :type effective_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_date is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_date`, must not be `None`")  # noqa: E501

        self._effective_date = effective_date

    @property
    def auction_date(self):
        """Gets the auction_date of this CdsCreditEventAllOf.  # noqa: E501

        The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined.  # noqa: E501

        :return: The auction_date of this CdsCreditEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._auction_date

    @auction_date.setter
    def auction_date(self, auction_date):
        """Sets the auction_date of this CdsCreditEventAllOf.

        The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined.  # noqa: E501

        :param auction_date: The auction_date of this CdsCreditEventAllOf.  # noqa: E501
        :type auction_date: datetime
        """

        self._auction_date = auction_date

    @property
    def recovery_rate(self):
        """Gets the recovery_rate of this CdsCreditEventAllOf.  # noqa: E501

        The fraction of the defaulted debt that can be recovered.  # noqa: E501

        :return: The recovery_rate of this CdsCreditEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._recovery_rate

    @recovery_rate.setter
    def recovery_rate(self, recovery_rate):
        """Sets the recovery_rate of this CdsCreditEventAllOf.

        The fraction of the defaulted debt that can be recovered.  # noqa: E501

        :param recovery_rate: The recovery_rate of this CdsCreditEventAllOf.  # noqa: E501
        :type recovery_rate: float
        """

        self._recovery_rate = recovery_rate

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this CdsCreditEventAllOf.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :return: The instrument_event_type of this CdsCreditEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this CdsCreditEventAllOf.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this CdsCreditEventAllOf.  # noqa: E501
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
        if not isinstance(other, CdsCreditEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CdsCreditEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
