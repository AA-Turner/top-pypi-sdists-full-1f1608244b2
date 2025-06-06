# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.257
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

from lusid.configuration import Configuration


class UpdateCutLabelDefinitionRequest(object):
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
        'display_name': 'str',
        'description': 'str',
        'cut_local_time': 'CutLocalTime',
        'time_zone': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'cut_local_time': 'cutLocalTime',
        'time_zone': 'timeZone'
    }

    required_map = {
        'display_name': 'required',
        'description': 'optional',
        'cut_local_time': 'required',
        'time_zone': 'required'
    }

    def __init__(self, display_name=None, description=None, cut_local_time=None, time_zone=None, local_vars_configuration=None):  # noqa: E501
        """UpdateCutLabelDefinitionRequest - a model defined in OpenAPI"
        
        :param display_name:  (required)
        :type display_name: str
        :param description: 
        :type description: str
        :param cut_local_time:  (required)
        :type cut_local_time: lusid.CutLocalTime
        :param time_zone:  (required)
        :type time_zone: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._description = None
        self._cut_local_time = None
        self._time_zone = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.cut_local_time = cut_local_time
        self.time_zone = time_zone

    @property
    def display_name(self):
        """Gets the display_name of this UpdateCutLabelDefinitionRequest.  # noqa: E501


        :return: The display_name of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateCutLabelDefinitionRequest.


        :param display_name: The display_name of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this UpdateCutLabelDefinitionRequest.  # noqa: E501


        :return: The description of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCutLabelDefinitionRequest.


        :param description: The description of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def cut_local_time(self):
        """Gets the cut_local_time of this UpdateCutLabelDefinitionRequest.  # noqa: E501


        :return: The cut_local_time of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :rtype: lusid.CutLocalTime
        """
        return self._cut_local_time

    @cut_local_time.setter
    def cut_local_time(self, cut_local_time):
        """Sets the cut_local_time of this UpdateCutLabelDefinitionRequest.


        :param cut_local_time: The cut_local_time of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :type cut_local_time: lusid.CutLocalTime
        """
        if self.local_vars_configuration.client_side_validation and cut_local_time is None:  # noqa: E501
            raise ValueError("Invalid value for `cut_local_time`, must not be `None`")  # noqa: E501

        self._cut_local_time = cut_local_time

    @property
    def time_zone(self):
        """Gets the time_zone of this UpdateCutLabelDefinitionRequest.  # noqa: E501


        :return: The time_zone of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UpdateCutLabelDefinitionRequest.


        :param time_zone: The time_zone of this UpdateCutLabelDefinitionRequest.  # noqa: E501
        :type time_zone: str
        """
        if self.local_vars_configuration.client_side_validation and time_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_zone is not None and len(time_zone) < 1):
            raise ValueError("Invalid value for `time_zone`, length must be greater than or equal to `1`")  # noqa: E501

        self._time_zone = time_zone

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
        if not isinstance(other, UpdateCutLabelDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCutLabelDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
