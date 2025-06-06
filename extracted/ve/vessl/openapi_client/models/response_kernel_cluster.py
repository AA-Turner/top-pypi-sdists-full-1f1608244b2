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


class ResponseKernelCluster(object):
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
        'created_dt': 'datetime',
        'id': 'int',
        'is_custom_resource_spec_allowed': 'bool',
        'is_savvihub_managed': 'bool',
        'is_vessl_managed': 'bool',
        'kubernetes_service_type': 'str',
        'metric_source': 'str',
        'name': 'str',
        'provider': 'str',
        'region': 'str',
        'updated_dt': 'datetime',
        'workload_service_type': 'str'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'id': 'id',
        'is_custom_resource_spec_allowed': 'is_custom_resource_spec_allowed',
        'is_savvihub_managed': 'is_savvihub_managed',
        'is_vessl_managed': 'is_vessl_managed',
        'kubernetes_service_type': 'kubernetes_service_type',
        'metric_source': 'metric_source',
        'name': 'name',
        'provider': 'provider',
        'region': 'region',
        'updated_dt': 'updated_dt',
        'workload_service_type': 'workload_service_type'
    }

    def __init__(self, created_dt=None, id=None, is_custom_resource_spec_allowed=None, is_savvihub_managed=None, is_vessl_managed=None, kubernetes_service_type=None, metric_source=None, name=None, provider=None, region=None, updated_dt=None, workload_service_type=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._id = None
        self._is_custom_resource_spec_allowed = None
        self._is_savvihub_managed = None
        self._is_vessl_managed = None
        self._kubernetes_service_type = None
        self._metric_source = None
        self._name = None
        self._provider = None
        self._region = None
        self._updated_dt = None
        self._workload_service_type = None
        self.discriminator = None

        self.created_dt = created_dt
        self.id = id
        self.is_custom_resource_spec_allowed = is_custom_resource_spec_allowed
        self.is_savvihub_managed = is_savvihub_managed
        self.is_vessl_managed = is_vessl_managed
        self.kubernetes_service_type = kubernetes_service_type
        self.metric_source = metric_source
        self.name = name
        self.provider = provider
        self.region = region
        self.updated_dt = updated_dt
        self.workload_service_type = workload_service_type

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelCluster.  # noqa: E501


        :return: The created_dt of this ResponseKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelCluster.


        :param created_dt: The created_dt of this ResponseKernelCluster.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def id(self):
        """Gets the id of this ResponseKernelCluster.  # noqa: E501


        :return: The id of this ResponseKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelCluster.


        :param id: The id of this ResponseKernelCluster.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_custom_resource_spec_allowed(self):
        """Gets the is_custom_resource_spec_allowed of this ResponseKernelCluster.  # noqa: E501


        :return: The is_custom_resource_spec_allowed of this ResponseKernelCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom_resource_spec_allowed

    @is_custom_resource_spec_allowed.setter
    def is_custom_resource_spec_allowed(self, is_custom_resource_spec_allowed):
        """Sets the is_custom_resource_spec_allowed of this ResponseKernelCluster.


        :param is_custom_resource_spec_allowed: The is_custom_resource_spec_allowed of this ResponseKernelCluster.  # noqa: E501
        :type is_custom_resource_spec_allowed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_custom_resource_spec_allowed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_custom_resource_spec_allowed`, must not be `None`")  # noqa: E501

        self._is_custom_resource_spec_allowed = is_custom_resource_spec_allowed

    @property
    def is_savvihub_managed(self):
        """Gets the is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501


        :return: The is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_savvihub_managed

    @is_savvihub_managed.setter
    def is_savvihub_managed(self, is_savvihub_managed):
        """Sets the is_savvihub_managed of this ResponseKernelCluster.


        :param is_savvihub_managed: The is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501
        :type is_savvihub_managed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_savvihub_managed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_savvihub_managed`, must not be `None`")  # noqa: E501

        self._is_savvihub_managed = is_savvihub_managed

    @property
    def is_vessl_managed(self):
        """Gets the is_vessl_managed of this ResponseKernelCluster.  # noqa: E501


        :return: The is_vessl_managed of this ResponseKernelCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_vessl_managed

    @is_vessl_managed.setter
    def is_vessl_managed(self, is_vessl_managed):
        """Sets the is_vessl_managed of this ResponseKernelCluster.


        :param is_vessl_managed: The is_vessl_managed of this ResponseKernelCluster.  # noqa: E501
        :type is_vessl_managed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_vessl_managed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_vessl_managed`, must not be `None`")  # noqa: E501

        self._is_vessl_managed = is_vessl_managed

    @property
    def kubernetes_service_type(self):
        """Gets the kubernetes_service_type of this ResponseKernelCluster.  # noqa: E501


        :return: The kubernetes_service_type of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_service_type

    @kubernetes_service_type.setter
    def kubernetes_service_type(self, kubernetes_service_type):
        """Sets the kubernetes_service_type of this ResponseKernelCluster.


        :param kubernetes_service_type: The kubernetes_service_type of this ResponseKernelCluster.  # noqa: E501
        :type kubernetes_service_type: str
        """
        if self.local_vars_configuration.client_side_validation and kubernetes_service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `kubernetes_service_type`, must not be `None`")  # noqa: E501

        self._kubernetes_service_type = kubernetes_service_type

    @property
    def metric_source(self):
        """Gets the metric_source of this ResponseKernelCluster.  # noqa: E501


        :return: The metric_source of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._metric_source

    @metric_source.setter
    def metric_source(self, metric_source):
        """Sets the metric_source of this ResponseKernelCluster.


        :param metric_source: The metric_source of this ResponseKernelCluster.  # noqa: E501
        :type metric_source: str
        """
        if self.local_vars_configuration.client_side_validation and metric_source is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_source`, must not be `None`")  # noqa: E501

        self._metric_source = metric_source

    @property
    def name(self):
        """Gets the name of this ResponseKernelCluster.  # noqa: E501


        :return: The name of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelCluster.


        :param name: The name of this ResponseKernelCluster.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this ResponseKernelCluster.  # noqa: E501


        :return: The provider of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResponseKernelCluster.


        :param provider: The provider of this ResponseKernelCluster.  # noqa: E501
        :type provider: str
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["vessl", "aws", "gcp", "azure", "oci", "on-premise"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and provider not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this ResponseKernelCluster.  # noqa: E501


        :return: The region of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ResponseKernelCluster.


        :param region: The region of this ResponseKernelCluster.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelCluster.  # noqa: E501


        :return: The updated_dt of this ResponseKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelCluster.


        :param updated_dt: The updated_dt of this ResponseKernelCluster.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def workload_service_type(self):
        """Gets the workload_service_type of this ResponseKernelCluster.  # noqa: E501


        :return: The workload_service_type of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._workload_service_type

    @workload_service_type.setter
    def workload_service_type(self, workload_service_type):
        """Sets the workload_service_type of this ResponseKernelCluster.


        :param workload_service_type: The workload_service_type of this ResponseKernelCluster.  # noqa: E501
        :type workload_service_type: str
        """
        if self.local_vars_configuration.client_side_validation and workload_service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `workload_service_type`, must not be `None`")  # noqa: E501

        self._workload_service_type = workload_service_type

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
        if not isinstance(other, ResponseKernelCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelCluster):
            return True

        return self.to_dict() != other.to_dict()
