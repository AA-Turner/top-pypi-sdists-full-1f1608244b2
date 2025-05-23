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


class GroupReconciliationUserReviewBreakCode(object):
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
        'break_code': 'str',
        'user_id': 'str',
        'as_at_added': 'datetime',
        'as_at_invalid': 'datetime'
    }

    attribute_map = {
        'break_code': 'breakCode',
        'user_id': 'userId',
        'as_at_added': 'asAtAdded',
        'as_at_invalid': 'asAtInvalid'
    }

    required_map = {
        'break_code': 'required',
        'user_id': 'optional',
        'as_at_added': 'optional',
        'as_at_invalid': 'optional'
    }

    def __init__(self, break_code=None, user_id=None, as_at_added=None, as_at_invalid=None, local_vars_configuration=None):  # noqa: E501
        """GroupReconciliationUserReviewBreakCode - a model defined in OpenAPI"
        
        :param break_code:  The break code of the reconciliation result. (required)
        :type break_code: str
        :param user_id:  Id of the user who made a User Review input.
        :type user_id: str
        :param as_at_added:  The timestamp of the added User Review input.
        :type as_at_added: datetime
        :param as_at_invalid:  The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.
        :type as_at_invalid: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._break_code = None
        self._user_id = None
        self._as_at_added = None
        self._as_at_invalid = None
        self.discriminator = None

        self.break_code = break_code
        self.user_id = user_id
        if as_at_added is not None:
            self.as_at_added = as_at_added
        if as_at_invalid is not None:
            self.as_at_invalid = as_at_invalid

    @property
    def break_code(self):
        """Gets the break_code of this GroupReconciliationUserReviewBreakCode.  # noqa: E501

        The break code of the reconciliation result.  # noqa: E501

        :return: The break_code of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :rtype: str
        """
        return self._break_code

    @break_code.setter
    def break_code(self, break_code):
        """Sets the break_code of this GroupReconciliationUserReviewBreakCode.

        The break code of the reconciliation result.  # noqa: E501

        :param break_code: The break_code of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :type break_code: str
        """
        if self.local_vars_configuration.client_side_validation and break_code is None:  # noqa: E501
            raise ValueError("Invalid value for `break_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                break_code is not None and len(break_code) < 1):
            raise ValueError("Invalid value for `break_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._break_code = break_code

    @property
    def user_id(self):
        """Gets the user_id of this GroupReconciliationUserReviewBreakCode.  # noqa: E501

        Id of the user who made a User Review input.  # noqa: E501

        :return: The user_id of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupReconciliationUserReviewBreakCode.

        Id of the user who made a User Review input.  # noqa: E501

        :param user_id: The user_id of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :type user_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) > 16384):
            raise ValueError("Invalid value for `user_id`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 0):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_id = user_id

    @property
    def as_at_added(self):
        """Gets the as_at_added of this GroupReconciliationUserReviewBreakCode.  # noqa: E501

        The timestamp of the added User Review input.  # noqa: E501

        :return: The as_at_added of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_added

    @as_at_added.setter
    def as_at_added(self, as_at_added):
        """Sets the as_at_added of this GroupReconciliationUserReviewBreakCode.

        The timestamp of the added User Review input.  # noqa: E501

        :param as_at_added: The as_at_added of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :type as_at_added: datetime
        """

        self._as_at_added = as_at_added

    @property
    def as_at_invalid(self):
        """Gets the as_at_invalid of this GroupReconciliationUserReviewBreakCode.  # noqa: E501

        The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.  # noqa: E501

        :return: The as_at_invalid of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_invalid

    @as_at_invalid.setter
    def as_at_invalid(self, as_at_invalid):
        """Sets the as_at_invalid of this GroupReconciliationUserReviewBreakCode.

        The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.  # noqa: E501

        :param as_at_invalid: The as_at_invalid of this GroupReconciliationUserReviewBreakCode.  # noqa: E501
        :type as_at_invalid: datetime
        """

        self._as_at_invalid = as_at_invalid

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
        if not isinstance(other, GroupReconciliationUserReviewBreakCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupReconciliationUserReviewBreakCode):
            return True

        return self.to_dict() != other.to_dict()
