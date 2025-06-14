r'''
# `tfe_team_token`

Refer to the Terraform Registry for docs: [`tfe_team_token`](https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token).
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


class TeamToken(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.teamToken.TeamToken",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token tfe_team_token}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        team_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expired_at: typing.Optional[builtins.str] = None,
        force_regenerate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token tfe_team_token} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param team_id: ID of the team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#team_id TeamToken#team_id}
        :param description: The description of the token, which must be unique per team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#description TeamToken#description}
        :param expired_at: The token's expiration date. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#expired_at TeamToken#expired_at}
        :param force_regenerate: When set to true will force the audit trail token to be recreated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#force_regenerate TeamToken#force_regenerate}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb30beab6b46ce916234883cbade92cc916e5bc0334be5bdecfc45b01b47a37e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = TeamTokenConfig(
            team_id=team_id,
            description=description,
            expired_at=expired_at,
            force_regenerate=force_regenerate,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a TeamToken resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the TeamToken to import.
        :param import_from_id: The id of the existing TeamToken that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the TeamToken to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9e214b8cb44f7b78068e8040c4b352281d77b1a974409496ca791b1d42bed9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExpiredAt")
    def reset_expired_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiredAt", []))

    @jsii.member(jsii_name="resetForceRegenerate")
    def reset_force_regenerate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRegenerate", []))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expiredAtInput")
    def expired_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiredAtInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRegenerateInput")
    def force_regenerate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceRegenerateInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8315caaff3774cf9a25d2841ba9258a57c803c3f90400db9f60396e6547c00b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expiredAt")
    def expired_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiredAt"))

    @expired_at.setter
    def expired_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d6eadd6410945f5ecac54ed3c1550e7ac8a49b7f2ded17be97e8f8a66f9c43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiredAt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="forceRegenerate")
    def force_regenerate(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceRegenerate"))

    @force_regenerate.setter
    def force_regenerate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06257573c942f56f4109bcecdf3ca8bb222cb9b36123b01c3d6541704b87077a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRegenerate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12902629cc614e3d881b1ae8f5869710dc1c70972f18645305a7aa9860a3e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.teamToken.TeamTokenConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "team_id": "teamId",
        "description": "description",
        "expired_at": "expiredAt",
        "force_regenerate": "forceRegenerate",
    },
)
class TeamTokenConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        team_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expired_at: typing.Optional[builtins.str] = None,
        force_regenerate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param team_id: ID of the team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#team_id TeamToken#team_id}
        :param description: The description of the token, which must be unique per team. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#description TeamToken#description}
        :param expired_at: The token's expiration date. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#expired_at TeamToken#expired_at}
        :param force_regenerate: When set to true will force the audit trail token to be recreated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#force_regenerate TeamToken#force_regenerate}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5819d6b01e765a40e2d126f5334f47277b339f12680c9bc4af58330100e3db92)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expired_at", value=expired_at, expected_type=type_hints["expired_at"])
            check_type(argname="argument force_regenerate", value=force_regenerate, expected_type=type_hints["force_regenerate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "team_id": team_id,
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
        if description is not None:
            self._values["description"] = description
        if expired_at is not None:
            self._values["expired_at"] = expired_at
        if force_regenerate is not None:
            self._values["force_regenerate"] = force_regenerate

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
    def team_id(self) -> builtins.str:
        '''ID of the team.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#team_id TeamToken#team_id}
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the token, which must be unique per team.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#description TeamToken#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expired_at(self) -> typing.Optional[builtins.str]:
        '''The token's expiration date.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#expired_at TeamToken#expired_at}
        '''
        result = self._values.get("expired_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_regenerate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When set to true will force the audit trail token to be recreated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/tfe/0.66.0/docs/resources/team_token#force_regenerate TeamToken#force_regenerate}
        '''
        result = self._values.get("force_regenerate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamTokenConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TeamToken",
    "TeamTokenConfig",
]

publication.publish()

def _typecheckingstub__fb30beab6b46ce916234883cbade92cc916e5bc0334be5bdecfc45b01b47a37e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    team_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    expired_at: typing.Optional[builtins.str] = None,
    force_regenerate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__7a9e214b8cb44f7b78068e8040c4b352281d77b1a974409496ca791b1d42bed9(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8315caaff3774cf9a25d2841ba9258a57c803c3f90400db9f60396e6547c00b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d6eadd6410945f5ecac54ed3c1550e7ac8a49b7f2ded17be97e8f8a66f9c43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06257573c942f56f4109bcecdf3ca8bb222cb9b36123b01c3d6541704b87077a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12902629cc614e3d881b1ae8f5869710dc1c70972f18645305a7aa9860a3e51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5819d6b01e765a40e2d126f5334f47277b339f12680c9bc4af58330100e3db92(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    team_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    expired_at: typing.Optional[builtins.str] = None,
    force_regenerate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
