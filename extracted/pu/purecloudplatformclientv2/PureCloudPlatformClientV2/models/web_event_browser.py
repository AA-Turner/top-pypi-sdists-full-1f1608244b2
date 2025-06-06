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


class WebEventBrowser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WebEventBrowser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'family': 'str',
            'version': 'str',
            'lang': 'str'
        }

        self.attribute_map = {
            'family': 'family',
            'version': 'version',
            'lang': 'lang'
        }

        self._family = None
        self._version = None
        self._lang = None

    @property
    def family(self) -> str:
        """
        Gets the family of this WebEventBrowser.
        Browser family (e.g. Chrome, Safari, Firefox).

        :return: The family of this WebEventBrowser.
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family: str) -> None:
        """
        Sets the family of this WebEventBrowser.
        Browser family (e.g. Chrome, Safari, Firefox).

        :param family: The family of this WebEventBrowser.
        :type: str
        """
        

        self._family = family

    @property
    def version(self) -> str:
        """
        Gets the version of this WebEventBrowser.
        Browser version (e.g. 68.0.3440.84).

        :return: The version of this WebEventBrowser.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Sets the version of this WebEventBrowser.
        Browser version (e.g. 68.0.3440.84).

        :param version: The version of this WebEventBrowser.
        :type: str
        """
        

        self._version = version

    @property
    def lang(self) -> str:
        """
        Gets the lang of this WebEventBrowser.
        Language the browser is set to. Must conform to BCP 47.

        :return: The lang of this WebEventBrowser.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str) -> None:
        """
        Sets the lang of this WebEventBrowser.
        Language the browser is set to. Must conform to BCP 47.

        :param lang: The lang of this WebEventBrowser.
        :type: str
        """
        

        self._lang = lang

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

