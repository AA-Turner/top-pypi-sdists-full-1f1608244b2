"""
Type annotations for cloudfront service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_cloudfront.client import CloudFrontClient

    session = get_session()
    async with session.create_client("cloudfront") as client:
        client: CloudFrontClient
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
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListKeyValueStoresPaginator,
    ListPublicKeysPaginator,
    ListStreamingDistributionsPaginator,
)
from .type_defs import (
    AssociateAliasRequestTypeDef,
    CopyDistributionRequestTypeDef,
    CopyDistributionResultTypeDef,
    CreateAnycastIpListRequestTypeDef,
    CreateAnycastIpListResultTypeDef,
    CreateCachePolicyRequestTypeDef,
    CreateCachePolicyResultTypeDef,
    CreateCloudFrontOriginAccessIdentityRequestTypeDef,
    CreateCloudFrontOriginAccessIdentityResultTypeDef,
    CreateContinuousDeploymentPolicyRequestTypeDef,
    CreateContinuousDeploymentPolicyResultTypeDef,
    CreateDistributionRequestTypeDef,
    CreateDistributionResultTypeDef,
    CreateDistributionWithTagsRequestTypeDef,
    CreateDistributionWithTagsResultTypeDef,
    CreateFieldLevelEncryptionConfigRequestTypeDef,
    CreateFieldLevelEncryptionConfigResultTypeDef,
    CreateFieldLevelEncryptionProfileRequestTypeDef,
    CreateFieldLevelEncryptionProfileResultTypeDef,
    CreateFunctionRequestTypeDef,
    CreateFunctionResultTypeDef,
    CreateInvalidationRequestTypeDef,
    CreateInvalidationResultTypeDef,
    CreateKeyGroupRequestTypeDef,
    CreateKeyGroupResultTypeDef,
    CreateKeyValueStoreRequestTypeDef,
    CreateKeyValueStoreResultTypeDef,
    CreateMonitoringSubscriptionRequestTypeDef,
    CreateMonitoringSubscriptionResultTypeDef,
    CreateOriginAccessControlRequestTypeDef,
    CreateOriginAccessControlResultTypeDef,
    CreateOriginRequestPolicyRequestTypeDef,
    CreateOriginRequestPolicyResultTypeDef,
    CreatePublicKeyRequestTypeDef,
    CreatePublicKeyResultTypeDef,
    CreateRealtimeLogConfigRequestTypeDef,
    CreateRealtimeLogConfigResultTypeDef,
    CreateResponseHeadersPolicyRequestTypeDef,
    CreateResponseHeadersPolicyResultTypeDef,
    CreateStreamingDistributionRequestTypeDef,
    CreateStreamingDistributionResultTypeDef,
    CreateStreamingDistributionWithTagsRequestTypeDef,
    CreateStreamingDistributionWithTagsResultTypeDef,
    CreateVpcOriginRequestTypeDef,
    CreateVpcOriginResultTypeDef,
    DeleteAnycastIpListRequestTypeDef,
    DeleteCachePolicyRequestTypeDef,
    DeleteCloudFrontOriginAccessIdentityRequestTypeDef,
    DeleteContinuousDeploymentPolicyRequestTypeDef,
    DeleteDistributionRequestTypeDef,
    DeleteFieldLevelEncryptionConfigRequestTypeDef,
    DeleteFieldLevelEncryptionProfileRequestTypeDef,
    DeleteFunctionRequestTypeDef,
    DeleteKeyGroupRequestTypeDef,
    DeleteKeyValueStoreRequestTypeDef,
    DeleteMonitoringSubscriptionRequestTypeDef,
    DeleteOriginAccessControlRequestTypeDef,
    DeleteOriginRequestPolicyRequestTypeDef,
    DeletePublicKeyRequestTypeDef,
    DeleteRealtimeLogConfigRequestTypeDef,
    DeleteResponseHeadersPolicyRequestTypeDef,
    DeleteStreamingDistributionRequestTypeDef,
    DeleteVpcOriginRequestTypeDef,
    DeleteVpcOriginResultTypeDef,
    DescribeFunctionRequestTypeDef,
    DescribeFunctionResultTypeDef,
    DescribeKeyValueStoreRequestTypeDef,
    DescribeKeyValueStoreResultTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAnycastIpListRequestTypeDef,
    GetAnycastIpListResultTypeDef,
    GetCachePolicyConfigRequestTypeDef,
    GetCachePolicyConfigResultTypeDef,
    GetCachePolicyRequestTypeDef,
    GetCachePolicyResultTypeDef,
    GetCloudFrontOriginAccessIdentityConfigRequestTypeDef,
    GetCloudFrontOriginAccessIdentityConfigResultTypeDef,
    GetCloudFrontOriginAccessIdentityRequestTypeDef,
    GetCloudFrontOriginAccessIdentityResultTypeDef,
    GetContinuousDeploymentPolicyConfigRequestTypeDef,
    GetContinuousDeploymentPolicyConfigResultTypeDef,
    GetContinuousDeploymentPolicyRequestTypeDef,
    GetContinuousDeploymentPolicyResultTypeDef,
    GetDistributionConfigRequestTypeDef,
    GetDistributionConfigResultTypeDef,
    GetDistributionRequestTypeDef,
    GetDistributionResultTypeDef,
    GetFieldLevelEncryptionConfigRequestTypeDef,
    GetFieldLevelEncryptionConfigResultTypeDef,
    GetFieldLevelEncryptionProfileConfigRequestTypeDef,
    GetFieldLevelEncryptionProfileConfigResultTypeDef,
    GetFieldLevelEncryptionProfileRequestTypeDef,
    GetFieldLevelEncryptionProfileResultTypeDef,
    GetFieldLevelEncryptionRequestTypeDef,
    GetFieldLevelEncryptionResultTypeDef,
    GetFunctionRequestTypeDef,
    GetFunctionResultTypeDef,
    GetInvalidationRequestTypeDef,
    GetInvalidationResultTypeDef,
    GetKeyGroupConfigRequestTypeDef,
    GetKeyGroupConfigResultTypeDef,
    GetKeyGroupRequestTypeDef,
    GetKeyGroupResultTypeDef,
    GetMonitoringSubscriptionRequestTypeDef,
    GetMonitoringSubscriptionResultTypeDef,
    GetOriginAccessControlConfigRequestTypeDef,
    GetOriginAccessControlConfigResultTypeDef,
    GetOriginAccessControlRequestTypeDef,
    GetOriginAccessControlResultTypeDef,
    GetOriginRequestPolicyConfigRequestTypeDef,
    GetOriginRequestPolicyConfigResultTypeDef,
    GetOriginRequestPolicyRequestTypeDef,
    GetOriginRequestPolicyResultTypeDef,
    GetPublicKeyConfigRequestTypeDef,
    GetPublicKeyConfigResultTypeDef,
    GetPublicKeyRequestTypeDef,
    GetPublicKeyResultTypeDef,
    GetRealtimeLogConfigRequestTypeDef,
    GetRealtimeLogConfigResultTypeDef,
    GetResponseHeadersPolicyConfigRequestTypeDef,
    GetResponseHeadersPolicyConfigResultTypeDef,
    GetResponseHeadersPolicyRequestTypeDef,
    GetResponseHeadersPolicyResultTypeDef,
    GetStreamingDistributionConfigRequestTypeDef,
    GetStreamingDistributionConfigResultTypeDef,
    GetStreamingDistributionRequestTypeDef,
    GetStreamingDistributionResultTypeDef,
    GetVpcOriginRequestTypeDef,
    GetVpcOriginResultTypeDef,
    ListAnycastIpListsRequestTypeDef,
    ListAnycastIpListsResultTypeDef,
    ListCachePoliciesRequestTypeDef,
    ListCachePoliciesResultTypeDef,
    ListCloudFrontOriginAccessIdentitiesRequestTypeDef,
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListConflictingAliasesRequestTypeDef,
    ListConflictingAliasesResultTypeDef,
    ListContinuousDeploymentPoliciesRequestTypeDef,
    ListContinuousDeploymentPoliciesResultTypeDef,
    ListDistributionsByAnycastIpListIdRequestTypeDef,
    ListDistributionsByAnycastIpListIdResultTypeDef,
    ListDistributionsByCachePolicyIdRequestTypeDef,
    ListDistributionsByCachePolicyIdResultTypeDef,
    ListDistributionsByKeyGroupRequestTypeDef,
    ListDistributionsByKeyGroupResultTypeDef,
    ListDistributionsByOriginRequestPolicyIdRequestTypeDef,
    ListDistributionsByOriginRequestPolicyIdResultTypeDef,
    ListDistributionsByRealtimeLogConfigRequestTypeDef,
    ListDistributionsByRealtimeLogConfigResultTypeDef,
    ListDistributionsByResponseHeadersPolicyIdRequestTypeDef,
    ListDistributionsByResponseHeadersPolicyIdResultTypeDef,
    ListDistributionsByVpcOriginIdRequestTypeDef,
    ListDistributionsByVpcOriginIdResultTypeDef,
    ListDistributionsByWebACLIdRequestTypeDef,
    ListDistributionsByWebACLIdResultTypeDef,
    ListDistributionsRequestTypeDef,
    ListDistributionsResultTypeDef,
    ListFieldLevelEncryptionConfigsRequestTypeDef,
    ListFieldLevelEncryptionConfigsResultTypeDef,
    ListFieldLevelEncryptionProfilesRequestTypeDef,
    ListFieldLevelEncryptionProfilesResultTypeDef,
    ListFunctionsRequestTypeDef,
    ListFunctionsResultTypeDef,
    ListInvalidationsRequestTypeDef,
    ListInvalidationsResultTypeDef,
    ListKeyGroupsRequestTypeDef,
    ListKeyGroupsResultTypeDef,
    ListKeyValueStoresRequestTypeDef,
    ListKeyValueStoresResultTypeDef,
    ListOriginAccessControlsRequestTypeDef,
    ListOriginAccessControlsResultTypeDef,
    ListOriginRequestPoliciesRequestTypeDef,
    ListOriginRequestPoliciesResultTypeDef,
    ListPublicKeysRequestTypeDef,
    ListPublicKeysResultTypeDef,
    ListRealtimeLogConfigsRequestTypeDef,
    ListRealtimeLogConfigsResultTypeDef,
    ListResponseHeadersPoliciesRequestTypeDef,
    ListResponseHeadersPoliciesResultTypeDef,
    ListStreamingDistributionsRequestTypeDef,
    ListStreamingDistributionsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    ListVpcOriginsRequestTypeDef,
    ListVpcOriginsResultTypeDef,
    PublishFunctionRequestTypeDef,
    PublishFunctionResultTypeDef,
    TagResourceRequestTypeDef,
    TestFunctionRequestTypeDef,
    TestFunctionResultTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCachePolicyRequestTypeDef,
    UpdateCachePolicyResultTypeDef,
    UpdateCloudFrontOriginAccessIdentityRequestTypeDef,
    UpdateCloudFrontOriginAccessIdentityResultTypeDef,
    UpdateContinuousDeploymentPolicyRequestTypeDef,
    UpdateContinuousDeploymentPolicyResultTypeDef,
    UpdateDistributionRequestTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateDistributionWithStagingConfigRequestTypeDef,
    UpdateDistributionWithStagingConfigResultTypeDef,
    UpdateFieldLevelEncryptionConfigRequestTypeDef,
    UpdateFieldLevelEncryptionConfigResultTypeDef,
    UpdateFieldLevelEncryptionProfileRequestTypeDef,
    UpdateFieldLevelEncryptionProfileResultTypeDef,
    UpdateFunctionRequestTypeDef,
    UpdateFunctionResultTypeDef,
    UpdateKeyGroupRequestTypeDef,
    UpdateKeyGroupResultTypeDef,
    UpdateKeyValueStoreRequestTypeDef,
    UpdateKeyValueStoreResultTypeDef,
    UpdateOriginAccessControlRequestTypeDef,
    UpdateOriginAccessControlResultTypeDef,
    UpdateOriginRequestPolicyRequestTypeDef,
    UpdateOriginRequestPolicyResultTypeDef,
    UpdatePublicKeyRequestTypeDef,
    UpdatePublicKeyResultTypeDef,
    UpdateRealtimeLogConfigRequestTypeDef,
    UpdateRealtimeLogConfigResultTypeDef,
    UpdateResponseHeadersPolicyRequestTypeDef,
    UpdateResponseHeadersPolicyResultTypeDef,
    UpdateStreamingDistributionRequestTypeDef,
    UpdateStreamingDistributionResultTypeDef,
    UpdateVpcOriginRequestTypeDef,
    UpdateVpcOriginResultTypeDef,
)
from .waiter import (
    DistributionDeployedWaiter,
    InvalidationCompletedWaiter,
    StreamingDistributionDeployedWaiter,
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


__all__ = ("CloudFrontClient",)


class Exceptions(BaseClientExceptions):
    AccessDenied: Type[BotocoreClientError]
    BatchTooLarge: Type[BotocoreClientError]
    CNAMEAlreadyExists: Type[BotocoreClientError]
    CachePolicyAlreadyExists: Type[BotocoreClientError]
    CachePolicyInUse: Type[BotocoreClientError]
    CannotChangeImmutablePublicKeyFields: Type[BotocoreClientError]
    CannotDeleteEntityWhileInUse: Type[BotocoreClientError]
    CannotUpdateEntityWhileInUse: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CloudFrontOriginAccessIdentityAlreadyExists: Type[BotocoreClientError]
    CloudFrontOriginAccessIdentityInUse: Type[BotocoreClientError]
    ContinuousDeploymentPolicyAlreadyExists: Type[BotocoreClientError]
    ContinuousDeploymentPolicyInUse: Type[BotocoreClientError]
    DistributionAlreadyExists: Type[BotocoreClientError]
    DistributionNotDisabled: Type[BotocoreClientError]
    EntityAlreadyExists: Type[BotocoreClientError]
    EntityLimitExceeded: Type[BotocoreClientError]
    EntityNotFound: Type[BotocoreClientError]
    EntitySizeLimitExceeded: Type[BotocoreClientError]
    FieldLevelEncryptionConfigAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionConfigInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileAlreadyExists: Type[BotocoreClientError]
    FieldLevelEncryptionProfileInUse: Type[BotocoreClientError]
    FieldLevelEncryptionProfileSizeExceeded: Type[BotocoreClientError]
    FunctionAlreadyExists: Type[BotocoreClientError]
    FunctionInUse: Type[BotocoreClientError]
    FunctionSizeLimitExceeded: Type[BotocoreClientError]
    IllegalDelete: Type[BotocoreClientError]
    IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: Type[BotocoreClientError]
    IllegalOriginAccessConfiguration: Type[BotocoreClientError]
    IllegalUpdate: Type[BotocoreClientError]
    InconsistentQuantities: Type[BotocoreClientError]
    InvalidArgument: Type[BotocoreClientError]
    InvalidDefaultRootObject: Type[BotocoreClientError]
    InvalidDomainNameForOriginAccessControl: Type[BotocoreClientError]
    InvalidErrorCode: Type[BotocoreClientError]
    InvalidForwardCookies: Type[BotocoreClientError]
    InvalidFunctionAssociation: Type[BotocoreClientError]
    InvalidGeoRestrictionParameter: Type[BotocoreClientError]
    InvalidHeadersForS3Origin: Type[BotocoreClientError]
    InvalidIfMatchVersion: Type[BotocoreClientError]
    InvalidLambdaFunctionAssociation: Type[BotocoreClientError]
    InvalidLocationCode: Type[BotocoreClientError]
    InvalidMinimumProtocolVersion: Type[BotocoreClientError]
    InvalidOrigin: Type[BotocoreClientError]
    InvalidOriginAccessControl: Type[BotocoreClientError]
    InvalidOriginAccessIdentity: Type[BotocoreClientError]
    InvalidOriginKeepaliveTimeout: Type[BotocoreClientError]
    InvalidOriginReadTimeout: Type[BotocoreClientError]
    InvalidProtocolSettings: Type[BotocoreClientError]
    InvalidQueryStringParameters: Type[BotocoreClientError]
    InvalidRelativePath: Type[BotocoreClientError]
    InvalidRequiredProtocol: Type[BotocoreClientError]
    InvalidResponseCode: Type[BotocoreClientError]
    InvalidTTLOrder: Type[BotocoreClientError]
    InvalidTagging: Type[BotocoreClientError]
    InvalidViewerCertificate: Type[BotocoreClientError]
    InvalidWebACLId: Type[BotocoreClientError]
    KeyGroupAlreadyExists: Type[BotocoreClientError]
    MissingBody: Type[BotocoreClientError]
    MonitoringSubscriptionAlreadyExists: Type[BotocoreClientError]
    NoSuchCachePolicy: Type[BotocoreClientError]
    NoSuchCloudFrontOriginAccessIdentity: Type[BotocoreClientError]
    NoSuchContinuousDeploymentPolicy: Type[BotocoreClientError]
    NoSuchDistribution: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionConfig: Type[BotocoreClientError]
    NoSuchFieldLevelEncryptionProfile: Type[BotocoreClientError]
    NoSuchFunctionExists: Type[BotocoreClientError]
    NoSuchInvalidation: Type[BotocoreClientError]
    NoSuchMonitoringSubscription: Type[BotocoreClientError]
    NoSuchOrigin: Type[BotocoreClientError]
    NoSuchOriginAccessControl: Type[BotocoreClientError]
    NoSuchOriginRequestPolicy: Type[BotocoreClientError]
    NoSuchPublicKey: Type[BotocoreClientError]
    NoSuchRealtimeLogConfig: Type[BotocoreClientError]
    NoSuchResource: Type[BotocoreClientError]
    NoSuchResponseHeadersPolicy: Type[BotocoreClientError]
    NoSuchStreamingDistribution: Type[BotocoreClientError]
    OriginAccessControlAlreadyExists: Type[BotocoreClientError]
    OriginAccessControlInUse: Type[BotocoreClientError]
    OriginRequestPolicyAlreadyExists: Type[BotocoreClientError]
    OriginRequestPolicyInUse: Type[BotocoreClientError]
    PreconditionFailed: Type[BotocoreClientError]
    PublicKeyAlreadyExists: Type[BotocoreClientError]
    PublicKeyInUse: Type[BotocoreClientError]
    QueryArgProfileEmpty: Type[BotocoreClientError]
    RealtimeLogConfigAlreadyExists: Type[BotocoreClientError]
    RealtimeLogConfigInUse: Type[BotocoreClientError]
    RealtimeLogConfigOwnerMismatch: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResponseHeadersPolicyAlreadyExists: Type[BotocoreClientError]
    ResponseHeadersPolicyInUse: Type[BotocoreClientError]
    StagingDistributionInUse: Type[BotocoreClientError]
    StreamingDistributionAlreadyExists: Type[BotocoreClientError]
    StreamingDistributionNotDisabled: Type[BotocoreClientError]
    TestFunctionFailed: Type[BotocoreClientError]
    TooLongCSPInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyCacheBehaviors: Type[BotocoreClientError]
    TooManyCachePolicies: Type[BotocoreClientError]
    TooManyCertificates: Type[BotocoreClientError]
    TooManyCloudFrontOriginAccessIdentities: Type[BotocoreClientError]
    TooManyContinuousDeploymentPolicies: Type[BotocoreClientError]
    TooManyCookieNamesInWhiteList: Type[BotocoreClientError]
    TooManyCookiesInCachePolicy: Type[BotocoreClientError]
    TooManyCookiesInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyCustomHeadersInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyDistributionCNAMEs: Type[BotocoreClientError]
    TooManyDistributions: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToCachePolicy: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToKeyGroup: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToOriginAccessControl: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToOriginRequestPolicy: Type[BotocoreClientError]
    TooManyDistributionsAssociatedToResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyDistributionsWithFunctionAssociations: Type[BotocoreClientError]
    TooManyDistributionsWithLambdaAssociations: Type[BotocoreClientError]
    TooManyDistributionsWithSingleFunctionARN: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionConfigs: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionContentTypeProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionEncryptionEntities: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionFieldPatterns: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionProfiles: Type[BotocoreClientError]
    TooManyFieldLevelEncryptionQueryArgProfiles: Type[BotocoreClientError]
    TooManyFunctionAssociations: Type[BotocoreClientError]
    TooManyFunctions: Type[BotocoreClientError]
    TooManyHeadersInCachePolicy: Type[BotocoreClientError]
    TooManyHeadersInForwardedValues: Type[BotocoreClientError]
    TooManyHeadersInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyInvalidationsInProgress: Type[BotocoreClientError]
    TooManyKeyGroups: Type[BotocoreClientError]
    TooManyKeyGroupsAssociatedToDistribution: Type[BotocoreClientError]
    TooManyLambdaFunctionAssociations: Type[BotocoreClientError]
    TooManyOriginAccessControls: Type[BotocoreClientError]
    TooManyOriginCustomHeaders: Type[BotocoreClientError]
    TooManyOriginGroupsPerDistribution: Type[BotocoreClientError]
    TooManyOriginRequestPolicies: Type[BotocoreClientError]
    TooManyOrigins: Type[BotocoreClientError]
    TooManyPublicKeys: Type[BotocoreClientError]
    TooManyPublicKeysInKeyGroup: Type[BotocoreClientError]
    TooManyQueryStringParameters: Type[BotocoreClientError]
    TooManyQueryStringsInCachePolicy: Type[BotocoreClientError]
    TooManyQueryStringsInOriginRequestPolicy: Type[BotocoreClientError]
    TooManyRealtimeLogConfigs: Type[BotocoreClientError]
    TooManyRemoveHeadersInResponseHeadersPolicy: Type[BotocoreClientError]
    TooManyResponseHeadersPolicies: Type[BotocoreClientError]
    TooManyStreamingDistributionCNAMEs: Type[BotocoreClientError]
    TooManyStreamingDistributions: Type[BotocoreClientError]
    TooManyTrustedSigners: Type[BotocoreClientError]
    TrustedKeyGroupDoesNotExist: Type[BotocoreClientError]
    TrustedSignerDoesNotExist: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class CloudFrontClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudFrontClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#generate_presigned_url)
        """

    async def associate_alias(
        self, **kwargs: Unpack[AssociateAliasRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an alias (also known as a CNAME or an alternate domain name) with a
        CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/associate_alias.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#associate_alias)
        """

    async def copy_distribution(
        self, **kwargs: Unpack[CopyDistributionRequestTypeDef]
    ) -> CopyDistributionResultTypeDef:
        """
        Creates a staging distribution using the configuration of the provided primary
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/copy_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#copy_distribution)
        """

    async def create_anycast_ip_list(
        self, **kwargs: Unpack[CreateAnycastIpListRequestTypeDef]
    ) -> CreateAnycastIpListResultTypeDef:
        """
        Creates an Anycast static IP list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_anycast_ip_list.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_anycast_ip_list)
        """

    async def create_cache_policy(
        self, **kwargs: Unpack[CreateCachePolicyRequestTypeDef]
    ) -> CreateCachePolicyResultTypeDef:
        """
        Creates a cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_cache_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_cache_policy)
        """

    async def create_cloud_front_origin_access_identity(
        self, **kwargs: Unpack[CreateCloudFrontOriginAccessIdentityRequestTypeDef]
    ) -> CreateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Creates a new origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_cloud_front_origin_access_identity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_cloud_front_origin_access_identity)
        """

    async def create_continuous_deployment_policy(
        self, **kwargs: Unpack[CreateContinuousDeploymentPolicyRequestTypeDef]
    ) -> CreateContinuousDeploymentPolicyResultTypeDef:
        """
        Creates a continuous deployment policy that distributes traffic for a custom
        domain name to two different CloudFront distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_continuous_deployment_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_continuous_deployment_policy)
        """

    async def create_distribution(
        self, **kwargs: Unpack[CreateDistributionRequestTypeDef]
    ) -> CreateDistributionResultTypeDef:
        """
        Creates a CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_distribution)
        """

    async def create_distribution_with_tags(
        self, **kwargs: Unpack[CreateDistributionWithTagsRequestTypeDef]
    ) -> CreateDistributionWithTagsResultTypeDef:
        """
        Create a new distribution with tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_distribution_with_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_distribution_with_tags)
        """

    async def create_field_level_encryption_config(
        self, **kwargs: Unpack[CreateFieldLevelEncryptionConfigRequestTypeDef]
    ) -> CreateFieldLevelEncryptionConfigResultTypeDef:
        """
        Create a new field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_field_level_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_field_level_encryption_config)
        """

    async def create_field_level_encryption_profile(
        self, **kwargs: Unpack[CreateFieldLevelEncryptionProfileRequestTypeDef]
    ) -> CreateFieldLevelEncryptionProfileResultTypeDef:
        """
        Create a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_field_level_encryption_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_field_level_encryption_profile)
        """

    async def create_function(
        self, **kwargs: Unpack[CreateFunctionRequestTypeDef]
    ) -> CreateFunctionResultTypeDef:
        """
        Creates a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_function)
        """

    async def create_invalidation(
        self, **kwargs: Unpack[CreateInvalidationRequestTypeDef]
    ) -> CreateInvalidationResultTypeDef:
        """
        Create a new invalidation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_invalidation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_invalidation)
        """

    async def create_key_group(
        self, **kwargs: Unpack[CreateKeyGroupRequestTypeDef]
    ) -> CreateKeyGroupResultTypeDef:
        """
        Creates a key group that you can use with <a
        href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">CloudFront
        signed URLs and signed cookies</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_key_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_key_group)
        """

    async def create_key_value_store(
        self, **kwargs: Unpack[CreateKeyValueStoreRequestTypeDef]
    ) -> CreateKeyValueStoreResultTypeDef:
        """
        Specifies the key value store resource to add to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_key_value_store.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_key_value_store)
        """

    async def create_monitoring_subscription(
        self, **kwargs: Unpack[CreateMonitoringSubscriptionRequestTypeDef]
    ) -> CreateMonitoringSubscriptionResultTypeDef:
        """
        Enables additional CloudWatch metrics for the specified CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_monitoring_subscription.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_monitoring_subscription)
        """

    async def create_origin_access_control(
        self, **kwargs: Unpack[CreateOriginAccessControlRequestTypeDef]
    ) -> CreateOriginAccessControlResultTypeDef:
        """
        Creates a new origin access control in CloudFront.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_origin_access_control.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_origin_access_control)
        """

    async def create_origin_request_policy(
        self, **kwargs: Unpack[CreateOriginRequestPolicyRequestTypeDef]
    ) -> CreateOriginRequestPolicyResultTypeDef:
        """
        Creates an origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_origin_request_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_origin_request_policy)
        """

    async def create_public_key(
        self, **kwargs: Unpack[CreatePublicKeyRequestTypeDef]
    ) -> CreatePublicKeyResultTypeDef:
        """
        Uploads a public key to CloudFront that you can use with <a
        href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">signed
        URLs and signed cookies</a>, or with <a
        href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption....

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_public_key)
        """

    async def create_realtime_log_config(
        self, **kwargs: Unpack[CreateRealtimeLogConfigRequestTypeDef]
    ) -> CreateRealtimeLogConfigResultTypeDef:
        """
        Creates a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_realtime_log_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_realtime_log_config)
        """

    async def create_response_headers_policy(
        self, **kwargs: Unpack[CreateResponseHeadersPolicyRequestTypeDef]
    ) -> CreateResponseHeadersPolicyResultTypeDef:
        """
        Creates a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_response_headers_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_response_headers_policy)
        """

    async def create_streaming_distribution(
        self, **kwargs: Unpack[CreateStreamingDistributionRequestTypeDef]
    ) -> CreateStreamingDistributionResultTypeDef:
        """
        This API is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_streaming_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_streaming_distribution)
        """

    async def create_streaming_distribution_with_tags(
        self, **kwargs: Unpack[CreateStreamingDistributionWithTagsRequestTypeDef]
    ) -> CreateStreamingDistributionWithTagsResultTypeDef:
        """
        This API is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_streaming_distribution_with_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_streaming_distribution_with_tags)
        """

    async def create_vpc_origin(
        self, **kwargs: Unpack[CreateVpcOriginRequestTypeDef]
    ) -> CreateVpcOriginResultTypeDef:
        """
        Create an Amazon CloudFront VPC origin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/create_vpc_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#create_vpc_origin)
        """

    async def delete_anycast_ip_list(
        self, **kwargs: Unpack[DeleteAnycastIpListRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Anycast static IP list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_anycast_ip_list.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_anycast_ip_list)
        """

    async def delete_cache_policy(
        self, **kwargs: Unpack[DeleteCachePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_cache_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_cache_policy)
        """

    async def delete_cloud_front_origin_access_identity(
        self, **kwargs: Unpack[DeleteCloudFrontOriginAccessIdentityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_cloud_front_origin_access_identity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_cloud_front_origin_access_identity)
        """

    async def delete_continuous_deployment_policy(
        self, **kwargs: Unpack[DeleteContinuousDeploymentPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_continuous_deployment_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_continuous_deployment_policy)
        """

    async def delete_distribution(
        self, **kwargs: Unpack[DeleteDistributionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_distribution)
        """

    async def delete_field_level_encryption_config(
        self, **kwargs: Unpack[DeleteFieldLevelEncryptionConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove a field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_field_level_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_field_level_encryption_config)
        """

    async def delete_field_level_encryption_profile(
        self, **kwargs: Unpack[DeleteFieldLevelEncryptionProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_field_level_encryption_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_field_level_encryption_profile)
        """

    async def delete_function(
        self, **kwargs: Unpack[DeleteFunctionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_function)
        """

    async def delete_key_group(
        self, **kwargs: Unpack[DeleteKeyGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_key_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_key_group)
        """

    async def delete_key_value_store(
        self, **kwargs: Unpack[DeleteKeyValueStoreRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Specifies the key value store to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_key_value_store.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_key_value_store)
        """

    async def delete_monitoring_subscription(
        self, **kwargs: Unpack[DeleteMonitoringSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disables additional CloudWatch metrics for the specified CloudFront
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_monitoring_subscription.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_monitoring_subscription)
        """

    async def delete_origin_access_control(
        self, **kwargs: Unpack[DeleteOriginAccessControlRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a CloudFront origin access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_origin_access_control.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_origin_access_control)
        """

    async def delete_origin_request_policy(
        self, **kwargs: Unpack[DeleteOriginRequestPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_origin_request_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_origin_request_policy)
        """

    async def delete_public_key(
        self, **kwargs: Unpack[DeletePublicKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove a public key you previously added to CloudFront.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_public_key)
        """

    async def delete_realtime_log_config(
        self, **kwargs: Unpack[DeleteRealtimeLogConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_realtime_log_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_realtime_log_config)
        """

    async def delete_response_headers_policy(
        self, **kwargs: Unpack[DeleteResponseHeadersPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_response_headers_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_response_headers_policy)
        """

    async def delete_streaming_distribution(
        self, **kwargs: Unpack[DeleteStreamingDistributionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_streaming_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_streaming_distribution)
        """

    async def delete_vpc_origin(
        self, **kwargs: Unpack[DeleteVpcOriginRequestTypeDef]
    ) -> DeleteVpcOriginResultTypeDef:
        """
        Delete an Amazon CloudFront VPC origin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/delete_vpc_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#delete_vpc_origin)
        """

    async def describe_function(
        self, **kwargs: Unpack[DescribeFunctionRequestTypeDef]
    ) -> DescribeFunctionResultTypeDef:
        """
        Gets configuration information and metadata about a CloudFront function, but
        not the function's code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/describe_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#describe_function)
        """

    async def describe_key_value_store(
        self, **kwargs: Unpack[DescribeKeyValueStoreRequestTypeDef]
    ) -> DescribeKeyValueStoreResultTypeDef:
        """
        Specifies the key value store and its configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/describe_key_value_store.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#describe_key_value_store)
        """

    async def get_anycast_ip_list(
        self, **kwargs: Unpack[GetAnycastIpListRequestTypeDef]
    ) -> GetAnycastIpListResultTypeDef:
        """
        Gets an Anycast static IP list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_anycast_ip_list.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_anycast_ip_list)
        """

    async def get_cache_policy(
        self, **kwargs: Unpack[GetCachePolicyRequestTypeDef]
    ) -> GetCachePolicyResultTypeDef:
        """
        Gets a cache policy, including the following metadata:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_cache_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_cache_policy)
        """

    async def get_cache_policy_config(
        self, **kwargs: Unpack[GetCachePolicyConfigRequestTypeDef]
    ) -> GetCachePolicyConfigResultTypeDef:
        """
        Gets a cache policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_cache_policy_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_cache_policy_config)
        """

    async def get_cloud_front_origin_access_identity(
        self, **kwargs: Unpack[GetCloudFrontOriginAccessIdentityRequestTypeDef]
    ) -> GetCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Get the information about an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_cloud_front_origin_access_identity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_cloud_front_origin_access_identity)
        """

    async def get_cloud_front_origin_access_identity_config(
        self, **kwargs: Unpack[GetCloudFrontOriginAccessIdentityConfigRequestTypeDef]
    ) -> GetCloudFrontOriginAccessIdentityConfigResultTypeDef:
        """
        Get the configuration information about an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_cloud_front_origin_access_identity_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_cloud_front_origin_access_identity_config)
        """

    async def get_continuous_deployment_policy(
        self, **kwargs: Unpack[GetContinuousDeploymentPolicyRequestTypeDef]
    ) -> GetContinuousDeploymentPolicyResultTypeDef:
        """
        Gets a continuous deployment policy, including metadata (the policy's
        identifier and the date and time when the policy was last modified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_continuous_deployment_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_continuous_deployment_policy)
        """

    async def get_continuous_deployment_policy_config(
        self, **kwargs: Unpack[GetContinuousDeploymentPolicyConfigRequestTypeDef]
    ) -> GetContinuousDeploymentPolicyConfigResultTypeDef:
        """
        Gets configuration information about a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_continuous_deployment_policy_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_continuous_deployment_policy_config)
        """

    async def get_distribution(
        self, **kwargs: Unpack[GetDistributionRequestTypeDef]
    ) -> GetDistributionResultTypeDef:
        """
        Get the information about a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_distribution)
        """

    async def get_distribution_config(
        self, **kwargs: Unpack[GetDistributionConfigRequestTypeDef]
    ) -> GetDistributionConfigResultTypeDef:
        """
        Get the configuration information about a distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_distribution_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_distribution_config)
        """

    async def get_field_level_encryption(
        self, **kwargs: Unpack[GetFieldLevelEncryptionRequestTypeDef]
    ) -> GetFieldLevelEncryptionResultTypeDef:
        """
        Get the field-level encryption configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_field_level_encryption.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_field_level_encryption)
        """

    async def get_field_level_encryption_config(
        self, **kwargs: Unpack[GetFieldLevelEncryptionConfigRequestTypeDef]
    ) -> GetFieldLevelEncryptionConfigResultTypeDef:
        """
        Get the field-level encryption configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_field_level_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_field_level_encryption_config)
        """

    async def get_field_level_encryption_profile(
        self, **kwargs: Unpack[GetFieldLevelEncryptionProfileRequestTypeDef]
    ) -> GetFieldLevelEncryptionProfileResultTypeDef:
        """
        Get the field-level encryption profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_field_level_encryption_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_field_level_encryption_profile)
        """

    async def get_field_level_encryption_profile_config(
        self, **kwargs: Unpack[GetFieldLevelEncryptionProfileConfigRequestTypeDef]
    ) -> GetFieldLevelEncryptionProfileConfigResultTypeDef:
        """
        Get the field-level encryption profile configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_field_level_encryption_profile_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_field_level_encryption_profile_config)
        """

    async def get_function(
        self, **kwargs: Unpack[GetFunctionRequestTypeDef]
    ) -> GetFunctionResultTypeDef:
        """
        Gets the code of a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_function)
        """

    async def get_invalidation(
        self, **kwargs: Unpack[GetInvalidationRequestTypeDef]
    ) -> GetInvalidationResultTypeDef:
        """
        Get the information about an invalidation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_invalidation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_invalidation)
        """

    async def get_key_group(
        self, **kwargs: Unpack[GetKeyGroupRequestTypeDef]
    ) -> GetKeyGroupResultTypeDef:
        """
        Gets a key group, including the date and time when the key group was last
        modified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_key_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_key_group)
        """

    async def get_key_group_config(
        self, **kwargs: Unpack[GetKeyGroupConfigRequestTypeDef]
    ) -> GetKeyGroupConfigResultTypeDef:
        """
        Gets a key group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_key_group_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_key_group_config)
        """

    async def get_monitoring_subscription(
        self, **kwargs: Unpack[GetMonitoringSubscriptionRequestTypeDef]
    ) -> GetMonitoringSubscriptionResultTypeDef:
        """
        Gets information about whether additional CloudWatch metrics are enabled for
        the specified CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_monitoring_subscription.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_monitoring_subscription)
        """

    async def get_origin_access_control(
        self, **kwargs: Unpack[GetOriginAccessControlRequestTypeDef]
    ) -> GetOriginAccessControlResultTypeDef:
        """
        Gets a CloudFront origin access control, including its unique identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_origin_access_control.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_origin_access_control)
        """

    async def get_origin_access_control_config(
        self, **kwargs: Unpack[GetOriginAccessControlConfigRequestTypeDef]
    ) -> GetOriginAccessControlConfigResultTypeDef:
        """
        Gets a CloudFront origin access control configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_origin_access_control_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_origin_access_control_config)
        """

    async def get_origin_request_policy(
        self, **kwargs: Unpack[GetOriginRequestPolicyRequestTypeDef]
    ) -> GetOriginRequestPolicyResultTypeDef:
        """
        Gets an origin request policy, including the following metadata:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_origin_request_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_origin_request_policy)
        """

    async def get_origin_request_policy_config(
        self, **kwargs: Unpack[GetOriginRequestPolicyConfigRequestTypeDef]
    ) -> GetOriginRequestPolicyConfigResultTypeDef:
        """
        Gets an origin request policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_origin_request_policy_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_origin_request_policy_config)
        """

    async def get_public_key(
        self, **kwargs: Unpack[GetPublicKeyRequestTypeDef]
    ) -> GetPublicKeyResultTypeDef:
        """
        Gets a public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_public_key)
        """

    async def get_public_key_config(
        self, **kwargs: Unpack[GetPublicKeyConfigRequestTypeDef]
    ) -> GetPublicKeyConfigResultTypeDef:
        """
        Gets a public key configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_public_key_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_public_key_config)
        """

    async def get_realtime_log_config(
        self, **kwargs: Unpack[GetRealtimeLogConfigRequestTypeDef]
    ) -> GetRealtimeLogConfigResultTypeDef:
        """
        Gets a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_realtime_log_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_realtime_log_config)
        """

    async def get_response_headers_policy(
        self, **kwargs: Unpack[GetResponseHeadersPolicyRequestTypeDef]
    ) -> GetResponseHeadersPolicyResultTypeDef:
        """
        Gets a response headers policy, including metadata (the policy's identifier and
        the date and time when the policy was last modified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_response_headers_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_response_headers_policy)
        """

    async def get_response_headers_policy_config(
        self, **kwargs: Unpack[GetResponseHeadersPolicyConfigRequestTypeDef]
    ) -> GetResponseHeadersPolicyConfigResultTypeDef:
        """
        Gets a response headers policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_response_headers_policy_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_response_headers_policy_config)
        """

    async def get_streaming_distribution(
        self, **kwargs: Unpack[GetStreamingDistributionRequestTypeDef]
    ) -> GetStreamingDistributionResultTypeDef:
        """
        Gets information about a specified RTMP distribution, including the
        distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_streaming_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_streaming_distribution)
        """

    async def get_streaming_distribution_config(
        self, **kwargs: Unpack[GetStreamingDistributionConfigRequestTypeDef]
    ) -> GetStreamingDistributionConfigResultTypeDef:
        """
        Get the configuration information about a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_streaming_distribution_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_streaming_distribution_config)
        """

    async def get_vpc_origin(
        self, **kwargs: Unpack[GetVpcOriginRequestTypeDef]
    ) -> GetVpcOriginResultTypeDef:
        """
        Get the details of an Amazon CloudFront VPC origin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_vpc_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_vpc_origin)
        """

    async def list_anycast_ip_lists(
        self, **kwargs: Unpack[ListAnycastIpListsRequestTypeDef]
    ) -> ListAnycastIpListsResultTypeDef:
        """
        Lists your Anycast static IP lists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_anycast_ip_lists.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_anycast_ip_lists)
        """

    async def list_cache_policies(
        self, **kwargs: Unpack[ListCachePoliciesRequestTypeDef]
    ) -> ListCachePoliciesResultTypeDef:
        """
        Gets a list of cache policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_cache_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_cache_policies)
        """

    async def list_cloud_front_origin_access_identities(
        self, **kwargs: Unpack[ListCloudFrontOriginAccessIdentitiesRequestTypeDef]
    ) -> ListCloudFrontOriginAccessIdentitiesResultTypeDef:
        """
        Lists origin access identities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_cloud_front_origin_access_identities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_cloud_front_origin_access_identities)
        """

    async def list_conflicting_aliases(
        self, **kwargs: Unpack[ListConflictingAliasesRequestTypeDef]
    ) -> ListConflictingAliasesResultTypeDef:
        """
        Gets a list of aliases (also called CNAMEs or alternate domain names) that
        conflict or overlap with the provided alias, and the associated CloudFront
        distributions and Amazon Web Services accounts for each conflicting alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_conflicting_aliases.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_conflicting_aliases)
        """

    async def list_continuous_deployment_policies(
        self, **kwargs: Unpack[ListContinuousDeploymentPoliciesRequestTypeDef]
    ) -> ListContinuousDeploymentPoliciesResultTypeDef:
        """
        Gets a list of the continuous deployment policies in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_continuous_deployment_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_continuous_deployment_policies)
        """

    async def list_distributions(
        self, **kwargs: Unpack[ListDistributionsRequestTypeDef]
    ) -> ListDistributionsResultTypeDef:
        """
        List CloudFront distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions)
        """

    async def list_distributions_by_anycast_ip_list_id(
        self, **kwargs: Unpack[ListDistributionsByAnycastIpListIdRequestTypeDef]
    ) -> ListDistributionsByAnycastIpListIdResultTypeDef:
        """
        Lists the distributions in your account that are associated with the specified
        <code>AnycastIpListId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_anycast_ip_list_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_anycast_ip_list_id)
        """

    async def list_distributions_by_cache_policy_id(
        self, **kwargs: Unpack[ListDistributionsByCachePolicyIdRequestTypeDef]
    ) -> ListDistributionsByCachePolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified cache policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_cache_policy_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_cache_policy_id)
        """

    async def list_distributions_by_key_group(
        self, **kwargs: Unpack[ListDistributionsByKeyGroupRequestTypeDef]
    ) -> ListDistributionsByKeyGroupResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that references the specified key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_key_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_key_group)
        """

    async def list_distributions_by_origin_request_policy_id(
        self, **kwargs: Unpack[ListDistributionsByOriginRequestPolicyIdRequestTypeDef]
    ) -> ListDistributionsByOriginRequestPolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified origin request policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_origin_request_policy_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_origin_request_policy_id)
        """

    async def list_distributions_by_realtime_log_config(
        self, **kwargs: Unpack[ListDistributionsByRealtimeLogConfigRequestTypeDef]
    ) -> ListDistributionsByRealtimeLogConfigResultTypeDef:
        """
        Gets a list of distributions that have a cache behavior that's associated with
        the specified real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_realtime_log_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_realtime_log_config)
        """

    async def list_distributions_by_response_headers_policy_id(
        self, **kwargs: Unpack[ListDistributionsByResponseHeadersPolicyIdRequestTypeDef]
    ) -> ListDistributionsByResponseHeadersPolicyIdResultTypeDef:
        """
        Gets a list of distribution IDs for distributions that have a cache behavior
        that's associated with the specified response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_response_headers_policy_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_response_headers_policy_id)
        """

    async def list_distributions_by_vpc_origin_id(
        self, **kwargs: Unpack[ListDistributionsByVpcOriginIdRequestTypeDef]
    ) -> ListDistributionsByVpcOriginIdResultTypeDef:
        """
        List CloudFront distributions by their VPC origin ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_vpc_origin_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_vpc_origin_id)
        """

    async def list_distributions_by_web_acl_id(
        self, **kwargs: Unpack[ListDistributionsByWebACLIdRequestTypeDef]
    ) -> ListDistributionsByWebACLIdResultTypeDef:
        """
        List the distributions that are associated with a specified WAF web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_distributions_by_web_acl_id.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_distributions_by_web_acl_id)
        """

    async def list_field_level_encryption_configs(
        self, **kwargs: Unpack[ListFieldLevelEncryptionConfigsRequestTypeDef]
    ) -> ListFieldLevelEncryptionConfigsResultTypeDef:
        """
        List all field-level encryption configurations that have been created in
        CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_field_level_encryption_configs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_field_level_encryption_configs)
        """

    async def list_field_level_encryption_profiles(
        self, **kwargs: Unpack[ListFieldLevelEncryptionProfilesRequestTypeDef]
    ) -> ListFieldLevelEncryptionProfilesResultTypeDef:
        """
        Request a list of field-level encryption profiles that have been created in
        CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_field_level_encryption_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_field_level_encryption_profiles)
        """

    async def list_functions(
        self, **kwargs: Unpack[ListFunctionsRequestTypeDef]
    ) -> ListFunctionsResultTypeDef:
        """
        Gets a list of all CloudFront functions in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_functions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_functions)
        """

    async def list_invalidations(
        self, **kwargs: Unpack[ListInvalidationsRequestTypeDef]
    ) -> ListInvalidationsResultTypeDef:
        """
        Lists invalidation batches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_invalidations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_invalidations)
        """

    async def list_key_groups(
        self, **kwargs: Unpack[ListKeyGroupsRequestTypeDef]
    ) -> ListKeyGroupsResultTypeDef:
        """
        Gets a list of key groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_key_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_key_groups)
        """

    async def list_key_value_stores(
        self, **kwargs: Unpack[ListKeyValueStoresRequestTypeDef]
    ) -> ListKeyValueStoresResultTypeDef:
        """
        Specifies the key value stores to list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_key_value_stores.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_key_value_stores)
        """

    async def list_origin_access_controls(
        self, **kwargs: Unpack[ListOriginAccessControlsRequestTypeDef]
    ) -> ListOriginAccessControlsResultTypeDef:
        """
        Gets the list of CloudFront origin access controls (OACs) in this Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_origin_access_controls.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_origin_access_controls)
        """

    async def list_origin_request_policies(
        self, **kwargs: Unpack[ListOriginRequestPoliciesRequestTypeDef]
    ) -> ListOriginRequestPoliciesResultTypeDef:
        """
        Gets a list of origin request policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_origin_request_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_origin_request_policies)
        """

    async def list_public_keys(
        self, **kwargs: Unpack[ListPublicKeysRequestTypeDef]
    ) -> ListPublicKeysResultTypeDef:
        """
        List all public keys that have been added to CloudFront for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_public_keys.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_public_keys)
        """

    async def list_realtime_log_configs(
        self, **kwargs: Unpack[ListRealtimeLogConfigsRequestTypeDef]
    ) -> ListRealtimeLogConfigsResultTypeDef:
        """
        Gets a list of real-time log configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_realtime_log_configs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_realtime_log_configs)
        """

    async def list_response_headers_policies(
        self, **kwargs: Unpack[ListResponseHeadersPoliciesRequestTypeDef]
    ) -> ListResponseHeadersPoliciesResultTypeDef:
        """
        Gets a list of response headers policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_response_headers_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_response_headers_policies)
        """

    async def list_streaming_distributions(
        self, **kwargs: Unpack[ListStreamingDistributionsRequestTypeDef]
    ) -> ListStreamingDistributionsResultTypeDef:
        """
        List streaming distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_streaming_distributions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_streaming_distributions)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        List tags for a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_tags_for_resource)
        """

    async def list_vpc_origins(
        self, **kwargs: Unpack[ListVpcOriginsRequestTypeDef]
    ) -> ListVpcOriginsResultTypeDef:
        """
        List the CloudFront VPC origins in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/list_vpc_origins.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#list_vpc_origins)
        """

    async def publish_function(
        self, **kwargs: Unpack[PublishFunctionRequestTypeDef]
    ) -> PublishFunctionResultTypeDef:
        """
        Publishes a CloudFront function by copying the function code from the
        <code>DEVELOPMENT</code> stage to <code>LIVE</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/publish_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#publish_function)
        """

    async def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Add tags to a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#tag_resource)
        """

    async def test_function(
        self, **kwargs: Unpack[TestFunctionRequestTypeDef]
    ) -> TestFunctionResultTypeDef:
        """
        Tests a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/test_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#test_function)
        """

    async def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove tags from a CloudFront resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#untag_resource)
        """

    async def update_cache_policy(
        self, **kwargs: Unpack[UpdateCachePolicyRequestTypeDef]
    ) -> UpdateCachePolicyResultTypeDef:
        """
        Updates a cache policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_cache_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_cache_policy)
        """

    async def update_cloud_front_origin_access_identity(
        self, **kwargs: Unpack[UpdateCloudFrontOriginAccessIdentityRequestTypeDef]
    ) -> UpdateCloudFrontOriginAccessIdentityResultTypeDef:
        """
        Update an origin access identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_cloud_front_origin_access_identity.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_cloud_front_origin_access_identity)
        """

    async def update_continuous_deployment_policy(
        self, **kwargs: Unpack[UpdateContinuousDeploymentPolicyRequestTypeDef]
    ) -> UpdateContinuousDeploymentPolicyResultTypeDef:
        """
        Updates a continuous deployment policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_continuous_deployment_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_continuous_deployment_policy)
        """

    async def update_distribution(
        self, **kwargs: Unpack[UpdateDistributionRequestTypeDef]
    ) -> UpdateDistributionResultTypeDef:
        """
        Updates the configuration for a CloudFront distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_distribution)
        """

    async def update_distribution_with_staging_config(
        self, **kwargs: Unpack[UpdateDistributionWithStagingConfigRequestTypeDef]
    ) -> UpdateDistributionWithStagingConfigResultTypeDef:
        """
        Copies the staging distribution's configuration to its corresponding primary
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_distribution_with_staging_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_distribution_with_staging_config)
        """

    async def update_field_level_encryption_config(
        self, **kwargs: Unpack[UpdateFieldLevelEncryptionConfigRequestTypeDef]
    ) -> UpdateFieldLevelEncryptionConfigResultTypeDef:
        """
        Update a field-level encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_field_level_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_field_level_encryption_config)
        """

    async def update_field_level_encryption_profile(
        self, **kwargs: Unpack[UpdateFieldLevelEncryptionProfileRequestTypeDef]
    ) -> UpdateFieldLevelEncryptionProfileResultTypeDef:
        """
        Update a field-level encryption profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_field_level_encryption_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_field_level_encryption_profile)
        """

    async def update_function(
        self, **kwargs: Unpack[UpdateFunctionRequestTypeDef]
    ) -> UpdateFunctionResultTypeDef:
        """
        Updates a CloudFront function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_function)
        """

    async def update_key_group(
        self, **kwargs: Unpack[UpdateKeyGroupRequestTypeDef]
    ) -> UpdateKeyGroupResultTypeDef:
        """
        Updates a key group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_key_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_key_group)
        """

    async def update_key_value_store(
        self, **kwargs: Unpack[UpdateKeyValueStoreRequestTypeDef]
    ) -> UpdateKeyValueStoreResultTypeDef:
        """
        Specifies the key value store to update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_key_value_store.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_key_value_store)
        """

    async def update_origin_access_control(
        self, **kwargs: Unpack[UpdateOriginAccessControlRequestTypeDef]
    ) -> UpdateOriginAccessControlResultTypeDef:
        """
        Updates a CloudFront origin access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_origin_access_control.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_origin_access_control)
        """

    async def update_origin_request_policy(
        self, **kwargs: Unpack[UpdateOriginRequestPolicyRequestTypeDef]
    ) -> UpdateOriginRequestPolicyResultTypeDef:
        """
        Updates an origin request policy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_origin_request_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_origin_request_policy)
        """

    async def update_public_key(
        self, **kwargs: Unpack[UpdatePublicKeyRequestTypeDef]
    ) -> UpdatePublicKeyResultTypeDef:
        """
        Update public key information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_public_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_public_key)
        """

    async def update_realtime_log_config(
        self, **kwargs: Unpack[UpdateRealtimeLogConfigRequestTypeDef]
    ) -> UpdateRealtimeLogConfigResultTypeDef:
        """
        Updates a real-time log configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_realtime_log_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_realtime_log_config)
        """

    async def update_response_headers_policy(
        self, **kwargs: Unpack[UpdateResponseHeadersPolicyRequestTypeDef]
    ) -> UpdateResponseHeadersPolicyResultTypeDef:
        """
        Updates a response headers policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_response_headers_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_response_headers_policy)
        """

    async def update_streaming_distribution(
        self, **kwargs: Unpack[UpdateStreamingDistributionRequestTypeDef]
    ) -> UpdateStreamingDistributionResultTypeDef:
        """
        Update a streaming distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_streaming_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_streaming_distribution)
        """

    async def update_vpc_origin(
        self, **kwargs: Unpack[UpdateVpcOriginRequestTypeDef]
    ) -> UpdateVpcOriginResultTypeDef:
        """
        Update an Amazon CloudFront VPC origin in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/update_vpc_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#update_vpc_origin)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cloud_front_origin_access_identities"]
    ) -> ListCloudFrontOriginAccessIdentitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_distributions"]
    ) -> ListDistributionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_invalidations"]
    ) -> ListInvalidationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_key_value_stores"]
    ) -> ListKeyValueStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_public_keys"]
    ) -> ListPublicKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_streaming_distributions"]
    ) -> ListStreamingDistributionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["distribution_deployed"]
    ) -> DistributionDeployedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["invalidation_completed"]
    ) -> InvalidationCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["streaming_distribution_deployed"]
    ) -> StreamingDistributionDeployedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/client/)
        """
