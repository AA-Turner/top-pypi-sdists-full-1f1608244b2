# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .storage_mount_configuration_details import StorageMountConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileStorageMountConfigurationDetails(StorageMountConfigurationDetails):
    """
    The File Storage Mount Configuration Details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FileStorageMountConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.FileStorageMountConfigurationDetails.storage_type` attribute
        of this class is ``FILE_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_type:
            The value to assign to the storage_type property of this FileStorageMountConfigurationDetails.
            Allowed values for this property are: "FILE_STORAGE", "OBJECT_STORAGE"
        :type storage_type: str

        :param destination_directory_name:
            The value to assign to the destination_directory_name property of this FileStorageMountConfigurationDetails.
        :type destination_directory_name: str

        :param destination_path:
            The value to assign to the destination_path property of this FileStorageMountConfigurationDetails.
        :type destination_path: str

        :param mount_target_id:
            The value to assign to the mount_target_id property of this FileStorageMountConfigurationDetails.
        :type mount_target_id: str

        :param export_id:
            The value to assign to the export_id property of this FileStorageMountConfigurationDetails.
        :type export_id: str

        """
        self.swagger_types = {
            'storage_type': 'str',
            'destination_directory_name': 'str',
            'destination_path': 'str',
            'mount_target_id': 'str',
            'export_id': 'str'
        }
        self.attribute_map = {
            'storage_type': 'storageType',
            'destination_directory_name': 'destinationDirectoryName',
            'destination_path': 'destinationPath',
            'mount_target_id': 'mountTargetId',
            'export_id': 'exportId'
        }
        self._storage_type = None
        self._destination_directory_name = None
        self._destination_path = None
        self._mount_target_id = None
        self._export_id = None
        self._storage_type = 'FILE_STORAGE'

    @property
    def mount_target_id(self):
        """
        **[Required]** Gets the mount_target_id of this FileStorageMountConfigurationDetails.
        OCID of the mount target


        :return: The mount_target_id of this FileStorageMountConfigurationDetails.
        :rtype: str
        """
        return self._mount_target_id

    @mount_target_id.setter
    def mount_target_id(self, mount_target_id):
        """
        Sets the mount_target_id of this FileStorageMountConfigurationDetails.
        OCID of the mount target


        :param mount_target_id: The mount_target_id of this FileStorageMountConfigurationDetails.
        :type: str
        """
        self._mount_target_id = mount_target_id

    @property
    def export_id(self):
        """
        **[Required]** Gets the export_id of this FileStorageMountConfigurationDetails.
        OCID of the export


        :return: The export_id of this FileStorageMountConfigurationDetails.
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """
        Sets the export_id of this FileStorageMountConfigurationDetails.
        OCID of the export


        :param export_id: The export_id of this FileStorageMountConfigurationDetails.
        :type: str
        """
        self._export_id = export_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
