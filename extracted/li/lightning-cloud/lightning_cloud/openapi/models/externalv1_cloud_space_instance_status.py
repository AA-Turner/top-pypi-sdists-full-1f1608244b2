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

class Externalv1CloudSpaceInstanceStatus(object):
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
        'app_url': 'str',
        'cloud_space_id': 'str',
        'cloud_space_instance_id': 'str',
        'compute_config': 'V1UserRequestedComputeConfig',
        'creation_timestamp': 'datetime',
        'data_connection_mounts': 'list[V1DataConnectionMount]',
        'free': 'bool',
        'ide': 'str',
        'instance_id': 'str',
        'instance_region': 'str',
        'instance_url': 'str',
        'jupyterlab_url': 'str',
        'phase': 'V1CloudSpaceInstanceState',
        'ssh_host': 'str',
        'ssh_port': 'int',
        'ssh_username': 'str',
        'start_timestamp': 'datetime',
        'startup_eta_seconds': 'str',
        'startup_percentage': 'str',
        'startup_phase': 'str',
        'startup_status': 'V1CloudSpaceInstanceStartupStatus',
        'status_message': 'str',
        'sync_eta_seconds': 'str',
        'sync_in_progress': 'bool',
        'sync_percentage': 'str',
        'vscode_url': 'str'
    }

    attribute_map = {
        'app_url': 'appUrl',
        'cloud_space_id': 'cloudSpaceId',
        'cloud_space_instance_id': 'cloudSpaceInstanceId',
        'compute_config': 'computeConfig',
        'creation_timestamp': 'creationTimestamp',
        'data_connection_mounts': 'dataConnectionMounts',
        'free': 'free',
        'ide': 'ide',
        'instance_id': 'instanceId',
        'instance_region': 'instanceRegion',
        'instance_url': 'instanceUrl',
        'jupyterlab_url': 'jupyterlabUrl',
        'phase': 'phase',
        'ssh_host': 'sshHost',
        'ssh_port': 'sshPort',
        'ssh_username': 'sshUsername',
        'start_timestamp': 'startTimestamp',
        'startup_eta_seconds': 'startupEtaSeconds',
        'startup_percentage': 'startupPercentage',
        'startup_phase': 'startupPhase',
        'startup_status': 'startupStatus',
        'status_message': 'statusMessage',
        'sync_eta_seconds': 'syncEtaSeconds',
        'sync_in_progress': 'syncInProgress',
        'sync_percentage': 'syncPercentage',
        'vscode_url': 'vscodeUrl'
    }

    def __init__(self, app_url: 'str' =None, cloud_space_id: 'str' =None, cloud_space_instance_id: 'str' =None, compute_config: 'V1UserRequestedComputeConfig' =None, creation_timestamp: 'datetime' =None, data_connection_mounts: 'list[V1DataConnectionMount]' =None, free: 'bool' =None, ide: 'str' =None, instance_id: 'str' =None, instance_region: 'str' =None, instance_url: 'str' =None, jupyterlab_url: 'str' =None, phase: 'V1CloudSpaceInstanceState' =None, ssh_host: 'str' =None, ssh_port: 'int' =None, ssh_username: 'str' =None, start_timestamp: 'datetime' =None, startup_eta_seconds: 'str' =None, startup_percentage: 'str' =None, startup_phase: 'str' =None, startup_status: 'V1CloudSpaceInstanceStartupStatus' =None, status_message: 'str' =None, sync_eta_seconds: 'str' =None, sync_in_progress: 'bool' =None, sync_percentage: 'str' =None, vscode_url: 'str' =None):  # noqa: E501
        """Externalv1CloudSpaceInstanceStatus - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._cloud_space_id = None
        self._cloud_space_instance_id = None
        self._compute_config = None
        self._creation_timestamp = None
        self._data_connection_mounts = None
        self._free = None
        self._ide = None
        self._instance_id = None
        self._instance_region = None
        self._instance_url = None
        self._jupyterlab_url = None
        self._phase = None
        self._ssh_host = None
        self._ssh_port = None
        self._ssh_username = None
        self._start_timestamp = None
        self._startup_eta_seconds = None
        self._startup_percentage = None
        self._startup_phase = None
        self._startup_status = None
        self._status_message = None
        self._sync_eta_seconds = None
        self._sync_in_progress = None
        self._sync_percentage = None
        self._vscode_url = None
        self.discriminator = None
        if app_url is not None:
            self.app_url = app_url
        if cloud_space_id is not None:
            self.cloud_space_id = cloud_space_id
        if cloud_space_instance_id is not None:
            self.cloud_space_instance_id = cloud_space_instance_id
        if compute_config is not None:
            self.compute_config = compute_config
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if data_connection_mounts is not None:
            self.data_connection_mounts = data_connection_mounts
        if free is not None:
            self.free = free
        if ide is not None:
            self.ide = ide
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_region is not None:
            self.instance_region = instance_region
        if instance_url is not None:
            self.instance_url = instance_url
        if jupyterlab_url is not None:
            self.jupyterlab_url = jupyterlab_url
        if phase is not None:
            self.phase = phase
        if ssh_host is not None:
            self.ssh_host = ssh_host
        if ssh_port is not None:
            self.ssh_port = ssh_port
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if startup_eta_seconds is not None:
            self.startup_eta_seconds = startup_eta_seconds
        if startup_percentage is not None:
            self.startup_percentage = startup_percentage
        if startup_phase is not None:
            self.startup_phase = startup_phase
        if startup_status is not None:
            self.startup_status = startup_status
        if status_message is not None:
            self.status_message = status_message
        if sync_eta_seconds is not None:
            self.sync_eta_seconds = sync_eta_seconds
        if sync_in_progress is not None:
            self.sync_in_progress = sync_in_progress
        if sync_percentage is not None:
            self.sync_percentage = sync_percentage
        if vscode_url is not None:
            self.vscode_url = vscode_url

    @property
    def app_url(self) -> 'str':
        """Gets the app_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The app_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url: 'str'):
        """Sets the app_url of this Externalv1CloudSpaceInstanceStatus.


        :param app_url: The app_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._app_url = app_url

    @property
    def cloud_space_id(self) -> 'str':
        """Gets the cloud_space_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The cloud_space_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._cloud_space_id

    @cloud_space_id.setter
    def cloud_space_id(self, cloud_space_id: 'str'):
        """Sets the cloud_space_id of this Externalv1CloudSpaceInstanceStatus.


        :param cloud_space_id: The cloud_space_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._cloud_space_id = cloud_space_id

    @property
    def cloud_space_instance_id(self) -> 'str':
        """Gets the cloud_space_instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The cloud_space_instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._cloud_space_instance_id

    @cloud_space_instance_id.setter
    def cloud_space_instance_id(self, cloud_space_instance_id: 'str'):
        """Sets the cloud_space_instance_id of this Externalv1CloudSpaceInstanceStatus.


        :param cloud_space_instance_id: The cloud_space_instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._cloud_space_instance_id = cloud_space_instance_id

    @property
    def compute_config(self) -> 'V1UserRequestedComputeConfig':
        """Gets the compute_config of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The compute_config of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: V1UserRequestedComputeConfig
        """
        return self._compute_config

    @compute_config.setter
    def compute_config(self, compute_config: 'V1UserRequestedComputeConfig'):
        """Sets the compute_config of this Externalv1CloudSpaceInstanceStatus.


        :param compute_config: The compute_config of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: V1UserRequestedComputeConfig
        """

        self._compute_config = compute_config

    @property
    def creation_timestamp(self) -> 'datetime':
        """Gets the creation_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The creation_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp: 'datetime'):
        """Sets the creation_timestamp of this Externalv1CloudSpaceInstanceStatus.


        :param creation_timestamp: The creation_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def data_connection_mounts(self) -> 'list[V1DataConnectionMount]':
        """Gets the data_connection_mounts of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The data_connection_mounts of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: list[V1DataConnectionMount]
        """
        return self._data_connection_mounts

    @data_connection_mounts.setter
    def data_connection_mounts(self, data_connection_mounts: 'list[V1DataConnectionMount]'):
        """Sets the data_connection_mounts of this Externalv1CloudSpaceInstanceStatus.


        :param data_connection_mounts: The data_connection_mounts of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: list[V1DataConnectionMount]
        """

        self._data_connection_mounts = data_connection_mounts

    @property
    def free(self) -> 'bool':
        """Gets the free of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The free of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free: 'bool'):
        """Sets the free of this Externalv1CloudSpaceInstanceStatus.


        :param free: The free of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: bool
        """

        self._free = free

    @property
    def ide(self) -> 'str':
        """Gets the ide of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The ide of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._ide

    @ide.setter
    def ide(self, ide: 'str'):
        """Sets the ide of this Externalv1CloudSpaceInstanceStatus.


        :param ide: The ide of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._ide = ide

    @property
    def instance_id(self) -> 'str':
        """Gets the instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id: 'str'):
        """Sets the instance_id of this Externalv1CloudSpaceInstanceStatus.


        :param instance_id: The instance_id of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_region(self) -> 'str':
        """Gets the instance_region of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The instance_region of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._instance_region

    @instance_region.setter
    def instance_region(self, instance_region: 'str'):
        """Sets the instance_region of this Externalv1CloudSpaceInstanceStatus.


        :param instance_region: The instance_region of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._instance_region = instance_region

    @property
    def instance_url(self) -> 'str':
        """Gets the instance_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The instance_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url: 'str'):
        """Sets the instance_url of this Externalv1CloudSpaceInstanceStatus.


        :param instance_url: The instance_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._instance_url = instance_url

    @property
    def jupyterlab_url(self) -> 'str':
        """Gets the jupyterlab_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The jupyterlab_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._jupyterlab_url

    @jupyterlab_url.setter
    def jupyterlab_url(self, jupyterlab_url: 'str'):
        """Sets the jupyterlab_url of this Externalv1CloudSpaceInstanceStatus.


        :param jupyterlab_url: The jupyterlab_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._jupyterlab_url = jupyterlab_url

    @property
    def phase(self) -> 'V1CloudSpaceInstanceState':
        """Gets the phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: V1CloudSpaceInstanceState
        """
        return self._phase

    @phase.setter
    def phase(self, phase: 'V1CloudSpaceInstanceState'):
        """Sets the phase of this Externalv1CloudSpaceInstanceStatus.


        :param phase: The phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: V1CloudSpaceInstanceState
        """

        self._phase = phase

    @property
    def ssh_host(self) -> 'str':
        """Gets the ssh_host of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The ssh_host of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._ssh_host

    @ssh_host.setter
    def ssh_host(self, ssh_host: 'str'):
        """Sets the ssh_host of this Externalv1CloudSpaceInstanceStatus.


        :param ssh_host: The ssh_host of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._ssh_host = ssh_host

    @property
    def ssh_port(self) -> 'int':
        """Gets the ssh_port of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The ssh_port of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: int
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port: 'int'):
        """Sets the ssh_port of this Externalv1CloudSpaceInstanceStatus.


        :param ssh_port: The ssh_port of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: int
        """

        self._ssh_port = ssh_port

    @property
    def ssh_username(self) -> 'str':
        """Gets the ssh_username of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The ssh_username of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username: 'str'):
        """Sets the ssh_username of this Externalv1CloudSpaceInstanceStatus.


        :param ssh_username: The ssh_username of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._ssh_username = ssh_username

    @property
    def start_timestamp(self) -> 'datetime':
        """Gets the start_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The start_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp: 'datetime'):
        """Sets the start_timestamp of this Externalv1CloudSpaceInstanceStatus.


        :param start_timestamp: The start_timestamp of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def startup_eta_seconds(self) -> 'str':
        """Gets the startup_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The startup_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._startup_eta_seconds

    @startup_eta_seconds.setter
    def startup_eta_seconds(self, startup_eta_seconds: 'str'):
        """Sets the startup_eta_seconds of this Externalv1CloudSpaceInstanceStatus.


        :param startup_eta_seconds: The startup_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._startup_eta_seconds = startup_eta_seconds

    @property
    def startup_percentage(self) -> 'str':
        """Gets the startup_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The startup_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._startup_percentage

    @startup_percentage.setter
    def startup_percentage(self, startup_percentage: 'str'):
        """Sets the startup_percentage of this Externalv1CloudSpaceInstanceStatus.


        :param startup_percentage: The startup_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._startup_percentage = startup_percentage

    @property
    def startup_phase(self) -> 'str':
        """Gets the startup_phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The startup_phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._startup_phase

    @startup_phase.setter
    def startup_phase(self, startup_phase: 'str'):
        """Sets the startup_phase of this Externalv1CloudSpaceInstanceStatus.


        :param startup_phase: The startup_phase of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._startup_phase = startup_phase

    @property
    def startup_status(self) -> 'V1CloudSpaceInstanceStartupStatus':
        """Gets the startup_status of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The startup_status of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: V1CloudSpaceInstanceStartupStatus
        """
        return self._startup_status

    @startup_status.setter
    def startup_status(self, startup_status: 'V1CloudSpaceInstanceStartupStatus'):
        """Sets the startup_status of this Externalv1CloudSpaceInstanceStatus.


        :param startup_status: The startup_status of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: V1CloudSpaceInstanceStartupStatus
        """

        self._startup_status = startup_status

    @property
    def status_message(self) -> 'str':
        """Gets the status_message of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The status_message of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message: 'str'):
        """Sets the status_message of this Externalv1CloudSpaceInstanceStatus.


        :param status_message: The status_message of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def sync_eta_seconds(self) -> 'str':
        """Gets the sync_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The sync_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._sync_eta_seconds

    @sync_eta_seconds.setter
    def sync_eta_seconds(self, sync_eta_seconds: 'str'):
        """Sets the sync_eta_seconds of this Externalv1CloudSpaceInstanceStatus.


        :param sync_eta_seconds: The sync_eta_seconds of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._sync_eta_seconds = sync_eta_seconds

    @property
    def sync_in_progress(self) -> 'bool':
        """Gets the sync_in_progress of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The sync_in_progress of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: bool
        """
        return self._sync_in_progress

    @sync_in_progress.setter
    def sync_in_progress(self, sync_in_progress: 'bool'):
        """Sets the sync_in_progress of this Externalv1CloudSpaceInstanceStatus.


        :param sync_in_progress: The sync_in_progress of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: bool
        """

        self._sync_in_progress = sync_in_progress

    @property
    def sync_percentage(self) -> 'str':
        """Gets the sync_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The sync_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._sync_percentage

    @sync_percentage.setter
    def sync_percentage(self, sync_percentage: 'str'):
        """Sets the sync_percentage of this Externalv1CloudSpaceInstanceStatus.


        :param sync_percentage: The sync_percentage of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._sync_percentage = sync_percentage

    @property
    def vscode_url(self) -> 'str':
        """Gets the vscode_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501


        :return: The vscode_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._vscode_url

    @vscode_url.setter
    def vscode_url(self, vscode_url: 'str'):
        """Sets the vscode_url of this Externalv1CloudSpaceInstanceStatus.


        :param vscode_url: The vscode_url of this Externalv1CloudSpaceInstanceStatus.  # noqa: E501
        :type: str
        """

        self._vscode_url = vscode_url

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
        if issubclass(Externalv1CloudSpaceInstanceStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'Externalv1CloudSpaceInstanceStatus') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, Externalv1CloudSpaceInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Externalv1CloudSpaceInstanceStatus') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
