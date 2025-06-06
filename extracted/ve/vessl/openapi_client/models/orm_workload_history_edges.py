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


class OrmWorkloadHistoryEdges(object):
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
        'resource_spec': 'OrmKernelResourceSpec',
        'workload': 'OrmWorkload'
    }

    attribute_map = {
        'resource_spec': 'resource_spec',
        'workload': 'workload'
    }

    def __init__(self, resource_spec=None, workload=None, local_vars_configuration=None):  # noqa: E501
        """OrmWorkloadHistoryEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resource_spec = None
        self._workload = None
        self.discriminator = None

        if resource_spec is not None:
            self.resource_spec = resource_spec
        if workload is not None:
            self.workload = workload

    @property
    def resource_spec(self):
        """Gets the resource_spec of this OrmWorkloadHistoryEdges.  # noqa: E501


        :return: The resource_spec of this OrmWorkloadHistoryEdges.  # noqa: E501
        :rtype: OrmKernelResourceSpec
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        """Sets the resource_spec of this OrmWorkloadHistoryEdges.


        :param resource_spec: The resource_spec of this OrmWorkloadHistoryEdges.  # noqa: E501
        :type resource_spec: OrmKernelResourceSpec
        """

        self._resource_spec = resource_spec

    @property
    def workload(self):
        """Gets the workload of this OrmWorkloadHistoryEdges.  # noqa: E501


        :return: The workload of this OrmWorkloadHistoryEdges.  # noqa: E501
        :rtype: OrmWorkload
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        """Sets the workload of this OrmWorkloadHistoryEdges.


        :param workload: The workload of this OrmWorkloadHistoryEdges.  # noqa: E501
        :type workload: OrmWorkload
        """

        self._workload = workload

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
        if not isinstance(other, OrmWorkloadHistoryEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmWorkloadHistoryEdges):
            return True

        return self.to_dict() != other.to_dict()
