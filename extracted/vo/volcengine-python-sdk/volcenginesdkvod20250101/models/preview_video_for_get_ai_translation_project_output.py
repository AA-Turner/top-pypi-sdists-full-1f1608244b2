# coding: utf-8

"""
    vod20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PreviewVideoForGetAITranslationProjectOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'duration_second': 'float',
        'is_audio': 'bool',
        'uri': 'str',
        'url': 'str',
        'vid': 'str'
    }

    attribute_map = {
        'duration_second': 'DurationSecond',
        'is_audio': 'IsAudio',
        'uri': 'Uri',
        'url': 'Url',
        'vid': 'Vid'
    }

    def __init__(self, duration_second=None, is_audio=None, uri=None, url=None, vid=None, _configuration=None):  # noqa: E501
        """PreviewVideoForGetAITranslationProjectOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration_second = None
        self._is_audio = None
        self._uri = None
        self._url = None
        self._vid = None
        self.discriminator = None

        if duration_second is not None:
            self.duration_second = duration_second
        if is_audio is not None:
            self.is_audio = is_audio
        if uri is not None:
            self.uri = uri
        if url is not None:
            self.url = url
        if vid is not None:
            self.vid = vid

    @property
    def duration_second(self):
        """Gets the duration_second of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501


        :return: The duration_second of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :rtype: float
        """
        return self._duration_second

    @duration_second.setter
    def duration_second(self, duration_second):
        """Sets the duration_second of this PreviewVideoForGetAITranslationProjectOutput.


        :param duration_second: The duration_second of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :type: float
        """

        self._duration_second = duration_second

    @property
    def is_audio(self):
        """Gets the is_audio of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501


        :return: The is_audio of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_audio

    @is_audio.setter
    def is_audio(self, is_audio):
        """Sets the is_audio of this PreviewVideoForGetAITranslationProjectOutput.


        :param is_audio: The is_audio of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :type: bool
        """

        self._is_audio = is_audio

    @property
    def uri(self):
        """Gets the uri of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501


        :return: The uri of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this PreviewVideoForGetAITranslationProjectOutput.


        :param uri: The uri of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def url(self):
        """Gets the url of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501


        :return: The url of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PreviewVideoForGetAITranslationProjectOutput.


        :param url: The url of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def vid(self):
        """Gets the vid of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501


        :return: The vid of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this PreviewVideoForGetAITranslationProjectOutput.


        :param vid: The vid of this PreviewVideoForGetAITranslationProjectOutput.  # noqa: E501
        :type: str
        """

        self._vid = vid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PreviewVideoForGetAITranslationProjectOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PreviewVideoForGetAITranslationProjectOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreviewVideoForGetAITranslationProjectOutput):
            return True

        return self.to_dict() != other.to_dict()
