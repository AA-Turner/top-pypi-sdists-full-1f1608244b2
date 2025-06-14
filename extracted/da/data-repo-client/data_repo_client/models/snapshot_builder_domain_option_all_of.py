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


class SnapshotBuilderDomainOptionAllOf(object):
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
        'root': 'SnapshotBuilderConcept',
        'concept_count': 'int',
        'participant_count': 'int'
    }

    attribute_map = {
        'root': 'root',
        'concept_count': 'conceptCount',
        'participant_count': 'participantCount'
    }

    def __init__(self, root=None, concept_count=None, participant_count=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotBuilderDomainOptionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._root = None
        self._concept_count = None
        self._participant_count = None
        self.discriminator = None

        self.root = root
        self.concept_count = concept_count
        self.participant_count = participant_count

    @property
    def root(self):
        """Gets the root of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501


        :return: The root of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :rtype: SnapshotBuilderConcept
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this SnapshotBuilderDomainOptionAllOf.


        :param root: The root of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :type: SnapshotBuilderConcept
        """
        if self.local_vars_configuration.client_side_validation and root is None:  # noqa: E501
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def concept_count(self):
        """Gets the concept_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501


        :return: The concept_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :rtype: int
        """
        return self._concept_count

    @concept_count.setter
    def concept_count(self, concept_count):
        """Sets the concept_count of this SnapshotBuilderDomainOptionAllOf.


        :param concept_count: The concept_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and concept_count is None:  # noqa: E501
            raise ValueError("Invalid value for `concept_count`, must not be `None`")  # noqa: E501

        self._concept_count = concept_count

    @property
    def participant_count(self):
        """Gets the participant_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501


        :return: The participant_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :rtype: int
        """
        return self._participant_count

    @participant_count.setter
    def participant_count(self, participant_count):
        """Sets the participant_count of this SnapshotBuilderDomainOptionAllOf.


        :param participant_count: The participant_count of this SnapshotBuilderDomainOptionAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and participant_count is None:  # noqa: E501
            raise ValueError("Invalid value for `participant_count`, must not be `None`")  # noqa: E501

        self._participant_count = participant_count

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
        if not isinstance(other, SnapshotBuilderDomainOptionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotBuilderDomainOptionAllOf):
            return True

        return self.to_dict() != other.to_dict()
