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

__all__ = [
    'GetTransactionSearchConfigResult',
    'AwaitableGetTransactionSearchConfigResult',
    'get_transaction_search_config',
    'get_transaction_search_config_output',
]

@pulumi.output_type
class GetTransactionSearchConfigResult:
    def __init__(__self__, account_id=None, indexing_percentage=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if indexing_percentage and not isinstance(indexing_percentage, float):
            raise TypeError("Expected argument 'indexing_percentage' to be a float")
        pulumi.set(__self__, "indexing_percentage", indexing_percentage)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="indexingPercentage")
    def indexing_percentage(self) -> Optional[builtins.float]:
        return pulumi.get(self, "indexing_percentage")


class AwaitableGetTransactionSearchConfigResult(GetTransactionSearchConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransactionSearchConfigResult(
            account_id=self.account_id,
            indexing_percentage=self.indexing_percentage)


def get_transaction_search_config(account_id: Optional[builtins.str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransactionSearchConfigResult:
    """
    This schema provides construct and validation rules for AWS-XRay TransactionSearchConfig resource parameters.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:xray:getTransactionSearchConfig', __args__, opts=opts, typ=GetTransactionSearchConfigResult).value

    return AwaitableGetTransactionSearchConfigResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        indexing_percentage=pulumi.get(__ret__, 'indexing_percentage'))
def get_transaction_search_config_output(account_id: Optional[pulumi.Input[builtins.str]] = None,
                                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetTransactionSearchConfigResult]:
    """
    This schema provides construct and validation rules for AWS-XRay TransactionSearchConfig resource parameters.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('aws-native:xray:getTransactionSearchConfig', __args__, opts=opts, typ=GetTransactionSearchConfigResult)
    return __ret__.apply(lambda __response__: GetTransactionSearchConfigResult(
        account_id=pulumi.get(__response__, 'account_id'),
        indexing_percentage=pulumi.get(__response__, 'indexing_percentage')))
