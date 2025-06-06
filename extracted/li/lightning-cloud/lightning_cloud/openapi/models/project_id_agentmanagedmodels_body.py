# coding: utf-8

"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

import pprint
import re  # noqa: F401

from typing import TYPE_CHECKING

import six

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class ProjectIdAgentmanagedmodelsBody(object):
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
        'model': 'V1ManagedModel',
        'org_id': 'str'
    }

    attribute_map = {
        'model': 'model',
        'org_id': 'orgId'
    }

    def __init__(self, model: 'V1ManagedModel' =None, org_id: 'str' =None):  # noqa: E501
        """ProjectIdAgentmanagedmodelsBody - a model defined in Swagger"""  # noqa: E501
        self._model = None
        self._org_id = None
        self.discriminator = None
        if model is not None:
            self.model = model
        if org_id is not None:
            self.org_id = org_id

    @property
    def model(self) -> 'V1ManagedModel':
        """Gets the model of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501


        :return: The model of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501
        :rtype: V1ManagedModel
        """
        return self._model

    @model.setter
    def model(self, model: 'V1ManagedModel'):
        """Sets the model of this ProjectIdAgentmanagedmodelsBody.


        :param model: The model of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501
        :type: V1ManagedModel
        """

        self._model = model

    @property
    def org_id(self) -> 'str':
        """Gets the org_id of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501


        :return: The org_id of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id: 'str'):
        """Sets the org_id of this ProjectIdAgentmanagedmodelsBody.


        :param org_id: The org_id of this ProjectIdAgentmanagedmodelsBody.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    def to_dict(self) -> dict:
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
        if issubclass(ProjectIdAgentmanagedmodelsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'ProjectIdAgentmanagedmodelsBody') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectIdAgentmanagedmodelsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectIdAgentmanagedmodelsBody') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
