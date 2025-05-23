# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterFinalizingProgress(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'finalizing_stage': 'FinalizingStage'
    }

    attribute_map = {
        'finalizing_stage': 'finalizing_stage'
    }

    def __init__(self, finalizing_stage=None):  # noqa: E501
        """ClusterFinalizingProgress - a model defined in Swagger"""  # noqa: E501

        self._finalizing_stage = None
        self.discriminator = None

        if finalizing_stage is not None:
            self.finalizing_stage = finalizing_stage

    @property
    def finalizing_stage(self):
        """Gets the finalizing_stage of this ClusterFinalizingProgress.  # noqa: E501


        :return: The finalizing_stage of this ClusterFinalizingProgress.  # noqa: E501
        :rtype: FinalizingStage
        """
        return self._finalizing_stage

    @finalizing_stage.setter
    def finalizing_stage(self, finalizing_stage):
        """Sets the finalizing_stage of this ClusterFinalizingProgress.


        :param finalizing_stage: The finalizing_stage of this ClusterFinalizingProgress.  # noqa: E501
        :type: FinalizingStage
        """

        self._finalizing_stage = finalizing_stage

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ClusterFinalizingProgress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterFinalizingProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
