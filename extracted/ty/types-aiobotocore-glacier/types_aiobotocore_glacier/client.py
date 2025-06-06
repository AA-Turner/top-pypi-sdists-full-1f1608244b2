"""
Type annotations for glacier service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_glacier.client import GlacierClient

    session = get_session()
    async with session.create_client("glacier") as client:
        client: GlacierClient
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
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from .type_defs import (
    AbortMultipartUploadInputTypeDef,
    AbortVaultLockInputTypeDef,
    AddTagsToVaultInputTypeDef,
    ArchiveCreationOutputTypeDef,
    CompleteMultipartUploadInputTypeDef,
    CompleteVaultLockInputTypeDef,
    CreateVaultInputTypeDef,
    CreateVaultOutputTypeDef,
    DeleteArchiveInputTypeDef,
    DeleteVaultAccessPolicyInputTypeDef,
    DeleteVaultInputTypeDef,
    DeleteVaultNotificationsInputTypeDef,
    DescribeJobInputTypeDef,
    DescribeVaultInputTypeDef,
    DescribeVaultResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDataRetrievalPolicyInputTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputInputTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyInputTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockInputTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsInputTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionResponseTypeDef,
    InitiateJobInputTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadInputTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    InitiateVaultLockInputTypeDef,
    InitiateVaultLockOutputTypeDef,
    ListJobsInputTypeDef,
    ListJobsOutputTypeDef,
    ListMultipartUploadsInputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsInputTypeDef,
    ListPartsOutputTypeDef,
    ListProvisionedCapacityInputTypeDef,
    ListProvisionedCapacityOutputTypeDef,
    ListTagsForVaultInputTypeDef,
    ListTagsForVaultOutputTypeDef,
    ListVaultsInputTypeDef,
    ListVaultsOutputTypeDef,
    PurchaseProvisionedCapacityInputTypeDef,
    PurchaseProvisionedCapacityOutputTypeDef,
    RemoveTagsFromVaultInputTypeDef,
    SetDataRetrievalPolicyInputTypeDef,
    SetVaultAccessPolicyInputTypeDef,
    SetVaultNotificationsInputTypeDef,
    UploadArchiveInputTypeDef,
    UploadMultipartPartInputTypeDef,
    UploadMultipartPartOutputTypeDef,
)
from .waiter import VaultExistsWaiter, VaultNotExistsWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("GlacierClient",)


class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    PolicyEnforcedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class GlacierClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GlacierClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#generate_presigned_url)
        """

    async def abort_multipart_upload(
        self, **kwargs: Unpack[AbortMultipartUploadInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation aborts a multipart upload identified by the upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/abort_multipart_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#abort_multipart_upload)
        """

    async def abort_vault_lock(
        self, **kwargs: Unpack[AbortVaultLockInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation aborts the vault locking process if the vault lock is not in the
        <code>Locked</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/abort_vault_lock.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#abort_vault_lock)
        """

    async def add_tags_to_vault(
        self, **kwargs: Unpack[AddTagsToVaultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation adds the specified tags to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/add_tags_to_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#add_tags_to_vault)
        """

    async def complete_multipart_upload(
        self, **kwargs: Unpack[CompleteMultipartUploadInputTypeDef]
    ) -> ArchiveCreationOutputTypeDef:
        """
        You call this operation to inform Amazon S3 Glacier (Glacier) that all the
        archive parts have been uploaded and that Glacier can now assemble the archive
        from the uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/complete_multipart_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#complete_multipart_upload)
        """

    async def complete_vault_lock(
        self, **kwargs: Unpack[CompleteVaultLockInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation completes the vault locking process by transitioning the vault
        lock from the <code>InProgress</code> state to the <code>Locked</code> state,
        which causes the vault lock policy to become unchangeable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/complete_vault_lock.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#complete_vault_lock)
        """

    async def create_vault(
        self, **kwargs: Unpack[CreateVaultInputTypeDef]
    ) -> CreateVaultOutputTypeDef:
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/create_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#create_vault)
        """

    async def delete_archive(
        self, **kwargs: Unpack[DeleteArchiveInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes an archive from a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/delete_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#delete_archive)
        """

    async def delete_vault(
        self, **kwargs: Unpack[DeleteVaultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/delete_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#delete_vault)
        """

    async def delete_vault_access_policy(
        self, **kwargs: Unpack[DeleteVaultAccessPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes the access policy associated with the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/delete_vault_access_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#delete_vault_access_policy)
        """

    async def delete_vault_notifications(
        self, **kwargs: Unpack[DeleteVaultNotificationsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes the notification configuration set for a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/delete_vault_notifications.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#delete_vault_notifications)
        """

    async def describe_job(
        self, **kwargs: Unpack[DescribeJobInputTypeDef]
    ) -> GlacierJobDescriptionResponseTypeDef:
        """
        This operation returns information about a job you previously initiated,
        including the job initiation date, the user who initiated the job, the job
        status code/message and the Amazon SNS topic to notify after Amazon S3 Glacier
        (Glacier) completes the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/describe_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#describe_job)
        """

    async def describe_vault(
        self, **kwargs: Unpack[DescribeVaultInputTypeDef]
    ) -> DescribeVaultResponseTypeDef:
        """
        This operation returns information about a vault, including the vault's Amazon
        Resource Name (ARN), the date the vault was created, the number of archives it
        contains, and the total size of all the archives in the vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/describe_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#describe_vault)
        """

    async def get_data_retrieval_policy(
        self, **kwargs: Unpack[GetDataRetrievalPolicyInputTypeDef]
    ) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        This operation returns the current data retrieval policy for the account and
        region specified in the GET request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_data_retrieval_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_data_retrieval_policy)
        """

    async def get_job_output(
        self, **kwargs: Unpack[GetJobOutputInputTypeDef]
    ) -> GetJobOutputOutputTypeDef:
        """
        This operation downloads the output of the job you initiated using
        <a>InitiateJob</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_job_output.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_job_output)
        """

    async def get_vault_access_policy(
        self, **kwargs: Unpack[GetVaultAccessPolicyInputTypeDef]
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        This operation retrieves the <code>access-policy</code> subresource set on the
        vault; for more information on setting this subresource, see <a
        href="https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html">Set
        Vault Access Policy (PUT access-policy)</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_vault_access_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_vault_access_policy)
        """

    async def get_vault_lock(
        self, **kwargs: Unpack[GetVaultLockInputTypeDef]
    ) -> GetVaultLockOutputTypeDef:
        """
        This operation retrieves the following attributes from the
        <code>lock-policy</code> subresource set on the specified vault:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_vault_lock.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_vault_lock)
        """

    async def get_vault_notifications(
        self, **kwargs: Unpack[GetVaultNotificationsInputTypeDef]
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        This operation retrieves the <code>notification-configuration</code>
        subresource of the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_vault_notifications.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_vault_notifications)
        """

    async def initiate_job(
        self, **kwargs: Unpack[InitiateJobInputTypeDef]
    ) -> InitiateJobOutputTypeDef:
        """
        This operation initiates a job of the specified type, which can be a select, an
        archival retrieval, or a vault retrieval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/initiate_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#initiate_job)
        """

    async def initiate_multipart_upload(
        self, **kwargs: Unpack[InitiateMultipartUploadInputTypeDef]
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        This operation initiates a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/initiate_multipart_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#initiate_multipart_upload)
        """

    async def initiate_vault_lock(
        self, **kwargs: Unpack[InitiateVaultLockInputTypeDef]
    ) -> InitiateVaultLockOutputTypeDef:
        """
        This operation initiates the vault locking process by doing the following:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/initiate_vault_lock.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#initiate_vault_lock)
        """

    async def list_jobs(self, **kwargs: Unpack[ListJobsInputTypeDef]) -> ListJobsOutputTypeDef:
        """
        This operation lists jobs for a vault, including jobs that are in-progress and
        jobs that have recently finished.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_jobs)
        """

    async def list_multipart_uploads(
        self, **kwargs: Unpack[ListMultipartUploadsInputTypeDef]
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        This operation lists in-progress multipart uploads for the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_multipart_uploads.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_multipart_uploads)
        """

    async def list_parts(self, **kwargs: Unpack[ListPartsInputTypeDef]) -> ListPartsOutputTypeDef:
        """
        This operation lists the parts of an archive that have been uploaded in a
        specific multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_parts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_parts)
        """

    async def list_provisioned_capacity(
        self, **kwargs: Unpack[ListProvisionedCapacityInputTypeDef]
    ) -> ListProvisionedCapacityOutputTypeDef:
        """
        This operation lists the provisioned capacity units for the specified AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_provisioned_capacity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_provisioned_capacity)
        """

    async def list_tags_for_vault(
        self, **kwargs: Unpack[ListTagsForVaultInputTypeDef]
    ) -> ListTagsForVaultOutputTypeDef:
        """
        This operation lists all the tags attached to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_tags_for_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_tags_for_vault)
        """

    async def list_vaults(
        self, **kwargs: Unpack[ListVaultsInputTypeDef]
    ) -> ListVaultsOutputTypeDef:
        """
        This operation lists all vaults owned by the calling user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/list_vaults.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#list_vaults)
        """

    async def purchase_provisioned_capacity(
        self, **kwargs: Unpack[PurchaseProvisionedCapacityInputTypeDef]
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        This operation purchases a provisioned capacity unit for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/purchase_provisioned_capacity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#purchase_provisioned_capacity)
        """

    async def remove_tags_from_vault(
        self, **kwargs: Unpack[RemoveTagsFromVaultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation removes one or more tags from the set of tags attached to a
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/remove_tags_from_vault.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#remove_tags_from_vault)
        """

    async def set_data_retrieval_policy(
        self, **kwargs: Unpack[SetDataRetrievalPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation sets and then enacts a data retrieval policy in the region
        specified in the PUT request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/set_data_retrieval_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#set_data_retrieval_policy)
        """

    async def set_vault_access_policy(
        self, **kwargs: Unpack[SetVaultAccessPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation configures an access policy for a vault and will overwrite an
        existing policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/set_vault_access_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#set_vault_access_policy)
        """

    async def set_vault_notifications(
        self, **kwargs: Unpack[SetVaultNotificationsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation configures notifications that will be sent when specific events
        happen to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/set_vault_notifications.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#set_vault_notifications)
        """

    async def upload_archive(
        self, **kwargs: Unpack[UploadArchiveInputTypeDef]
    ) -> ArchiveCreationOutputTypeDef:
        """
        This operation adds an archive to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/upload_archive.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#upload_archive)
        """

    async def upload_multipart_part(
        self, **kwargs: Unpack[UploadMultipartPartInputTypeDef]
    ) -> UploadMultipartPartOutputTypeDef:
        """
        This operation uploads a part of an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/upload_multipart_part.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#upload_multipart_part)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_parts"]
    ) -> ListPartsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vaults"]
    ) -> ListVaultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vault_exists"]
    ) -> VaultExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vault_not_exists"]
    ) -> VaultNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/client/)
        """
