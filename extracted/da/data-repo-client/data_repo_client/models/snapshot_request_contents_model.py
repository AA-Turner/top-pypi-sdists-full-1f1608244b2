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


class SnapshotRequestContentsModel(object):
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
        'dataset_name': 'str',
        'mode': 'str',
        'asset_spec': 'SnapshotRequestAssetModel',
        'query_spec': 'SnapshotRequestQueryModel',
        'row_id_spec': 'SnapshotRequestRowIdModel',
        'request_id_spec': 'SnapshotRequestIdModel'
    }

    attribute_map = {
        'dataset_name': 'datasetName',
        'mode': 'mode',
        'asset_spec': 'assetSpec',
        'query_spec': 'querySpec',
        'row_id_spec': 'rowIdSpec',
        'request_id_spec': 'requestIdSpec'
    }

    def __init__(self, dataset_name=None, mode=None, asset_spec=None, query_spec=None, row_id_spec=None, request_id_spec=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotRequestContentsModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dataset_name = None
        self._mode = None
        self._asset_spec = None
        self._query_spec = None
        self._row_id_spec = None
        self._request_id_spec = None
        self.discriminator = None

        self.dataset_name = dataset_name
        self.mode = mode
        if asset_spec is not None:
            self.asset_spec = asset_spec
        if query_spec is not None:
            self.query_spec = query_spec
        if row_id_spec is not None:
            self.row_id_spec = row_id_spec
        if request_id_spec is not None:
            self.request_id_spec = request_id_spec

    @property
    def dataset_name(self):
        """Gets the dataset_name of this SnapshotRequestContentsModel.  # noqa: E501

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :return: The dataset_name of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this SnapshotRequestContentsModel.

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :param dataset_name: The dataset_name of this SnapshotRequestContentsModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dataset_name is None:  # noqa: E501
            raise ValueError("Invalid value for `dataset_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dataset_name is not None and len(dataset_name) > 511):
            raise ValueError("Invalid value for `dataset_name`, length must be less than or equal to `511`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dataset_name is not None and len(dataset_name) < 1):
            raise ValueError("Invalid value for `dataset_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dataset_name is not None and not re.search(r'^[a-zA-Z0-9][_a-zA-Z0-9]*$', dataset_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `dataset_name`, must be a follow pattern or equal to `/^[a-zA-Z0-9][_a-zA-Z0-9]*$/`")  # noqa: E501

        self._dataset_name = dataset_name

    @property
    def mode(self):
        """Gets the mode of this SnapshotRequestContentsModel.  # noqa: E501


        :return: The mode of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SnapshotRequestContentsModel.


        :param mode: The mode of this SnapshotRequestContentsModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["byAsset", "byFullView", "byQuery", "byRowId", "byRequestId"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def asset_spec(self):
        """Gets the asset_spec of this SnapshotRequestContentsModel.  # noqa: E501


        :return: The asset_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: SnapshotRequestAssetModel
        """
        return self._asset_spec

    @asset_spec.setter
    def asset_spec(self, asset_spec):
        """Sets the asset_spec of this SnapshotRequestContentsModel.


        :param asset_spec: The asset_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :type: SnapshotRequestAssetModel
        """

        self._asset_spec = asset_spec

    @property
    def query_spec(self):
        """Gets the query_spec of this SnapshotRequestContentsModel.  # noqa: E501


        :return: The query_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: SnapshotRequestQueryModel
        """
        return self._query_spec

    @query_spec.setter
    def query_spec(self, query_spec):
        """Sets the query_spec of this SnapshotRequestContentsModel.


        :param query_spec: The query_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :type: SnapshotRequestQueryModel
        """

        self._query_spec = query_spec

    @property
    def row_id_spec(self):
        """Gets the row_id_spec of this SnapshotRequestContentsModel.  # noqa: E501


        :return: The row_id_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: SnapshotRequestRowIdModel
        """
        return self._row_id_spec

    @row_id_spec.setter
    def row_id_spec(self, row_id_spec):
        """Sets the row_id_spec of this SnapshotRequestContentsModel.


        :param row_id_spec: The row_id_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :type: SnapshotRequestRowIdModel
        """

        self._row_id_spec = row_id_spec

    @property
    def request_id_spec(self):
        """Gets the request_id_spec of this SnapshotRequestContentsModel.  # noqa: E501


        :return: The request_id_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :rtype: SnapshotRequestIdModel
        """
        return self._request_id_spec

    @request_id_spec.setter
    def request_id_spec(self, request_id_spec):
        """Sets the request_id_spec of this SnapshotRequestContentsModel.


        :param request_id_spec: The request_id_spec of this SnapshotRequestContentsModel.  # noqa: E501
        :type: SnapshotRequestIdModel
        """

        self._request_id_spec = request_id_spec

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
        if not isinstance(other, SnapshotRequestContentsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotRequestContentsModel):
            return True

        return self.to_dict() != other.to_dict()
