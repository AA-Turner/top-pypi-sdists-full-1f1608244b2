# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class ReportTemplateInputV1(object):
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
        'description': 'str',
        'folder_id': 'str',
        'html_template': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'folder_id': 'folderId',
        'html_template': 'htmlTemplate',
        'name': 'name'
    }

    def __init__(self, description=None, folder_id=None, html_template=None, name=None):
        """
        ReportTemplateInputV1 - a model defined in Swagger
        """

        self._description = None
        self._folder_id = None
        self._html_template = None
        self._name = None

        if description is not None:
          self.description = description
        if folder_id is not None:
          self.folder_id = folder_id
        if html_template is not None:
          self.html_template = html_template
        if name is not None:
          self.name = name

    @property
    def description(self):
        """
        Gets the description of this ReportTemplateInputV1.
        The description of the template

        :return: The description of this ReportTemplateInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ReportTemplateInputV1.
        The description of the template

        :param description: The description of this ReportTemplateInputV1.
        :type: str
        """

        self._description = description

    @property
    def folder_id(self):
        """
        Gets the folder_id of this ReportTemplateInputV1.
        The id of the folder to place the new report template into. Special values of 'mine' or 'corporate' to place the item in the authenticated user's home folder or the corporate folder, respectively. If null, the workbook will be created in the authenticated user's home folder.

        :return: The folder_id of this ReportTemplateInputV1.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this ReportTemplateInputV1.
        The id of the folder to place the new report template into. Special values of 'mine' or 'corporate' to place the item in the authenticated user's home folder or the corporate folder, respectively. If null, the workbook will be created in the authenticated user's home folder.

        :param folder_id: The folder_id of this ReportTemplateInputV1.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def html_template(self):
        """
        Gets the html_template of this ReportTemplateInputV1.
        The actual html template for the report template

        :return: The html_template of this ReportTemplateInputV1.
        :rtype: str
        """
        return self._html_template

    @html_template.setter
    def html_template(self, html_template):
        """
        Sets the html_template of this ReportTemplateInputV1.
        The actual html template for the report template

        :param html_template: The html_template of this ReportTemplateInputV1.
        :type: str
        """
        if html_template is None:
            raise ValueError("Invalid value for `html_template`, must not be `None`")

        self._html_template = html_template

    @property
    def name(self):
        """
        Gets the name of this ReportTemplateInputV1.
        The name of the template

        :return: The name of this ReportTemplateInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportTemplateInputV1.
        The name of the template

        :param name: The name of this ReportTemplateInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, ReportTemplateInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
