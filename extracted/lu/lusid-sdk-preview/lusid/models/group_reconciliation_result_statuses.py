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


class GroupReconciliationResultStatuses(object):
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
        'count_new': 'int',
        'link_new': 'Link',
        'count_confirmed': 'int',
        'link_confirmed': 'Link',
        'count_changed': 'int',
        'link_changed': 'Link'
    }

    attribute_map = {
        'count_new': 'countNew',
        'link_new': 'linkNew',
        'count_confirmed': 'countConfirmed',
        'link_confirmed': 'linkConfirmed',
        'count_changed': 'countChanged',
        'link_changed': 'linkChanged'
    }

    required_map = {
        'count_new': 'required',
        'link_new': 'required',
        'count_confirmed': 'required',
        'link_confirmed': 'required',
        'count_changed': 'required',
        'link_changed': 'required'
    }

    def __init__(self, count_new=None, link_new=None, count_confirmed=None, link_confirmed=None, count_changed=None, link_changed=None, local_vars_configuration=None):  # noqa: E501
        """GroupReconciliationResultStatuses - a model defined in OpenAPI"
        
        :param count_new:  The number of comparison results of resultStatus \"New\" with this instanceId and reconciliationType (required)
        :type count_new: int
        :param link_new:  (required)
        :type link_new: lusid.Link
        :param count_confirmed:  The number of comparison results of resultStatus \"Confirmed\" with this instanceId and reconciliationType (required)
        :type count_confirmed: int
        :param link_confirmed:  (required)
        :type link_confirmed: lusid.Link
        :param count_changed:  The number of comparison results of resultStatus \"Changed\" with this instanceId and reconciliationType (required)
        :type count_changed: int
        :param link_changed:  (required)
        :type link_changed: lusid.Link

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count_new = None
        self._link_new = None
        self._count_confirmed = None
        self._link_confirmed = None
        self._count_changed = None
        self._link_changed = None
        self.discriminator = None

        self.count_new = count_new
        self.link_new = link_new
        self.count_confirmed = count_confirmed
        self.link_confirmed = link_confirmed
        self.count_changed = count_changed
        self.link_changed = link_changed

    @property
    def count_new(self):
        """Gets the count_new of this GroupReconciliationResultStatuses.  # noqa: E501

        The number of comparison results of resultStatus \"New\" with this instanceId and reconciliationType  # noqa: E501

        :return: The count_new of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: int
        """
        return self._count_new

    @count_new.setter
    def count_new(self, count_new):
        """Sets the count_new of this GroupReconciliationResultStatuses.

        The number of comparison results of resultStatus \"New\" with this instanceId and reconciliationType  # noqa: E501

        :param count_new: The count_new of this GroupReconciliationResultStatuses.  # noqa: E501
        :type count_new: int
        """
        if self.local_vars_configuration.client_side_validation and count_new is None:  # noqa: E501
            raise ValueError("Invalid value for `count_new`, must not be `None`")  # noqa: E501

        self._count_new = count_new

    @property
    def link_new(self):
        """Gets the link_new of this GroupReconciliationResultStatuses.  # noqa: E501


        :return: The link_new of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: lusid.Link
        """
        return self._link_new

    @link_new.setter
    def link_new(self, link_new):
        """Sets the link_new of this GroupReconciliationResultStatuses.


        :param link_new: The link_new of this GroupReconciliationResultStatuses.  # noqa: E501
        :type link_new: lusid.Link
        """
        if self.local_vars_configuration.client_side_validation and link_new is None:  # noqa: E501
            raise ValueError("Invalid value for `link_new`, must not be `None`")  # noqa: E501

        self._link_new = link_new

    @property
    def count_confirmed(self):
        """Gets the count_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501

        The number of comparison results of resultStatus \"Confirmed\" with this instanceId and reconciliationType  # noqa: E501

        :return: The count_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: int
        """
        return self._count_confirmed

    @count_confirmed.setter
    def count_confirmed(self, count_confirmed):
        """Sets the count_confirmed of this GroupReconciliationResultStatuses.

        The number of comparison results of resultStatus \"Confirmed\" with this instanceId and reconciliationType  # noqa: E501

        :param count_confirmed: The count_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501
        :type count_confirmed: int
        """
        if self.local_vars_configuration.client_side_validation and count_confirmed is None:  # noqa: E501
            raise ValueError("Invalid value for `count_confirmed`, must not be `None`")  # noqa: E501

        self._count_confirmed = count_confirmed

    @property
    def link_confirmed(self):
        """Gets the link_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501


        :return: The link_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: lusid.Link
        """
        return self._link_confirmed

    @link_confirmed.setter
    def link_confirmed(self, link_confirmed):
        """Sets the link_confirmed of this GroupReconciliationResultStatuses.


        :param link_confirmed: The link_confirmed of this GroupReconciliationResultStatuses.  # noqa: E501
        :type link_confirmed: lusid.Link
        """
        if self.local_vars_configuration.client_side_validation and link_confirmed is None:  # noqa: E501
            raise ValueError("Invalid value for `link_confirmed`, must not be `None`")  # noqa: E501

        self._link_confirmed = link_confirmed

    @property
    def count_changed(self):
        """Gets the count_changed of this GroupReconciliationResultStatuses.  # noqa: E501

        The number of comparison results of resultStatus \"Changed\" with this instanceId and reconciliationType  # noqa: E501

        :return: The count_changed of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: int
        """
        return self._count_changed

    @count_changed.setter
    def count_changed(self, count_changed):
        """Sets the count_changed of this GroupReconciliationResultStatuses.

        The number of comparison results of resultStatus \"Changed\" with this instanceId and reconciliationType  # noqa: E501

        :param count_changed: The count_changed of this GroupReconciliationResultStatuses.  # noqa: E501
        :type count_changed: int
        """
        if self.local_vars_configuration.client_side_validation and count_changed is None:  # noqa: E501
            raise ValueError("Invalid value for `count_changed`, must not be `None`")  # noqa: E501

        self._count_changed = count_changed

    @property
    def link_changed(self):
        """Gets the link_changed of this GroupReconciliationResultStatuses.  # noqa: E501


        :return: The link_changed of this GroupReconciliationResultStatuses.  # noqa: E501
        :rtype: lusid.Link
        """
        return self._link_changed

    @link_changed.setter
    def link_changed(self, link_changed):
        """Sets the link_changed of this GroupReconciliationResultStatuses.


        :param link_changed: The link_changed of this GroupReconciliationResultStatuses.  # noqa: E501
        :type link_changed: lusid.Link
        """
        if self.local_vars_configuration.client_side_validation and link_changed is None:  # noqa: E501
            raise ValueError("Invalid value for `link_changed`, must not be `None`")  # noqa: E501

        self._link_changed = link_changed

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
        if not isinstance(other, GroupReconciliationResultStatuses):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupReconciliationResultStatuses):
            return True

        return self.to_dict() != other.to_dict()
