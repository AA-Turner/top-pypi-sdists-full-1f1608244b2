# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails(object):
    """
    The details for creating the operations performed on a block volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachments:
            The value to assign to the attachments property of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :type attachments: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeAttachOperationDetails]

        :param mounts:
            The value to assign to the mounts property of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :type mounts: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeMountOperationDetails]

        """
        self.swagger_types = {
            'attachments': 'list[CreateComputeInstanceNonMovableBlockVolumeAttachOperationDetails]',
            'mounts': 'list[CreateComputeInstanceNonMovableBlockVolumeMountOperationDetails]'
        }
        self.attribute_map = {
            'attachments': 'attachments',
            'mounts': 'mounts'
        }
        self._attachments = None
        self._mounts = None

    @property
    def attachments(self):
        """
        Gets the attachments of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        A list of details of attach or detach operations performed on block volumes.


        :return: The attachments of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :rtype: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeAttachOperationDetails]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        A list of details of attach or detach operations performed on block volumes.


        :param attachments: The attachments of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :type: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeAttachOperationDetails]
        """
        self._attachments = attachments

    @property
    def mounts(self):
        """
        Gets the mounts of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        A list of details of mount operations performed on block volumes.


        :return: The mounts of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :rtype: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeMountOperationDetails]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """
        Sets the mounts of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        A list of details of mount operations performed on block volumes.


        :param mounts: The mounts of this CreateComputeInstanceNonMovableBlockVolumeAttachAndMountOperationsDetails.
        :type: list[oci.disaster_recovery.models.CreateComputeInstanceNonMovableBlockVolumeMountOperationDetails]
        """
        self._mounts = mounts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
