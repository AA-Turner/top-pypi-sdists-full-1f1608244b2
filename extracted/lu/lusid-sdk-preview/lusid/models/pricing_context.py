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


class PricingContext(object):
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
        'model_rules': 'list[VendorModelRule]',
        'model_choice': 'dict(str, ModelSelection)',
        'options': 'PricingOptions',
        'result_data_rules': 'list[ResultKeyRule]',
        'holding_pricing_info': 'HoldingPricingInfo'
    }

    attribute_map = {
        'model_rules': 'modelRules',
        'model_choice': 'modelChoice',
        'options': 'options',
        'result_data_rules': 'resultDataRules',
        'holding_pricing_info': 'holdingPricingInfo'
    }

    required_map = {
        'model_rules': 'optional',
        'model_choice': 'optional',
        'options': 'optional',
        'result_data_rules': 'optional',
        'holding_pricing_info': 'optional'
    }

    def __init__(self, model_rules=None, model_choice=None, options=None, result_data_rules=None, holding_pricing_info=None, local_vars_configuration=None):  # noqa: E501
        """PricingContext - a model defined in OpenAPI"
        
        :param model_rules:  The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.
        :type model_rules: list[lusid.VendorModelRule]
        :param model_choice:  The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.
        :type model_choice: dict[str, lusid.ModelSelection]
        :param options: 
        :type options: lusid.PricingOptions
        :param result_data_rules:  Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.
        :type result_data_rules: list[lusid.ResultKeyRule]
        :param holding_pricing_info: 
        :type holding_pricing_info: lusid.HoldingPricingInfo

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._model_rules = None
        self._model_choice = None
        self._options = None
        self._result_data_rules = None
        self._holding_pricing_info = None
        self.discriminator = None

        self.model_rules = model_rules
        self.model_choice = model_choice
        if options is not None:
            self.options = options
        self.result_data_rules = result_data_rules
        if holding_pricing_info is not None:
            self.holding_pricing_info = holding_pricing_info

    @property
    def model_rules(self):
        """Gets the model_rules of this PricingContext.  # noqa: E501

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :return: The model_rules of this PricingContext.  # noqa: E501
        :rtype: list[lusid.VendorModelRule]
        """
        return self._model_rules

    @model_rules.setter
    def model_rules(self, model_rules):
        """Sets the model_rules of this PricingContext.

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :param model_rules: The model_rules of this PricingContext.  # noqa: E501
        :type model_rules: list[lusid.VendorModelRule]
        """

        self._model_rules = model_rules

    @property
    def model_choice(self):
        """Gets the model_choice of this PricingContext.  # noqa: E501

        The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.  # noqa: E501

        :return: The model_choice of this PricingContext.  # noqa: E501
        :rtype: dict[str, lusid.ModelSelection]
        """
        return self._model_choice

    @model_choice.setter
    def model_choice(self, model_choice):
        """Sets the model_choice of this PricingContext.

        The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.  # noqa: E501

        :param model_choice: The model_choice of this PricingContext.  # noqa: E501
        :type model_choice: dict[str, lusid.ModelSelection]
        """

        self._model_choice = model_choice

    @property
    def options(self):
        """Gets the options of this PricingContext.  # noqa: E501


        :return: The options of this PricingContext.  # noqa: E501
        :rtype: lusid.PricingOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PricingContext.


        :param options: The options of this PricingContext.  # noqa: E501
        :type options: lusid.PricingOptions
        """

        self._options = options

    @property
    def result_data_rules(self):
        """Gets the result_data_rules of this PricingContext.  # noqa: E501

        Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.  # noqa: E501

        :return: The result_data_rules of this PricingContext.  # noqa: E501
        :rtype: list[lusid.ResultKeyRule]
        """
        return self._result_data_rules

    @result_data_rules.setter
    def result_data_rules(self, result_data_rules):
        """Sets the result_data_rules of this PricingContext.

        Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.  # noqa: E501

        :param result_data_rules: The result_data_rules of this PricingContext.  # noqa: E501
        :type result_data_rules: list[lusid.ResultKeyRule]
        """

        self._result_data_rules = result_data_rules

    @property
    def holding_pricing_info(self):
        """Gets the holding_pricing_info of this PricingContext.  # noqa: E501


        :return: The holding_pricing_info of this PricingContext.  # noqa: E501
        :rtype: lusid.HoldingPricingInfo
        """
        return self._holding_pricing_info

    @holding_pricing_info.setter
    def holding_pricing_info(self, holding_pricing_info):
        """Sets the holding_pricing_info of this PricingContext.


        :param holding_pricing_info: The holding_pricing_info of this PricingContext.  # noqa: E501
        :type holding_pricing_info: lusid.HoldingPricingInfo
        """

        self._holding_pricing_info = holding_pricing_info

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
        if not isinstance(other, PricingContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PricingContext):
            return True

        return self.to_dict() != other.to_dict()
