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
    def __init__(__self__, arn=None, custom_document_enrichment_configuration=None, data_source_configuration=None, description=None, id=None, index_id=None, language_code=None, name=None, role_arn=None, schedule=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if custom_document_enrichment_configuration and not isinstance(custom_document_enrichment_configuration, dict):
            raise TypeError("Expected argument 'custom_document_enrichment_configuration' to be a dict")
        pulumi.set(__self__, "custom_document_enrichment_configuration", custom_document_enrichment_configuration)
        if data_source_configuration and not isinstance(data_source_configuration, dict):
            raise TypeError("Expected argument 'data_source_configuration' to be a dict")
        pulumi.set(__self__, "data_source_configuration", data_source_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if index_id and not isinstance(index_id, str):
            raise TypeError("Expected argument 'index_id' to be a str")
        pulumi.set(__self__, "index_id", index_id)
        if language_code and not isinstance(language_code, str):
            raise TypeError("Expected argument 'language_code' to be a str")
        pulumi.set(__self__, "language_code", language_code)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if schedule and not isinstance(schedule, str):
            raise TypeError("Expected argument 'schedule' to be a str")
        pulumi.set(__self__, "schedule", schedule)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of the data source. For example:

        `arn:aws:kendra:us-west-2:111122223333:index/335c3741-41df-46a6-b5d3-61f85b787884/data-source/b8cae438-6787-4091-8897-684a652bbb0a`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="customDocumentEnrichmentConfiguration")
    def custom_document_enrichment_configuration(self) -> Optional['outputs.DataSourceCustomDocumentEnrichmentConfiguration']:
        """
        Configuration information for altering document metadata and content during the document ingestion process.
        """
        return pulumi.get(self, "custom_document_enrichment_configuration")

    @property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> Optional['outputs.DataSourceConfiguration']:
        """
        Configuration information for an Amazon Kendra data source. The contents of the configuration depend on the type of data source. You can only specify one type of data source in the configuration.

        You can't specify the `Configuration` parameter when the `Type` parameter is set to `CUSTOM` .

        The `Configuration` parameter is required for all other data sources.
        """
        return pulumi.get(self, "data_source_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        A description for the data source connector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The identifier for the data source. For example:

        `b8cae438-6787-4091-8897-684a652bbb0a` .
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="indexId")
    def index_id(self) -> Optional[builtins.str]:
        """
        The identifier of the index you want to use with the data source connector.
        """
        return pulumi.get(self, "index_id")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[builtins.str]:
        """
        The code for a language. This shows a supported language for all documents in the data source. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html) .
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the data source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of a role with permission to access the data source.

        You can't specify the `RoleArn` parameter when the `Type` parameter is set to `CUSTOM` .

        The `RoleArn` parameter is required for all other data sources.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def schedule(self) -> Optional[builtins.str]:
        """
        Sets the frequency that Amazon Kendra checks the documents in your data source and updates the index. If you don't set a schedule, Amazon Kendra doesn't periodically update the index.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Tags for labeling the data source
        """
        return pulumi.get(self, "tags")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            arn=self.arn,
            custom_document_enrichment_configuration=self.custom_document_enrichment_configuration,
            data_source_configuration=self.data_source_configuration,
            description=self.description,
            id=self.id,
            index_id=self.index_id,
            language_code=self.language_code,
            name=self.name,
            role_arn=self.role_arn,
            schedule=self.schedule,
            tags=self.tags)


def get_data_source(id: Optional[builtins.str] = None,
                    index_id: Optional[builtins.str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Kendra DataSource


    :param builtins.str id: The identifier for the data source. For example:
           
           `b8cae438-6787-4091-8897-684a652bbb0a` .
    :param builtins.str index_id: The identifier of the index you want to use with the data source connector.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kendra:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        arn=pulumi.get(__ret__, 'arn'),
        custom_document_enrichment_configuration=pulumi.get(__ret__, 'custom_document_enrichment_configuration'),
        data_source_configuration=pulumi.get(__ret__, 'data_source_configuration'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        index_id=pulumi.get(__ret__, 'index_id'),
        language_code=pulumi.get(__ret__, 'language_code'),
        name=pulumi.get(__ret__, 'name'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        schedule=pulumi.get(__ret__, 'schedule'),
        tags=pulumi.get(__ret__, 'tags'))
def get_data_source_output(id: Optional[pulumi.Input[builtins.str]] = None,
                           index_id: Optional[pulumi.Input[builtins.str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDataSourceResult]:
    """
    Kendra DataSource


    :param builtins.str id: The identifier for the data source. For example:
           
           `b8cae438-6787-4091-8897-684a652bbb0a` .
    :param builtins.str index_id: The identifier of the index you want to use with the data source connector.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['indexId'] = index_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:kendra:getDataSource', __args__, opts=opts, typ=GetDataSourceResult)
    return __ret__.apply(lambda __response__: GetDataSourceResult(
        arn=pulumi.get(__response__, 'arn'),
        custom_document_enrichment_configuration=pulumi.get(__response__, 'custom_document_enrichment_configuration'),
        data_source_configuration=pulumi.get(__response__, 'data_source_configuration'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        index_id=pulumi.get(__response__, 'index_id'),
        language_code=pulumi.get(__response__, 'language_code'),
        name=pulumi.get(__response__, 'name'),
        role_arn=pulumi.get(__response__, 'role_arn'),
        schedule=pulumi.get(__response__, 'schedule'),
        tags=pulumi.get(__response__, 'tags')))
