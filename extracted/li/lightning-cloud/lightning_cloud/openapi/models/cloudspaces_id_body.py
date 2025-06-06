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

class CloudspacesIdBody(object):
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
        'code_url': 'str',
        'data_connection_mounts': 'list[V1DataConnectionMount]',
        'description': 'str',
        'display_name': 'str',
        'env': 'list[V1EnvVar]',
        'featured': 'bool',
        'hide_files': 'bool',
        'is_cloudspace_private': 'bool',
        'is_code_private': 'bool',
        'is_favorite': 'bool',
        'is_published': 'bool',
        'license': 'str',
        'license_url': 'str',
        'multi_user_edit': 'bool',
        'operating_cost': 'str',
        'paper_authors': 'str',
        'paper_org': 'str',
        'paper_org_avatar_url': 'str',
        'paper_url': 'str',
        'publish_with_compute_name': 'str',
        'tags': 'list[V1CloudSpaceTag]',
        'thumbnail': 'str',
        'thumbnail_file_type': 'str',
        'user_metadata': 'str'
    }

    attribute_map = {
        'code_url': 'codeUrl',
        'data_connection_mounts': 'dataConnectionMounts',
        'description': 'description',
        'display_name': 'displayName',
        'env': 'env',
        'featured': 'featured',
        'hide_files': 'hideFiles',
        'is_cloudspace_private': 'isCloudspacePrivate',
        'is_code_private': 'isCodePrivate',
        'is_favorite': 'isFavorite',
        'is_published': 'isPublished',
        'license': 'license',
        'license_url': 'licenseUrl',
        'multi_user_edit': 'multiUserEdit',
        'operating_cost': 'operatingCost',
        'paper_authors': 'paperAuthors',
        'paper_org': 'paperOrg',
        'paper_org_avatar_url': 'paperOrgAvatarUrl',
        'paper_url': 'paperUrl',
        'publish_with_compute_name': 'publishWithComputeName',
        'tags': 'tags',
        'thumbnail': 'thumbnail',
        'thumbnail_file_type': 'thumbnailFileType',
        'user_metadata': 'userMetadata'
    }

    def __init__(self, code_url: 'str' =None, data_connection_mounts: 'list[V1DataConnectionMount]' =None, description: 'str' =None, display_name: 'str' =None, env: 'list[V1EnvVar]' =None, featured: 'bool' =None, hide_files: 'bool' =None, is_cloudspace_private: 'bool' =None, is_code_private: 'bool' =None, is_favorite: 'bool' =None, is_published: 'bool' =None, license: 'str' =None, license_url: 'str' =None, multi_user_edit: 'bool' =None, operating_cost: 'str' =None, paper_authors: 'str' =None, paper_org: 'str' =None, paper_org_avatar_url: 'str' =None, paper_url: 'str' =None, publish_with_compute_name: 'str' =None, tags: 'list[V1CloudSpaceTag]' =None, thumbnail: 'str' =None, thumbnail_file_type: 'str' =None, user_metadata: 'str' =None):  # noqa: E501
        """CloudspacesIdBody - a model defined in Swagger"""  # noqa: E501
        self._code_url = None
        self._data_connection_mounts = None
        self._description = None
        self._display_name = None
        self._env = None
        self._featured = None
        self._hide_files = None
        self._is_cloudspace_private = None
        self._is_code_private = None
        self._is_favorite = None
        self._is_published = None
        self._license = None
        self._license_url = None
        self._multi_user_edit = None
        self._operating_cost = None
        self._paper_authors = None
        self._paper_org = None
        self._paper_org_avatar_url = None
        self._paper_url = None
        self._publish_with_compute_name = None
        self._tags = None
        self._thumbnail = None
        self._thumbnail_file_type = None
        self._user_metadata = None
        self.discriminator = None
        if code_url is not None:
            self.code_url = code_url
        if data_connection_mounts is not None:
            self.data_connection_mounts = data_connection_mounts
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if env is not None:
            self.env = env
        if featured is not None:
            self.featured = featured
        if hide_files is not None:
            self.hide_files = hide_files
        if is_cloudspace_private is not None:
            self.is_cloudspace_private = is_cloudspace_private
        if is_code_private is not None:
            self.is_code_private = is_code_private
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if is_published is not None:
            self.is_published = is_published
        if license is not None:
            self.license = license
        if license_url is not None:
            self.license_url = license_url
        if multi_user_edit is not None:
            self.multi_user_edit = multi_user_edit
        if operating_cost is not None:
            self.operating_cost = operating_cost
        if paper_authors is not None:
            self.paper_authors = paper_authors
        if paper_org is not None:
            self.paper_org = paper_org
        if paper_org_avatar_url is not None:
            self.paper_org_avatar_url = paper_org_avatar_url
        if paper_url is not None:
            self.paper_url = paper_url
        if publish_with_compute_name is not None:
            self.publish_with_compute_name = publish_with_compute_name
        if tags is not None:
            self.tags = tags
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if thumbnail_file_type is not None:
            self.thumbnail_file_type = thumbnail_file_type
        if user_metadata is not None:
            self.user_metadata = user_metadata

    @property
    def code_url(self) -> 'str':
        """Gets the code_url of this CloudspacesIdBody.  # noqa: E501


        :return: The code_url of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url: 'str'):
        """Sets the code_url of this CloudspacesIdBody.


        :param code_url: The code_url of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._code_url = code_url

    @property
    def data_connection_mounts(self) -> 'list[V1DataConnectionMount]':
        """Gets the data_connection_mounts of this CloudspacesIdBody.  # noqa: E501


        :return: The data_connection_mounts of this CloudspacesIdBody.  # noqa: E501
        :rtype: list[V1DataConnectionMount]
        """
        return self._data_connection_mounts

    @data_connection_mounts.setter
    def data_connection_mounts(self, data_connection_mounts: 'list[V1DataConnectionMount]'):
        """Sets the data_connection_mounts of this CloudspacesIdBody.


        :param data_connection_mounts: The data_connection_mounts of this CloudspacesIdBody.  # noqa: E501
        :type: list[V1DataConnectionMount]
        """

        self._data_connection_mounts = data_connection_mounts

    @property
    def description(self) -> 'str':
        """Gets the description of this CloudspacesIdBody.  # noqa: E501


        :return: The description of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: 'str'):
        """Sets the description of this CloudspacesIdBody.


        :param description: The description of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self) -> 'str':
        """Gets the display_name of this CloudspacesIdBody.  # noqa: E501


        :return: The display_name of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: 'str'):
        """Sets the display_name of this CloudspacesIdBody.


        :param display_name: The display_name of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def env(self) -> 'list[V1EnvVar]':
        """Gets the env of this CloudspacesIdBody.  # noqa: E501


        :return: The env of this CloudspacesIdBody.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env: 'list[V1EnvVar]'):
        """Sets the env of this CloudspacesIdBody.


        :param env: The env of this CloudspacesIdBody.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def featured(self) -> 'bool':
        """Gets the featured of this CloudspacesIdBody.  # noqa: E501


        :return: The featured of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured: 'bool'):
        """Sets the featured of this CloudspacesIdBody.


        :param featured: The featured of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def hide_files(self) -> 'bool':
        """Gets the hide_files of this CloudspacesIdBody.  # noqa: E501


        :return: The hide_files of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._hide_files

    @hide_files.setter
    def hide_files(self, hide_files: 'bool'):
        """Sets the hide_files of this CloudspacesIdBody.


        :param hide_files: The hide_files of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._hide_files = hide_files

    @property
    def is_cloudspace_private(self) -> 'bool':
        """Gets the is_cloudspace_private of this CloudspacesIdBody.  # noqa: E501


        :return: The is_cloudspace_private of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloudspace_private

    @is_cloudspace_private.setter
    def is_cloudspace_private(self, is_cloudspace_private: 'bool'):
        """Sets the is_cloudspace_private of this CloudspacesIdBody.


        :param is_cloudspace_private: The is_cloudspace_private of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._is_cloudspace_private = is_cloudspace_private

    @property
    def is_code_private(self) -> 'bool':
        """Gets the is_code_private of this CloudspacesIdBody.  # noqa: E501


        :return: The is_code_private of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_code_private

    @is_code_private.setter
    def is_code_private(self, is_code_private: 'bool'):
        """Sets the is_code_private of this CloudspacesIdBody.


        :param is_code_private: The is_code_private of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._is_code_private = is_code_private

    @property
    def is_favorite(self) -> 'bool':
        """Gets the is_favorite of this CloudspacesIdBody.  # noqa: E501


        :return: The is_favorite of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite: 'bool'):
        """Sets the is_favorite of this CloudspacesIdBody.


        :param is_favorite: The is_favorite of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._is_favorite = is_favorite

    @property
    def is_published(self) -> 'bool':
        """Gets the is_published of this CloudspacesIdBody.  # noqa: E501


        :return: The is_published of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published: 'bool'):
        """Sets the is_published of this CloudspacesIdBody.


        :param is_published: The is_published of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._is_published = is_published

    @property
    def license(self) -> 'str':
        """Gets the license of this CloudspacesIdBody.  # noqa: E501


        :return: The license of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license: 'str'):
        """Sets the license of this CloudspacesIdBody.


        :param license: The license of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def license_url(self) -> 'str':
        """Gets the license_url of this CloudspacesIdBody.  # noqa: E501


        :return: The license_url of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._license_url

    @license_url.setter
    def license_url(self, license_url: 'str'):
        """Sets the license_url of this CloudspacesIdBody.


        :param license_url: The license_url of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._license_url = license_url

    @property
    def multi_user_edit(self) -> 'bool':
        """Gets the multi_user_edit of this CloudspacesIdBody.  # noqa: E501


        :return: The multi_user_edit of this CloudspacesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._multi_user_edit

    @multi_user_edit.setter
    def multi_user_edit(self, multi_user_edit: 'bool'):
        """Sets the multi_user_edit of this CloudspacesIdBody.


        :param multi_user_edit: The multi_user_edit of this CloudspacesIdBody.  # noqa: E501
        :type: bool
        """

        self._multi_user_edit = multi_user_edit

    @property
    def operating_cost(self) -> 'str':
        """Gets the operating_cost of this CloudspacesIdBody.  # noqa: E501


        :return: The operating_cost of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._operating_cost

    @operating_cost.setter
    def operating_cost(self, operating_cost: 'str'):
        """Sets the operating_cost of this CloudspacesIdBody.


        :param operating_cost: The operating_cost of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._operating_cost = operating_cost

    @property
    def paper_authors(self) -> 'str':
        """Gets the paper_authors of this CloudspacesIdBody.  # noqa: E501


        :return: The paper_authors of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._paper_authors

    @paper_authors.setter
    def paper_authors(self, paper_authors: 'str'):
        """Sets the paper_authors of this CloudspacesIdBody.


        :param paper_authors: The paper_authors of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._paper_authors = paper_authors

    @property
    def paper_org(self) -> 'str':
        """Gets the paper_org of this CloudspacesIdBody.  # noqa: E501


        :return: The paper_org of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._paper_org

    @paper_org.setter
    def paper_org(self, paper_org: 'str'):
        """Sets the paper_org of this CloudspacesIdBody.


        :param paper_org: The paper_org of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._paper_org = paper_org

    @property
    def paper_org_avatar_url(self) -> 'str':
        """Gets the paper_org_avatar_url of this CloudspacesIdBody.  # noqa: E501


        :return: The paper_org_avatar_url of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._paper_org_avatar_url

    @paper_org_avatar_url.setter
    def paper_org_avatar_url(self, paper_org_avatar_url: 'str'):
        """Sets the paper_org_avatar_url of this CloudspacesIdBody.


        :param paper_org_avatar_url: The paper_org_avatar_url of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._paper_org_avatar_url = paper_org_avatar_url

    @property
    def paper_url(self) -> 'str':
        """Gets the paper_url of this CloudspacesIdBody.  # noqa: E501


        :return: The paper_url of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._paper_url

    @paper_url.setter
    def paper_url(self, paper_url: 'str'):
        """Sets the paper_url of this CloudspacesIdBody.


        :param paper_url: The paper_url of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._paper_url = paper_url

    @property
    def publish_with_compute_name(self) -> 'str':
        """Gets the publish_with_compute_name of this CloudspacesIdBody.  # noqa: E501


        :return: The publish_with_compute_name of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._publish_with_compute_name

    @publish_with_compute_name.setter
    def publish_with_compute_name(self, publish_with_compute_name: 'str'):
        """Sets the publish_with_compute_name of this CloudspacesIdBody.


        :param publish_with_compute_name: The publish_with_compute_name of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._publish_with_compute_name = publish_with_compute_name

    @property
    def tags(self) -> 'list[V1CloudSpaceTag]':
        """Gets the tags of this CloudspacesIdBody.  # noqa: E501


        :return: The tags of this CloudspacesIdBody.  # noqa: E501
        :rtype: list[V1CloudSpaceTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: 'list[V1CloudSpaceTag]'):
        """Sets the tags of this CloudspacesIdBody.


        :param tags: The tags of this CloudspacesIdBody.  # noqa: E501
        :type: list[V1CloudSpaceTag]
        """

        self._tags = tags

    @property
    def thumbnail(self) -> 'str':
        """Gets the thumbnail of this CloudspacesIdBody.  # noqa: E501


        :return: The thumbnail of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail: 'str'):
        """Sets the thumbnail of this CloudspacesIdBody.


        :param thumbnail: The thumbnail of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def thumbnail_file_type(self) -> 'str':
        """Gets the thumbnail_file_type of this CloudspacesIdBody.  # noqa: E501


        :return: The thumbnail_file_type of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_file_type

    @thumbnail_file_type.setter
    def thumbnail_file_type(self, thumbnail_file_type: 'str'):
        """Sets the thumbnail_file_type of this CloudspacesIdBody.


        :param thumbnail_file_type: The thumbnail_file_type of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._thumbnail_file_type = thumbnail_file_type

    @property
    def user_metadata(self) -> 'str':
        """Gets the user_metadata of this CloudspacesIdBody.  # noqa: E501


        :return: The user_metadata of this CloudspacesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata: 'str'):
        """Sets the user_metadata of this CloudspacesIdBody.


        :param user_metadata: The user_metadata of this CloudspacesIdBody.  # noqa: E501
        :type: str
        """

        self._user_metadata = user_metadata

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
        if issubclass(CloudspacesIdBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'CloudspacesIdBody') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudspacesIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CloudspacesIdBody') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
