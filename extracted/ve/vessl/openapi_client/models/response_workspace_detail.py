# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ResponseWorkspaceDetail(object):
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
        'backup_volume_id': 'int',
        'created_by': 'ResponseUser',
        'created_dt': 'datetime',
        'end_dt': 'datetime',
        'endpoints': 'ResponseWorkloadEndpoints',
        'exit_code': 'int',
        'histories': 'list[ResponseWorkloadHistoryInfo]',
        'id': 'int',
        'idle_shutdown_minutes': 'int',
        'init_script': 'str',
        'kernel_cluster': 'ResponseKernelCluster',
        'kernel_cluster_node': 'ResponseKernelClusterNode',
        'kernel_cluster_select_policies': 'OrmKernelClusterSelectPolicies',
        'kernel_image': 'ResponseKernelImage',
        'kernel_resource_spec': 'ResponseKernelResourceSpec',
        'kubernetes_resource_info': 'ResponseKubernetesResourceInfo',
        'last_backup': 'ResponseWorkspaceBackup',
        'last_backup_succeeded': 'bool',
        'max_running_hours': 'int',
        'name': 'str',
        'organization': 'ResponseOrganization',
        'ports': 'OrmWorkspacePorts',
        'service_account_name': 'str',
        'start_command': 'str',
        'status': 'str',
        'status_last_updated': 'datetime',
        'status_reason': 'str',
        'updated_dt': 'datetime',
        'volume_mounts': 'ResponseVolumeMountInfos',
        'volume_v2_mounts': 'ResponseLegacyWorkloadVolumeV2Mounts'
    }

    attribute_map = {
        'backup_volume_id': 'backup_volume_id',
        'created_by': 'created_by',
        'created_dt': 'created_dt',
        'end_dt': 'end_dt',
        'endpoints': 'endpoints',
        'exit_code': 'exit_code',
        'histories': 'histories',
        'id': 'id',
        'idle_shutdown_minutes': 'idle_shutdown_minutes',
        'init_script': 'init_script',
        'kernel_cluster': 'kernel_cluster',
        'kernel_cluster_node': 'kernel_cluster_node',
        'kernel_cluster_select_policies': 'kernel_cluster_select_policies',
        'kernel_image': 'kernel_image',
        'kernel_resource_spec': 'kernel_resource_spec',
        'kubernetes_resource_info': 'kubernetes_resource_info',
        'last_backup': 'last_backup',
        'last_backup_succeeded': 'last_backup_succeeded',
        'max_running_hours': 'max_running_hours',
        'name': 'name',
        'organization': 'organization',
        'ports': 'ports',
        'service_account_name': 'service_account_name',
        'start_command': 'start_command',
        'status': 'status',
        'status_last_updated': 'status_last_updated',
        'status_reason': 'status_reason',
        'updated_dt': 'updated_dt',
        'volume_mounts': 'volume_mounts',
        'volume_v2_mounts': 'volume_v2_mounts'
    }

    def __init__(self, backup_volume_id=None, created_by=None, created_dt=None, end_dt=None, endpoints=None, exit_code=None, histories=None, id=None, idle_shutdown_minutes=None, init_script=None, kernel_cluster=None, kernel_cluster_node=None, kernel_cluster_select_policies=None, kernel_image=None, kernel_resource_spec=None, kubernetes_resource_info=None, last_backup=None, last_backup_succeeded=None, max_running_hours=None, name=None, organization=None, ports=None, service_account_name=None, start_command=None, status=None, status_last_updated=None, status_reason=None, updated_dt=None, volume_mounts=None, volume_v2_mounts=None, local_vars_configuration=None):  # noqa: E501
        """ResponseWorkspaceDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._backup_volume_id = None
        self._created_by = None
        self._created_dt = None
        self._end_dt = None
        self._endpoints = None
        self._exit_code = None
        self._histories = None
        self._id = None
        self._idle_shutdown_minutes = None
        self._init_script = None
        self._kernel_cluster = None
        self._kernel_cluster_node = None
        self._kernel_cluster_select_policies = None
        self._kernel_image = None
        self._kernel_resource_spec = None
        self._kubernetes_resource_info = None
        self._last_backup = None
        self._last_backup_succeeded = None
        self._max_running_hours = None
        self._name = None
        self._organization = None
        self._ports = None
        self._service_account_name = None
        self._start_command = None
        self._status = None
        self._status_last_updated = None
        self._status_reason = None
        self._updated_dt = None
        self._volume_mounts = None
        self._volume_v2_mounts = None
        self.discriminator = None

        self.backup_volume_id = backup_volume_id
        self.created_by = created_by
        if created_dt is not None:
            self.created_dt = created_dt
        self.end_dt = end_dt
        if endpoints is not None:
            self.endpoints = endpoints
        self.exit_code = exit_code
        self.histories = histories
        self.id = id
        if idle_shutdown_minutes is not None:
            self.idle_shutdown_minutes = idle_shutdown_minutes
        self.init_script = init_script
        if kernel_cluster is not None:
            self.kernel_cluster = kernel_cluster
        if kernel_cluster_node is not None:
            self.kernel_cluster_node = kernel_cluster_node
        self.kernel_cluster_select_policies = kernel_cluster_select_policies
        self.kernel_image = kernel_image
        self.kernel_resource_spec = kernel_resource_spec
        if kubernetes_resource_info is not None:
            self.kubernetes_resource_info = kubernetes_resource_info
        if last_backup is not None:
            self.last_backup = last_backup
        self.last_backup_succeeded = last_backup_succeeded
        if max_running_hours is not None:
            self.max_running_hours = max_running_hours
        self.name = name
        self.organization = organization
        if ports is not None:
            self.ports = ports
        if service_account_name is not None:
            self.service_account_name = service_account_name
        self.start_command = start_command
        self.status = status
        self.status_last_updated = status_last_updated
        self.status_reason = status_reason
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if volume_v2_mounts is not None:
            self.volume_v2_mounts = volume_v2_mounts

    @property
    def backup_volume_id(self):
        """Gets the backup_volume_id of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The backup_volume_id of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: int
        """
        return self._backup_volume_id

    @backup_volume_id.setter
    def backup_volume_id(self, backup_volume_id):
        """Sets the backup_volume_id of this ResponseWorkspaceDetail.


        :param backup_volume_id: The backup_volume_id of this ResponseWorkspaceDetail.  # noqa: E501
        :type backup_volume_id: int
        """
        if self.local_vars_configuration.client_side_validation and backup_volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_volume_id`, must not be `None`")  # noqa: E501

        self._backup_volume_id = backup_volume_id

    @property
    def created_by(self):
        """Gets the created_by of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The created_by of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResponseWorkspaceDetail.


        :param created_by: The created_by of this ResponseWorkspaceDetail.  # noqa: E501
        :type created_by: ResponseUser
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The created_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseWorkspaceDetail.


        :param created_dt: The created_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def end_dt(self):
        """Gets the end_dt of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The end_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._end_dt

    @end_dt.setter
    def end_dt(self, end_dt):
        """Sets the end_dt of this ResponseWorkspaceDetail.


        :param end_dt: The end_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :type end_dt: datetime
        """

        self._end_dt = end_dt

    @property
    def endpoints(self):
        """Gets the endpoints of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The endpoints of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseWorkloadEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ResponseWorkspaceDetail.


        :param endpoints: The endpoints of this ResponseWorkspaceDetail.  # noqa: E501
        :type endpoints: ResponseWorkloadEndpoints
        """

        self._endpoints = endpoints

    @property
    def exit_code(self):
        """Gets the exit_code of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The exit_code of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this ResponseWorkspaceDetail.


        :param exit_code: The exit_code of this ResponseWorkspaceDetail.  # noqa: E501
        :type exit_code: int
        """

        self._exit_code = exit_code

    @property
    def histories(self):
        """Gets the histories of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The histories of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: list[ResponseWorkloadHistoryInfo]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ResponseWorkspaceDetail.


        :param histories: The histories of this ResponseWorkspaceDetail.  # noqa: E501
        :type histories: list[ResponseWorkloadHistoryInfo]
        """
        if self.local_vars_configuration.client_side_validation and histories is None:  # noqa: E501
            raise ValueError("Invalid value for `histories`, must not be `None`")  # noqa: E501

        self._histories = histories

    @property
    def id(self):
        """Gets the id of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The id of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseWorkspaceDetail.


        :param id: The id of this ResponseWorkspaceDetail.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def idle_shutdown_minutes(self):
        """Gets the idle_shutdown_minutes of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The idle_shutdown_minutes of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: int
        """
        return self._idle_shutdown_minutes

    @idle_shutdown_minutes.setter
    def idle_shutdown_minutes(self, idle_shutdown_minutes):
        """Sets the idle_shutdown_minutes of this ResponseWorkspaceDetail.


        :param idle_shutdown_minutes: The idle_shutdown_minutes of this ResponseWorkspaceDetail.  # noqa: E501
        :type idle_shutdown_minutes: int
        """

        self._idle_shutdown_minutes = idle_shutdown_minutes

    @property
    def init_script(self):
        """Gets the init_script of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The init_script of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._init_script

    @init_script.setter
    def init_script(self, init_script):
        """Sets the init_script of this ResponseWorkspaceDetail.


        :param init_script: The init_script of this ResponseWorkspaceDetail.  # noqa: E501
        :type init_script: str
        """

        self._init_script = init_script

    @property
    def kernel_cluster(self):
        """Gets the kernel_cluster of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kernel_cluster of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseKernelCluster
        """
        return self._kernel_cluster

    @kernel_cluster.setter
    def kernel_cluster(self, kernel_cluster):
        """Sets the kernel_cluster of this ResponseWorkspaceDetail.


        :param kernel_cluster: The kernel_cluster of this ResponseWorkspaceDetail.  # noqa: E501
        :type kernel_cluster: ResponseKernelCluster
        """

        self._kernel_cluster = kernel_cluster

    @property
    def kernel_cluster_node(self):
        """Gets the kernel_cluster_node of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kernel_cluster_node of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseKernelClusterNode
        """
        return self._kernel_cluster_node

    @kernel_cluster_node.setter
    def kernel_cluster_node(self, kernel_cluster_node):
        """Sets the kernel_cluster_node of this ResponseWorkspaceDetail.


        :param kernel_cluster_node: The kernel_cluster_node of this ResponseWorkspaceDetail.  # noqa: E501
        :type kernel_cluster_node: ResponseKernelClusterNode
        """

        self._kernel_cluster_node = kernel_cluster_node

    @property
    def kernel_cluster_select_policies(self):
        """Gets the kernel_cluster_select_policies of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kernel_cluster_select_policies of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: OrmKernelClusterSelectPolicies
        """
        return self._kernel_cluster_select_policies

    @kernel_cluster_select_policies.setter
    def kernel_cluster_select_policies(self, kernel_cluster_select_policies):
        """Sets the kernel_cluster_select_policies of this ResponseWorkspaceDetail.


        :param kernel_cluster_select_policies: The kernel_cluster_select_policies of this ResponseWorkspaceDetail.  # noqa: E501
        :type kernel_cluster_select_policies: OrmKernelClusterSelectPolicies
        """
        if self.local_vars_configuration.client_side_validation and kernel_cluster_select_policies is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_cluster_select_policies`, must not be `None`")  # noqa: E501

        self._kernel_cluster_select_policies = kernel_cluster_select_policies

    @property
    def kernel_image(self):
        """Gets the kernel_image of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kernel_image of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseKernelImage
        """
        return self._kernel_image

    @kernel_image.setter
    def kernel_image(self, kernel_image):
        """Sets the kernel_image of this ResponseWorkspaceDetail.


        :param kernel_image: The kernel_image of this ResponseWorkspaceDetail.  # noqa: E501
        :type kernel_image: ResponseKernelImage
        """
        if self.local_vars_configuration.client_side_validation and kernel_image is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_image`, must not be `None`")  # noqa: E501

        self._kernel_image = kernel_image

    @property
    def kernel_resource_spec(self):
        """Gets the kernel_resource_spec of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kernel_resource_spec of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseKernelResourceSpec
        """
        return self._kernel_resource_spec

    @kernel_resource_spec.setter
    def kernel_resource_spec(self, kernel_resource_spec):
        """Sets the kernel_resource_spec of this ResponseWorkspaceDetail.


        :param kernel_resource_spec: The kernel_resource_spec of this ResponseWorkspaceDetail.  # noqa: E501
        :type kernel_resource_spec: ResponseKernelResourceSpec
        """
        if self.local_vars_configuration.client_side_validation and kernel_resource_spec is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_resource_spec`, must not be `None`")  # noqa: E501

        self._kernel_resource_spec = kernel_resource_spec

    @property
    def kubernetes_resource_info(self):
        """Gets the kubernetes_resource_info of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The kubernetes_resource_info of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseKubernetesResourceInfo
        """
        return self._kubernetes_resource_info

    @kubernetes_resource_info.setter
    def kubernetes_resource_info(self, kubernetes_resource_info):
        """Sets the kubernetes_resource_info of this ResponseWorkspaceDetail.


        :param kubernetes_resource_info: The kubernetes_resource_info of this ResponseWorkspaceDetail.  # noqa: E501
        :type kubernetes_resource_info: ResponseKubernetesResourceInfo
        """

        self._kubernetes_resource_info = kubernetes_resource_info

    @property
    def last_backup(self):
        """Gets the last_backup of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The last_backup of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseWorkspaceBackup
        """
        return self._last_backup

    @last_backup.setter
    def last_backup(self, last_backup):
        """Sets the last_backup of this ResponseWorkspaceDetail.


        :param last_backup: The last_backup of this ResponseWorkspaceDetail.  # noqa: E501
        :type last_backup: ResponseWorkspaceBackup
        """

        self._last_backup = last_backup

    @property
    def last_backup_succeeded(self):
        """Gets the last_backup_succeeded of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The last_backup_succeeded of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: bool
        """
        return self._last_backup_succeeded

    @last_backup_succeeded.setter
    def last_backup_succeeded(self, last_backup_succeeded):
        """Sets the last_backup_succeeded of this ResponseWorkspaceDetail.


        :param last_backup_succeeded: The last_backup_succeeded of this ResponseWorkspaceDetail.  # noqa: E501
        :type last_backup_succeeded: bool
        """

        self._last_backup_succeeded = last_backup_succeeded

    @property
    def max_running_hours(self):
        """Gets the max_running_hours of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The max_running_hours of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: int
        """
        return self._max_running_hours

    @max_running_hours.setter
    def max_running_hours(self, max_running_hours):
        """Sets the max_running_hours of this ResponseWorkspaceDetail.


        :param max_running_hours: The max_running_hours of this ResponseWorkspaceDetail.  # noqa: E501
        :type max_running_hours: int
        """

        self._max_running_hours = max_running_hours

    @property
    def name(self):
        """Gets the name of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The name of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseWorkspaceDetail.


        :param name: The name of this ResponseWorkspaceDetail.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The organization of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ResponseWorkspaceDetail.


        :param organization: The organization of this ResponseWorkspaceDetail.  # noqa: E501
        :type organization: ResponseOrganization
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def ports(self):
        """Gets the ports of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The ports of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: OrmWorkspacePorts
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ResponseWorkspaceDetail.


        :param ports: The ports of this ResponseWorkspaceDetail.  # noqa: E501
        :type ports: OrmWorkspacePorts
        """

        self._ports = ports

    @property
    def service_account_name(self):
        """Gets the service_account_name of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The service_account_name of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this ResponseWorkspaceDetail.


        :param service_account_name: The service_account_name of this ResponseWorkspaceDetail.  # noqa: E501
        :type service_account_name: str
        """

        self._service_account_name = service_account_name

    @property
    def start_command(self):
        """Gets the start_command of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The start_command of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._start_command

    @start_command.setter
    def start_command(self, start_command):
        """Sets the start_command of this ResponseWorkspaceDetail.


        :param start_command: The start_command of this ResponseWorkspaceDetail.  # noqa: E501
        :type start_command: str
        """

        self._start_command = start_command

    @property
    def status(self):
        """Gets the status of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The status of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseWorkspaceDetail.


        :param status: The status of this ResponseWorkspaceDetail.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_last_updated(self):
        """Gets the status_last_updated of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The status_last_updated of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._status_last_updated

    @status_last_updated.setter
    def status_last_updated(self, status_last_updated):
        """Sets the status_last_updated of this ResponseWorkspaceDetail.


        :param status_last_updated: The status_last_updated of this ResponseWorkspaceDetail.  # noqa: E501
        :type status_last_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and status_last_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `status_last_updated`, must not be `None`")  # noqa: E501

        self._status_last_updated = status_last_updated

    @property
    def status_reason(self):
        """Gets the status_reason of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The status_reason of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ResponseWorkspaceDetail.


        :param status_reason: The status_reason of this ResponseWorkspaceDetail.  # noqa: E501
        :type status_reason: str
        """
        if self.local_vars_configuration.client_side_validation and status_reason is None:  # noqa: E501
            raise ValueError("Invalid value for `status_reason`, must not be `None`")  # noqa: E501

        self._status_reason = status_reason

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The updated_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseWorkspaceDetail.


        :param updated_dt: The updated_dt of this ResponseWorkspaceDetail.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The volume_mounts of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseVolumeMountInfos
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this ResponseWorkspaceDetail.


        :param volume_mounts: The volume_mounts of this ResponseWorkspaceDetail.  # noqa: E501
        :type volume_mounts: ResponseVolumeMountInfos
        """

        self._volume_mounts = volume_mounts

    @property
    def volume_v2_mounts(self):
        """Gets the volume_v2_mounts of this ResponseWorkspaceDetail.  # noqa: E501


        :return: The volume_v2_mounts of this ResponseWorkspaceDetail.  # noqa: E501
        :rtype: ResponseLegacyWorkloadVolumeV2Mounts
        """
        return self._volume_v2_mounts

    @volume_v2_mounts.setter
    def volume_v2_mounts(self, volume_v2_mounts):
        """Sets the volume_v2_mounts of this ResponseWorkspaceDetail.


        :param volume_v2_mounts: The volume_v2_mounts of this ResponseWorkspaceDetail.  # noqa: E501
        :type volume_v2_mounts: ResponseLegacyWorkloadVolumeV2Mounts
        """

        self._volume_v2_mounts = volume_v2_mounts

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseWorkspaceDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseWorkspaceDetail):
            return True

        return self.to_dict() != other.to_dict()
