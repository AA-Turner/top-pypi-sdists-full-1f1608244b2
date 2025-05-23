# coding: utf-8

"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

import pprint
import re  # noqa: F401

from typing import TYPE_CHECKING

import six

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class V1UpdateUserRequest(object):
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
        'agree_to_terms_and_conditions': 'bool',
        'complete_sign_up': 'bool',
        'completed_project_onboarding': 'bool',
        'country': 'str',
        'email': 'str',
        'first_name': 'str',
        'general_audience_mode': 'bool',
        'last_name': 'str',
        'non_developer_mode': 'bool',
        'opted_in_marketing_emails': 'bool',
        'organization': 'str',
        'preferred_color_scheme': 'str',
        'preferred_ide': 'str',
        'preferred_shell': 'str',
        'preferred_vscode_marketplace': 'str',
        'role': 'str',
        'saw_create_first_project_dialog': 'bool',
        'saw_forums_login_merge_dialog': 'bool',
        'saw_free_credits_notification': 'bool',
        'user_metadata': 'str',
        'username': 'str',
        'website': 'str'
    }

    attribute_map = {
        'agree_to_terms_and_conditions': 'agreeToTermsAndConditions',
        'complete_sign_up': 'completeSignUp',
        'completed_project_onboarding': 'completedProjectOnboarding',
        'country': 'country',
        'email': 'email',
        'first_name': 'firstName',
        'general_audience_mode': 'generalAudienceMode',
        'last_name': 'lastName',
        'non_developer_mode': 'nonDeveloperMode',
        'opted_in_marketing_emails': 'optedInMarketingEmails',
        'organization': 'organization',
        'preferred_color_scheme': 'preferredColorScheme',
        'preferred_ide': 'preferredIde',
        'preferred_shell': 'preferredShell',
        'preferred_vscode_marketplace': 'preferredVscodeMarketplace',
        'role': 'role',
        'saw_create_first_project_dialog': 'sawCreateFirstProjectDialog',
        'saw_forums_login_merge_dialog': 'sawForumsLoginMergeDialog',
        'saw_free_credits_notification': 'sawFreeCreditsNotification',
        'user_metadata': 'userMetadata',
        'username': 'username',
        'website': 'website'
    }

    def __init__(self, agree_to_terms_and_conditions: 'bool' =None, complete_sign_up: 'bool' =None, completed_project_onboarding: 'bool' =None, country: 'str' =None, email: 'str' =None, first_name: 'str' =None, general_audience_mode: 'bool' =None, last_name: 'str' =None, non_developer_mode: 'bool' =None, opted_in_marketing_emails: 'bool' =None, organization: 'str' =None, preferred_color_scheme: 'str' =None, preferred_ide: 'str' =None, preferred_shell: 'str' =None, preferred_vscode_marketplace: 'str' =None, role: 'str' =None, saw_create_first_project_dialog: 'bool' =None, saw_forums_login_merge_dialog: 'bool' =None, saw_free_credits_notification: 'bool' =None, user_metadata: 'str' =None, username: 'str' =None, website: 'str' =None):  # noqa: E501
        """V1UpdateUserRequest - a model defined in Swagger"""  # noqa: E501
        self._agree_to_terms_and_conditions = None
        self._complete_sign_up = None
        self._completed_project_onboarding = None
        self._country = None
        self._email = None
        self._first_name = None
        self._general_audience_mode = None
        self._last_name = None
        self._non_developer_mode = None
        self._opted_in_marketing_emails = None
        self._organization = None
        self._preferred_color_scheme = None
        self._preferred_ide = None
        self._preferred_shell = None
        self._preferred_vscode_marketplace = None
        self._role = None
        self._saw_create_first_project_dialog = None
        self._saw_forums_login_merge_dialog = None
        self._saw_free_credits_notification = None
        self._user_metadata = None
        self._username = None
        self._website = None
        self.discriminator = None
        if agree_to_terms_and_conditions is not None:
            self.agree_to_terms_and_conditions = agree_to_terms_and_conditions
        if complete_sign_up is not None:
            self.complete_sign_up = complete_sign_up
        if completed_project_onboarding is not None:
            self.completed_project_onboarding = completed_project_onboarding
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if general_audience_mode is not None:
            self.general_audience_mode = general_audience_mode
        if last_name is not None:
            self.last_name = last_name
        if non_developer_mode is not None:
            self.non_developer_mode = non_developer_mode
        if opted_in_marketing_emails is not None:
            self.opted_in_marketing_emails = opted_in_marketing_emails
        if organization is not None:
            self.organization = organization
        if preferred_color_scheme is not None:
            self.preferred_color_scheme = preferred_color_scheme
        if preferred_ide is not None:
            self.preferred_ide = preferred_ide
        if preferred_shell is not None:
            self.preferred_shell = preferred_shell
        if preferred_vscode_marketplace is not None:
            self.preferred_vscode_marketplace = preferred_vscode_marketplace
        if role is not None:
            self.role = role
        if saw_create_first_project_dialog is not None:
            self.saw_create_first_project_dialog = saw_create_first_project_dialog
        if saw_forums_login_merge_dialog is not None:
            self.saw_forums_login_merge_dialog = saw_forums_login_merge_dialog
        if saw_free_credits_notification is not None:
            self.saw_free_credits_notification = saw_free_credits_notification
        if user_metadata is not None:
            self.user_metadata = user_metadata
        if username is not None:
            self.username = username
        if website is not None:
            self.website = website

    @property
    def agree_to_terms_and_conditions(self) -> 'bool':
        """Gets the agree_to_terms_and_conditions of this V1UpdateUserRequest.  # noqa: E501


        :return: The agree_to_terms_and_conditions of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._agree_to_terms_and_conditions

    @agree_to_terms_and_conditions.setter
    def agree_to_terms_and_conditions(self, agree_to_terms_and_conditions: 'bool'):
        """Sets the agree_to_terms_and_conditions of this V1UpdateUserRequest.


        :param agree_to_terms_and_conditions: The agree_to_terms_and_conditions of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._agree_to_terms_and_conditions = agree_to_terms_and_conditions

    @property
    def complete_sign_up(self) -> 'bool':
        """Gets the complete_sign_up of this V1UpdateUserRequest.  # noqa: E501


        :return: The complete_sign_up of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._complete_sign_up

    @complete_sign_up.setter
    def complete_sign_up(self, complete_sign_up: 'bool'):
        """Sets the complete_sign_up of this V1UpdateUserRequest.


        :param complete_sign_up: The complete_sign_up of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._complete_sign_up = complete_sign_up

    @property
    def completed_project_onboarding(self) -> 'bool':
        """Gets the completed_project_onboarding of this V1UpdateUserRequest.  # noqa: E501


        :return: The completed_project_onboarding of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._completed_project_onboarding

    @completed_project_onboarding.setter
    def completed_project_onboarding(self, completed_project_onboarding: 'bool'):
        """Sets the completed_project_onboarding of this V1UpdateUserRequest.


        :param completed_project_onboarding: The completed_project_onboarding of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._completed_project_onboarding = completed_project_onboarding

    @property
    def country(self) -> 'str':
        """Gets the country of this V1UpdateUserRequest.  # noqa: E501


        :return: The country of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: 'str'):
        """Sets the country of this V1UpdateUserRequest.


        :param country: The country of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self) -> 'str':
        """Gets the email of this V1UpdateUserRequest.  # noqa: E501


        :return: The email of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: 'str'):
        """Sets the email of this V1UpdateUserRequest.


        :param email: The email of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self) -> 'str':
        """Gets the first_name of this V1UpdateUserRequest.  # noqa: E501


        :return: The first_name of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: 'str'):
        """Sets the first_name of this V1UpdateUserRequest.


        :param first_name: The first_name of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def general_audience_mode(self) -> 'bool':
        """Gets the general_audience_mode of this V1UpdateUserRequest.  # noqa: E501


        :return: The general_audience_mode of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._general_audience_mode

    @general_audience_mode.setter
    def general_audience_mode(self, general_audience_mode: 'bool'):
        """Sets the general_audience_mode of this V1UpdateUserRequest.


        :param general_audience_mode: The general_audience_mode of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._general_audience_mode = general_audience_mode

    @property
    def last_name(self) -> 'str':
        """Gets the last_name of this V1UpdateUserRequest.  # noqa: E501


        :return: The last_name of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: 'str'):
        """Sets the last_name of this V1UpdateUserRequest.


        :param last_name: The last_name of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def non_developer_mode(self) -> 'bool':
        """Gets the non_developer_mode of this V1UpdateUserRequest.  # noqa: E501


        :return: The non_developer_mode of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._non_developer_mode

    @non_developer_mode.setter
    def non_developer_mode(self, non_developer_mode: 'bool'):
        """Sets the non_developer_mode of this V1UpdateUserRequest.


        :param non_developer_mode: The non_developer_mode of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._non_developer_mode = non_developer_mode

    @property
    def opted_in_marketing_emails(self) -> 'bool':
        """Gets the opted_in_marketing_emails of this V1UpdateUserRequest.  # noqa: E501


        :return: The opted_in_marketing_emails of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._opted_in_marketing_emails

    @opted_in_marketing_emails.setter
    def opted_in_marketing_emails(self, opted_in_marketing_emails: 'bool'):
        """Sets the opted_in_marketing_emails of this V1UpdateUserRequest.


        :param opted_in_marketing_emails: The opted_in_marketing_emails of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._opted_in_marketing_emails = opted_in_marketing_emails

    @property
    def organization(self) -> 'str':
        """Gets the organization of this V1UpdateUserRequest.  # noqa: E501


        :return: The organization of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization: 'str'):
        """Sets the organization of this V1UpdateUserRequest.


        :param organization: The organization of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def preferred_color_scheme(self) -> 'str':
        """Gets the preferred_color_scheme of this V1UpdateUserRequest.  # noqa: E501


        :return: The preferred_color_scheme of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._preferred_color_scheme

    @preferred_color_scheme.setter
    def preferred_color_scheme(self, preferred_color_scheme: 'str'):
        """Sets the preferred_color_scheme of this V1UpdateUserRequest.


        :param preferred_color_scheme: The preferred_color_scheme of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._preferred_color_scheme = preferred_color_scheme

    @property
    def preferred_ide(self) -> 'str':
        """Gets the preferred_ide of this V1UpdateUserRequest.  # noqa: E501


        :return: The preferred_ide of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._preferred_ide

    @preferred_ide.setter
    def preferred_ide(self, preferred_ide: 'str'):
        """Sets the preferred_ide of this V1UpdateUserRequest.


        :param preferred_ide: The preferred_ide of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._preferred_ide = preferred_ide

    @property
    def preferred_shell(self) -> 'str':
        """Gets the preferred_shell of this V1UpdateUserRequest.  # noqa: E501


        :return: The preferred_shell of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._preferred_shell

    @preferred_shell.setter
    def preferred_shell(self, preferred_shell: 'str'):
        """Sets the preferred_shell of this V1UpdateUserRequest.


        :param preferred_shell: The preferred_shell of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._preferred_shell = preferred_shell

    @property
    def preferred_vscode_marketplace(self) -> 'str':
        """Gets the preferred_vscode_marketplace of this V1UpdateUserRequest.  # noqa: E501


        :return: The preferred_vscode_marketplace of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._preferred_vscode_marketplace

    @preferred_vscode_marketplace.setter
    def preferred_vscode_marketplace(self, preferred_vscode_marketplace: 'str'):
        """Sets the preferred_vscode_marketplace of this V1UpdateUserRequest.


        :param preferred_vscode_marketplace: The preferred_vscode_marketplace of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._preferred_vscode_marketplace = preferred_vscode_marketplace

    @property
    def role(self) -> 'str':
        """Gets the role of this V1UpdateUserRequest.  # noqa: E501


        :return: The role of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: 'str'):
        """Sets the role of this V1UpdateUserRequest.


        :param role: The role of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def saw_create_first_project_dialog(self) -> 'bool':
        """Gets the saw_create_first_project_dialog of this V1UpdateUserRequest.  # noqa: E501


        :return: The saw_create_first_project_dialog of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._saw_create_first_project_dialog

    @saw_create_first_project_dialog.setter
    def saw_create_first_project_dialog(self, saw_create_first_project_dialog: 'bool'):
        """Sets the saw_create_first_project_dialog of this V1UpdateUserRequest.


        :param saw_create_first_project_dialog: The saw_create_first_project_dialog of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._saw_create_first_project_dialog = saw_create_first_project_dialog

    @property
    def saw_forums_login_merge_dialog(self) -> 'bool':
        """Gets the saw_forums_login_merge_dialog of this V1UpdateUserRequest.  # noqa: E501


        :return: The saw_forums_login_merge_dialog of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._saw_forums_login_merge_dialog

    @saw_forums_login_merge_dialog.setter
    def saw_forums_login_merge_dialog(self, saw_forums_login_merge_dialog: 'bool'):
        """Sets the saw_forums_login_merge_dialog of this V1UpdateUserRequest.


        :param saw_forums_login_merge_dialog: The saw_forums_login_merge_dialog of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._saw_forums_login_merge_dialog = saw_forums_login_merge_dialog

    @property
    def saw_free_credits_notification(self) -> 'bool':
        """Gets the saw_free_credits_notification of this V1UpdateUserRequest.  # noqa: E501


        :return: The saw_free_credits_notification of this V1UpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._saw_free_credits_notification

    @saw_free_credits_notification.setter
    def saw_free_credits_notification(self, saw_free_credits_notification: 'bool'):
        """Sets the saw_free_credits_notification of this V1UpdateUserRequest.


        :param saw_free_credits_notification: The saw_free_credits_notification of this V1UpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._saw_free_credits_notification = saw_free_credits_notification

    @property
    def user_metadata(self) -> 'str':
        """Gets the user_metadata of this V1UpdateUserRequest.  # noqa: E501


        :return: The user_metadata of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata: 'str'):
        """Sets the user_metadata of this V1UpdateUserRequest.


        :param user_metadata: The user_metadata of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._user_metadata = user_metadata

    @property
    def username(self) -> 'str':
        """Gets the username of this V1UpdateUserRequest.  # noqa: E501


        :return: The username of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: 'str'):
        """Sets the username of this V1UpdateUserRequest.


        :param username: The username of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def website(self) -> 'str':
        """Gets the website of this V1UpdateUserRequest.  # noqa: E501


        :return: The website of this V1UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: 'str'):
        """Sets the website of this V1UpdateUserRequest.


        :param website: The website of this V1UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._website = website

    def to_dict(self) -> dict:
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
        if issubclass(V1UpdateUserRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1UpdateUserRequest') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1UpdateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1UpdateUserRequest') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
