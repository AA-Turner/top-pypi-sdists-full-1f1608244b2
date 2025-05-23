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


class InstrumentEvent(object):
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
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'instrument_event_type': 'required'
    }

    discriminator_value_class_map = {
        'CashFlowEvent': 'CashFlowEvent',
        'DividendReinvestmentEvent': 'DividendReinvestmentEvent',
        'ProtectionPayoutCashFlowEvent': 'ProtectionPayoutCashFlowEvent',
        'OpenEvent': 'OpenEvent',
        'CreditPremiumCashFlowEvent': 'CreditPremiumCashFlowEvent',
        'CallOnIntermediateSecuritiesEvent': 'CallOnIntermediateSecuritiesEvent',
        'CloseEvent': 'CloseEvent',
        'SwapPrincipalEvent': 'SwapPrincipalEvent',
        'InformationalEvent': 'InformationalEvent',
        'CapitalDistributionEvent': 'CapitalDistributionEvent',
        'IntermediateSecuritiesDistributionEvent': 'IntermediateSecuritiesDistributionEvent',
        'MergerEvent': 'MergerEvent',
        'BonusIssueEvent': 'BonusIssueEvent',
        'FutureExpiryEvent': 'FutureExpiryEvent',
        'DividendOptionEvent': 'DividendOptionEvent',
        'ExpiryEvent': 'ExpiryEvent',
        'ScripDividendEvent': 'ScripDividendEvent',
        'TermDepositPrincipalEvent': 'TermDepositPrincipalEvent',
        'ResetEvent': 'ResetEvent',
        'MbsInterestDeferralEvent': 'MbsInterestDeferralEvent',
        'SwapCashFlowEvent': 'SwapCashFlowEvent',
        'OptionExercisePhysicalEvent': 'OptionExercisePhysicalEvent',
        'AmortisationEvent': 'AmortisationEvent',
        'FxForwardSettlementEvent': 'FxForwardSettlementEvent',
        'BondDefaultEvent': 'BondDefaultEvent',
        'RawVendorEvent': 'RawVendorEvent',
        'MaturityEvent': 'MaturityEvent',
        'StockSplitEvent': 'StockSplitEvent',
        'StockDividendEvent': 'StockDividendEvent',
        'TriggerEvent': 'TriggerEvent',
        'BondPrincipalEvent': 'BondPrincipalEvent',
        'CashDividendEvent': 'CashDividendEvent',
        'CdxCreditEvent': 'CdxCreditEvent',
        'MbsCouponEvent': 'MbsCouponEvent',
        'SpinOffEvent': 'SpinOffEvent',
        'ExerciseEvent': 'ExerciseEvent',
        'MbsInterestShortfallEvent': 'MbsInterestShortfallEvent',
        'TenderEvent': 'TenderEvent',
        'MbsPrincipalEvent': 'MbsPrincipalEvent',
        'AccumulationEvent': 'AccumulationEvent',
        'BondCouponEvent': 'BondCouponEvent',
        'TermDepositInterestEvent': 'TermDepositInterestEvent',
        'MbsPrincipalWriteOffEvent': 'MbsPrincipalWriteOffEvent',
        'CdsCreditEvent': 'CdsCreditEvent',
        'InformationalErrorEvent': 'InformationalErrorEvent',
        'ReverseStockSplitEvent': 'ReverseStockSplitEvent',
        'TransitionEvent': 'TransitionEvent',
        'OptionExerciseCashEvent': 'OptionExerciseCashEvent'
    }

    def __init__(self, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentEvent - a model defined in OpenAPI"
        
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_event_type = None
        self.discriminator = 'instrument_event_type'

        self.instrument_event_type = instrument_event_type

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this InstrumentEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :return: The instrument_event_type of this InstrumentEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this InstrumentEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this InstrumentEvent.  # noqa: E501
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

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, InstrumentEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentEvent):
            return True

        return self.to_dict() != other.to_dict()
