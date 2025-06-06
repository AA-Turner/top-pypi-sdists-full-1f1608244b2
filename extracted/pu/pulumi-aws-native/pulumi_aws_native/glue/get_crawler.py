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

__all__ = [
    'GetCrawlerResult',
    'AwaitableGetCrawlerResult',
    'get_crawler',
    'get_crawler_output',
]

@pulumi.output_type
class GetCrawlerResult:
    def __init__(__self__, classifiers=None, configuration=None, crawler_security_configuration=None, database_name=None, description=None, lake_formation_configuration=None, recrawl_policy=None, role=None, schedule=None, schema_change_policy=None, table_prefix=None, tags=None, targets=None):
        if classifiers and not isinstance(classifiers, list):
            raise TypeError("Expected argument 'classifiers' to be a list")
        pulumi.set(__self__, "classifiers", classifiers)
        if configuration and not isinstance(configuration, str):
            raise TypeError("Expected argument 'configuration' to be a str")
        pulumi.set(__self__, "configuration", configuration)
        if crawler_security_configuration and not isinstance(crawler_security_configuration, str):
            raise TypeError("Expected argument 'crawler_security_configuration' to be a str")
        pulumi.set(__self__, "crawler_security_configuration", crawler_security_configuration)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if lake_formation_configuration and not isinstance(lake_formation_configuration, dict):
            raise TypeError("Expected argument 'lake_formation_configuration' to be a dict")
        pulumi.set(__self__, "lake_formation_configuration", lake_formation_configuration)
        if recrawl_policy and not isinstance(recrawl_policy, dict):
            raise TypeError("Expected argument 'recrawl_policy' to be a dict")
        pulumi.set(__self__, "recrawl_policy", recrawl_policy)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if schema_change_policy and not isinstance(schema_change_policy, dict):
            raise TypeError("Expected argument 'schema_change_policy' to be a dict")
        pulumi.set(__self__, "schema_change_policy", schema_change_policy)
        if table_prefix and not isinstance(table_prefix, str):
            raise TypeError("Expected argument 'table_prefix' to be a str")
        pulumi.set(__self__, "table_prefix", table_prefix)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if targets and not isinstance(targets, dict):
            raise TypeError("Expected argument 'targets' to be a dict")
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter
    def classifiers(self) -> Optional[Sequence[builtins.str]]:
        """
        A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.
        """
        return pulumi.get(self, "classifiers")

    @property
    @pulumi.getter
    def configuration(self) -> Optional[builtins.str]:
        """
        Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="crawlerSecurityConfiguration")
    def crawler_security_configuration(self) -> Optional[builtins.str]:
        """
        The name of the SecurityConfiguration structure to be used by this crawler.
        """
        return pulumi.get(self, "crawler_security_configuration")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[builtins.str]:
        """
        The name of the database in which the crawler's output is stored.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def description(self) -> Optional[builtins.str]:
        """
        A description of the crawler.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lakeFormationConfiguration")
    def lake_formation_configuration(self) -> Optional['outputs.CrawlerLakeFormationConfiguration']:
        """
        Specifies whether the crawler should use AWS Lake Formation credentials for the crawler instead of the IAM role credentials.
        """
        return pulumi.get(self, "lake_formation_configuration")

    @property
    @pulumi.getter(name="recrawlPolicy")
    def recrawl_policy(self) -> Optional['outputs.CrawlerRecrawlPolicy']:
        """
        A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.
        """
        return pulumi.get(self, "recrawl_policy")

    @property
    @pulumi.getter
    def role(self) -> Optional[builtins.str]:
        """
        The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.CrawlerSchedule']:
        """
        For scheduled crawlers, the schedule when the crawler runs.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="schemaChangePolicy")
    def schema_change_policy(self) -> Optional['outputs.CrawlerSchemaChangePolicy']:
        """
        The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The `SchemaChangePolicy` does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the `SchemaChangePolicy` on a crawler.

        The SchemaChangePolicy consists of two components, `UpdateBehavior` and `DeleteBehavior` .
        """
        return pulumi.get(self, "schema_change_policy")

    @property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[builtins.str]:
        """
        The prefix added to the names of tables that are created.
        """
        return pulumi.get(self, "table_prefix")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The tags to use with this crawler.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Crawler` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def targets(self) -> Optional['outputs.CrawlerTargets']:
        """
        A collection of targets to crawl.
        """
        return pulumi.get(self, "targets")


class AwaitableGetCrawlerResult(GetCrawlerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCrawlerResult(
            classifiers=self.classifiers,
            configuration=self.configuration,
            crawler_security_configuration=self.crawler_security_configuration,
            database_name=self.database_name,
            description=self.description,
            lake_formation_configuration=self.lake_formation_configuration,
            recrawl_policy=self.recrawl_policy,
            role=self.role,
            schedule=self.schedule,
            schema_change_policy=self.schema_change_policy,
            table_prefix=self.table_prefix,
            tags=self.tags,
            targets=self.targets)


def get_crawler(name: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCrawlerResult:
    """
    Resource Type definition for AWS::Glue::Crawler


    :param builtins.str name: The name of the crawler.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getCrawler', __args__, opts=opts, typ=GetCrawlerResult).value

    return AwaitableGetCrawlerResult(
        classifiers=pulumi.get(__ret__, 'classifiers'),
        configuration=pulumi.get(__ret__, 'configuration'),
        crawler_security_configuration=pulumi.get(__ret__, 'crawler_security_configuration'),
        database_name=pulumi.get(__ret__, 'database_name'),
        description=pulumi.get(__ret__, 'description'),
        lake_formation_configuration=pulumi.get(__ret__, 'lake_formation_configuration'),
        recrawl_policy=pulumi.get(__ret__, 'recrawl_policy'),
        role=pulumi.get(__ret__, 'role'),
        schedule=pulumi.get(__ret__, 'schedule'),
        schema_change_policy=pulumi.get(__ret__, 'schema_change_policy'),
        table_prefix=pulumi.get(__ret__, 'table_prefix'),
        tags=pulumi.get(__ret__, 'tags'),
        targets=pulumi.get(__ret__, 'targets'))
def get_crawler_output(name: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCrawlerResult]:
    """
    Resource Type definition for AWS::Glue::Crawler


    :param builtins.str name: The name of the crawler.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:glue:getCrawler', __args__, opts=opts, typ=GetCrawlerResult)
    return __ret__.apply(lambda __response__: GetCrawlerResult(
        classifiers=pulumi.get(__response__, 'classifiers'),
        configuration=pulumi.get(__response__, 'configuration'),
        crawler_security_configuration=pulumi.get(__response__, 'crawler_security_configuration'),
        database_name=pulumi.get(__response__, 'database_name'),
        description=pulumi.get(__response__, 'description'),
        lake_formation_configuration=pulumi.get(__response__, 'lake_formation_configuration'),
        recrawl_policy=pulumi.get(__response__, 'recrawl_policy'),
        role=pulumi.get(__response__, 'role'),
        schedule=pulumi.get(__response__, 'schedule'),
        schema_change_policy=pulumi.get(__response__, 'schema_change_policy'),
        table_prefix=pulumi.get(__response__, 'table_prefix'),
        tags=pulumi.get(__response__, 'tags'),
        targets=pulumi.get(__response__, 'targets')))
