# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DecoratedBuild(object):
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
    """
    openapi_types = {
        'application_template_id': 'str',
        'config_json': 'AppConfigConfigSchema',
        'containerfile': 'str',
        'docker_image_name': 'str',
        'registry_login_secret': 'str',
        'ray_version': 'str',
        'id': 'str',
        'application_template': 'AppConfig',
        'revision': 'int',
        'creator_id': 'str',
        'error_message': 'str',
        'status': 'BuildStatus',
        'created_at': 'datetime',
        'last_modified_at': 'datetime',
        'deleted_at': 'datetime',
        'is_byod': 'bool',
        'cloud_id': 'str',
        'digest': 'str',
        'creator': 'MiniUser',
        'byod_ray_version': 'str'
    }

    attribute_map = {
        'application_template_id': 'application_template_id',
        'config_json': 'config_json',
        'containerfile': 'containerfile',
        'docker_image_name': 'docker_image_name',
        'registry_login_secret': 'registry_login_secret',
        'ray_version': 'ray_version',
        'id': 'id',
        'application_template': 'application_template',
        'revision': 'revision',
        'creator_id': 'creator_id',
        'error_message': 'error_message',
        'status': 'status',
        'created_at': 'created_at',
        'last_modified_at': 'last_modified_at',
        'deleted_at': 'deleted_at',
        'is_byod': 'is_byod',
        'cloud_id': 'cloud_id',
        'digest': 'digest',
        'creator': 'creator',
        'byod_ray_version': 'byod_ray_version'
    }

    def __init__(self, application_template_id=None, config_json=None, containerfile=None, docker_image_name=None, registry_login_secret=None, ray_version=None, id=None, application_template=None, revision=None, creator_id=None, error_message=None, status=None, created_at=None, last_modified_at=None, deleted_at=None, is_byod=None, cloud_id=None, digest=None, creator=None, byod_ray_version=None, local_vars_configuration=None):  # noqa: E501
        """DecoratedBuild - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_template_id = None
        self._config_json = None
        self._containerfile = None
        self._docker_image_name = None
        self._registry_login_secret = None
        self._ray_version = None
        self._id = None
        self._application_template = None
        self._revision = None
        self._creator_id = None
        self._error_message = None
        self._status = None
        self._created_at = None
        self._last_modified_at = None
        self._deleted_at = None
        self._is_byod = None
        self._cloud_id = None
        self._digest = None
        self._creator = None
        self._byod_ray_version = None
        self.discriminator = None

        self.application_template_id = application_template_id
        if config_json is not None:
            self.config_json = config_json
        if containerfile is not None:
            self.containerfile = containerfile
        if docker_image_name is not None:
            self.docker_image_name = docker_image_name
        if registry_login_secret is not None:
            self.registry_login_secret = registry_login_secret
        if ray_version is not None:
            self.ray_version = ray_version
        self.id = id
        self.application_template = application_template
        self.revision = revision
        self.creator_id = creator_id
        if error_message is not None:
            self.error_message = error_message
        self.status = status
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        self.is_byod = is_byod
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if digest is not None:
            self.digest = digest
        self.creator = creator
        if byod_ray_version is not None:
            self.byod_ray_version = byod_ray_version

    @property
    def application_template_id(self):
        """Gets the application_template_id of this DecoratedBuild.  # noqa: E501

        ID of the App Config this Build belongs to.  # noqa: E501

        :return: The application_template_id of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._application_template_id

    @application_template_id.setter
    def application_template_id(self, application_template_id):
        """Sets the application_template_id of this DecoratedBuild.

        ID of the App Config this Build belongs to.  # noqa: E501

        :param application_template_id: The application_template_id of this DecoratedBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_template_id`, must not be `None`")  # noqa: E501

        self._application_template_id = application_template_id

    @property
    def config_json(self):
        """Gets the config_json of this DecoratedBuild.  # noqa: E501

        Config JSON used to create this Build.  # noqa: E501

        :return: The config_json of this DecoratedBuild.  # noqa: E501
        :rtype: AppConfigConfigSchema
        """
        return self._config_json

    @config_json.setter
    def config_json(self, config_json):
        """Sets the config_json of this DecoratedBuild.

        Config JSON used to create this Build.  # noqa: E501

        :param config_json: The config_json of this DecoratedBuild.  # noqa: E501
        :type: AppConfigConfigSchema
        """

        self._config_json = config_json

    @property
    def containerfile(self):
        """Gets the containerfile of this DecoratedBuild.  # noqa: E501

        The containerfile used to build the image.  # noqa: E501

        :return: The containerfile of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._containerfile

    @containerfile.setter
    def containerfile(self, containerfile):
        """Sets the containerfile of this DecoratedBuild.

        The containerfile used to build the image.  # noqa: E501

        :param containerfile: The containerfile of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._containerfile = containerfile

    @property
    def docker_image_name(self):
        """Gets the docker_image_name of this DecoratedBuild.  # noqa: E501

        The name of the docker image for this build.  # noqa: E501

        :return: The docker_image_name of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._docker_image_name

    @docker_image_name.setter
    def docker_image_name(self, docker_image_name):
        """Sets the docker_image_name of this DecoratedBuild.

        The name of the docker image for this build.  # noqa: E501

        :param docker_image_name: The docker_image_name of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._docker_image_name = docker_image_name

    @property
    def registry_login_secret(self):
        """Gets the registry_login_secret of this DecoratedBuild.  # noqa: E501

        The name or identifier of a secret containing credentials to authenticate to the docker registry hosting the image.  # noqa: E501

        :return: The registry_login_secret of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._registry_login_secret

    @registry_login_secret.setter
    def registry_login_secret(self, registry_login_secret):
        """Sets the registry_login_secret of this DecoratedBuild.

        The name or identifier of a secret containing credentials to authenticate to the docker registry hosting the image.  # noqa: E501

        :param registry_login_secret: The registry_login_secret of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._registry_login_secret = registry_login_secret

    @property
    def ray_version(self):
        """Gets the ray_version of this DecoratedBuild.  # noqa: E501

        The Ray version to use for this build.  # noqa: E501

        :return: The ray_version of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._ray_version

    @ray_version.setter
    def ray_version(self, ray_version):
        """Sets the ray_version of this DecoratedBuild.

        The Ray version to use for this build.  # noqa: E501

        :param ray_version: The ray_version of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._ray_version = ray_version

    @property
    def id(self):
        """Gets the id of this DecoratedBuild.  # noqa: E501

        Server assigned unique identifier.  # noqa: E501

        :return: The id of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DecoratedBuild.

        Server assigned unique identifier.  # noqa: E501

        :param id: The id of this DecoratedBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def application_template(self):
        """Gets the application_template of this DecoratedBuild.  # noqa: E501

        App Config this Build belongs to.  # noqa: E501

        :return: The application_template of this DecoratedBuild.  # noqa: E501
        :rtype: AppConfig
        """
        return self._application_template

    @application_template.setter
    def application_template(self, application_template):
        """Sets the application_template of this DecoratedBuild.

        App Config this Build belongs to.  # noqa: E501

        :param application_template: The application_template of this DecoratedBuild.  # noqa: E501
        :type: AppConfig
        """
        if self.local_vars_configuration.client_side_validation and application_template is None:  # noqa: E501
            raise ValueError("Invalid value for `application_template`, must not be `None`")  # noqa: E501

        self._application_template = application_template

    @property
    def revision(self):
        """Gets the revision of this DecoratedBuild.  # noqa: E501

        Auto incrementing version number for this Build  # noqa: E501

        :return: The revision of this DecoratedBuild.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this DecoratedBuild.

        Auto incrementing version number for this Build  # noqa: E501

        :param revision: The revision of this DecoratedBuild.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def creator_id(self):
        """Gets the creator_id of this DecoratedBuild.  # noqa: E501

        ID of the user who created this Build.  # noqa: E501

        :return: The creator_id of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this DecoratedBuild.

        ID of the user who created this Build.  # noqa: E501

        :param creator_id: The creator_id of this DecoratedBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and creator_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def error_message(self):
        """Gets the error_message of this DecoratedBuild.  # noqa: E501

        Detailed error message. This will only be populated if the Build operation failed.  # noqa: E501

        :return: The error_message of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DecoratedBuild.

        Detailed error message. This will only be populated if the Build operation failed.  # noqa: E501

        :param error_message: The error_message of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def status(self):
        """Gets the status of this DecoratedBuild.  # noqa: E501

             Status of the Build.      `pending` - Build operation is queued and has not started yet.     `in_progress` - Build operation is in progress.     `succeeded` - Build operation completed successfully.     `failed` - Build operation completed unsuccessfully.     `pending_cancellation` - Build operation is marked for cancellation.     `cancelled` - Build operation was cancelled before it completed.       # noqa: E501

        :return: The status of this DecoratedBuild.  # noqa: E501
        :rtype: BuildStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DecoratedBuild.

             Status of the Build.      `pending` - Build operation is queued and has not started yet.     `in_progress` - Build operation is in progress.     `succeeded` - Build operation completed successfully.     `failed` - Build operation completed unsuccessfully.     `pending_cancellation` - Build operation is marked for cancellation.     `cancelled` - Build operation was cancelled before it completed.       # noqa: E501

        :param status: The status of this DecoratedBuild.  # noqa: E501
        :type: BuildStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this DecoratedBuild.  # noqa: E501

        Timestamp of when this Build was created.  # noqa: E501

        :return: The created_at of this DecoratedBuild.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DecoratedBuild.

        Timestamp of when this Build was created.  # noqa: E501

        :param created_at: The created_at of this DecoratedBuild.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this DecoratedBuild.  # noqa: E501

        Timestamp of when this Build was last updated.  # noqa: E501

        :return: The last_modified_at of this DecoratedBuild.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this DecoratedBuild.

        Timestamp of when this Build was last updated.  # noqa: E501

        :param last_modified_at: The last_modified_at of this DecoratedBuild.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this DecoratedBuild.  # noqa: E501

        Timestamp of when this Build was deleted.  # noqa: E501

        :return: The deleted_at of this DecoratedBuild.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this DecoratedBuild.

        Timestamp of when this Build was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this DecoratedBuild.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def is_byod(self):
        """Gets the is_byod of this DecoratedBuild.  # noqa: E501

        True if the image URI used in this build was user-specified.  # noqa: E501

        :return: The is_byod of this DecoratedBuild.  # noqa: E501
        :rtype: bool
        """
        return self._is_byod

    @is_byod.setter
    def is_byod(self, is_byod):
        """Sets the is_byod of this DecoratedBuild.

        True if the image URI used in this build was user-specified.  # noqa: E501

        :param is_byod: The is_byod of this DecoratedBuild.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_byod is None:  # noqa: E501
            raise ValueError("Invalid value for `is_byod`, must not be `None`")  # noqa: E501

        self._is_byod = is_byod

    @property
    def cloud_id(self):
        """Gets the cloud_id of this DecoratedBuild.  # noqa: E501

        The build cloud associated with this build. If None, the build is a v1 build.  # noqa: E501

        :return: The cloud_id of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this DecoratedBuild.

        The build cloud associated with this build. If None, the build is a v1 build.  # noqa: E501

        :param cloud_id: The cloud_id of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._cloud_id = cloud_id

    @property
    def digest(self):
        """Gets the digest of this DecoratedBuild.  # noqa: E501

        The digest of the image created by this build.  # noqa: E501

        :return: The digest of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this DecoratedBuild.

        The digest of the image created by this build.  # noqa: E501

        :param digest: The digest of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def creator(self):
        """Gets the creator of this DecoratedBuild.  # noqa: E501

        Read-only field. Information about the creator.  # noqa: E501

        :return: The creator of this DecoratedBuild.  # noqa: E501
        :rtype: MiniUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DecoratedBuild.

        Read-only field. Information about the creator.  # noqa: E501

        :param creator: The creator of this DecoratedBuild.  # noqa: E501
        :type: MiniUser
        """
        if self.local_vars_configuration.client_side_validation and creator is None:  # noqa: E501
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def byod_ray_version(self):
        """Gets the byod_ray_version of this DecoratedBuild.  # noqa: E501

        Read-only field. If this is a BYOD build, contains the user specified Ray version.  # noqa: E501

        :return: The byod_ray_version of this DecoratedBuild.  # noqa: E501
        :rtype: str
        """
        return self._byod_ray_version

    @byod_ray_version.setter
    def byod_ray_version(self, byod_ray_version):
        """Sets the byod_ray_version of this DecoratedBuild.

        Read-only field. If this is a BYOD build, contains the user specified Ray version.  # noqa: E501

        :param byod_ray_version: The byod_ray_version of this DecoratedBuild.  # noqa: E501
        :type: str
        """

        self._byod_ray_version = byod_ray_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DecoratedBuild):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecoratedBuild):
            return True

        return self.to_dict() != other.to_dict()
