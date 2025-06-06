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


class V1WorkflowRevisionInput(object):
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
        'edges': 'dict[str, list[V1SingleWorkflowEdgeInput]]',
        'end_node_rendering_hints': 'V1RenderingHints',
        'kind': 'str',
        'nodes': 'dict[str, V1WorkflowNodeInput]',
        'start_node_rendering_hints': 'V1RenderingHints',
        'variables': 'dict[str, V1VariableValueInput]'
    }

    attribute_map = {
        'edges': 'edges',
        'end_node_rendering_hints': 'end_node_rendering_hints',
        'kind': 'kind',
        'nodes': 'nodes',
        'start_node_rendering_hints': 'start_node_rendering_hints',
        'variables': 'variables'
    }

    def __init__(self, edges=None, end_node_rendering_hints=None, kind=None, nodes=None, start_node_rendering_hints=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """V1WorkflowRevisionInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._edges = None
        self._end_node_rendering_hints = None
        self._kind = None
        self._nodes = None
        self._start_node_rendering_hints = None
        self._variables = None
        self.discriminator = None

        if edges is not None:
            self.edges = edges
        if end_node_rendering_hints is not None:
            self.end_node_rendering_hints = end_node_rendering_hints
        if kind is not None:
            self.kind = kind
        if nodes is not None:
            self.nodes = nodes
        if start_node_rendering_hints is not None:
            self.start_node_rendering_hints = start_node_rendering_hints
        if variables is not None:
            self.variables = variables

    @property
    def edges(self):
        """Gets the edges of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The edges of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: dict[str, list[V1SingleWorkflowEdgeInput]]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this V1WorkflowRevisionInput.


        :param edges: The edges of this V1WorkflowRevisionInput.  # noqa: E501
        :type edges: dict[str, list[V1SingleWorkflowEdgeInput]]
        """

        self._edges = edges

    @property
    def end_node_rendering_hints(self):
        """Gets the end_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The end_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: V1RenderingHints
        """
        return self._end_node_rendering_hints

    @end_node_rendering_hints.setter
    def end_node_rendering_hints(self, end_node_rendering_hints):
        """Sets the end_node_rendering_hints of this V1WorkflowRevisionInput.


        :param end_node_rendering_hints: The end_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501
        :type end_node_rendering_hints: V1RenderingHints
        """

        self._end_node_rendering_hints = end_node_rendering_hints

    @property
    def kind(self):
        """Gets the kind of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The kind of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1WorkflowRevisionInput.


        :param kind: The kind of this V1WorkflowRevisionInput.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def nodes(self):
        """Gets the nodes of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The nodes of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: dict[str, V1WorkflowNodeInput]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this V1WorkflowRevisionInput.


        :param nodes: The nodes of this V1WorkflowRevisionInput.  # noqa: E501
        :type nodes: dict[str, V1WorkflowNodeInput]
        """

        self._nodes = nodes

    @property
    def start_node_rendering_hints(self):
        """Gets the start_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The start_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: V1RenderingHints
        """
        return self._start_node_rendering_hints

    @start_node_rendering_hints.setter
    def start_node_rendering_hints(self, start_node_rendering_hints):
        """Sets the start_node_rendering_hints of this V1WorkflowRevisionInput.


        :param start_node_rendering_hints: The start_node_rendering_hints of this V1WorkflowRevisionInput.  # noqa: E501
        :type start_node_rendering_hints: V1RenderingHints
        """

        self._start_node_rendering_hints = start_node_rendering_hints

    @property
    def variables(self):
        """Gets the variables of this V1WorkflowRevisionInput.  # noqa: E501


        :return: The variables of this V1WorkflowRevisionInput.  # noqa: E501
        :rtype: dict[str, V1VariableValueInput]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this V1WorkflowRevisionInput.


        :param variables: The variables of this V1WorkflowRevisionInput.  # noqa: E501
        :type variables: dict[str, V1VariableValueInput]
        """

        self._variables = variables

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
        if not isinstance(other, V1WorkflowRevisionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1WorkflowRevisionInput):
            return True

        return self.to_dict() != other.to_dict()
