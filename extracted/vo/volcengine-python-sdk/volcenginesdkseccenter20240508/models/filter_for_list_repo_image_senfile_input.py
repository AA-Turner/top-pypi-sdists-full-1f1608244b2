# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FilterForListRepoImageSenfileInput(object):
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
        'file_name': 'str',
        'section_desc': 'str',
        'severity': 'list[str]'
    }

    attribute_map = {
        'file_name': 'FileName',
        'section_desc': 'SectionDesc',
        'severity': 'Severity'
    }

    def __init__(self, file_name=None, section_desc=None, severity=None, _configuration=None):  # noqa: E501
        """FilterForListRepoImageSenfileInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_name = None
        self._section_desc = None
        self._severity = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if section_desc is not None:
            self.section_desc = section_desc
        if severity is not None:
            self.severity = severity

    @property
    def file_name(self):
        """Gets the file_name of this FilterForListRepoImageSenfileInput.  # noqa: E501


        :return: The file_name of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FilterForListRepoImageSenfileInput.


        :param file_name: The file_name of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def section_desc(self):
        """Gets the section_desc of this FilterForListRepoImageSenfileInput.  # noqa: E501


        :return: The section_desc of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :rtype: str
        """
        return self._section_desc

    @section_desc.setter
    def section_desc(self, section_desc):
        """Sets the section_desc of this FilterForListRepoImageSenfileInput.


        :param section_desc: The section_desc of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :type: str
        """

        self._section_desc = section_desc

    @property
    def severity(self):
        """Gets the severity of this FilterForListRepoImageSenfileInput.  # noqa: E501


        :return: The severity of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this FilterForListRepoImageSenfileInput.


        :param severity: The severity of this FilterForListRepoImageSenfileInput.  # noqa: E501
        :type: list[str]
        """

        self._severity = severity

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
        if issubclass(FilterForListRepoImageSenfileInput, dict):
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
        if not isinstance(other, FilterForListRepoImageSenfileInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListRepoImageSenfileInput):
            return True

        return self.to_dict() != other.to_dict()
