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


class OrmModelServiceRolloutStepSendNotification(object):
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
        'channel': 'str',
        'fail_action': 'str',
        'target': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'fail_action': 'fail_action',
        'target': 'target'
    }

    def __init__(self, channel=None, fail_action=None, target=None, local_vars_configuration=None):  # noqa: E501
        """OrmModelServiceRolloutStepSendNotification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._channel = None
        self._fail_action = None
        self._target = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        if fail_action is not None:
            self.fail_action = fail_action
        self.target = target

    @property
    def channel(self):
        """Gets the channel of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501


        :return: The channel of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this OrmModelServiceRolloutStepSendNotification.


        :param channel: The channel of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :type channel: str
        """
        allowed_values = ["slack", "email"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and channel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

    @property
    def fail_action(self):
        """Gets the fail_action of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501


        :return: The fail_action of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :rtype: str
        """
        return self._fail_action

    @fail_action.setter
    def fail_action(self, fail_action):
        """Sets the fail_action of this OrmModelServiceRolloutStepSendNotification.


        :param fail_action: The fail_action of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :type fail_action: str
        """
        allowed_values = ["skip", "abort"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fail_action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fail_action` ({0}), must be one of {1}"  # noqa: E501
                .format(fail_action, allowed_values)
            )

        self._fail_action = fail_action

    @property
    def target(self):
        """Gets the target of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501


        :return: The target of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this OrmModelServiceRolloutStepSendNotification.


        :param target: The target of this OrmModelServiceRolloutStepSendNotification.  # noqa: E501
        :type target: str
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, OrmModelServiceRolloutStepSendNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmModelServiceRolloutStepSendNotification):
            return True

        return self.to_dict() != other.to_dict()
