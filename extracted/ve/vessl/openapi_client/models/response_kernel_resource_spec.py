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


class ResponseKernelResourceSpec(object):
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
        'cpu_limit': 'float',
        'cpu_type': 'str',
        'created_dt': 'datetime',
        'default_hourly_credit': 'int',
        'deleted_dt': 'datetime',
        'description': 'str',
        'experiment_enabled': 'bool',
        'gpu_limit': 'int',
        'gpu_type': 'str',
        'id': 'int',
        'memory_limit': 'str',
        'name': 'str',
        'node_selector': 'OrmKernelResourceSpecNodeSelector',
        'pricing_plan_eligible': 'bool',
        'priority': 'int',
        'processor_type': 'str',
        'spot': 'bool',
        'tolerations': 'list[V1Toleration]',
        'updated_dt': 'datetime',
        'workspace_enabled': 'bool'
    }

    attribute_map = {
        'cpu_limit': 'cpu_limit',
        'cpu_type': 'cpu_type',
        'created_dt': 'created_dt',
        'default_hourly_credit': 'default_hourly_credit',
        'deleted_dt': 'deleted_dt',
        'description': 'description',
        'experiment_enabled': 'experiment_enabled',
        'gpu_limit': 'gpu_limit',
        'gpu_type': 'gpu_type',
        'id': 'id',
        'memory_limit': 'memory_limit',
        'name': 'name',
        'node_selector': 'node_selector',
        'pricing_plan_eligible': 'pricing_plan_eligible',
        'priority': 'priority',
        'processor_type': 'processor_type',
        'spot': 'spot',
        'tolerations': 'tolerations',
        'updated_dt': 'updated_dt',
        'workspace_enabled': 'workspace_enabled'
    }

    def __init__(self, cpu_limit=None, cpu_type=None, created_dt=None, default_hourly_credit=None, deleted_dt=None, description=None, experiment_enabled=None, gpu_limit=None, gpu_type=None, id=None, memory_limit=None, name=None, node_selector=None, pricing_plan_eligible=None, priority=None, processor_type=None, spot=None, tolerations=None, updated_dt=None, workspace_enabled=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelResourceSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_limit = None
        self._cpu_type = None
        self._created_dt = None
        self._default_hourly_credit = None
        self._deleted_dt = None
        self._description = None
        self._experiment_enabled = None
        self._gpu_limit = None
        self._gpu_type = None
        self._id = None
        self._memory_limit = None
        self._name = None
        self._node_selector = None
        self._pricing_plan_eligible = None
        self._priority = None
        self._processor_type = None
        self._spot = None
        self._tolerations = None
        self._updated_dt = None
        self._workspace_enabled = None
        self.discriminator = None

        self.cpu_limit = cpu_limit
        if cpu_type is not None:
            self.cpu_type = cpu_type
        self.created_dt = created_dt
        self.default_hourly_credit = default_hourly_credit
        self.deleted_dt = deleted_dt
        self.description = description
        self.experiment_enabled = experiment_enabled
        self.gpu_limit = gpu_limit
        self.gpu_type = gpu_type
        self.id = id
        self.memory_limit = memory_limit
        self.name = name
        if node_selector is not None:
            self.node_selector = node_selector
        self.pricing_plan_eligible = pricing_plan_eligible
        self.priority = priority
        self.processor_type = processor_type
        self.spot = spot
        self.tolerations = tolerations
        self.updated_dt = updated_dt
        self.workspace_enabled = workspace_enabled

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The cpu_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: float
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this ResponseKernelResourceSpec.


        :param cpu_limit: The cpu_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :type cpu_limit: float
        """

        self._cpu_limit = cpu_limit

    @property
    def cpu_type(self):
        """Gets the cpu_type of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The cpu_type of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this ResponseKernelResourceSpec.


        :param cpu_type: The cpu_type of this ResponseKernelResourceSpec.  # noqa: E501
        :type cpu_type: str
        """

        self._cpu_type = cpu_type

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The created_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelResourceSpec.


        :param created_dt: The created_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def default_hourly_credit(self):
        """Gets the default_hourly_credit of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The default_hourly_credit of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._default_hourly_credit

    @default_hourly_credit.setter
    def default_hourly_credit(self, default_hourly_credit):
        """Sets the default_hourly_credit of this ResponseKernelResourceSpec.


        :param default_hourly_credit: The default_hourly_credit of this ResponseKernelResourceSpec.  # noqa: E501
        :type default_hourly_credit: int
        """
        if self.local_vars_configuration.client_side_validation and default_hourly_credit is None:  # noqa: E501
            raise ValueError("Invalid value for `default_hourly_credit`, must not be `None`")  # noqa: E501

        self._default_hourly_credit = default_hourly_credit

    @property
    def deleted_dt(self):
        """Gets the deleted_dt of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The deleted_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_dt

    @deleted_dt.setter
    def deleted_dt(self, deleted_dt):
        """Sets the deleted_dt of this ResponseKernelResourceSpec.


        :param deleted_dt: The deleted_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :type deleted_dt: datetime
        """

        self._deleted_dt = deleted_dt

    @property
    def description(self):
        """Gets the description of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The description of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseKernelResourceSpec.


        :param description: The description of this ResponseKernelResourceSpec.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def experiment_enabled(self):
        """Gets the experiment_enabled of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The experiment_enabled of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._experiment_enabled

    @experiment_enabled.setter
    def experiment_enabled(self, experiment_enabled):
        """Sets the experiment_enabled of this ResponseKernelResourceSpec.


        :param experiment_enabled: The experiment_enabled of this ResponseKernelResourceSpec.  # noqa: E501
        :type experiment_enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and experiment_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `experiment_enabled`, must not be `None`")  # noqa: E501

        self._experiment_enabled = experiment_enabled

    @property
    def gpu_limit(self):
        """Gets the gpu_limit of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The gpu_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._gpu_limit

    @gpu_limit.setter
    def gpu_limit(self, gpu_limit):
        """Sets the gpu_limit of this ResponseKernelResourceSpec.


        :param gpu_limit: The gpu_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :type gpu_limit: int
        """

        self._gpu_limit = gpu_limit

    @property
    def gpu_type(self):
        """Gets the gpu_type of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The gpu_type of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this ResponseKernelResourceSpec.


        :param gpu_type: The gpu_type of this ResponseKernelResourceSpec.  # noqa: E501
        :type gpu_type: str
        """

        self._gpu_type = gpu_type

    @property
    def id(self):
        """Gets the id of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The id of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelResourceSpec.


        :param id: The id of this ResponseKernelResourceSpec.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def memory_limit(self):
        """Gets the memory_limit of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The memory_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this ResponseKernelResourceSpec.


        :param memory_limit: The memory_limit of this ResponseKernelResourceSpec.  # noqa: E501
        :type memory_limit: str
        """

        self._memory_limit = memory_limit

    @property
    def name(self):
        """Gets the name of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The name of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelResourceSpec.


        :param name: The name of this ResponseKernelResourceSpec.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_selector(self):
        """Gets the node_selector of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The node_selector of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: OrmKernelResourceSpecNodeSelector
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this ResponseKernelResourceSpec.


        :param node_selector: The node_selector of this ResponseKernelResourceSpec.  # noqa: E501
        :type node_selector: OrmKernelResourceSpecNodeSelector
        """

        self._node_selector = node_selector

    @property
    def pricing_plan_eligible(self):
        """Gets the pricing_plan_eligible of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The pricing_plan_eligible of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._pricing_plan_eligible

    @pricing_plan_eligible.setter
    def pricing_plan_eligible(self, pricing_plan_eligible):
        """Sets the pricing_plan_eligible of this ResponseKernelResourceSpec.


        :param pricing_plan_eligible: The pricing_plan_eligible of this ResponseKernelResourceSpec.  # noqa: E501
        :type pricing_plan_eligible: bool
        """
        if self.local_vars_configuration.client_side_validation and pricing_plan_eligible is None:  # noqa: E501
            raise ValueError("Invalid value for `pricing_plan_eligible`, must not be `None`")  # noqa: E501

        self._pricing_plan_eligible = pricing_plan_eligible

    @property
    def priority(self):
        """Gets the priority of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The priority of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ResponseKernelResourceSpec.


        :param priority: The priority of this ResponseKernelResourceSpec.  # noqa: E501
        :type priority: int
        """
        if self.local_vars_configuration.client_side_validation and priority is None:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def processor_type(self):
        """Gets the processor_type of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The processor_type of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        """Sets the processor_type of this ResponseKernelResourceSpec.


        :param processor_type: The processor_type of this ResponseKernelResourceSpec.  # noqa: E501
        :type processor_type: str
        """
        if self.local_vars_configuration.client_side_validation and processor_type is None:  # noqa: E501
            raise ValueError("Invalid value for `processor_type`, must not be `None`")  # noqa: E501

        self._processor_type = processor_type

    @property
    def spot(self):
        """Gets the spot of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The spot of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._spot

    @spot.setter
    def spot(self, spot):
        """Sets the spot of this ResponseKernelResourceSpec.


        :param spot: The spot of this ResponseKernelResourceSpec.  # noqa: E501
        :type spot: bool
        """
        if self.local_vars_configuration.client_side_validation and spot is None:  # noqa: E501
            raise ValueError("Invalid value for `spot`, must not be `None`")  # noqa: E501

        self._spot = spot

    @property
    def tolerations(self):
        """Gets the tolerations of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The tolerations of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this ResponseKernelResourceSpec.


        :param tolerations: The tolerations of this ResponseKernelResourceSpec.  # noqa: E501
        :type tolerations: list[V1Toleration]
        """
        if self.local_vars_configuration.client_side_validation and tolerations is None:  # noqa: E501
            raise ValueError("Invalid value for `tolerations`, must not be `None`")  # noqa: E501

        self._tolerations = tolerations

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The updated_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelResourceSpec.


        :param updated_dt: The updated_dt of this ResponseKernelResourceSpec.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def workspace_enabled(self):
        """Gets the workspace_enabled of this ResponseKernelResourceSpec.  # noqa: E501


        :return: The workspace_enabled of this ResponseKernelResourceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._workspace_enabled

    @workspace_enabled.setter
    def workspace_enabled(self, workspace_enabled):
        """Sets the workspace_enabled of this ResponseKernelResourceSpec.


        :param workspace_enabled: The workspace_enabled of this ResponseKernelResourceSpec.  # noqa: E501
        :type workspace_enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and workspace_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `workspace_enabled`, must not be `None`")  # noqa: E501

        self._workspace_enabled = workspace_enabled

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
        if not isinstance(other, ResponseKernelResourceSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelResourceSpec):
            return True

        return self.to_dict() != other.to_dict()
