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


class GroupReconciliationRunRequest(object):
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
        'instance_id': 'str',
        'dates_to_reconcile': 'GroupReconciliationDates'
    }

    attribute_map = {
        'instance_id': 'instanceId',
        'dates_to_reconcile': 'datesToReconcile'
    }

    required_map = {
        'instance_id': 'required',
        'dates_to_reconcile': 'optional'
    }

    def __init__(self, instance_id=None, dates_to_reconcile=None, local_vars_configuration=None):  # noqa: E501
        """GroupReconciliationRunRequest - a model defined in OpenAPI"
        
        :param instance_id:  Reconciliation run Id. Consists of run type (manual or workflow) and identifier. (required)
        :type instance_id: str
        :param dates_to_reconcile: 
        :type dates_to_reconcile: lusid.GroupReconciliationDates

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instance_id = None
        self._dates_to_reconcile = None
        self.discriminator = None

        self.instance_id = instance_id
        if dates_to_reconcile is not None:
            self.dates_to_reconcile = dates_to_reconcile

    @property
    def instance_id(self):
        """Gets the instance_id of this GroupReconciliationRunRequest.  # noqa: E501

        Reconciliation run Id. Consists of run type (manual or workflow) and identifier.  # noqa: E501

        :return: The instance_id of this GroupReconciliationRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this GroupReconciliationRunRequest.

        Reconciliation run Id. Consists of run type (manual or workflow) and identifier.  # noqa: E501

        :param instance_id: The instance_id of this GroupReconciliationRunRequest.  # noqa: E501
        :type instance_id: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) > 64):
            raise ValueError("Invalid value for `instance_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) < 1):
            raise ValueError("Invalid value for `instance_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def dates_to_reconcile(self):
        """Gets the dates_to_reconcile of this GroupReconciliationRunRequest.  # noqa: E501


        :return: The dates_to_reconcile of this GroupReconciliationRunRequest.  # noqa: E501
        :rtype: lusid.GroupReconciliationDates
        """
        return self._dates_to_reconcile

    @dates_to_reconcile.setter
    def dates_to_reconcile(self, dates_to_reconcile):
        """Sets the dates_to_reconcile of this GroupReconciliationRunRequest.


        :param dates_to_reconcile: The dates_to_reconcile of this GroupReconciliationRunRequest.  # noqa: E501
        :type dates_to_reconcile: lusid.GroupReconciliationDates
        """

        self._dates_to_reconcile = dates_to_reconcile

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
        if not isinstance(other, GroupReconciliationRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupReconciliationRunRequest):
            return True

        return self.to_dict() != other.to_dict()
