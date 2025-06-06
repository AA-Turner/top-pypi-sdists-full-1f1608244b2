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


class OrmOrganizationKernelCluster(object):
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
        'allowed_node_ids': 'list[int]',
        'allowed_resource_spec_names': 'list[str]',
        'created_dt': 'datetime',
        'edges': 'OrmOrganizationKernelClusterEdges',
        'id': 'int',
        'immutable_slug': 'str',
        'initialized_dt': 'datetime',
        'is_resource_spec_restricted': 'bool',
        'kernel_cluster_id': 'int',
        'organization_id': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'allowed_node_ids': 'allowed_node_ids',
        'allowed_resource_spec_names': 'allowed_resource_spec_names',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'initialized_dt': 'initialized_dt',
        'is_resource_spec_restricted': 'is_resource_spec_restricted',
        'kernel_cluster_id': 'kernel_cluster_id',
        'organization_id': 'organization_id',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, allowed_node_ids=None, allowed_resource_spec_names=None, created_dt=None, edges=None, id=None, immutable_slug=None, initialized_dt=None, is_resource_spec_restricted=None, kernel_cluster_id=None, organization_id=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmOrganizationKernelCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_node_ids = None
        self._allowed_resource_spec_names = None
        self._created_dt = None
        self._edges = None
        self._id = None
        self._immutable_slug = None
        self._initialized_dt = None
        self._is_resource_spec_restricted = None
        self._kernel_cluster_id = None
        self._organization_id = None
        self._updated_dt = None
        self.discriminator = None

        if allowed_node_ids is not None:
            self.allowed_node_ids = allowed_node_ids
        if allowed_resource_spec_names is not None:
            self.allowed_resource_spec_names = allowed_resource_spec_names
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        self.initialized_dt = initialized_dt
        if is_resource_spec_restricted is not None:
            self.is_resource_spec_restricted = is_resource_spec_restricted
        if kernel_cluster_id is not None:
            self.kernel_cluster_id = kernel_cluster_id
        if organization_id is not None:
            self.organization_id = organization_id
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def allowed_node_ids(self):
        """Gets the allowed_node_ids of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The allowed_node_ids of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: list[int]
        """
        return self._allowed_node_ids

    @allowed_node_ids.setter
    def allowed_node_ids(self, allowed_node_ids):
        """Sets the allowed_node_ids of this OrmOrganizationKernelCluster.


        :param allowed_node_ids: The allowed_node_ids of this OrmOrganizationKernelCluster.  # noqa: E501
        :type allowed_node_ids: list[int]
        """

        self._allowed_node_ids = allowed_node_ids

    @property
    def allowed_resource_spec_names(self):
        """Gets the allowed_resource_spec_names of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The allowed_resource_spec_names of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_resource_spec_names

    @allowed_resource_spec_names.setter
    def allowed_resource_spec_names(self, allowed_resource_spec_names):
        """Sets the allowed_resource_spec_names of this OrmOrganizationKernelCluster.


        :param allowed_resource_spec_names: The allowed_resource_spec_names of this OrmOrganizationKernelCluster.  # noqa: E501
        :type allowed_resource_spec_names: list[str]
        """

        self._allowed_resource_spec_names = allowed_resource_spec_names

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The created_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmOrganizationKernelCluster.


        :param created_dt: The created_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The edges of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: OrmOrganizationKernelClusterEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmOrganizationKernelCluster.


        :param edges: The edges of this OrmOrganizationKernelCluster.  # noqa: E501
        :type edges: OrmOrganizationKernelClusterEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The id of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmOrganizationKernelCluster.


        :param id: The id of this OrmOrganizationKernelCluster.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The immutable_slug of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmOrganizationKernelCluster.


        :param immutable_slug: The immutable_slug of this OrmOrganizationKernelCluster.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def initialized_dt(self):
        """Gets the initialized_dt of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The initialized_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._initialized_dt

    @initialized_dt.setter
    def initialized_dt(self, initialized_dt):
        """Sets the initialized_dt of this OrmOrganizationKernelCluster.


        :param initialized_dt: The initialized_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :type initialized_dt: datetime
        """

        self._initialized_dt = initialized_dt

    @property
    def is_resource_spec_restricted(self):
        """Gets the is_resource_spec_restricted of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The is_resource_spec_restricted of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_resource_spec_restricted

    @is_resource_spec_restricted.setter
    def is_resource_spec_restricted(self, is_resource_spec_restricted):
        """Sets the is_resource_spec_restricted of this OrmOrganizationKernelCluster.


        :param is_resource_spec_restricted: The is_resource_spec_restricted of this OrmOrganizationKernelCluster.  # noqa: E501
        :type is_resource_spec_restricted: bool
        """

        self._is_resource_spec_restricted = is_resource_spec_restricted

    @property
    def kernel_cluster_id(self):
        """Gets the kernel_cluster_id of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The kernel_cluster_id of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._kernel_cluster_id

    @kernel_cluster_id.setter
    def kernel_cluster_id(self, kernel_cluster_id):
        """Sets the kernel_cluster_id of this OrmOrganizationKernelCluster.


        :param kernel_cluster_id: The kernel_cluster_id of this OrmOrganizationKernelCluster.  # noqa: E501
        :type kernel_cluster_id: int
        """

        self._kernel_cluster_id = kernel_cluster_id

    @property
    def organization_id(self):
        """Gets the organization_id of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The organization_id of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this OrmOrganizationKernelCluster.


        :param organization_id: The organization_id of this OrmOrganizationKernelCluster.  # noqa: E501
        :type organization_id: int
        """

        self._organization_id = organization_id

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmOrganizationKernelCluster.  # noqa: E501


        :return: The updated_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmOrganizationKernelCluster.


        :param updated_dt: The updated_dt of this OrmOrganizationKernelCluster.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, OrmOrganizationKernelCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmOrganizationKernelCluster):
            return True

        return self.to_dict() != other.to_dict()
