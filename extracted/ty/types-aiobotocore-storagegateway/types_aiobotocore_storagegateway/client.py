"""
Type annotations for storagegateway service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_storagegateway.client import StorageGatewayClient

    session = get_session()
    async with session.create_client("storagegateway") as client:
        client: StorageGatewayClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListCacheReportsPaginator,
    ListFileSharesPaginator,
    ListFileSystemAssociationsPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapePoolsPaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)
from .type_defs import (
    ActivateGatewayInputTypeDef,
    ActivateGatewayOutputTypeDef,
    AddCacheInputTypeDef,
    AddCacheOutputTypeDef,
    AddTagsToResourceInputTypeDef,
    AddTagsToResourceOutputTypeDef,
    AddUploadBufferInputTypeDef,
    AddUploadBufferOutputTypeDef,
    AddWorkingStorageInputTypeDef,
    AddWorkingStorageOutputTypeDef,
    AssignTapePoolInputTypeDef,
    AssignTapePoolOutputTypeDef,
    AssociateFileSystemInputTypeDef,
    AssociateFileSystemOutputTypeDef,
    AttachVolumeInputTypeDef,
    AttachVolumeOutputTypeDef,
    CancelArchivalInputTypeDef,
    CancelArchivalOutputTypeDef,
    CancelCacheReportInputTypeDef,
    CancelCacheReportOutputTypeDef,
    CancelRetrievalInputTypeDef,
    CancelRetrievalOutputTypeDef,
    CreateCachediSCSIVolumeInputTypeDef,
    CreateCachediSCSIVolumeOutputTypeDef,
    CreateNFSFileShareInputTypeDef,
    CreateNFSFileShareOutputTypeDef,
    CreateSMBFileShareInputTypeDef,
    CreateSMBFileShareOutputTypeDef,
    CreateSnapshotFromVolumeRecoveryPointInputTypeDef,
    CreateSnapshotFromVolumeRecoveryPointOutputTypeDef,
    CreateSnapshotInputTypeDef,
    CreateSnapshotOutputTypeDef,
    CreateStorediSCSIVolumeInputTypeDef,
    CreateStorediSCSIVolumeOutputTypeDef,
    CreateTapePoolInputTypeDef,
    CreateTapePoolOutputTypeDef,
    CreateTapesInputTypeDef,
    CreateTapesOutputTypeDef,
    CreateTapeWithBarcodeInputTypeDef,
    CreateTapeWithBarcodeOutputTypeDef,
    DeleteAutomaticTapeCreationPolicyInputTypeDef,
    DeleteAutomaticTapeCreationPolicyOutputTypeDef,
    DeleteBandwidthRateLimitInputTypeDef,
    DeleteBandwidthRateLimitOutputTypeDef,
    DeleteCacheReportInputTypeDef,
    DeleteCacheReportOutputTypeDef,
    DeleteChapCredentialsInputTypeDef,
    DeleteChapCredentialsOutputTypeDef,
    DeleteFileShareInputTypeDef,
    DeleteFileShareOutputTypeDef,
    DeleteGatewayInputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteSnapshotScheduleInputTypeDef,
    DeleteSnapshotScheduleOutputTypeDef,
    DeleteTapeArchiveInputTypeDef,
    DeleteTapeArchiveOutputTypeDef,
    DeleteTapeInputTypeDef,
    DeleteTapeOutputTypeDef,
    DeleteTapePoolInputTypeDef,
    DeleteTapePoolOutputTypeDef,
    DeleteVolumeInputTypeDef,
    DeleteVolumeOutputTypeDef,
    DescribeAvailabilityMonitorTestInputTypeDef,
    DescribeAvailabilityMonitorTestOutputTypeDef,
    DescribeBandwidthRateLimitInputTypeDef,
    DescribeBandwidthRateLimitOutputTypeDef,
    DescribeBandwidthRateLimitScheduleInputTypeDef,
    DescribeBandwidthRateLimitScheduleOutputTypeDef,
    DescribeCachediSCSIVolumesInputTypeDef,
    DescribeCachediSCSIVolumesOutputTypeDef,
    DescribeCacheInputTypeDef,
    DescribeCacheOutputTypeDef,
    DescribeCacheReportInputTypeDef,
    DescribeCacheReportOutputTypeDef,
    DescribeChapCredentialsInputTypeDef,
    DescribeChapCredentialsOutputTypeDef,
    DescribeFileSystemAssociationsInputTypeDef,
    DescribeFileSystemAssociationsOutputTypeDef,
    DescribeGatewayInformationInputTypeDef,
    DescribeGatewayInformationOutputTypeDef,
    DescribeMaintenanceStartTimeInputTypeDef,
    DescribeMaintenanceStartTimeOutputTypeDef,
    DescribeNFSFileSharesInputTypeDef,
    DescribeNFSFileSharesOutputTypeDef,
    DescribeSMBFileSharesInputTypeDef,
    DescribeSMBFileSharesOutputTypeDef,
    DescribeSMBSettingsInputTypeDef,
    DescribeSMBSettingsOutputTypeDef,
    DescribeSnapshotScheduleInputTypeDef,
    DescribeSnapshotScheduleOutputTypeDef,
    DescribeStorediSCSIVolumesInputTypeDef,
    DescribeStorediSCSIVolumesOutputTypeDef,
    DescribeTapeArchivesInputTypeDef,
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsInputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesInputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeUploadBufferInputTypeDef,
    DescribeUploadBufferOutputTypeDef,
    DescribeVTLDevicesInputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    DescribeWorkingStorageInputTypeDef,
    DescribeWorkingStorageOutputTypeDef,
    DetachVolumeInputTypeDef,
    DetachVolumeOutputTypeDef,
    DisableGatewayInputTypeDef,
    DisableGatewayOutputTypeDef,
    DisassociateFileSystemInputTypeDef,
    DisassociateFileSystemOutputTypeDef,
    EvictFilesFailingUploadInputTypeDef,
    EvictFilesFailingUploadOutputTypeDef,
    JoinDomainInputTypeDef,
    JoinDomainOutputTypeDef,
    ListAutomaticTapeCreationPoliciesInputTypeDef,
    ListAutomaticTapeCreationPoliciesOutputTypeDef,
    ListCacheReportsInputTypeDef,
    ListCacheReportsOutputTypeDef,
    ListFileSharesInputTypeDef,
    ListFileSharesOutputTypeDef,
    ListFileSystemAssociationsInputTypeDef,
    ListFileSystemAssociationsOutputTypeDef,
    ListGatewaysInputTypeDef,
    ListGatewaysOutputTypeDef,
    ListLocalDisksInputTypeDef,
    ListLocalDisksOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapePoolsInputTypeDef,
    ListTapePoolsOutputTypeDef,
    ListTapesInputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumeInitiatorsInputTypeDef,
    ListVolumeInitiatorsOutputTypeDef,
    ListVolumeRecoveryPointsInputTypeDef,
    ListVolumeRecoveryPointsOutputTypeDef,
    ListVolumesInputTypeDef,
    ListVolumesOutputTypeDef,
    NotifyWhenUploadedInputTypeDef,
    NotifyWhenUploadedOutputTypeDef,
    RefreshCacheInputTypeDef,
    RefreshCacheOutputTypeDef,
    RemoveTagsFromResourceInputTypeDef,
    RemoveTagsFromResourceOutputTypeDef,
    ResetCacheInputTypeDef,
    ResetCacheOutputTypeDef,
    RetrieveTapeArchiveInputTypeDef,
    RetrieveTapeArchiveOutputTypeDef,
    RetrieveTapeRecoveryPointInputTypeDef,
    RetrieveTapeRecoveryPointOutputTypeDef,
    SetLocalConsolePasswordInputTypeDef,
    SetLocalConsolePasswordOutputTypeDef,
    SetSMBGuestPasswordInputTypeDef,
    SetSMBGuestPasswordOutputTypeDef,
    ShutdownGatewayInputTypeDef,
    ShutdownGatewayOutputTypeDef,
    StartAvailabilityMonitorTestInputTypeDef,
    StartAvailabilityMonitorTestOutputTypeDef,
    StartCacheReportInputTypeDef,
    StartCacheReportOutputTypeDef,
    StartGatewayInputTypeDef,
    StartGatewayOutputTypeDef,
    UpdateAutomaticTapeCreationPolicyInputTypeDef,
    UpdateAutomaticTapeCreationPolicyOutputTypeDef,
    UpdateBandwidthRateLimitInputTypeDef,
    UpdateBandwidthRateLimitOutputTypeDef,
    UpdateBandwidthRateLimitScheduleInputTypeDef,
    UpdateBandwidthRateLimitScheduleOutputTypeDef,
    UpdateChapCredentialsInputTypeDef,
    UpdateChapCredentialsOutputTypeDef,
    UpdateFileSystemAssociationInputTypeDef,
    UpdateFileSystemAssociationOutputTypeDef,
    UpdateGatewayInformationInputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowInputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateMaintenanceStartTimeInputTypeDef,
    UpdateMaintenanceStartTimeOutputTypeDef,
    UpdateNFSFileShareInputTypeDef,
    UpdateNFSFileShareOutputTypeDef,
    UpdateSMBFileShareInputTypeDef,
    UpdateSMBFileShareOutputTypeDef,
    UpdateSMBFileShareVisibilityInputTypeDef,
    UpdateSMBFileShareVisibilityOutputTypeDef,
    UpdateSMBLocalGroupsInputTypeDef,
    UpdateSMBLocalGroupsOutputTypeDef,
    UpdateSMBSecurityStrategyInputTypeDef,
    UpdateSMBSecurityStrategyOutputTypeDef,
    UpdateSnapshotScheduleInputTypeDef,
    UpdateSnapshotScheduleOutputTypeDef,
    UpdateVTLDeviceTypeInputTypeDef,
    UpdateVTLDeviceTypeOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("StorageGatewayClient",)


class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidGatewayRequestException: Type[BotocoreClientError]
    ServiceUnavailableError: Type[BotocoreClientError]


class StorageGatewayClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        StorageGatewayClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#generate_presigned_url)
        """

    async def activate_gateway(
        self, **kwargs: Unpack[ActivateGatewayInputTypeDef]
    ) -> ActivateGatewayOutputTypeDef:
        """
        Activates the gateway you previously deployed on your host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/activate_gateway.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#activate_gateway)
        """

    async def add_cache(self, **kwargs: Unpack[AddCacheInputTypeDef]) -> AddCacheOutputTypeDef:
        """
        Configures one or more gateway local disks as cache for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/add_cache.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#add_cache)
        """

    async def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceInputTypeDef]
    ) -> AddTagsToResourceOutputTypeDef:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/add_tags_to_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#add_tags_to_resource)
        """

    async def add_upload_buffer(
        self, **kwargs: Unpack[AddUploadBufferInputTypeDef]
    ) -> AddUploadBufferOutputTypeDef:
        """
        Configures one or more gateway local disks as upload buffer for a specified
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/add_upload_buffer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#add_upload_buffer)
        """

    async def add_working_storage(
        self, **kwargs: Unpack[AddWorkingStorageInputTypeDef]
    ) -> AddWorkingStorageOutputTypeDef:
        """
        Configures one or more gateway local disks as working storage for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/add_working_storage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#add_working_storage)
        """

    async def assign_tape_pool(
        self, **kwargs: Unpack[AssignTapePoolInputTypeDef]
    ) -> AssignTapePoolOutputTypeDef:
        """
        Assigns a tape to a tape pool for archiving.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/assign_tape_pool.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#assign_tape_pool)
        """

    async def associate_file_system(
        self, **kwargs: Unpack[AssociateFileSystemInputTypeDef]
    ) -> AssociateFileSystemOutputTypeDef:
        """
        Associate an Amazon FSx file system with the FSx File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/associate_file_system.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#associate_file_system)
        """

    async def attach_volume(
        self, **kwargs: Unpack[AttachVolumeInputTypeDef]
    ) -> AttachVolumeOutputTypeDef:
        """
        Connects a volume to an iSCSI connection and then attaches the volume to the
        specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/attach_volume.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#attach_volume)
        """

    async def cancel_archival(
        self, **kwargs: Unpack[CancelArchivalInputTypeDef]
    ) -> CancelArchivalOutputTypeDef:
        """
        Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the
        archiving process is initiated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/cancel_archival.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#cancel_archival)
        """

    async def cancel_cache_report(
        self, **kwargs: Unpack[CancelCacheReportInputTypeDef]
    ) -> CancelCacheReportOutputTypeDef:
        """
        Cancels generation of a specified cache report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/cancel_cache_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#cancel_cache_report)
        """

    async def cancel_retrieval(
        self, **kwargs: Unpack[CancelRetrievalInputTypeDef]
    ) -> CancelRetrievalOutputTypeDef:
        """
        Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a
        gateway after the retrieval process is initiated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/cancel_retrieval.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#cancel_retrieval)
        """

    async def create_cached_iscsi_volume(
        self, **kwargs: Unpack[CreateCachediSCSIVolumeInputTypeDef]
    ) -> CreateCachediSCSIVolumeOutputTypeDef:
        """
        Creates a cached volume on a specified cached volume gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_cached_iscsi_volume.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_cached_iscsi_volume)
        """

    async def create_nfs_file_share(
        self, **kwargs: Unpack[CreateNFSFileShareInputTypeDef]
    ) -> CreateNFSFileShareOutputTypeDef:
        """
        Creates a Network File System (NFS) file share on an existing S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_nfs_file_share.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_nfs_file_share)
        """

    async def create_smb_file_share(
        self, **kwargs: Unpack[CreateSMBFileShareInputTypeDef]
    ) -> CreateSMBFileShareOutputTypeDef:
        """
        Creates a Server Message Block (SMB) file share on an existing S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_smb_file_share.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_smb_file_share)
        """

    async def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotInputTypeDef]
    ) -> CreateSnapshotOutputTypeDef:
        """
        Initiates a snapshot of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_snapshot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_snapshot)
        """

    async def create_snapshot_from_volume_recovery_point(
        self, **kwargs: Unpack[CreateSnapshotFromVolumeRecoveryPointInputTypeDef]
    ) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
        """
        Initiates a snapshot of a gateway from a volume recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_snapshot_from_volume_recovery_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_snapshot_from_volume_recovery_point)
        """

    async def create_stored_iscsi_volume(
        self, **kwargs: Unpack[CreateStorediSCSIVolumeInputTypeDef]
    ) -> CreateStorediSCSIVolumeOutputTypeDef:
        """
        Creates a volume on a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_stored_iscsi_volume.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_stored_iscsi_volume)
        """

    async def create_tape_pool(
        self, **kwargs: Unpack[CreateTapePoolInputTypeDef]
    ) -> CreateTapePoolOutputTypeDef:
        """
        Creates a new custom tape pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_tape_pool.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_tape_pool)
        """

    async def create_tape_with_barcode(
        self, **kwargs: Unpack[CreateTapeWithBarcodeInputTypeDef]
    ) -> CreateTapeWithBarcodeOutputTypeDef:
        """
        Creates a virtual tape by using your own barcode.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_tape_with_barcode.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_tape_with_barcode)
        """

    async def create_tapes(
        self, **kwargs: Unpack[CreateTapesInputTypeDef]
    ) -> CreateTapesOutputTypeDef:
        """
        Creates one or more virtual tapes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/create_tapes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#create_tapes)
        """

    async def delete_automatic_tape_creation_policy(
        self, **kwargs: Unpack[DeleteAutomaticTapeCreationPolicyInputTypeDef]
    ) -> DeleteAutomaticTapeCreationPolicyOutputTypeDef:
        """
        Deletes the automatic tape creation policy of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_automatic_tape_creation_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_automatic_tape_creation_policy)
        """

    async def delete_bandwidth_rate_limit(
        self, **kwargs: Unpack[DeleteBandwidthRateLimitInputTypeDef]
    ) -> DeleteBandwidthRateLimitOutputTypeDef:
        """
        Deletes the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_bandwidth_rate_limit.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_bandwidth_rate_limit)
        """

    async def delete_cache_report(
        self, **kwargs: Unpack[DeleteCacheReportInputTypeDef]
    ) -> DeleteCacheReportOutputTypeDef:
        """
        Deletes the specified cache report and any associated tags from the Storage
        Gateway database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_cache_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_cache_report)
        """

    async def delete_chap_credentials(
        self, **kwargs: Unpack[DeleteChapCredentialsInputTypeDef]
    ) -> DeleteChapCredentialsOutputTypeDef:
        """
        Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a
        specified iSCSI target and initiator pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_chap_credentials.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_chap_credentials)
        """

    async def delete_file_share(
        self, **kwargs: Unpack[DeleteFileShareInputTypeDef]
    ) -> DeleteFileShareOutputTypeDef:
        """
        Deletes a file share from an S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_file_share.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_file_share)
        """

    async def delete_gateway(
        self, **kwargs: Unpack[DeleteGatewayInputTypeDef]
    ) -> DeleteGatewayOutputTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_gateway.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_gateway)
        """

    async def delete_snapshot_schedule(
        self, **kwargs: Unpack[DeleteSnapshotScheduleInputTypeDef]
    ) -> DeleteSnapshotScheduleOutputTypeDef:
        """
        Deletes a snapshot of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_snapshot_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_snapshot_schedule)
        """

    async def delete_tape(
        self, **kwargs: Unpack[DeleteTapeInputTypeDef]
    ) -> DeleteTapeOutputTypeDef:
        """
        Deletes the specified virtual tape.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_tape.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_tape)
        """

    async def delete_tape_archive(
        self, **kwargs: Unpack[DeleteTapeArchiveInputTypeDef]
    ) -> DeleteTapeArchiveOutputTypeDef:
        """
        Deletes the specified virtual tape from the virtual tape shelf (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_tape_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_tape_archive)
        """

    async def delete_tape_pool(
        self, **kwargs: Unpack[DeleteTapePoolInputTypeDef]
    ) -> DeleteTapePoolOutputTypeDef:
        """
        Delete a custom tape pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_tape_pool.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_tape_pool)
        """

    async def delete_volume(
        self, **kwargs: Unpack[DeleteVolumeInputTypeDef]
    ) -> DeleteVolumeOutputTypeDef:
        """
        Deletes the specified storage volume that you previously created using the
        <a>CreateCachediSCSIVolume</a> or <a>CreateStorediSCSIVolume</a> API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/delete_volume.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#delete_volume)
        """

    async def describe_availability_monitor_test(
        self, **kwargs: Unpack[DescribeAvailabilityMonitorTestInputTypeDef]
    ) -> DescribeAvailabilityMonitorTestOutputTypeDef:
        """
        Returns information about the most recent high availability monitoring test
        that was performed on the host in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_availability_monitor_test.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_availability_monitor_test)
        """

    async def describe_bandwidth_rate_limit(
        self, **kwargs: Unpack[DescribeBandwidthRateLimitInputTypeDef]
    ) -> DescribeBandwidthRateLimitOutputTypeDef:
        """
        Returns the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_bandwidth_rate_limit.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_bandwidth_rate_limit)
        """

    async def describe_bandwidth_rate_limit_schedule(
        self, **kwargs: Unpack[DescribeBandwidthRateLimitScheduleInputTypeDef]
    ) -> DescribeBandwidthRateLimitScheduleOutputTypeDef:
        """
        Returns information about the bandwidth rate limit schedule of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_bandwidth_rate_limit_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_bandwidth_rate_limit_schedule)
        """

    async def describe_cache(
        self, **kwargs: Unpack[DescribeCacheInputTypeDef]
    ) -> DescribeCacheOutputTypeDef:
        """
        Returns information about the cache of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_cache.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_cache)
        """

    async def describe_cache_report(
        self, **kwargs: Unpack[DescribeCacheReportInputTypeDef]
    ) -> DescribeCacheReportOutputTypeDef:
        """
        Returns information about the specified cache report, including completion
        status and generation progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_cache_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_cache_report)
        """

    async def describe_cached_iscsi_volumes(
        self, **kwargs: Unpack[DescribeCachediSCSIVolumesInputTypeDef]
    ) -> DescribeCachediSCSIVolumesOutputTypeDef:
        """
        Returns a description of the gateway volumes specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_cached_iscsi_volumes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_cached_iscsi_volumes)
        """

    async def describe_chap_credentials(
        self, **kwargs: Unpack[DescribeChapCredentialsInputTypeDef]
    ) -> DescribeChapCredentialsOutputTypeDef:
        """
        Returns an array of Challenge-Handshake Authentication Protocol (CHAP)
        credentials information for a specified iSCSI target, one for each
        target-initiator pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_chap_credentials.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_chap_credentials)
        """

    async def describe_file_system_associations(
        self, **kwargs: Unpack[DescribeFileSystemAssociationsInputTypeDef]
    ) -> DescribeFileSystemAssociationsOutputTypeDef:
        """
        Gets the file system association information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_file_system_associations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_file_system_associations)
        """

    async def describe_gateway_information(
        self, **kwargs: Unpack[DescribeGatewayInformationInputTypeDef]
    ) -> DescribeGatewayInformationOutputTypeDef:
        """
        Returns metadata about a gateway such as its name, network interfaces, time
        zone, status, and software version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_gateway_information.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_gateway_information)
        """

    async def describe_maintenance_start_time(
        self, **kwargs: Unpack[DescribeMaintenanceStartTimeInputTypeDef]
    ) -> DescribeMaintenanceStartTimeOutputTypeDef:
        """
        Returns your gateway's maintenance window schedule information, with values for
        monthly or weekly cadence, specific day and time to begin maintenance, and
        which types of updates to apply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_maintenance_start_time.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_maintenance_start_time)
        """

    async def describe_nfs_file_shares(
        self, **kwargs: Unpack[DescribeNFSFileSharesInputTypeDef]
    ) -> DescribeNFSFileSharesOutputTypeDef:
        """
        Gets a description for one or more Network File System (NFS) file shares from
        an S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_nfs_file_shares.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_nfs_file_shares)
        """

    async def describe_smb_file_shares(
        self, **kwargs: Unpack[DescribeSMBFileSharesInputTypeDef]
    ) -> DescribeSMBFileSharesOutputTypeDef:
        """
        Gets a description for one or more Server Message Block (SMB) file shares from
        a S3 File Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_smb_file_shares.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_smb_file_shares)
        """

    async def describe_smb_settings(
        self, **kwargs: Unpack[DescribeSMBSettingsInputTypeDef]
    ) -> DescribeSMBSettingsOutputTypeDef:
        """
        Gets a description of a Server Message Block (SMB) file share settings from a
        file gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_smb_settings.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_smb_settings)
        """

    async def describe_snapshot_schedule(
        self, **kwargs: Unpack[DescribeSnapshotScheduleInputTypeDef]
    ) -> DescribeSnapshotScheduleOutputTypeDef:
        """
        Describes the snapshot schedule for the specified gateway volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_snapshot_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_snapshot_schedule)
        """

    async def describe_stored_iscsi_volumes(
        self, **kwargs: Unpack[DescribeStorediSCSIVolumesInputTypeDef]
    ) -> DescribeStorediSCSIVolumesOutputTypeDef:
        """
        Returns the description of the gateway volumes specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_stored_iscsi_volumes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_stored_iscsi_volumes)
        """

    async def describe_tape_archives(
        self, **kwargs: Unpack[DescribeTapeArchivesInputTypeDef]
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        Returns a description of specified virtual tapes in the virtual tape shelf
        (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_tape_archives.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_tape_archives)
        """

    async def describe_tape_recovery_points(
        self, **kwargs: Unpack[DescribeTapeRecoveryPointsInputTypeDef]
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        Returns a list of virtual tape recovery points that are available for the
        specified tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_tape_recovery_points.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_tape_recovery_points)
        """

    async def describe_tapes(
        self, **kwargs: Unpack[DescribeTapesInputTypeDef]
    ) -> DescribeTapesOutputTypeDef:
        """
        Returns a description of virtual tapes that correspond to the specified Amazon
        Resource Names (ARNs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_tapes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_tapes)
        """

    async def describe_upload_buffer(
        self, **kwargs: Unpack[DescribeUploadBufferInputTypeDef]
    ) -> DescribeUploadBufferOutputTypeDef:
        """
        Returns information about the upload buffer of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_upload_buffer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_upload_buffer)
        """

    async def describe_vtl_devices(
        self, **kwargs: Unpack[DescribeVTLDevicesInputTypeDef]
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        Returns a description of virtual tape library (VTL) devices for the specified
        tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_vtl_devices.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_vtl_devices)
        """

    async def describe_working_storage(
        self, **kwargs: Unpack[DescribeWorkingStorageInputTypeDef]
    ) -> DescribeWorkingStorageOutputTypeDef:
        """
        Returns information about the working storage of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/describe_working_storage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#describe_working_storage)
        """

    async def detach_volume(
        self, **kwargs: Unpack[DetachVolumeInputTypeDef]
    ) -> DetachVolumeOutputTypeDef:
        """
        Disconnects a volume from an iSCSI connection and then detaches the volume from
        the specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/detach_volume.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#detach_volume)
        """

    async def disable_gateway(
        self, **kwargs: Unpack[DisableGatewayInputTypeDef]
    ) -> DisableGatewayOutputTypeDef:
        """
        Disables a tape gateway when the gateway is no longer functioning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/disable_gateway.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#disable_gateway)
        """

    async def disassociate_file_system(
        self, **kwargs: Unpack[DisassociateFileSystemInputTypeDef]
    ) -> DisassociateFileSystemOutputTypeDef:
        """
        Disassociates an Amazon FSx file system from the specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/disassociate_file_system.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#disassociate_file_system)
        """

    async def evict_files_failing_upload(
        self, **kwargs: Unpack[EvictFilesFailingUploadInputTypeDef]
    ) -> EvictFilesFailingUploadOutputTypeDef:
        """
        Starts a process that cleans the specified file share's cache of file entries
        that are failing upload to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/evict_files_failing_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#evict_files_failing_upload)
        """

    async def join_domain(
        self, **kwargs: Unpack[JoinDomainInputTypeDef]
    ) -> JoinDomainOutputTypeDef:
        """
        Adds a file gateway to an Active Directory domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/join_domain.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#join_domain)
        """

    async def list_automatic_tape_creation_policies(
        self, **kwargs: Unpack[ListAutomaticTapeCreationPoliciesInputTypeDef]
    ) -> ListAutomaticTapeCreationPoliciesOutputTypeDef:
        """
        Lists the automatic tape creation policies for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_automatic_tape_creation_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_automatic_tape_creation_policies)
        """

    async def list_cache_reports(
        self, **kwargs: Unpack[ListCacheReportsInputTypeDef]
    ) -> ListCacheReportsOutputTypeDef:
        """
        Returns a list of existing cache reports for all file shares associated with
        your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_cache_reports.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_cache_reports)
        """

    async def list_file_shares(
        self, **kwargs: Unpack[ListFileSharesInputTypeDef]
    ) -> ListFileSharesOutputTypeDef:
        """
        Gets a list of the file shares for a specific S3 File Gateway, or the list of
        file shares that belong to the calling Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_file_shares.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_file_shares)
        """

    async def list_file_system_associations(
        self, **kwargs: Unpack[ListFileSystemAssociationsInputTypeDef]
    ) -> ListFileSystemAssociationsOutputTypeDef:
        """
        Gets a list of <code>FileSystemAssociationSummary</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_file_system_associations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_file_system_associations)
        """

    async def list_gateways(
        self, **kwargs: Unpack[ListGatewaysInputTypeDef]
    ) -> ListGatewaysOutputTypeDef:
        """
        Lists gateways owned by an Amazon Web Services account in an Amazon Web
        Services Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_gateways.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_gateways)
        """

    async def list_local_disks(
        self, **kwargs: Unpack[ListLocalDisksInputTypeDef]
    ) -> ListLocalDisksOutputTypeDef:
        """
        Returns a list of the gateway's local disks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_local_disks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_local_disks)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags that have been added to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_tags_for_resource)
        """

    async def list_tape_pools(
        self, **kwargs: Unpack[ListTapePoolsInputTypeDef]
    ) -> ListTapePoolsOutputTypeDef:
        """
        Lists custom tape pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_tape_pools.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_tape_pools)
        """

    async def list_tapes(self, **kwargs: Unpack[ListTapesInputTypeDef]) -> ListTapesOutputTypeDef:
        """
        Lists virtual tapes in your virtual tape library (VTL) and your virtual tape
        shelf (VTS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_tapes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_tapes)
        """

    async def list_volume_initiators(
        self, **kwargs: Unpack[ListVolumeInitiatorsInputTypeDef]
    ) -> ListVolumeInitiatorsOutputTypeDef:
        """
        Lists iSCSI initiators that are connected to a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_volume_initiators.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_volume_initiators)
        """

    async def list_volume_recovery_points(
        self, **kwargs: Unpack[ListVolumeRecoveryPointsInputTypeDef]
    ) -> ListVolumeRecoveryPointsOutputTypeDef:
        """
        Lists the recovery points for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_volume_recovery_points.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_volume_recovery_points)
        """

    async def list_volumes(
        self, **kwargs: Unpack[ListVolumesInputTypeDef]
    ) -> ListVolumesOutputTypeDef:
        """
        Lists the iSCSI stored volumes of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/list_volumes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#list_volumes)
        """

    async def notify_when_uploaded(
        self, **kwargs: Unpack[NotifyWhenUploadedInputTypeDef]
    ) -> NotifyWhenUploadedOutputTypeDef:
        """
        Sends you notification through Amazon EventBridge when all files written to
        your file share have been uploaded to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/notify_when_uploaded.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#notify_when_uploaded)
        """

    async def refresh_cache(
        self, **kwargs: Unpack[RefreshCacheInputTypeDef]
    ) -> RefreshCacheOutputTypeDef:
        """
        Refreshes the cached inventory of objects for the specified file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/refresh_cache.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#refresh_cache)
        """

    async def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceInputTypeDef]
    ) -> RemoveTagsFromResourceOutputTypeDef:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/remove_tags_from_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#remove_tags_from_resource)
        """

    async def reset_cache(
        self, **kwargs: Unpack[ResetCacheInputTypeDef]
    ) -> ResetCacheOutputTypeDef:
        """
        Resets all cache disks that have encountered an error and makes the disks
        available for reconfiguration as cache storage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/reset_cache.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#reset_cache)
        """

    async def retrieve_tape_archive(
        self, **kwargs: Unpack[RetrieveTapeArchiveInputTypeDef]
    ) -> RetrieveTapeArchiveOutputTypeDef:
        """
        Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/retrieve_tape_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#retrieve_tape_archive)
        """

    async def retrieve_tape_recovery_point(
        self, **kwargs: Unpack[RetrieveTapeRecoveryPointInputTypeDef]
    ) -> RetrieveTapeRecoveryPointOutputTypeDef:
        """
        Retrieves the recovery point for the specified virtual tape.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/retrieve_tape_recovery_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#retrieve_tape_recovery_point)
        """

    async def set_local_console_password(
        self, **kwargs: Unpack[SetLocalConsolePasswordInputTypeDef]
    ) -> SetLocalConsolePasswordOutputTypeDef:
        """
        Sets the password for your VM local console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/set_local_console_password.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#set_local_console_password)
        """

    async def set_smb_guest_password(
        self, **kwargs: Unpack[SetSMBGuestPasswordInputTypeDef]
    ) -> SetSMBGuestPasswordOutputTypeDef:
        """
        Sets the password for the guest user <code>smbguest</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/set_smb_guest_password.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#set_smb_guest_password)
        """

    async def shutdown_gateway(
        self, **kwargs: Unpack[ShutdownGatewayInputTypeDef]
    ) -> ShutdownGatewayOutputTypeDef:
        """
        Shuts down a Tape Gateway or Volume Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/shutdown_gateway.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#shutdown_gateway)
        """

    async def start_availability_monitor_test(
        self, **kwargs: Unpack[StartAvailabilityMonitorTestInputTypeDef]
    ) -> StartAvailabilityMonitorTestOutputTypeDef:
        """
        Start a test that verifies that the specified gateway is configured for High
        Availability monitoring in your host environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/start_availability_monitor_test.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#start_availability_monitor_test)
        """

    async def start_cache_report(
        self, **kwargs: Unpack[StartCacheReportInputTypeDef]
    ) -> StartCacheReportOutputTypeDef:
        """
        Starts generating a report of the file metadata currently cached by an S3 File
        Gateway for a specific file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/start_cache_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#start_cache_report)
        """

    async def start_gateway(
        self, **kwargs: Unpack[StartGatewayInputTypeDef]
    ) -> StartGatewayOutputTypeDef:
        """
        Starts a gateway that you previously shut down (see <a>ShutdownGateway</a>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/start_gateway.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#start_gateway)
        """

    async def update_automatic_tape_creation_policy(
        self, **kwargs: Unpack[UpdateAutomaticTapeCreationPolicyInputTypeDef]
    ) -> UpdateAutomaticTapeCreationPolicyOutputTypeDef:
        """
        Updates the automatic tape creation policy of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_automatic_tape_creation_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_automatic_tape_creation_policy)
        """

    async def update_bandwidth_rate_limit(
        self, **kwargs: Unpack[UpdateBandwidthRateLimitInputTypeDef]
    ) -> UpdateBandwidthRateLimitOutputTypeDef:
        """
        Updates the bandwidth rate limits of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_bandwidth_rate_limit.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_bandwidth_rate_limit)
        """

    async def update_bandwidth_rate_limit_schedule(
        self, **kwargs: Unpack[UpdateBandwidthRateLimitScheduleInputTypeDef]
    ) -> UpdateBandwidthRateLimitScheduleOutputTypeDef:
        """
        Updates the bandwidth rate limit schedule for a specified gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_bandwidth_rate_limit_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_bandwidth_rate_limit_schedule)
        """

    async def update_chap_credentials(
        self, **kwargs: Unpack[UpdateChapCredentialsInputTypeDef]
    ) -> UpdateChapCredentialsOutputTypeDef:
        """
        Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for
        a specified iSCSI target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_chap_credentials.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_chap_credentials)
        """

    async def update_file_system_association(
        self, **kwargs: Unpack[UpdateFileSystemAssociationInputTypeDef]
    ) -> UpdateFileSystemAssociationOutputTypeDef:
        """
        Updates a file system association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_file_system_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_file_system_association)
        """

    async def update_gateway_information(
        self, **kwargs: Unpack[UpdateGatewayInformationInputTypeDef]
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        Updates a gateway's metadata, which includes the gateway's name, time zone, and
        metadata cache size.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_gateway_information.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_gateway_information)
        """

    async def update_gateway_software_now(
        self, **kwargs: Unpack[UpdateGatewaySoftwareNowInputTypeDef]
    ) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        Updates the gateway virtual machine (VM) software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_gateway_software_now.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_gateway_software_now)
        """

    async def update_maintenance_start_time(
        self, **kwargs: Unpack[UpdateMaintenanceStartTimeInputTypeDef]
    ) -> UpdateMaintenanceStartTimeOutputTypeDef:
        """
        Updates a gateway's maintenance window schedule, with settings for monthly or
        weekly cadence, specific day and time to begin maintenance, and which types of
        updates to apply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_maintenance_start_time.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_maintenance_start_time)
        """

    async def update_nfs_file_share(
        self, **kwargs: Unpack[UpdateNFSFileShareInputTypeDef]
    ) -> UpdateNFSFileShareOutputTypeDef:
        """
        Updates a Network File System (NFS) file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_nfs_file_share.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_nfs_file_share)
        """

    async def update_smb_file_share(
        self, **kwargs: Unpack[UpdateSMBFileShareInputTypeDef]
    ) -> UpdateSMBFileShareOutputTypeDef:
        """
        Updates a Server Message Block (SMB) file share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_smb_file_share.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_smb_file_share)
        """

    async def update_smb_file_share_visibility(
        self, **kwargs: Unpack[UpdateSMBFileShareVisibilityInputTypeDef]
    ) -> UpdateSMBFileShareVisibilityOutputTypeDef:
        """
        Controls whether the shares on an S3 File Gateway are visible in a net view or
        browse list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_smb_file_share_visibility.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_smb_file_share_visibility)
        """

    async def update_smb_local_groups(
        self, **kwargs: Unpack[UpdateSMBLocalGroupsInputTypeDef]
    ) -> UpdateSMBLocalGroupsOutputTypeDef:
        """
        Updates the list of Active Directory users and groups that have special
        permissions for SMB file shares on the gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_smb_local_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_smb_local_groups)
        """

    async def update_smb_security_strategy(
        self, **kwargs: Unpack[UpdateSMBSecurityStrategyInputTypeDef]
    ) -> UpdateSMBSecurityStrategyOutputTypeDef:
        """
        Updates the SMB security strategy level for an Amazon S3 file gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_smb_security_strategy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_smb_security_strategy)
        """

    async def update_snapshot_schedule(
        self, **kwargs: Unpack[UpdateSnapshotScheduleInputTypeDef]
    ) -> UpdateSnapshotScheduleOutputTypeDef:
        """
        Updates a snapshot schedule configured for a gateway volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_snapshot_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_snapshot_schedule)
        """

    async def update_vtl_device_type(
        self, **kwargs: Unpack[UpdateVTLDeviceTypeInputTypeDef]
    ) -> UpdateVTLDeviceTypeOutputTypeDef:
        """
        Updates the type of medium changer in a tape gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/update_vtl_device_type.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#update_vtl_device_type)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_tape_archives"]
    ) -> DescribeTapeArchivesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> DescribeTapeRecoveryPointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_tapes"]
    ) -> DescribeTapesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> DescribeVTLDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cache_reports"]
    ) -> ListCacheReportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_file_shares"]
    ) -> ListFileSharesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_file_system_associations"]
    ) -> ListFileSystemAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateways"]
    ) -> ListGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tape_pools"]
    ) -> ListTapePoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tapes"]
    ) -> ListTapesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_volumes"]
    ) -> ListVolumesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_storagegateway/client/)
        """
