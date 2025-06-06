# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.32.3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1NetworkPolicyIngressRule(object):
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
        '_from': 'list[V1NetworkPolicyPeer]',
        'ports': 'list[V1NetworkPolicyPort]'
    }

    attribute_map = {
        '_from': 'from',
        'ports': 'ports'
    }

    def __init__(self, _from=None, ports=None, local_vars_configuration=None):  # noqa: E501
        """V1NetworkPolicyIngressRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._ports = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if ports is not None:
            self.ports = ports

    @property
    def _from(self):
        """Gets the _from of this V1NetworkPolicyIngressRule.  # noqa: E501

        from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.  # noqa: E501

        :return: The _from of this V1NetworkPolicyIngressRule.  # noqa: E501
        :rtype: list[V1NetworkPolicyPeer]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this V1NetworkPolicyIngressRule.

        from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.  # noqa: E501

        :param _from: The _from of this V1NetworkPolicyIngressRule.  # noqa: E501
        :type _from: list[V1NetworkPolicyPeer]
        """

        self.__from = _from

    @property
    def ports(self):
        """Gets the ports of this V1NetworkPolicyIngressRule.  # noqa: E501

        ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.  # noqa: E501

        :return: The ports of this V1NetworkPolicyIngressRule.  # noqa: E501
        :rtype: list[V1NetworkPolicyPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1NetworkPolicyIngressRule.

        ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.  # noqa: E501

        :param ports: The ports of this V1NetworkPolicyIngressRule.  # noqa: E501
        :type ports: list[V1NetworkPolicyPort]
        """

        self._ports = ports

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
        if not isinstance(other, V1NetworkPolicyIngressRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1NetworkPolicyIngressRule):
            return True

        return self.to_dict() != other.to_dict()
