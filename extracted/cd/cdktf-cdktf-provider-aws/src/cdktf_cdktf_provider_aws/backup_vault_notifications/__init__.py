r'''
# `aws_backup_vault_notifications`

Refer to the Terraform Registry for docs: [`aws_backup_vault_notifications`](https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications).
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

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class BackupVaultNotifications(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.backupVaultNotifications.BackupVaultNotifications",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications aws_backup_vault_notifications}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        backup_vault_events: typing.Sequence[builtins.str],
        backup_vault_name: builtins.str,
        sns_topic_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications aws_backup_vault_notifications} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backup_vault_events: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_events BackupVaultNotifications#backup_vault_events}.
        :param backup_vault_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_name BackupVaultNotifications#backup_vault_name}.
        :param sns_topic_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#sns_topic_arn BackupVaultNotifications#sns_topic_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#id BackupVaultNotifications#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3b3aeae89405d87db0829b4f80a66346b8580f48406fbd1ca55febba679fea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupVaultNotificationsConfig(
            backup_vault_events=backup_vault_events,
            backup_vault_name=backup_vault_name,
            sns_topic_arn=sns_topic_arn,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a BackupVaultNotifications resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the BackupVaultNotifications to import.
        :param import_from_id: The id of the existing BackupVaultNotifications that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the BackupVaultNotifications to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0d36b56d4ed51c3777584ffa1e1fa2c8b874fa22b0c41831744e01dfeabf0a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultEventsInput")
    def backup_vault_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "backupVaultEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultNameInput")
    def backup_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="snsTopicArnInput")
    def sns_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultEvents")
    def backup_vault_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "backupVaultEvents"))

    @backup_vault_events.setter
    def backup_vault_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78367f963c4bced262a16a56c71c618e4ce530c5fce90b7f142085156a6a9bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultEvents", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))

    @backup_vault_name.setter
    def backup_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf72428fc23bb58518652a6845053cd907bda77737709ae62ef359a24c3648d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99bf8fd618adca473abf32581375f7dfefdb8b255f9a6c7ca1f5dd328751c5c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0cf77778c05258743427d0d6611bc1cd97ea86323bcb9222e72175dcd08e170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.backupVaultNotifications.BackupVaultNotificationsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backup_vault_events": "backupVaultEvents",
        "backup_vault_name": "backupVaultName",
        "sns_topic_arn": "snsTopicArn",
        "id": "id",
    },
)
class BackupVaultNotificationsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        backup_vault_events: typing.Sequence[builtins.str],
        backup_vault_name: builtins.str,
        sns_topic_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backup_vault_events: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_events BackupVaultNotifications#backup_vault_events}.
        :param backup_vault_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_name BackupVaultNotifications#backup_vault_name}.
        :param sns_topic_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#sns_topic_arn BackupVaultNotifications#sns_topic_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#id BackupVaultNotifications#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5b8fb5748417c4443065adc91feba9f50f026d7dc32880e371504f289d998d3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backup_vault_events", value=backup_vault_events, expected_type=type_hints["backup_vault_events"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_vault_events": backup_vault_events,
            "backup_vault_name": backup_vault_name,
            "sns_topic_arn": sns_topic_arn,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def backup_vault_events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_events BackupVaultNotifications#backup_vault_events}.'''
        result = self._values.get("backup_vault_events")
        assert result is not None, "Required property 'backup_vault_events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def backup_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#backup_vault_name BackupVaultNotifications#backup_vault_name}.'''
        result = self._values.get("backup_vault_name")
        assert result is not None, "Required property 'backup_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#sns_topic_arn BackupVaultNotifications#sns_topic_arn}.'''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/backup_vault_notifications#id BackupVaultNotifications#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupVaultNotificationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BackupVaultNotifications",
    "BackupVaultNotificationsConfig",
]

publication.publish()

def _typecheckingstub__8f3b3aeae89405d87db0829b4f80a66346b8580f48406fbd1ca55febba679fea(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    backup_vault_events: typing.Sequence[builtins.str],
    backup_vault_name: builtins.str,
    sns_topic_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0d36b56d4ed51c3777584ffa1e1fa2c8b874fa22b0c41831744e01dfeabf0a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78367f963c4bced262a16a56c71c618e4ce530c5fce90b7f142085156a6a9bc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf72428fc23bb58518652a6845053cd907bda77737709ae62ef359a24c3648d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99bf8fd618adca473abf32581375f7dfefdb8b255f9a6c7ca1f5dd328751c5c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0cf77778c05258743427d0d6611bc1cd97ea86323bcb9222e72175dcd08e170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5b8fb5748417c4443065adc91feba9f50f026d7dc32880e371504f289d998d3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backup_vault_events: typing.Sequence[builtins.str],
    backup_vault_name: builtins.str,
    sns_topic_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
