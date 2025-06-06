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


class JourneyAppEventsNotificationBrowser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyAppEventsNotificationBrowser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'family': 'str',
            'version': 'str',
            'lang': 'str',
            'fingerprint': 'str',
            'view_height': 'int',
            'view_width': 'int',
            'features_flash': 'bool',
            'features_java': 'bool',
            'features_pdf': 'bool',
            'features_webrtc': 'bool'
        }

        self.attribute_map = {
            'family': 'family',
            'version': 'version',
            'lang': 'lang',
            'fingerprint': 'fingerprint',
            'view_height': 'viewHeight',
            'view_width': 'viewWidth',
            'features_flash': 'featuresFlash',
            'features_java': 'featuresJava',
            'features_pdf': 'featuresPdf',
            'features_webrtc': 'featuresWebrtc'
        }

        self._family = None
        self._version = None
        self._lang = None
        self._fingerprint = None
        self._view_height = None
        self._view_width = None
        self._features_flash = None
        self._features_java = None
        self._features_pdf = None
        self._features_webrtc = None

    @property
    def family(self) -> str:
        """
        Gets the family of this JourneyAppEventsNotificationBrowser.


        :return: The family of this JourneyAppEventsNotificationBrowser.
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family: str) -> None:
        """
        Sets the family of this JourneyAppEventsNotificationBrowser.


        :param family: The family of this JourneyAppEventsNotificationBrowser.
        :type: str
        """
        

        self._family = family

    @property
    def version(self) -> str:
        """
        Gets the version of this JourneyAppEventsNotificationBrowser.


        :return: The version of this JourneyAppEventsNotificationBrowser.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Sets the version of this JourneyAppEventsNotificationBrowser.


        :param version: The version of this JourneyAppEventsNotificationBrowser.
        :type: str
        """
        

        self._version = version

    @property
    def lang(self) -> str:
        """
        Gets the lang of this JourneyAppEventsNotificationBrowser.


        :return: The lang of this JourneyAppEventsNotificationBrowser.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str) -> None:
        """
        Sets the lang of this JourneyAppEventsNotificationBrowser.


        :param lang: The lang of this JourneyAppEventsNotificationBrowser.
        :type: str
        """
        

        self._lang = lang

    @property
    def fingerprint(self) -> str:
        """
        Gets the fingerprint of this JourneyAppEventsNotificationBrowser.


        :return: The fingerprint of this JourneyAppEventsNotificationBrowser.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint: str) -> None:
        """
        Sets the fingerprint of this JourneyAppEventsNotificationBrowser.


        :param fingerprint: The fingerprint of this JourneyAppEventsNotificationBrowser.
        :type: str
        """
        

        self._fingerprint = fingerprint

    @property
    def view_height(self) -> int:
        """
        Gets the view_height of this JourneyAppEventsNotificationBrowser.


        :return: The view_height of this JourneyAppEventsNotificationBrowser.
        :rtype: int
        """
        return self._view_height

    @view_height.setter
    def view_height(self, view_height: int) -> None:
        """
        Sets the view_height of this JourneyAppEventsNotificationBrowser.


        :param view_height: The view_height of this JourneyAppEventsNotificationBrowser.
        :type: int
        """
        

        self._view_height = view_height

    @property
    def view_width(self) -> int:
        """
        Gets the view_width of this JourneyAppEventsNotificationBrowser.


        :return: The view_width of this JourneyAppEventsNotificationBrowser.
        :rtype: int
        """
        return self._view_width

    @view_width.setter
    def view_width(self, view_width: int) -> None:
        """
        Sets the view_width of this JourneyAppEventsNotificationBrowser.


        :param view_width: The view_width of this JourneyAppEventsNotificationBrowser.
        :type: int
        """
        

        self._view_width = view_width

    @property
    def features_flash(self) -> bool:
        """
        Gets the features_flash of this JourneyAppEventsNotificationBrowser.


        :return: The features_flash of this JourneyAppEventsNotificationBrowser.
        :rtype: bool
        """
        return self._features_flash

    @features_flash.setter
    def features_flash(self, features_flash: bool) -> None:
        """
        Sets the features_flash of this JourneyAppEventsNotificationBrowser.


        :param features_flash: The features_flash of this JourneyAppEventsNotificationBrowser.
        :type: bool
        """
        

        self._features_flash = features_flash

    @property
    def features_java(self) -> bool:
        """
        Gets the features_java of this JourneyAppEventsNotificationBrowser.


        :return: The features_java of this JourneyAppEventsNotificationBrowser.
        :rtype: bool
        """
        return self._features_java

    @features_java.setter
    def features_java(self, features_java: bool) -> None:
        """
        Sets the features_java of this JourneyAppEventsNotificationBrowser.


        :param features_java: The features_java of this JourneyAppEventsNotificationBrowser.
        :type: bool
        """
        

        self._features_java = features_java

    @property
    def features_pdf(self) -> bool:
        """
        Gets the features_pdf of this JourneyAppEventsNotificationBrowser.


        :return: The features_pdf of this JourneyAppEventsNotificationBrowser.
        :rtype: bool
        """
        return self._features_pdf

    @features_pdf.setter
    def features_pdf(self, features_pdf: bool) -> None:
        """
        Sets the features_pdf of this JourneyAppEventsNotificationBrowser.


        :param features_pdf: The features_pdf of this JourneyAppEventsNotificationBrowser.
        :type: bool
        """
        

        self._features_pdf = features_pdf

    @property
    def features_webrtc(self) -> bool:
        """
        Gets the features_webrtc of this JourneyAppEventsNotificationBrowser.


        :return: The features_webrtc of this JourneyAppEventsNotificationBrowser.
        :rtype: bool
        """
        return self._features_webrtc

    @features_webrtc.setter
    def features_webrtc(self, features_webrtc: bool) -> None:
        """
        Sets the features_webrtc of this JourneyAppEventsNotificationBrowser.


        :param features_webrtc: The features_webrtc of this JourneyAppEventsNotificationBrowser.
        :type: bool
        """
        

        self._features_webrtc = features_webrtc

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

