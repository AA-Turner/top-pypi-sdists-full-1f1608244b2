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


class GeneralLedgerProfileResponse(object):
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
        'href': 'str',
        'chart_of_accounts_id': 'ResourceId',
        'general_ledger_profile_code': 'str',
        'display_name': 'str',
        'description': 'str',
        'general_ledger_profile_mappings': 'list[GeneralLedgerProfileMapping]',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'chart_of_accounts_id': 'chartOfAccountsId',
        'general_ledger_profile_code': 'generalLedgerProfileCode',
        'display_name': 'displayName',
        'description': 'description',
        'general_ledger_profile_mappings': 'generalLedgerProfileMappings',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'chart_of_accounts_id': 'required',
        'general_ledger_profile_code': 'required',
        'display_name': 'required',
        'description': 'optional',
        'general_ledger_profile_mappings': 'required',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, chart_of_accounts_id=None, general_ledger_profile_code=None, display_name=None, description=None, general_ledger_profile_mappings=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """GeneralLedgerProfileResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param chart_of_accounts_id:  (required)
        :type chart_of_accounts_id: lusid.ResourceId
        :param general_ledger_profile_code:  The unique code for the General Ledger Profile (required)
        :type general_ledger_profile_code: str
        :param display_name:  The name of the General Ledger Profile (required)
        :type display_name: str
        :param description:  A description for the General Ledger Profile
        :type description: str
        :param general_ledger_profile_mappings:  Rules for mapping Account or property values to aggregation pattern definitions (required)
        :type general_ledger_profile_mappings: list[lusid.GeneralLedgerProfileMapping]
        :param version: 
        :type version: lusid.Version
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._chart_of_accounts_id = None
        self._general_ledger_profile_code = None
        self._display_name = None
        self._description = None
        self._general_ledger_profile_mappings = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.chart_of_accounts_id = chart_of_accounts_id
        self.general_ledger_profile_code = general_ledger_profile_code
        self.display_name = display_name
        self.description = description
        self.general_ledger_profile_mappings = general_ledger_profile_mappings
        if version is not None:
            self.version = version
        self.links = links

    @property
    def href(self):
        """Gets the href of this GeneralLedgerProfileResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GeneralLedgerProfileResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this GeneralLedgerProfileResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def chart_of_accounts_id(self):
        """Gets the chart_of_accounts_id of this GeneralLedgerProfileResponse.  # noqa: E501


        :return: The chart_of_accounts_id of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._chart_of_accounts_id

    @chart_of_accounts_id.setter
    def chart_of_accounts_id(self, chart_of_accounts_id):
        """Sets the chart_of_accounts_id of this GeneralLedgerProfileResponse.


        :param chart_of_accounts_id: The chart_of_accounts_id of this GeneralLedgerProfileResponse.  # noqa: E501
        :type chart_of_accounts_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and chart_of_accounts_id is None:  # noqa: E501
            raise ValueError("Invalid value for `chart_of_accounts_id`, must not be `None`")  # noqa: E501

        self._chart_of_accounts_id = chart_of_accounts_id

    @property
    def general_ledger_profile_code(self):
        """Gets the general_ledger_profile_code of this GeneralLedgerProfileResponse.  # noqa: E501

        The unique code for the General Ledger Profile  # noqa: E501

        :return: The general_ledger_profile_code of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: str
        """
        return self._general_ledger_profile_code

    @general_ledger_profile_code.setter
    def general_ledger_profile_code(self, general_ledger_profile_code):
        """Sets the general_ledger_profile_code of this GeneralLedgerProfileResponse.

        The unique code for the General Ledger Profile  # noqa: E501

        :param general_ledger_profile_code: The general_ledger_profile_code of this GeneralLedgerProfileResponse.  # noqa: E501
        :type general_ledger_profile_code: str
        """
        if self.local_vars_configuration.client_side_validation and general_ledger_profile_code is None:  # noqa: E501
            raise ValueError("Invalid value for `general_ledger_profile_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_profile_code is not None and len(general_ledger_profile_code) > 64):
            raise ValueError("Invalid value for `general_ledger_profile_code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_profile_code is not None and len(general_ledger_profile_code) < 1):
            raise ValueError("Invalid value for `general_ledger_profile_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_profile_code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', general_ledger_profile_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `general_ledger_profile_code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._general_ledger_profile_code = general_ledger_profile_code

    @property
    def display_name(self):
        """Gets the display_name of this GeneralLedgerProfileResponse.  # noqa: E501

        The name of the General Ledger Profile  # noqa: E501

        :return: The display_name of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GeneralLedgerProfileResponse.

        The name of the General Ledger Profile  # noqa: E501

        :param display_name: The display_name of this GeneralLedgerProfileResponse.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this GeneralLedgerProfileResponse.  # noqa: E501

        A description for the General Ledger Profile  # noqa: E501

        :return: The description of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GeneralLedgerProfileResponse.

        A description for the General Ledger Profile  # noqa: E501

        :param description: The description of this GeneralLedgerProfileResponse.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def general_ledger_profile_mappings(self):
        """Gets the general_ledger_profile_mappings of this GeneralLedgerProfileResponse.  # noqa: E501

        Rules for mapping Account or property values to aggregation pattern definitions  # noqa: E501

        :return: The general_ledger_profile_mappings of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: list[lusid.GeneralLedgerProfileMapping]
        """
        return self._general_ledger_profile_mappings

    @general_ledger_profile_mappings.setter
    def general_ledger_profile_mappings(self, general_ledger_profile_mappings):
        """Sets the general_ledger_profile_mappings of this GeneralLedgerProfileResponse.

        Rules for mapping Account or property values to aggregation pattern definitions  # noqa: E501

        :param general_ledger_profile_mappings: The general_ledger_profile_mappings of this GeneralLedgerProfileResponse.  # noqa: E501
        :type general_ledger_profile_mappings: list[lusid.GeneralLedgerProfileMapping]
        """
        if self.local_vars_configuration.client_side_validation and general_ledger_profile_mappings is None:  # noqa: E501
            raise ValueError("Invalid value for `general_ledger_profile_mappings`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_profile_mappings is not None and len(general_ledger_profile_mappings) > 1000):
            raise ValueError("Invalid value for `general_ledger_profile_mappings`, number of items must be less than or equal to `1000`")  # noqa: E501

        self._general_ledger_profile_mappings = general_ledger_profile_mappings

    @property
    def version(self):
        """Gets the version of this GeneralLedgerProfileResponse.  # noqa: E501


        :return: The version of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GeneralLedgerProfileResponse.


        :param version: The version of this GeneralLedgerProfileResponse.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this GeneralLedgerProfileResponse.  # noqa: E501


        :return: The links of this GeneralLedgerProfileResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GeneralLedgerProfileResponse.


        :param links: The links of this GeneralLedgerProfileResponse.  # noqa: E501
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
        if not isinstance(other, GeneralLedgerProfileResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralLedgerProfileResponse):
            return True

        return self.to_dict() != other.to_dict()
