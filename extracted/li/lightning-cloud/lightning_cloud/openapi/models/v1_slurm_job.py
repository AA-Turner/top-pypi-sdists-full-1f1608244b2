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

class V1SLURMJob(object):
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
        'cache_id': 'str',
        'cloudspace_id': 'str',
        'cluster_id': 'str',
        'command': 'str',
        'created_at': 'datetime',
        'id': 'str',
        'linked_project_id': 'str',
        'linked_user_id': 'str',
        'message': 'str',
        'name': 'str',
        'num_gpus': 'str',
        'project_id': 'str',
        'run_id': 'str',
        'service_id': 'str',
        'slurm_v1_status': 'V1SlurmV1JobStatus',
        'state': 'str',
        'updated_at': 'datetime',
        'upload_eta_seconds': 'str',
        'upload_in_progress': 'bool',
        'upload_percentage': 'str',
        'user_id': 'str',
        'work_dir': 'str'
    }

    attribute_map = {
        'cache_id': 'cacheId',
        'cloudspace_id': 'cloudspaceId',
        'cluster_id': 'clusterId',
        'command': 'command',
        'created_at': 'createdAt',
        'id': 'id',
        'linked_project_id': 'linkedProjectId',
        'linked_user_id': 'linkedUserId',
        'message': 'message',
        'name': 'name',
        'num_gpus': 'numGpus',
        'project_id': 'projectId',
        'run_id': 'runId',
        'service_id': 'serviceId',
        'slurm_v1_status': 'slurmV1Status',
        'state': 'state',
        'updated_at': 'updatedAt',
        'upload_eta_seconds': 'uploadEtaSeconds',
        'upload_in_progress': 'uploadInProgress',
        'upload_percentage': 'uploadPercentage',
        'user_id': 'userId',
        'work_dir': 'workDir'
    }

    def __init__(self, cache_id: 'str' =None, cloudspace_id: 'str' =None, cluster_id: 'str' =None, command: 'str' =None, created_at: 'datetime' =None, id: 'str' =None, linked_project_id: 'str' =None, linked_user_id: 'str' =None, message: 'str' =None, name: 'str' =None, num_gpus: 'str' =None, project_id: 'str' =None, run_id: 'str' =None, service_id: 'str' =None, slurm_v1_status: 'V1SlurmV1JobStatus' =None, state: 'str' =None, updated_at: 'datetime' =None, upload_eta_seconds: 'str' =None, upload_in_progress: 'bool' =None, upload_percentage: 'str' =None, user_id: 'str' =None, work_dir: 'str' =None):  # noqa: E501
        """V1SLURMJob - a model defined in Swagger"""  # noqa: E501
        self._cache_id = None
        self._cloudspace_id = None
        self._cluster_id = None
        self._command = None
        self._created_at = None
        self._id = None
        self._linked_project_id = None
        self._linked_user_id = None
        self._message = None
        self._name = None
        self._num_gpus = None
        self._project_id = None
        self._run_id = None
        self._service_id = None
        self._slurm_v1_status = None
        self._state = None
        self._updated_at = None
        self._upload_eta_seconds = None
        self._upload_in_progress = None
        self._upload_percentage = None
        self._user_id = None
        self._work_dir = None
        self.discriminator = None
        if cache_id is not None:
            self.cache_id = cache_id
        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if command is not None:
            self.command = command
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if linked_project_id is not None:
            self.linked_project_id = linked_project_id
        if linked_user_id is not None:
            self.linked_user_id = linked_user_id
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if num_gpus is not None:
            self.num_gpus = num_gpus
        if project_id is not None:
            self.project_id = project_id
        if run_id is not None:
            self.run_id = run_id
        if service_id is not None:
            self.service_id = service_id
        if slurm_v1_status is not None:
            self.slurm_v1_status = slurm_v1_status
        if state is not None:
            self.state = state
        if updated_at is not None:
            self.updated_at = updated_at
        if upload_eta_seconds is not None:
            self.upload_eta_seconds = upload_eta_seconds
        if upload_in_progress is not None:
            self.upload_in_progress = upload_in_progress
        if upload_percentage is not None:
            self.upload_percentage = upload_percentage
        if user_id is not None:
            self.user_id = user_id
        if work_dir is not None:
            self.work_dir = work_dir

    @property
    def cache_id(self) -> 'str':
        """Gets the cache_id of this V1SLURMJob.  # noqa: E501


        :return: The cache_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._cache_id

    @cache_id.setter
    def cache_id(self, cache_id: 'str'):
        """Sets the cache_id of this V1SLURMJob.


        :param cache_id: The cache_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._cache_id = cache_id

    @property
    def cloudspace_id(self) -> 'str':
        """Gets the cloudspace_id of this V1SLURMJob.  # noqa: E501


        :return: The cloudspace_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id: 'str'):
        """Sets the cloudspace_id of this V1SLURMJob.


        :param cloudspace_id: The cloudspace_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def cluster_id(self) -> 'str':
        """Gets the cluster_id of this V1SLURMJob.  # noqa: E501


        :return: The cluster_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id: 'str'):
        """Sets the cluster_id of this V1SLURMJob.


        :param cluster_id: The cluster_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def command(self) -> 'str':
        """Gets the command of this V1SLURMJob.  # noqa: E501


        :return: The command of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command: 'str'):
        """Sets the command of this V1SLURMJob.


        :param command: The command of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this V1SLURMJob.  # noqa: E501


        :return: The created_at of this V1SLURMJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this V1SLURMJob.


        :param created_at: The created_at of this V1SLURMJob.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self) -> 'str':
        """Gets the id of this V1SLURMJob.  # noqa: E501


        :return: The id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: 'str'):
        """Sets the id of this V1SLURMJob.


        :param id: The id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def linked_project_id(self) -> 'str':
        """Gets the linked_project_id of this V1SLURMJob.  # noqa: E501


        :return: The linked_project_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._linked_project_id

    @linked_project_id.setter
    def linked_project_id(self, linked_project_id: 'str'):
        """Sets the linked_project_id of this V1SLURMJob.


        :param linked_project_id: The linked_project_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._linked_project_id = linked_project_id

    @property
    def linked_user_id(self) -> 'str':
        """Gets the linked_user_id of this V1SLURMJob.  # noqa: E501


        :return: The linked_user_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._linked_user_id

    @linked_user_id.setter
    def linked_user_id(self, linked_user_id: 'str'):
        """Sets the linked_user_id of this V1SLURMJob.


        :param linked_user_id: The linked_user_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._linked_user_id = linked_user_id

    @property
    def message(self) -> 'str':
        """Gets the message of this V1SLURMJob.  # noqa: E501


        :return: The message of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: 'str'):
        """Sets the message of this V1SLURMJob.


        :param message: The message of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self) -> 'str':
        """Gets the name of this V1SLURMJob.  # noqa: E501


        :return: The name of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: 'str'):
        """Sets the name of this V1SLURMJob.


        :param name: The name of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_gpus(self) -> 'str':
        """Gets the num_gpus of this V1SLURMJob.  # noqa: E501


        :return: The num_gpus of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._num_gpus

    @num_gpus.setter
    def num_gpus(self, num_gpus: 'str'):
        """Sets the num_gpus of this V1SLURMJob.


        :param num_gpus: The num_gpus of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._num_gpus = num_gpus

    @property
    def project_id(self) -> 'str':
        """Gets the project_id of this V1SLURMJob.  # noqa: E501


        :return: The project_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: 'str'):
        """Sets the project_id of this V1SLURMJob.


        :param project_id: The project_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def run_id(self) -> 'str':
        """Gets the run_id of this V1SLURMJob.  # noqa: E501


        :return: The run_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id: 'str'):
        """Sets the run_id of this V1SLURMJob.


        :param run_id: The run_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def service_id(self) -> 'str':
        """Gets the service_id of this V1SLURMJob.  # noqa: E501


        :return: The service_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id: 'str'):
        """Sets the service_id of this V1SLURMJob.


        :param service_id: The service_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def slurm_v1_status(self) -> 'V1SlurmV1JobStatus':
        """Gets the slurm_v1_status of this V1SLURMJob.  # noqa: E501


        :return: The slurm_v1_status of this V1SLURMJob.  # noqa: E501
        :rtype: V1SlurmV1JobStatus
        """
        return self._slurm_v1_status

    @slurm_v1_status.setter
    def slurm_v1_status(self, slurm_v1_status: 'V1SlurmV1JobStatus'):
        """Sets the slurm_v1_status of this V1SLURMJob.


        :param slurm_v1_status: The slurm_v1_status of this V1SLURMJob.  # noqa: E501
        :type: V1SlurmV1JobStatus
        """

        self._slurm_v1_status = slurm_v1_status

    @property
    def state(self) -> 'str':
        """Gets the state of this V1SLURMJob.  # noqa: E501


        :return: The state of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: 'str'):
        """Sets the state of this V1SLURMJob.


        :param state: The state of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def updated_at(self) -> 'datetime':
        """Gets the updated_at of this V1SLURMJob.  # noqa: E501


        :return: The updated_at of this V1SLURMJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: 'datetime'):
        """Sets the updated_at of this V1SLURMJob.


        :param updated_at: The updated_at of this V1SLURMJob.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def upload_eta_seconds(self) -> 'str':
        """Gets the upload_eta_seconds of this V1SLURMJob.  # noqa: E501


        :return: The upload_eta_seconds of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._upload_eta_seconds

    @upload_eta_seconds.setter
    def upload_eta_seconds(self, upload_eta_seconds: 'str'):
        """Sets the upload_eta_seconds of this V1SLURMJob.


        :param upload_eta_seconds: The upload_eta_seconds of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._upload_eta_seconds = upload_eta_seconds

    @property
    def upload_in_progress(self) -> 'bool':
        """Gets the upload_in_progress of this V1SLURMJob.  # noqa: E501


        :return: The upload_in_progress of this V1SLURMJob.  # noqa: E501
        :rtype: bool
        """
        return self._upload_in_progress

    @upload_in_progress.setter
    def upload_in_progress(self, upload_in_progress: 'bool'):
        """Sets the upload_in_progress of this V1SLURMJob.


        :param upload_in_progress: The upload_in_progress of this V1SLURMJob.  # noqa: E501
        :type: bool
        """

        self._upload_in_progress = upload_in_progress

    @property
    def upload_percentage(self) -> 'str':
        """Gets the upload_percentage of this V1SLURMJob.  # noqa: E501


        :return: The upload_percentage of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._upload_percentage

    @upload_percentage.setter
    def upload_percentage(self, upload_percentage: 'str'):
        """Sets the upload_percentage of this V1SLURMJob.


        :param upload_percentage: The upload_percentage of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._upload_percentage = upload_percentage

    @property
    def user_id(self) -> 'str':
        """Gets the user_id of this V1SLURMJob.  # noqa: E501


        :return: The user_id of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: 'str'):
        """Sets the user_id of this V1SLURMJob.


        :param user_id: The user_id of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def work_dir(self) -> 'str':
        """Gets the work_dir of this V1SLURMJob.  # noqa: E501

        Where the files will be downloaded, for example: /scratch/nyu/<username> Then the directories that Lightning will create/use: /scratch/nyu/<username>/lightning_manager/<studio name>/<job-id>/...  # noqa: E501

        :return: The work_dir of this V1SLURMJob.  # noqa: E501
        :rtype: str
        """
        return self._work_dir

    @work_dir.setter
    def work_dir(self, work_dir: 'str'):
        """Sets the work_dir of this V1SLURMJob.

        Where the files will be downloaded, for example: /scratch/nyu/<username> Then the directories that Lightning will create/use: /scratch/nyu/<username>/lightning_manager/<studio name>/<job-id>/...  # noqa: E501

        :param work_dir: The work_dir of this V1SLURMJob.  # noqa: E501
        :type: str
        """

        self._work_dir = work_dir

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
        if issubclass(V1SLURMJob, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1SLURMJob') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SLURMJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1SLURMJob') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
