# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.24
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


class ReconciliationBreakId(object):
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
        'reconciliation_run': 'ReconciliationRunId',
        'break_id': 'str',
        'as_string': 'str'
    }

    attribute_map = {
        'reconciliation_run': 'reconciliationRun',
        'break_id': 'breakId',
        'as_string': 'asString'
    }

    required_map = {
        'reconciliation_run': 'optional',
        'break_id': 'optional',
        'as_string': 'optional'
    }

    def __init__(self, reconciliation_run=None, break_id=None, as_string=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationBreakId - a model defined in OpenAPI"
        
        :param reconciliation_run: 
        :type reconciliation_run: lusid.ReconciliationRunId
        :param break_id: 
        :type break_id: str
        :param as_string: 
        :type as_string: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._reconciliation_run = None
        self._break_id = None
        self._as_string = None
        self.discriminator = None

        if reconciliation_run is not None:
            self.reconciliation_run = reconciliation_run
        self.break_id = break_id
        self.as_string = as_string

    @property
    def reconciliation_run(self):
        """Gets the reconciliation_run of this ReconciliationBreakId.  # noqa: E501


        :return: The reconciliation_run of this ReconciliationBreakId.  # noqa: E501
        :rtype: lusid.ReconciliationRunId
        """
        return self._reconciliation_run

    @reconciliation_run.setter
    def reconciliation_run(self, reconciliation_run):
        """Sets the reconciliation_run of this ReconciliationBreakId.


        :param reconciliation_run: The reconciliation_run of this ReconciliationBreakId.  # noqa: E501
        :type reconciliation_run: lusid.ReconciliationRunId
        """

        self._reconciliation_run = reconciliation_run

    @property
    def break_id(self):
        """Gets the break_id of this ReconciliationBreakId.  # noqa: E501


        :return: The break_id of this ReconciliationBreakId.  # noqa: E501
        :rtype: str
        """
        return self._break_id

    @break_id.setter
    def break_id(self, break_id):
        """Sets the break_id of this ReconciliationBreakId.


        :param break_id: The break_id of this ReconciliationBreakId.  # noqa: E501
        :type break_id: str
        """

        self._break_id = break_id

    @property
    def as_string(self):
        """Gets the as_string of this ReconciliationBreakId.  # noqa: E501


        :return: The as_string of this ReconciliationBreakId.  # noqa: E501
        :rtype: str
        """
        return self._as_string

    @as_string.setter
    def as_string(self, as_string):
        """Sets the as_string of this ReconciliationBreakId.


        :param as_string: The as_string of this ReconciliationBreakId.  # noqa: E501
        :type as_string: str
        """

        self._as_string = as_string

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
        if not isinstance(other, ReconciliationBreakId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationBreakId):
            return True

        return self.to_dict() != other.to_dict()
