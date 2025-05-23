# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetDataSourceResult',
    'AwaitableGetDataSourceResult',
    'get_data_source',
    'get_data_source_output',
]

@pulumi.output_type
class GetDataSourceResult:
    def __init__(__self__, configuration=None, created_at=None, data_source_arn=None, data_source_id=None, description=None, display_name=None, document_enrichment_configuration=None, media_extraction_configuration=None, role_arn=None, status=None, sync_schedule=None, tags=None, type=None, updated_at=None, vpc_configuration=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if data_source_arn and not isinstance(data_source_arn, str):
            raise TypeError("Expected argument 'data_source_arn' to be a str")
        pulumi.set(__self__, "data_source_arn", data_source_arn)
        if data_source_id and not isinstance(data_source_id, str):
            raise TypeError("Expected argument 'data_source_id' to be a str")
        pulumi.set(__self__, "data_source_id", data_source_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if document_enrichment_configuration and not isinstance(document_enrichment_configuration, dict):
            raise TypeError("Expected argument 'document_enrichment_configuration' to be a dict")
        pulumi.set(__self__, "document_enrichment_configuration", document_enrichment_configuration)
        if media_extraction_configuration and not isinstance(media_extraction_configuration, dict):
            raise TypeError("Expected argument 'media_extraction_configuration' to be a dict")
        pulumi.set(__self__, "media_extraction_configuration", media_extraction_configuration)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if sync_schedule and not isinstance(sync_schedule, str):
            raise TypeError("Expected argument 'sync_schedule' to be a str")
        pulumi.set(__self__, "sync_schedule", sync_schedule)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if vpc_configuration and not isinstance(vpc_configuration, dict):
            raise TypeError("Expected argument 'vpc_configuration' to be a dict")
        pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[Any]:
        """
        Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business . You must use the JSON or YAML schema provided by Amazon Q .

        The following links have the configuration properties and schemas for AWS CloudFormation for the following connectors:

        - [Amazon Simple Storage Service](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html)
        - [Amazon Q Web Crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html)

        Similarly, you can find configuration templates and properties for your specific data source using the following steps:

        - Navigate to the [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html) page in the Amazon Q Business User Guide, and select the data source connector of your choice.
        - Then, from that specific data source connector's page, choose the topic containing *Using AWS CloudFormation* to find the schemas for your data source connector, including configuration parameter descriptions and examples.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::QBusiness::DataSource` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        The Unix timestamp when the Amazon Q Business data source was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application.
        """
        return pulumi.get(self, "data_source_arn")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[builtins.str]:
        """
        The identifier of the Amazon Q Business data source.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        A description for the data source connector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[builtins.str]:
        """
        The name of the Amazon Q Business data source.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="documentEnrichmentConfiguration")
    def document_enrichment_configuration(self) -> Optional['outputs.DataSourceDocumentEnrichmentConfiguration']:
        """
        Provides the configuration information for altering document metadata and content during the document ingestion process.

        For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html) .
        """
        return pulumi.get(self, "document_enrichment_configuration")

    @property
    @pulumi.getter(name="mediaExtractionConfiguration")
    def media_extraction_configuration(self) -> Optional['outputs.DataSourceMediaExtractionConfiguration']:
        """
        The configuration for extracting information from media in documents.
        """
        return pulumi.get(self, "media_extraction_configuration")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def status(self) -> Optional['DataSourceStatus']:
        """
        The status of the Amazon Q Business data source.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="syncSchedule")
    def sync_schedule(self) -> Optional[builtins.str]:
        """
        Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index.

        Specify a `cron-` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the `Schedule` parameter when the `Type` parameter is set to `CUSTOM` . If you do, you receive a `ValidationException` exception.
        """
        return pulumi.get(self, "sync_schedule")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[builtins.str]:
        """
        The type of the Amazon Q Business data source.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[builtins.str]:
        """
        The Unix timestamp when the Amazon Q Business data source was last updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional['outputs.DataSourceVpcConfiguration']:
        """
        Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see [Using Amazon VPC with Amazon Q Business connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html) .
        """
        return pulumi.get(self, "vpc_configuration")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            configuration=self.configuration,
            created_at=self.created_at,
            data_source_arn=self.data_source_arn,
            data_source_id=self.data_source_id,
            description=self.description,
            display_name=self.display_name,
            document_enrichment_configuration=self.document_enrichment_configuration,
            media_extraction_configuration=self.media_extraction_configuration,
            role_arn=self.role_arn,
            status=self.status,
            sync_schedule=self.sync_schedule,
            tags=self.tags,
            type=self.type,
            updated_at=self.updated_at,
            vpc_configuration=self.vpc_configuration)


def get_data_source(application_id: Optional[builtins.str] = None,
                    data_source_id: Optional[builtins.str] = None,
                    index_id: Optional[builtins.str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Definition of AWS::QBusiness::DataSource Resource Type


    :param builtins.str application_id: The identifier of the Amazon Q Business application the data source will be attached to.
    :param builtins.str data_source_id: The identifier of the Amazon Q Business data source.
    :param builtins.str index_id: The identifier of the index the data source is attached to.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['dataSourceId'] = data_source_id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:qbusiness:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        configuration=pulumi.get(__ret__, 'configuration'),
        created_at=pulumi.get(__ret__, 'created_at'),
        data_source_arn=pulumi.get(__ret__, 'data_source_arn'),
        data_source_id=pulumi.get(__ret__, 'data_source_id'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        document_enrichment_configuration=pulumi.get(__ret__, 'document_enrichment_configuration'),
        media_extraction_configuration=pulumi.get(__ret__, 'media_extraction_configuration'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        status=pulumi.get(__ret__, 'status'),
        sync_schedule=pulumi.get(__ret__, 'sync_schedule'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        vpc_configuration=pulumi.get(__ret__, 'vpc_configuration'))
def get_data_source_output(application_id: Optional[pulumi.Input[builtins.str]] = None,
                           data_source_id: Optional[pulumi.Input[builtins.str]] = None,
                           index_id: Optional[pulumi.Input[builtins.str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDataSourceResult]:
    """
    Definition of AWS::QBusiness::DataSource Resource Type


    :param builtins.str application_id: The identifier of the Amazon Q Business application the data source will be attached to.
    :param builtins.str data_source_id: The identifier of the Amazon Q Business data source.
    :param builtins.str index_id: The identifier of the index the data source is attached to.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    __args__['dataSourceId'] = data_source_id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:qbusiness:getDataSource', __args__, opts=opts, typ=GetDataSourceResult)
    return __ret__.apply(lambda __response__: GetDataSourceResult(
        configuration=pulumi.get(__response__, 'configuration'),
        created_at=pulumi.get(__response__, 'created_at'),
        data_source_arn=pulumi.get(__response__, 'data_source_arn'),
        data_source_id=pulumi.get(__response__, 'data_source_id'),
        description=pulumi.get(__response__, 'description'),
        display_name=pulumi.get(__response__, 'display_name'),
        document_enrichment_configuration=pulumi.get(__response__, 'document_enrichment_configuration'),
        media_extraction_configuration=pulumi.get(__response__, 'media_extraction_configuration'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        status=pulumi.get(__response__, 'status'),
        sync_schedule=pulumi.get(__response__, 'sync_schedule'),
        tags=pulumi.get(__response__, 'tags'),
        type=pulumi.get(__response__, 'type'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        vpc_configuration=pulumi.get(__response__, 'vpc_configuration')))
