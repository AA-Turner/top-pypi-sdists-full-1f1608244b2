# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cudo_compute.configuration import Configuration


class ListProjectsResponse(object):
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
        'projects': 'list[Project]',
        'page_token': 'str',
        'page_size': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'page_token': 'pageToken',
        'page_size': 'pageSize'
    }

    def __init__(self, projects=None, page_token=None, page_size=None, _configuration=None):  # noqa: E501
        """ListProjectsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._projects = None
        self._page_token = None
        self._page_size = None
        self.discriminator = None

        self.projects = projects
        self.page_token = page_token
        self.page_size = page_size

    @property
    def projects(self):
        """Gets the projects of this ListProjectsResponse.  # noqa: E501


        :return: The projects of this ListProjectsResponse.  # noqa: E501
        :rtype: list[Project]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ListProjectsResponse.


        :param projects: The projects of this ListProjectsResponse.  # noqa: E501
        :type: list[Project]
        """
        if self._configuration.client_side_validation and projects is None:
            raise ValueError("Invalid value for `projects`, must not be `None`")  # noqa: E501

        self._projects = projects

    @property
    def page_token(self):
        """Gets the page_token of this ListProjectsResponse.  # noqa: E501


        :return: The page_token of this ListProjectsResponse.  # noqa: E501
        :rtype: str
        """
        return self._page_token

    @page_token.setter
    def page_token(self, page_token):
        """Sets the page_token of this ListProjectsResponse.


        :param page_token: The page_token of this ListProjectsResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and page_token is None:
            raise ValueError("Invalid value for `page_token`, must not be `None`")  # noqa: E501

        self._page_token = page_token

    @property
    def page_size(self):
        """Gets the page_size of this ListProjectsResponse.  # noqa: E501


        :return: The page_size of this ListProjectsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListProjectsResponse.


        :param page_size: The page_size of this ListProjectsResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

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
        if issubclass(ListProjectsResponse, dict):
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
        if not isinstance(other, ListProjectsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListProjectsResponse):
            return True

        return self.to_dict() != other.to_dict()
