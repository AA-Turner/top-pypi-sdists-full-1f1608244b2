# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class FineTunedModel(object):
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
    openapi_types = {
        'id': 'str',
        'base_model_id': 'str',
        'creator_id': 'str',
        'creator': 'MiniUser',
        'created_at': 'datetime',
        'storage_uri': 'str',
        'generation_config': 'object',
        'ft_type': 'FineTuneType',
        'cloud_id': 'str',
        'project_id': 'str',
        'job_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'base_model_id': 'base_model_id',
        'creator_id': 'creator_id',
        'creator': 'creator',
        'created_at': 'created_at',
        'storage_uri': 'storage_uri',
        'generation_config': 'generation_config',
        'ft_type': 'ft_type',
        'cloud_id': 'cloud_id',
        'project_id': 'project_id',
        'job_id': 'job_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, id=None, base_model_id=None, creator_id=None, creator=None, created_at=None, storage_uri=None, generation_config=None, ft_type=None, cloud_id=None, project_id=None, job_id=None, workspace_id=None, local_vars_configuration=None):  # noqa: E501
        """FineTunedModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._base_model_id = None
        self._creator_id = None
        self._creator = None
        self._created_at = None
        self._storage_uri = None
        self._generation_config = None
        self._ft_type = None
        self._cloud_id = None
        self._project_id = None
        self._job_id = None
        self._workspace_id = None
        self.discriminator = None

        self.id = id
        self.base_model_id = base_model_id
        if creator_id is not None:
            self.creator_id = creator_id
        if creator is not None:
            self.creator = creator
        self.created_at = created_at
        self.storage_uri = storage_uri
        if generation_config is not None:
            self.generation_config = generation_config
        self.ft_type = ft_type
        self.cloud_id = cloud_id
        if project_id is not None:
            self.project_id = project_id
        if job_id is not None:
            self.job_id = job_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def id(self):
        """Gets the id of this FineTunedModel.  # noqa: E501


        :return: The id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FineTunedModel.


        :param id: The id of this FineTunedModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def base_model_id(self):
        """Gets the base_model_id of this FineTunedModel.  # noqa: E501


        :return: The base_model_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._base_model_id

    @base_model_id.setter
    def base_model_id(self, base_model_id):
        """Sets the base_model_id of this FineTunedModel.


        :param base_model_id: The base_model_id of this FineTunedModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_model_id is None:  # noqa: E501
            raise ValueError("Invalid value for `base_model_id`, must not be `None`")  # noqa: E501

        self._base_model_id = base_model_id

    @property
    def creator_id(self):
        """Gets the creator_id of this FineTunedModel.  # noqa: E501


        :return: The creator_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this FineTunedModel.


        :param creator_id: The creator_id of this FineTunedModel.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def creator(self):
        """Gets the creator of this FineTunedModel.  # noqa: E501


        :return: The creator of this FineTunedModel.  # noqa: E501
        :rtype: MiniUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FineTunedModel.


        :param creator: The creator of this FineTunedModel.  # noqa: E501
        :type: MiniUser
        """

        self._creator = creator

    @property
    def created_at(self):
        """Gets the created_at of this FineTunedModel.  # noqa: E501


        :return: The created_at of this FineTunedModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FineTunedModel.


        :param created_at: The created_at of this FineTunedModel.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def storage_uri(self):
        """Gets the storage_uri of this FineTunedModel.  # noqa: E501


        :return: The storage_uri of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._storage_uri

    @storage_uri.setter
    def storage_uri(self, storage_uri):
        """Sets the storage_uri of this FineTunedModel.


        :param storage_uri: The storage_uri of this FineTunedModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and storage_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_uri`, must not be `None`")  # noqa: E501

        self._storage_uri = storage_uri

    @property
    def generation_config(self):
        """Gets the generation_config of this FineTunedModel.  # noqa: E501


        :return: The generation_config of this FineTunedModel.  # noqa: E501
        :rtype: object
        """
        return self._generation_config

    @generation_config.setter
    def generation_config(self, generation_config):
        """Sets the generation_config of this FineTunedModel.


        :param generation_config: The generation_config of this FineTunedModel.  # noqa: E501
        :type: object
        """

        self._generation_config = generation_config

    @property
    def ft_type(self):
        """Gets the ft_type of this FineTunedModel.  # noqa: E501


        :return: The ft_type of this FineTunedModel.  # noqa: E501
        :rtype: FineTuneType
        """
        return self._ft_type

    @ft_type.setter
    def ft_type(self, ft_type):
        """Sets the ft_type of this FineTunedModel.


        :param ft_type: The ft_type of this FineTunedModel.  # noqa: E501
        :type: FineTuneType
        """
        if self.local_vars_configuration.client_side_validation and ft_type is None:  # noqa: E501
            raise ValueError("Invalid value for `ft_type`, must not be `None`")  # noqa: E501

        self._ft_type = ft_type

    @property
    def cloud_id(self):
        """Gets the cloud_id of this FineTunedModel.  # noqa: E501


        :return: The cloud_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this FineTunedModel.


        :param cloud_id: The cloud_id of this FineTunedModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cloud_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_id`, must not be `None`")  # noqa: E501

        self._cloud_id = cloud_id

    @property
    def project_id(self):
        """Gets the project_id of this FineTunedModel.  # noqa: E501


        :return: The project_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FineTunedModel.


        :param project_id: The project_id of this FineTunedModel.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def job_id(self):
        """Gets the job_id of this FineTunedModel.  # noqa: E501


        :return: The job_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FineTunedModel.


        :param job_id: The job_id of this FineTunedModel.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this FineTunedModel.  # noqa: E501


        :return: The workspace_id of this FineTunedModel.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this FineTunedModel.


        :param workspace_id: The workspace_id of this FineTunedModel.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FineTunedModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FineTunedModel):
            return True

        return self.to_dict() != other.to_dict()
