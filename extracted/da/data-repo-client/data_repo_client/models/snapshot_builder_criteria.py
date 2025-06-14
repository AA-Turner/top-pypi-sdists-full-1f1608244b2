# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class SnapshotBuilderCriteria(object):
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
        'kind': 'str',
        'id': 'int'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id'
    }

    discriminator_value_class_map = {
        'SnapshotBuilderDomainCriteria': 'SnapshotBuilderDomainCriteria',
        'SnapshotBuilderProgramDataListCriteria': 'SnapshotBuilderProgramDataListCriteria',
        'SnapshotBuilderProgramDataRangeCriteria': 'SnapshotBuilderProgramDataRangeCriteria'
    }

    def __init__(self, kind=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotBuilderCriteria - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self.discriminator = 'kind'

        self.kind = kind
        self.id = id

    @property
    def kind(self):
        """Gets the kind of this SnapshotBuilderCriteria.  # noqa: E501


        :return: The kind of this SnapshotBuilderCriteria.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this SnapshotBuilderCriteria.


        :param kind: The kind of this SnapshotBuilderCriteria.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["list", "range", "domain"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kind not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this SnapshotBuilderCriteria.  # noqa: E501

        the ID of either the domain or program data entry  # noqa: E501

        :return: The id of this SnapshotBuilderCriteria.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotBuilderCriteria.

        the ID of either the domain or program data entry  # noqa: E501

        :param id: The id of this SnapshotBuilderCriteria.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnapshotBuilderCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotBuilderCriteria):
            return True

        return self.to_dict() != other.to_dict()
