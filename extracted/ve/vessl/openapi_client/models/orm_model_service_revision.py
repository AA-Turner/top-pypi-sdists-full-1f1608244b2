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


class OrmModelServiceRevision(object):
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
        'arguments': 'dict[str, object]',
        'autoscaler_config': 'dict[str, object]',
        'available_replicas': 'int',
        'created_by_id': 'int',
        'created_dt': 'datetime',
        'edges': 'OrmModelServiceRevisionEdges',
        'id': 'int',
        'immutable_slug': 'str',
        'kernel_image_id': 'int',
        'llm_workflow_revision_id': 'int',
        'message': 'str',
        'model_service_id': 'int',
        'number': 'int',
        'ports': 'dict[str, object]',
        'revision_yaml': 'str',
        'spec': 'dict[str, object]',
        'total_replicas': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'arguments': 'arguments',
        'autoscaler_config': 'autoscaler_config',
        'available_replicas': 'available_replicas',
        'created_by_id': 'created_by_id',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'kernel_image_id': 'kernel_image_id',
        'llm_workflow_revision_id': 'llm_workflow_revision_id',
        'message': 'message',
        'model_service_id': 'model_service_id',
        'number': 'number',
        'ports': 'ports',
        'revision_yaml': 'revision_yaml',
        'spec': 'spec',
        'total_replicas': 'total_replicas',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, arguments=None, autoscaler_config=None, available_replicas=None, created_by_id=None, created_dt=None, edges=None, id=None, immutable_slug=None, kernel_image_id=None, llm_workflow_revision_id=None, message=None, model_service_id=None, number=None, ports=None, revision_yaml=None, spec=None, total_replicas=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmModelServiceRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._arguments = None
        self._autoscaler_config = None
        self._available_replicas = None
        self._created_by_id = None
        self._created_dt = None
        self._edges = None
        self._id = None
        self._immutable_slug = None
        self._kernel_image_id = None
        self._llm_workflow_revision_id = None
        self._message = None
        self._model_service_id = None
        self._number = None
        self._ports = None
        self._revision_yaml = None
        self._spec = None
        self._total_replicas = None
        self._updated_dt = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if autoscaler_config is not None:
            self.autoscaler_config = autoscaler_config
        if available_replicas is not None:
            self.available_replicas = available_replicas
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if kernel_image_id is not None:
            self.kernel_image_id = kernel_image_id
        self.llm_workflow_revision_id = llm_workflow_revision_id
        if message is not None:
            self.message = message
        if model_service_id is not None:
            self.model_service_id = model_service_id
        if number is not None:
            self.number = number
        if ports is not None:
            self.ports = ports
        self.revision_yaml = revision_yaml
        if spec is not None:
            self.spec = spec
        if total_replicas is not None:
            self.total_replicas = total_replicas
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def arguments(self):
        """Gets the arguments of this OrmModelServiceRevision.  # noqa: E501


        :return: The arguments of this OrmModelServiceRevision.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this OrmModelServiceRevision.


        :param arguments: The arguments of this OrmModelServiceRevision.  # noqa: E501
        :type arguments: dict[str, object]
        """

        self._arguments = arguments

    @property
    def autoscaler_config(self):
        """Gets the autoscaler_config of this OrmModelServiceRevision.  # noqa: E501


        :return: The autoscaler_config of this OrmModelServiceRevision.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._autoscaler_config

    @autoscaler_config.setter
    def autoscaler_config(self, autoscaler_config):
        """Sets the autoscaler_config of this OrmModelServiceRevision.


        :param autoscaler_config: The autoscaler_config of this OrmModelServiceRevision.  # noqa: E501
        :type autoscaler_config: dict[str, object]
        """

        self._autoscaler_config = autoscaler_config

    @property
    def available_replicas(self):
        """Gets the available_replicas of this OrmModelServiceRevision.  # noqa: E501


        :return: The available_replicas of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this OrmModelServiceRevision.


        :param available_replicas: The available_replicas of this OrmModelServiceRevision.  # noqa: E501
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def created_by_id(self):
        """Gets the created_by_id of this OrmModelServiceRevision.  # noqa: E501


        :return: The created_by_id of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this OrmModelServiceRevision.


        :param created_by_id: The created_by_id of this OrmModelServiceRevision.  # noqa: E501
        :type created_by_id: int
        """

        self._created_by_id = created_by_id

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmModelServiceRevision.  # noqa: E501


        :return: The created_dt of this OrmModelServiceRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmModelServiceRevision.


        :param created_dt: The created_dt of this OrmModelServiceRevision.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmModelServiceRevision.  # noqa: E501


        :return: The edges of this OrmModelServiceRevision.  # noqa: E501
        :rtype: OrmModelServiceRevisionEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmModelServiceRevision.


        :param edges: The edges of this OrmModelServiceRevision.  # noqa: E501
        :type edges: OrmModelServiceRevisionEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmModelServiceRevision.  # noqa: E501


        :return: The id of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmModelServiceRevision.


        :param id: The id of this OrmModelServiceRevision.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmModelServiceRevision.  # noqa: E501


        :return: The immutable_slug of this OrmModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmModelServiceRevision.


        :param immutable_slug: The immutable_slug of this OrmModelServiceRevision.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def kernel_image_id(self):
        """Gets the kernel_image_id of this OrmModelServiceRevision.  # noqa: E501


        :return: The kernel_image_id of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._kernel_image_id

    @kernel_image_id.setter
    def kernel_image_id(self, kernel_image_id):
        """Sets the kernel_image_id of this OrmModelServiceRevision.


        :param kernel_image_id: The kernel_image_id of this OrmModelServiceRevision.  # noqa: E501
        :type kernel_image_id: int
        """

        self._kernel_image_id = kernel_image_id

    @property
    def llm_workflow_revision_id(self):
        """Gets the llm_workflow_revision_id of this OrmModelServiceRevision.  # noqa: E501


        :return: The llm_workflow_revision_id of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._llm_workflow_revision_id

    @llm_workflow_revision_id.setter
    def llm_workflow_revision_id(self, llm_workflow_revision_id):
        """Sets the llm_workflow_revision_id of this OrmModelServiceRevision.


        :param llm_workflow_revision_id: The llm_workflow_revision_id of this OrmModelServiceRevision.  # noqa: E501
        :type llm_workflow_revision_id: int
        """

        self._llm_workflow_revision_id = llm_workflow_revision_id

    @property
    def message(self):
        """Gets the message of this OrmModelServiceRevision.  # noqa: E501


        :return: The message of this OrmModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OrmModelServiceRevision.


        :param message: The message of this OrmModelServiceRevision.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def model_service_id(self):
        """Gets the model_service_id of this OrmModelServiceRevision.  # noqa: E501


        :return: The model_service_id of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._model_service_id

    @model_service_id.setter
    def model_service_id(self, model_service_id):
        """Sets the model_service_id of this OrmModelServiceRevision.


        :param model_service_id: The model_service_id of this OrmModelServiceRevision.  # noqa: E501
        :type model_service_id: int
        """

        self._model_service_id = model_service_id

    @property
    def number(self):
        """Gets the number of this OrmModelServiceRevision.  # noqa: E501


        :return: The number of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this OrmModelServiceRevision.


        :param number: The number of this OrmModelServiceRevision.  # noqa: E501
        :type number: int
        """

        self._number = number

    @property
    def ports(self):
        """Gets the ports of this OrmModelServiceRevision.  # noqa: E501


        :return: The ports of this OrmModelServiceRevision.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this OrmModelServiceRevision.


        :param ports: The ports of this OrmModelServiceRevision.  # noqa: E501
        :type ports: dict[str, object]
        """

        self._ports = ports

    @property
    def revision_yaml(self):
        """Gets the revision_yaml of this OrmModelServiceRevision.  # noqa: E501


        :return: The revision_yaml of this OrmModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._revision_yaml

    @revision_yaml.setter
    def revision_yaml(self, revision_yaml):
        """Sets the revision_yaml of this OrmModelServiceRevision.


        :param revision_yaml: The revision_yaml of this OrmModelServiceRevision.  # noqa: E501
        :type revision_yaml: str
        """

        self._revision_yaml = revision_yaml

    @property
    def spec(self):
        """Gets the spec of this OrmModelServiceRevision.  # noqa: E501


        :return: The spec of this OrmModelServiceRevision.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this OrmModelServiceRevision.


        :param spec: The spec of this OrmModelServiceRevision.  # noqa: E501
        :type spec: dict[str, object]
        """

        self._spec = spec

    @property
    def total_replicas(self):
        """Gets the total_replicas of this OrmModelServiceRevision.  # noqa: E501


        :return: The total_replicas of this OrmModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._total_replicas

    @total_replicas.setter
    def total_replicas(self, total_replicas):
        """Sets the total_replicas of this OrmModelServiceRevision.


        :param total_replicas: The total_replicas of this OrmModelServiceRevision.  # noqa: E501
        :type total_replicas: int
        """

        self._total_replicas = total_replicas

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmModelServiceRevision.  # noqa: E501


        :return: The updated_dt of this OrmModelServiceRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmModelServiceRevision.


        :param updated_dt: The updated_dt of this OrmModelServiceRevision.  # noqa: E501
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
        if not isinstance(other, OrmModelServiceRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmModelServiceRevision):
            return True

        return self.to_dict() != other.to_dict()
