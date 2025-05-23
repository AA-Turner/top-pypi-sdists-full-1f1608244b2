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

class ProjectIdServiceexecutionBody(object):
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
        'arguments': 'list[V1CommandArgument]',
        'file_endpoint_id': 'str',
        'pipeline_id': 'str'
    }

    attribute_map = {
        'arguments': 'arguments',
        'file_endpoint_id': 'fileEndpointId',
        'pipeline_id': 'pipelineId'
    }

    def __init__(self, arguments: 'list[V1CommandArgument]' =None, file_endpoint_id: 'str' =None, pipeline_id: 'str' =None):  # noqa: E501
        """ProjectIdServiceexecutionBody - a model defined in Swagger"""  # noqa: E501
        self._arguments = None
        self._file_endpoint_id = None
        self._pipeline_id = None
        self.discriminator = None
        if arguments is not None:
            self.arguments = arguments
        if file_endpoint_id is not None:
            self.file_endpoint_id = file_endpoint_id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id

    @property
    def arguments(self) -> 'list[V1CommandArgument]':
        """Gets the arguments of this ProjectIdServiceexecutionBody.  # noqa: E501


        :return: The arguments of this ProjectIdServiceexecutionBody.  # noqa: E501
        :rtype: list[V1CommandArgument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments: 'list[V1CommandArgument]'):
        """Sets the arguments of this ProjectIdServiceexecutionBody.


        :param arguments: The arguments of this ProjectIdServiceexecutionBody.  # noqa: E501
        :type: list[V1CommandArgument]
        """

        self._arguments = arguments

    @property
    def file_endpoint_id(self) -> 'str':
        """Gets the file_endpoint_id of this ProjectIdServiceexecutionBody.  # noqa: E501


        :return: The file_endpoint_id of this ProjectIdServiceexecutionBody.  # noqa: E501
        :rtype: str
        """
        return self._file_endpoint_id

    @file_endpoint_id.setter
    def file_endpoint_id(self, file_endpoint_id: 'str'):
        """Sets the file_endpoint_id of this ProjectIdServiceexecutionBody.


        :param file_endpoint_id: The file_endpoint_id of this ProjectIdServiceexecutionBody.  # noqa: E501
        :type: str
        """

        self._file_endpoint_id = file_endpoint_id

    @property
    def pipeline_id(self) -> 'str':
        """Gets the pipeline_id of this ProjectIdServiceexecutionBody.  # noqa: E501


        :return: The pipeline_id of this ProjectIdServiceexecutionBody.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id: 'str'):
        """Sets the pipeline_id of this ProjectIdServiceexecutionBody.


        :param pipeline_id: The pipeline_id of this ProjectIdServiceexecutionBody.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

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
        if issubclass(ProjectIdServiceexecutionBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'ProjectIdServiceexecutionBody') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectIdServiceexecutionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectIdServiceexecutionBody') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
