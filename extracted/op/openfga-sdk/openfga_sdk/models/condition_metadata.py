"""
Python SDK for OpenFGA

API version: 1.x
Website: https://openfga.dev
Documentation: https://openfga.dev/docs
Support: https://openfga.dev/community
License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

import pprint

from inspect import getfullargspec

from openfga_sdk.configuration import Configuration


class ConditionMetadata:
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
    """
    openapi_types: dict[str, str] = {"module": "str", "source_info": "SourceInfo"}

    attribute_map: dict[str, str] = {"module": "module", "source_info": "source_info"}

    def __init__(self, module=None, source_info=None, local_vars_configuration=None):
        """ConditionMetadata - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._module = None
        self._source_info = None
        self.discriminator = None

        if module is not None:
            self.module = module
        if source_info is not None:
            self.source_info = source_info

    @property
    def module(self):
        """Gets the module of this ConditionMetadata.


        :return: The module of this ConditionMetadata.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ConditionMetadata.


        :param module: The module of this ConditionMetadata.
        :type module: str
        """

        self._module = module

    @property
    def source_info(self):
        """Gets the source_info of this ConditionMetadata.


        :return: The source_info of this ConditionMetadata.
        :rtype: SourceInfo
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        """Sets the source_info of this ConditionMetadata.


        :param source_info: The source_info of this ConditionMetadata.
        :type source_info: SourceInfo
        """

        self._source_info = source_info

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

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
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
        if not isinstance(other, ConditionMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionMetadata):
            return True

        return self.to_dict() != other.to_dict()
