# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.26.0-v202506111109-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class FormulaUpdateInputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'binary_data': 'str',
        'formula': 'str',
        'parameters': 'list[str]'
    }

    attribute_map = {
        'binary_data': 'binaryData',
        'formula': 'formula',
        'parameters': 'parameters'
    }

    def __init__(self, binary_data=None, formula=None, parameters=None):
        """
        FormulaUpdateInputV1 - a model defined in Swagger
        """

        self._binary_data = None
        self._formula = None
        self._parameters = None

        if binary_data is not None:
          self.binary_data = binary_data
        if formula is not None:
          self.formula = formula
        if parameters is not None:
          self.parameters = parameters

    @property
    def binary_data(self):
        """
        Gets the binary_data of this FormulaUpdateInputV1.
        The binary data for the formula

        :return: The binary_data of this FormulaUpdateInputV1.
        :rtype: str
        """
        return self._binary_data

    @binary_data.setter
    def binary_data(self, binary_data):
        """
        Sets the binary_data of this FormulaUpdateInputV1.
        The binary data for the formula

        :param binary_data: The binary_data of this FormulaUpdateInputV1.
        :type: str
        """

        self._binary_data = binary_data

    @property
    def formula(self):
        """
        Gets the formula of this FormulaUpdateInputV1.
        The formula to be applied

        :return: The formula of this FormulaUpdateInputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this FormulaUpdateInputV1.
        The formula to be applied

        :param formula: The formula of this FormulaUpdateInputV1.
        :type: str
        """
        if formula is None:
            raise ValueError("Invalid value for `formula`, must not be `None`")

        self._formula = formula

    @property
    def parameters(self):
        """
        Gets the parameters of this FormulaUpdateInputV1.

        :return: The parameters of this FormulaUpdateInputV1.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this FormulaUpdateInputV1.

        :param parameters: The parameters of this FormulaUpdateInputV1.
        :type: list[str]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")

        self._parameters = parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FormulaUpdateInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
