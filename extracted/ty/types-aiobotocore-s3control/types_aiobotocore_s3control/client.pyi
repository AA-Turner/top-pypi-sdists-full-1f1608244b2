"""
Type annotations for s3control service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_s3control.client import S3ControlClient

    session = get_session()
    async with session.create_client("s3control") as client:
        client: S3ControlClient
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

from .paginator import ListAccessPointsForObjectLambdaPaginator, ListCallerAccessGrantsPaginator
from .type_defs import (
    AssociateAccessGrantsIdentityCenterRequestTypeDef,
    CreateAccessGrantRequestTypeDef,
    CreateAccessGrantResultTypeDef,
    CreateAccessGrantsInstanceRequestTypeDef,
    CreateAccessGrantsInstanceResultTypeDef,
    CreateAccessGrantsLocationRequestTypeDef,
    CreateAccessGrantsLocationResultTypeDef,
    CreateAccessPointForObjectLambdaRequestTypeDef,
    CreateAccessPointForObjectLambdaResultTypeDef,
    CreateAccessPointRequestTypeDef,
    CreateAccessPointResultTypeDef,
    CreateBucketRequestTypeDef,
    CreateBucketResultTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResultTypeDef,
    CreateMultiRegionAccessPointRequestTypeDef,
    CreateMultiRegionAccessPointResultTypeDef,
    CreateStorageLensGroupRequestTypeDef,
    DeleteAccessGrantRequestTypeDef,
    DeleteAccessGrantsInstanceRequestTypeDef,
    DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef,
    DeleteAccessGrantsLocationRequestTypeDef,
    DeleteAccessPointForObjectLambdaRequestTypeDef,
    DeleteAccessPointPolicyForObjectLambdaRequestTypeDef,
    DeleteAccessPointPolicyRequestTypeDef,
    DeleteAccessPointRequestTypeDef,
    DeleteBucketLifecycleConfigurationRequestTypeDef,
    DeleteBucketPolicyRequestTypeDef,
    DeleteBucketReplicationRequestTypeDef,
    DeleteBucketRequestTypeDef,
    DeleteBucketTaggingRequestTypeDef,
    DeleteJobTaggingRequestTypeDef,
    DeleteMultiRegionAccessPointRequestTypeDef,
    DeleteMultiRegionAccessPointResultTypeDef,
    DeletePublicAccessBlockRequestTypeDef,
    DeleteStorageLensConfigurationRequestTypeDef,
    DeleteStorageLensConfigurationTaggingRequestTypeDef,
    DeleteStorageLensGroupRequestTypeDef,
    DescribeJobRequestTypeDef,
    DescribeJobResultTypeDef,
    DescribeMultiRegionAccessPointOperationRequestTypeDef,
    DescribeMultiRegionAccessPointOperationResultTypeDef,
    DissociateAccessGrantsIdentityCenterRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccessGrantRequestTypeDef,
    GetAccessGrantResultTypeDef,
    GetAccessGrantsInstanceForPrefixRequestTypeDef,
    GetAccessGrantsInstanceForPrefixResultTypeDef,
    GetAccessGrantsInstanceRequestTypeDef,
    GetAccessGrantsInstanceResourcePolicyRequestTypeDef,
    GetAccessGrantsInstanceResourcePolicyResultTypeDef,
    GetAccessGrantsInstanceResultTypeDef,
    GetAccessGrantsLocationRequestTypeDef,
    GetAccessGrantsLocationResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaRequestTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaRequestTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaRequestTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyRequestTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusRequestTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointRequestTypeDef,
    GetAccessPointResultTypeDef,
    GetBucketLifecycleConfigurationRequestTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyRequestTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketReplicationRequestTypeDef,
    GetBucketReplicationResultTypeDef,
    GetBucketRequestTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingRequestTypeDef,
    GetBucketTaggingResultTypeDef,
    GetBucketVersioningRequestTypeDef,
    GetBucketVersioningResultTypeDef,
    GetDataAccessRequestTypeDef,
    GetDataAccessResultTypeDef,
    GetJobTaggingRequestTypeDef,
    GetJobTaggingResultTypeDef,
    GetMultiRegionAccessPointPolicyRequestTypeDef,
    GetMultiRegionAccessPointPolicyResultTypeDef,
    GetMultiRegionAccessPointPolicyStatusRequestTypeDef,
    GetMultiRegionAccessPointPolicyStatusResultTypeDef,
    GetMultiRegionAccessPointRequestTypeDef,
    GetMultiRegionAccessPointResultTypeDef,
    GetMultiRegionAccessPointRoutesRequestTypeDef,
    GetMultiRegionAccessPointRoutesResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetPublicAccessBlockRequestTypeDef,
    GetStorageLensConfigurationRequestTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingRequestTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    GetStorageLensGroupRequestTypeDef,
    GetStorageLensGroupResultTypeDef,
    ListAccessGrantsInstancesRequestTypeDef,
    ListAccessGrantsInstancesResultTypeDef,
    ListAccessGrantsLocationsRequestTypeDef,
    ListAccessGrantsLocationsResultTypeDef,
    ListAccessGrantsRequestTypeDef,
    ListAccessGrantsResultTypeDef,
    ListAccessPointsForObjectLambdaRequestTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsRequestTypeDef,
    ListAccessPointsResultTypeDef,
    ListCallerAccessGrantsRequestTypeDef,
    ListCallerAccessGrantsResultTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResultTypeDef,
    ListMultiRegionAccessPointsRequestTypeDef,
    ListMultiRegionAccessPointsResultTypeDef,
    ListRegionalBucketsRequestTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsRequestTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ListStorageLensGroupsRequestTypeDef,
    ListStorageLensGroupsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PutAccessGrantsInstanceResourcePolicyRequestTypeDef,
    PutAccessGrantsInstanceResourcePolicyResultTypeDef,
    PutAccessPointConfigurationForObjectLambdaRequestTypeDef,
    PutAccessPointPolicyForObjectLambdaRequestTypeDef,
    PutAccessPointPolicyRequestTypeDef,
    PutBucketLifecycleConfigurationRequestTypeDef,
    PutBucketPolicyRequestTypeDef,
    PutBucketReplicationRequestTypeDef,
    PutBucketTaggingRequestTypeDef,
    PutBucketVersioningRequestTypeDef,
    PutJobTaggingRequestTypeDef,
    PutMultiRegionAccessPointPolicyRequestTypeDef,
    PutMultiRegionAccessPointPolicyResultTypeDef,
    PutPublicAccessBlockRequestTypeDef,
    PutStorageLensConfigurationRequestTypeDef,
    PutStorageLensConfigurationTaggingRequestTypeDef,
    SubmitMultiRegionAccessPointRoutesRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessGrantsLocationRequestTypeDef,
    UpdateAccessGrantsLocationResultTypeDef,
    UpdateJobPriorityRequestTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusRequestTypeDef,
    UpdateJobStatusResultTypeDef,
    UpdateStorageLensGroupRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack

__all__ = ("S3ControlClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobStatusException: Type[BotocoreClientError]
    NoSuchPublicAccessBlockConfiguration: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class S3ControlClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3ControlClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#generate_presigned_url)
        """

    async def associate_access_grants_identity_center(
        self, **kwargs: Unpack[AssociateAccessGrantsIdentityCenterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associate your S3 Access Grants instance with an Amazon Web Services IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/associate_access_grants_identity_center.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#associate_access_grants_identity_center)
        """

    async def create_access_grant(
        self, **kwargs: Unpack[CreateAccessGrantRequestTypeDef]
    ) -> CreateAccessGrantResultTypeDef:
        """
        Creates an access grant that gives a grantee access to your S3 data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_access_grant)
        """

    async def create_access_grants_instance(
        self, **kwargs: Unpack[CreateAccessGrantsInstanceRequestTypeDef]
    ) -> CreateAccessGrantsInstanceResultTypeDef:
        """
        Creates an S3 Access Grants instance, which serves as a logical grouping for
        access grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grants_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_access_grants_instance)
        """

    async def create_access_grants_location(
        self, **kwargs: Unpack[CreateAccessGrantsLocationRequestTypeDef]
    ) -> CreateAccessGrantsLocationResultTypeDef:
        """
        The S3 data location that you would like to register in your S3 Access Grants
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grants_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_access_grants_location)
        """

    async def create_access_point(
        self, **kwargs: Unpack[CreateAccessPointRequestTypeDef]
    ) -> CreateAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_access_point)
        """

    async def create_access_point_for_object_lambda(
        self, **kwargs: Unpack[CreateAccessPointForObjectLambdaRequestTypeDef]
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_point_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_access_point_for_object_lambda)
        """

    async def create_bucket(
        self, **kwargs: Unpack[CreateBucketRequestTypeDef]
    ) -> CreateBucketResultTypeDef:
        """
        This action creates an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_bucket.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_bucket)
        """

    async def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResultTypeDef:
        """
        This operation creates an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_job)
        """

    async def create_multi_region_access_point(
        self, **kwargs: Unpack[CreateMultiRegionAccessPointRequestTypeDef]
    ) -> CreateMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_multi_region_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_multi_region_access_point)
        """

    async def create_storage_lens_group(
        self, **kwargs: Unpack[CreateStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a new S3 Storage Lens group and associates it with the specified Amazon
        Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_storage_lens_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#create_storage_lens_group)
        """

    async def delete_access_grant(
        self, **kwargs: Unpack[DeleteAccessGrantRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the access grant from the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_grant)
        """

    async def delete_access_grants_instance(
        self, **kwargs: Unpack[DeleteAccessGrantsInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_grants_instance)
        """

    async def delete_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_instance_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_grants_instance_resource_policy)
        """

    async def delete_access_grants_location(
        self, **kwargs: Unpack[DeleteAccessGrantsLocationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters a location from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_grants_location)
        """

    async def delete_access_point(
        self, **kwargs: Unpack[DeleteAccessPointRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_point)
        """

    async def delete_access_point_for_object_lambda(
        self, **kwargs: Unpack[DeleteAccessPointForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_point_for_object_lambda)
        """

    async def delete_access_point_policy(
        self, **kwargs: Unpack[DeleteAccessPointPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_point_policy)
        """

    async def delete_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[DeleteAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_policy_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_access_point_policy_for_object_lambda)
        """

    async def delete_bucket(
        self, **kwargs: Unpack[DeleteBucketRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_bucket)
        """

    async def delete_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[DeleteBucketLifecycleConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket's lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_lifecycle_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_bucket_lifecycle_configuration)
        """

    async def delete_bucket_policy(
        self, **kwargs: Unpack[DeleteBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_bucket_policy)
        """

    async def delete_bucket_replication(
        self, **kwargs: Unpack[DeleteBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes an Amazon S3 on Outposts bucket's replication
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_replication.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_bucket_replication)
        """

    async def delete_bucket_tagging(
        self, **kwargs: Unpack[DeleteBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket's tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_bucket_tagging)
        """

    async def delete_job_tagging(
        self, **kwargs: Unpack[DeleteJobTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the entire tag set from the specified S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_job_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_job_tagging)
        """

    async def delete_multi_region_access_point(
        self, **kwargs: Unpack[DeleteMultiRegionAccessPointRequestTypeDef]
    ) -> DeleteMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_multi_region_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_multi_region_access_point)
        """

    async def delete_public_access_block(
        self, **kwargs: Unpack[DeletePublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_public_access_block.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_public_access_block)
        """

    async def delete_storage_lens_configuration(
        self, **kwargs: Unpack[DeleteStorageLensConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_storage_lens_configuration)
        """

    async def delete_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[DeleteStorageLensConfigurationTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_configuration_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_storage_lens_configuration_tagging)
        """

    async def delete_storage_lens_group(
        self, **kwargs: Unpack[DeleteStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing S3 Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#delete_storage_lens_group)
        """

    async def describe_job(
        self, **kwargs: Unpack[DescribeJobRequestTypeDef]
    ) -> DescribeJobResultTypeDef:
        """
        Retrieves the configuration parameters and status for a Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/describe_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#describe_job)
        """

    async def describe_multi_region_access_point_operation(
        self, **kwargs: Unpack[DescribeMultiRegionAccessPointOperationRequestTypeDef]
    ) -> DescribeMultiRegionAccessPointOperationResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/describe_multi_region_access_point_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#describe_multi_region_access_point_operation)
        """

    async def dissociate_access_grants_identity_center(
        self, **kwargs: Unpack[DissociateAccessGrantsIdentityCenterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Dissociates the Amazon Web Services IAM Identity Center instance from the S3
        Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/dissociate_access_grants_identity_center.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#dissociate_access_grants_identity_center)
        """

    async def get_access_grant(
        self, **kwargs: Unpack[GetAccessGrantRequestTypeDef]
    ) -> GetAccessGrantResultTypeDef:
        """
        Get the details of an access grant from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_grant)
        """

    async def get_access_grants_instance(
        self, **kwargs: Unpack[GetAccessGrantsInstanceRequestTypeDef]
    ) -> GetAccessGrantsInstanceResultTypeDef:
        """
        Retrieves the S3 Access Grants instance for a Region in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_grants_instance)
        """

    async def get_access_grants_instance_for_prefix(
        self, **kwargs: Unpack[GetAccessGrantsInstanceForPrefixRequestTypeDef]
    ) -> GetAccessGrantsInstanceForPrefixResultTypeDef:
        """
        Retrieve the S3 Access Grants instance that contains a particular prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance_for_prefix.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_grants_instance_for_prefix)
        """

    async def get_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[GetAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> GetAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Returns the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_grants_instance_resource_policy)
        """

    async def get_access_grants_location(
        self, **kwargs: Unpack[GetAccessGrantsLocationRequestTypeDef]
    ) -> GetAccessGrantsLocationResultTypeDef:
        """
        Retrieves the details of a particular location registered in your S3 Access
        Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_grants_location)
        """

    async def get_access_point(
        self, **kwargs: Unpack[GetAccessPointRequestTypeDef]
    ) -> GetAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point)
        """

    async def get_access_point_configuration_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointConfigurationForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_configuration_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_configuration_for_object_lambda)
        """

    async def get_access_point_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_for_object_lambda)
        """

    async def get_access_point_policy(
        self, **kwargs: Unpack[GetAccessPointPolicyRequestTypeDef]
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_policy)
        """

    async def get_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_policy_for_object_lambda)
        """

    async def get_access_point_policy_status(
        self, **kwargs: Unpack[GetAccessPointPolicyStatusRequestTypeDef]
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_policy_status)
        """

    async def get_access_point_policy_status_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_status_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_access_point_policy_status_for_object_lambda)
        """

    async def get_bucket(self, **kwargs: Unpack[GetBucketRequestTypeDef]) -> GetBucketResultTypeDef:
        """
        Gets an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket)
        """

    async def get_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[GetBucketLifecycleConfigurationRequestTypeDef]
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        This action gets an Amazon S3 on Outposts bucket's lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_lifecycle_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket_lifecycle_configuration)
        """

    async def get_bucket_policy(
        self, **kwargs: Unpack[GetBucketPolicyRequestTypeDef]
    ) -> GetBucketPolicyResultTypeDef:
        """
        This action gets a bucket policy for an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket_policy)
        """

    async def get_bucket_replication(
        self, **kwargs: Unpack[GetBucketReplicationRequestTypeDef]
    ) -> GetBucketReplicationResultTypeDef:
        """
        This operation gets an Amazon S3 on Outposts bucket's replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_replication.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket_replication)
        """

    async def get_bucket_tagging(
        self, **kwargs: Unpack[GetBucketTaggingRequestTypeDef]
    ) -> GetBucketTaggingResultTypeDef:
        """
        This action gets an Amazon S3 on Outposts bucket's tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket_tagging)
        """

    async def get_bucket_versioning(
        self, **kwargs: Unpack[GetBucketVersioningRequestTypeDef]
    ) -> GetBucketVersioningResultTypeDef:
        """
        This operation returns the versioning state for S3 on Outposts buckets only.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_versioning.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_bucket_versioning)
        """

    async def get_data_access(
        self, **kwargs: Unpack[GetDataAccessRequestTypeDef]
    ) -> GetDataAccessResultTypeDef:
        """
        Returns a temporary access credential from S3 Access Grants to the grantee or
        client application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_data_access.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_data_access)
        """

    async def get_job_tagging(
        self, **kwargs: Unpack[GetJobTaggingRequestTypeDef]
    ) -> GetJobTaggingResultTypeDef:
        """
        Returns the tags on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_job_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_job_tagging)
        """

    async def get_multi_region_access_point(
        self, **kwargs: Unpack[GetMultiRegionAccessPointRequestTypeDef]
    ) -> GetMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_multi_region_access_point)
        """

    async def get_multi_region_access_point_policy(
        self, **kwargs: Unpack[GetMultiRegionAccessPointPolicyRequestTypeDef]
    ) -> GetMultiRegionAccessPointPolicyResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_multi_region_access_point_policy)
        """

    async def get_multi_region_access_point_policy_status(
        self, **kwargs: Unpack[GetMultiRegionAccessPointPolicyStatusRequestTypeDef]
    ) -> GetMultiRegionAccessPointPolicyStatusResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_policy_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_multi_region_access_point_policy_status)
        """

    async def get_multi_region_access_point_routes(
        self, **kwargs: Unpack[GetMultiRegionAccessPointRoutesRequestTypeDef]
    ) -> GetMultiRegionAccessPointRoutesResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_routes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_multi_region_access_point_routes)
        """

    async def get_public_access_block(
        self, **kwargs: Unpack[GetPublicAccessBlockRequestTypeDef]
    ) -> GetPublicAccessBlockOutputTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_public_access_block.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_public_access_block)
        """

    async def get_storage_lens_configuration(
        self, **kwargs: Unpack[GetStorageLensConfigurationRequestTypeDef]
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_storage_lens_configuration)
        """

    async def get_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[GetStorageLensConfigurationTaggingRequestTypeDef]
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_configuration_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_storage_lens_configuration_tagging)
        """

    async def get_storage_lens_group(
        self, **kwargs: Unpack[GetStorageLensGroupRequestTypeDef]
    ) -> GetStorageLensGroupResultTypeDef:
        """
        Retrieves the Storage Lens group configuration details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_storage_lens_group)
        """

    async def list_access_grants(
        self, **kwargs: Unpack[ListAccessGrantsRequestTypeDef]
    ) -> ListAccessGrantsResultTypeDef:
        """
        Returns the list of access grants in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_access_grants)
        """

    async def list_access_grants_instances(
        self, **kwargs: Unpack[ListAccessGrantsInstancesRequestTypeDef]
    ) -> ListAccessGrantsInstancesResultTypeDef:
        """
        Returns a list of S3 Access Grants instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants_instances.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_access_grants_instances)
        """

    async def list_access_grants_locations(
        self, **kwargs: Unpack[ListAccessGrantsLocationsRequestTypeDef]
    ) -> ListAccessGrantsLocationsResultTypeDef:
        """
        Returns a list of the locations registered in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants_locations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_access_grants_locations)
        """

    async def list_access_points(
        self, **kwargs: Unpack[ListAccessPointsRequestTypeDef]
    ) -> ListAccessPointsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_points.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_access_points)
        """

    async def list_access_points_for_object_lambda(
        self, **kwargs: Unpack[ListAccessPointsForObjectLambdaRequestTypeDef]
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_points_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_access_points_for_object_lambda)
        """

    async def list_caller_access_grants(
        self, **kwargs: Unpack[ListCallerAccessGrantsRequestTypeDef]
    ) -> ListCallerAccessGrantsResultTypeDef:
        """
        Use this API to list the access grants that grant the caller access to Amazon
        S3 data through S3 Access Grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_caller_access_grants.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_caller_access_grants)
        """

    async def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResultTypeDef:
        """
        Lists current S3 Batch Operations jobs as well as the jobs that have ended
        within the last 90 days for the Amazon Web Services account making the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_jobs)
        """

    async def list_multi_region_access_points(
        self, **kwargs: Unpack[ListMultiRegionAccessPointsRequestTypeDef]
    ) -> ListMultiRegionAccessPointsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_multi_region_access_points.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_multi_region_access_points)
        """

    async def list_regional_buckets(
        self, **kwargs: Unpack[ListRegionalBucketsRequestTypeDef]
    ) -> ListRegionalBucketsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_regional_buckets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_regional_buckets)
        """

    async def list_storage_lens_configurations(
        self, **kwargs: Unpack[ListStorageLensConfigurationsRequestTypeDef]
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_storage_lens_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_storage_lens_configurations)
        """

    async def list_storage_lens_groups(
        self, **kwargs: Unpack[ListStorageLensGroupsRequestTypeDef]
    ) -> ListStorageLensGroupsResultTypeDef:
        """
        Lists all the Storage Lens groups in the specified home Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_storage_lens_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_storage_lens_groups)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        This operation allows you to list all the Amazon Web Services resource tags for
        a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#list_tags_for_resource)
        """

    async def put_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[PutAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> PutAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Updates the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_grants_instance_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_access_grants_instance_resource_policy)
        """

    async def put_access_point_configuration_for_object_lambda(
        self, **kwargs: Unpack[PutAccessPointConfigurationForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_configuration_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_access_point_configuration_for_object_lambda)
        """

    async def put_access_point_policy(
        self, **kwargs: Unpack[PutAccessPointPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_access_point_policy)
        """

    async def put_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[PutAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_policy_for_object_lambda.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_access_point_policy_for_object_lambda)
        """

    async def put_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[PutBucketLifecycleConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_lifecycle_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_bucket_lifecycle_configuration)
        """

    async def put_bucket_policy(
        self, **kwargs: Unpack[PutBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts a bucket policy to an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_bucket_policy)
        """

    async def put_bucket_replication(
        self, **kwargs: Unpack[PutBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action creates an Amazon S3 on Outposts bucket's replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_replication.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_bucket_replication)
        """

    async def put_bucket_tagging(
        self, **kwargs: Unpack[PutBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts tags on an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_bucket_tagging)
        """

    async def put_bucket_versioning(
        self, **kwargs: Unpack[PutBucketVersioningRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation sets the versioning state for S3 on Outposts buckets only.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_versioning.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_bucket_versioning)
        """

    async def put_job_tagging(
        self, **kwargs: Unpack[PutJobTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the supplied tag-set on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_job_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_job_tagging)
        """

    async def put_multi_region_access_point_policy(
        self, **kwargs: Unpack[PutMultiRegionAccessPointPolicyRequestTypeDef]
    ) -> PutMultiRegionAccessPointPolicyResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_multi_region_access_point_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_multi_region_access_point_policy)
        """

    async def put_public_access_block(
        self, **kwargs: Unpack[PutPublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_public_access_block.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_public_access_block)
        """

    async def put_storage_lens_configuration(
        self, **kwargs: Unpack[PutStorageLensConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_storage_lens_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_storage_lens_configuration)
        """

    async def put_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[PutStorageLensConfigurationTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_storage_lens_configuration_tagging.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#put_storage_lens_configuration_tagging)
        """

    async def submit_multi_region_access_point_routes(
        self, **kwargs: Unpack[SubmitMultiRegionAccessPointRoutesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/submit_multi_region_access_point_routes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#submit_multi_region_access_point_routes)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new Amazon Web Services resource tag or updates an existing resource
        tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        This operation removes the specified Amazon Web Services resource tags from an
        S3 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#untag_resource)
        """

    async def update_access_grants_location(
        self, **kwargs: Unpack[UpdateAccessGrantsLocationRequestTypeDef]
    ) -> UpdateAccessGrantsLocationResultTypeDef:
        """
        Updates the IAM role of a registered location in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_access_grants_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#update_access_grants_location)
        """

    async def update_job_priority(
        self, **kwargs: Unpack[UpdateJobPriorityRequestTypeDef]
    ) -> UpdateJobPriorityResultTypeDef:
        """
        Updates an existing S3 Batch Operations job's priority.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_job_priority.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#update_job_priority)
        """

    async def update_job_status(
        self, **kwargs: Unpack[UpdateJobStatusRequestTypeDef]
    ) -> UpdateJobStatusResultTypeDef:
        """
        Updates the status for the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_job_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#update_job_status)
        """

    async def update_storage_lens_group(
        self, **kwargs: Unpack[UpdateStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the existing Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_storage_lens_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#update_storage_lens_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_caller_access_grants"]
    ) -> ListCallerAccessGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client/)
        """
