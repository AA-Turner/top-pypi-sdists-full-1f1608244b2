# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import TestMatchesEventOperation
    from . import TestSchemaOperation

class TestModeEventResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TestModeEventResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'schema_validation': 'TestSchemaOperation',
            'trigger_match_validation': 'TestMatchesEventOperation'
        }

        self.attribute_map = {
            'schema_validation': 'schemaValidation',
            'trigger_match_validation': 'triggerMatchValidation'
        }

        self._schema_validation = None
        self._trigger_match_validation = None

    @property
    def schema_validation(self) -> 'TestSchemaOperation':
        """
        Gets the schema_validation of this TestModeEventResults.
        Information about the validation of the schema of the event body passed in to test mode

        :return: The schema_validation of this TestModeEventResults.
        :rtype: TestSchemaOperation
        """
        return self._schema_validation

    @schema_validation.setter
    def schema_validation(self, schema_validation: 'TestSchemaOperation') -> None:
        """
        Sets the schema_validation of this TestModeEventResults.
        Information about the validation of the schema of the event body passed in to test mode

        :param schema_validation: The schema_validation of this TestModeEventResults.
        :type: TestSchemaOperation
        """
        

        self._schema_validation = schema_validation

    @property
    def trigger_match_validation(self) -> 'TestMatchesEventOperation':
        """
        Gets the trigger_match_validation of this TestModeEventResults.
        Information about matched and unmatched triggers

        :return: The trigger_match_validation of this TestModeEventResults.
        :rtype: TestMatchesEventOperation
        """
        return self._trigger_match_validation

    @trigger_match_validation.setter
    def trigger_match_validation(self, trigger_match_validation: 'TestMatchesEventOperation') -> None:
        """
        Sets the trigger_match_validation of this TestModeEventResults.
        Information about matched and unmatched triggers

        :param trigger_match_validation: The trigger_match_validation of this TestModeEventResults.
        :type: TestMatchesEventOperation
        """
        

        self._trigger_match_validation = trigger_match_validation

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

