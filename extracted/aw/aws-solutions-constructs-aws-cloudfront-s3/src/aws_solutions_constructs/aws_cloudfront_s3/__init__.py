r'''
# aws-cloudfront-s3 module

<!--BEGIN STABILITY BANNER-->---


![Stability: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_cloudfront_s3`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-cloudfront-s3`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.cloudfronts3`|

## Overview

This AWS Solutions Construct provisions an Amazon CloudFront Distribution that serves objects from an AWS S3 Bucket via an Origin Access Control (OAC).

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CloudFrontToS3 } from '@aws-solutions-constructs/aws-cloudfront-s3';

new CloudFrontToS3(this, 'test-cloudfront-s3', {});
```

Python

```python
from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3
from aws_cdk import Stack
from constructs import Construct

CloudFrontToS3(self, 'test-cloudfront-s3')
```

Java

```java
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.cloudfronts3.*;

new CloudFrontToS3(this, "test-cloudfront-s3", new CloudFrontToS3Props.Builder()
        .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|cloudFrontDistributionProps?|[`cloudfront.DistributionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.DistributionProps.html)|Optional user provided props to override the default props for CloudFront Distribution|
|insertHttpSecurityHeaders?|`boolean`|Optional user provided props to turn on/off the automatic injection of best practice HTTP security headers in all responses from CloudFront|
|responseHeadersPolicyProps?   | [`cloudfront.ResponseHeadersPolicyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.ResponseHeadersPolicyProps.html) | Optional user provided configuration that cloudfront applies to all http responses.|
|originPath?|`string`|Optional user provided props to provide an[originPath](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront_origins.S3OriginProps.html#originpath) that CloudFront appends to the origin domain name when CloudFront requests content from the origin. The string should start with a `/`, for example: `/production`. Default value is `'/'`|
|existingBucketObj?|[`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)|Existing instance of S3 content bucket object or interface. If this is provided, then also providing bucketProps will cause an error. |
|bucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the S3 content bucket. Note - to log S3 access for this bucket to an existing S3 bucket, put the existing log bucket in bucketProps: `serverAccessLogsBucket`|
|logS3AccessLogs?| boolean|Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true|
|loggingBucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the S3 Logging Bucket.|
|cloudFrontLoggingBucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the CloudFront Logging Bucket. Note: to use an existing bucketto  hold CloudFront logs, pass the existing log bucket in |
|logCloudFrontAccessLog|`boolean`|Optional - Whether to maintain access logs for the CloudFront Logging bucket. Specifying false for this while providing info about the log bucket will cause an error. Default = true |
|cloudFrontLoggingBucketAccessLogBucketProps|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the CloudFront Log Bucket Access Log bucket. Providing both this and `existingcloudFrontLoggingBucketAccessLogBucket` will cause an error. To provide an existing bucket to accept these logs, pass the existing bucket in `cloudFrontLoggingBucketProps::serverAccessLogBucket`|

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|cloudFrontWebDistribution|[`cloudfront.Distribution`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Distribution.html)|Returns an instance of cloudfront.Distribution created by the construct.|
|cloudFrontFunction?|[`cloudfront.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Function.html)|Returns an instance of the Cloudfront function created by the construct.|
|originAccessControl?|[`cloudfront.CfnOriginAccessControl`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.cloudfront.CfnOriginAccessControl.html)|Returns an instance of cloudfront.CfnOriginAccessControl created by the construct.|
|s3BucketInterface|[`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)|Returns an instance of s3.IBucket created by the construct.|
|s3Bucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of s3.Bucket created by the construct. IMPORTANT: If `existingBucketObj` was provided in Pattern Construct Props, this property will be `undefined`|
|s3LoggingBucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket.|
|cloudFrontLoggingBucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|The S3 bucket created by the construct to hold CloudFront logs. Only populated if the construct creates the bucket (not if an existing bucket is passed in via DistributionProps)|
|cloudFrontLoggingBucketAccessLogBucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|The S3 bucket containing the S3 access logs for the CloudFront log bucket. Only populated if the construct creates the bucket (not if the bucket is passed in via `cloudFrontLoggingBucketProps::serverAccessLogBucket`|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon CloudFront

* Configure Access logging for CloudFront Distribution
* Enable automatic injection of best practice HTTP security headers in all responses from CloudFront Distribution
* CloudFront originPath set to `'/'`
* Create an Origin Access Control to access S3 bucket

### Amazon S3 Bucket

* Configure Access logging for S3 Bucket
* Enable server-side encryption for S3 Bucket using AWS managed KMS Key
* Enforce encryption of data in transit
* Turn on the versioning for S3 Bucket
* Don't allow public access for S3 Bucket
* Retain the S3 Bucket when deleting the CloudFormation stack
* Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class CloudFrontToS3(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-cloudfront-s3.CloudFrontToS3",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_front_distribution_props: typing.Any = None,
        cloud_front_logging_bucket_access_log_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_front_logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        insert_http_security_headers: typing.Optional[builtins.bool] = None,
        log_cloud_front_access_log: typing.Optional[builtins.bool] = None,
        logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
        origin_path: typing.Optional[builtins.str] = None,
        response_headers_policy_props: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param bucket_props: Optional user provided props to override the default props for the S3 Content Bucket. Default: - Default props are used
        :param cloud_front_distribution_props: Optional user provided props to override the default props. Default: - Default props are used
        :param cloud_front_logging_bucket_access_log_bucket_props: Optional user provided props to override the default props for the CloudFront Log Bucket Access Log bucket. Providing both this and ``existingcloudFrontLoggingBucketAccessLogBucket`` will cause an error Default: - Default props are used
        :param cloud_front_logging_bucket_props: Optional user provided props to override the default props for the CloudFront Log Bucket. Default: - Default props are used
        :param existing_bucket_obj: Existing instance of S3 Content Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param insert_http_security_headers: Optional user provided props to turn on/off the automatic injection of best practice HTTP security headers in all responses from cloudfront. Turning this on will inject default headers and is mutually exclusive with passing custom security headers via the responseHeadersPolicyProps parameter. Default: - true
        :param log_cloud_front_access_log: Optional - Whether to maintain access logs for the CloudFront Logging bucket. Specifying false for this while providing info about the log bucket will cause an error. Default: - true
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Content Bucket Access Log Bucket. Default: - Default props are used
        :param log_s3_access_logs: Optional - Whether to maintain access logs for the S3 Content bucket. Default: - true
        :param origin_path: Optional user provided props to provide an originPath that CloudFront appends to the origin domain name when CloudFront requests content from the origin. The string should start with a ``/``, for example ``/production``. Default: = '/'
        :param response_headers_policy_props: Optional user provided configuration that cloudfront applies to all http responses. Can be used to pass a custom ResponseSecurityHeadersBehavior, ResponseCustomHeadersBehavior or ResponseHeadersCorsBehavior to the cloudfront distribution. Passing a custom ResponseSecurityHeadersBehavior is mutually exclusive with turning on the default security headers via ``insertHttpSecurityHeaders`` prop. Will throw an error if both ``insertHttpSecurityHeaders`` is set to ``true`` and ResponseSecurityHeadersBehavior is passed. Default: - undefined

        :access: public
        :since: 0.8.0
        :summary: Constructs a new instance of the CloudFrontToS3 class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d15f8a2b88f946a68b3ada628d7d8ccfce684f8b89a5c653f4f53f0c015b1284)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFrontToS3Props(
            bucket_props=bucket_props,
            cloud_front_distribution_props=cloud_front_distribution_props,
            cloud_front_logging_bucket_access_log_bucket_props=cloud_front_logging_bucket_access_log_bucket_props,
            cloud_front_logging_bucket_props=cloud_front_logging_bucket_props,
            existing_bucket_obj=existing_bucket_obj,
            insert_http_security_headers=insert_http_security_headers,
            log_cloud_front_access_log=log_cloud_front_access_log,
            logging_bucket_props=logging_bucket_props,
            log_s3_access_logs=log_s3_access_logs,
            origin_path=origin_path,
            response_headers_policy_props=response_headers_policy_props,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cloudFrontWebDistribution")
    def cloud_front_web_distribution(
        self,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.Distribution:
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.Distribution, jsii.get(self, "cloudFrontWebDistribution"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInterface")
    def s3_bucket_interface(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, jsii.get(self, "s3BucketInterface"))

    @builtins.property
    @jsii.member(jsii_name="cloudFrontFunction")
    def cloud_front_function(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.Function]:
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.Function], jsii.get(self, "cloudFrontFunction"))

    @builtins.property
    @jsii.member(jsii_name="cloudFrontLoggingBucket")
    def cloud_front_logging_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "cloudFrontLoggingBucket"))

    @builtins.property
    @jsii.member(jsii_name="cloudFrontLoggingBucketAccessLogBucket")
    def cloud_front_logging_bucket_access_log_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "cloudFrontLoggingBucketAccessLogBucket"))

    @builtins.property
    @jsii.member(jsii_name="originAccessControl")
    def origin_access_control(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CfnOriginAccessControl]:
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CfnOriginAccessControl], jsii.get(self, "originAccessControl"))

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "s3Bucket"))

    @builtins.property
    @jsii.member(jsii_name="s3LoggingBucket")
    def s3_logging_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "s3LoggingBucket"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-cloudfront-s3.CloudFrontToS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_props": "bucketProps",
        "cloud_front_distribution_props": "cloudFrontDistributionProps",
        "cloud_front_logging_bucket_access_log_bucket_props": "cloudFrontLoggingBucketAccessLogBucketProps",
        "cloud_front_logging_bucket_props": "cloudFrontLoggingBucketProps",
        "existing_bucket_obj": "existingBucketObj",
        "insert_http_security_headers": "insertHttpSecurityHeaders",
        "log_cloud_front_access_log": "logCloudFrontAccessLog",
        "logging_bucket_props": "loggingBucketProps",
        "log_s3_access_logs": "logS3AccessLogs",
        "origin_path": "originPath",
        "response_headers_policy_props": "responseHeadersPolicyProps",
    },
)
class CloudFrontToS3Props:
    def __init__(
        self,
        *,
        bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_front_distribution_props: typing.Any = None,
        cloud_front_logging_bucket_access_log_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_front_logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        insert_http_security_headers: typing.Optional[builtins.bool] = None,
        log_cloud_front_access_log: typing.Optional[builtins.bool] = None,
        logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
        origin_path: typing.Optional[builtins.str] = None,
        response_headers_policy_props: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_props: Optional user provided props to override the default props for the S3 Content Bucket. Default: - Default props are used
        :param cloud_front_distribution_props: Optional user provided props to override the default props. Default: - Default props are used
        :param cloud_front_logging_bucket_access_log_bucket_props: Optional user provided props to override the default props for the CloudFront Log Bucket Access Log bucket. Providing both this and ``existingcloudFrontLoggingBucketAccessLogBucket`` will cause an error Default: - Default props are used
        :param cloud_front_logging_bucket_props: Optional user provided props to override the default props for the CloudFront Log Bucket. Default: - Default props are used
        :param existing_bucket_obj: Existing instance of S3 Content Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param insert_http_security_headers: Optional user provided props to turn on/off the automatic injection of best practice HTTP security headers in all responses from cloudfront. Turning this on will inject default headers and is mutually exclusive with passing custom security headers via the responseHeadersPolicyProps parameter. Default: - true
        :param log_cloud_front_access_log: Optional - Whether to maintain access logs for the CloudFront Logging bucket. Specifying false for this while providing info about the log bucket will cause an error. Default: - true
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Content Bucket Access Log Bucket. Default: - Default props are used
        :param log_s3_access_logs: Optional - Whether to maintain access logs for the S3 Content bucket. Default: - true
        :param origin_path: Optional user provided props to provide an originPath that CloudFront appends to the origin domain name when CloudFront requests content from the origin. The string should start with a ``/``, for example ``/production``. Default: = '/'
        :param response_headers_policy_props: Optional user provided configuration that cloudfront applies to all http responses. Can be used to pass a custom ResponseSecurityHeadersBehavior, ResponseCustomHeadersBehavior or ResponseHeadersCorsBehavior to the cloudfront distribution. Passing a custom ResponseSecurityHeadersBehavior is mutually exclusive with turning on the default security headers via ``insertHttpSecurityHeaders`` prop. Will throw an error if both ``insertHttpSecurityHeaders`` is set to ``true`` and ResponseSecurityHeadersBehavior is passed. Default: - undefined

        :summary: The properties for the CloudFrontToS3 Construct
        '''
        if isinstance(bucket_props, dict):
            bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**bucket_props)
        if isinstance(cloud_front_logging_bucket_access_log_bucket_props, dict):
            cloud_front_logging_bucket_access_log_bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**cloud_front_logging_bucket_access_log_bucket_props)
        if isinstance(cloud_front_logging_bucket_props, dict):
            cloud_front_logging_bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**cloud_front_logging_bucket_props)
        if isinstance(logging_bucket_props, dict):
            logging_bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**logging_bucket_props)
        if isinstance(response_headers_policy_props, dict):
            response_headers_policy_props = _aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps(**response_headers_policy_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__705452aa48ee0cf2bee41d0c5a78911cd5a7da0555110af58b091f4ccb70b808)
            check_type(argname="argument bucket_props", value=bucket_props, expected_type=type_hints["bucket_props"])
            check_type(argname="argument cloud_front_distribution_props", value=cloud_front_distribution_props, expected_type=type_hints["cloud_front_distribution_props"])
            check_type(argname="argument cloud_front_logging_bucket_access_log_bucket_props", value=cloud_front_logging_bucket_access_log_bucket_props, expected_type=type_hints["cloud_front_logging_bucket_access_log_bucket_props"])
            check_type(argname="argument cloud_front_logging_bucket_props", value=cloud_front_logging_bucket_props, expected_type=type_hints["cloud_front_logging_bucket_props"])
            check_type(argname="argument existing_bucket_obj", value=existing_bucket_obj, expected_type=type_hints["existing_bucket_obj"])
            check_type(argname="argument insert_http_security_headers", value=insert_http_security_headers, expected_type=type_hints["insert_http_security_headers"])
            check_type(argname="argument log_cloud_front_access_log", value=log_cloud_front_access_log, expected_type=type_hints["log_cloud_front_access_log"])
            check_type(argname="argument logging_bucket_props", value=logging_bucket_props, expected_type=type_hints["logging_bucket_props"])
            check_type(argname="argument log_s3_access_logs", value=log_s3_access_logs, expected_type=type_hints["log_s3_access_logs"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument response_headers_policy_props", value=response_headers_policy_props, expected_type=type_hints["response_headers_policy_props"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_props is not None:
            self._values["bucket_props"] = bucket_props
        if cloud_front_distribution_props is not None:
            self._values["cloud_front_distribution_props"] = cloud_front_distribution_props
        if cloud_front_logging_bucket_access_log_bucket_props is not None:
            self._values["cloud_front_logging_bucket_access_log_bucket_props"] = cloud_front_logging_bucket_access_log_bucket_props
        if cloud_front_logging_bucket_props is not None:
            self._values["cloud_front_logging_bucket_props"] = cloud_front_logging_bucket_props
        if existing_bucket_obj is not None:
            self._values["existing_bucket_obj"] = existing_bucket_obj
        if insert_http_security_headers is not None:
            self._values["insert_http_security_headers"] = insert_http_security_headers
        if log_cloud_front_access_log is not None:
            self._values["log_cloud_front_access_log"] = log_cloud_front_access_log
        if logging_bucket_props is not None:
            self._values["logging_bucket_props"] = logging_bucket_props
        if log_s3_access_logs is not None:
            self._values["log_s3_access_logs"] = log_s3_access_logs
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if response_headers_policy_props is not None:
            self._values["response_headers_policy_props"] = response_headers_policy_props

    @builtins.property
    def bucket_props(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''Optional user provided props to override the default props for the S3 Content Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def cloud_front_distribution_props(self) -> typing.Any:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("cloud_front_distribution_props")
        return typing.cast(typing.Any, result)

    @builtins.property
    def cloud_front_logging_bucket_access_log_bucket_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''Optional user provided props to override the default props for the CloudFront Log Bucket Access Log bucket.

        Providing both this and ``existingcloudFrontLoggingBucketAccessLogBucket`` will cause an error

        :default: - Default props are used
        '''
        result = self._values.get("cloud_front_logging_bucket_access_log_bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def cloud_front_logging_bucket_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''Optional user provided props to override the default props for the CloudFront Log Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("cloud_front_logging_bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def existing_bucket_obj(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''Existing instance of S3 Content Bucket object, providing both this and ``bucketProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_bucket_obj")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def insert_http_security_headers(self) -> typing.Optional[builtins.bool]:
        '''Optional user provided props to turn on/off the automatic injection of best practice HTTP security headers in all responses from cloudfront.

        Turning this on will inject default headers and is mutually exclusive with passing custom security headers
        via the responseHeadersPolicyProps parameter.

        :default: - true
        '''
        result = self._values.get("insert_http_security_headers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def log_cloud_front_access_log(self) -> typing.Optional[builtins.bool]:
        '''Optional - Whether to maintain access logs for the CloudFront Logging bucket.

        Specifying false for this
        while providing info about the log bucket will cause an error.

        :default: - true
        '''
        result = self._values.get("log_cloud_front_access_log")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def logging_bucket_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''Optional user provided props to override the default props for the S3 Content Bucket Access Log Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("logging_bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def log_s3_access_logs(self) -> typing.Optional[builtins.bool]:
        '''Optional - Whether to maintain access logs for the S3 Content bucket.

        :default: - true
        '''
        result = self._values.get("log_s3_access_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''Optional user provided props to provide an originPath that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        The string should start with a ``/``, for example ``/production``.

        :default: = '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_headers_policy_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps]:
        '''Optional user provided configuration that cloudfront applies to all http responses.

        Can be used to pass a custom ResponseSecurityHeadersBehavior, ResponseCustomHeadersBehavior or
        ResponseHeadersCorsBehavior to the cloudfront distribution.

        Passing a custom ResponseSecurityHeadersBehavior is mutually exclusive with turning on the default security headers
        via ``insertHttpSecurityHeaders`` prop. Will throw an error if both ``insertHttpSecurityHeaders`` is set to ``true``
        and ResponseSecurityHeadersBehavior is passed.

        :default: - undefined
        '''
        result = self._values.get("response_headers_policy_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFrontToS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudFrontToS3",
    "CloudFrontToS3Props",
]

publication.publish()

def _typecheckingstub__d15f8a2b88f946a68b3ada628d7d8ccfce684f8b89a5c653f4f53f0c015b1284(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_front_distribution_props: typing.Any = None,
    cloud_front_logging_bucket_access_log_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_front_logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    insert_http_security_headers: typing.Optional[builtins.bool] = None,
    log_cloud_front_access_log: typing.Optional[builtins.bool] = None,
    logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_s3_access_logs: typing.Optional[builtins.bool] = None,
    origin_path: typing.Optional[builtins.str] = None,
    response_headers_policy_props: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__705452aa48ee0cf2bee41d0c5a78911cd5a7da0555110af58b091f4ccb70b808(
    *,
    bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_front_distribution_props: typing.Any = None,
    cloud_front_logging_bucket_access_log_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_front_logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    insert_http_security_headers: typing.Optional[builtins.bool] = None,
    log_cloud_front_access_log: typing.Optional[builtins.bool] = None,
    logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_s3_access_logs: typing.Optional[builtins.bool] = None,
    origin_path: typing.Optional[builtins.str] = None,
    response_headers_policy_props: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseHeadersPolicyProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
