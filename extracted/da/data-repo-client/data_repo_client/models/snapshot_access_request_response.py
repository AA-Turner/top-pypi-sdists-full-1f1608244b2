# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class SnapshotAccessRequestResponse(object):
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
        'id': 'str',
        'dataset_id': 'str',
        'source_snapshot_id': 'str',
        'snapshot_name': 'str',
        'snapshot_research_purpose': 'str',
        'snapshot_specification': 'SnapshotBuilderRequest',
        'created_by': 'str',
        'status': 'SnapshotAccessRequestStatus',
        'created_date': 'str',
        'status_updated_date': 'str',
        'flightid': 'str',
        'created_snapshot_id': 'str',
        'summary': 'str',
        'auth_group_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'dataset_id': 'datasetId',
        'source_snapshot_id': 'sourceSnapshotId',
        'snapshot_name': 'snapshotName',
        'snapshot_research_purpose': 'snapshotResearchPurpose',
        'snapshot_specification': 'snapshotSpecification',
        'created_by': 'createdBy',
        'status': 'status',
        'created_date': 'createdDate',
        'status_updated_date': 'statusUpdatedDate',
        'flightid': 'flightid',
        'created_snapshot_id': 'createdSnapshotId',
        'summary': 'summary',
        'auth_group_name': 'authGroupName'
    }

    def __init__(self, id=None, dataset_id=None, source_snapshot_id=None, snapshot_name=None, snapshot_research_purpose=None, snapshot_specification=None, created_by=None, status=None, created_date=None, status_updated_date=None, flightid=None, created_snapshot_id=None, summary=None, auth_group_name=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotAccessRequestResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._dataset_id = None
        self._source_snapshot_id = None
        self._snapshot_name = None
        self._snapshot_research_purpose = None
        self._snapshot_specification = None
        self._created_by = None
        self._status = None
        self._created_date = None
        self._status_updated_date = None
        self._flightid = None
        self._created_snapshot_id = None
        self._summary = None
        self._auth_group_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if source_snapshot_id is not None:
            self.source_snapshot_id = source_snapshot_id
        if snapshot_name is not None:
            self.snapshot_name = snapshot_name
        if snapshot_research_purpose is not None:
            self.snapshot_research_purpose = snapshot_research_purpose
        if snapshot_specification is not None:
            self.snapshot_specification = snapshot_specification
        if created_by is not None:
            self.created_by = created_by
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        if status_updated_date is not None:
            self.status_updated_date = status_updated_date
        if flightid is not None:
            self.flightid = flightid
        if created_snapshot_id is not None:
            self.created_snapshot_id = created_snapshot_id
        if summary is not None:
            self.summary = summary
        if auth_group_name is not None:
            self.auth_group_name = auth_group_name

    @property
    def id(self):
        """Gets the id of this SnapshotAccessRequestResponse.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The id of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotAccessRequestResponse.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param id: The id of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this SnapshotAccessRequestResponse.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The dataset_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this SnapshotAccessRequestResponse.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param dataset_id: The dataset_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def source_snapshot_id(self):
        """Gets the source_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The source_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_snapshot_id

    @source_snapshot_id.setter
    def source_snapshot_id(self, source_snapshot_id):
        """Sets the source_snapshot_id of this SnapshotAccessRequestResponse.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param source_snapshot_id: The source_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._source_snapshot_id = source_snapshot_id

    @property
    def snapshot_name(self):
        """Gets the snapshot_name of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The snapshot_name of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """Sets the snapshot_name of this SnapshotAccessRequestResponse.


        :param snapshot_name: The snapshot_name of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._snapshot_name = snapshot_name

    @property
    def snapshot_research_purpose(self):
        """Gets the snapshot_research_purpose of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The snapshot_research_purpose of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_research_purpose

    @snapshot_research_purpose.setter
    def snapshot_research_purpose(self, snapshot_research_purpose):
        """Sets the snapshot_research_purpose of this SnapshotAccessRequestResponse.


        :param snapshot_research_purpose: The snapshot_research_purpose of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._snapshot_research_purpose = snapshot_research_purpose

    @property
    def snapshot_specification(self):
        """Gets the snapshot_specification of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The snapshot_specification of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: SnapshotBuilderRequest
        """
        return self._snapshot_specification

    @snapshot_specification.setter
    def snapshot_specification(self, snapshot_specification):
        """Sets the snapshot_specification of this SnapshotAccessRequestResponse.


        :param snapshot_specification: The snapshot_specification of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: SnapshotBuilderRequest
        """

        self._snapshot_specification = snapshot_specification

    @property
    def created_by(self):
        """Gets the created_by of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The created_by of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SnapshotAccessRequestResponse.


        :param created_by: The created_by of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def status(self):
        """Gets the status of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The status of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: SnapshotAccessRequestStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotAccessRequestResponse.


        :param status: The status of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: SnapshotAccessRequestStatus
        """

        self._status = status

    @property
    def created_date(self):
        """Gets the created_date of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The created_date of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SnapshotAccessRequestResponse.


        :param created_date: The created_date of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def status_updated_date(self):
        """Gets the status_updated_date of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The status_updated_date of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_updated_date

    @status_updated_date.setter
    def status_updated_date(self, status_updated_date):
        """Sets the status_updated_date of this SnapshotAccessRequestResponse.


        :param status_updated_date: The status_updated_date of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._status_updated_date = status_updated_date

    @property
    def flightid(self):
        """Gets the flightid of this SnapshotAccessRequestResponse.  # noqa: E501

        Unique identifier for flights, jobs, etc.   # noqa: E501

        :return: The flightid of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._flightid

    @flightid.setter
    def flightid(self, flightid):
        """Sets the flightid of this SnapshotAccessRequestResponse.

        Unique identifier for flights, jobs, etc.   # noqa: E501

        :param flightid: The flightid of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                flightid is not None and not re.search(r'[A-Za-z0-9_\\-]{22}', flightid)):  # noqa: E501
            raise ValueError(r"Invalid value for `flightid`, must be a follow pattern or equal to `/[A-Za-z0-9_\\-]{22}/`")  # noqa: E501

        self._flightid = flightid

    @property
    def created_snapshot_id(self):
        """Gets the created_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The created_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_snapshot_id

    @created_snapshot_id.setter
    def created_snapshot_id(self, created_snapshot_id):
        """Sets the created_snapshot_id of this SnapshotAccessRequestResponse.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param created_snapshot_id: The created_snapshot_id of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._created_snapshot_id = created_snapshot_id

    @property
    def summary(self):
        """Gets the summary of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The summary of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this SnapshotAccessRequestResponse.


        :param summary: The summary of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def auth_group_name(self):
        """Gets the auth_group_name of this SnapshotAccessRequestResponse.  # noqa: E501


        :return: The auth_group_name of this SnapshotAccessRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth_group_name

    @auth_group_name.setter
    def auth_group_name(self, auth_group_name):
        """Sets the auth_group_name of this SnapshotAccessRequestResponse.


        :param auth_group_name: The auth_group_name of this SnapshotAccessRequestResponse.  # noqa: E501
        :type: str
        """

        self._auth_group_name = auth_group_name

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
        if not isinstance(other, SnapshotAccessRequestResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotAccessRequestResponse):
            return True

        return self.to_dict() != other.to_dict()
