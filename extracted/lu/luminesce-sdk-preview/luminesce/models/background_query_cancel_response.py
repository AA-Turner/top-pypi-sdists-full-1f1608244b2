# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from luminesce.configuration import Configuration


class BackgroundQueryCancelResponse(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'had_data': 'bool',
        'previous_status': 'TaskStatus',
        'previous_state': 'BackgroundQueryState',
        'progress': 'str'
    }

    attribute_map = {
        'had_data': 'hadData',
        'previous_status': 'previousStatus',
        'previous_state': 'previousState',
        'progress': 'progress'
    }

    required_map = {
        'had_data': 'optional',
        'previous_status': 'optional',
        'previous_state': 'optional',
        'progress': 'optional'
    }

    def __init__(self, had_data=None, previous_status=None, previous_state=None, progress=None, local_vars_configuration=None):  # noqa: E501
        """BackgroundQueryCancelResponse - a model defined in OpenAPI"
        
        :param had_data: 
        :type had_data: bool
        :param previous_status: 
        :type previous_status: luminesce.TaskStatus
        :param previous_state: 
        :type previous_state: luminesce.BackgroundQueryState
        :param progress: 
        :type progress: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._had_data = None
        self._previous_status = None
        self._previous_state = None
        self._progress = None
        self.discriminator = None

        if had_data is not None:
            self.had_data = had_data
        if previous_status is not None:
            self.previous_status = previous_status
        if previous_state is not None:
            self.previous_state = previous_state
        self.progress = progress

    @property
    def had_data(self):
        """Gets the had_data of this BackgroundQueryCancelResponse.  # noqa: E501


        :return: The had_data of this BackgroundQueryCancelResponse.  # noqa: E501
        :rtype: bool
        """
        return self._had_data

    @had_data.setter
    def had_data(self, had_data):
        """Sets the had_data of this BackgroundQueryCancelResponse.


        :param had_data: The had_data of this BackgroundQueryCancelResponse.  # noqa: E501
        :type had_data: bool
        """

        self._had_data = had_data

    @property
    def previous_status(self):
        """Gets the previous_status of this BackgroundQueryCancelResponse.  # noqa: E501


        :return: The previous_status of this BackgroundQueryCancelResponse.  # noqa: E501
        :rtype: luminesce.TaskStatus
        """
        return self._previous_status

    @previous_status.setter
    def previous_status(self, previous_status):
        """Sets the previous_status of this BackgroundQueryCancelResponse.


        :param previous_status: The previous_status of this BackgroundQueryCancelResponse.  # noqa: E501
        :type previous_status: luminesce.TaskStatus
        """

        self._previous_status = previous_status

    @property
    def previous_state(self):
        """Gets the previous_state of this BackgroundQueryCancelResponse.  # noqa: E501


        :return: The previous_state of this BackgroundQueryCancelResponse.  # noqa: E501
        :rtype: luminesce.BackgroundQueryState
        """
        return self._previous_state

    @previous_state.setter
    def previous_state(self, previous_state):
        """Sets the previous_state of this BackgroundQueryCancelResponse.


        :param previous_state: The previous_state of this BackgroundQueryCancelResponse.  # noqa: E501
        :type previous_state: luminesce.BackgroundQueryState
        """

        self._previous_state = previous_state

    @property
    def progress(self):
        """Gets the progress of this BackgroundQueryCancelResponse.  # noqa: E501


        :return: The progress of this BackgroundQueryCancelResponse.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BackgroundQueryCancelResponse.


        :param progress: The progress of this BackgroundQueryCancelResponse.  # noqa: E501
        :type progress: str
        """

        self._progress = progress

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
        if not isinstance(other, BackgroundQueryCancelResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackgroundQueryCancelResponse):
            return True

        return self.to_dict() != other.to_dict()
