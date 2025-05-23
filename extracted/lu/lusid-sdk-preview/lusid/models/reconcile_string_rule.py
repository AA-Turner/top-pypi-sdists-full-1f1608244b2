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


class ReconcileStringRule(object):
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
        'comparison_type': 'str',
        'one_of_candidates': 'dict(str, list[str])',
        'applies_to': 'AggregateSpec',
        'rule_type': 'str'
    }

    attribute_map = {
        'comparison_type': 'comparisonType',
        'one_of_candidates': 'oneOfCandidates',
        'applies_to': 'appliesTo',
        'rule_type': 'ruleType'
    }

    required_map = {
        'comparison_type': 'required',
        'one_of_candidates': 'optional',
        'applies_to': 'required',
        'rule_type': 'required'
    }

    def __init__(self, comparison_type=None, one_of_candidates=None, applies_to=None, rule_type=None, local_vars_configuration=None):  # noqa: E501
        """ReconcileStringRule - a model defined in OpenAPI"
        
        :param comparison_type:  The available values are: Exact, Contains, CaseInsensitive, ContainsAnyCase, IsOneOf (required)
        :type comparison_type: str
        :param one_of_candidates:  For cases of \"IsOneOf\" a set is required to match values against.  Fuzzy matching of strings against one of a set. There can be cases where systems \"A\" and \"B\" might use different terms for the same logical entity. A common case would be  comparison of something like a day count fraction where some convention like the \"actual 365\" convention might be represented as one of [\"A365\", \"Act365\", \"Actual365\"] or similar.  This is to allow this kind of fuzzy matching of values. Note that as this is exhaustive comparison across sets it will be slow and should therefore be used sparingly.
        :type one_of_candidates: dict(str, list[str])
        :param applies_to:  (required)
        :type applies_to: lusid.AggregateSpec
        :param rule_type:  The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact (required)
        :type rule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._comparison_type = None
        self._one_of_candidates = None
        self._applies_to = None
        self._rule_type = None
        self.discriminator = None

        self.comparison_type = comparison_type
        self.one_of_candidates = one_of_candidates
        self.applies_to = applies_to
        self.rule_type = rule_type

    @property
    def comparison_type(self):
        """Gets the comparison_type of this ReconcileStringRule.  # noqa: E501

        The available values are: Exact, Contains, CaseInsensitive, ContainsAnyCase, IsOneOf  # noqa: E501

        :return: The comparison_type of this ReconcileStringRule.  # noqa: E501
        :rtype: str
        """
        return self._comparison_type

    @comparison_type.setter
    def comparison_type(self, comparison_type):
        """Sets the comparison_type of this ReconcileStringRule.

        The available values are: Exact, Contains, CaseInsensitive, ContainsAnyCase, IsOneOf  # noqa: E501

        :param comparison_type: The comparison_type of this ReconcileStringRule.  # noqa: E501
        :type comparison_type: str
        """
        if self.local_vars_configuration.client_side_validation and comparison_type is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Exact", "Contains", "CaseInsensitive", "ContainsAnyCase", "IsOneOf"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and comparison_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `comparison_type` ({0}), must be one of {1}"  # noqa: E501
                .format(comparison_type, allowed_values)
            )

        self._comparison_type = comparison_type

    @property
    def one_of_candidates(self):
        """Gets the one_of_candidates of this ReconcileStringRule.  # noqa: E501

        For cases of \"IsOneOf\" a set is required to match values against.  Fuzzy matching of strings against one of a set. There can be cases where systems \"A\" and \"B\" might use different terms for the same logical entity. A common case would be  comparison of something like a day count fraction where some convention like the \"actual 365\" convention might be represented as one of [\"A365\", \"Act365\", \"Actual365\"] or similar.  This is to allow this kind of fuzzy matching of values. Note that as this is exhaustive comparison across sets it will be slow and should therefore be used sparingly.  # noqa: E501

        :return: The one_of_candidates of this ReconcileStringRule.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._one_of_candidates

    @one_of_candidates.setter
    def one_of_candidates(self, one_of_candidates):
        """Sets the one_of_candidates of this ReconcileStringRule.

        For cases of \"IsOneOf\" a set is required to match values against.  Fuzzy matching of strings against one of a set. There can be cases where systems \"A\" and \"B\" might use different terms for the same logical entity. A common case would be  comparison of something like a day count fraction where some convention like the \"actual 365\" convention might be represented as one of [\"A365\", \"Act365\", \"Actual365\"] or similar.  This is to allow this kind of fuzzy matching of values. Note that as this is exhaustive comparison across sets it will be slow and should therefore be used sparingly.  # noqa: E501

        :param one_of_candidates: The one_of_candidates of this ReconcileStringRule.  # noqa: E501
        :type one_of_candidates: dict(str, list[str])
        """

        self._one_of_candidates = one_of_candidates

    @property
    def applies_to(self):
        """Gets the applies_to of this ReconcileStringRule.  # noqa: E501


        :return: The applies_to of this ReconcileStringRule.  # noqa: E501
        :rtype: lusid.AggregateSpec
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this ReconcileStringRule.


        :param applies_to: The applies_to of this ReconcileStringRule.  # noqa: E501
        :type applies_to: lusid.AggregateSpec
        """
        if self.local_vars_configuration.client_side_validation and applies_to is None:  # noqa: E501
            raise ValueError("Invalid value for `applies_to`, must not be `None`")  # noqa: E501

        self._applies_to = applies_to

    @property
    def rule_type(self):
        """Gets the rule_type of this ReconcileStringRule.  # noqa: E501

        The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact  # noqa: E501

        :return: The rule_type of this ReconcileStringRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ReconcileStringRule.

        The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact  # noqa: E501

        :param rule_type: The rule_type of this ReconcileStringRule.  # noqa: E501
        :type rule_type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ReconcileNumericRule", "ReconcileDateTimeRule", "ReconcileStringRule", "ReconcileExact"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rule_type, allowed_values)
            )

        self._rule_type = rule_type

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
        if not isinstance(other, ReconcileStringRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconcileStringRule):
            return True

        return self.to_dict() != other.to_dict()
