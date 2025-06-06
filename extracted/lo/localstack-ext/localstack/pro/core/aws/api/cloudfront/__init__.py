from datetime import datetime
from enum import StrEnum
from typing import IO, Iterable, List, Optional, TypedDict, Union

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AnycastIpListName = str
CommentType = str
CreateDistributionTenantRequestNameString = str
FunctionARN = str
FunctionName = str
KeyValueStoreARN = str
KeyValueStoreComment = str
KeyValueStoreName = str
LambdaFunctionARN = str
OriginShieldRegion = str
ParameterName = str
ParameterValue = str
ResourceARN = str
SamplingRate = float
TagKey = str
TagValue = str
aliasString = str
boolean = bool
distributionIdString = str
float = float
integer = int
listConflictingAliasesMaxItemsInteger = int
sensitiveStringType = str
string = str


class CachePolicyCookieBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"
    allExcept = "allExcept"
    all = "all"


class CachePolicyHeaderBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"


class CachePolicyQueryStringBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"
    allExcept = "allExcept"
    all = "all"


class CachePolicyType(StrEnum):
    managed = "managed"
    custom = "custom"


class CertificateSource(StrEnum):
    cloudfront = "cloudfront"
    iam = "iam"
    acm = "acm"


class CertificateTransparencyLoggingPreference(StrEnum):
    enabled = "enabled"
    disabled = "disabled"


class ConnectionMode(StrEnum):
    direct = "direct"
    tenant_only = "tenant-only"


class ContinuousDeploymentPolicyType(StrEnum):
    SingleWeight = "SingleWeight"
    SingleHeader = "SingleHeader"


class CustomizationActionType(StrEnum):
    override = "override"
    disable = "disable"


class DistributionResourceType(StrEnum):
    distribution = "distribution"
    distribution_tenant = "distribution-tenant"


class DnsConfigurationStatus(StrEnum):
    valid_configuration = "valid-configuration"
    invalid_configuration = "invalid-configuration"
    unknown_configuration = "unknown-configuration"


class DomainStatus(StrEnum):
    active = "active"
    inactive = "inactive"


class EventType(StrEnum):
    viewer_request = "viewer-request"
    viewer_response = "viewer-response"
    origin_request = "origin-request"
    origin_response = "origin-response"


class Format(StrEnum):
    URLEncoded = "URLEncoded"


class FrameOptionsList(StrEnum):
    DENY = "DENY"
    SAMEORIGIN = "SAMEORIGIN"


class FunctionRuntime(StrEnum):
    cloudfront_js_1_0 = "cloudfront-js-1.0"
    cloudfront_js_2_0 = "cloudfront-js-2.0"


class FunctionStage(StrEnum):
    DEVELOPMENT = "DEVELOPMENT"
    LIVE = "LIVE"


class GeoRestrictionType(StrEnum):
    blacklist = "blacklist"
    whitelist = "whitelist"
    none = "none"


class HttpVersion(StrEnum):
    http1_1 = "http1.1"
    http2 = "http2"
    http3 = "http3"
    http2and3 = "http2and3"


class ICPRecordalStatus(StrEnum):
    APPROVED = "APPROVED"
    SUSPENDED = "SUSPENDED"
    PENDING = "PENDING"


class ImportSourceType(StrEnum):
    S3 = "S3"


class ItemSelection(StrEnum):
    none = "none"
    whitelist = "whitelist"
    all = "all"


class ManagedCertificateStatus(StrEnum):
    pending_validation = "pending-validation"
    issued = "issued"
    inactive = "inactive"
    expired = "expired"
    validation_timed_out = "validation-timed-out"
    revoked = "revoked"
    failed = "failed"


class Method(StrEnum):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    DELETE = "DELETE"


class MinimumProtocolVersion(StrEnum):
    SSLv3 = "SSLv3"
    TLSv1 = "TLSv1"
    TLSv1_2016 = "TLSv1_2016"
    TLSv1_1_2016 = "TLSv1.1_2016"
    TLSv1_2_2018 = "TLSv1.2_2018"
    TLSv1_2_2019 = "TLSv1.2_2019"
    TLSv1_2_2021 = "TLSv1.2_2021"


class OriginAccessControlOriginTypes(StrEnum):
    s3 = "s3"
    mediastore = "mediastore"
    mediapackagev2 = "mediapackagev2"
    lambda_ = "lambda"


class OriginAccessControlSigningBehaviors(StrEnum):
    never = "never"
    always = "always"
    no_override = "no-override"


class OriginAccessControlSigningProtocols(StrEnum):
    sigv4 = "sigv4"


class OriginGroupSelectionCriteria(StrEnum):
    default = "default"
    media_quality_based = "media-quality-based"


class OriginProtocolPolicy(StrEnum):
    http_only = "http-only"
    match_viewer = "match-viewer"
    https_only = "https-only"


class OriginRequestPolicyCookieBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"
    all = "all"
    allExcept = "allExcept"


class OriginRequestPolicyHeaderBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"
    allViewer = "allViewer"
    allViewerAndWhitelistCloudFront = "allViewerAndWhitelistCloudFront"
    allExcept = "allExcept"


class OriginRequestPolicyQueryStringBehavior(StrEnum):
    none = "none"
    whitelist = "whitelist"
    all = "all"
    allExcept = "allExcept"


class OriginRequestPolicyType(StrEnum):
    managed = "managed"
    custom = "custom"


class PriceClass(StrEnum):
    PriceClass_100 = "PriceClass_100"
    PriceClass_200 = "PriceClass_200"
    PriceClass_All = "PriceClass_All"
    None_ = "None"


class RealtimeMetricsSubscriptionStatus(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ReferrerPolicyList(StrEnum):
    no_referrer = "no-referrer"
    no_referrer_when_downgrade = "no-referrer-when-downgrade"
    origin = "origin"
    origin_when_cross_origin = "origin-when-cross-origin"
    same_origin = "same-origin"
    strict_origin = "strict-origin"
    strict_origin_when_cross_origin = "strict-origin-when-cross-origin"
    unsafe_url = "unsafe-url"


class ResponseHeadersPolicyAccessControlAllowMethodsValues(StrEnum):
    GET = "GET"
    POST = "POST"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    ALL = "ALL"


class ResponseHeadersPolicyType(StrEnum):
    managed = "managed"
    custom = "custom"


class SSLSupportMethod(StrEnum):
    sni_only = "sni-only"
    vip = "vip"
    static_ip = "static-ip"


class SslProtocol(StrEnum):
    SSLv3 = "SSLv3"
    TLSv1 = "TLSv1"
    TLSv1_1 = "TLSv1.1"
    TLSv1_2 = "TLSv1.2"


class ValidationTokenHost(StrEnum):
    cloudfront = "cloudfront"
    self_hosted = "self-hosted"


class ViewerProtocolPolicy(StrEnum):
    allow_all = "allow-all"
    https_only = "https-only"
    redirect_to_https = "redirect-to-https"


class AccessDenied(ServiceException):
    """Access denied."""

    code: str = "AccessDenied"
    sender_fault: bool = True
    status_code: int = 403


class BatchTooLarge(ServiceException):
    """Invalidation batch specified is too large."""

    code: str = "BatchTooLarge"
    sender_fault: bool = True
    status_code: int = 413


class CNAMEAlreadyExists(ServiceException):
    """The CNAME specified is already defined for CloudFront."""

    code: str = "CNAMEAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class CachePolicyAlreadyExists(ServiceException):
    """A cache policy with this name already exists. You must provide a unique
    name. To modify an existing cache policy, use ``UpdateCachePolicy``.
    """

    code: str = "CachePolicyAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class CachePolicyInUse(ServiceException):
    """Cannot delete the cache policy because it is attached to one or more
    cache behaviors.
    """

    code: str = "CachePolicyInUse"
    sender_fault: bool = True
    status_code: int = 409


class CannotChangeImmutablePublicKeyFields(ServiceException):
    """You can't change the value of a public key."""

    code: str = "CannotChangeImmutablePublicKeyFields"
    sender_fault: bool = True
    status_code: int = 400


class CannotDeleteEntityWhileInUse(ServiceException):
    """The entity cannot be deleted while it is in use."""

    code: str = "CannotDeleteEntityWhileInUse"
    sender_fault: bool = True
    status_code: int = 409


class CannotUpdateEntityWhileInUse(ServiceException):
    """The entity cannot be updated while it is in use."""

    code: str = "CannotUpdateEntityWhileInUse"
    sender_fault: bool = True
    status_code: int = 409


class CloudFrontOriginAccessIdentityAlreadyExists(ServiceException):
    """If the ``CallerReference`` is a value you already sent in a previous
    request to create an identity but the content of the
    ``CloudFrontOriginAccessIdentityConfig`` is different from the original
    request, CloudFront returns a
    ``CloudFrontOriginAccessIdentityAlreadyExists`` error.
    """

    code: str = "CloudFrontOriginAccessIdentityAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class CloudFrontOriginAccessIdentityInUse(ServiceException):
    """The Origin Access Identity specified is already in use."""

    code: str = "CloudFrontOriginAccessIdentityInUse"
    sender_fault: bool = True
    status_code: int = 409


class ContinuousDeploymentPolicyAlreadyExists(ServiceException):
    """A continuous deployment policy with this configuration already exists."""

    code: str = "ContinuousDeploymentPolicyAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class ContinuousDeploymentPolicyInUse(ServiceException):
    """You cannot delete a continuous deployment policy that is associated with
    a primary distribution.
    """

    code: str = "ContinuousDeploymentPolicyInUse"
    sender_fault: bool = True
    status_code: int = 409


class DistributionAlreadyExists(ServiceException):
    """The caller reference you attempted to create the distribution with is
    associated with another distribution.
    """

    code: str = "DistributionAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class DistributionNotDisabled(ServiceException):
    """The specified CloudFront distribution is not disabled. You must disable
    the distribution before you can delete it.
    """

    code: str = "DistributionNotDisabled"
    sender_fault: bool = True
    status_code: int = 409


class EntityAlreadyExists(ServiceException):
    """The entity already exists. You must provide a unique entity."""

    code: str = "EntityAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class EntityLimitExceeded(ServiceException):
    """The entity limit has been exceeded."""

    code: str = "EntityLimitExceeded"
    sender_fault: bool = True
    status_code: int = 400


class EntityNotFound(ServiceException):
    """The entity was not found."""

    code: str = "EntityNotFound"
    sender_fault: bool = True
    status_code: int = 404


class EntitySizeLimitExceeded(ServiceException):
    """The entity size limit was exceeded."""

    code: str = "EntitySizeLimitExceeded"
    sender_fault: bool = True
    status_code: int = 413


class FieldLevelEncryptionConfigAlreadyExists(ServiceException):
    """The specified configuration for field-level encryption already exists."""

    code: str = "FieldLevelEncryptionConfigAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class FieldLevelEncryptionConfigInUse(ServiceException):
    """The specified configuration for field-level encryption is in use."""

    code: str = "FieldLevelEncryptionConfigInUse"
    sender_fault: bool = True
    status_code: int = 409


class FieldLevelEncryptionProfileAlreadyExists(ServiceException):
    """The specified profile for field-level encryption already exists."""

    code: str = "FieldLevelEncryptionProfileAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class FieldLevelEncryptionProfileInUse(ServiceException):
    """The specified profile for field-level encryption is in use."""

    code: str = "FieldLevelEncryptionProfileInUse"
    sender_fault: bool = True
    status_code: int = 409


class FieldLevelEncryptionProfileSizeExceeded(ServiceException):
    """The maximum size of a profile for field-level encryption was exceeded."""

    code: str = "FieldLevelEncryptionProfileSizeExceeded"
    sender_fault: bool = True
    status_code: int = 400


class FunctionAlreadyExists(ServiceException):
    """A function with the same name already exists in this Amazon Web Services
    account. To create a function, you must provide a unique name. To update
    an existing function, use ``UpdateFunction``.
    """

    code: str = "FunctionAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class FunctionInUse(ServiceException):
    """Cannot delete the function because it's attached to one or more cache
    behaviors.
    """

    code: str = "FunctionInUse"
    sender_fault: bool = True
    status_code: int = 409


class FunctionSizeLimitExceeded(ServiceException):
    """The function is too large. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "FunctionSizeLimitExceeded"
    sender_fault: bool = True
    status_code: int = 413


class IllegalDelete(ServiceException):
    """Deletion is not allowed for this entity."""

    code: str = "IllegalDelete"
    sender_fault: bool = True
    status_code: int = 400


class IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior(ServiceException):
    """The specified configuration for field-level encryption can't be
    associated with the specified cache behavior.
    """

    code: str = "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior"
    sender_fault: bool = True
    status_code: int = 400


class IllegalOriginAccessConfiguration(ServiceException):
    """An origin cannot contain both an origin access control (OAC) and an
    origin access identity (OAI).
    """

    code: str = "IllegalOriginAccessConfiguration"
    sender_fault: bool = True
    status_code: int = 400


class IllegalUpdate(ServiceException):
    """The update contains modifications that are not allowed."""

    code: str = "IllegalUpdate"
    sender_fault: bool = True
    status_code: int = 400


class InconsistentQuantities(ServiceException):
    """The value of ``Quantity`` and the size of ``Items`` don't match."""

    code: str = "InconsistentQuantities"
    sender_fault: bool = True
    status_code: int = 400


class InvalidArgument(ServiceException):
    """An argument is invalid."""

    code: str = "InvalidArgument"
    sender_fault: bool = True
    status_code: int = 400


class InvalidAssociation(ServiceException):
    """The specified CloudFront resource can't be associated."""

    code: str = "InvalidAssociation"
    sender_fault: bool = True
    status_code: int = 409


class InvalidDefaultRootObject(ServiceException):
    """The default root object file name is too big or contains an invalid
    character.
    """

    code: str = "InvalidDefaultRootObject"
    sender_fault: bool = True
    status_code: int = 400


class InvalidDomainNameForOriginAccessControl(ServiceException):
    """An origin access control is associated with an origin whose domain name
    is not supported.
    """

    code: str = "InvalidDomainNameForOriginAccessControl"
    sender_fault: bool = True
    status_code: int = 400


class InvalidErrorCode(ServiceException):
    """An invalid error code was specified."""

    code: str = "InvalidErrorCode"
    sender_fault: bool = True
    status_code: int = 400


class InvalidForwardCookies(ServiceException):
    """Your request contains forward cookies option which doesn't match with
    the expectation for the ``whitelisted`` list of cookie names. Either
    list of cookie names has been specified when not allowed or list of
    cookie names is missing when expected.
    """

    code: str = "InvalidForwardCookies"
    sender_fault: bool = True
    status_code: int = 400


class InvalidFunctionAssociation(ServiceException):
    """A CloudFront function association is invalid."""

    code: str = "InvalidFunctionAssociation"
    sender_fault: bool = True
    status_code: int = 400


class InvalidGeoRestrictionParameter(ServiceException):
    """The specified geo restriction parameter is not valid."""

    code: str = "InvalidGeoRestrictionParameter"
    sender_fault: bool = True
    status_code: int = 400


class InvalidHeadersForS3Origin(ServiceException):
    """The headers specified are not valid for an Amazon S3 origin."""

    code: str = "InvalidHeadersForS3Origin"
    sender_fault: bool = True
    status_code: int = 400


class InvalidIfMatchVersion(ServiceException):
    """The ``If-Match`` version is missing or not valid."""

    code: str = "InvalidIfMatchVersion"
    sender_fault: bool = True
    status_code: int = 400


class InvalidLambdaFunctionAssociation(ServiceException):
    """The specified Lambda@Edge function association is invalid."""

    code: str = "InvalidLambdaFunctionAssociation"
    sender_fault: bool = True
    status_code: int = 400


class InvalidLocationCode(ServiceException):
    """The location code specified is not valid."""

    code: str = "InvalidLocationCode"
    sender_fault: bool = True
    status_code: int = 400


class InvalidMinimumProtocolVersion(ServiceException):
    """The minimum protocol version specified is not valid."""

    code: str = "InvalidMinimumProtocolVersion"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOrigin(ServiceException):
    """The Amazon S3 origin server specified does not refer to a valid Amazon
    S3 bucket.
    """

    code: str = "InvalidOrigin"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOriginAccessControl(ServiceException):
    """The origin access control is not valid."""

    code: str = "InvalidOriginAccessControl"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOriginAccessIdentity(ServiceException):
    """The origin access identity is not valid or doesn't exist."""

    code: str = "InvalidOriginAccessIdentity"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOriginKeepaliveTimeout(ServiceException):
    """The keep alive timeout specified for the origin is not valid."""

    code: str = "InvalidOriginKeepaliveTimeout"
    sender_fault: bool = True
    status_code: int = 400


class InvalidOriginReadTimeout(ServiceException):
    """The read timeout specified for the origin is not valid."""

    code: str = "InvalidOriginReadTimeout"
    sender_fault: bool = True
    status_code: int = 400


class InvalidProtocolSettings(ServiceException):
    """You cannot specify SSLv3 as the minimum protocol version if you only
    want to support only clients that support Server Name Indication (SNI).
    """

    code: str = "InvalidProtocolSettings"
    sender_fault: bool = True
    status_code: int = 400


class InvalidQueryStringParameters(ServiceException):
    """The query string parameters specified are not valid."""

    code: str = "InvalidQueryStringParameters"
    sender_fault: bool = True
    status_code: int = 400


class InvalidRelativePath(ServiceException):
    """The relative path is too big, is not URL-encoded, or does not begin with
    a slash (/).
    """

    code: str = "InvalidRelativePath"
    sender_fault: bool = True
    status_code: int = 400


class InvalidRequiredProtocol(ServiceException):
    """This operation requires the HTTPS protocol. Ensure that you specify the
    HTTPS protocol in your request, or omit the ``RequiredProtocols``
    element from your distribution configuration.
    """

    code: str = "InvalidRequiredProtocol"
    sender_fault: bool = True
    status_code: int = 400


class InvalidResponseCode(ServiceException):
    """A response code is not valid."""

    code: str = "InvalidResponseCode"
    sender_fault: bool = True
    status_code: int = 400


class InvalidTTLOrder(ServiceException):
    """The TTL order specified is not valid."""

    code: str = "InvalidTTLOrder"
    sender_fault: bool = True
    status_code: int = 400


class InvalidTagging(ServiceException):
    """The tagging specified is not valid."""

    code: str = "InvalidTagging"
    sender_fault: bool = True
    status_code: int = 400


class InvalidViewerCertificate(ServiceException):
    """A viewer certificate specified is not valid."""

    code: str = "InvalidViewerCertificate"
    sender_fault: bool = True
    status_code: int = 400


class InvalidWebACLId(ServiceException):
    """A web ACL ID specified is not valid. To specify a web ACL created using
    the latest version of WAF, use the ACL ARN, for example
    ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
    To specify a web ACL created using WAF Classic, use the ACL ID, for
    example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.
    """

    code: str = "InvalidWebACLId"
    sender_fault: bool = True
    status_code: int = 400


class KeyGroupAlreadyExists(ServiceException):
    """A key group with this name already exists. You must provide a unique
    name. To modify an existing key group, use ``UpdateKeyGroup``.
    """

    code: str = "KeyGroupAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class MissingBody(ServiceException):
    """This operation requires a body. Ensure that the body is present and the
    ``Content-Type`` header is set.
    """

    code: str = "MissingBody"
    sender_fault: bool = True
    status_code: int = 400


class MonitoringSubscriptionAlreadyExists(ServiceException):
    """A monitoring subscription already exists for the specified distribution."""

    code: str = "MonitoringSubscriptionAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class NoSuchCachePolicy(ServiceException):
    """The cache policy does not exist."""

    code: str = "NoSuchCachePolicy"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchCloudFrontOriginAccessIdentity(ServiceException):
    """The specified origin access identity does not exist."""

    code: str = "NoSuchCloudFrontOriginAccessIdentity"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchContinuousDeploymentPolicy(ServiceException):
    """The continuous deployment policy doesn't exist."""

    code: str = "NoSuchContinuousDeploymentPolicy"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchDistribution(ServiceException):
    """The specified distribution does not exist."""

    code: str = "NoSuchDistribution"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchFieldLevelEncryptionConfig(ServiceException):
    """The specified configuration for field-level encryption doesn't exist."""

    code: str = "NoSuchFieldLevelEncryptionConfig"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchFieldLevelEncryptionProfile(ServiceException):
    """The specified profile for field-level encryption doesn't exist."""

    code: str = "NoSuchFieldLevelEncryptionProfile"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchFunctionExists(ServiceException):
    """The function does not exist."""

    code: str = "NoSuchFunctionExists"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchInvalidation(ServiceException):
    """The specified invalidation does not exist."""

    code: str = "NoSuchInvalidation"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchMonitoringSubscription(ServiceException):
    """A monitoring subscription does not exist for the specified distribution."""

    code: str = "NoSuchMonitoringSubscription"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchOrigin(ServiceException):
    """No origin exists with the specified ``Origin Id``."""

    code: str = "NoSuchOrigin"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchOriginAccessControl(ServiceException):
    """The origin access control does not exist."""

    code: str = "NoSuchOriginAccessControl"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchOriginRequestPolicy(ServiceException):
    """The origin request policy does not exist."""

    code: str = "NoSuchOriginRequestPolicy"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchPublicKey(ServiceException):
    """The specified public key doesn't exist."""

    code: str = "NoSuchPublicKey"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchRealtimeLogConfig(ServiceException):
    """The real-time log configuration does not exist."""

    code: str = "NoSuchRealtimeLogConfig"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchResource(ServiceException):
    """A resource that was specified is not valid."""

    code: str = "NoSuchResource"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchResponseHeadersPolicy(ServiceException):
    """The response headers policy does not exist."""

    code: str = "NoSuchResponseHeadersPolicy"
    sender_fault: bool = True
    status_code: int = 404


class NoSuchStreamingDistribution(ServiceException):
    """The specified streaming distribution does not exist."""

    code: str = "NoSuchStreamingDistribution"
    sender_fault: bool = True
    status_code: int = 404


class OriginAccessControlAlreadyExists(ServiceException):
    """An origin access control with the specified parameters already exists."""

    code: str = "OriginAccessControlAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class OriginAccessControlInUse(ServiceException):
    """Cannot delete the origin access control because it's in use by one or
    more distributions.
    """

    code: str = "OriginAccessControlInUse"
    sender_fault: bool = True
    status_code: int = 409


class OriginRequestPolicyAlreadyExists(ServiceException):
    """An origin request policy with this name already exists. You must provide
    a unique name. To modify an existing origin request policy, use
    ``UpdateOriginRequestPolicy``.
    """

    code: str = "OriginRequestPolicyAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class OriginRequestPolicyInUse(ServiceException):
    """Cannot delete the origin request policy because it is attached to one or
    more cache behaviors.
    """

    code: str = "OriginRequestPolicyInUse"
    sender_fault: bool = True
    status_code: int = 409


class PreconditionFailed(ServiceException):
    """The precondition in one or more of the request fields evaluated to
    ``false``.
    """

    code: str = "PreconditionFailed"
    sender_fault: bool = True
    status_code: int = 412


class PublicKeyAlreadyExists(ServiceException):
    """The specified public key already exists."""

    code: str = "PublicKeyAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class PublicKeyInUse(ServiceException):
    """The specified public key is in use."""

    code: str = "PublicKeyInUse"
    sender_fault: bool = True
    status_code: int = 409


class QueryArgProfileEmpty(ServiceException):
    """No profile specified for the field-level encryption query argument."""

    code: str = "QueryArgProfileEmpty"
    sender_fault: bool = True
    status_code: int = 400


class RealtimeLogConfigAlreadyExists(ServiceException):
    """A real-time log configuration with this name already exists. You must
    provide a unique name. To modify an existing real-time log
    configuration, use ``UpdateRealtimeLogConfig``.
    """

    code: str = "RealtimeLogConfigAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class RealtimeLogConfigInUse(ServiceException):
    """Cannot delete the real-time log configuration because it is attached to
    one or more cache behaviors.
    """

    code: str = "RealtimeLogConfigInUse"
    sender_fault: bool = True
    status_code: int = 400


class RealtimeLogConfigOwnerMismatch(ServiceException):
    """The specified real-time log configuration belongs to a different Amazon
    Web Services account.
    """

    code: str = "RealtimeLogConfigOwnerMismatch"
    sender_fault: bool = True
    status_code: int = 401


class ResourceInUse(ServiceException):
    """Cannot delete this resource because it is in use."""

    code: str = "ResourceInUse"
    sender_fault: bool = True
    status_code: int = 409


class ResourceNotDisabled(ServiceException):
    """The specified CloudFront resource hasn't been disabled yet."""

    code: str = "ResourceNotDisabled"
    sender_fault: bool = True
    status_code: int = 409


class ResponseHeadersPolicyAlreadyExists(ServiceException):
    """A response headers policy with this name already exists. You must
    provide a unique name. To modify an existing response headers policy,
    use ``UpdateResponseHeadersPolicy``.
    """

    code: str = "ResponseHeadersPolicyAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class ResponseHeadersPolicyInUse(ServiceException):
    """Cannot delete the response headers policy because it is attached to one
    or more cache behaviors in a CloudFront distribution.
    """

    code: str = "ResponseHeadersPolicyInUse"
    sender_fault: bool = True
    status_code: int = 409


class StagingDistributionInUse(ServiceException):
    """A continuous deployment policy for this staging distribution already
    exists.
    """

    code: str = "StagingDistributionInUse"
    sender_fault: bool = True
    status_code: int = 409


class StreamingDistributionAlreadyExists(ServiceException):
    """The caller reference you attempted to create the streaming distribution
    with is associated with another distribution
    """

    code: str = "StreamingDistributionAlreadyExists"
    sender_fault: bool = True
    status_code: int = 409


class StreamingDistributionNotDisabled(ServiceException):
    """The specified CloudFront distribution is not disabled. You must disable
    the distribution before you can delete it.
    """

    code: str = "StreamingDistributionNotDisabled"
    sender_fault: bool = True
    status_code: int = 409


class TestFunctionFailed(ServiceException):
    """The CloudFront function failed."""

    code: str = "TestFunctionFailed"
    sender_fault: bool = False
    status_code: int = 500


class TooLongCSPInResponseHeadersPolicy(ServiceException):
    """The length of the ``Content-Security-Policy`` header value in the
    response headers policy exceeds the maximum.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooLongCSPInResponseHeadersPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCacheBehaviors(ServiceException):
    """You cannot create more cache behaviors for the distribution."""

    code: str = "TooManyCacheBehaviors"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCachePolicies(ServiceException):
    """You have reached the maximum number of cache policies for this Amazon
    Web Services account. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyCachePolicies"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCertificates(ServiceException):
    """You cannot create anymore custom SSL/TLS certificates."""

    code: str = "TooManyCertificates"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCloudFrontOriginAccessIdentities(ServiceException):
    """Processing your request would cause you to exceed the maximum number of
    origin access identities allowed.
    """

    code: str = "TooManyCloudFrontOriginAccessIdentities"
    sender_fault: bool = True
    status_code: int = 400


class TooManyContinuousDeploymentPolicies(ServiceException):
    """You have reached the maximum number of continuous deployment policies
    for this Amazon Web Services account.
    """

    code: str = "TooManyContinuousDeploymentPolicies"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCookieNamesInWhiteList(ServiceException):
    """Your request contains more cookie names in the whitelist than are
    allowed per cache behavior.
    """

    code: str = "TooManyCookieNamesInWhiteList"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCookiesInCachePolicy(ServiceException):
    """The number of cookies in the cache policy exceeds the maximum. For more
    information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyCookiesInCachePolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCookiesInOriginRequestPolicy(ServiceException):
    """The number of cookies in the origin request policy exceeds the maximum.
    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyCookiesInOriginRequestPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyCustomHeadersInResponseHeadersPolicy(ServiceException):
    """The number of custom headers in the response headers policy exceeds the
    maximum.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyCustomHeadersInResponseHeadersPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionCNAMEs(ServiceException):
    """Your request contains more CNAMEs than are allowed per distribution."""

    code: str = "TooManyDistributionCNAMEs"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributions(ServiceException):
    """Processing your request would cause you to exceed the maximum number of
    distributions allowed.
    """

    code: str = "TooManyDistributions"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToCachePolicy(ServiceException):
    """The maximum number of distributions have been associated with the
    specified cache policy. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsAssociatedToCachePolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToFieldLevelEncryptionConfig(ServiceException):
    """The maximum number of distributions have been associated with the
    specified configuration for field-level encryption.
    """

    code: str = "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToKeyGroup(ServiceException):
    """The number of distributions that reference this key group is more than
    the maximum allowed. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsAssociatedToKeyGroup"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToOriginAccessControl(ServiceException):
    """The maximum number of distributions have been associated with the
    specified origin access control.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsAssociatedToOriginAccessControl"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToOriginRequestPolicy(ServiceException):
    """The maximum number of distributions have been associated with the
    specified origin request policy. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsAssociatedToOriginRequestPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsAssociatedToResponseHeadersPolicy(ServiceException):
    """The maximum number of distributions have been associated with the
    specified response headers policy.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsAssociatedToResponseHeadersPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsWithFunctionAssociations(ServiceException):
    """You have reached the maximum number of distributions that are associated
    with a CloudFront function. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyDistributionsWithFunctionAssociations"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsWithLambdaAssociations(ServiceException):
    """Processing your request would cause the maximum number of distributions
    with Lambda@Edge function associations per owner to be exceeded.
    """

    code: str = "TooManyDistributionsWithLambdaAssociations"
    sender_fault: bool = True
    status_code: int = 400


class TooManyDistributionsWithSingleFunctionARN(ServiceException):
    """The maximum number of distributions have been associated with the
    specified Lambda@Edge function.
    """

    code: str = "TooManyDistributionsWithSingleFunctionARN"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionConfigs(ServiceException):
    """The maximum number of configurations for field-level encryption have
    been created.
    """

    code: str = "TooManyFieldLevelEncryptionConfigs"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionContentTypeProfiles(ServiceException):
    """The maximum number of content type profiles for field-level encryption
    have been created.
    """

    code: str = "TooManyFieldLevelEncryptionContentTypeProfiles"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionEncryptionEntities(ServiceException):
    """The maximum number of encryption entities for field-level encryption
    have been created.
    """

    code: str = "TooManyFieldLevelEncryptionEncryptionEntities"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionFieldPatterns(ServiceException):
    """The maximum number of field patterns for field-level encryption have
    been created.
    """

    code: str = "TooManyFieldLevelEncryptionFieldPatterns"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionProfiles(ServiceException):
    """The maximum number of profiles for field-level encryption have been
    created.
    """

    code: str = "TooManyFieldLevelEncryptionProfiles"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFieldLevelEncryptionQueryArgProfiles(ServiceException):
    """The maximum number of query arg profiles for field-level encryption have
    been created.
    """

    code: str = "TooManyFieldLevelEncryptionQueryArgProfiles"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFunctionAssociations(ServiceException):
    """You have reached the maximum number of CloudFront function associations
    for this distribution. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyFunctionAssociations"
    sender_fault: bool = True
    status_code: int = 400


class TooManyFunctions(ServiceException):
    """You have reached the maximum number of CloudFront functions for this
    Amazon Web Services account. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyFunctions"
    sender_fault: bool = True
    status_code: int = 400


class TooManyHeadersInCachePolicy(ServiceException):
    """The number of headers in the cache policy exceeds the maximum. For more
    information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyHeadersInCachePolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyHeadersInForwardedValues(ServiceException):
    """Your request contains too many headers in forwarded values."""

    code: str = "TooManyHeadersInForwardedValues"
    sender_fault: bool = True
    status_code: int = 400


class TooManyHeadersInOriginRequestPolicy(ServiceException):
    """The number of headers in the origin request policy exceeds the maximum.
    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyHeadersInOriginRequestPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyInvalidationsInProgress(ServiceException):
    """You have exceeded the maximum number of allowable InProgress
    invalidation batch requests, or invalidation objects.
    """

    code: str = "TooManyInvalidationsInProgress"
    sender_fault: bool = True
    status_code: int = 400


class TooManyKeyGroups(ServiceException):
    """You have reached the maximum number of key groups for this Amazon Web
    Services account. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyKeyGroups"
    sender_fault: bool = True
    status_code: int = 400


class TooManyKeyGroupsAssociatedToDistribution(ServiceException):
    """The number of key groups referenced by this distribution is more than
    the maximum allowed. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyKeyGroupsAssociatedToDistribution"
    sender_fault: bool = True
    status_code: int = 400


class TooManyLambdaFunctionAssociations(ServiceException):
    """Your request contains more Lambda@Edge function associations than are
    allowed per distribution.
    """

    code: str = "TooManyLambdaFunctionAssociations"
    sender_fault: bool = True
    status_code: int = 400


class TooManyOriginAccessControls(ServiceException):
    """The number of origin access controls in your Amazon Web Services account
    exceeds the maximum allowed.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyOriginAccessControls"
    sender_fault: bool = True
    status_code: int = 400


class TooManyOriginCustomHeaders(ServiceException):
    """Your request contains too many origin custom headers."""

    code: str = "TooManyOriginCustomHeaders"
    sender_fault: bool = True
    status_code: int = 400


class TooManyOriginGroupsPerDistribution(ServiceException):
    """Processing your request would cause you to exceed the maximum number of
    origin groups allowed.
    """

    code: str = "TooManyOriginGroupsPerDistribution"
    sender_fault: bool = True
    status_code: int = 400


class TooManyOriginRequestPolicies(ServiceException):
    """You have reached the maximum number of origin request policies for this
    Amazon Web Services account. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyOriginRequestPolicies"
    sender_fault: bool = True
    status_code: int = 400


class TooManyOrigins(ServiceException):
    """You cannot create more origins for the distribution."""

    code: str = "TooManyOrigins"
    sender_fault: bool = True
    status_code: int = 400


class TooManyPublicKeys(ServiceException):
    """The maximum number of public keys for field-level encryption have been
    created. To create a new public key, delete one of the existing keys.
    """

    code: str = "TooManyPublicKeys"
    sender_fault: bool = True
    status_code: int = 400


class TooManyPublicKeysInKeyGroup(ServiceException):
    """The number of public keys in this key group is more than the maximum
    allowed. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyPublicKeysInKeyGroup"
    sender_fault: bool = True
    status_code: int = 400


class TooManyQueryStringParameters(ServiceException):
    """Your request contains too many query string parameters."""

    code: str = "TooManyQueryStringParameters"
    sender_fault: bool = True
    status_code: int = 400


class TooManyQueryStringsInCachePolicy(ServiceException):
    """The number of query strings in the cache policy exceeds the maximum. For
    more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyQueryStringsInCachePolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyQueryStringsInOriginRequestPolicy(ServiceException):
    """The number of query strings in the origin request policy exceeds the
    maximum. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyQueryStringsInOriginRequestPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyRealtimeLogConfigs(ServiceException):
    """You have reached the maximum number of real-time log configurations for
    this Amazon Web Services account. For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyRealtimeLogConfigs"
    sender_fault: bool = True
    status_code: int = 400


class TooManyRemoveHeadersInResponseHeadersPolicy(ServiceException):
    """The number of headers in ``RemoveHeadersConfig`` in the response headers
    policy exceeds the maximum.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyRemoveHeadersInResponseHeadersPolicy"
    sender_fault: bool = True
    status_code: int = 400


class TooManyResponseHeadersPolicies(ServiceException):
    """You have reached the maximum number of response headers policies for
    this Amazon Web Services account.

    For more information, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    (formerly known as limits) in the *Amazon CloudFront Developer Guide*.
    """

    code: str = "TooManyResponseHeadersPolicies"
    sender_fault: bool = True
    status_code: int = 400


class TooManyStreamingDistributionCNAMEs(ServiceException):
    """Your request contains more CNAMEs than are allowed per distribution."""

    code: str = "TooManyStreamingDistributionCNAMEs"
    sender_fault: bool = True
    status_code: int = 400


class TooManyStreamingDistributions(ServiceException):
    """Processing your request would cause you to exceed the maximum number of
    streaming distributions allowed.
    """

    code: str = "TooManyStreamingDistributions"
    sender_fault: bool = True
    status_code: int = 400


class TooManyTrustedSigners(ServiceException):
    """Your request contains more trusted signers than are allowed per
    distribution.
    """

    code: str = "TooManyTrustedSigners"
    sender_fault: bool = True
    status_code: int = 400


class TrustedKeyGroupDoesNotExist(ServiceException):
    """The specified key group does not exist."""

    code: str = "TrustedKeyGroupDoesNotExist"
    sender_fault: bool = True
    status_code: int = 400


class TrustedSignerDoesNotExist(ServiceException):
    """One or more of your trusted signers don't exist."""

    code: str = "TrustedSignerDoesNotExist"
    sender_fault: bool = True
    status_code: int = 400


class UnsupportedOperation(ServiceException):
    """This operation is not supported in this Amazon Web Services Region."""

    code: str = "UnsupportedOperation"
    sender_fault: bool = True
    status_code: int = 400


AccessControlAllowHeadersList = List[string]
AccessControlAllowMethodsList = List[ResponseHeadersPolicyAccessControlAllowMethodsValues]
AccessControlAllowOriginsList = List[string]
AccessControlExposeHeadersList = List[string]
KeyPairIdList = List[string]


class KeyPairIds(TypedDict, total=False):
    """A list of CloudFront key pair identifiers."""

    Quantity: integer
    Items: Optional[KeyPairIdList]


class KGKeyPairIds(TypedDict, total=False):
    """A list of identifiers for the public keys that CloudFront can use to
    verify the signatures of signed URLs and signed cookies.
    """

    KeyGroupId: Optional[string]
    KeyPairIds: Optional[KeyPairIds]


KGKeyPairIdsList = List[KGKeyPairIds]


class ActiveTrustedKeyGroups(TypedDict, total=False):
    """A list of key groups, and the public keys in each key group, that
    CloudFront can use to verify the signatures of signed URLs and signed
    cookies.
    """

    Enabled: boolean
    Quantity: integer
    Items: Optional[KGKeyPairIdsList]


class Signer(TypedDict, total=False):
    """A list of Amazon Web Services accounts and the active CloudFront key
    pairs in each account that CloudFront can use to verify the signatures
    of signed URLs and signed cookies.
    """

    AwsAccountNumber: Optional[string]
    KeyPairIds: Optional[KeyPairIds]


SignerList = List[Signer]


class ActiveTrustedSigners(TypedDict, total=False):
    """A list of Amazon Web Services accounts and the active CloudFront key
    pairs in each account that CloudFront can use to verify the signatures
    of signed URLs and signed cookies.
    """

    Enabled: boolean
    Quantity: integer
    Items: Optional[SignerList]


class AliasICPRecordal(TypedDict, total=False):
    """Amazon Web Services services in China customers must file for an
    Internet Content Provider (ICP) recordal if they want to serve content
    publicly on an alternate domain name, also known as a CNAME, that
    they've added to CloudFront. AliasICPRecordal provides the ICP recordal
    status for CNAMEs associated with distributions. The status is returned
    in the CloudFront response; you can't configure it yourself.

    For more information about ICP recordals, see `Signup, Accounts, and
    Credentials <https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html>`__
    in *Getting Started with Amazon Web Services services in China*.
    """

    CNAME: Optional[string]
    ICPRecordalStatus: Optional[ICPRecordalStatus]


AliasICPRecordals = List[AliasICPRecordal]
AliasList = List[string]


class Aliases(TypedDict, total=False):
    """A complex type that contains information about CNAMEs (alternate domain
    names), if any, for this distribution.
    """

    Quantity: integer
    Items: Optional[AliasList]


MethodsList = List[Method]


class CachedMethods(TypedDict, total=False):
    """A complex type that controls whether CloudFront caches the response to
    requests using the specified HTTP methods. There are two choices:

    -  CloudFront caches responses to ``GET`` and ``HEAD`` requests.

    -  CloudFront caches responses to ``GET``, ``HEAD``, and ``OPTIONS``
       requests.

    If you pick the second choice for your Amazon S3 Origin, you may need to
    forward Access-Control-Request-Method, Access-Control-Request-Headers,
    and Origin headers for the responses to be cached correctly.
    """

    Quantity: integer
    Items: MethodsList


class AllowedMethods(TypedDict, total=False):
    """A complex type that controls which HTTP methods CloudFront processes and
    forwards to your Amazon S3 bucket or your custom origin. There are three
    choices:

    -  CloudFront forwards only ``GET`` and ``HEAD`` requests.

    -  CloudFront forwards only ``GET``, ``HEAD``, and ``OPTIONS`` requests.

    -  CloudFront forwards ``GET, HEAD, OPTIONS, PUT, PATCH, POST``, and
       ``DELETE`` requests.

    If you pick the third choice, you may need to restrict access to your
    Amazon S3 bucket or to your custom origin so users can't perform
    operations that you don't want them to. For example, you might not want
    users to have permissions to delete objects from your origin.
    """

    Quantity: integer
    Items: MethodsList
    CachedMethods: Optional[CachedMethods]


timestamp = datetime
AnycastIps = List[string]


class AnycastIpList(TypedDict, total=False):
    """An Anycast static IP list. For more information, see `Request Anycast
    static IPs to use for
    allowlisting <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/request-static-ips.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Id: string
    Name: AnycastIpListName
    Status: string
    Arn: string
    AnycastIps: AnycastIps
    IpCount: integer
    LastModifiedTime: timestamp


class AnycastIpListSummary(TypedDict, total=False):
    """An abbreviated version of the AnycastIpList structure. Omits the
    allocated static IP addresses (AnycastIpList$AnycastIps).
    """

    Id: string
    Name: AnycastIpListName
    Status: string
    Arn: string
    IpCount: integer
    LastModifiedTime: timestamp


AnycastIpListSummaries = List[AnycastIpListSummary]


class AnycastIpListCollection(TypedDict, total=False):
    """The Anycast static IP list collection."""

    Items: Optional[AnycastIpListSummaries]
    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer


class AssociateAliasRequest(ServiceRequest):
    TargetDistributionId: string
    Alias: string


class AssociateDistributionTenantWebACLRequest(ServiceRequest):
    Id: string
    WebACLArn: string
    IfMatch: Optional[string]


class AssociateDistributionTenantWebACLResult(TypedDict, total=False):
    Id: Optional[string]
    WebACLArn: Optional[string]
    ETag: Optional[string]


class AssociateDistributionWebACLRequest(ServiceRequest):
    Id: string
    WebACLArn: string
    IfMatch: Optional[string]


class AssociateDistributionWebACLResult(TypedDict, total=False):
    Id: Optional[string]
    WebACLArn: Optional[string]
    ETag: Optional[string]


AwsAccountNumberList = List[string]
long = int
QueryStringCacheKeysList = List[string]


class QueryStringCacheKeys(TypedDict, total=False):
    """This field is deprecated. We recommend that you use a cache policy or an
    origin request policy instead of this field.

    If you want to include query strings in the cache key, use
    ``QueryStringsConfig`` in a cache policy. See ``CachePolicy``.

    If you want to send query strings to the origin but not include them in
    the cache key, use ``QueryStringsConfig`` in an origin request policy.
    See ``OriginRequestPolicy``.

    A complex type that contains information about the query string
    parameters that you want CloudFront to use for caching for a cache
    behavior.
    """

    Quantity: integer
    Items: Optional[QueryStringCacheKeysList]


HeaderList = List[string]


class Headers(TypedDict, total=False):
    """Contains a list of HTTP header names."""

    Quantity: integer
    Items: Optional[HeaderList]


CookieNameList = List[string]


class CookieNames(TypedDict, total=False):
    """Contains a list of cookie names."""

    Quantity: integer
    Items: Optional[CookieNameList]


class CookiePreference(TypedDict, total=False):
    """This field is deprecated. We recommend that you use a cache policy or an
    origin request policy instead of this field.

    If you want to include cookies in the cache key, use ``CookiesConfig``
    in a cache policy. See ``CachePolicy``.

    If you want to send cookies to the origin but not include them in the
    cache key, use ``CookiesConfig`` in an origin request policy. See
    ``OriginRequestPolicy``.

    A complex type that specifies whether you want CloudFront to forward
    cookies to the origin and, if so, which ones. For more information about
    forwarding cookies to the origin, see `Caching Content Based on
    Cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Forward: ItemSelection
    WhitelistedNames: Optional[CookieNames]


class ForwardedValues(TypedDict, total=False):
    """This field is deprecated. We recommend that you use a cache policy or an
    origin request policy instead of this field.

    If you want to include values in the cache key, use a cache policy. For
    more information, see `Creating cache
    policies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy>`__
    in the *Amazon CloudFront Developer Guide*.

    If you want to send values to the origin but not include them in the
    cache key, use an origin request policy. For more information, see
    `Creating origin request
    policies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy>`__
    in the *Amazon CloudFront Developer Guide*.

    A complex type that specifies how CloudFront handles query strings,
    cookies, and HTTP headers.
    """

    QueryString: boolean
    Cookies: CookiePreference
    Headers: Optional[Headers]
    QueryStringCacheKeys: Optional[QueryStringCacheKeys]


class GrpcConfig(TypedDict, total=False):
    """Amazon CloudFront supports gRPC, an open-source remote procedure call
    (RPC) framework built on HTTP/2. gRPC offers bi-directional streaming
    and binary protocol that buffers payloads, making it suitable for
    applications that require low latency communications.

    To enable your distribution to handle gRPC requests, you must include
    HTTP/2 as one of the supported ``HTTP`` versions and allow ``HTTP``
    methods, including ``POST``.

    For more information, see `Using gRPC with CloudFront
    distributions <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-using-grpc.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Enabled: boolean


class FunctionAssociation(TypedDict, total=False):
    """A CloudFront function that is associated with a cache behavior in a
    CloudFront distribution.
    """

    FunctionARN: FunctionARN
    EventType: EventType


FunctionAssociationList = List[FunctionAssociation]


class FunctionAssociations(TypedDict, total=False):
    """A list of CloudFront functions that are associated with a cache behavior
    in a CloudFront distribution. Your functions must be published to the
    ``LIVE`` stage to associate them with a cache behavior.
    """

    Quantity: integer
    Items: Optional[FunctionAssociationList]


class LambdaFunctionAssociation(TypedDict, total=False):
    """A complex type that contains a Lambda@Edge function association."""

    LambdaFunctionARN: LambdaFunctionARN
    EventType: EventType
    IncludeBody: Optional[boolean]


LambdaFunctionAssociationList = List[LambdaFunctionAssociation]


class LambdaFunctionAssociations(TypedDict, total=False):
    """A complex type that specifies a list of Lambda@Edge functions
    associations for a cache behavior.

    If you want to invoke one or more Lambda@Edge functions triggered by
    requests that match the ``PathPattern`` of the cache behavior, specify
    the applicable values for ``Quantity`` and ``Items``. Note that there
    can be up to 4 ``LambdaFunctionAssociation`` items in this list (one for
    each possible value of ``EventType``) and each ``EventType`` can be
    associated with only one function.

    If you don't want to invoke any Lambda@Edge functions for the requests
    that match ``PathPattern``, specify ``0`` for ``Quantity`` and omit
    ``Items``.
    """

    Quantity: integer
    Items: Optional[LambdaFunctionAssociationList]


TrustedKeyGroupIdList = List[string]


class TrustedKeyGroups(TypedDict, total=False):
    """A list of key groups whose public keys CloudFront can use to verify the
    signatures of signed URLs and signed cookies.
    """

    Enabled: boolean
    Quantity: integer
    Items: Optional[TrustedKeyGroupIdList]


class TrustedSigners(TypedDict, total=False):
    """A list of Amazon Web Services accounts whose public keys CloudFront can
    use to verify the signatures of signed URLs and signed cookies.
    """

    Enabled: boolean
    Quantity: integer
    Items: Optional[AwsAccountNumberList]


class CacheBehavior(TypedDict, total=False):
    """A complex type that describes how CloudFront processes requests.

    You must create at least as many cache behaviors (including the default
    cache behavior) as you have origins if you want CloudFront to serve
    objects from all of the origins. Each cache behavior specifies the one
    origin from which you want CloudFront to get objects. If you have two
    origins and only the default cache behavior, the default cache behavior
    will cause CloudFront to get objects from one of the origins, but the
    other origin is never used.

    For the current quota (formerly known as limit) on the number of cache
    behaviors that you can add to a distribution, see
    `Quotas <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html>`__
    in the *Amazon CloudFront Developer Guide*.

    If you don't want to specify any cache behaviors, include only an empty
    ``CacheBehaviors`` element. Don't specify an empty individual
    ``CacheBehavior`` element, because this is invalid. For more
    information, see
    `CacheBehaviors <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheBehaviors.html>`__.

    To delete all cache behaviors in an existing distribution, update the
    distribution configuration and include only an empty ``CacheBehaviors``
    element.

    To add, change, or remove one or more cache behaviors, update the
    distribution configuration and specify all of the cache behaviors that
    you want to include in the updated distribution.

    For more information about cache behaviors, see `Cache Behavior
    Settings <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    PathPattern: string
    TargetOriginId: string
    TrustedSigners: Optional[TrustedSigners]
    TrustedKeyGroups: Optional[TrustedKeyGroups]
    ViewerProtocolPolicy: ViewerProtocolPolicy
    AllowedMethods: Optional[AllowedMethods]
    SmoothStreaming: Optional[boolean]
    Compress: Optional[boolean]
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociations]
    FunctionAssociations: Optional[FunctionAssociations]
    FieldLevelEncryptionId: Optional[string]
    RealtimeLogConfigArn: Optional[string]
    CachePolicyId: Optional[string]
    OriginRequestPolicyId: Optional[string]
    ResponseHeadersPolicyId: Optional[string]
    GrpcConfig: Optional[GrpcConfig]
    ForwardedValues: Optional[ForwardedValues]
    MinTTL: Optional[long]
    DefaultTTL: Optional[long]
    MaxTTL: Optional[long]


CacheBehaviorList = List[CacheBehavior]


class CacheBehaviors(TypedDict, total=False):
    """A complex type that contains zero or more ``CacheBehavior`` elements."""

    Quantity: integer
    Items: Optional[CacheBehaviorList]


QueryStringNamesList = List[string]


class QueryStringNames(TypedDict, total=False):
    """Contains a list of query string names."""

    Quantity: integer
    Items: Optional[QueryStringNamesList]


class CachePolicyQueryStringsConfig(TypedDict, total=False):
    """An object that determines whether any URL query strings in viewer
    requests (and if so, which query strings) are included in the cache key
    and in requests that CloudFront sends to the origin.
    """

    QueryStringBehavior: CachePolicyQueryStringBehavior
    QueryStrings: Optional[QueryStringNames]


class CachePolicyCookiesConfig(TypedDict, total=False):
    """An object that determines whether any cookies in viewer requests (and if
    so, which cookies) are included in the cache key and in requests that
    CloudFront sends to the origin.
    """

    CookieBehavior: CachePolicyCookieBehavior
    Cookies: Optional[CookieNames]


class CachePolicyHeadersConfig(TypedDict, total=False):
    """An object that determines whether any HTTP headers (and if so, which
    headers) are included in the cache key and in requests that CloudFront
    sends to the origin.
    """

    HeaderBehavior: CachePolicyHeaderBehavior
    Headers: Optional[Headers]


class ParametersInCacheKeyAndForwardedToOrigin(TypedDict, total=False):
    """This object determines the values that CloudFront includes in the cache
    key. These values can include HTTP headers, cookies, and URL query
    strings. CloudFront uses the cache key to find an object in its cache
    that it can return to the viewer.

    The headers, cookies, and query strings that are included in the cache
    key are also included in requests that CloudFront sends to the origin.
    CloudFront sends a request when it can't find an object in its cache
    that matches the request's cache key. If you want to send values to the
    origin but *not* include them in the cache key, use
    ``OriginRequestPolicy``.
    """

    EnableAcceptEncodingGzip: boolean
    EnableAcceptEncodingBrotli: Optional[boolean]
    HeadersConfig: CachePolicyHeadersConfig
    CookiesConfig: CachePolicyCookiesConfig
    QueryStringsConfig: CachePolicyQueryStringsConfig


class CachePolicyConfig(TypedDict, total=False):
    """A cache policy configuration.

    This configuration determines the following:

    -  The values that CloudFront includes in the cache key. These values
       can include HTTP headers, cookies, and URL query strings. CloudFront
       uses the cache key to find an object in its cache that it can return
       to the viewer.

    -  The default, minimum, and maximum time to live (TTL) values that you
       want objects to stay in the CloudFront cache.

    The headers, cookies, and query strings that are included in the cache
    key are also included in requests that CloudFront sends to the origin.
    CloudFront sends a request when it can't find a valid object in its
    cache that matches the request's cache key. If you want to send values
    to the origin but *not* include them in the cache key, use
    ``OriginRequestPolicy``.
    """

    Comment: Optional[string]
    Name: string
    DefaultTTL: Optional[long]
    MaxTTL: Optional[long]
    MinTTL: long
    ParametersInCacheKeyAndForwardedToOrigin: Optional[ParametersInCacheKeyAndForwardedToOrigin]


class CachePolicy(TypedDict, total=False):
    """A cache policy.

    When it's attached to a cache behavior, the cache policy determines the
    following:

    -  The values that CloudFront includes in the cache key. These values
       can include HTTP headers, cookies, and URL query strings. CloudFront
       uses the cache key to find an object in its cache that it can return
       to the viewer.

    -  The default, minimum, and maximum time to live (TTL) values that you
       want objects to stay in the CloudFront cache.

    The headers, cookies, and query strings that are included in the cache
    key are also included in requests that CloudFront sends to the origin.
    CloudFront sends a request when it can't find a valid object in its
    cache that matches the request's cache key. If you want to send values
    to the origin but *not* include them in the cache key, use
    ``OriginRequestPolicy``.
    """

    Id: string
    LastModifiedTime: timestamp
    CachePolicyConfig: CachePolicyConfig


class CachePolicySummary(TypedDict, total=False):
    """Contains a cache policy."""

    Type: CachePolicyType
    CachePolicy: CachePolicy


CachePolicySummaryList = List[CachePolicySummary]


class CachePolicyList(TypedDict, total=False):
    """A list of cache policies."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[CachePolicySummaryList]


class Certificate(TypedDict, total=False):
    """The Certificate Manager (ACM) certificate associated with your
    distribution.
    """

    Arn: string


class CloudFrontOriginAccessIdentityConfig(TypedDict, total=False):
    """Origin access identity configuration. Send a ``GET`` request to the
    ``/CloudFront API version/CloudFront/identity ID/config`` resource.
    """

    CallerReference: string
    Comment: string


class CloudFrontOriginAccessIdentity(TypedDict, total=False):
    """CloudFront origin access identity."""

    Id: string
    S3CanonicalUserId: string
    CloudFrontOriginAccessIdentityConfig: Optional[CloudFrontOriginAccessIdentityConfig]


class CloudFrontOriginAccessIdentitySummary(TypedDict, total=False):
    """Summary of the information about a CloudFront origin access identity."""

    Id: string
    S3CanonicalUserId: string
    Comment: string


CloudFrontOriginAccessIdentitySummaryList = List[CloudFrontOriginAccessIdentitySummary]


class CloudFrontOriginAccessIdentityList(TypedDict, total=False):
    """Lists the origin access identities for CloudFront.Send a ``GET`` request
    to the ``/CloudFront API version/origin-access-identity/cloudfront``
    resource. The response includes a ``CloudFrontOriginAccessIdentityList``
    element with zero or more ``CloudFrontOriginAccessIdentitySummary``
    child elements. By default, your entire list of origin access identities
    is returned in one single page. If the list is long, you can paginate it
    using the ``MaxItems`` and ``Marker`` parameters.
    """

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[CloudFrontOriginAccessIdentitySummaryList]


class ConflictingAlias(TypedDict, total=False):
    """An alias (also called a CNAME) and the CloudFront distribution and
    Amazon Web Services account ID that it's associated with. The
    distribution and account IDs are partially hidden, which allows you to
    identify the distributions and accounts that you own, but helps to
    protect the information of ones that you don't own.
    """

    Alias: Optional[string]
    DistributionId: Optional[string]
    AccountId: Optional[string]


ConflictingAliases = List[ConflictingAlias]


class ConflictingAliasesList(TypedDict, total=False):
    """A list of aliases (also called CNAMEs) and the CloudFront distributions
    and Amazon Web Services accounts that they are associated with. In the
    list, the distribution and account IDs are partially hidden, which
    allows you to identify the distributions and accounts that you own, but
    helps to protect the information of ones that you don't own.
    """

    NextMarker: Optional[string]
    MaxItems: Optional[integer]
    Quantity: Optional[integer]
    Items: Optional[ConflictingAliases]


class Tag(TypedDict, total=False):
    """A complex type that contains ``Tag`` key and ``Tag`` value."""

    Key: TagKey
    Value: Optional[TagValue]


TagList = List[Tag]


class Tags(TypedDict, total=False):
    """A complex type that contains zero or more ``Tag`` elements."""

    Items: Optional[TagList]


class ConnectionGroup(TypedDict, total=False):
    """The connection group for your distribution tenants. When you first
    create a distribution tenant and you don't specify a connection group,
    CloudFront will automatically create a default connection group for you.
    When you create a new distribution tenant and don't specify a connection
    group, the default one will be associated with your distribution tenant.
    """

    Id: Optional[string]
    Name: Optional[string]
    Arn: Optional[string]
    CreatedTime: Optional[timestamp]
    LastModifiedTime: Optional[timestamp]
    Tags: Optional[Tags]
    Ipv6Enabled: Optional[boolean]
    RoutingEndpoint: Optional[string]
    AnycastIpListId: Optional[string]
    Status: Optional[string]
    Enabled: Optional[boolean]
    IsDefault: Optional[boolean]


class ConnectionGroupAssociationFilter(TypedDict, total=False):
    """Contains information about what CloudFront resources your connection
    groups are associated with.
    """

    AnycastIpListId: Optional[string]


class ConnectionGroupSummary(TypedDict, total=False):
    """A summary that contains details about your connection groups."""

    Id: string
    Name: string
    Arn: string
    RoutingEndpoint: string
    CreatedTime: timestamp
    LastModifiedTime: timestamp
    ETag: string
    AnycastIpListId: Optional[string]
    Enabled: Optional[boolean]
    Status: Optional[string]
    IsDefault: Optional[boolean]


ConnectionGroupSummaryList = List[ConnectionGroupSummary]


class ContentTypeProfile(TypedDict, total=False):
    """A field-level encryption content type profile."""

    Format: Format
    ProfileId: Optional[string]
    ContentType: string


ContentTypeProfileList = List[ContentTypeProfile]


class ContentTypeProfiles(TypedDict, total=False):
    """Field-level encryption content type-profile."""

    Quantity: integer
    Items: Optional[ContentTypeProfileList]


class ContentTypeProfileConfig(TypedDict, total=False):
    """The configuration for a field-level encryption content type-profile
    mapping.
    """

    ForwardWhenContentTypeIsUnknown: boolean
    ContentTypeProfiles: Optional[ContentTypeProfiles]


class ContinuousDeploymentSingleHeaderConfig(TypedDict, total=False):
    """This configuration determines which HTTP requests are sent to the
    staging distribution. If the HTTP request contains a header and value
    that matches what you specify here, the request is sent to the staging
    distribution. Otherwise the request is sent to the primary distribution.
    """

    Header: string
    Value: string


class SessionStickinessConfig(TypedDict, total=False):
    """Session stickiness provides the ability to define multiple requests from
    a single viewer as a single session. This prevents the potentially
    inconsistent experience of sending some of a given user's requests to
    your staging distribution, while others are sent to your primary
    distribution. Define the session duration using TTL values.
    """

    IdleTTL: integer
    MaximumTTL: integer


class ContinuousDeploymentSingleWeightConfig(TypedDict, total=False):
    """Contains the percentage of traffic to send to a staging distribution."""

    Weight: float
    SessionStickinessConfig: Optional[SessionStickinessConfig]


class TrafficConfig(TypedDict, total=False):
    """The traffic configuration of your continuous deployment."""

    SingleWeightConfig: Optional[ContinuousDeploymentSingleWeightConfig]
    SingleHeaderConfig: Optional[ContinuousDeploymentSingleHeaderConfig]
    Type: ContinuousDeploymentPolicyType


StagingDistributionDnsNameList = List[string]


class StagingDistributionDnsNames(TypedDict, total=False):
    """The CloudFront domain name of the staging distribution."""

    Quantity: integer
    Items: Optional[StagingDistributionDnsNameList]


class ContinuousDeploymentPolicyConfig(TypedDict, total=False):
    """Contains the configuration for a continuous deployment policy."""

    StagingDistributionDnsNames: StagingDistributionDnsNames
    Enabled: boolean
    TrafficConfig: Optional[TrafficConfig]


class ContinuousDeploymentPolicy(TypedDict, total=False):
    """A continuous deployment policy."""

    Id: string
    LastModifiedTime: timestamp
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfig


class ContinuousDeploymentPolicySummary(TypedDict, total=False):
    """A summary of the information about your continuous deployment policies."""

    ContinuousDeploymentPolicy: ContinuousDeploymentPolicy


ContinuousDeploymentPolicySummaryList = List[ContinuousDeploymentPolicySummary]


class ContinuousDeploymentPolicyList(TypedDict, total=False):
    """Contains a list of continuous deployment policies."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[ContinuousDeploymentPolicySummaryList]


class CopyDistributionRequest(ServiceRequest):
    PrimaryDistributionId: string
    Staging: Optional[boolean]
    IfMatch: Optional[string]
    CallerReference: string
    Enabled: Optional[boolean]


class StringSchemaConfig(TypedDict, total=False):
    """The configuration for a string schema."""

    Comment: Optional[string]
    DefaultValue: Optional[ParameterValue]
    Required: boolean


class ParameterDefinitionSchema(TypedDict, total=False):
    """An object that contains information about the parameter definition."""

    StringSchema: Optional[StringSchemaConfig]


class ParameterDefinition(TypedDict, total=False):
    """A list of parameter values to add to the resource. A parameter is
    specified as a key-value pair. A valid parameter value must exist for
    any parameter that is marked as required in the multi-tenant
    distribution.
    """

    Name: ParameterName
    Definition: ParameterDefinitionSchema


ParameterDefinitions = List[ParameterDefinition]


class TenantConfig(TypedDict, total=False):
    """The configuration for a distribution tenant."""

    ParameterDefinitions: Optional[ParameterDefinitions]


LocationList = List[string]


class GeoRestriction(TypedDict, total=False):
    """A complex type that controls the countries in which your content is
    distributed. CloudFront determines the location of your users using
    ``MaxMind`` GeoIP databases.
    """

    RestrictionType: GeoRestrictionType
    Quantity: integer
    Items: Optional[LocationList]


class Restrictions(TypedDict, total=False):
    """A complex type that identifies ways in which you want to restrict
    distribution of your content.
    """

    GeoRestriction: GeoRestriction


class ViewerCertificate(TypedDict, total=False):
    """A complex type that determines the distribution's SSL/TLS configuration
    for communicating with viewers.

    If the distribution doesn't use ``Aliases`` (also known as alternate
    domain names or CNAMEs)—that is, if the distribution uses the CloudFront
    domain name such as ``d111111abcdef8.cloudfront.net``—set
    ``CloudFrontDefaultCertificate`` to ``true`` and leave all other fields
    empty.

    If the distribution uses ``Aliases`` (alternate domain names or CNAMEs),
    use the fields in this type to specify the following settings:

    -  Which viewers the distribution accepts HTTPS connections from: only
       viewers that support `server name indication
       (SNI) <https://en.wikipedia.org/wiki/Server_Name_Indication>`__
       (recommended), or all viewers including those that don't support SNI.

       -  To accept HTTPS connections from only viewers that support SNI,
          set ``SSLSupportMethod`` to ``sni-only``. This is recommended.
          Most browsers and clients support SNI.

       -  To accept HTTPS connections from all viewers, including those that
          don't support SNI, set ``SSLSupportMethod`` to ``vip``. This is
          not recommended, and results in additional monthly charges from
          CloudFront.

    -  The minimum SSL/TLS protocol version that the distribution can use to
       communicate with viewers. To specify a minimum version, choose a
       value for ``MinimumProtocolVersion``. For more information, see
       `Security
       Policy <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy>`__
       in the *Amazon CloudFront Developer Guide*.

    -  The location of the SSL/TLS certificate, `Certificate Manager
       (ACM) <https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html>`__
       (recommended) or `Identity and Access Management
       (IAM) <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html>`__.
       You specify the location by setting a value in one of the following
       fields (not both):

       -  ``ACMCertificateArn``

       -  ``IAMCertificateId``

    All distributions support HTTPS connections from viewers. To require
    viewers to use HTTPS only, or to redirect them from HTTP to HTTPS, use
    ``ViewerProtocolPolicy`` in the ``CacheBehavior`` or
    ``DefaultCacheBehavior``. To specify how CloudFront should use SSL/TLS
    to communicate with your custom origin, use ``CustomOriginConfig``.

    For more information, see `Using HTTPS with
    CloudFront <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html>`__
    and `Using Alternate Domain Names and
    HTTPS <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-alternate-domain-names.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    CloudFrontDefaultCertificate: Optional[boolean]
    IAMCertificateId: Optional[string]
    ACMCertificateArn: Optional[string]
    SSLSupportMethod: Optional[SSLSupportMethod]
    MinimumProtocolVersion: Optional[MinimumProtocolVersion]
    Certificate: Optional[string]
    CertificateSource: Optional[CertificateSource]


class LoggingConfig(TypedDict, total=False):
    """A complex type that specifies whether access logs are written for the
    distribution.

    If you already enabled standard logging (legacy) and you want to enable
    standard logging (v2) to send your access logs to Amazon S3, we
    recommend that you specify a *different* Amazon S3 bucket or use a
    *separate path* in the same bucket (for example, use a log prefix or
    partitioning). This helps you keep track of which log files are
    associated with which logging subscription and prevents log files from
    overwriting each other. For more information, see `Standard logging
    (access
    logs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Enabled: Optional[boolean]
    IncludeCookies: Optional[boolean]
    Bucket: Optional[string]
    Prefix: Optional[string]


class CustomErrorResponse(TypedDict, total=False):
    """A complex type that controls:

    -  Whether CloudFront replaces HTTP status codes in the 4xx and 5xx
       range with custom error messages before returning the response to the
       viewer.

    -  How long CloudFront caches HTTP status codes in the 4xx and 5xx
       range.

    For more information about custom error pages, see `Customizing Error
    Responses <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    ErrorCode: integer
    ResponsePagePath: Optional[string]
    ResponseCode: Optional[string]
    ErrorCachingMinTTL: Optional[long]


CustomErrorResponseList = List[CustomErrorResponse]


class CustomErrorResponses(TypedDict, total=False):
    """A complex type that controls:

    -  Whether CloudFront replaces HTTP status codes in the 4xx and 5xx
       range with custom error messages before returning the response to the
       viewer.

    -  How long CloudFront caches HTTP status codes in the 4xx and 5xx
       range.

    For more information about custom error pages, see `Customizing Error
    Responses <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Quantity: integer
    Items: Optional[CustomErrorResponseList]


class DefaultCacheBehavior(TypedDict, total=False):
    """A complex type that describes the default cache behavior if you don't
    specify a ``CacheBehavior`` element or if request URLs don't match any
    of the values of ``PathPattern`` in ``CacheBehavior`` elements. You must
    create exactly one default cache behavior.
    """

    TargetOriginId: string
    TrustedSigners: Optional[TrustedSigners]
    TrustedKeyGroups: Optional[TrustedKeyGroups]
    ViewerProtocolPolicy: ViewerProtocolPolicy
    AllowedMethods: Optional[AllowedMethods]
    SmoothStreaming: Optional[boolean]
    Compress: Optional[boolean]
    LambdaFunctionAssociations: Optional[LambdaFunctionAssociations]
    FunctionAssociations: Optional[FunctionAssociations]
    FieldLevelEncryptionId: Optional[string]
    RealtimeLogConfigArn: Optional[string]
    CachePolicyId: Optional[string]
    OriginRequestPolicyId: Optional[string]
    ResponseHeadersPolicyId: Optional[string]
    GrpcConfig: Optional[GrpcConfig]
    ForwardedValues: Optional[ForwardedValues]
    MinTTL: Optional[long]
    DefaultTTL: Optional[long]
    MaxTTL: Optional[long]


class OriginGroupMember(TypedDict, total=False):
    """An origin in an origin group."""

    OriginId: string


OriginGroupMemberList = List[OriginGroupMember]


class OriginGroupMembers(TypedDict, total=False):
    """A complex data type for the origins included in an origin group."""

    Quantity: integer
    Items: OriginGroupMemberList


StatusCodeList = List[integer]


class StatusCodes(TypedDict, total=False):
    """A complex data type for the status codes that you specify that, when
    returned by a primary origin, trigger CloudFront to failover to a second
    origin.
    """

    Quantity: integer
    Items: StatusCodeList


class OriginGroupFailoverCriteria(TypedDict, total=False):
    """A complex data type that includes information about the failover
    criteria for an origin group, including the status codes for which
    CloudFront will failover from the primary origin to the second origin.
    """

    StatusCodes: StatusCodes


class OriginGroup(TypedDict, total=False):
    """An origin group includes two origins (a primary origin and a secondary
    origin to failover to) and a failover criteria that you specify. You
    create an origin group to support origin failover in CloudFront. When
    you create or update a distribution, you can specify the origin group
    instead of a single origin, and CloudFront will failover from the
    primary origin to the secondary origin under the failover conditions
    that you've chosen.

    Optionally, you can choose selection criteria for your origin group to
    specify how your origins are selected when your distribution routes
    viewer requests.
    """

    Id: string
    FailoverCriteria: OriginGroupFailoverCriteria
    Members: OriginGroupMembers
    SelectionCriteria: Optional[OriginGroupSelectionCriteria]


OriginGroupList = List[OriginGroup]


class OriginGroups(TypedDict, total=False):
    """A complex data type for the origin groups specified for a distribution."""

    Quantity: integer
    Items: Optional[OriginGroupList]


class OriginShield(TypedDict, total=False):
    """CloudFront Origin Shield.

    Using Origin Shield can help reduce the load on your origin. For more
    information, see `Using Origin
    Shield <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Enabled: boolean
    OriginShieldRegion: Optional[OriginShieldRegion]


class VpcOriginConfig(TypedDict, total=False):
    """An Amazon CloudFront VPC origin configuration."""

    VpcOriginId: string
    OriginReadTimeout: Optional[integer]
    OriginKeepaliveTimeout: Optional[integer]


SslProtocolsList = List[SslProtocol]


class OriginSslProtocols(TypedDict, total=False):
    """A complex type that contains information about the SSL/TLS protocols
    that CloudFront can use when establishing an HTTPS connection with your
    origin.
    """

    Quantity: integer
    Items: SslProtocolsList


class CustomOriginConfig(TypedDict, total=False):
    """A custom origin. A custom origin is any origin that is *not* an Amazon
    S3 bucket, with one exception. An Amazon S3 bucket that is `configured
    with static website
    hosting <https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`__
    *is* a custom origin.
    """

    HTTPPort: integer
    HTTPSPort: integer
    OriginProtocolPolicy: OriginProtocolPolicy
    OriginSslProtocols: Optional[OriginSslProtocols]
    OriginReadTimeout: Optional[integer]
    OriginKeepaliveTimeout: Optional[integer]


class S3OriginConfig(TypedDict, total=False):
    """A complex type that contains information about the Amazon S3 origin. If
    the origin is a custom origin or an S3 bucket that is configured as a
    website endpoint, use the ``CustomOriginConfig`` element instead.
    """

    OriginAccessIdentity: string


class OriginCustomHeader(TypedDict, total=False):
    """A complex type that contains ``HeaderName`` and ``HeaderValue``
    elements, if any, for this distribution.
    """

    HeaderName: string
    HeaderValue: sensitiveStringType


OriginCustomHeadersList = List[OriginCustomHeader]


class CustomHeaders(TypedDict, total=False):
    """A complex type that contains the list of Custom Headers for each origin."""

    Quantity: integer
    Items: Optional[OriginCustomHeadersList]


class Origin(TypedDict, total=False):
    """An origin.

    An origin is the location where content is stored, and from which
    CloudFront gets content to serve to viewers. To specify an origin:

    -  Use ``S3OriginConfig`` to specify an Amazon S3 bucket that is not
       configured with static website hosting.

    -  Use ``VpcOriginConfig`` to specify a VPC origin.

    -  Use ``CustomOriginConfig`` to specify all other kinds of origins,
       including:

       -  An Amazon S3 bucket that is configured with static website hosting

       -  An Elastic Load Balancing load balancer

       -  An Elemental MediaPackage endpoint

       -  An Elemental MediaStore container

       -  Any other HTTP server, running on an Amazon EC2 instance or any
          other kind of host

    For the current maximum number of origins that you can specify per
    distribution, see `General Quotas on Web
    Distributions <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html#limits-web-distributions>`__
    in the *Amazon CloudFront Developer Guide* (quotas were formerly
    referred to as limits).
    """

    Id: string
    DomainName: string
    OriginPath: Optional[string]
    CustomHeaders: Optional[CustomHeaders]
    S3OriginConfig: Optional[S3OriginConfig]
    CustomOriginConfig: Optional[CustomOriginConfig]
    VpcOriginConfig: Optional[VpcOriginConfig]
    ConnectionAttempts: Optional[integer]
    ConnectionTimeout: Optional[integer]
    OriginShield: Optional[OriginShield]
    OriginAccessControlId: Optional[string]


OriginList = List[Origin]


class Origins(TypedDict, total=False):
    """Contains information about the origins for this distribution."""

    Quantity: integer
    Items: OriginList


class DistributionConfig(TypedDict, total=False):
    """A distribution configuration."""

    CallerReference: string
    Aliases: Optional[Aliases]
    DefaultRootObject: Optional[string]
    Origins: Origins
    OriginGroups: Optional[OriginGroups]
    DefaultCacheBehavior: DefaultCacheBehavior
    CacheBehaviors: Optional[CacheBehaviors]
    CustomErrorResponses: Optional[CustomErrorResponses]
    Comment: CommentType
    Logging: Optional[LoggingConfig]
    PriceClass: Optional[PriceClass]
    Enabled: boolean
    ViewerCertificate: Optional[ViewerCertificate]
    Restrictions: Optional[Restrictions]
    WebACLId: Optional[string]
    HttpVersion: Optional[HttpVersion]
    IsIPV6Enabled: Optional[boolean]
    ContinuousDeploymentPolicyId: Optional[string]
    Staging: Optional[boolean]
    AnycastIpListId: Optional[string]
    TenantConfig: Optional[TenantConfig]
    ConnectionMode: Optional[ConnectionMode]


class Distribution(TypedDict, total=False):
    """A distribution tells CloudFront where you want content to be delivered
    from, and the details about how to track and manage content delivery.
    """

    Id: string
    ARN: string
    Status: string
    LastModifiedTime: timestamp
    InProgressInvalidationBatches: integer
    DomainName: string
    ActiveTrustedSigners: Optional[ActiveTrustedSigners]
    ActiveTrustedKeyGroups: Optional[ActiveTrustedKeyGroups]
    DistributionConfig: DistributionConfig
    AliasICPRecordals: Optional[AliasICPRecordals]


class CopyDistributionResult(TypedDict, total=False):
    Distribution: Optional[Distribution]
    Location: Optional[string]
    ETag: Optional[string]


class CreateAnycastIpListRequest(ServiceRequest):
    Name: AnycastIpListName
    IpCount: integer
    Tags: Optional[Tags]


class CreateAnycastIpListResult(TypedDict, total=False):
    AnycastIpList: Optional[AnycastIpList]
    ETag: Optional[string]


class CreateCachePolicyRequest(ServiceRequest):
    CachePolicyConfig: CachePolicyConfig


class CreateCachePolicyResult(TypedDict, total=False):
    CachePolicy: Optional[CachePolicy]
    Location: Optional[string]
    ETag: Optional[string]


class CreateCloudFrontOriginAccessIdentityRequest(ServiceRequest):
    """The request to create a new origin access identity (OAI). An origin
    access identity is a special CloudFront user that you can associate with
    Amazon S3 origins, so that you can secure all or just some of your
    Amazon S3 content. For more information, see `Restricting Access to
    Amazon S3 Content by Using an Origin Access
    Identity <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfig


class CreateCloudFrontOriginAccessIdentityResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    CloudFrontOriginAccessIdentity: Optional[CloudFrontOriginAccessIdentity]
    Location: Optional[string]
    ETag: Optional[string]


class CreateConnectionGroupRequest(ServiceRequest):
    Name: string
    Ipv6Enabled: Optional[boolean]
    Tags: Optional[Tags]
    AnycastIpListId: Optional[string]
    Enabled: Optional[boolean]


class CreateConnectionGroupResult(TypedDict, total=False):
    ConnectionGroup: Optional[ConnectionGroup]
    ETag: Optional[string]


class CreateContinuousDeploymentPolicyRequest(ServiceRequest):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfig


class CreateContinuousDeploymentPolicyResult(TypedDict, total=False):
    ContinuousDeploymentPolicy: Optional[ContinuousDeploymentPolicy]
    Location: Optional[string]
    ETag: Optional[string]


class CreateDistributionRequest(ServiceRequest):
    """The request to create a new distribution."""

    DistributionConfig: DistributionConfig


class CreateDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Distribution: Optional[Distribution]
    Location: Optional[string]
    ETag: Optional[string]


class ManagedCertificateRequest(TypedDict, total=False):
    """An object that represents the request for the Amazon CloudFront managed
    ACM certificate.
    """

    ValidationTokenHost: ValidationTokenHost
    PrimaryDomainName: Optional[string]
    CertificateTransparencyLoggingPreference: Optional[CertificateTransparencyLoggingPreference]


class Parameter(TypedDict, total=False):
    """A list of parameter values to add to the resource. A parameter is
    specified as a key-value pair. A valid parameter value must exist for
    any parameter that is marked as required in the multi-tenant
    distribution.
    """

    Name: ParameterName
    Value: ParameterValue


Parameters = List[Parameter]


class GeoRestrictionCustomization(TypedDict, total=False):
    """The customizations that you specified for the distribution tenant for
    geographic restrictions.
    """

    RestrictionType: GeoRestrictionType
    Locations: Optional[LocationList]


class WebAclCustomization(TypedDict, total=False):
    """The WAF web ACL customization specified for the distribution tenant."""

    Action: CustomizationActionType
    Arn: Optional[string]


class Customizations(TypedDict, total=False):
    """Customizations for the distribution tenant. For each distribution
    tenant, you can specify the geographic restrictions, and the Amazon
    Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are
    specific values that you can override or disable from the multi-tenant
    distribution that was used to create the distribution tenant.
    """

    WebAcl: Optional[WebAclCustomization]
    Certificate: Optional[Certificate]
    GeoRestrictions: Optional[GeoRestrictionCustomization]


class DomainItem(TypedDict, total=False):
    """The domain for the specified distribution tenant."""

    Domain: string


DomainList = List[DomainItem]


class CreateDistributionTenantRequest(ServiceRequest):
    DistributionId: string
    Name: CreateDistributionTenantRequestNameString
    Domains: DomainList
    Tags: Optional[Tags]
    Customizations: Optional[Customizations]
    Parameters: Optional[Parameters]
    ConnectionGroupId: Optional[string]
    ManagedCertificateRequest: Optional[ManagedCertificateRequest]
    Enabled: Optional[boolean]


class DomainResult(TypedDict, total=False):
    """The details about the domain result."""

    Domain: string
    Status: Optional[DomainStatus]


DomainResultList = List[DomainResult]


class DistributionTenant(TypedDict, total=False):
    """The distribution tenant."""

    Id: Optional[string]
    DistributionId: Optional[string]
    Name: Optional[string]
    Arn: Optional[string]
    Domains: Optional[DomainResultList]
    Tags: Optional[Tags]
    Customizations: Optional[Customizations]
    Parameters: Optional[Parameters]
    ConnectionGroupId: Optional[string]
    CreatedTime: Optional[timestamp]
    LastModifiedTime: Optional[timestamp]
    Enabled: Optional[boolean]
    Status: Optional[string]


class CreateDistributionTenantResult(TypedDict, total=False):
    DistributionTenant: Optional[DistributionTenant]
    ETag: Optional[string]


class DistributionConfigWithTags(TypedDict, total=False):
    """A distribution Configuration and a list of tags to be associated with
    the distribution.
    """

    DistributionConfig: DistributionConfig
    Tags: Tags


class CreateDistributionWithTagsRequest(ServiceRequest):
    """The request to create a new distribution with tags."""

    DistributionConfigWithTags: DistributionConfigWithTags


class CreateDistributionWithTagsResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Distribution: Optional[Distribution]
    Location: Optional[string]
    ETag: Optional[string]


class QueryArgProfile(TypedDict, total=False):
    """Query argument-profile mapping for field-level encryption."""

    QueryArg: string
    ProfileId: string


QueryArgProfileList = List[QueryArgProfile]


class QueryArgProfiles(TypedDict, total=False):
    """Query argument-profile mapping for field-level encryption."""

    Quantity: integer
    Items: Optional[QueryArgProfileList]


class QueryArgProfileConfig(TypedDict, total=False):
    """Configuration for query argument-profile mapping for field-level
    encryption.
    """

    ForwardWhenQueryArgProfileIsUnknown: boolean
    QueryArgProfiles: Optional[QueryArgProfiles]


class FieldLevelEncryptionConfig(TypedDict, total=False):
    """A complex data type that includes the profile configurations specified
    for field-level encryption.
    """

    CallerReference: string
    Comment: Optional[string]
    QueryArgProfileConfig: Optional[QueryArgProfileConfig]
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfig]


class CreateFieldLevelEncryptionConfigRequest(ServiceRequest):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfig


class FieldLevelEncryption(TypedDict, total=False):
    """A complex data type that includes the profile configurations and other
    options specified for field-level encryption.
    """

    Id: string
    LastModifiedTime: timestamp
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfig


class CreateFieldLevelEncryptionConfigResult(TypedDict, total=False):
    FieldLevelEncryption: Optional[FieldLevelEncryption]
    Location: Optional[string]
    ETag: Optional[string]


FieldPatternList = List[string]


class FieldPatterns(TypedDict, total=False):
    """A complex data type that includes the field patterns to match for
    field-level encryption.
    """

    Quantity: integer
    Items: Optional[FieldPatternList]


class EncryptionEntity(TypedDict, total=False):
    """Complex data type for field-level encryption profiles that includes the
    encryption key and field pattern specifications.
    """

    PublicKeyId: string
    ProviderId: string
    FieldPatterns: FieldPatterns


EncryptionEntityList = List[EncryptionEntity]


class EncryptionEntities(TypedDict, total=False):
    """Complex data type for field-level encryption profiles that includes all
    of the encryption entities.
    """

    Quantity: integer
    Items: Optional[EncryptionEntityList]


class FieldLevelEncryptionProfileConfig(TypedDict, total=False):
    """A complex data type of profiles for the field-level encryption."""

    Name: string
    CallerReference: string
    Comment: Optional[string]
    EncryptionEntities: EncryptionEntities


class CreateFieldLevelEncryptionProfileRequest(ServiceRequest):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfig


class FieldLevelEncryptionProfile(TypedDict, total=False):
    """A complex data type for field-level encryption profiles."""

    Id: string
    LastModifiedTime: timestamp
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfig


class CreateFieldLevelEncryptionProfileResult(TypedDict, total=False):
    FieldLevelEncryptionProfile: Optional[FieldLevelEncryptionProfile]
    Location: Optional[string]
    ETag: Optional[string]


FunctionBlob = bytes


class KeyValueStoreAssociation(TypedDict, total=False):
    """The key value store association."""

    KeyValueStoreARN: KeyValueStoreARN


KeyValueStoreAssociationList = List[KeyValueStoreAssociation]


class KeyValueStoreAssociations(TypedDict, total=False):
    """The key value store associations."""

    Quantity: integer
    Items: Optional[KeyValueStoreAssociationList]


class FunctionConfig(TypedDict, total=False):
    """Contains configuration information about a CloudFront function."""

    Comment: string
    Runtime: FunctionRuntime
    KeyValueStoreAssociations: Optional[KeyValueStoreAssociations]


class CreateFunctionRequest(ServiceRequest):
    Name: FunctionName
    FunctionConfig: FunctionConfig
    FunctionCode: FunctionBlob


class FunctionMetadata(TypedDict, total=False):
    """Contains metadata about a CloudFront function."""

    FunctionARN: string
    Stage: Optional[FunctionStage]
    CreatedTime: Optional[timestamp]
    LastModifiedTime: timestamp


class FunctionSummary(TypedDict, total=False):
    """Contains configuration information and metadata about a CloudFront
    function.
    """

    Name: FunctionName
    Status: Optional[string]
    FunctionConfig: FunctionConfig
    FunctionMetadata: FunctionMetadata


class CreateFunctionResult(TypedDict, total=False):
    FunctionSummary: Optional[FunctionSummary]
    Location: Optional[string]
    ETag: Optional[string]


PathList = List[string]


class Paths(TypedDict, total=False):
    """A complex type that contains information about the objects that you want
    to invalidate. For more information, see `Specifying the Objects to
    Invalidate <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Quantity: integer
    Items: Optional[PathList]


class InvalidationBatch(TypedDict, total=False):
    """An invalidation batch."""

    Paths: Paths
    CallerReference: string


class CreateInvalidationForDistributionTenantRequest(ServiceRequest):
    Id: string
    InvalidationBatch: InvalidationBatch


class Invalidation(TypedDict, total=False):
    """An invalidation."""

    Id: string
    Status: string
    CreateTime: timestamp
    InvalidationBatch: InvalidationBatch


class CreateInvalidationForDistributionTenantResult(TypedDict, total=False):
    Location: Optional[string]
    Invalidation: Optional[Invalidation]


class CreateInvalidationRequest(ServiceRequest):
    """The request to create an invalidation."""

    DistributionId: string
    InvalidationBatch: InvalidationBatch


class CreateInvalidationResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Location: Optional[string]
    Invalidation: Optional[Invalidation]


PublicKeyIdList = List[string]


class KeyGroupConfig(TypedDict, total=False):
    """A key group configuration.

    A key group contains a list of public keys that you can use with
    `CloudFront signed URLs and signed
    cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__.
    """

    Name: string
    Items: PublicKeyIdList
    Comment: Optional[string]


class CreateKeyGroupRequest(ServiceRequest):
    KeyGroupConfig: KeyGroupConfig


class KeyGroup(TypedDict, total=False):
    """A key group.

    A key group contains a list of public keys that you can use with
    `CloudFront signed URLs and signed
    cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__.
    """

    Id: string
    LastModifiedTime: timestamp
    KeyGroupConfig: KeyGroupConfig


class CreateKeyGroupResult(TypedDict, total=False):
    KeyGroup: Optional[KeyGroup]
    Location: Optional[string]
    ETag: Optional[string]


class ImportSource(TypedDict, total=False):
    """The import source for the key value store."""

    SourceType: ImportSourceType
    SourceARN: string


class CreateKeyValueStoreRequest(ServiceRequest):
    Name: KeyValueStoreName
    Comment: Optional[KeyValueStoreComment]
    ImportSource: Optional[ImportSource]


class KeyValueStore(TypedDict, total=False):
    """The key value store. Use this to separate data from function code,
    allowing you to update data without having to publish a new version of a
    function. The key value store holds keys and their corresponding values.
    """

    Name: string
    Id: string
    Comment: string
    ARN: string
    Status: Optional[string]
    LastModifiedTime: timestamp


class CreateKeyValueStoreResult(TypedDict, total=False):
    KeyValueStore: Optional[KeyValueStore]
    ETag: Optional[string]
    Location: Optional[string]


class RealtimeMetricsSubscriptionConfig(TypedDict, total=False):
    """A subscription configuration for additional CloudWatch metrics."""

    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatus


class MonitoringSubscription(TypedDict, total=False):
    """A monitoring subscription. This structure contains information about
    whether additional CloudWatch metrics are enabled for a given CloudFront
    distribution.
    """

    RealtimeMetricsSubscriptionConfig: Optional[RealtimeMetricsSubscriptionConfig]


class CreateMonitoringSubscriptionRequest(ServiceRequest):
    DistributionId: string
    MonitoringSubscription: MonitoringSubscription


class CreateMonitoringSubscriptionResult(TypedDict, total=False):
    MonitoringSubscription: Optional[MonitoringSubscription]


class OriginAccessControlConfig(TypedDict, total=False):
    """A CloudFront origin access control configuration."""

    Name: string
    Description: Optional[string]
    SigningProtocol: OriginAccessControlSigningProtocols
    SigningBehavior: OriginAccessControlSigningBehaviors
    OriginAccessControlOriginType: OriginAccessControlOriginTypes


class CreateOriginAccessControlRequest(ServiceRequest):
    OriginAccessControlConfig: OriginAccessControlConfig


class OriginAccessControl(TypedDict, total=False):
    """A CloudFront origin access control, including its unique identifier."""

    Id: string
    OriginAccessControlConfig: Optional[OriginAccessControlConfig]


class CreateOriginAccessControlResult(TypedDict, total=False):
    OriginAccessControl: Optional[OriginAccessControl]
    Location: Optional[string]
    ETag: Optional[string]


class OriginRequestPolicyQueryStringsConfig(TypedDict, total=False):
    """An object that determines whether any URL query strings in viewer
    requests (and if so, which query strings) are included in requests that
    CloudFront sends to the origin.
    """

    QueryStringBehavior: OriginRequestPolicyQueryStringBehavior
    QueryStrings: Optional[QueryStringNames]


class OriginRequestPolicyCookiesConfig(TypedDict, total=False):
    """An object that determines whether any cookies in viewer requests (and if
    so, which cookies) are included in requests that CloudFront sends to the
    origin.
    """

    CookieBehavior: OriginRequestPolicyCookieBehavior
    Cookies: Optional[CookieNames]


class OriginRequestPolicyHeadersConfig(TypedDict, total=False):
    """An object that determines whether any HTTP headers (and if so, which
    headers) are included in requests that CloudFront sends to the origin.
    """

    HeaderBehavior: OriginRequestPolicyHeaderBehavior
    Headers: Optional[Headers]


class OriginRequestPolicyConfig(TypedDict, total=False):
    """An origin request policy configuration.

    This configuration determines the values that CloudFront includes in
    requests that it sends to the origin. Each request that CloudFront sends
    to the origin includes the following:

    -  The request body and the URL path (without the domain name) from the
       viewer request.

    -  The headers that CloudFront automatically includes in every origin
       request, including ``Host``, ``User-Agent``, and ``X-Amz-Cf-Id``.

    -  All HTTP headers, cookies, and URL query strings that are specified
       in the cache policy or the origin request policy. These can include
       items from the viewer request and, in the case of headers, additional
       ones that are added by CloudFront.

    CloudFront sends a request when it can't find an object in its cache
    that matches the request. If you want to send values to the origin and
    also include them in the cache key, use ``CachePolicy``.
    """

    Comment: Optional[string]
    Name: string
    HeadersConfig: OriginRequestPolicyHeadersConfig
    CookiesConfig: OriginRequestPolicyCookiesConfig
    QueryStringsConfig: OriginRequestPolicyQueryStringsConfig


class CreateOriginRequestPolicyRequest(ServiceRequest):
    OriginRequestPolicyConfig: OriginRequestPolicyConfig


class OriginRequestPolicy(TypedDict, total=False):
    """An origin request policy.

    When it's attached to a cache behavior, the origin request policy
    determines the values that CloudFront includes in requests that it sends
    to the origin. Each request that CloudFront sends to the origin includes
    the following:

    -  The request body and the URL path (without the domain name) from the
       viewer request.

    -  The headers that CloudFront automatically includes in every origin
       request, including ``Host``, ``User-Agent``, and ``X-Amz-Cf-Id``.

    -  All HTTP headers, cookies, and URL query strings that are specified
       in the cache policy or the origin request policy. These can include
       items from the viewer request and, in the case of headers, additional
       ones that are added by CloudFront.

    CloudFront sends a request when it can't find an object in its cache
    that matches the request. If you want to send values to the origin and
    also include them in the cache key, use ``CachePolicy``.
    """

    Id: string
    LastModifiedTime: timestamp
    OriginRequestPolicyConfig: OriginRequestPolicyConfig


class CreateOriginRequestPolicyResult(TypedDict, total=False):
    OriginRequestPolicy: Optional[OriginRequestPolicy]
    Location: Optional[string]
    ETag: Optional[string]


class PublicKeyConfig(TypedDict, total=False):
    """Configuration information about a public key that you can use with
    `signed URLs and signed
    cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__,
    or with `field-level
    encryption <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html>`__.
    """

    CallerReference: string
    Name: string
    EncodedKey: string
    Comment: Optional[string]


class CreatePublicKeyRequest(ServiceRequest):
    PublicKeyConfig: PublicKeyConfig


class PublicKey(TypedDict, total=False):
    """A public key that you can use with `signed URLs and signed
    cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__,
    or with `field-level
    encryption <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html>`__.
    """

    Id: string
    CreatedTime: timestamp
    PublicKeyConfig: PublicKeyConfig


class CreatePublicKeyResult(TypedDict, total=False):
    PublicKey: Optional[PublicKey]
    Location: Optional[string]
    ETag: Optional[string]


FieldList = List[string]


class KinesisStreamConfig(TypedDict, total=False):
    """Contains information about the Amazon Kinesis data stream where you are
    sending real-time log data.
    """

    RoleARN: string
    StreamARN: string


class EndPoint(TypedDict, total=False):
    """Contains information about the Amazon Kinesis data stream where you're
    sending real-time log data in a real-time log configuration.
    """

    StreamType: string
    KinesisStreamConfig: Optional[KinesisStreamConfig]


EndPointList = List[EndPoint]


class CreateRealtimeLogConfigRequest(ServiceRequest):
    EndPoints: EndPointList
    Fields: FieldList
    Name: string
    SamplingRate: long


class RealtimeLogConfig(TypedDict, total=False):
    """A real-time log configuration."""

    ARN: string
    Name: string
    SamplingRate: long
    EndPoints: EndPointList
    Fields: FieldList


class CreateRealtimeLogConfigResult(TypedDict, total=False):
    RealtimeLogConfig: Optional[RealtimeLogConfig]


class ResponseHeadersPolicyRemoveHeader(TypedDict, total=False):
    """The name of an HTTP header that CloudFront removes from HTTP responses
    to requests that match the cache behavior that this response headers
    policy is attached to.
    """

    Header: string


ResponseHeadersPolicyRemoveHeaderList = List[ResponseHeadersPolicyRemoveHeader]


class ResponseHeadersPolicyRemoveHeadersConfig(TypedDict, total=False):
    """A list of HTTP header names that CloudFront removes from HTTP responses
    to requests that match the cache behavior that this response headers
    policy is attached to.
    """

    Quantity: integer
    Items: Optional[ResponseHeadersPolicyRemoveHeaderList]


class ResponseHeadersPolicyCustomHeader(TypedDict, total=False):
    """An HTTP response header name and its value. CloudFront includes this
    header in HTTP responses that it sends for requests that match a cache
    behavior that's associated with this response headers policy.
    """

    Header: string
    Value: string
    Override: boolean


ResponseHeadersPolicyCustomHeaderList = List[ResponseHeadersPolicyCustomHeader]


class ResponseHeadersPolicyCustomHeadersConfig(TypedDict, total=False):
    """A list of HTTP response header names and their values. CloudFront
    includes these headers in HTTP responses that it sends for requests that
    match a cache behavior that's associated with this response headers
    policy.
    """

    Quantity: integer
    Items: Optional[ResponseHeadersPolicyCustomHeaderList]


class ResponseHeadersPolicyServerTimingHeadersConfig(TypedDict, total=False):
    """A configuration for enabling the ``Server-Timing`` header in HTTP
    responses sent from CloudFront. CloudFront adds this header to HTTP
    responses that it sends in response to requests that match a cache
    behavior that's associated with this response headers policy.

    You can use the ``Server-Timing`` header to view metrics that can help
    you gain insights about the behavior and performance of CloudFront. For
    example, you can see which cache layer served a cache hit, or the first
    byte latency from the origin when there was a cache miss. You can use
    the metrics in the ``Server-Timing`` header to troubleshoot issues or
    test the efficiency of your CloudFront configuration. For more
    information, see `Server-Timing
    header <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#server-timing-header>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Enabled: boolean
    SamplingRate: Optional[SamplingRate]


class ResponseHeadersPolicyStrictTransportSecurity(TypedDict, total=False):
    """Determines whether CloudFront includes the ``Strict-Transport-Security``
    HTTP response header and the header's value.

    For more information about the ``Strict-Transport-Security`` HTTP
    response header, see
    `Strict-Transport-Security <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__
    in the MDN Web Docs.
    """

    Override: boolean
    IncludeSubdomains: Optional[boolean]
    Preload: Optional[boolean]
    AccessControlMaxAgeSec: integer


class ResponseHeadersPolicyContentTypeOptions(TypedDict, total=False):
    """Determines whether CloudFront includes the ``X-Content-Type-Options``
    HTTP response header with its value set to ``nosniff``.

    For more information about the ``X-Content-Type-Options`` HTTP response
    header, see
    `X-Content-Type-Options <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options>`__
    in the MDN Web Docs.
    """

    Override: boolean


class ResponseHeadersPolicyContentSecurityPolicy(TypedDict, total=False):
    """The policy directives and their values that CloudFront includes as
    values for the ``Content-Security-Policy`` HTTP response header.

    For more information about the ``Content-Security-Policy`` HTTP response
    header, see
    `Content-Security-Policy <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>`__
    in the MDN Web Docs.
    """

    Override: boolean
    ContentSecurityPolicy: string


class ResponseHeadersPolicyReferrerPolicy(TypedDict, total=False):
    """Determines whether CloudFront includes the ``Referrer-Policy`` HTTP
    response header and the header's value.

    For more information about the ``Referrer-Policy`` HTTP response header,
    see
    `Referrer-Policy <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy>`__
    in the MDN Web Docs.
    """

    Override: boolean
    ReferrerPolicy: ReferrerPolicyList


class ResponseHeadersPolicyFrameOptions(TypedDict, total=False):
    """Determines whether CloudFront includes the ``X-Frame-Options`` HTTP
    response header and the header's value.

    For more information about the ``X-Frame-Options`` HTTP response header,
    see
    `X-Frame-Options <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options>`__
    in the MDN Web Docs.
    """

    Override: boolean
    FrameOption: FrameOptionsList


class ResponseHeadersPolicyXSSProtection(TypedDict, total=False):
    """Determines whether CloudFront includes the ``X-XSS-Protection`` HTTP
    response header and the header's value.

    For more information about the ``X-XSS-Protection`` HTTP response
    header, see
    `X-XSS-Protection <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection>`__
    in the MDN Web Docs.
    """

    Override: boolean
    Protection: boolean
    ModeBlock: Optional[boolean]
    ReportUri: Optional[string]


class ResponseHeadersPolicySecurityHeadersConfig(TypedDict, total=False):
    """A configuration for a set of security-related HTTP response headers.
    CloudFront adds these headers to HTTP responses that it sends for
    requests that match a cache behavior associated with this response
    headers policy.
    """

    XSSProtection: Optional[ResponseHeadersPolicyXSSProtection]
    FrameOptions: Optional[ResponseHeadersPolicyFrameOptions]
    ReferrerPolicy: Optional[ResponseHeadersPolicyReferrerPolicy]
    ContentSecurityPolicy: Optional[ResponseHeadersPolicyContentSecurityPolicy]
    ContentTypeOptions: Optional[ResponseHeadersPolicyContentTypeOptions]
    StrictTransportSecurity: Optional[ResponseHeadersPolicyStrictTransportSecurity]


class ResponseHeadersPolicyAccessControlExposeHeaders(TypedDict, total=False):
    """A list of HTTP headers that CloudFront includes as values for the
    ``Access-Control-Expose-Headers`` HTTP response header.

    For more information about the ``Access-Control-Expose-Headers`` HTTP
    response header, see
    `Access-Control-Expose-Headers <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers>`__
    in the MDN Web Docs.
    """

    Quantity: integer
    Items: Optional[AccessControlExposeHeadersList]


class ResponseHeadersPolicyAccessControlAllowMethods(TypedDict, total=False):
    """A list of HTTP methods that CloudFront includes as values for the
    ``Access-Control-Allow-Methods`` HTTP response header.

    For more information about the ``Access-Control-Allow-Methods`` HTTP
    response header, see
    `Access-Control-Allow-Methods <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods>`__
    in the MDN Web Docs.
    """

    Quantity: integer
    Items: AccessControlAllowMethodsList


class ResponseHeadersPolicyAccessControlAllowHeaders(TypedDict, total=False):
    """A list of HTTP header names that CloudFront includes as values for the
    ``Access-Control-Allow-Headers`` HTTP response header.

    For more information about the ``Access-Control-Allow-Headers`` HTTP
    response header, see
    `Access-Control-Allow-Headers <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers>`__
    in the MDN Web Docs.
    """

    Quantity: integer
    Items: AccessControlAllowHeadersList


class ResponseHeadersPolicyAccessControlAllowOrigins(TypedDict, total=False):
    """A list of origins (domain names) that CloudFront can use as the value
    for the ``Access-Control-Allow-Origin`` HTTP response header.

    For more information about the ``Access-Control-Allow-Origin`` HTTP
    response header, see
    `Access-Control-Allow-Origin <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin>`__
    in the MDN Web Docs.
    """

    Quantity: integer
    Items: AccessControlAllowOriginsList


class ResponseHeadersPolicyCorsConfig(TypedDict, total=False):
    """A configuration for a set of HTTP response headers that are used for
    cross-origin resource sharing (CORS). CloudFront adds these headers to
    HTTP responses that it sends for CORS requests that match a cache
    behavior associated with this response headers policy.

    For more information about CORS, see `Cross-Origin Resource Sharing
    (CORS) <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`__ in
    the MDN Web Docs.
    """

    AccessControlAllowOrigins: ResponseHeadersPolicyAccessControlAllowOrigins
    AccessControlAllowHeaders: ResponseHeadersPolicyAccessControlAllowHeaders
    AccessControlAllowMethods: ResponseHeadersPolicyAccessControlAllowMethods
    AccessControlAllowCredentials: boolean
    AccessControlExposeHeaders: Optional[ResponseHeadersPolicyAccessControlExposeHeaders]
    AccessControlMaxAgeSec: Optional[integer]
    OriginOverride: boolean


class ResponseHeadersPolicyConfig(TypedDict, total=False):
    """A response headers policy configuration.

    A response headers policy configuration contains metadata about the
    response headers policy, and configurations for sets of HTTP response
    headers.
    """

    Comment: Optional[string]
    Name: string
    CorsConfig: Optional[ResponseHeadersPolicyCorsConfig]
    SecurityHeadersConfig: Optional[ResponseHeadersPolicySecurityHeadersConfig]
    ServerTimingHeadersConfig: Optional[ResponseHeadersPolicyServerTimingHeadersConfig]
    CustomHeadersConfig: Optional[ResponseHeadersPolicyCustomHeadersConfig]
    RemoveHeadersConfig: Optional[ResponseHeadersPolicyRemoveHeadersConfig]


class CreateResponseHeadersPolicyRequest(ServiceRequest):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfig


class ResponseHeadersPolicy(TypedDict, total=False):
    """A response headers policy.

    A response headers policy contains information about a set of HTTP
    response headers.

    After you create a response headers policy, you can use its ID to attach
    it to one or more cache behaviors in a CloudFront distribution. When
    it's attached to a cache behavior, the response headers policy affects
    the HTTP headers that CloudFront includes in HTTP responses to requests
    that match the cache behavior. CloudFront adds or removes response
    headers according to the configuration of the response headers policy.

    For more information, see `Adding or removing HTTP headers in CloudFront
    responses <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Id: string
    LastModifiedTime: timestamp
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfig


class CreateResponseHeadersPolicyResult(TypedDict, total=False):
    ResponseHeadersPolicy: Optional[ResponseHeadersPolicy]
    Location: Optional[string]
    ETag: Optional[string]


class StreamingLoggingConfig(TypedDict, total=False):
    """A complex type that controls whether access logs are written for this
    streaming distribution.
    """

    Enabled: boolean
    Bucket: string
    Prefix: string


class S3Origin(TypedDict, total=False):
    """A complex type that contains information about the Amazon S3 bucket from
    which you want CloudFront to get your media files for distribution.
    """

    DomainName: string
    OriginAccessIdentity: string


class StreamingDistributionConfig(TypedDict, total=False):
    """The RTMP distribution's configuration information."""

    CallerReference: string
    S3Origin: S3Origin
    Aliases: Optional[Aliases]
    Comment: string
    Logging: Optional[StreamingLoggingConfig]
    TrustedSigners: TrustedSigners
    PriceClass: Optional[PriceClass]
    Enabled: boolean


class CreateStreamingDistributionRequest(ServiceRequest):
    """The request to create a new streaming distribution."""

    StreamingDistributionConfig: StreamingDistributionConfig


class StreamingDistribution(TypedDict, total=False):
    """A streaming distribution tells CloudFront where you want RTMP content to
    be delivered from, and the details about how to track and manage content
    delivery.
    """

    Id: string
    ARN: string
    Status: string
    LastModifiedTime: Optional[timestamp]
    DomainName: string
    ActiveTrustedSigners: ActiveTrustedSigners
    StreamingDistributionConfig: StreamingDistributionConfig


class CreateStreamingDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistribution: Optional[StreamingDistribution]
    Location: Optional[string]
    ETag: Optional[string]


class StreamingDistributionConfigWithTags(TypedDict, total=False):
    """A streaming distribution Configuration and a list of tags to be
    associated with the streaming distribution.
    """

    StreamingDistributionConfig: StreamingDistributionConfig
    Tags: Tags


class CreateStreamingDistributionWithTagsRequest(ServiceRequest):
    """The request to create a new streaming distribution with tags."""

    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTags


class CreateStreamingDistributionWithTagsResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistribution: Optional[StreamingDistribution]
    Location: Optional[string]
    ETag: Optional[string]


class VpcOriginEndpointConfig(TypedDict, total=False):
    """An Amazon CloudFront VPC origin endpoint configuration."""

    Name: string
    Arn: string
    HTTPPort: integer
    HTTPSPort: integer
    OriginProtocolPolicy: OriginProtocolPolicy
    OriginSslProtocols: Optional[OriginSslProtocols]


class CreateVpcOriginRequest(ServiceRequest):
    VpcOriginEndpointConfig: VpcOriginEndpointConfig
    Tags: Optional[Tags]


class VpcOrigin(TypedDict, total=False):
    """An Amazon CloudFront VPC origin."""

    Id: string
    Arn: string
    Status: string
    CreatedTime: timestamp
    LastModifiedTime: timestamp
    VpcOriginEndpointConfig: VpcOriginEndpointConfig


class CreateVpcOriginResult(TypedDict, total=False):
    VpcOrigin: Optional[VpcOrigin]
    Location: Optional[string]
    ETag: Optional[string]


class DeleteAnycastIpListRequest(ServiceRequest):
    Id: string
    IfMatch: string


class DeleteCachePolicyRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteCloudFrontOriginAccessIdentityRequest(ServiceRequest):
    """Deletes a origin access identity."""

    Id: string
    IfMatch: Optional[string]


class DeleteConnectionGroupRequest(ServiceRequest):
    Id: string
    IfMatch: string


class DeleteContinuousDeploymentPolicyRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteDistributionRequest(ServiceRequest):
    """This action deletes a web distribution. To delete a web distribution
    using the CloudFront API, perform the following steps.

    **To delete a web distribution using the CloudFront API:**

    #. Disable the web distribution

    #. Submit a ``GET Distribution Config`` request to get the current
       configuration and the ``Etag`` header for the distribution.

    #. Update the XML document that was returned in the response to your
       ``GET Distribution Config`` request to change the value of
       ``Enabled`` to ``false``.

    #. Submit a ``PUT Distribution Config`` request to update the
       configuration for your distribution. In the request body, include the
       XML document that you updated in Step 3. Set the value of the HTTP
       ``If-Match`` header to the value of the ``ETag`` header that
       CloudFront returned when you submitted the
       ``GET Distribution Config`` request in Step 2.

    #. Review the response to the ``PUT Distribution Config`` request to
       confirm that the distribution was successfully disabled.

    #. Submit a ``GET Distribution`` request to confirm that your changes
       have propagated. When propagation is complete, the value of
       ``Status`` is ``Deployed``.

    #. Submit a ``DELETE Distribution`` request. Set the value of the HTTP
       ``If-Match`` header to the value of the ``ETag`` header that
       CloudFront returned when you submitted the
       ``GET Distribution Config`` request in Step 6.

    #. Review the response to your ``DELETE Distribution`` request to
       confirm that the distribution was successfully deleted.

    For information about deleting a distribution using the CloudFront
    console, see `Deleting a
    Distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Id: string
    IfMatch: Optional[string]


class DeleteDistributionTenantRequest(ServiceRequest):
    Id: string
    IfMatch: string


class DeleteFieldLevelEncryptionConfigRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteFieldLevelEncryptionProfileRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteFunctionRequest(ServiceRequest):
    Name: string
    IfMatch: string


class DeleteKeyGroupRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteKeyValueStoreRequest(ServiceRequest):
    Name: KeyValueStoreName
    IfMatch: string


class DeleteMonitoringSubscriptionRequest(ServiceRequest):
    DistributionId: string


class DeleteMonitoringSubscriptionResult(TypedDict, total=False):
    pass


class DeleteOriginAccessControlRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteOriginRequestPolicyRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeletePublicKeyRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteRealtimeLogConfigRequest(ServiceRequest):
    Name: Optional[string]
    ARN: Optional[string]


class DeleteResponseHeadersPolicyRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DeleteStreamingDistributionRequest(ServiceRequest):
    """The request to delete a streaming distribution."""

    Id: string
    IfMatch: Optional[string]


class DeleteVpcOriginRequest(ServiceRequest):
    Id: string
    IfMatch: string


class DeleteVpcOriginResult(TypedDict, total=False):
    VpcOrigin: Optional[VpcOrigin]
    ETag: Optional[string]


class DescribeFunctionRequest(ServiceRequest):
    Name: string
    Stage: Optional[FunctionStage]


class DescribeFunctionResult(TypedDict, total=False):
    FunctionSummary: Optional[FunctionSummary]
    ETag: Optional[string]


class DescribeKeyValueStoreRequest(ServiceRequest):
    Name: KeyValueStoreName


class DescribeKeyValueStoreResult(TypedDict, total=False):
    KeyValueStore: Optional[KeyValueStore]
    ETag: Optional[string]


class DisassociateDistributionTenantWebACLRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DisassociateDistributionTenantWebACLResult(TypedDict, total=False):
    Id: Optional[string]
    ETag: Optional[string]


class DisassociateDistributionWebACLRequest(ServiceRequest):
    Id: string
    IfMatch: Optional[string]


class DisassociateDistributionWebACLResult(TypedDict, total=False):
    Id: Optional[string]
    ETag: Optional[string]


DistributionIdListSummary = List[string]


class DistributionIdList(TypedDict, total=False):
    """A list of distribution IDs."""

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[DistributionIdListSummary]


class DistributionSummary(TypedDict, total=False):
    """A summary of the information about a CloudFront distribution."""

    Id: string
    ARN: string
    ETag: Optional[string]
    Status: string
    LastModifiedTime: timestamp
    DomainName: string
    Aliases: Aliases
    Origins: Origins
    OriginGroups: Optional[OriginGroups]
    DefaultCacheBehavior: DefaultCacheBehavior
    CacheBehaviors: CacheBehaviors
    CustomErrorResponses: CustomErrorResponses
    Comment: string
    PriceClass: PriceClass
    Enabled: boolean
    ViewerCertificate: ViewerCertificate
    Restrictions: Restrictions
    WebACLId: string
    HttpVersion: HttpVersion
    IsIPV6Enabled: boolean
    AliasICPRecordals: Optional[AliasICPRecordals]
    Staging: boolean
    ConnectionMode: Optional[ConnectionMode]
    AnycastIpListId: Optional[string]


DistributionSummaryList = List[DistributionSummary]


class DistributionList(TypedDict, total=False):
    """A distribution list."""

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[DistributionSummaryList]


class DistributionResourceId(TypedDict, total=False):
    """The IDs for the distribution resources."""

    DistributionId: Optional[string]
    DistributionTenantId: Optional[string]


class DistributionTenantAssociationFilter(TypedDict, total=False):
    """Filter by the associated distribution ID or connection group ID."""

    DistributionId: Optional[string]
    ConnectionGroupId: Optional[string]


class DistributionTenantSummary(TypedDict, total=False):
    """A summary of the information about a distribution tenant."""

    Id: string
    DistributionId: string
    Name: string
    Arn: string
    Domains: DomainResultList
    ConnectionGroupId: Optional[string]
    Customizations: Optional[Customizations]
    CreatedTime: timestamp
    LastModifiedTime: timestamp
    ETag: string
    Enabled: Optional[boolean]
    Status: Optional[string]


DistributionTenantList = List[DistributionTenantSummary]


class DnsConfiguration(TypedDict, total=False):
    """The DNS configuration for your domain names."""

    Domain: string
    Status: DnsConfigurationStatus
    Reason: Optional[string]


DnsConfigurationList = List[DnsConfiguration]


class DomainConflict(TypedDict, total=False):
    """Contains information about the domain conflict. Use this information to
    determine the affected domain, the related resource, and the affected
    Amazon Web Services account.
    """

    Domain: string
    ResourceType: DistributionResourceType
    ResourceId: string
    AccountId: string


DomainConflictsList = List[DomainConflict]


class FieldLevelEncryptionSummary(TypedDict, total=False):
    """A summary of a field-level encryption item."""

    Id: string
    LastModifiedTime: timestamp
    Comment: Optional[string]
    QueryArgProfileConfig: Optional[QueryArgProfileConfig]
    ContentTypeProfileConfig: Optional[ContentTypeProfileConfig]


FieldLevelEncryptionSummaryList = List[FieldLevelEncryptionSummary]


class FieldLevelEncryptionList(TypedDict, total=False):
    """List of field-level encryption configurations."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[FieldLevelEncryptionSummaryList]


class FieldLevelEncryptionProfileSummary(TypedDict, total=False):
    """The field-level encryption profile summary."""

    Id: string
    LastModifiedTime: timestamp
    Name: string
    EncryptionEntities: EncryptionEntities
    Comment: Optional[string]


FieldLevelEncryptionProfileSummaryList = List[FieldLevelEncryptionProfileSummary]


class FieldLevelEncryptionProfileList(TypedDict, total=False):
    """List of field-level encryption profiles."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[FieldLevelEncryptionProfileSummaryList]


FunctionEventObject = bytes
FunctionExecutionLogList = List[string]
FunctionSummaryList = List[FunctionSummary]


class FunctionList(TypedDict, total=False):
    """A list of CloudFront functions."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[FunctionSummaryList]


class GetAnycastIpListRequest(ServiceRequest):
    Id: string


class GetAnycastIpListResult(TypedDict, total=False):
    AnycastIpList: Optional[AnycastIpList]
    ETag: Optional[string]


class GetCachePolicyConfigRequest(ServiceRequest):
    Id: string


class GetCachePolicyConfigResult(TypedDict, total=False):
    CachePolicyConfig: Optional[CachePolicyConfig]
    ETag: Optional[string]


class GetCachePolicyRequest(ServiceRequest):
    Id: string


class GetCachePolicyResult(TypedDict, total=False):
    CachePolicy: Optional[CachePolicy]
    ETag: Optional[string]


class GetCloudFrontOriginAccessIdentityConfigRequest(ServiceRequest):
    """The origin access identity's configuration information. For more
    information, see
    `CloudFrontOriginAccessIdentityConfig <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CloudFrontOriginAccessIdentityConfig.html>`__.
    """

    Id: string


class GetCloudFrontOriginAccessIdentityConfigResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    CloudFrontOriginAccessIdentityConfig: Optional[CloudFrontOriginAccessIdentityConfig]
    ETag: Optional[string]


class GetCloudFrontOriginAccessIdentityRequest(ServiceRequest):
    """The request to get an origin access identity's information."""

    Id: string


class GetCloudFrontOriginAccessIdentityResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    CloudFrontOriginAccessIdentity: Optional[CloudFrontOriginAccessIdentity]
    ETag: Optional[string]


class GetConnectionGroupByRoutingEndpointRequest(ServiceRequest):
    RoutingEndpoint: string


class GetConnectionGroupByRoutingEndpointResult(TypedDict, total=False):
    ConnectionGroup: Optional[ConnectionGroup]
    ETag: Optional[string]


class GetConnectionGroupRequest(ServiceRequest):
    Identifier: string


class GetConnectionGroupResult(TypedDict, total=False):
    ConnectionGroup: Optional[ConnectionGroup]
    ETag: Optional[string]


class GetContinuousDeploymentPolicyConfigRequest(ServiceRequest):
    Id: string


class GetContinuousDeploymentPolicyConfigResult(TypedDict, total=False):
    ContinuousDeploymentPolicyConfig: Optional[ContinuousDeploymentPolicyConfig]
    ETag: Optional[string]


class GetContinuousDeploymentPolicyRequest(ServiceRequest):
    Id: string


class GetContinuousDeploymentPolicyResult(TypedDict, total=False):
    ContinuousDeploymentPolicy: Optional[ContinuousDeploymentPolicy]
    ETag: Optional[string]


class GetDistributionConfigRequest(ServiceRequest):
    """The request to get a distribution configuration."""

    Id: string


class GetDistributionConfigResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    DistributionConfig: Optional[DistributionConfig]
    ETag: Optional[string]


class GetDistributionRequest(ServiceRequest):
    """The request to get a distribution's information."""

    Id: string


class GetDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Distribution: Optional[Distribution]
    ETag: Optional[string]


class GetDistributionTenantByDomainRequest(ServiceRequest):
    Domain: string


class GetDistributionTenantByDomainResult(TypedDict, total=False):
    DistributionTenant: Optional[DistributionTenant]
    ETag: Optional[string]


class GetDistributionTenantRequest(ServiceRequest):
    Identifier: string


class GetDistributionTenantResult(TypedDict, total=False):
    DistributionTenant: Optional[DistributionTenant]
    ETag: Optional[string]


class GetFieldLevelEncryptionConfigRequest(ServiceRequest):
    Id: string


class GetFieldLevelEncryptionConfigResult(TypedDict, total=False):
    FieldLevelEncryptionConfig: Optional[FieldLevelEncryptionConfig]
    ETag: Optional[string]


class GetFieldLevelEncryptionProfileConfigRequest(ServiceRequest):
    Id: string


class GetFieldLevelEncryptionProfileConfigResult(TypedDict, total=False):
    FieldLevelEncryptionProfileConfig: Optional[FieldLevelEncryptionProfileConfig]
    ETag: Optional[string]


class GetFieldLevelEncryptionProfileRequest(ServiceRequest):
    Id: string


class GetFieldLevelEncryptionProfileResult(TypedDict, total=False):
    FieldLevelEncryptionProfile: Optional[FieldLevelEncryptionProfile]
    ETag: Optional[string]


class GetFieldLevelEncryptionRequest(ServiceRequest):
    Id: string


class GetFieldLevelEncryptionResult(TypedDict, total=False):
    FieldLevelEncryption: Optional[FieldLevelEncryption]
    ETag: Optional[string]


class GetFunctionRequest(ServiceRequest):
    Name: string
    Stage: Optional[FunctionStage]


class GetFunctionResult(TypedDict, total=False):
    FunctionCode: Optional[Union[FunctionBlob, IO[FunctionBlob], Iterable[FunctionBlob]]]
    ETag: Optional[string]
    ContentType: Optional[string]


class GetInvalidationForDistributionTenantRequest(ServiceRequest):
    DistributionTenantId: string
    Id: string


class GetInvalidationForDistributionTenantResult(TypedDict, total=False):
    Invalidation: Optional[Invalidation]


class GetInvalidationRequest(ServiceRequest):
    """The request to get an invalidation's information."""

    DistributionId: string
    Id: string


class GetInvalidationResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Invalidation: Optional[Invalidation]


class GetKeyGroupConfigRequest(ServiceRequest):
    Id: string


class GetKeyGroupConfigResult(TypedDict, total=False):
    KeyGroupConfig: Optional[KeyGroupConfig]
    ETag: Optional[string]


class GetKeyGroupRequest(ServiceRequest):
    Id: string


class GetKeyGroupResult(TypedDict, total=False):
    KeyGroup: Optional[KeyGroup]
    ETag: Optional[string]


class GetManagedCertificateDetailsRequest(ServiceRequest):
    Identifier: string


class ValidationTokenDetail(TypedDict, total=False):
    """Contains details about the validation token."""

    Domain: string
    RedirectTo: Optional[string]
    RedirectFrom: Optional[string]


ValidationTokenDetailList = List[ValidationTokenDetail]


class ManagedCertificateDetails(TypedDict, total=False):
    """Contains details about the CloudFront managed ACM certificate."""

    CertificateArn: Optional[string]
    CertificateStatus: Optional[ManagedCertificateStatus]
    ValidationTokenHost: Optional[ValidationTokenHost]
    ValidationTokenDetails: Optional[ValidationTokenDetailList]


class GetManagedCertificateDetailsResult(TypedDict, total=False):
    ManagedCertificateDetails: Optional[ManagedCertificateDetails]


class GetMonitoringSubscriptionRequest(ServiceRequest):
    DistributionId: string


class GetMonitoringSubscriptionResult(TypedDict, total=False):
    MonitoringSubscription: Optional[MonitoringSubscription]


class GetOriginAccessControlConfigRequest(ServiceRequest):
    Id: string


class GetOriginAccessControlConfigResult(TypedDict, total=False):
    OriginAccessControlConfig: Optional[OriginAccessControlConfig]
    ETag: Optional[string]


class GetOriginAccessControlRequest(ServiceRequest):
    Id: string


class GetOriginAccessControlResult(TypedDict, total=False):
    OriginAccessControl: Optional[OriginAccessControl]
    ETag: Optional[string]


class GetOriginRequestPolicyConfigRequest(ServiceRequest):
    Id: string


class GetOriginRequestPolicyConfigResult(TypedDict, total=False):
    OriginRequestPolicyConfig: Optional[OriginRequestPolicyConfig]
    ETag: Optional[string]


class GetOriginRequestPolicyRequest(ServiceRequest):
    Id: string


class GetOriginRequestPolicyResult(TypedDict, total=False):
    OriginRequestPolicy: Optional[OriginRequestPolicy]
    ETag: Optional[string]


class GetPublicKeyConfigRequest(ServiceRequest):
    Id: string


class GetPublicKeyConfigResult(TypedDict, total=False):
    PublicKeyConfig: Optional[PublicKeyConfig]
    ETag: Optional[string]


class GetPublicKeyRequest(ServiceRequest):
    Id: string


class GetPublicKeyResult(TypedDict, total=False):
    PublicKey: Optional[PublicKey]
    ETag: Optional[string]


class GetRealtimeLogConfigRequest(ServiceRequest):
    Name: Optional[string]
    ARN: Optional[string]


class GetRealtimeLogConfigResult(TypedDict, total=False):
    RealtimeLogConfig: Optional[RealtimeLogConfig]


class GetResponseHeadersPolicyConfigRequest(ServiceRequest):
    Id: string


class GetResponseHeadersPolicyConfigResult(TypedDict, total=False):
    ResponseHeadersPolicyConfig: Optional[ResponseHeadersPolicyConfig]
    ETag: Optional[string]


class GetResponseHeadersPolicyRequest(ServiceRequest):
    Id: string


class GetResponseHeadersPolicyResult(TypedDict, total=False):
    ResponseHeadersPolicy: Optional[ResponseHeadersPolicy]
    ETag: Optional[string]


class GetStreamingDistributionConfigRequest(ServiceRequest):
    """To request to get a streaming distribution configuration."""

    Id: string


class GetStreamingDistributionConfigResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistributionConfig: Optional[StreamingDistributionConfig]
    ETag: Optional[string]


class GetStreamingDistributionRequest(ServiceRequest):
    """The request to get a streaming distribution's information."""

    Id: string


class GetStreamingDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistribution: Optional[StreamingDistribution]
    ETag: Optional[string]


class GetVpcOriginRequest(ServiceRequest):
    Id: string


class GetVpcOriginResult(TypedDict, total=False):
    VpcOrigin: Optional[VpcOrigin]
    ETag: Optional[string]


class InvalidationSummary(TypedDict, total=False):
    """A summary of an invalidation request."""

    Id: string
    CreateTime: timestamp
    Status: string


InvalidationSummaryList = List[InvalidationSummary]


class InvalidationList(TypedDict, total=False):
    """The ``InvalidationList`` complex type describes the list of invalidation
    objects. For more information about invalidation, see `Invalidating
    Objects (Web Distributions
    Only) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html>`__
    in the *Amazon CloudFront Developer Guide*.
    """

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[InvalidationSummaryList]


class KeyGroupSummary(TypedDict, total=False):
    """Contains information about a key group."""

    KeyGroup: KeyGroup


KeyGroupSummaryList = List[KeyGroupSummary]


class KeyGroupList(TypedDict, total=False):
    """A list of key groups."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[KeyGroupSummaryList]


KeyValueStoreSummaryList = List[KeyValueStore]


class KeyValueStoreList(TypedDict, total=False):
    """The key value store list."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[KeyValueStoreSummaryList]


class ListAnycastIpListsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[integer]


class ListAnycastIpListsResult(TypedDict, total=False):
    AnycastIpLists: Optional[AnycastIpListCollection]


class ListCachePoliciesRequest(ServiceRequest):
    Type: Optional[CachePolicyType]
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListCachePoliciesResult(TypedDict, total=False):
    CachePolicyList: Optional[CachePolicyList]


class ListCloudFrontOriginAccessIdentitiesRequest(ServiceRequest):
    """The request to list origin access identities."""

    Marker: Optional[string]
    MaxItems: Optional[string]


class ListCloudFrontOriginAccessIdentitiesResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    CloudFrontOriginAccessIdentityList: Optional[CloudFrontOriginAccessIdentityList]


class ListConflictingAliasesRequest(ServiceRequest):
    DistributionId: distributionIdString
    Alias: aliasString
    Marker: Optional[string]
    MaxItems: Optional[listConflictingAliasesMaxItemsInteger]


class ListConflictingAliasesResult(TypedDict, total=False):
    ConflictingAliasesList: Optional[ConflictingAliasesList]


class ListConnectionGroupsRequest(ServiceRequest):
    AssociationFilter: Optional[ConnectionGroupAssociationFilter]
    Marker: Optional[string]
    MaxItems: Optional[integer]


class ListConnectionGroupsResult(TypedDict, total=False):
    NextMarker: Optional[string]
    ConnectionGroups: Optional[ConnectionGroupSummaryList]


class ListContinuousDeploymentPoliciesRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListContinuousDeploymentPoliciesResult(TypedDict, total=False):
    ContinuousDeploymentPolicyList: Optional[ContinuousDeploymentPolicyList]


class ListDistributionTenantsByCustomizationRequest(ServiceRequest):
    WebACLArn: Optional[string]
    CertificateArn: Optional[string]
    Marker: Optional[string]
    MaxItems: Optional[integer]


class ListDistributionTenantsByCustomizationResult(TypedDict, total=False):
    NextMarker: Optional[string]
    DistributionTenantList: Optional[DistributionTenantList]


class ListDistributionTenantsRequest(ServiceRequest):
    AssociationFilter: Optional[DistributionTenantAssociationFilter]
    Marker: Optional[string]
    MaxItems: Optional[integer]


class ListDistributionTenantsResult(TypedDict, total=False):
    NextMarker: Optional[string]
    DistributionTenantList: Optional[DistributionTenantList]


class ListDistributionsByAnycastIpListIdRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    AnycastIpListId: string


class ListDistributionsByAnycastIpListIdResult(TypedDict, total=False):
    DistributionList: Optional[DistributionList]


class ListDistributionsByCachePolicyIdRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    CachePolicyId: string


class ListDistributionsByCachePolicyIdResult(TypedDict, total=False):
    DistributionIdList: Optional[DistributionIdList]


class ListDistributionsByConnectionModeRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[integer]
    ConnectionMode: ConnectionMode


class ListDistributionsByConnectionModeResult(TypedDict, total=False):
    DistributionList: Optional[DistributionList]


class ListDistributionsByKeyGroupRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    KeyGroupId: string


class ListDistributionsByKeyGroupResult(TypedDict, total=False):
    DistributionIdList: Optional[DistributionIdList]


class ListDistributionsByOriginRequestPolicyIdRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    OriginRequestPolicyId: string


class ListDistributionsByOriginRequestPolicyIdResult(TypedDict, total=False):
    DistributionIdList: Optional[DistributionIdList]


class ListDistributionsByRealtimeLogConfigRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    RealtimeLogConfigName: Optional[string]
    RealtimeLogConfigArn: Optional[string]


class ListDistributionsByRealtimeLogConfigResult(TypedDict, total=False):
    DistributionList: Optional[DistributionList]


class ListDistributionsByResponseHeadersPolicyIdRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    ResponseHeadersPolicyId: string


class ListDistributionsByResponseHeadersPolicyIdResult(TypedDict, total=False):
    DistributionIdList: Optional[DistributionIdList]


class ListDistributionsByVpcOriginIdRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    VpcOriginId: string


class ListDistributionsByVpcOriginIdResult(TypedDict, total=False):
    DistributionIdList: Optional[DistributionIdList]


class ListDistributionsByWebACLIdRequest(ServiceRequest):
    """The request to list distributions that are associated with a specified
    WAF web ACL.
    """

    Marker: Optional[string]
    MaxItems: Optional[string]
    WebACLId: string


class ListDistributionsByWebACLIdResult(TypedDict, total=False):
    """The response to a request to list the distributions that are associated
    with a specified WAF web ACL.
    """

    DistributionList: Optional[DistributionList]


class ListDistributionsRequest(ServiceRequest):
    """The request to list your distributions."""

    Marker: Optional[string]
    MaxItems: Optional[string]


class ListDistributionsResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    DistributionList: Optional[DistributionList]


class ListDomainConflictsRequest(ServiceRequest):
    Domain: string
    DomainControlValidationResource: DistributionResourceId
    MaxItems: Optional[integer]
    Marker: Optional[string]


class ListDomainConflictsResult(TypedDict, total=False):
    DomainConflicts: Optional[DomainConflictsList]
    NextMarker: Optional[string]


class ListFieldLevelEncryptionConfigsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListFieldLevelEncryptionConfigsResult(TypedDict, total=False):
    FieldLevelEncryptionList: Optional[FieldLevelEncryptionList]


class ListFieldLevelEncryptionProfilesRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListFieldLevelEncryptionProfilesResult(TypedDict, total=False):
    FieldLevelEncryptionProfileList: Optional[FieldLevelEncryptionProfileList]


class ListFunctionsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    Stage: Optional[FunctionStage]


class ListFunctionsResult(TypedDict, total=False):
    FunctionList: Optional[FunctionList]


class ListInvalidationsForDistributionTenantRequest(ServiceRequest):
    Id: string
    Marker: Optional[string]
    MaxItems: Optional[integer]


class ListInvalidationsForDistributionTenantResult(TypedDict, total=False):
    InvalidationList: Optional[InvalidationList]


class ListInvalidationsRequest(ServiceRequest):
    """The request to list invalidations."""

    DistributionId: string
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListInvalidationsResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    InvalidationList: Optional[InvalidationList]


class ListKeyGroupsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class ListKeyGroupsResult(TypedDict, total=False):
    KeyGroupList: Optional[KeyGroupList]


class ListKeyValueStoresRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]
    Status: Optional[string]


class ListKeyValueStoresResult(TypedDict, total=False):
    KeyValueStoreList: Optional[KeyValueStoreList]


class ListOriginAccessControlsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class OriginAccessControlSummary(TypedDict, total=False):
    """A CloudFront origin access control."""

    Id: string
    Description: string
    Name: string
    SigningProtocol: OriginAccessControlSigningProtocols
    SigningBehavior: OriginAccessControlSigningBehaviors
    OriginAccessControlOriginType: OriginAccessControlOriginTypes


OriginAccessControlSummaryList = List[OriginAccessControlSummary]


class OriginAccessControlList(TypedDict, total=False):
    """A list of CloudFront origin access controls."""

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[OriginAccessControlSummaryList]


class ListOriginAccessControlsResult(TypedDict, total=False):
    OriginAccessControlList: Optional[OriginAccessControlList]


class ListOriginRequestPoliciesRequest(ServiceRequest):
    Type: Optional[OriginRequestPolicyType]
    Marker: Optional[string]
    MaxItems: Optional[string]


class OriginRequestPolicySummary(TypedDict, total=False):
    """Contains an origin request policy."""

    Type: OriginRequestPolicyType
    OriginRequestPolicy: OriginRequestPolicy


OriginRequestPolicySummaryList = List[OriginRequestPolicySummary]


class OriginRequestPolicyList(TypedDict, total=False):
    """A list of origin request policies."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[OriginRequestPolicySummaryList]


class ListOriginRequestPoliciesResult(TypedDict, total=False):
    OriginRequestPolicyList: Optional[OriginRequestPolicyList]


class ListPublicKeysRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class PublicKeySummary(TypedDict, total=False):
    """Contains information about a public key."""

    Id: string
    Name: string
    CreatedTime: timestamp
    EncodedKey: string
    Comment: Optional[string]


PublicKeySummaryList = List[PublicKeySummary]


class PublicKeyList(TypedDict, total=False):
    """A list of public keys that you can use with `signed URLs and signed
    cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__,
    or with `field-level
    encryption <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html>`__.
    """

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[PublicKeySummaryList]


class ListPublicKeysResult(TypedDict, total=False):
    PublicKeyList: Optional[PublicKeyList]


class ListRealtimeLogConfigsRequest(ServiceRequest):
    MaxItems: Optional[string]
    Marker: Optional[string]


RealtimeLogConfigList = List[RealtimeLogConfig]


class RealtimeLogConfigs(TypedDict, total=False):
    """A list of real-time log configurations."""

    MaxItems: integer
    Items: Optional[RealtimeLogConfigList]
    IsTruncated: boolean
    Marker: string
    NextMarker: Optional[string]


class ListRealtimeLogConfigsResult(TypedDict, total=False):
    RealtimeLogConfigs: Optional[RealtimeLogConfigs]


class ListResponseHeadersPoliciesRequest(ServiceRequest):
    Type: Optional[ResponseHeadersPolicyType]
    Marker: Optional[string]
    MaxItems: Optional[string]


class ResponseHeadersPolicySummary(TypedDict, total=False):
    """Contains a response headers policy."""

    Type: ResponseHeadersPolicyType
    ResponseHeadersPolicy: ResponseHeadersPolicy


ResponseHeadersPolicySummaryList = List[ResponseHeadersPolicySummary]


class ResponseHeadersPolicyList(TypedDict, total=False):
    """A list of response headers policies."""

    NextMarker: Optional[string]
    MaxItems: integer
    Quantity: integer
    Items: Optional[ResponseHeadersPolicySummaryList]


class ListResponseHeadersPoliciesResult(TypedDict, total=False):
    ResponseHeadersPolicyList: Optional[ResponseHeadersPolicyList]


class ListStreamingDistributionsRequest(ServiceRequest):
    """The request to list your streaming distributions."""

    Marker: Optional[string]
    MaxItems: Optional[string]


class StreamingDistributionSummary(TypedDict, total=False):
    """A summary of the information for a CloudFront streaming distribution."""

    Id: string
    ARN: string
    Status: string
    LastModifiedTime: timestamp
    DomainName: string
    S3Origin: S3Origin
    Aliases: Aliases
    TrustedSigners: TrustedSigners
    Comment: string
    PriceClass: PriceClass
    Enabled: boolean


StreamingDistributionSummaryList = List[StreamingDistributionSummary]


class StreamingDistributionList(TypedDict, total=False):
    """A streaming distribution list."""

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[StreamingDistributionSummaryList]


class ListStreamingDistributionsResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistributionList: Optional[StreamingDistributionList]


class ListTagsForResourceRequest(ServiceRequest):
    """The request to list tags for a CloudFront resource."""

    Resource: ResourceARN


class ListTagsForResourceResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Tags: Tags


class ListVpcOriginsRequest(ServiceRequest):
    Marker: Optional[string]
    MaxItems: Optional[string]


class VpcOriginSummary(TypedDict, total=False):
    """A summary of the CloudFront VPC origin."""

    Id: string
    Name: string
    Status: string
    CreatedTime: timestamp
    LastModifiedTime: timestamp
    Arn: string
    OriginEndpointArn: string


VpcOriginSummaryList = List[VpcOriginSummary]


class VpcOriginList(TypedDict, total=False):
    """A list of CloudFront VPC origins."""

    Marker: string
    NextMarker: Optional[string]
    MaxItems: integer
    IsTruncated: boolean
    Quantity: integer
    Items: Optional[VpcOriginSummaryList]


class ListVpcOriginsResult(TypedDict, total=False):
    VpcOriginList: Optional[VpcOriginList]


class PublishFunctionRequest(ServiceRequest):
    Name: string
    IfMatch: string


class PublishFunctionResult(TypedDict, total=False):
    FunctionSummary: Optional[FunctionSummary]


TagKeyList = List[TagKey]


class TagKeys(TypedDict, total=False):
    """A complex type that contains zero or more ``Tag`` elements."""

    Items: Optional[TagKeyList]


class TagResourceRequest(ServiceRequest):
    """The request to add tags to a CloudFront resource."""

    Resource: ResourceARN
    Tags: Tags


class TestFunctionRequest(ServiceRequest):
    Name: string
    IfMatch: string
    Stage: Optional[FunctionStage]
    EventObject: FunctionEventObject


class TestResult(TypedDict, total=False):
    """Contains the result of testing a CloudFront function with
    ``TestFunction``.
    """

    FunctionSummary: Optional[FunctionSummary]
    ComputeUtilization: Optional[string]
    FunctionExecutionLogs: Optional[FunctionExecutionLogList]
    FunctionErrorMessage: Optional[sensitiveStringType]
    FunctionOutput: Optional[sensitiveStringType]


class TestFunctionResult(TypedDict, total=False):
    TestResult: Optional[TestResult]


class UntagResourceRequest(ServiceRequest):
    """The request to remove tags from a CloudFront resource."""

    Resource: ResourceARN
    TagKeys: TagKeys


class UpdateCachePolicyRequest(ServiceRequest):
    CachePolicyConfig: CachePolicyConfig
    Id: string
    IfMatch: Optional[string]


class UpdateCachePolicyResult(TypedDict, total=False):
    CachePolicy: Optional[CachePolicy]
    ETag: Optional[string]


class UpdateCloudFrontOriginAccessIdentityRequest(ServiceRequest):
    """The request to update an origin access identity."""

    CloudFrontOriginAccessIdentityConfig: CloudFrontOriginAccessIdentityConfig
    Id: string
    IfMatch: Optional[string]


class UpdateCloudFrontOriginAccessIdentityResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    CloudFrontOriginAccessIdentity: Optional[CloudFrontOriginAccessIdentity]
    ETag: Optional[string]


class UpdateConnectionGroupRequest(ServiceRequest):
    Id: string
    Ipv6Enabled: Optional[boolean]
    IfMatch: string
    AnycastIpListId: Optional[string]
    Enabled: Optional[boolean]


class UpdateConnectionGroupResult(TypedDict, total=False):
    ConnectionGroup: Optional[ConnectionGroup]
    ETag: Optional[string]


class UpdateContinuousDeploymentPolicyRequest(ServiceRequest):
    ContinuousDeploymentPolicyConfig: ContinuousDeploymentPolicyConfig
    Id: string
    IfMatch: Optional[string]


class UpdateContinuousDeploymentPolicyResult(TypedDict, total=False):
    ContinuousDeploymentPolicy: Optional[ContinuousDeploymentPolicy]
    ETag: Optional[string]


class UpdateDistributionRequest(ServiceRequest):
    """The request to update a distribution."""

    DistributionConfig: DistributionConfig
    Id: string
    IfMatch: Optional[string]


class UpdateDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    Distribution: Optional[Distribution]
    ETag: Optional[string]


class UpdateDistributionTenantRequest(ServiceRequest):
    Id: string
    DistributionId: Optional[string]
    Domains: Optional[DomainList]
    Customizations: Optional[Customizations]
    Parameters: Optional[Parameters]
    ConnectionGroupId: Optional[string]
    IfMatch: string
    ManagedCertificateRequest: Optional[ManagedCertificateRequest]
    Enabled: Optional[boolean]


class UpdateDistributionTenantResult(TypedDict, total=False):
    DistributionTenant: Optional[DistributionTenant]
    ETag: Optional[string]


class UpdateDistributionWithStagingConfigRequest(ServiceRequest):
    Id: string
    StagingDistributionId: Optional[string]
    IfMatch: Optional[string]


class UpdateDistributionWithStagingConfigResult(TypedDict, total=False):
    Distribution: Optional[Distribution]
    ETag: Optional[string]


class UpdateDomainAssociationRequest(ServiceRequest):
    Domain: string
    TargetResource: DistributionResourceId
    IfMatch: Optional[string]


class UpdateDomainAssociationResult(TypedDict, total=False):
    Domain: Optional[string]
    ResourceId: Optional[string]
    ETag: Optional[string]


class UpdateFieldLevelEncryptionConfigRequest(ServiceRequest):
    FieldLevelEncryptionConfig: FieldLevelEncryptionConfig
    Id: string
    IfMatch: Optional[string]


class UpdateFieldLevelEncryptionConfigResult(TypedDict, total=False):
    FieldLevelEncryption: Optional[FieldLevelEncryption]
    ETag: Optional[string]


class UpdateFieldLevelEncryptionProfileRequest(ServiceRequest):
    FieldLevelEncryptionProfileConfig: FieldLevelEncryptionProfileConfig
    Id: string
    IfMatch: Optional[string]


class UpdateFieldLevelEncryptionProfileResult(TypedDict, total=False):
    FieldLevelEncryptionProfile: Optional[FieldLevelEncryptionProfile]
    ETag: Optional[string]


class UpdateFunctionRequest(ServiceRequest):
    Name: string
    IfMatch: string
    FunctionConfig: FunctionConfig
    FunctionCode: FunctionBlob


class UpdateFunctionResult(TypedDict, total=False):
    FunctionSummary: Optional[FunctionSummary]
    ETag: Optional[string]


class UpdateKeyGroupRequest(ServiceRequest):
    KeyGroupConfig: KeyGroupConfig
    Id: string
    IfMatch: Optional[string]


class UpdateKeyGroupResult(TypedDict, total=False):
    KeyGroup: Optional[KeyGroup]
    ETag: Optional[string]


class UpdateKeyValueStoreRequest(ServiceRequest):
    Name: KeyValueStoreName
    Comment: KeyValueStoreComment
    IfMatch: string


class UpdateKeyValueStoreResult(TypedDict, total=False):
    KeyValueStore: Optional[KeyValueStore]
    ETag: Optional[string]


class UpdateOriginAccessControlRequest(ServiceRequest):
    OriginAccessControlConfig: OriginAccessControlConfig
    Id: string
    IfMatch: Optional[string]


class UpdateOriginAccessControlResult(TypedDict, total=False):
    OriginAccessControl: Optional[OriginAccessControl]
    ETag: Optional[string]


class UpdateOriginRequestPolicyRequest(ServiceRequest):
    OriginRequestPolicyConfig: OriginRequestPolicyConfig
    Id: string
    IfMatch: Optional[string]


class UpdateOriginRequestPolicyResult(TypedDict, total=False):
    OriginRequestPolicy: Optional[OriginRequestPolicy]
    ETag: Optional[string]


class UpdatePublicKeyRequest(ServiceRequest):
    PublicKeyConfig: PublicKeyConfig
    Id: string
    IfMatch: Optional[string]


class UpdatePublicKeyResult(TypedDict, total=False):
    PublicKey: Optional[PublicKey]
    ETag: Optional[string]


class UpdateRealtimeLogConfigRequest(ServiceRequest):
    EndPoints: Optional[EndPointList]
    Fields: Optional[FieldList]
    Name: Optional[string]
    ARN: Optional[string]
    SamplingRate: Optional[long]


class UpdateRealtimeLogConfigResult(TypedDict, total=False):
    RealtimeLogConfig: Optional[RealtimeLogConfig]


class UpdateResponseHeadersPolicyRequest(ServiceRequest):
    ResponseHeadersPolicyConfig: ResponseHeadersPolicyConfig
    Id: string
    IfMatch: Optional[string]


class UpdateResponseHeadersPolicyResult(TypedDict, total=False):
    ResponseHeadersPolicy: Optional[ResponseHeadersPolicy]
    ETag: Optional[string]


class UpdateStreamingDistributionRequest(ServiceRequest):
    """The request to update a streaming distribution."""

    StreamingDistributionConfig: StreamingDistributionConfig
    Id: string
    IfMatch: Optional[string]


class UpdateStreamingDistributionResult(TypedDict, total=False):
    """The returned result of the corresponding request."""

    StreamingDistribution: Optional[StreamingDistribution]
    ETag: Optional[string]


class UpdateVpcOriginRequest(ServiceRequest):
    VpcOriginEndpointConfig: VpcOriginEndpointConfig
    Id: string
    IfMatch: string


class UpdateVpcOriginResult(TypedDict, total=False):
    VpcOrigin: Optional[VpcOrigin]
    ETag: Optional[string]


class VerifyDnsConfigurationRequest(ServiceRequest):
    Domain: Optional[string]
    Identifier: string


class VerifyDnsConfigurationResult(TypedDict, total=False):
    DnsConfigurationList: Optional[DnsConfigurationList]


class CloudfrontApi:
    service = "cloudfront"
    version = "2020-05-31"

    @handler("AssociateAlias")
    def associate_alias(
        self, context: RequestContext, target_distribution_id: string, alias: string, **kwargs
    ) -> None:
        """Associates an alias (also known as a CNAME or an alternate domain name)
        with a CloudFront distribution.

        With this operation you can move an alias that's already in use on a
        CloudFront distribution to a different distribution in one step. This
        prevents the downtime that could occur if you first remove the alias
        from one distribution and then separately add the alias to another
        distribution.

        To use this operation to associate an alias with a distribution, you
        provide the alias and the ID of the target distribution for the alias.
        For more information, including how to set up the target distribution,
        prerequisites that you must complete, and other restrictions, see
        `Moving an alternate domain name to a different
        distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move>`__
        in the *Amazon CloudFront Developer Guide*.

        :param target_distribution_id: The ID of the distribution that you're associating the alias with.
        :param alias: The alias (also known as a CNAME) to add to the target distribution.
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises TooManyDistributionCNAMEs:
        """
        raise NotImplementedError

    @handler("AssociateDistributionTenantWebACL")
    def associate_distribution_tenant_web_acl(
        self,
        context: RequestContext,
        id: string,
        web_acl_arn: string,
        if_match: string | None = None,
        **kwargs,
    ) -> AssociateDistributionTenantWebACLResult:
        """Associates the WAF web ACL with a distribution tenant.

        :param id: The ID of the distribution tenant.
        :param web_acl_arn: The Amazon Resource Name (ARN) of the WAF web ACL to associate.
        :param if_match: The current ``ETag`` of the distribution tenant.
        :returns: AssociateDistributionTenantWebACLResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("AssociateDistributionWebACL")
    def associate_distribution_web_acl(
        self,
        context: RequestContext,
        id: string,
        web_acl_arn: string,
        if_match: string | None = None,
        **kwargs,
    ) -> AssociateDistributionWebACLResult:
        """Associates the WAF web ACL with a distribution.

        :param id: The ID of the distribution.
        :param web_acl_arn: The Amazon Resource Name (ARN) of the WAF web ACL to associate.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        distribution that you're associating with the WAF web ACL.
        :returns: AssociateDistributionWebACLResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("CopyDistribution")
    def copy_distribution(
        self,
        context: RequestContext,
        primary_distribution_id: string,
        caller_reference: string,
        staging: boolean | None = None,
        if_match: string | None = None,
        enabled: boolean | None = None,
        **kwargs,
    ) -> CopyDistributionResult:
        """Creates a staging distribution using the configuration of the provided
        primary distribution. A staging distribution is a copy of an existing
        distribution (called the primary distribution) that you can use in a
        continuous deployment workflow.

        After you create a staging distribution, you can use
        ``UpdateDistribution`` to modify the staging distribution's
        configuration. Then you can use ``CreateContinuousDeploymentPolicy`` to
        incrementally move traffic to the staging distribution.

        This API operation requires the following IAM permissions:

        -  `GetDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html>`__

        -  `CreateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html>`__

        -  `CopyDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html>`__

        :param primary_distribution_id: The identifier of the primary distribution whose configuration you are
        copying.
        :param caller_reference: A value that uniquely identifies a request to create a resource.
        :param staging: The type of distribution that your primary distribution will be copied
        to.
        :param if_match: The version identifier of the primary distribution whose configuration
        you are copying.
        :param enabled: A Boolean flag to specify the state of the staging distribution when
        it's created.
        :returns: CopyDistributionResult
        :raises AccessDenied:
        :raises TooManyDistributionsAssociatedToOriginAccessControl:
        :raises InvalidDefaultRootObject:
        :raises InvalidQueryStringParameters:
        :raises TooManyTrustedSigners:
        :raises TooManyCookieNamesInWhiteList:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidErrorCode:
        :raises InvalidProtocolSettings:
        :raises TooManyFunctionAssociations:
        :raises TooManyOriginCustomHeaders:
        :raises InvalidOrigin:
        :raises InvalidForwardCookies:
        :raises InvalidMinimumProtocolVersion:
        :raises NoSuchCachePolicy:
        :raises TooManyKeyGroupsAssociatedToDistribution:
        :raises TooManyDistributionsAssociatedToCachePolicy:
        :raises InvalidRequiredProtocol:
        :raises TooManyDistributionsWithFunctionAssociations:
        :raises TooManyOriginGroupsPerDistribution:
        :raises TooManyDistributions:
        :raises InvalidTTLOrder:
        :raises IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior:
        :raises InvalidOriginKeepaliveTimeout:
        :raises InvalidArgument:
        :raises InvalidOriginReadTimeout:
        :raises InvalidOriginAccessControl:
        :raises InvalidHeadersForS3Origin:
        :raises TrustedSignerDoesNotExist:
        :raises InvalidWebACLId:
        :raises TooManyDistributionsWithSingleFunctionARN:
        :raises InvalidRelativePath:
        :raises TooManyLambdaFunctionAssociations:
        :raises NoSuchDistribution:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyDistributionsAssociatedToFieldLevelEncryptionConfig:
        :raises InconsistentQuantities:
        :raises InvalidLocationCode:
        :raises InvalidOriginAccessIdentity:
        :raises TooManyDistributionCNAMEs:
        :raises InvalidIfMatchVersion:
        :raises TooManyDistributionsAssociatedToOriginRequestPolicy:
        :raises TooManyQueryStringParameters:
        :raises RealtimeLogConfigOwnerMismatch:
        :raises PreconditionFailed:
        :raises MissingBody:
        :raises TooManyHeadersInForwardedValues:
        :raises InvalidLambdaFunctionAssociation:
        :raises CNAMEAlreadyExists:
        :raises TooManyCertificates:
        :raises TrustedKeyGroupDoesNotExist:
        :raises TooManyDistributionsAssociatedToResponseHeadersPolicy:
        :raises NoSuchResponseHeadersPolicy:
        :raises NoSuchRealtimeLogConfig:
        :raises InvalidResponseCode:
        :raises InvalidGeoRestrictionParameter:
        :raises TooManyOrigins:
        :raises InvalidViewerCertificate:
        :raises InvalidFunctionAssociation:
        :raises TooManyDistributionsWithLambdaAssociations:
        :raises TooManyDistributionsAssociatedToKeyGroup:
        :raises DistributionAlreadyExists:
        :raises NoSuchOrigin:
        :raises TooManyCacheBehaviors:
        """
        raise NotImplementedError

    @handler("CreateAnycastIpList")
    def create_anycast_ip_list(
        self,
        context: RequestContext,
        name: AnycastIpListName,
        ip_count: integer,
        tags: Tags | None = None,
        **kwargs,
    ) -> CreateAnycastIpListResult:
        """Creates an Anycast static IP list.

        :param name: Name of the Anycast static IP list.
        :param ip_count: The number of static IP addresses that are allocated to the Anycast
        static IP list.
        :param tags: A complex type that contains zero or more ``Tag`` elements.
        :returns: CreateAnycastIpListResult
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises EntityAlreadyExists:
        :raises InvalidTagging:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateCachePolicy")
    def create_cache_policy(
        self, context: RequestContext, cache_policy_config: CachePolicyConfig, **kwargs
    ) -> CreateCachePolicyResult:
        """Creates a cache policy.

        After you create a cache policy, you can attach it to one or more cache
        behaviors. When it's attached to a cache behavior, the cache policy
        determines the following:

        -  The values that CloudFront includes in the *cache key*. These values
           can include HTTP headers, cookies, and URL query strings. CloudFront
           uses the cache key to find an object in its cache that it can return
           to the viewer.

        -  The default, minimum, and maximum time to live (TTL) values that you
           want objects to stay in the CloudFront cache.

        The headers, cookies, and query strings that are included in the cache
        key are also included in requests that CloudFront sends to the origin.
        CloudFront sends a request when it can't find an object in its cache
        that matches the request's cache key. If you want to send values to the
        origin but *not* include them in the cache key, use
        ``OriginRequestPolicy``.

        For more information about cache policies, see `Controlling the cache
        key <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param cache_policy_config: A cache policy configuration.
        :returns: CreateCachePolicyResult
        :raises AccessDenied:
        :raises TooManyHeadersInCachePolicy:
        :raises CachePolicyAlreadyExists:
        :raises TooManyCookiesInCachePolicy:
        :raises InconsistentQuantities:
        :raises TooManyCachePolicies:
        :raises InvalidArgument:
        :raises TooManyQueryStringsInCachePolicy:
        """
        raise NotImplementedError

    @handler("CreateCloudFrontOriginAccessIdentity")
    def create_cloud_front_origin_access_identity(
        self,
        context: RequestContext,
        cloud_front_origin_access_identity_config: CloudFrontOriginAccessIdentityConfig,
        **kwargs,
    ) -> CreateCloudFrontOriginAccessIdentityResult:
        """Creates a new origin access identity. If you're using Amazon S3 for your
        origin, you can use an origin access identity to require users to access
        your content using a CloudFront URL instead of the Amazon S3 URL. For
        more information about how to use origin access identities, see `Serving
        Private Content through
        CloudFront <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param cloud_front_origin_access_identity_config: The current configuration information for the identity.
        :returns: CreateCloudFrontOriginAccessIdentityResult
        :raises MissingBody:
        :raises TooManyCloudFrontOriginAccessIdentities:
        :raises InconsistentQuantities:
        :raises CloudFrontOriginAccessIdentityAlreadyExists:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateConnectionGroup")
    def create_connection_group(
        self,
        context: RequestContext,
        name: string,
        ipv6_enabled: boolean | None = None,
        tags: Tags | None = None,
        anycast_ip_list_id: string | None = None,
        enabled: boolean | None = None,
        **kwargs,
    ) -> CreateConnectionGroupResult:
        """Creates a connection group.

        :param name: The name of the connection group.
        :param ipv6_enabled: Enable IPv6 for the connection group.
        :param tags: A complex type that contains zero or more ``Tag`` elements.
        :param anycast_ip_list_id: The ID of the Anycast static IP list.
        :param enabled: Enable the connection group.
        :returns: CreateConnectionGroupResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises EntityAlreadyExists:
        :raises InvalidTagging:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateContinuousDeploymentPolicy")
    def create_continuous_deployment_policy(
        self,
        context: RequestContext,
        continuous_deployment_policy_config: ContinuousDeploymentPolicyConfig,
        **kwargs,
    ) -> CreateContinuousDeploymentPolicyResult:
        """Creates a continuous deployment policy that distributes traffic for a
        custom domain name to two different CloudFront distributions.

        To use a continuous deployment policy, first use ``CopyDistribution`` to
        create a staging distribution, then use ``UpdateDistribution`` to modify
        the staging distribution's configuration.

        After you create and update a staging distribution, you can use a
        continuous deployment policy to incrementally move traffic to the
        staging distribution. This workflow enables you to test changes to a
        distribution's configuration before moving all of your domain's
        production traffic to the new configuration.

        :param continuous_deployment_policy_config: Contains the configuration for a continuous deployment policy.
        :returns: CreateContinuousDeploymentPolicyResult
        :raises AccessDenied:
        :raises TooManyContinuousDeploymentPolicies:
        :raises StagingDistributionInUse:
        :raises InconsistentQuantities:
        :raises ContinuousDeploymentPolicyAlreadyExists:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateDistribution")
    def create_distribution(
        self, context: RequestContext, distribution_config: DistributionConfig, **kwargs
    ) -> CreateDistributionResult:
        """Creates a CloudFront distribution.

        :param distribution_config: The distribution's configuration information.
        :returns: CreateDistributionResult
        :raises AccessDenied:
        :raises TooManyDistributionsAssociatedToOriginAccessControl:
        :raises InvalidDefaultRootObject:
        :raises InvalidDomainNameForOriginAccessControl:
        :raises InvalidQueryStringParameters:
        :raises TooManyTrustedSigners:
        :raises TooManyCookieNamesInWhiteList:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidErrorCode:
        :raises IllegalOriginAccessConfiguration:
        :raises InvalidProtocolSettings:
        :raises TooManyFunctionAssociations:
        :raises TooManyOriginCustomHeaders:
        :raises InvalidOrigin:
        :raises InvalidForwardCookies:
        :raises InvalidMinimumProtocolVersion:
        :raises NoSuchCachePolicy:
        :raises TooManyKeyGroupsAssociatedToDistribution:
        :raises TooManyDistributionsAssociatedToCachePolicy:
        :raises InvalidRequiredProtocol:
        :raises TooManyDistributionsWithFunctionAssociations:
        :raises TooManyOriginGroupsPerDistribution:
        :raises TooManyDistributions:
        :raises InvalidTTLOrder:
        :raises IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior:
        :raises InvalidOriginKeepaliveTimeout:
        :raises InvalidArgument:
        :raises InvalidOriginReadTimeout:
        :raises InvalidOriginAccessControl:
        :raises EntityNotFound:
        :raises InvalidHeadersForS3Origin:
        :raises TrustedSignerDoesNotExist:
        :raises InvalidWebACLId:
        :raises TooManyDistributionsWithSingleFunctionARN:
        :raises InvalidRelativePath:
        :raises TooManyLambdaFunctionAssociations:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyDistributionsAssociatedToFieldLevelEncryptionConfig:
        :raises InconsistentQuantities:
        :raises InvalidLocationCode:
        :raises InvalidOriginAccessIdentity:
        :raises TooManyDistributionCNAMEs:
        :raises NoSuchContinuousDeploymentPolicy:
        :raises TooManyDistributionsAssociatedToOriginRequestPolicy:
        :raises TooManyQueryStringParameters:
        :raises RealtimeLogConfigOwnerMismatch:
        :raises ContinuousDeploymentPolicyInUse:
        :raises MissingBody:
        :raises TooManyHeadersInForwardedValues:
        :raises InvalidLambdaFunctionAssociation:
        :raises CNAMEAlreadyExists:
        :raises TooManyCertificates:
        :raises TrustedKeyGroupDoesNotExist:
        :raises TooManyDistributionsAssociatedToResponseHeadersPolicy:
        :raises NoSuchResponseHeadersPolicy:
        :raises NoSuchRealtimeLogConfig:
        :raises InvalidResponseCode:
        :raises InvalidGeoRestrictionParameter:
        :raises TooManyOrigins:
        :raises InvalidViewerCertificate:
        :raises InvalidFunctionAssociation:
        :raises TooManyDistributionsWithLambdaAssociations:
        :raises TooManyDistributionsAssociatedToKeyGroup:
        :raises EntityLimitExceeded:
        :raises DistributionAlreadyExists:
        :raises NoSuchOrigin:
        :raises TooManyCacheBehaviors:
        """
        raise NotImplementedError

    @handler("CreateDistributionTenant")
    def create_distribution_tenant(
        self,
        context: RequestContext,
        distribution_id: string,
        name: CreateDistributionTenantRequestNameString,
        domains: DomainList,
        tags: Tags | None = None,
        customizations: Customizations | None = None,
        parameters: Parameters | None = None,
        connection_group_id: string | None = None,
        managed_certificate_request: ManagedCertificateRequest | None = None,
        enabled: boolean | None = None,
        **kwargs,
    ) -> CreateDistributionTenantResult:
        """Creates a distribution tenant.

        :param distribution_id: The ID of the multi-tenant distribution to use for creating the
        distribution tenant.
        :param name: The name of the distribution tenant.
        :param domains: The domains associated with the distribution tenant.
        :param tags: A complex type that contains zero or more ``Tag`` elements.
        :param customizations: Customizations for the distribution tenant.
        :param parameters: A list of parameter values to add to the resource.
        :param connection_group_id: The ID of the connection group to associate with the distribution
        tenant.
        :param managed_certificate_request: The configuration for the CloudFront managed ACM certificate request.
        :param enabled: Indicates whether the distribution tenant should be enabled when
        created.
        :returns: CreateDistributionTenantResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises EntityAlreadyExists:
        :raises CNAMEAlreadyExists:
        :raises InvalidTagging:
        :raises InvalidAssociation:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateDistributionWithTags")
    def create_distribution_with_tags(
        self,
        context: RequestContext,
        distribution_config_with_tags: DistributionConfigWithTags,
        **kwargs,
    ) -> CreateDistributionWithTagsResult:
        """Create a new distribution with tags. This API operation requires the
        following IAM permissions:

        -  `CreateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html>`__

        -  `TagResource <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html>`__

        :param distribution_config_with_tags: The distribution's configuration information.
        :returns: CreateDistributionWithTagsResult
        :raises AccessDenied:
        :raises TooManyDistributionsAssociatedToOriginAccessControl:
        :raises InvalidDefaultRootObject:
        :raises InvalidDomainNameForOriginAccessControl:
        :raises InvalidQueryStringParameters:
        :raises TooManyTrustedSigners:
        :raises TooManyCookieNamesInWhiteList:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidErrorCode:
        :raises IllegalOriginAccessConfiguration:
        :raises InvalidProtocolSettings:
        :raises TooManyFunctionAssociations:
        :raises TooManyOriginCustomHeaders:
        :raises InvalidOrigin:
        :raises InvalidForwardCookies:
        :raises InvalidMinimumProtocolVersion:
        :raises NoSuchCachePolicy:
        :raises TooManyKeyGroupsAssociatedToDistribution:
        :raises TooManyDistributionsAssociatedToCachePolicy:
        :raises InvalidRequiredProtocol:
        :raises TooManyDistributionsWithFunctionAssociations:
        :raises TooManyOriginGroupsPerDistribution:
        :raises TooManyDistributions:
        :raises InvalidTTLOrder:
        :raises IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior:
        :raises InvalidOriginKeepaliveTimeout:
        :raises InvalidArgument:
        :raises InvalidOriginReadTimeout:
        :raises InvalidOriginAccessControl:
        :raises EntityNotFound:
        :raises InvalidHeadersForS3Origin:
        :raises TrustedSignerDoesNotExist:
        :raises InvalidWebACLId:
        :raises TooManyDistributionsWithSingleFunctionARN:
        :raises InvalidRelativePath:
        :raises TooManyLambdaFunctionAssociations:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyDistributionsAssociatedToFieldLevelEncryptionConfig:
        :raises InconsistentQuantities:
        :raises InvalidLocationCode:
        :raises InvalidOriginAccessIdentity:
        :raises InvalidTagging:
        :raises TooManyDistributionCNAMEs:
        :raises NoSuchContinuousDeploymentPolicy:
        :raises TooManyDistributionsAssociatedToOriginRequestPolicy:
        :raises TooManyQueryStringParameters:
        :raises RealtimeLogConfigOwnerMismatch:
        :raises ContinuousDeploymentPolicyInUse:
        :raises MissingBody:
        :raises TooManyHeadersInForwardedValues:
        :raises InvalidLambdaFunctionAssociation:
        :raises CNAMEAlreadyExists:
        :raises TooManyCertificates:
        :raises TrustedKeyGroupDoesNotExist:
        :raises TooManyDistributionsAssociatedToResponseHeadersPolicy:
        :raises NoSuchResponseHeadersPolicy:
        :raises NoSuchRealtimeLogConfig:
        :raises InvalidResponseCode:
        :raises InvalidGeoRestrictionParameter:
        :raises TooManyOrigins:
        :raises InvalidViewerCertificate:
        :raises InvalidFunctionAssociation:
        :raises TooManyDistributionsWithLambdaAssociations:
        :raises TooManyDistributionsAssociatedToKeyGroup:
        :raises DistributionAlreadyExists:
        :raises NoSuchOrigin:
        :raises TooManyCacheBehaviors:
        """
        raise NotImplementedError

    @handler("CreateFieldLevelEncryptionConfig")
    def create_field_level_encryption_config(
        self,
        context: RequestContext,
        field_level_encryption_config: FieldLevelEncryptionConfig,
        **kwargs,
    ) -> CreateFieldLevelEncryptionConfigResult:
        """Create a new field-level encryption configuration.

        :param field_level_encryption_config: The request to create a new field-level encryption configuration.
        :returns: CreateFieldLevelEncryptionConfigResult
        :raises QueryArgProfileEmpty:
        :raises TooManyFieldLevelEncryptionContentTypeProfiles:
        :raises TooManyFieldLevelEncryptionQueryArgProfiles:
        :raises FieldLevelEncryptionConfigAlreadyExists:
        :raises InconsistentQuantities:
        :raises TooManyFieldLevelEncryptionConfigs:
        :raises NoSuchFieldLevelEncryptionProfile:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateFieldLevelEncryptionProfile")
    def create_field_level_encryption_profile(
        self,
        context: RequestContext,
        field_level_encryption_profile_config: FieldLevelEncryptionProfileConfig,
        **kwargs,
    ) -> CreateFieldLevelEncryptionProfileResult:
        """Create a field-level encryption profile.

        :param field_level_encryption_profile_config: The request to create a field-level encryption profile.
        :returns: CreateFieldLevelEncryptionProfileResult
        :raises TooManyFieldLevelEncryptionFieldPatterns:
        :raises FieldLevelEncryptionProfileAlreadyExists:
        :raises NoSuchPublicKey:
        :raises FieldLevelEncryptionProfileSizeExceeded:
        :raises InconsistentQuantities:
        :raises TooManyFieldLevelEncryptionProfiles:
        :raises TooManyFieldLevelEncryptionEncryptionEntities:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateFunction")
    def create_function(
        self,
        context: RequestContext,
        name: FunctionName,
        function_config: FunctionConfig,
        function_code: FunctionBlob,
        **kwargs,
    ) -> CreateFunctionResult:
        """Creates a CloudFront function.

        To create a function, you provide the function code and some
        configuration information about the function. The response contains an
        Amazon Resource Name (ARN) that uniquely identifies the function.

        When you create a function, it's in the ``DEVELOPMENT`` stage. In this
        stage, you can test the function with ``TestFunction``, and update it
        with ``UpdateFunction``.

        When you're ready to use your function with a CloudFront distribution,
        use ``PublishFunction`` to copy the function from the ``DEVELOPMENT``
        stage to ``LIVE``. When it's live, you can attach the function to a
        distribution's cache behavior, using the function's ARN.

        :param name: A name to identify the function.
        :param function_config: Configuration information about the function, including an optional
        comment and the function's runtime.
        :param function_code: The function code.
        :returns: CreateFunctionResult
        :raises FunctionAlreadyExists:
        :raises UnsupportedOperation:
        :raises FunctionSizeLimitExceeded:
        :raises InvalidArgument:
        :raises TooManyFunctions:
        """
        raise NotImplementedError

    @handler("CreateInvalidation")
    def create_invalidation(
        self,
        context: RequestContext,
        distribution_id: string,
        invalidation_batch: InvalidationBatch,
        **kwargs,
    ) -> CreateInvalidationResult:
        """Create a new invalidation. For more information, see `Invalidating
        files <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param distribution_id: The distribution's id.
        :param invalidation_batch: The batch information for the invalidation.
        :returns: CreateInvalidationResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises TooManyInvalidationsInProgress:
        :raises MissingBody:
        :raises InconsistentQuantities:
        :raises BatchTooLarge:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateInvalidationForDistributionTenant")
    def create_invalidation_for_distribution_tenant(
        self, context: RequestContext, id: string, invalidation_batch: InvalidationBatch, **kwargs
    ) -> CreateInvalidationForDistributionTenantResult:
        """Creates an invalidation for a distribution tenant. For more information,
        see `Invalidating
        files <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param id: The ID of the distribution tenant.
        :param invalidation_batch: An invalidation batch.
        :returns: CreateInvalidationForDistributionTenantResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises TooManyInvalidationsInProgress:
        :raises MissingBody:
        :raises InconsistentQuantities:
        :raises BatchTooLarge:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateKeyGroup")
    def create_key_group(
        self, context: RequestContext, key_group_config: KeyGroupConfig, **kwargs
    ) -> CreateKeyGroupResult:
        """Creates a key group that you can use with `CloudFront signed URLs and
        signed
        cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__.

        To create a key group, you must specify at least one public key for the
        key group. After you create a key group, you can reference it from one
        or more cache behaviors. When you reference a key group in a cache
        behavior, CloudFront requires signed URLs or signed cookies for all
        requests that match the cache behavior. The URLs or cookies must be
        signed with a private key whose corresponding public key is in the key
        group. The signed URL or cookie contains information about which public
        key CloudFront should use to verify the signature. For more information,
        see `Serving private
        content <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param key_group_config: A key group configuration.
        :returns: CreateKeyGroupResult
        :raises TooManyPublicKeysInKeyGroup:
        :raises TooManyKeyGroups:
        :raises InvalidArgument:
        :raises KeyGroupAlreadyExists:
        """
        raise NotImplementedError

    @handler("CreateKeyValueStore")
    def create_key_value_store(
        self,
        context: RequestContext,
        name: KeyValueStoreName,
        comment: KeyValueStoreComment | None = None,
        import_source: ImportSource | None = None,
        **kwargs,
    ) -> CreateKeyValueStoreResult:
        """Specifies the key value store resource to add to your account. In your
        account, the key value store names must be unique. You can also import
        key value store data in JSON format from an S3 bucket by providing a
        valid ``ImportSource`` that you own.

        :param name: The name of the key value store.
        :param comment: The comment of the key value store.
        :param import_source: The S3 bucket that provides the source for the import.
        :returns: CreateKeyValueStoreResult
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises EntityAlreadyExists:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        :raises EntitySizeLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateMonitoringSubscription")
    def create_monitoring_subscription(
        self,
        context: RequestContext,
        distribution_id: string,
        monitoring_subscription: MonitoringSubscription,
        **kwargs,
    ) -> CreateMonitoringSubscriptionResult:
        """Enables or disables additional Amazon CloudWatch metrics for the
        specified CloudFront distribution. The additional metrics incur an
        additional cost.

        For more information, see `Viewing additional CloudFront distribution
        metrics <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional>`__
        in the *Amazon CloudFront Developer Guide*.

        :param distribution_id: The ID of the distribution that you are enabling metrics for.
        :param monitoring_subscription: A monitoring subscription.
        :returns: CreateMonitoringSubscriptionResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises MonitoringSubscriptionAlreadyExists:
        :raises UnsupportedOperation:
        """
        raise NotImplementedError

    @handler("CreateOriginAccessControl")
    def create_origin_access_control(
        self,
        context: RequestContext,
        origin_access_control_config: OriginAccessControlConfig,
        **kwargs,
    ) -> CreateOriginAccessControlResult:
        """Creates a new origin access control in CloudFront. After you create an
        origin access control, you can add it to an origin in a CloudFront
        distribution so that CloudFront sends authenticated (signed) requests to
        the origin.

        This makes it possible to block public access to the origin, allowing
        viewers (users) to access the origin's content only through CloudFront.

        For more information about using a CloudFront origin access control, see
        `Restricting access to an Amazon Web Services
        origin <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param origin_access_control_config: Contains the origin access control.
        :returns: CreateOriginAccessControlResult
        :raises OriginAccessControlAlreadyExists:
        :raises TooManyOriginAccessControls:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateOriginRequestPolicy")
    def create_origin_request_policy(
        self,
        context: RequestContext,
        origin_request_policy_config: OriginRequestPolicyConfig,
        **kwargs,
    ) -> CreateOriginRequestPolicyResult:
        """Creates an origin request policy.

        After you create an origin request policy, you can attach it to one or
        more cache behaviors. When it's attached to a cache behavior, the origin
        request policy determines the values that CloudFront includes in
        requests that it sends to the origin. Each request that CloudFront sends
        to the origin includes the following:

        -  The request body and the URL path (without the domain name) from the
           viewer request.

        -  The headers that CloudFront automatically includes in every origin
           request, including ``Host``, ``User-Agent``, and ``X-Amz-Cf-Id``.

        -  All HTTP headers, cookies, and URL query strings that are specified
           in the cache policy or the origin request policy. These can include
           items from the viewer request and, in the case of headers, additional
           ones that are added by CloudFront.

        CloudFront sends a request when it can't find a valid object in its
        cache that matches the request. If you want to send values to the origin
        and also include them in the cache key, use ``CachePolicy``.

        For more information about origin request policies, see `Controlling
        origin
        requests <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param origin_request_policy_config: An origin request policy configuration.
        :returns: CreateOriginRequestPolicyResult
        :raises AccessDenied:
        :raises TooManyHeadersInOriginRequestPolicy:
        :raises TooManyCookiesInOriginRequestPolicy:
        :raises InconsistentQuantities:
        :raises OriginRequestPolicyAlreadyExists:
        :raises TooManyQueryStringsInOriginRequestPolicy:
        :raises InvalidArgument:
        :raises TooManyOriginRequestPolicies:
        """
        raise NotImplementedError

    @handler("CreatePublicKey")
    def create_public_key(
        self, context: RequestContext, public_key_config: PublicKeyConfig, **kwargs
    ) -> CreatePublicKeyResult:
        """Uploads a public key to CloudFront that you can use with `signed URLs
        and signed
        cookies <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__,
        or with `field-level
        encryption <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html>`__.

        :param public_key_config: A CloudFront public key configuration.
        :returns: CreatePublicKeyResult
        :raises TooManyPublicKeys:
        :raises PublicKeyAlreadyExists:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateRealtimeLogConfig")
    def create_realtime_log_config(
        self,
        context: RequestContext,
        end_points: EndPointList,
        fields: FieldList,
        name: string,
        sampling_rate: long,
        **kwargs,
    ) -> CreateRealtimeLogConfigResult:
        """Creates a real-time log configuration.

        After you create a real-time log configuration, you can attach it to one
        or more cache behaviors to send real-time log data to the specified
        Amazon Kinesis data stream.

        For more information about real-time log configurations, see `Real-time
        logs <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param end_points: Contains information about the Amazon Kinesis data stream where you are
        sending real-time log data.
        :param fields: A list of fields to include in each real-time log record.
        :param name: A unique name to identify this real-time log configuration.
        :param sampling_rate: The sampling rate for this real-time log configuration.
        :returns: CreateRealtimeLogConfigResult
        :raises AccessDenied:
        :raises RealtimeLogConfigAlreadyExists:
        :raises TooManyRealtimeLogConfigs:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("CreateResponseHeadersPolicy")
    def create_response_headers_policy(
        self,
        context: RequestContext,
        response_headers_policy_config: ResponseHeadersPolicyConfig,
        **kwargs,
    ) -> CreateResponseHeadersPolicyResult:
        """Creates a response headers policy.

        A response headers policy contains information about a set of HTTP
        headers. To create a response headers policy, you provide some metadata
        about the policy and a set of configurations that specify the headers.

        After you create a response headers policy, you can use its ID to attach
        it to one or more cache behaviors in a CloudFront distribution. When
        it's attached to a cache behavior, the response headers policy affects
        the HTTP headers that CloudFront includes in HTTP responses to requests
        that match the cache behavior. CloudFront adds or removes response
        headers according to the configuration of the response headers policy.

        For more information, see `Adding or removing HTTP headers in CloudFront
        responses <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param response_headers_policy_config: Contains metadata about the response headers policy, and a set of
        configurations that specify the HTTP headers.
        :returns: CreateResponseHeadersPolicyResult
        :raises AccessDenied:
        :raises TooManyCustomHeadersInResponseHeadersPolicy:
        :raises ResponseHeadersPolicyAlreadyExists:
        :raises InconsistentQuantities:
        :raises TooLongCSPInResponseHeadersPolicy:
        :raises InvalidArgument:
        :raises TooManyRemoveHeadersInResponseHeadersPolicy:
        :raises TooManyResponseHeadersPolicies:
        """
        raise NotImplementedError

    @handler("CreateStreamingDistribution")
    def create_streaming_distribution(
        self,
        context: RequestContext,
        streaming_distribution_config: StreamingDistributionConfig,
        **kwargs,
    ) -> CreateStreamingDistributionResult:
        """This API is deprecated. Amazon CloudFront is deprecating real-time
        messaging protocol (RTMP) distributions on December 31, 2020. For more
        information, `read the
        announcement <http://forums.aws.amazon.com/ann.jspa?annID=7356>`__ on
        the Amazon CloudFront discussion forum.

        :param streaming_distribution_config: The streaming distribution's configuration information.
        :returns: CreateStreamingDistributionResult
        :raises AccessDenied:
        :raises StreamingDistributionAlreadyExists:
        :raises InconsistentQuantities:
        :raises InvalidOriginAccessIdentity:
        :raises InvalidArgument:
        :raises TooManyTrustedSigners:
        :raises InvalidOriginAccessControl:
        :raises TooManyStreamingDistributions:
        :raises MissingBody:
        :raises TooManyStreamingDistributionCNAMEs:
        :raises TrustedSignerDoesNotExist:
        :raises CNAMEAlreadyExists:
        :raises InvalidOrigin:
        """
        raise NotImplementedError

    @handler("CreateStreamingDistributionWithTags")
    def create_streaming_distribution_with_tags(
        self,
        context: RequestContext,
        streaming_distribution_config_with_tags: StreamingDistributionConfigWithTags,
        **kwargs,
    ) -> CreateStreamingDistributionWithTagsResult:
        """This API is deprecated. Amazon CloudFront is deprecating real-time
        messaging protocol (RTMP) distributions on December 31, 2020. For more
        information, `read the
        announcement <http://forums.aws.amazon.com/ann.jspa?annID=7356>`__ on
        the Amazon CloudFront discussion forum.

        :param streaming_distribution_config_with_tags: The streaming distribution's configuration information.
        :returns: CreateStreamingDistributionWithTagsResult
        :raises AccessDenied:
        :raises StreamingDistributionAlreadyExists:
        :raises InconsistentQuantities:
        :raises InvalidOriginAccessIdentity:
        :raises InvalidTagging:
        :raises InvalidArgument:
        :raises TooManyTrustedSigners:
        :raises InvalidOriginAccessControl:
        :raises TooManyStreamingDistributions:
        :raises MissingBody:
        :raises TooManyStreamingDistributionCNAMEs:
        :raises TrustedSignerDoesNotExist:
        :raises CNAMEAlreadyExists:
        :raises InvalidOrigin:
        """
        raise NotImplementedError

    @handler("CreateVpcOrigin")
    def create_vpc_origin(
        self,
        context: RequestContext,
        vpc_origin_endpoint_config: VpcOriginEndpointConfig,
        tags: Tags | None = None,
        **kwargs,
    ) -> CreateVpcOriginResult:
        """Create an Amazon CloudFront VPC origin.

        :param vpc_origin_endpoint_config: The VPC origin endpoint configuration.
        :param tags: A complex type that contains zero or more ``Tag`` elements.
        :returns: CreateVpcOriginResult
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises EntityAlreadyExists:
        :raises InconsistentQuantities:
        :raises InvalidTagging:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("DeleteAnycastIpList")
    def delete_anycast_ip_list(
        self, context: RequestContext, id: string, if_match: string, **kwargs
    ) -> None:
        """Deletes an Anycast static IP list.

        :param id: The ID of the Anycast static IP list.
        :param if_match: The current version (``ETag`` value) of the Anycast static IP list that
        you are deleting.
        :raises CannotDeleteEntityWhileInUse:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises IllegalDelete:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteCachePolicy")
    def delete_cache_policy(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes a cache policy.

        You cannot delete a cache policy if it's attached to a cache behavior.
        First update your distributions to remove the cache policy from all
        cache behaviors, then delete the cache policy.

        To delete a cache policy, you must provide the policy's identifier and
        version. To get these values, you can use ``ListCachePolicies`` or
        ``GetCachePolicy``.

        :param id: The unique identifier for the cache policy that you are deleting.
        :param if_match: The version of the cache policy that you are deleting.
        :raises NoSuchCachePolicy:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises IllegalDelete:
        :raises CachePolicyInUse:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteCloudFrontOriginAccessIdentity")
    def delete_cloud_front_origin_access_identity(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Delete an origin access identity.

        :param id: The origin access identity's ID.
        :param if_match: The value of the ``ETag`` header you received from a previous ``GET`` or
        ``PUT`` request.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises CloudFrontOriginAccessIdentityInUse:
        :raises InvalidIfMatchVersion:
        :raises NoSuchCloudFrontOriginAccessIdentity:
        """
        raise NotImplementedError

    @handler("DeleteConnectionGroup")
    def delete_connection_group(
        self, context: RequestContext, id: string, if_match: string, **kwargs
    ) -> None:
        """Deletes a connection group.

        :param id: The ID of the connection group to delete.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        connection group to delete.
        :raises CannotDeleteEntityWhileInUse:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises ResourceNotDisabled:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteContinuousDeploymentPolicy")
    def delete_continuous_deployment_policy(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes a continuous deployment policy.

        You cannot delete a continuous deployment policy that's attached to a
        primary distribution. First update your distribution to remove the
        continuous deployment policy, then you can delete the policy.

        :param id: The identifier of the continuous deployment policy that you are
        deleting.
        :param if_match: The current version (``ETag`` value) of the continuous deployment policy
        that you are deleting.
        :raises ContinuousDeploymentPolicyInUse:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchContinuousDeploymentPolicy:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteDistribution")
    def delete_distribution(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Delete a distribution.

        :param id: The distribution ID.
        :param if_match: The value of the ``ETag`` header that you received when you disabled the
        distribution.
        :raises ResourceInUse:
        :raises NoSuchDistribution:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises DistributionNotDisabled:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteDistributionTenant")
    def delete_distribution_tenant(
        self, context: RequestContext, id: string, if_match: string, **kwargs
    ) -> None:
        """Deletes a distribution tenant. If you use this API operation to delete a
        distribution tenant that is currently enabled, the request will fail.

        To delete a distribution tenant, you must first disable the distribution
        tenant by using the ``UpdateDistributionTenant`` API operation.

        :param id: The ID of the distribution tenant to delete.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        distribution tenant.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises ResourceNotDisabled:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteFieldLevelEncryptionConfig")
    def delete_field_level_encryption_config(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Remove a field-level encryption configuration.

        :param id: The ID of the configuration you want to delete from CloudFront.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        configuration identity to delete.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises FieldLevelEncryptionConfigInUse:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteFieldLevelEncryptionProfile")
    def delete_field_level_encryption_profile(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Remove a field-level encryption profile.

        :param id: Request the ID of the profile you want to delete from CloudFront.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        profile to delete.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionProfile:
        :raises FieldLevelEncryptionProfileInUse:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteFunction")
    def delete_function(
        self, context: RequestContext, name: string, if_match: string, **kwargs
    ) -> None:
        """Deletes a CloudFront function.

        You cannot delete a function if it's associated with a cache behavior.
        First, update your distributions to remove the function association from
        all cache behaviors, then delete the function.

        To delete a function, you must provide the function's name and version
        (``ETag`` value). To get these values, you can use ``ListFunctions`` and
        ``DescribeFunction``.

        :param name: The name of the function that you are deleting.
        :param if_match: The current version (``ETag`` value) of the function that you are
        deleting, which you can get using ``DescribeFunction``.
        :raises PreconditionFailed:
        :raises UnsupportedOperation:
        :raises FunctionInUse:
        :raises NoSuchFunctionExists:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteKeyGroup")
    def delete_key_group(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes a key group.

        You cannot delete a key group that is referenced in a cache behavior.
        First update your distributions to remove the key group from all cache
        behaviors, then delete the key group.

        To delete a key group, you must provide the key group's identifier and
        version. To get these values, use ``ListKeyGroups`` followed by
        ``GetKeyGroup`` or ``GetKeyGroupConfig``.

        :param id: The identifier of the key group that you are deleting.
        :param if_match: The version of the key group that you are deleting.
        :raises PreconditionFailed:
        :raises ResourceInUse:
        :raises NoSuchResource:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteKeyValueStore")
    def delete_key_value_store(
        self, context: RequestContext, name: KeyValueStoreName, if_match: string, **kwargs
    ) -> None:
        """Specifies the key value store to delete.

        :param name: The name of the key value store.
        :param if_match: The key value store to delete, if a match occurs.
        :raises CannotDeleteEntityWhileInUse:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteMonitoringSubscription")
    def delete_monitoring_subscription(
        self, context: RequestContext, distribution_id: string, **kwargs
    ) -> DeleteMonitoringSubscriptionResult:
        """Disables additional CloudWatch metrics for the specified CloudFront
        distribution.

        :param distribution_id: The ID of the distribution that you are disabling metrics for.
        :returns: DeleteMonitoringSubscriptionResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises NoSuchMonitoringSubscription:
        """
        raise NotImplementedError

    @handler("DeleteOriginAccessControl")
    def delete_origin_access_control(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes a CloudFront origin access control.

        You cannot delete an origin access control if it's in use. First, update
        all distributions to remove the origin access control from all origins,
        then delete the origin access control.

        :param id: The unique identifier of the origin access control that you are
        deleting.
        :param if_match: The current version (``ETag`` value) of the origin access control that
        you are deleting.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises OriginAccessControlInUse:
        :raises NoSuchOriginAccessControl:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteOriginRequestPolicy")
    def delete_origin_request_policy(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes an origin request policy.

        You cannot delete an origin request policy if it's attached to any cache
        behaviors. First update your distributions to remove the origin request
        policy from all cache behaviors, then delete the origin request policy.

        To delete an origin request policy, you must provide the policy's
        identifier and version. To get the identifier, you can use
        ``ListOriginRequestPolicies`` or ``GetOriginRequestPolicy``.

        :param id: The unique identifier for the origin request policy that you are
        deleting.
        :param if_match: The version of the origin request policy that you are deleting.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises IllegalDelete:
        :raises NoSuchOriginRequestPolicy:
        :raises InvalidIfMatchVersion:
        :raises OriginRequestPolicyInUse:
        """
        raise NotImplementedError

    @handler("DeletePublicKey")
    def delete_public_key(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Remove a public key you previously added to CloudFront.

        :param id: The ID of the public key you want to remove from CloudFront.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        public key identity to delete.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises NoSuchPublicKey:
        :raises PublicKeyInUse:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteRealtimeLogConfig")
    def delete_realtime_log_config(
        self,
        context: RequestContext,
        name: string | None = None,
        arn: string | None = None,
        **kwargs,
    ) -> None:
        """Deletes a real-time log configuration.

        You cannot delete a real-time log configuration if it's attached to a
        cache behavior. First update your distributions to remove the real-time
        log configuration from all cache behaviors, then delete the real-time
        log configuration.

        To delete a real-time log configuration, you can provide the
        configuration's name or its Amazon Resource Name (ARN). You must provide
        at least one. If you provide both, CloudFront uses the name to identify
        the real-time log configuration to delete.

        :param name: The name of the real-time log configuration to delete.
        :param arn: The Amazon Resource Name (ARN) of the real-time log configuration to
        delete.
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchRealtimeLogConfig:
        :raises RealtimeLogConfigInUse:
        """
        raise NotImplementedError

    @handler("DeleteResponseHeadersPolicy")
    def delete_response_headers_policy(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Deletes a response headers policy.

        You cannot delete a response headers policy if it's attached to a cache
        behavior. First update your distributions to remove the response headers
        policy from all cache behaviors, then delete the response headers
        policy.

        To delete a response headers policy, you must provide the policy's
        identifier and version. To get these values, you can use
        ``ListResponseHeadersPolicies`` or ``GetResponseHeadersPolicy``.

        :param id: The identifier for the response headers policy that you are deleting.
        :param if_match: The version of the response headers policy that you are deleting.
        :raises PreconditionFailed:
        :raises ResponseHeadersPolicyInUse:
        :raises AccessDenied:
        :raises IllegalDelete:
        :raises NoSuchResponseHeadersPolicy:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteStreamingDistribution")
    def delete_streaming_distribution(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> None:
        """Delete a streaming distribution. To delete an RTMP distribution using
        the CloudFront API, perform the following steps.

        **To delete an RTMP distribution using the CloudFront API**:

        #. Disable the RTMP distribution.

        #. Submit a ``GET Streaming Distribution Config`` request to get the
           current configuration and the ``Etag`` header for the distribution.

        #. Update the XML document that was returned in the response to your
           ``GET Streaming Distribution Config`` request to change the value of
           ``Enabled`` to ``false``.

        #. Submit a ``PUT Streaming Distribution Config`` request to update the
           configuration for your distribution. In the request body, include the
           XML document that you updated in Step 3. Then set the value of the
           HTTP ``If-Match`` header to the value of the ``ETag`` header that
           CloudFront returned when you submitted the
           ``GET Streaming Distribution Config`` request in Step 2.

        #. Review the response to the ``PUT Streaming Distribution Config``
           request to confirm that the distribution was successfully disabled.

        #. Submit a ``GET Streaming Distribution Config`` request to confirm
           that your changes have propagated. When propagation is complete, the
           value of ``Status`` is ``Deployed``.

        #. Submit a ``DELETE Streaming Distribution`` request. Set the value of
           the HTTP ``If-Match`` header to the value of the ``ETag`` header that
           CloudFront returned when you submitted the
           ``GET Streaming Distribution Config`` request in Step 2.

        #. Review the response to your ``DELETE Streaming Distribution`` request
           to confirm that the distribution was successfully deleted.

        For information about deleting a distribution using the CloudFront
        console, see `Deleting a
        Distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param id: The distribution ID.
        :param if_match: The value of the ``ETag`` header that you received when you disabled the
        streaming distribution.
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises NoSuchStreamingDistribution:
        :raises StreamingDistributionNotDisabled:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DeleteVpcOrigin")
    def delete_vpc_origin(
        self, context: RequestContext, id: string, if_match: string, **kwargs
    ) -> DeleteVpcOriginResult:
        """Delete an Amazon CloudFront VPC origin.

        :param id: The VPC origin ID.
        :param if_match: The version identifier of the VPC origin to delete.
        :returns: DeleteVpcOriginResult
        :raises CannotDeleteEntityWhileInUse:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises IllegalDelete:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DescribeFunction")
    def describe_function(
        self, context: RequestContext, name: string, stage: FunctionStage | None = None, **kwargs
    ) -> DescribeFunctionResult:
        """Gets configuration information and metadata about a CloudFront function,
        but not the function's code. To get a function's code, use
        ``GetFunction``.

        To get configuration information and metadata about a function, you must
        provide the function's name and stage. To get these values, you can use
        ``ListFunctions``.

        :param name: The name of the function that you are getting information about.
        :param stage: The function's stage, either ``DEVELOPMENT`` or ``LIVE``.
        :returns: DescribeFunctionResult
        :raises UnsupportedOperation:
        :raises NoSuchFunctionExists:
        """
        raise NotImplementedError

    @handler("DescribeKeyValueStore")
    def describe_key_value_store(
        self, context: RequestContext, name: KeyValueStoreName, **kwargs
    ) -> DescribeKeyValueStoreResult:
        """Specifies the key value store and its configuration.

        :param name: The name of the key value store.
        :returns: DescribeKeyValueStoreResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("DisassociateDistributionTenantWebACL")
    def disassociate_distribution_tenant_web_acl(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> DisassociateDistributionTenantWebACLResult:
        """Disassociates a distribution tenant from the WAF web ACL.

        :param id: The ID of the distribution tenant.
        :param if_match: The current version of the distribution tenant that you're
        disassociating from the WAF web ACL.
        :returns: DisassociateDistributionTenantWebACLResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("DisassociateDistributionWebACL")
    def disassociate_distribution_web_acl(
        self, context: RequestContext, id: string, if_match: string | None = None, **kwargs
    ) -> DisassociateDistributionWebACLResult:
        """Disassociates a distribution from the WAF web ACL.

        :param id: The ID of the distribution.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        distribution that you're disassociating from the WAF web ACL.
        :returns: DisassociateDistributionWebACLResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("GetAnycastIpList")
    def get_anycast_ip_list(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetAnycastIpListResult:
        """Gets an Anycast static IP list.

        :param id: The ID of the Anycast static IP list.
        :returns: GetAnycastIpListResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("GetCachePolicy")
    def get_cache_policy(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetCachePolicyResult:
        """Gets a cache policy, including the following metadata:

        -  The policy's identifier.

        -  The date and time when the policy was last modified.

        To get a cache policy, you must provide the policy's identifier. If the
        cache policy is attached to a distribution's cache behavior, you can get
        the policy's identifier using ``ListDistributions`` or
        ``GetDistribution``. If the cache policy is not attached to a cache
        behavior, you can get the identifier using ``ListCachePolicies``.

        :param id: The unique identifier for the cache policy.
        :returns: GetCachePolicyResult
        :raises NoSuchCachePolicy:
        :raises AccessDenied:
        """
        raise NotImplementedError

    @handler("GetCachePolicyConfig")
    def get_cache_policy_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetCachePolicyConfigResult:
        """Gets a cache policy configuration.

        To get a cache policy configuration, you must provide the policy's
        identifier. If the cache policy is attached to a distribution's cache
        behavior, you can get the policy's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the cache policy is not
        attached to a cache behavior, you can get the identifier using
        ``ListCachePolicies``.

        :param id: The unique identifier for the cache policy.
        :returns: GetCachePolicyConfigResult
        :raises NoSuchCachePolicy:
        :raises AccessDenied:
        """
        raise NotImplementedError

    @handler("GetCloudFrontOriginAccessIdentity")
    def get_cloud_front_origin_access_identity(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetCloudFrontOriginAccessIdentityResult:
        """Get the information about an origin access identity.

        :param id: The identity's ID.
        :returns: GetCloudFrontOriginAccessIdentityResult
        :raises AccessDenied:
        :raises NoSuchCloudFrontOriginAccessIdentity:
        """
        raise NotImplementedError

    @handler("GetCloudFrontOriginAccessIdentityConfig")
    def get_cloud_front_origin_access_identity_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetCloudFrontOriginAccessIdentityConfigResult:
        """Get the configuration information about an origin access identity.

        :param id: The identity's ID.
        :returns: GetCloudFrontOriginAccessIdentityConfigResult
        :raises AccessDenied:
        :raises NoSuchCloudFrontOriginAccessIdentity:
        """
        raise NotImplementedError

    @handler("GetConnectionGroup")
    def get_connection_group(
        self, context: RequestContext, identifier: string, **kwargs
    ) -> GetConnectionGroupResult:
        """Gets information about a connection group.

        :param identifier: The ID, name, or Amazon Resource Name (ARN) of the connection group.
        :returns: GetConnectionGroupResult
        :raises AccessDenied:
        :raises EntityNotFound:
        """
        raise NotImplementedError

    @handler("GetConnectionGroupByRoutingEndpoint")
    def get_connection_group_by_routing_endpoint(
        self, context: RequestContext, routing_endpoint: string, **kwargs
    ) -> GetConnectionGroupByRoutingEndpointResult:
        """Gets information about a connection group by using the endpoint that you
        specify.

        :param routing_endpoint: The routing endpoint for the target connection group, such as
        d111111abcdef8.
        :returns: GetConnectionGroupByRoutingEndpointResult
        :raises AccessDenied:
        :raises EntityNotFound:
        """
        raise NotImplementedError

    @handler("GetContinuousDeploymentPolicy")
    def get_continuous_deployment_policy(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetContinuousDeploymentPolicyResult:
        """Gets a continuous deployment policy, including metadata (the policy's
        identifier and the date and time when the policy was last modified).

        :param id: The identifier of the continuous deployment policy that you are getting.
        :returns: GetContinuousDeploymentPolicyResult
        :raises AccessDenied:
        :raises NoSuchContinuousDeploymentPolicy:
        """
        raise NotImplementedError

    @handler("GetContinuousDeploymentPolicyConfig")
    def get_continuous_deployment_policy_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetContinuousDeploymentPolicyConfigResult:
        """Gets configuration information about a continuous deployment policy.

        :param id: The identifier of the continuous deployment policy whose configuration
        you are getting.
        :returns: GetContinuousDeploymentPolicyConfigResult
        :raises AccessDenied:
        :raises NoSuchContinuousDeploymentPolicy:
        """
        raise NotImplementedError

    @handler("GetDistribution")
    def get_distribution(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetDistributionResult:
        """Get the information about a distribution.

        :param id: The distribution's ID.
        :returns: GetDistributionResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        """
        raise NotImplementedError

    @handler("GetDistributionConfig")
    def get_distribution_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetDistributionConfigResult:
        """Get the configuration information about a distribution.

        :param id: The distribution's ID.
        :returns: GetDistributionConfigResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        """
        raise NotImplementedError

    @handler("GetDistributionTenant")
    def get_distribution_tenant(
        self, context: RequestContext, identifier: string, **kwargs
    ) -> GetDistributionTenantResult:
        """Gets information about a distribution tenant.

        :param identifier: The identifier of the distribution tenant.
        :returns: GetDistributionTenantResult
        :raises AccessDenied:
        :raises EntityNotFound:
        """
        raise NotImplementedError

    @handler("GetDistributionTenantByDomain")
    def get_distribution_tenant_by_domain(
        self, context: RequestContext, domain: string, **kwargs
    ) -> GetDistributionTenantByDomainResult:
        """Gets information about a distribution tenant by the associated domain.

        :param domain: A domain name associated with the target distribution tenant.
        :returns: GetDistributionTenantByDomainResult
        :raises AccessDenied:
        :raises EntityNotFound:
        """
        raise NotImplementedError

    @handler("GetFieldLevelEncryption")
    def get_field_level_encryption(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetFieldLevelEncryptionResult:
        """Get the field-level encryption configuration information.

        :param id: Request the ID for the field-level encryption configuration information.
        :returns: GetFieldLevelEncryptionResult
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionConfig:
        """
        raise NotImplementedError

    @handler("GetFieldLevelEncryptionConfig")
    def get_field_level_encryption_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetFieldLevelEncryptionConfigResult:
        """Get the field-level encryption configuration information.

        :param id: Request the ID for the field-level encryption configuration information.
        :returns: GetFieldLevelEncryptionConfigResult
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionConfig:
        """
        raise NotImplementedError

    @handler("GetFieldLevelEncryptionProfile")
    def get_field_level_encryption_profile(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetFieldLevelEncryptionProfileResult:
        """Get the field-level encryption profile information.

        :param id: Get the ID for the field-level encryption profile information.
        :returns: GetFieldLevelEncryptionProfileResult
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionProfile:
        """
        raise NotImplementedError

    @handler("GetFieldLevelEncryptionProfileConfig")
    def get_field_level_encryption_profile_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetFieldLevelEncryptionProfileConfigResult:
        """Get the field-level encryption profile configuration information.

        :param id: Get the ID for the field-level encryption profile configuration
        information.
        :returns: GetFieldLevelEncryptionProfileConfigResult
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionProfile:
        """
        raise NotImplementedError

    @handler("GetFunction")
    def get_function(
        self, context: RequestContext, name: string, stage: FunctionStage | None = None, **kwargs
    ) -> GetFunctionResult:
        """Gets the code of a CloudFront function. To get configuration information
        and metadata about a function, use ``DescribeFunction``.

        To get a function's code, you must provide the function's name and
        stage. To get these values, you can use ``ListFunctions``.

        :param name: The name of the function whose code you are getting.
        :param stage: The function's stage, either ``DEVELOPMENT`` or ``LIVE``.
        :returns: GetFunctionResult
        :raises UnsupportedOperation:
        :raises NoSuchFunctionExists:
        """
        raise NotImplementedError

    @handler("GetInvalidation")
    def get_invalidation(
        self, context: RequestContext, distribution_id: string, id: string, **kwargs
    ) -> GetInvalidationResult:
        """Get the information about an invalidation.

        :param distribution_id: The distribution's ID.
        :param id: The identifier for the invalidation request, for example,
        ``IDFDVBD632BHDS5``.
        :returns: GetInvalidationResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises NoSuchInvalidation:
        """
        raise NotImplementedError

    @handler("GetInvalidationForDistributionTenant")
    def get_invalidation_for_distribution_tenant(
        self, context: RequestContext, distribution_tenant_id: string, id: string, **kwargs
    ) -> GetInvalidationForDistributionTenantResult:
        """Gets information about a specific invalidation for a distribution
        tenant.

        :param distribution_tenant_id: The ID of the distribution tenant.
        :param id: The ID of the invalidation to retrieve.
        :returns: GetInvalidationForDistributionTenantResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises NoSuchInvalidation:
        """
        raise NotImplementedError

    @handler("GetKeyGroup")
    def get_key_group(self, context: RequestContext, id: string, **kwargs) -> GetKeyGroupResult:
        """Gets a key group, including the date and time when the key group was
        last modified.

        To get a key group, you must provide the key group's identifier. If the
        key group is referenced in a distribution's cache behavior, you can get
        the key group's identifier using ``ListDistributions`` or
        ``GetDistribution``. If the key group is not referenced in a cache
        behavior, you can get the identifier using ``ListKeyGroups``.

        :param id: The identifier of the key group that you are getting.
        :returns: GetKeyGroupResult
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("GetKeyGroupConfig")
    def get_key_group_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetKeyGroupConfigResult:
        """Gets a key group configuration.

        To get a key group configuration, you must provide the key group's
        identifier. If the key group is referenced in a distribution's cache
        behavior, you can get the key group's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the key group is not
        referenced in a cache behavior, you can get the identifier using
        ``ListKeyGroups``.

        :param id: The identifier of the key group whose configuration you are getting.
        :returns: GetKeyGroupConfigResult
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("GetManagedCertificateDetails")
    def get_managed_certificate_details(
        self, context: RequestContext, identifier: string, **kwargs
    ) -> GetManagedCertificateDetailsResult:
        """Gets details about the CloudFront managed ACM certificate.

        :param identifier: The identifier of the distribution tenant.
        :returns: GetManagedCertificateDetailsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        """
        raise NotImplementedError

    @handler("GetMonitoringSubscription")
    def get_monitoring_subscription(
        self, context: RequestContext, distribution_id: string, **kwargs
    ) -> GetMonitoringSubscriptionResult:
        """Gets information about whether additional CloudWatch metrics are enabled
        for the specified CloudFront distribution.

        :param distribution_id: The ID of the distribution that you are getting metrics information for.
        :returns: GetMonitoringSubscriptionResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises NoSuchMonitoringSubscription:
        """
        raise NotImplementedError

    @handler("GetOriginAccessControl")
    def get_origin_access_control(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetOriginAccessControlResult:
        """Gets a CloudFront origin access control, including its unique
        identifier.

        :param id: The unique identifier of the origin access control.
        :returns: GetOriginAccessControlResult
        :raises AccessDenied:
        :raises NoSuchOriginAccessControl:
        """
        raise NotImplementedError

    @handler("GetOriginAccessControlConfig")
    def get_origin_access_control_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetOriginAccessControlConfigResult:
        """Gets a CloudFront origin access control configuration.

        :param id: The unique identifier of the origin access control.
        :returns: GetOriginAccessControlConfigResult
        :raises AccessDenied:
        :raises NoSuchOriginAccessControl:
        """
        raise NotImplementedError

    @handler("GetOriginRequestPolicy")
    def get_origin_request_policy(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetOriginRequestPolicyResult:
        """Gets an origin request policy, including the following metadata:

        -  The policy's identifier.

        -  The date and time when the policy was last modified.

        To get an origin request policy, you must provide the policy's
        identifier. If the origin request policy is attached to a distribution's
        cache behavior, you can get the policy's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the origin request
        policy is not attached to a cache behavior, you can get the identifier
        using ``ListOriginRequestPolicies``.

        :param id: The unique identifier for the origin request policy.
        :returns: GetOriginRequestPolicyResult
        :raises AccessDenied:
        :raises NoSuchOriginRequestPolicy:
        """
        raise NotImplementedError

    @handler("GetOriginRequestPolicyConfig")
    def get_origin_request_policy_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetOriginRequestPolicyConfigResult:
        """Gets an origin request policy configuration.

        To get an origin request policy configuration, you must provide the
        policy's identifier. If the origin request policy is attached to a
        distribution's cache behavior, you can get the policy's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the origin request
        policy is not attached to a cache behavior, you can get the identifier
        using ``ListOriginRequestPolicies``.

        :param id: The unique identifier for the origin request policy.
        :returns: GetOriginRequestPolicyConfigResult
        :raises AccessDenied:
        :raises NoSuchOriginRequestPolicy:
        """
        raise NotImplementedError

    @handler("GetPublicKey")
    def get_public_key(self, context: RequestContext, id: string, **kwargs) -> GetPublicKeyResult:
        """Gets a public key.

        :param id: The identifier of the public key you are getting.
        :returns: GetPublicKeyResult
        :raises AccessDenied:
        :raises NoSuchPublicKey:
        """
        raise NotImplementedError

    @handler("GetPublicKeyConfig")
    def get_public_key_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetPublicKeyConfigResult:
        """Gets a public key configuration.

        :param id: The identifier of the public key whose configuration you are getting.
        :returns: GetPublicKeyConfigResult
        :raises AccessDenied:
        :raises NoSuchPublicKey:
        """
        raise NotImplementedError

    @handler("GetRealtimeLogConfig")
    def get_realtime_log_config(
        self,
        context: RequestContext,
        name: string | None = None,
        arn: string | None = None,
        **kwargs,
    ) -> GetRealtimeLogConfigResult:
        """Gets a real-time log configuration.

        To get a real-time log configuration, you can provide the
        configuration's name or its Amazon Resource Name (ARN). You must provide
        at least one. If you provide both, CloudFront uses the name to identify
        the real-time log configuration to get.

        :param name: The name of the real-time log configuration to get.
        :param arn: The Amazon Resource Name (ARN) of the real-time log configuration to
        get.
        :returns: GetRealtimeLogConfigResult
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchRealtimeLogConfig:
        """
        raise NotImplementedError

    @handler("GetResponseHeadersPolicy")
    def get_response_headers_policy(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetResponseHeadersPolicyResult:
        """Gets a response headers policy, including metadata (the policy's
        identifier and the date and time when the policy was last modified).

        To get a response headers policy, you must provide the policy's
        identifier. If the response headers policy is attached to a
        distribution's cache behavior, you can get the policy's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the response headers
        policy is not attached to a cache behavior, you can get the identifier
        using ``ListResponseHeadersPolicies``.

        :param id: The identifier for the response headers policy.
        :returns: GetResponseHeadersPolicyResult
        :raises AccessDenied:
        :raises NoSuchResponseHeadersPolicy:
        """
        raise NotImplementedError

    @handler("GetResponseHeadersPolicyConfig")
    def get_response_headers_policy_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetResponseHeadersPolicyConfigResult:
        """Gets a response headers policy configuration.

        To get a response headers policy configuration, you must provide the
        policy's identifier. If the response headers policy is attached to a
        distribution's cache behavior, you can get the policy's identifier using
        ``ListDistributions`` or ``GetDistribution``. If the response headers
        policy is not attached to a cache behavior, you can get the identifier
        using ``ListResponseHeadersPolicies``.

        :param id: The identifier for the response headers policy.
        :returns: GetResponseHeadersPolicyConfigResult
        :raises AccessDenied:
        :raises NoSuchResponseHeadersPolicy:
        """
        raise NotImplementedError

    @handler("GetStreamingDistribution")
    def get_streaming_distribution(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetStreamingDistributionResult:
        """Gets information about a specified RTMP distribution, including the
        distribution configuration.

        :param id: The streaming distribution's ID.
        :returns: GetStreamingDistributionResult
        :raises AccessDenied:
        :raises NoSuchStreamingDistribution:
        """
        raise NotImplementedError

    @handler("GetStreamingDistributionConfig")
    def get_streaming_distribution_config(
        self, context: RequestContext, id: string, **kwargs
    ) -> GetStreamingDistributionConfigResult:
        """Get the configuration information about a streaming distribution.

        :param id: The streaming distribution's ID.
        :returns: GetStreamingDistributionConfigResult
        :raises AccessDenied:
        :raises NoSuchStreamingDistribution:
        """
        raise NotImplementedError

    @handler("GetVpcOrigin")
    def get_vpc_origin(self, context: RequestContext, id: string, **kwargs) -> GetVpcOriginResult:
        """Get the details of an Amazon CloudFront VPC origin.

        :param id: The VPC origin ID.
        :returns: GetVpcOriginResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListAnycastIpLists")
    def list_anycast_ip_lists(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListAnycastIpListsResult:
        """Lists your Anycast static IP lists.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list.
        :param max_items: The maximum number of Anycast static IP lists that you want returned in
        the response.
        :returns: ListAnycastIpListsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListCachePolicies", expand=False)
    def list_cache_policies(
        self, context: RequestContext, request: ListCachePoliciesRequest, **kwargs
    ) -> ListCachePoliciesResult:
        """Gets a list of cache policies.

        You can optionally apply a filter to return only the managed policies
        created by Amazon Web Services, or only the custom policies created in
        your Amazon Web Services account.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param type: A filter to return only the specified kinds of cache policies.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of cache policies.
        :param max_items: The maximum number of cache policies that you want in the response.
        :returns: ListCachePoliciesResult
        :raises NoSuchCachePolicy:
        :raises AccessDenied:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListCloudFrontOriginAccessIdentities")
    def list_cloud_front_origin_access_identities(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListCloudFrontOriginAccessIdentitiesResult:
        """Lists origin access identities.

        :param marker: Use this when paginating results to indicate where to begin in your list
        of origin access identities.
        :param max_items: The maximum number of origin access identities you want in the response
        body.
        :returns: ListCloudFrontOriginAccessIdentitiesResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListConflictingAliases")
    def list_conflicting_aliases(
        self,
        context: RequestContext,
        distribution_id: distributionIdString,
        alias: aliasString,
        marker: string | None = None,
        max_items: listConflictingAliasesMaxItemsInteger | None = None,
        **kwargs,
    ) -> ListConflictingAliasesResult:
        """Gets a list of aliases (also called CNAMEs or alternate domain names)
        that conflict or overlap with the provided alias, and the associated
        CloudFront distributions and Amazon Web Services accounts for each
        conflicting alias. In the returned list, the distribution and account
        IDs are partially hidden, which allows you to identify the distributions
        and accounts that you own, but helps to protect the information of ones
        that you don't own.

        Use this operation to find aliases that are in use in CloudFront that
        conflict or overlap with the provided alias. For example, if you provide
        ``www.example.com`` as input, the returned list can include
        ``www.example.com`` and the overlapping wildcard alternate domain name
        (``*.example.com``), if they exist. If you provide ``*.example.com`` as
        input, the returned list can include ``*.example.com`` and any alternate
        domain names covered by that wildcard (for example, ``www.example.com``,
        ``test.example.com``, ``dev.example.com``, and so on), if they exist.

        To list conflicting aliases, you provide the alias to search and the ID
        of a distribution in your account that has an attached SSL/TLS
        certificate that includes the provided alias. For more information,
        including how to set up the distribution and certificate, see `Moving an
        alternate domain name to a different
        distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move>`__
        in the *Amazon CloudFront Developer Guide*.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param distribution_id: The ID of a distribution in your account that has an attached SSL/TLS
        certificate that includes the provided alias.
        :param alias: The alias (also called a CNAME) to search for conflicting aliases.
        :param marker: Use this field when paginating results to indicate where to begin in the
        list of conflicting aliases.
        :param max_items: The maximum number of conflicting aliases that you want in the response.
        :returns: ListConflictingAliasesResult
        :raises NoSuchDistribution:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListConnectionGroups")
    def list_connection_groups(
        self,
        context: RequestContext,
        association_filter: ConnectionGroupAssociationFilter | None = None,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListConnectionGroupsResult:
        """Lists the connection groups in your Amazon Web Services account.

        :param association_filter: Filter by associated Anycast IP list ID.
        :param marker: The marker for the next set of connection groups to retrieve.
        :param max_items: The maximum number of connection groups to return.
        :returns: ListConnectionGroupsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListContinuousDeploymentPolicies")
    def list_continuous_deployment_policies(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListContinuousDeploymentPoliciesResult:
        """Gets a list of the continuous deployment policies in your Amazon Web
        Services account.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list of continuous deployment policies.
        :param max_items: The maximum number of continuous deployment policies that you want
        returned in the response.
        :returns: ListContinuousDeploymentPoliciesResult
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchContinuousDeploymentPolicy:
        """
        raise NotImplementedError

    @handler("ListDistributionTenants")
    def list_distribution_tenants(
        self,
        context: RequestContext,
        association_filter: DistributionTenantAssociationFilter | None = None,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListDistributionTenantsResult:
        """Lists the distribution tenants in your Amazon Web Services account.

        :param association_filter: Filter by the associated distribution ID or connection group ID.
        :param marker: The marker for the next set of results.
        :param max_items: The maximum number of distribution tenants to return.
        :returns: ListDistributionTenantsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionTenantsByCustomization")
    def list_distribution_tenants_by_customization(
        self,
        context: RequestContext,
        web_acl_arn: string | None = None,
        certificate_arn: string | None = None,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListDistributionTenantsByCustomizationResult:
        """Lists distribution tenants by the customization that you specify.

        You must specify either the ``CertificateArn`` parameter or
        ``WebACLArn`` parameter, but not both in the same request.

        :param web_acl_arn: Filter by the ARN of the associated WAF web ACL.
        :param certificate_arn: Filter by the ARN of the associated ACM certificate.
        :param marker: The marker for the next set of results.
        :param max_items: The maximum number of distribution tenants to return by the specified
        customization.
        :returns: ListDistributionTenantsByCustomizationResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributions")
    def list_distributions(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsResult:
        """List CloudFront distributions.

        :param marker: Use this when paginating results to indicate where to begin in your list
        of distributions.
        :param max_items: The maximum number of distributions you want in the response body.
        :returns: ListDistributionsResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByAnycastIpListId")
    def list_distributions_by_anycast_ip_list_id(
        self,
        context: RequestContext,
        anycast_ip_list_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByAnycastIpListIdResult:
        """Lists the distributions in your account that are associated with the
        specified ``AnycastIpListId``.

        :param anycast_ip_list_id: The ID of the Anycast static IP list.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list.
        :param max_items: The maximum number of distributions that you want returned in the
        response.
        :returns: ListDistributionsByAnycastIpListIdResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByCachePolicyId")
    def list_distributions_by_cache_policy_id(
        self,
        context: RequestContext,
        cache_policy_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByCachePolicyIdResult:
        """Gets a list of distribution IDs for distributions that have a cache
        behavior that's associated with the specified cache policy.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param cache_policy_id: The ID of the cache policy whose associated distribution IDs you want to
        list.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of distribution IDs.
        :param max_items: The maximum number of distribution IDs that you want in the response.
        :returns: ListDistributionsByCachePolicyIdResult
        :raises NoSuchCachePolicy:
        :raises AccessDenied:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByConnectionMode")
    def list_distributions_by_connection_mode(
        self,
        context: RequestContext,
        connection_mode: ConnectionMode,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListDistributionsByConnectionModeResult:
        """Lists the distributions by the connection mode that you specify.

        :param connection_mode: The connection mode to filter distributions by.
        :param marker: The marker for the next set of distributions to retrieve.
        :param max_items: The maximum number of distributions to return.
        :returns: ListDistributionsByConnectionModeResult
        :raises AccessDenied:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByKeyGroup")
    def list_distributions_by_key_group(
        self,
        context: RequestContext,
        key_group_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByKeyGroupResult:
        """Gets a list of distribution IDs for distributions that have a cache
        behavior that references the specified key group.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param key_group_id: The ID of the key group whose associated distribution IDs you are
        listing.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of distribution IDs.
        :param max_items: The maximum number of distribution IDs that you want in the response.
        :returns: ListDistributionsByKeyGroupResult
        :raises InvalidArgument:
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("ListDistributionsByOriginRequestPolicyId")
    def list_distributions_by_origin_request_policy_id(
        self,
        context: RequestContext,
        origin_request_policy_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByOriginRequestPolicyIdResult:
        """Gets a list of distribution IDs for distributions that have a cache
        behavior that's associated with the specified origin request policy.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param origin_request_policy_id: The ID of the origin request policy whose associated distribution IDs
        you want to list.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of distribution IDs.
        :param max_items: The maximum number of distribution IDs that you want in the response.
        :returns: ListDistributionsByOriginRequestPolicyIdResult
        :raises AccessDenied:
        :raises NoSuchOriginRequestPolicy:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByRealtimeLogConfig")
    def list_distributions_by_realtime_log_config(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        realtime_log_config_name: string | None = None,
        realtime_log_config_arn: string | None = None,
        **kwargs,
    ) -> ListDistributionsByRealtimeLogConfigResult:
        """Gets a list of distributions that have a cache behavior that's
        associated with the specified real-time log configuration.

        You can specify the real-time log configuration by its name or its
        Amazon Resource Name (ARN). You must provide at least one. If you
        provide both, CloudFront uses the name to identify the real-time log
        configuration to list distributions for.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list of distributions.
        :param max_items: The maximum number of distributions that you want in the response.
        :param realtime_log_config_name: The name of the real-time log configuration whose associated
        distributions you want to list.
        :param realtime_log_config_arn: The Amazon Resource Name (ARN) of the real-time log configuration whose
        associated distributions you want to list.
        :returns: ListDistributionsByRealtimeLogConfigResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByResponseHeadersPolicyId")
    def list_distributions_by_response_headers_policy_id(
        self,
        context: RequestContext,
        response_headers_policy_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByResponseHeadersPolicyIdResult:
        """Gets a list of distribution IDs for distributions that have a cache
        behavior that's associated with the specified response headers policy.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param response_headers_policy_id: The ID of the response headers policy whose associated distribution IDs
        you want to list.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of distribution IDs.
        :param max_items: The maximum number of distribution IDs that you want to get in the
        response.
        :returns: ListDistributionsByResponseHeadersPolicyIdResult
        :raises AccessDenied:
        :raises NoSuchResponseHeadersPolicy:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByVpcOriginId")
    def list_distributions_by_vpc_origin_id(
        self,
        context: RequestContext,
        vpc_origin_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByVpcOriginIdResult:
        """List CloudFront distributions by their VPC origin ID.

        :param vpc_origin_id: The VPC origin ID.
        :param marker: The marker associated with the VPC origin distributions list.
        :param max_items: The maximum number of items included in the list.
        :returns: ListDistributionsByVpcOriginIdResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDistributionsByWebACLId")
    def list_distributions_by_web_acl_id(
        self,
        context: RequestContext,
        web_acl_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListDistributionsByWebACLIdResult:
        """List the distributions that are associated with a specified WAF web ACL.

        :param web_acl_id: The ID of the WAF web ACL that you want to list the associated
        distributions.
        :param marker: Use ``Marker`` and ``MaxItems`` to control pagination of results.
        :param max_items: The maximum number of distributions that you want CloudFront to return
        in the response body.
        :returns: ListDistributionsByWebACLIdResult
        :raises InvalidWebACLId:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListDomainConflicts")
    def list_domain_conflicts(
        self,
        context: RequestContext,
        domain: string,
        domain_control_validation_resource: DistributionResourceId,
        max_items: integer | None = None,
        marker: string | None = None,
        **kwargs,
    ) -> ListDomainConflictsResult:
        """Lists existing domain associations that conflict with the domain that
        you specify.

        You can use this API operation when transferring domains to identify
        potential domain conflicts. Domain conflicts must be resolved first
        before they can be moved.

        :param domain: The domain to check for conflicts.
        :param domain_control_validation_resource: The distribution resource identifier.
        :param max_items: The maximum number of domain conflicts to return.
        :param marker: The marker for the next set of domain conflicts.
        :returns: ListDomainConflictsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListFieldLevelEncryptionConfigs")
    def list_field_level_encryption_configs(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListFieldLevelEncryptionConfigsResult:
        """List all field-level encryption configurations that have been created in
        CloudFront for this account.

        :param marker: Use this when paginating results to indicate where to begin in your list
        of configurations.
        :param max_items: The maximum number of field-level encryption configurations you want in
        the response body.
        :returns: ListFieldLevelEncryptionConfigsResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListFieldLevelEncryptionProfiles")
    def list_field_level_encryption_profiles(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListFieldLevelEncryptionProfilesResult:
        """Request a list of field-level encryption profiles that have been created
        in CloudFront for this account.

        :param marker: Use this when paginating results to indicate where to begin in your list
        of profiles.
        :param max_items: The maximum number of field-level encryption profiles you want in the
        response body.
        :returns: ListFieldLevelEncryptionProfilesResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListFunctions")
    def list_functions(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        stage: FunctionStage | None = None,
        **kwargs,
    ) -> ListFunctionsResult:
        """Gets a list of all CloudFront functions in your Amazon Web Services
        account.

        You can optionally apply a filter to return only the functions that are
        in the specified stage, either ``DEVELOPMENT`` or ``LIVE``.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list of functions.
        :param max_items: The maximum number of functions that you want in the response.
        :param stage: An optional filter to return only the functions that are in the
        specified stage, either ``DEVELOPMENT`` or ``LIVE``.
        :returns: ListFunctionsResult
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListInvalidations")
    def list_invalidations(
        self,
        context: RequestContext,
        distribution_id: string,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListInvalidationsResult:
        """Lists invalidation batches.

        :param distribution_id: The distribution's ID.
        :param marker: Use this parameter when paginating results to indicate where to begin in
        your list of invalidation batches.
        :param max_items: The maximum number of invalidation batches that you want in the response
        body.
        :returns: ListInvalidationsResult
        :raises NoSuchDistribution:
        :raises AccessDenied:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListInvalidationsForDistributionTenant")
    def list_invalidations_for_distribution_tenant(
        self,
        context: RequestContext,
        id: string,
        marker: string | None = None,
        max_items: integer | None = None,
        **kwargs,
    ) -> ListInvalidationsForDistributionTenantResult:
        """Lists the invalidations for a distribution tenant.

        :param id: The ID of the distribution tenant.
        :param marker: Use this parameter when paginating results to indicate where to begin in
        your list of invalidation batches.
        :param max_items: The maximum number of invalidations to return for the distribution
        tenant.
        :returns: ListInvalidationsForDistributionTenantResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListKeyGroups")
    def list_key_groups(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListKeyGroupsResult:
        """Gets a list of key groups.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list of key groups.
        :param max_items: The maximum number of key groups that you want in the response.
        :returns: ListKeyGroupsResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListKeyValueStores")
    def list_key_value_stores(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        status: string | None = None,
        **kwargs,
    ) -> ListKeyValueStoresResult:
        """Specifies the key value stores to list.

        :param marker: The marker associated with the key value stores list.
        :param max_items: The maximum number of items in the key value stores list.
        :param status: The status of the request for the key value stores list.
        :returns: ListKeyValueStoresResult
        :raises AccessDenied:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListOriginAccessControls")
    def list_origin_access_controls(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListOriginAccessControlsResult:
        """Gets the list of CloudFront origin access controls (OACs) in this Amazon
        Web Services account.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send another request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the next request.

        If you're not using origin access controls for your Amazon Web Services
        account, the ``ListOriginAccessControls`` operation doesn't return the
        ``Items`` element in the response.

        :param marker: Use this field when paginating results to indicate where to begin in
        your list of origin access controls.
        :param max_items: The maximum number of origin access controls that you want in the
        response.
        :returns: ListOriginAccessControlsResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListOriginRequestPolicies", expand=False)
    def list_origin_request_policies(
        self, context: RequestContext, request: ListOriginRequestPoliciesRequest, **kwargs
    ) -> ListOriginRequestPoliciesResult:
        """Gets a list of origin request policies.

        You can optionally apply a filter to return only the managed policies
        created by Amazon Web Services, or only the custom policies created in
        your Amazon Web Services account.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param type: A filter to return only the specified kinds of origin request policies.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of origin request policies.
        :param max_items: The maximum number of origin request policies that you want in the
        response.
        :returns: ListOriginRequestPoliciesResult
        :raises AccessDenied:
        :raises NoSuchOriginRequestPolicy:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListPublicKeys")
    def list_public_keys(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListPublicKeysResult:
        """List all public keys that have been added to CloudFront for this
        account.

        :param marker: Use this when paginating results to indicate where to begin in your list
        of public keys.
        :param max_items: The maximum number of public keys you want in the response body.
        :returns: ListPublicKeysResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListRealtimeLogConfigs")
    def list_realtime_log_configs(
        self,
        context: RequestContext,
        max_items: string | None = None,
        marker: string | None = None,
        **kwargs,
    ) -> ListRealtimeLogConfigsResult:
        """Gets a list of real-time log configurations.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param max_items: The maximum number of real-time log configurations that you want in the
        response.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of real-time log configurations.
        :returns: ListRealtimeLogConfigsResult
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchRealtimeLogConfig:
        """
        raise NotImplementedError

    @handler("ListResponseHeadersPolicies", expand=False)
    def list_response_headers_policies(
        self, context: RequestContext, request: ListResponseHeadersPoliciesRequest, **kwargs
    ) -> ListResponseHeadersPoliciesResult:
        """Gets a list of response headers policies.

        You can optionally apply a filter to get only the managed policies
        created by Amazon Web Services, or only the custom policies created in
        your Amazon Web Services account.

        You can optionally specify the maximum number of items to receive in the
        response. If the total number of items in the list exceeds the maximum
        that you specify, or the default maximum, the response is paginated. To
        get the next page of items, send a subsequent request that specifies the
        ``NextMarker`` value from the current response as the ``Marker`` value
        in the subsequent request.

        :param type: A filter to get only the specified kind of response headers policies.
        :param marker: Use this field when paginating results to indicate where to begin in
        your list of response headers policies.
        :param max_items: The maximum number of response headers policies that you want to get in
        the response.
        :returns: ListResponseHeadersPoliciesResult
        :raises AccessDenied:
        :raises NoSuchResponseHeadersPolicy:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListStreamingDistributions")
    def list_streaming_distributions(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListStreamingDistributionsResult:
        """List streaming distributions.

        :param marker: The value that you provided for the ``Marker`` request parameter.
        :param max_items: The value that you provided for the ``MaxItems`` request parameter.
        :returns: ListStreamingDistributionsResult
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource: ResourceARN, **kwargs
    ) -> ListTagsForResourceResult:
        """List tags for a CloudFront resource. For more information, see `Tagging
        a
        distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param resource: An ARN of a CloudFront resource.
        :returns: ListTagsForResourceResult
        :raises AccessDenied:
        :raises InvalidTagging:
        :raises InvalidArgument:
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("ListVpcOrigins")
    def list_vpc_origins(
        self,
        context: RequestContext,
        marker: string | None = None,
        max_items: string | None = None,
        **kwargs,
    ) -> ListVpcOriginsResult:
        """List the CloudFront VPC origins in your account.

        :param marker: The marker associated with the VPC origins list.
        :param max_items: The maximum number of items included in the list.
        :returns: ListVpcOriginsResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        """
        raise NotImplementedError

    @handler("PublishFunction")
    def publish_function(
        self, context: RequestContext, name: string, if_match: string, **kwargs
    ) -> PublishFunctionResult:
        """Publishes a CloudFront function by copying the function code from the
        ``DEVELOPMENT`` stage to ``LIVE``. This automatically updates all cache
        behaviors that are using this function to use the newly published copy
        in the ``LIVE`` stage.

        When a function is published to the ``LIVE`` stage, you can attach the
        function to a distribution's cache behavior, using the function's Amazon
        Resource Name (ARN).

        To publish a function, you must provide the function's name and version
        (``ETag`` value). To get these values, you can use ``ListFunctions`` and
        ``DescribeFunction``.

        :param name: The name of the function that you are publishing.
        :param if_match: The current version (``ETag`` value) of the function that you are
        publishing, which you can get using ``DescribeFunction``.
        :returns: PublishFunctionResult
        :raises PreconditionFailed:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        :raises NoSuchFunctionExists:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource: ResourceARN, tags: Tags, **kwargs
    ) -> None:
        """Add tags to a CloudFront resource. For more information, see `Tagging a
        distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param resource: An ARN of a CloudFront resource.
        :param tags: A complex type that contains zero or more ``Tag`` elements.
        :raises AccessDenied:
        :raises InvalidTagging:
        :raises InvalidArgument:
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("TestFunction")
    def test_function(
        self,
        context: RequestContext,
        name: string,
        if_match: string,
        event_object: FunctionEventObject,
        stage: FunctionStage | None = None,
        **kwargs,
    ) -> TestFunctionResult:
        """Tests a CloudFront function.

        To test a function, you provide an *event object* that represents an
        HTTP request or response that your CloudFront distribution could receive
        in production. CloudFront runs the function, passing it the event object
        that you provided, and returns the function's result (the modified event
        object) in the response. The response also contains function logs and
        error messages, if any exist. For more information about testing
        functions, see `Testing
        functions <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function>`__
        in the *Amazon CloudFront Developer Guide*.

        To test a function, you provide the function's name and version
        (``ETag`` value) along with the event object. To get the function's name
        and version, you can use ``ListFunctions`` and ``DescribeFunction``.

        :param name: The name of the function that you are testing.
        :param if_match: The current version (``ETag`` value) of the function that you are
        testing, which you can get using ``DescribeFunction``.
        :param event_object: The event object to test the function with.
        :param stage: The stage of the function that you are testing, either ``DEVELOPMENT``
        or ``LIVE``.
        :returns: TestFunctionResult
        :raises TestFunctionFailed:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        :raises NoSuchFunctionExists:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource: ResourceARN, tag_keys: TagKeys, **kwargs
    ) -> None:
        """Remove tags from a CloudFront resource. For more information, see
        `Tagging a
        distribution <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html>`__
        in the *Amazon CloudFront Developer Guide*.

        :param resource: An ARN of a CloudFront resource.
        :param tag_keys: A complex type that contains zero or more ``Tag`` key elements.
        :raises AccessDenied:
        :raises InvalidTagging:
        :raises InvalidArgument:
        :raises NoSuchResource:
        """
        raise NotImplementedError

    @handler("UpdateCachePolicy")
    def update_cache_policy(
        self,
        context: RequestContext,
        cache_policy_config: CachePolicyConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateCachePolicyResult:
        """Updates a cache policy configuration.

        When you update a cache policy configuration, all the fields are updated
        with the values provided in the request. You cannot update some fields
        independent of others. To update a cache policy configuration:

        #. Use ``GetCachePolicyConfig`` to get the current configuration.

        #. Locally modify the fields in the cache policy configuration that you
           want to update.

        #. Call ``UpdateCachePolicy`` by providing the entire cache policy
           configuration, including the fields that you modified and those that
           you didn't.

        :param cache_policy_config: A cache policy configuration.
        :param id: The unique identifier for the cache policy that you are updating.
        :param if_match: The version of the cache policy that you are updating.
        :returns: UpdateCachePolicyResult
        :raises NoSuchCachePolicy:
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises TooManyHeadersInCachePolicy:
        :raises CachePolicyAlreadyExists:
        :raises TooManyCookiesInCachePolicy:
        :raises InconsistentQuantities:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises TooManyQueryStringsInCachePolicy:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateCloudFrontOriginAccessIdentity")
    def update_cloud_front_origin_access_identity(
        self,
        context: RequestContext,
        cloud_front_origin_access_identity_config: CloudFrontOriginAccessIdentityConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateCloudFrontOriginAccessIdentityResult:
        """Update an origin access identity.

        :param cloud_front_origin_access_identity_config: The identity's configuration information.
        :param id: The identity's id.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        identity's configuration.
        :returns: UpdateCloudFrontOriginAccessIdentityResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises MissingBody:
        :raises InconsistentQuantities:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        :raises NoSuchCloudFrontOriginAccessIdentity:
        """
        raise NotImplementedError

    @handler("UpdateConnectionGroup")
    def update_connection_group(
        self,
        context: RequestContext,
        id: string,
        if_match: string,
        ipv6_enabled: boolean | None = None,
        anycast_ip_list_id: string | None = None,
        enabled: boolean | None = None,
        **kwargs,
    ) -> UpdateConnectionGroupResult:
        """Updates a connection group.

        :param id: The ID of the connection group.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        connection group that you're updating.
        :param ipv6_enabled: Enable IPv6 for the connection group.
        :param anycast_ip_list_id: The ID of the Anycast static IP list.
        :param enabled: Whether the connection group is enabled.
        :returns: UpdateConnectionGroupResult
        :raises PreconditionFailed:
        :raises ResourceInUse:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises EntityAlreadyExists:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateContinuousDeploymentPolicy")
    def update_continuous_deployment_policy(
        self,
        context: RequestContext,
        continuous_deployment_policy_config: ContinuousDeploymentPolicyConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateContinuousDeploymentPolicyResult:
        """Updates a continuous deployment policy. You can update a continuous
        deployment policy to enable or disable it, to change the percentage of
        traffic that it sends to the staging distribution, or to change the
        staging distribution that it sends traffic to.

        When you update a continuous deployment policy configuration, all the
        fields are updated with the values that are provided in the request. You
        cannot update some fields independent of others. To update a continuous
        deployment policy configuration:

        #. Use ``GetContinuousDeploymentPolicyConfig`` to get the current
           configuration.

        #. Locally modify the fields in the continuous deployment policy
           configuration that you want to update.

        #. Use ``UpdateContinuousDeploymentPolicy``, providing the entire
           continuous deployment policy configuration, including the fields that
           you modified and those that you didn't.

        :param continuous_deployment_policy_config: The continuous deployment policy configuration.
        :param id: The identifier of the continuous deployment policy that you are
        updating.
        :param if_match: The current version (``ETag`` value) of the continuous deployment policy
        that you are updating.
        :returns: UpdateContinuousDeploymentPolicyResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises StagingDistributionInUse:
        :raises InconsistentQuantities:
        :raises InvalidArgument:
        :raises NoSuchContinuousDeploymentPolicy:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateDistribution")
    def update_distribution(
        self,
        context: RequestContext,
        distribution_config: DistributionConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateDistributionResult:
        """Updates the configuration for a CloudFront distribution.

        The update process includes getting the current distribution
        configuration, updating it to make your changes, and then submitting an
        ``UpdateDistribution`` request to make the updates.

        **To update a web distribution using the CloudFront API**

        #. Use ``GetDistributionConfig`` to get the current configuration,
           including the version identifier (``ETag``).

        #. Update the distribution configuration that was returned in the
           response. Note the following important requirements and restrictions:

           -  You must copy the ``ETag`` field value from the response. (You'll
              use it for the ``IfMatch`` parameter in your request.) Then,
              remove the ``ETag`` field from the distribution configuration.

           -  You can't change the value of ``CallerReference``.

        #. Submit an ``UpdateDistribution`` request, providing the updated
           distribution configuration. The new configuration replaces the
           existing configuration. The values that you specify in an
           ``UpdateDistribution`` request are not merged into your existing
           configuration. Make sure to include all fields: the ones that you
           modified and also the ones that you didn't.

        :param distribution_config: The distribution's configuration information.
        :param id: The distribution's id.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        distribution's configuration.
        :returns: UpdateDistributionResult
        :raises AccessDenied:
        :raises TooManyDistributionsAssociatedToOriginAccessControl:
        :raises InvalidDefaultRootObject:
        :raises InvalidDomainNameForOriginAccessControl:
        :raises InvalidQueryStringParameters:
        :raises TooManyTrustedSigners:
        :raises TooManyCookieNamesInWhiteList:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidErrorCode:
        :raises IllegalOriginAccessConfiguration:
        :raises TooManyFunctionAssociations:
        :raises TooManyOriginCustomHeaders:
        :raises InvalidForwardCookies:
        :raises InvalidMinimumProtocolVersion:
        :raises NoSuchCachePolicy:
        :raises TooManyKeyGroupsAssociatedToDistribution:
        :raises TooManyDistributionsAssociatedToCachePolicy:
        :raises InvalidRequiredProtocol:
        :raises TooManyDistributionsWithFunctionAssociations:
        :raises TooManyOriginGroupsPerDistribution:
        :raises InvalidTTLOrder:
        :raises IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior:
        :raises InvalidOriginKeepaliveTimeout:
        :raises InvalidArgument:
        :raises InvalidOriginReadTimeout:
        :raises IllegalUpdate:
        :raises InvalidOriginAccessControl:
        :raises EntityNotFound:
        :raises StagingDistributionInUse:
        :raises InvalidHeadersForS3Origin:
        :raises TrustedSignerDoesNotExist:
        :raises InvalidWebACLId:
        :raises TooManyDistributionsWithSingleFunctionARN:
        :raises InvalidRelativePath:
        :raises TooManyLambdaFunctionAssociations:
        :raises NoSuchDistribution:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyDistributionsAssociatedToFieldLevelEncryptionConfig:
        :raises InconsistentQuantities:
        :raises InvalidLocationCode:
        :raises InvalidOriginAccessIdentity:
        :raises TooManyDistributionCNAMEs:
        :raises NoSuchContinuousDeploymentPolicy:
        :raises InvalidIfMatchVersion:
        :raises TooManyDistributionsAssociatedToOriginRequestPolicy:
        :raises TooManyQueryStringParameters:
        :raises RealtimeLogConfigOwnerMismatch:
        :raises PreconditionFailed:
        :raises ContinuousDeploymentPolicyInUse:
        :raises MissingBody:
        :raises TooManyHeadersInForwardedValues:
        :raises InvalidLambdaFunctionAssociation:
        :raises CNAMEAlreadyExists:
        :raises TooManyCertificates:
        :raises TrustedKeyGroupDoesNotExist:
        :raises TooManyDistributionsAssociatedToResponseHeadersPolicy:
        :raises NoSuchResponseHeadersPolicy:
        :raises NoSuchRealtimeLogConfig:
        :raises InvalidResponseCode:
        :raises InvalidGeoRestrictionParameter:
        :raises TooManyOrigins:
        :raises InvalidViewerCertificate:
        :raises InvalidFunctionAssociation:
        :raises TooManyDistributionsWithLambdaAssociations:
        :raises TooManyDistributionsAssociatedToKeyGroup:
        :raises NoSuchOrigin:
        :raises TooManyCacheBehaviors:
        """
        raise NotImplementedError

    @handler("UpdateDistributionTenant")
    def update_distribution_tenant(
        self,
        context: RequestContext,
        id: string,
        if_match: string,
        distribution_id: string | None = None,
        domains: DomainList | None = None,
        customizations: Customizations | None = None,
        parameters: Parameters | None = None,
        connection_group_id: string | None = None,
        managed_certificate_request: ManagedCertificateRequest | None = None,
        enabled: boolean | None = None,
        **kwargs,
    ) -> UpdateDistributionTenantResult:
        """Updates a distribution tenant.

        :param id: The ID of the distribution tenant.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        distribution tenant to update.
        :param distribution_id: The ID for the multi-tenant distribution.
        :param domains: The domains to update for the distribution tenant.
        :param customizations: Customizations for the distribution tenant.
        :param parameters: A list of parameter values to add to the resource.
        :param connection_group_id: The ID of the target connection group.
        :param managed_certificate_request: An object that contains the CloudFront managed ACM certificate request.
        :param enabled: Indicates whether the distribution tenant should be updated to an
        enabled state.
        :returns: UpdateDistributionTenantResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises EntityAlreadyExists:
        :raises CNAMEAlreadyExists:
        :raises InvalidAssociation:
        :raises EntityLimitExceeded:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateDistributionWithStagingConfig")
    def update_distribution_with_staging_config(
        self,
        context: RequestContext,
        id: string,
        staging_distribution_id: string | None = None,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateDistributionWithStagingConfigResult:
        """Copies the staging distribution's configuration to its corresponding
        primary distribution. The primary distribution retains its ``Aliases``
        (also known as alternate domain names or CNAMEs) and
        ``ContinuousDeploymentPolicyId`` value, but otherwise its configuration
        is overwritten to match the staging distribution.

        You can use this operation in a continuous deployment workflow after you
        have tested configuration changes on the staging distribution. After
        using a continuous deployment policy to move a portion of your domain
        name's traffic to the staging distribution and verifying that it works
        as intended, you can use this operation to copy the staging
        distribution's configuration to the primary distribution. This action
        will disable the continuous deployment policy and move your domain's
        traffic back to the primary distribution.

        This API operation requires the following IAM permissions:

        -  `GetDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html>`__

        -  `UpdateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html>`__

        :param id: The identifier of the primary distribution to which you are copying a
        staging distribution's configuration.
        :param staging_distribution_id: The identifier of the staging distribution whose configuration you are
        copying to the primary distribution.
        :param if_match: The current versions (``ETag`` values) of both primary and staging
        distributions.
        :returns: UpdateDistributionWithStagingConfigResult
        :raises AccessDenied:
        :raises TooManyDistributionsAssociatedToOriginAccessControl:
        :raises InvalidDefaultRootObject:
        :raises InvalidQueryStringParameters:
        :raises TooManyTrustedSigners:
        :raises TooManyCookieNamesInWhiteList:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises InvalidErrorCode:
        :raises TooManyFunctionAssociations:
        :raises TooManyOriginCustomHeaders:
        :raises InvalidForwardCookies:
        :raises InvalidMinimumProtocolVersion:
        :raises NoSuchCachePolicy:
        :raises TooManyKeyGroupsAssociatedToDistribution:
        :raises TooManyDistributionsAssociatedToCachePolicy:
        :raises InvalidRequiredProtocol:
        :raises TooManyDistributionsWithFunctionAssociations:
        :raises TooManyOriginGroupsPerDistribution:
        :raises InvalidTTLOrder:
        :raises IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior:
        :raises InvalidOriginKeepaliveTimeout:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidOriginReadTimeout:
        :raises InvalidOriginAccessControl:
        :raises EntityNotFound:
        :raises InvalidHeadersForS3Origin:
        :raises TrustedSignerDoesNotExist:
        :raises InvalidWebACLId:
        :raises TooManyDistributionsWithSingleFunctionARN:
        :raises InvalidRelativePath:
        :raises TooManyLambdaFunctionAssociations:
        :raises NoSuchDistribution:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyDistributionsAssociatedToFieldLevelEncryptionConfig:
        :raises InconsistentQuantities:
        :raises InvalidLocationCode:
        :raises InvalidOriginAccessIdentity:
        :raises TooManyDistributionCNAMEs:
        :raises InvalidIfMatchVersion:
        :raises TooManyDistributionsAssociatedToOriginRequestPolicy:
        :raises TooManyQueryStringParameters:
        :raises PreconditionFailed:
        :raises RealtimeLogConfigOwnerMismatch:
        :raises MissingBody:
        :raises TooManyHeadersInForwardedValues:
        :raises InvalidLambdaFunctionAssociation:
        :raises CNAMEAlreadyExists:
        :raises TooManyCertificates:
        :raises TooManyDistributionsAssociatedToResponseHeadersPolicy:
        :raises TrustedKeyGroupDoesNotExist:
        :raises NoSuchResponseHeadersPolicy:
        :raises InvalidResponseCode:
        :raises NoSuchRealtimeLogConfig:
        :raises InvalidGeoRestrictionParameter:
        :raises InvalidViewerCertificate:
        :raises TooManyOrigins:
        :raises InvalidFunctionAssociation:
        :raises TooManyDistributionsWithLambdaAssociations:
        :raises TooManyDistributionsAssociatedToKeyGroup:
        :raises NoSuchOrigin:
        :raises TooManyCacheBehaviors:
        """
        raise NotImplementedError

    @handler("UpdateDomainAssociation")
    def update_domain_association(
        self,
        context: RequestContext,
        domain: string,
        target_resource: DistributionResourceId,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateDomainAssociationResult:
        """Moves a domain from its current distribution or distribution tenant to
        another one.

        :param domain: The domain to update.
        :param target_resource: The target distribution resource for the domain.
        :param if_match: The value of the ``ETag`` identifier for the distribution or
        distribution tenant that will be associated with the domain.
        :returns: UpdateDomainAssociationResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateFieldLevelEncryptionConfig")
    def update_field_level_encryption_config(
        self,
        context: RequestContext,
        field_level_encryption_config: FieldLevelEncryptionConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateFieldLevelEncryptionConfigResult:
        """Update a field-level encryption configuration.

        :param field_level_encryption_config: Request to update a field-level encryption configuration.
        :param id: The ID of the configuration you want to update.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        configuration identity to update.
        :returns: UpdateFieldLevelEncryptionConfigResult
        :raises PreconditionFailed:
        :raises QueryArgProfileEmpty:
        :raises AccessDenied:
        :raises NoSuchFieldLevelEncryptionConfig:
        :raises TooManyFieldLevelEncryptionContentTypeProfiles:
        :raises TooManyFieldLevelEncryptionQueryArgProfiles:
        :raises InconsistentQuantities:
        :raises NoSuchFieldLevelEncryptionProfile:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateFieldLevelEncryptionProfile")
    def update_field_level_encryption_profile(
        self,
        context: RequestContext,
        field_level_encryption_profile_config: FieldLevelEncryptionProfileConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateFieldLevelEncryptionProfileResult:
        """Update a field-level encryption profile.

        :param field_level_encryption_profile_config: Request to update a field-level encryption profile.
        :param id: The ID of the field-level encryption profile request.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        profile identity to update.
        :returns: UpdateFieldLevelEncryptionProfileResult
        :raises PreconditionFailed:
        :raises TooManyFieldLevelEncryptionFieldPatterns:
        :raises AccessDenied:
        :raises FieldLevelEncryptionProfileAlreadyExists:
        :raises NoSuchPublicKey:
        :raises FieldLevelEncryptionProfileSizeExceeded:
        :raises InconsistentQuantities:
        :raises NoSuchFieldLevelEncryptionProfile:
        :raises TooManyFieldLevelEncryptionEncryptionEntities:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateFunction")
    def update_function(
        self,
        context: RequestContext,
        name: string,
        if_match: string,
        function_config: FunctionConfig,
        function_code: FunctionBlob,
        **kwargs,
    ) -> UpdateFunctionResult:
        """Updates a CloudFront function.

        You can update a function's code or the comment that describes the
        function. You cannot update a function's name.

        To update a function, you provide the function's name and version
        (``ETag`` value) along with the updated function code. To get the name
        and version, you can use ``ListFunctions`` and ``DescribeFunction``.

        :param name: The name of the function that you are updating.
        :param if_match: The current version (``ETag`` value) of the function that you are
        updating, which you can get using ``DescribeFunction``.
        :param function_config: Configuration information about the function.
        :param function_code: The function code.
        :returns: UpdateFunctionResult
        :raises PreconditionFailed:
        :raises UnsupportedOperation:
        :raises FunctionSizeLimitExceeded:
        :raises InvalidArgument:
        :raises NoSuchFunctionExists:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateKeyGroup")
    def update_key_group(
        self,
        context: RequestContext,
        key_group_config: KeyGroupConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateKeyGroupResult:
        """Updates a key group.

        When you update a key group, all the fields are updated with the values
        provided in the request. You cannot update some fields independent of
        others. To update a key group:

        #. Get the current key group with ``GetKeyGroup`` or
           ``GetKeyGroupConfig``.

        #. Locally modify the fields in the key group that you want to update.
           For example, add or remove public key IDs.

        #. Call ``UpdateKeyGroup`` with the entire key group object, including
           the fields that you modified and those that you didn't.

        :param key_group_config: The key group configuration.
        :param id: The identifier of the key group that you are updating.
        :param if_match: The version of the key group that you are updating.
        :returns: UpdateKeyGroupResult
        :raises PreconditionFailed:
        :raises TooManyPublicKeysInKeyGroup:
        :raises InvalidArgument:
        :raises NoSuchResource:
        :raises InvalidIfMatchVersion:
        :raises KeyGroupAlreadyExists:
        """
        raise NotImplementedError

    @handler("UpdateKeyValueStore")
    def update_key_value_store(
        self,
        context: RequestContext,
        name: KeyValueStoreName,
        comment: KeyValueStoreComment,
        if_match: string,
        **kwargs,
    ) -> UpdateKeyValueStoreResult:
        """Specifies the key value store to update.

        :param name: The name of the key value store to update.
        :param comment: The comment of the key value store to update.
        :param if_match: The key value store to update, if a match occurs.
        :returns: UpdateKeyValueStoreResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateOriginAccessControl")
    def update_origin_access_control(
        self,
        context: RequestContext,
        origin_access_control_config: OriginAccessControlConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateOriginAccessControlResult:
        """Updates a CloudFront origin access control.

        :param origin_access_control_config: An origin access control.
        :param id: The unique identifier of the origin access control that you are
        updating.
        :param if_match: The current version (``ETag`` value) of the origin access control that
        you are updating.
        :returns: UpdateOriginAccessControlResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises OriginAccessControlAlreadyExists:
        :raises NoSuchOriginAccessControl:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateOriginRequestPolicy")
    def update_origin_request_policy(
        self,
        context: RequestContext,
        origin_request_policy_config: OriginRequestPolicyConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateOriginRequestPolicyResult:
        """Updates an origin request policy configuration.

        When you update an origin request policy configuration, all the fields
        are updated with the values provided in the request. You cannot update
        some fields independent of others. To update an origin request policy
        configuration:

        #. Use ``GetOriginRequestPolicyConfig`` to get the current
           configuration.

        #. Locally modify the fields in the origin request policy configuration
           that you want to update.

        #. Call ``UpdateOriginRequestPolicy`` by providing the entire origin
           request policy configuration, including the fields that you modified
           and those that you didn't.

        :param origin_request_policy_config: An origin request policy configuration.
        :param id: The unique identifier for the origin request policy that you are
        updating.
        :param if_match: The version of the origin request policy that you are updating.
        :returns: UpdateOriginRequestPolicyResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises TooManyHeadersInOriginRequestPolicy:
        :raises NoSuchOriginRequestPolicy:
        :raises TooManyCookiesInOriginRequestPolicy:
        :raises InconsistentQuantities:
        :raises OriginRequestPolicyAlreadyExists:
        :raises TooManyQueryStringsInOriginRequestPolicy:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdatePublicKey")
    def update_public_key(
        self,
        context: RequestContext,
        public_key_config: PublicKeyConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdatePublicKeyResult:
        """Update public key information. Note that the only value you can change
        is the comment.

        :param public_key_config: A public key configuration.
        :param id: The identifier of the public key that you are updating.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        public key to update.
        :returns: UpdatePublicKeyResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises NoSuchPublicKey:
        :raises CannotChangeImmutablePublicKeyFields:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateRealtimeLogConfig")
    def update_realtime_log_config(
        self,
        context: RequestContext,
        end_points: EndPointList | None = None,
        fields: FieldList | None = None,
        name: string | None = None,
        arn: string | None = None,
        sampling_rate: long | None = None,
        **kwargs,
    ) -> UpdateRealtimeLogConfigResult:
        """Updates a real-time log configuration.

        When you update a real-time log configuration, all the parameters are
        updated with the values provided in the request. You cannot update some
        parameters independent of others. To update a real-time log
        configuration:

        #. Call ``GetRealtimeLogConfig`` to get the current real-time log
           configuration.

        #. Locally modify the parameters in the real-time log configuration that
           you want to update.

        #. Call this API (``UpdateRealtimeLogConfig``) by providing the entire
           real-time log configuration, including the parameters that you
           modified and those that you didn't.

        You cannot update a real-time log configuration's ``Name`` or ``ARN``.

        :param end_points: Contains information about the Amazon Kinesis data stream where you are
        sending real-time log data.
        :param fields: A list of fields to include in each real-time log record.
        :param name: The name for this real-time log configuration.
        :param arn: The Amazon Resource Name (ARN) for this real-time log configuration.
        :param sampling_rate: The sampling rate for this real-time log configuration.
        :returns: UpdateRealtimeLogConfigResult
        :raises AccessDenied:
        :raises InvalidArgument:
        :raises NoSuchRealtimeLogConfig:
        """
        raise NotImplementedError

    @handler("UpdateResponseHeadersPolicy")
    def update_response_headers_policy(
        self,
        context: RequestContext,
        response_headers_policy_config: ResponseHeadersPolicyConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateResponseHeadersPolicyResult:
        """Updates a response headers policy.

        When you update a response headers policy, the entire policy is
        replaced. You cannot update some policy fields independent of others. To
        update a response headers policy configuration:

        #. Use ``GetResponseHeadersPolicyConfig`` to get the current policy's
           configuration.

        #. Modify the fields in the response headers policy configuration that
           you want to update.

        #. Call ``UpdateResponseHeadersPolicy``, providing the entire response
           headers policy configuration, including the fields that you modified
           and those that you didn't.

        :param response_headers_policy_config: A response headers policy configuration.
        :param id: The identifier for the response headers policy that you are updating.
        :param if_match: The version of the response headers policy that you are updating.
        :returns: UpdateResponseHeadersPolicyResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises TooManyCustomHeadersInResponseHeadersPolicy:
        :raises ResponseHeadersPolicyAlreadyExists:
        :raises InconsistentQuantities:
        :raises NoSuchResponseHeadersPolicy:
        :raises TooLongCSPInResponseHeadersPolicy:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises TooManyRemoveHeadersInResponseHeadersPolicy:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("UpdateStreamingDistribution")
    def update_streaming_distribution(
        self,
        context: RequestContext,
        streaming_distribution_config: StreamingDistributionConfig,
        id: string,
        if_match: string | None = None,
        **kwargs,
    ) -> UpdateStreamingDistributionResult:
        """Update a streaming distribution.

        :param streaming_distribution_config: The streaming distribution's configuration information.
        :param id: The streaming distribution's id.
        :param if_match: The value of the ``ETag`` header that you received when retrieving the
        streaming distribution's configuration.
        :returns: UpdateStreamingDistributionResult
        :raises AccessDenied:
        :raises InconsistentQuantities:
        :raises InvalidOriginAccessIdentity:
        :raises InvalidArgument:
        :raises IllegalUpdate:
        :raises TooManyTrustedSigners:
        :raises InvalidOriginAccessControl:
        :raises InvalidIfMatchVersion:
        :raises PreconditionFailed:
        :raises MissingBody:
        :raises TooManyStreamingDistributionCNAMEs:
        :raises TrustedSignerDoesNotExist:
        :raises CNAMEAlreadyExists:
        :raises NoSuchStreamingDistribution:
        """
        raise NotImplementedError

    @handler("UpdateVpcOrigin")
    def update_vpc_origin(
        self,
        context: RequestContext,
        vpc_origin_endpoint_config: VpcOriginEndpointConfig,
        id: string,
        if_match: string,
        **kwargs,
    ) -> UpdateVpcOriginResult:
        """Update an Amazon CloudFront VPC origin in your account.

        :param vpc_origin_endpoint_config: The VPC origin endpoint configuration.
        :param id: The VPC origin ID.
        :param if_match: The VPC origin to update, if a match occurs.
        :returns: UpdateVpcOriginResult
        :raises PreconditionFailed:
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises UnsupportedOperation:
        :raises EntityAlreadyExists:
        :raises InconsistentQuantities:
        :raises CannotUpdateEntityWhileInUse:
        :raises EntityLimitExceeded:
        :raises IllegalUpdate:
        :raises InvalidArgument:
        :raises InvalidIfMatchVersion:
        """
        raise NotImplementedError

    @handler("VerifyDnsConfiguration")
    def verify_dns_configuration(
        self, context: RequestContext, identifier: string, domain: string | None = None, **kwargs
    ) -> VerifyDnsConfigurationResult:
        """Verify the DNS configuration for your domain names. This API operation
        checks whether your domain name points to the correct routing endpoint
        of the connection group, such as d111111abcdef8.cloudfront.net. You can
        use this API operation to troubleshoot and resolve DNS configuration
        issues.

        :param identifier: The identifier of the distribution tenant.
        :param domain: The domain name that you're verifying.
        :returns: VerifyDnsConfigurationResult
        :raises AccessDenied:
        :raises EntityNotFound:
        :raises InvalidArgument:
        """
        raise NotImplementedError
