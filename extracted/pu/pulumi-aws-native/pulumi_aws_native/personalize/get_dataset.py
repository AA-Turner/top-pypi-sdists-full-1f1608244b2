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
    'GetDatasetResult',
    'AwaitableGetDatasetResult',
    'get_dataset',
    'get_dataset_output',
]

@pulumi.output_type
class GetDatasetResult:
    def __init__(__self__, dataset_arn=None, dataset_import_job=None):
        if dataset_arn and not isinstance(dataset_arn, str):
            raise TypeError("Expected argument 'dataset_arn' to be a str")
        pulumi.set(__self__, "dataset_arn", dataset_arn)
        if dataset_import_job and not isinstance(dataset_import_job, dict):
            raise TypeError("Expected argument 'dataset_import_job' to be a dict")
        pulumi.set(__self__, "dataset_import_job", dataset_import_job)

    @property
    @pulumi.getter(name="datasetArn")
    def dataset_arn(self) -> Optional[builtins.str]:
        """
        The ARN of the dataset
        """
        return pulumi.get(self, "dataset_arn")

    @property
    @pulumi.getter(name="datasetImportJob")
    def dataset_import_job(self) -> Optional['outputs.DatasetImportJob']:
        """
        Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset. If you specify a dataset import job as part of a dataset, all dataset import job fields are required.
        """
        return pulumi.get(self, "dataset_import_job")


class AwaitableGetDatasetResult(GetDatasetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetResult(
            dataset_arn=self.dataset_arn,
            dataset_import_job=self.dataset_import_job)


def get_dataset(dataset_arn: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetResult:
    """
    Resource schema for AWS::Personalize::Dataset.


    :param builtins.str dataset_arn: The ARN of the dataset
    """
    __args__ = dict()
    __args__['datasetArn'] = dataset_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:personalize:getDataset', __args__, opts=opts, typ=GetDatasetResult).value

    return AwaitableGetDatasetResult(
        dataset_arn=pulumi.get(__ret__, 'dataset_arn'),
        dataset_import_job=pulumi.get(__ret__, 'dataset_import_job'))
def get_dataset_output(dataset_arn: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDatasetResult]:
    """
    Resource schema for AWS::Personalize::Dataset.


    :param builtins.str dataset_arn: The ARN of the dataset
    """
    __args__ = dict()
    __args__['datasetArn'] = dataset_arn
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:personalize:getDataset', __args__, opts=opts, typ=GetDatasetResult)
    return __ret__.apply(lambda __response__: GetDatasetResult(
        dataset_arn=pulumi.get(__response__, 'dataset_arn'),
        dataset_import_job=pulumi.get(__response__, 'dataset_import_job')))
