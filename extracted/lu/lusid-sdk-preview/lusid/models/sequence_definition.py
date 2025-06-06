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


class SequenceDefinition(object):
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
        'id': 'ResourceId',
        'increment': 'int',
        'min_value': 'int',
        'max_value': 'int',
        'start': 'int',
        'value': 'int',
        'cycle': 'bool',
        'pattern': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'increment': 'increment',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'start': 'start',
        'value': 'value',
        'cycle': 'cycle',
        'pattern': 'pattern',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'increment': 'required',
        'min_value': 'required',
        'max_value': 'required',
        'start': 'required',
        'value': 'optional',
        'cycle': 'required',
        'pattern': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, increment=None, min_value=None, max_value=None, start=None, value=None, cycle=None, pattern=None, links=None, local_vars_configuration=None):  # noqa: E501
        """SequenceDefinition - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param increment:  The Resource Id of the sequence definition (required)
        :type increment: int
        :param min_value:  The minimum value of the sequence (required)
        :type min_value: int
        :param max_value:  The maximum value of the sequence (required)
        :type max_value: int
        :param start:  The start value of the sequence (required)
        :type start: int
        :param value:  The last used value of the sequence
        :type value: int
        :param cycle:  Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. (required)
        :type cycle: bool
        :param pattern:  The pattern to be used to generate next values in the sequence.
        :type pattern: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._increment = None
        self._min_value = None
        self._max_value = None
        self._start = None
        self._value = None
        self._cycle = None
        self._pattern = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.increment = increment
        self.min_value = min_value
        self.max_value = max_value
        self.start = start
        self.value = value
        self.cycle = cycle
        self.pattern = pattern
        self.links = links

    @property
    def id(self):
        """Gets the id of this SequenceDefinition.  # noqa: E501


        :return: The id of this SequenceDefinition.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SequenceDefinition.


        :param id: The id of this SequenceDefinition.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def increment(self):
        """Gets the increment of this SequenceDefinition.  # noqa: E501

        The Resource Id of the sequence definition  # noqa: E501

        :return: The increment of this SequenceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._increment

    @increment.setter
    def increment(self, increment):
        """Sets the increment of this SequenceDefinition.

        The Resource Id of the sequence definition  # noqa: E501

        :param increment: The increment of this SequenceDefinition.  # noqa: E501
        :type increment: int
        """
        if self.local_vars_configuration.client_side_validation and increment is None:  # noqa: E501
            raise ValueError("Invalid value for `increment`, must not be `None`")  # noqa: E501

        self._increment = increment

    @property
    def min_value(self):
        """Gets the min_value of this SequenceDefinition.  # noqa: E501

        The minimum value of the sequence  # noqa: E501

        :return: The min_value of this SequenceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this SequenceDefinition.

        The minimum value of the sequence  # noqa: E501

        :param min_value: The min_value of this SequenceDefinition.  # noqa: E501
        :type min_value: int
        """
        if self.local_vars_configuration.client_side_validation and min_value is None:  # noqa: E501
            raise ValueError("Invalid value for `min_value`, must not be `None`")  # noqa: E501

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this SequenceDefinition.  # noqa: E501

        The maximum value of the sequence  # noqa: E501

        :return: The max_value of this SequenceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this SequenceDefinition.

        The maximum value of the sequence  # noqa: E501

        :param max_value: The max_value of this SequenceDefinition.  # noqa: E501
        :type max_value: int
        """
        if self.local_vars_configuration.client_side_validation and max_value is None:  # noqa: E501
            raise ValueError("Invalid value for `max_value`, must not be `None`")  # noqa: E501

        self._max_value = max_value

    @property
    def start(self):
        """Gets the start of this SequenceDefinition.  # noqa: E501

        The start value of the sequence  # noqa: E501

        :return: The start of this SequenceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SequenceDefinition.

        The start value of the sequence  # noqa: E501

        :param start: The start of this SequenceDefinition.  # noqa: E501
        :type start: int
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def value(self):
        """Gets the value of this SequenceDefinition.  # noqa: E501

        The last used value of the sequence  # noqa: E501

        :return: The value of this SequenceDefinition.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SequenceDefinition.

        The last used value of the sequence  # noqa: E501

        :param value: The value of this SequenceDefinition.  # noqa: E501
        :type value: int
        """

        self._value = value

    @property
    def cycle(self):
        """Gets the cycle of this SequenceDefinition.  # noqa: E501

        Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value.  # noqa: E501

        :return: The cycle of this SequenceDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this SequenceDefinition.

        Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value.  # noqa: E501

        :param cycle: The cycle of this SequenceDefinition.  # noqa: E501
        :type cycle: bool
        """
        if self.local_vars_configuration.client_side_validation and cycle is None:  # noqa: E501
            raise ValueError("Invalid value for `cycle`, must not be `None`")  # noqa: E501

        self._cycle = cycle

    @property
    def pattern(self):
        """Gets the pattern of this SequenceDefinition.  # noqa: E501

        The pattern to be used to generate next values in the sequence.  # noqa: E501

        :return: The pattern of this SequenceDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this SequenceDefinition.

        The pattern to be used to generate next values in the sequence.  # noqa: E501

        :param pattern: The pattern of this SequenceDefinition.  # noqa: E501
        :type pattern: str
        """

        self._pattern = pattern

    @property
    def links(self):
        """Gets the links of this SequenceDefinition.  # noqa: E501


        :return: The links of this SequenceDefinition.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SequenceDefinition.


        :param links: The links of this SequenceDefinition.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, SequenceDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SequenceDefinition):
            return True

        return self.to_dict() != other.to_dict()
