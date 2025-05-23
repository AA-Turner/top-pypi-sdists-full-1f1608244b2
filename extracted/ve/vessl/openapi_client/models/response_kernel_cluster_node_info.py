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


class ResponseKernelClusterNodeInfo(object):
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
        'cpu_allocatable': 'float',
        'cpu_limits': 'float',
        'cpu_requests': 'float',
        'created_dt': 'datetime',
        'current_system_metrics': 'list[InfluxdbCurrentSystemMetric]',
        'ephemeral_storage_allocatable': 'int',
        'ephemeral_storage_limits': 'int',
        'ephemeral_storage_requests': 'int',
        'experiments': 'list[ResponseExperimentListResponse]',
        'gpu_allocatable': 'int',
        'gpu_limits': 'int',
        'gpu_product_name': 'str',
        'gpu_requests': 'int',
        'id': 'int',
        'internal_ip': 'str',
        'issues': 'list[str]',
        'memory_allocatable': 'int',
        'memory_limits': 'int',
        'memory_requests': 'int',
        'name': 'str',
        'status': 'str',
        'updated_dt': 'datetime',
        'workloads_summary': 'OrmWorkloadsSummary',
        'workspaces': 'list[ResponseWorkspaceList]'
    }

    attribute_map = {
        'cpu_allocatable': 'cpu_allocatable',
        'cpu_limits': 'cpu_limits',
        'cpu_requests': 'cpu_requests',
        'created_dt': 'created_dt',
        'current_system_metrics': 'current_system_metrics',
        'ephemeral_storage_allocatable': 'ephemeral_storage_allocatable',
        'ephemeral_storage_limits': 'ephemeral_storage_limits',
        'ephemeral_storage_requests': 'ephemeral_storage_requests',
        'experiments': 'experiments',
        'gpu_allocatable': 'gpu_allocatable',
        'gpu_limits': 'gpu_limits',
        'gpu_product_name': 'gpu_product_name',
        'gpu_requests': 'gpu_requests',
        'id': 'id',
        'internal_ip': 'internal_ip',
        'issues': 'issues',
        'memory_allocatable': 'memory_allocatable',
        'memory_limits': 'memory_limits',
        'memory_requests': 'memory_requests',
        'name': 'name',
        'status': 'status',
        'updated_dt': 'updated_dt',
        'workloads_summary': 'workloads_summary',
        'workspaces': 'workspaces'
    }

    def __init__(self, cpu_allocatable=None, cpu_limits=None, cpu_requests=None, created_dt=None, current_system_metrics=None, ephemeral_storage_allocatable=None, ephemeral_storage_limits=None, ephemeral_storage_requests=None, experiments=None, gpu_allocatable=None, gpu_limits=None, gpu_product_name=None, gpu_requests=None, id=None, internal_ip=None, issues=None, memory_allocatable=None, memory_limits=None, memory_requests=None, name=None, status=None, updated_dt=None, workloads_summary=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelClusterNodeInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_allocatable = None
        self._cpu_limits = None
        self._cpu_requests = None
        self._created_dt = None
        self._current_system_metrics = None
        self._ephemeral_storage_allocatable = None
        self._ephemeral_storage_limits = None
        self._ephemeral_storage_requests = None
        self._experiments = None
        self._gpu_allocatable = None
        self._gpu_limits = None
        self._gpu_product_name = None
        self._gpu_requests = None
        self._id = None
        self._internal_ip = None
        self._issues = None
        self._memory_allocatable = None
        self._memory_limits = None
        self._memory_requests = None
        self._name = None
        self._status = None
        self._updated_dt = None
        self._workloads_summary = None
        self._workspaces = None
        self.discriminator = None

        self.cpu_allocatable = cpu_allocatable
        self.cpu_limits = cpu_limits
        self.cpu_requests = cpu_requests
        self.created_dt = created_dt
        self.current_system_metrics = current_system_metrics
        self.ephemeral_storage_allocatable = ephemeral_storage_allocatable
        self.ephemeral_storage_limits = ephemeral_storage_limits
        self.ephemeral_storage_requests = ephemeral_storage_requests
        if experiments is not None:
            self.experiments = experiments
        self.gpu_allocatable = gpu_allocatable
        self.gpu_limits = gpu_limits
        self.gpu_product_name = gpu_product_name
        self.gpu_requests = gpu_requests
        self.id = id
        self.internal_ip = internal_ip
        self.issues = issues
        self.memory_allocatable = memory_allocatable
        self.memory_limits = memory_limits
        self.memory_requests = memory_requests
        self.name = name
        self.status = status
        self.updated_dt = updated_dt
        self.workloads_summary = workloads_summary
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def cpu_allocatable(self):
        """Gets the cpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The cpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: float
        """
        return self._cpu_allocatable

    @cpu_allocatable.setter
    def cpu_allocatable(self, cpu_allocatable):
        """Sets the cpu_allocatable of this ResponseKernelClusterNodeInfo.


        :param cpu_allocatable: The cpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type cpu_allocatable: float
        """

        self._cpu_allocatable = cpu_allocatable

    @property
    def cpu_limits(self):
        """Gets the cpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The cpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: float
        """
        return self._cpu_limits

    @cpu_limits.setter
    def cpu_limits(self, cpu_limits):
        """Sets the cpu_limits of this ResponseKernelClusterNodeInfo.


        :param cpu_limits: The cpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type cpu_limits: float
        """

        self._cpu_limits = cpu_limits

    @property
    def cpu_requests(self):
        """Gets the cpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The cpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: float
        """
        return self._cpu_requests

    @cpu_requests.setter
    def cpu_requests(self, cpu_requests):
        """Sets the cpu_requests of this ResponseKernelClusterNodeInfo.


        :param cpu_requests: The cpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type cpu_requests: float
        """

        self._cpu_requests = cpu_requests

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The created_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelClusterNodeInfo.


        :param created_dt: The created_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def current_system_metrics(self):
        """Gets the current_system_metrics of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The current_system_metrics of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: list[InfluxdbCurrentSystemMetric]
        """
        return self._current_system_metrics

    @current_system_metrics.setter
    def current_system_metrics(self, current_system_metrics):
        """Sets the current_system_metrics of this ResponseKernelClusterNodeInfo.


        :param current_system_metrics: The current_system_metrics of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type current_system_metrics: list[InfluxdbCurrentSystemMetric]
        """
        if self.local_vars_configuration.client_side_validation and current_system_metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `current_system_metrics`, must not be `None`")  # noqa: E501

        self._current_system_metrics = current_system_metrics

    @property
    def ephemeral_storage_allocatable(self):
        """Gets the ephemeral_storage_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The ephemeral_storage_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_allocatable

    @ephemeral_storage_allocatable.setter
    def ephemeral_storage_allocatable(self, ephemeral_storage_allocatable):
        """Sets the ephemeral_storage_allocatable of this ResponseKernelClusterNodeInfo.


        :param ephemeral_storage_allocatable: The ephemeral_storage_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type ephemeral_storage_allocatable: int
        """

        self._ephemeral_storage_allocatable = ephemeral_storage_allocatable

    @property
    def ephemeral_storage_limits(self):
        """Gets the ephemeral_storage_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The ephemeral_storage_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_limits

    @ephemeral_storage_limits.setter
    def ephemeral_storage_limits(self, ephemeral_storage_limits):
        """Sets the ephemeral_storage_limits of this ResponseKernelClusterNodeInfo.


        :param ephemeral_storage_limits: The ephemeral_storage_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type ephemeral_storage_limits: int
        """

        self._ephemeral_storage_limits = ephemeral_storage_limits

    @property
    def ephemeral_storage_requests(self):
        """Gets the ephemeral_storage_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The ephemeral_storage_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_requests

    @ephemeral_storage_requests.setter
    def ephemeral_storage_requests(self, ephemeral_storage_requests):
        """Sets the ephemeral_storage_requests of this ResponseKernelClusterNodeInfo.


        :param ephemeral_storage_requests: The ephemeral_storage_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type ephemeral_storage_requests: int
        """

        self._ephemeral_storage_requests = ephemeral_storage_requests

    @property
    def experiments(self):
        """Gets the experiments of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The experiments of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: list[ResponseExperimentListResponse]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this ResponseKernelClusterNodeInfo.


        :param experiments: The experiments of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type experiments: list[ResponseExperimentListResponse]
        """

        self._experiments = experiments

    @property
    def gpu_allocatable(self):
        """Gets the gpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The gpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._gpu_allocatable

    @gpu_allocatable.setter
    def gpu_allocatable(self, gpu_allocatable):
        """Sets the gpu_allocatable of this ResponseKernelClusterNodeInfo.


        :param gpu_allocatable: The gpu_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type gpu_allocatable: int
        """

        self._gpu_allocatable = gpu_allocatable

    @property
    def gpu_limits(self):
        """Gets the gpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The gpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._gpu_limits

    @gpu_limits.setter
    def gpu_limits(self, gpu_limits):
        """Sets the gpu_limits of this ResponseKernelClusterNodeInfo.


        :param gpu_limits: The gpu_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type gpu_limits: int
        """

        self._gpu_limits = gpu_limits

    @property
    def gpu_product_name(self):
        """Gets the gpu_product_name of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The gpu_product_name of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._gpu_product_name

    @gpu_product_name.setter
    def gpu_product_name(self, gpu_product_name):
        """Sets the gpu_product_name of this ResponseKernelClusterNodeInfo.


        :param gpu_product_name: The gpu_product_name of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type gpu_product_name: str
        """

        self._gpu_product_name = gpu_product_name

    @property
    def gpu_requests(self):
        """Gets the gpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The gpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._gpu_requests

    @gpu_requests.setter
    def gpu_requests(self, gpu_requests):
        """Sets the gpu_requests of this ResponseKernelClusterNodeInfo.


        :param gpu_requests: The gpu_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type gpu_requests: int
        """

        self._gpu_requests = gpu_requests

    @property
    def id(self):
        """Gets the id of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The id of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelClusterNodeInfo.


        :param id: The id of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def internal_ip(self):
        """Gets the internal_ip of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The internal_ip of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this ResponseKernelClusterNodeInfo.


        :param internal_ip: The internal_ip of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type internal_ip: str
        """

        self._internal_ip = internal_ip

    @property
    def issues(self):
        """Gets the issues of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The issues of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this ResponseKernelClusterNodeInfo.


        :param issues: The issues of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type issues: list[str]
        """
        if self.local_vars_configuration.client_side_validation and issues is None:  # noqa: E501
            raise ValueError("Invalid value for `issues`, must not be `None`")  # noqa: E501

        self._issues = issues

    @property
    def memory_allocatable(self):
        """Gets the memory_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The memory_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocatable

    @memory_allocatable.setter
    def memory_allocatable(self, memory_allocatable):
        """Sets the memory_allocatable of this ResponseKernelClusterNodeInfo.


        :param memory_allocatable: The memory_allocatable of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type memory_allocatable: int
        """

        self._memory_allocatable = memory_allocatable

    @property
    def memory_limits(self):
        """Gets the memory_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The memory_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._memory_limits

    @memory_limits.setter
    def memory_limits(self, memory_limits):
        """Sets the memory_limits of this ResponseKernelClusterNodeInfo.


        :param memory_limits: The memory_limits of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type memory_limits: int
        """

        self._memory_limits = memory_limits

    @property
    def memory_requests(self):
        """Gets the memory_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The memory_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._memory_requests

    @memory_requests.setter
    def memory_requests(self, memory_requests):
        """Sets the memory_requests of this ResponseKernelClusterNodeInfo.


        :param memory_requests: The memory_requests of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type memory_requests: int
        """

        self._memory_requests = memory_requests

    @property
    def name(self):
        """Gets the name of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The name of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelClusterNodeInfo.


        :param name: The name of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The status of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseKernelClusterNodeInfo.


        :param status: The status of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The updated_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelClusterNodeInfo.


        :param updated_dt: The updated_dt of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def workloads_summary(self):
        """Gets the workloads_summary of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The workloads_summary of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: OrmWorkloadsSummary
        """
        return self._workloads_summary

    @workloads_summary.setter
    def workloads_summary(self, workloads_summary):
        """Sets the workloads_summary of this ResponseKernelClusterNodeInfo.


        :param workloads_summary: The workloads_summary of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type workloads_summary: OrmWorkloadsSummary
        """
        if self.local_vars_configuration.client_side_validation and workloads_summary is None:  # noqa: E501
            raise ValueError("Invalid value for `workloads_summary`, must not be `None`")  # noqa: E501

        self._workloads_summary = workloads_summary

    @property
    def workspaces(self):
        """Gets the workspaces of this ResponseKernelClusterNodeInfo.  # noqa: E501


        :return: The workspaces of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :rtype: list[ResponseWorkspaceList]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this ResponseKernelClusterNodeInfo.


        :param workspaces: The workspaces of this ResponseKernelClusterNodeInfo.  # noqa: E501
        :type workspaces: list[ResponseWorkspaceList]
        """

        self._workspaces = workspaces

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
        if not isinstance(other, ResponseKernelClusterNodeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelClusterNodeInfo):
            return True

        return self.to_dict() != other.to_dict()
