r'''
# `aws_vpc_peering_connection`

Refer to the Terraform Registry for docs: [`aws_vpc_peering_connection`](https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection).
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


class VpcPeeringConnection(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnection",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection aws_vpc_peering_connection}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        peer_vpc_id: builtins.str,
        vpc_id: builtins.str,
        accepter: typing.Optional[typing.Union["VpcPeeringConnectionAccepter", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        peer_owner_id: typing.Optional[builtins.str] = None,
        peer_region: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionRequester", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpcPeeringConnectionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection aws_vpc_peering_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param peer_vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_vpc_id VpcPeeringConnection#peer_vpc_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#vpc_id VpcPeeringConnection#vpc_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#accepter VpcPeeringConnection#accepter}
        :param auto_accept: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#auto_accept VpcPeeringConnection#auto_accept}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#id VpcPeeringConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param peer_owner_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_owner_id VpcPeeringConnection#peer_owner_id}.
        :param peer_region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_region VpcPeeringConnection#peer_region}.
        :param requester: requester block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#requester VpcPeeringConnection#requester}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags VpcPeeringConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags_all VpcPeeringConnection#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#timeouts VpcPeeringConnection#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b3e9b5399f79091e3069ff9ef2de205533a0c8431f1458533f12d355fcfb28f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpcPeeringConnectionConfig(
            peer_vpc_id=peer_vpc_id,
            vpc_id=vpc_id,
            accepter=accepter,
            auto_accept=auto_accept,
            id=id,
            peer_owner_id=peer_owner_id,
            peer_region=peer_region,
            requester=requester,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
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
        '''Generates CDKTF code for importing a VpcPeeringConnection resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the VpcPeeringConnection to import.
        :param import_from_id: The id of the existing VpcPeeringConnection that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the VpcPeeringConnection to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f7aa549029fd2b799c1264a8f5c2f704bc9b2e786bebb0cdd8b0d7713efeaa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAccepter")
    def put_accepter(
        self,
        *,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.
        '''
        value = VpcPeeringConnectionAccepter(
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution
        )

        return typing.cast(None, jsii.invoke(self, "putAccepter", [value]))

    @jsii.member(jsii_name="putRequester")
    def put_requester(
        self,
        *,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.
        '''
        value = VpcPeeringConnectionRequester(
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution
        )

        return typing.cast(None, jsii.invoke(self, "putRequester", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#create VpcPeeringConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#delete VpcPeeringConnection#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#update VpcPeeringConnection#update}.
        '''
        value = VpcPeeringConnectionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccepter")
    def reset_accepter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccepter", []))

    @jsii.member(jsii_name="resetAutoAccept")
    def reset_auto_accept(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAccept", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPeerOwnerId")
    def reset_peer_owner_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerOwnerId", []))

    @jsii.member(jsii_name="resetPeerRegion")
    def reset_peer_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerRegion", []))

    @jsii.member(jsii_name="resetRequester")
    def reset_requester(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequester", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="accepter")
    def accepter(self) -> "VpcPeeringConnectionAccepterOutputReference":
        return typing.cast("VpcPeeringConnectionAccepterOutputReference", jsii.get(self, "accepter"))

    @builtins.property
    @jsii.member(jsii_name="acceptStatus")
    def accept_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceptStatus"))

    @builtins.property
    @jsii.member(jsii_name="requester")
    def requester(self) -> "VpcPeeringConnectionRequesterOutputReference":
        return typing.cast("VpcPeeringConnectionRequesterOutputReference", jsii.get(self, "requester"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VpcPeeringConnectionTimeoutsOutputReference":
        return typing.cast("VpcPeeringConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accepterInput")
    def accepter_input(self) -> typing.Optional["VpcPeeringConnectionAccepter"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionAccepter"], jsii.get(self, "accepterInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAcceptInput")
    def auto_accept_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAcceptInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="peerOwnerIdInput")
    def peer_owner_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerOwnerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="peerRegionInput")
    def peer_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="peerVpcIdInput")
    def peer_vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requesterInput")
    def requester_input(self) -> typing.Optional["VpcPeeringConnectionRequester"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionRequester"], jsii.get(self, "requesterInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "VpcPeeringConnectionTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "VpcPeeringConnectionTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAccept")
    def auto_accept(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAccept"))

    @auto_accept.setter
    def auto_accept(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac44dc469b37d3e3dc0eefda24d382092154563e16c218dc19246067c78d2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAccept", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94fb799803b30f1aa6df98f2caa29b644c80ff4e0d94477d6a9742fa8a4b8b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerOwnerId")
    def peer_owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerOwnerId"))

    @peer_owner_id.setter
    def peer_owner_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e8d3d9cfa68a13e63adb8acb274a1ee8ca0fa6ed8a4c933c2a4a0d55bd6231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerOwnerId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerRegion")
    def peer_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerRegion"))

    @peer_region.setter
    def peer_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d303684b969f0a0aadd43cc3ef60d6a1ee1184845c19f830965a31877a74095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVpcId"))

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a32f104e227f40cd59ae557c1800df7207555fd37826b5a4e81a31e69d3f51c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9dd7dd199f670d467a9757355f19f6133918ea211b8d4e64931ba2b34e61db8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c81234b9305108673db5e5a1a2deefe654e97edd91021ad88576542dd2baa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff7930dd2e9ede9f6d878e745436279c98175cfd4488e2c67f1bd29726437e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionAccepter",
    jsii_struct_bases=[],
    name_mapping={"allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution"},
)
class VpcPeeringConnectionAccepter:
    def __init__(
        self,
        *,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__311101396883c7d8bb39672229f62f158f62fe94712e30fb1c70b5a629d84d71)
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionAccepter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionAccepterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionAccepterOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a26ecce1df40cac53216ef447d1d89ff0529257c578bf793c6ddf0b0e3c6ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586adc092ee8c44f8e23add85db5ae6a8fd1801a189a636c70d05107ec12eaf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionAccepter]:
        return typing.cast(typing.Optional[VpcPeeringConnectionAccepter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionAccepter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe7f4239dcef6f43809adf1e7e97732562a8aba6425ba2bbe2f5362ba2b581b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "peer_vpc_id": "peerVpcId",
        "vpc_id": "vpcId",
        "accepter": "accepter",
        "auto_accept": "autoAccept",
        "id": "id",
        "peer_owner_id": "peerOwnerId",
        "peer_region": "peerRegion",
        "requester": "requester",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class VpcPeeringConnectionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        peer_vpc_id: builtins.str,
        vpc_id: builtins.str,
        accepter: typing.Optional[typing.Union[VpcPeeringConnectionAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        peer_owner_id: typing.Optional[builtins.str] = None,
        peer_region: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionRequester", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpcPeeringConnectionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param peer_vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_vpc_id VpcPeeringConnection#peer_vpc_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#vpc_id VpcPeeringConnection#vpc_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#accepter VpcPeeringConnection#accepter}
        :param auto_accept: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#auto_accept VpcPeeringConnection#auto_accept}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#id VpcPeeringConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param peer_owner_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_owner_id VpcPeeringConnection#peer_owner_id}.
        :param peer_region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_region VpcPeeringConnection#peer_region}.
        :param requester: requester block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#requester VpcPeeringConnection#requester}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags VpcPeeringConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags_all VpcPeeringConnection#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#timeouts VpcPeeringConnection#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(accepter, dict):
            accepter = VpcPeeringConnectionAccepter(**accepter)
        if isinstance(requester, dict):
            requester = VpcPeeringConnectionRequester(**requester)
        if isinstance(timeouts, dict):
            timeouts = VpcPeeringConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0a10519566feaa062037fb51d1f571f252b6d754b983064ce56c843799e90d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument peer_vpc_id", value=peer_vpc_id, expected_type=type_hints["peer_vpc_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument accepter", value=accepter, expected_type=type_hints["accepter"])
            check_type(argname="argument auto_accept", value=auto_accept, expected_type=type_hints["auto_accept"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument peer_owner_id", value=peer_owner_id, expected_type=type_hints["peer_owner_id"])
            check_type(argname="argument peer_region", value=peer_region, expected_type=type_hints["peer_region"])
            check_type(argname="argument requester", value=requester, expected_type=type_hints["requester"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "peer_vpc_id": peer_vpc_id,
            "vpc_id": vpc_id,
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
        if accepter is not None:
            self._values["accepter"] = accepter
        if auto_accept is not None:
            self._values["auto_accept"] = auto_accept
        if id is not None:
            self._values["id"] = id
        if peer_owner_id is not None:
            self._values["peer_owner_id"] = peer_owner_id
        if peer_region is not None:
            self._values["peer_region"] = peer_region
        if requester is not None:
            self._values["requester"] = requester
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def peer_vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_vpc_id VpcPeeringConnection#peer_vpc_id}.'''
        result = self._values.get("peer_vpc_id")
        assert result is not None, "Required property 'peer_vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#vpc_id VpcPeeringConnection#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter(self) -> typing.Optional[VpcPeeringConnectionAccepter]:
        '''accepter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#accepter VpcPeeringConnection#accepter}
        '''
        result = self._values.get("accepter")
        return typing.cast(typing.Optional[VpcPeeringConnectionAccepter], result)

    @builtins.property
    def auto_accept(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#auto_accept VpcPeeringConnection#auto_accept}.'''
        result = self._values.get("auto_accept")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#id VpcPeeringConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_owner_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_owner_id VpcPeeringConnection#peer_owner_id}.'''
        result = self._values.get("peer_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#peer_region VpcPeeringConnection#peer_region}.'''
        result = self._values.get("peer_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requester(self) -> typing.Optional["VpcPeeringConnectionRequester"]:
        '''requester block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#requester VpcPeeringConnection#requester}
        '''
        result = self._values.get("requester")
        return typing.cast(typing.Optional["VpcPeeringConnectionRequester"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags VpcPeeringConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#tags_all VpcPeeringConnection#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VpcPeeringConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#timeouts VpcPeeringConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VpcPeeringConnectionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionRequester",
    jsii_struct_bases=[],
    name_mapping={"allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution"},
)
class VpcPeeringConnectionRequester:
    def __init__(
        self,
        *,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b285f6732a019b3ef6715c4da81716ca5e48aba3b5ac47855afa257e198716a4)
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#allow_remote_vpc_dns_resolution VpcPeeringConnection#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionRequester(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionRequesterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionRequesterOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87816d62067813956809ba5c144457f7962fab9617fb655b25a93ac1e6f3c11f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe883c24effe6ae82d3e291205ec77f0356ef2dcecabf1e838a0809cab606cfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionRequester]:
        return typing.cast(typing.Optional[VpcPeeringConnectionRequester], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionRequester],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__780a4af7d02040f249a5289236c82be9634ff15a570ba772e65444985366eb0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class VpcPeeringConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#create VpcPeeringConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#delete VpcPeeringConnection#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#update VpcPeeringConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300028b5e0144b97a05861264292ae0908dcf08a426ffc278dd526d675e88da7)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#create VpcPeeringConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#delete VpcPeeringConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.100.0/docs/resources/vpc_peering_connection#update VpcPeeringConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnection.VpcPeeringConnectionTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbbc58a8ccd5a04ec5a57a76089113d6da5c316b7a53679c62dd2c1754ed3dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09f7398b48e11f75bfe466a06e1360a083c2600c8240f990a466d356f4acf26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55453936864cc30819f644cf92f5e523ec4d5c7917cc16a0afdd3319f884643b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcaa78fc7ef19a4450886f3c7ddf5dfead4988a412d823675128ff9b931766e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, VpcPeeringConnectionTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, VpcPeeringConnectionTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, VpcPeeringConnectionTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b3a060f819318f8f8fb85e4373f3b28176bb24fcfdab04af6305864e0ccc31b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "VpcPeeringConnection",
    "VpcPeeringConnectionAccepter",
    "VpcPeeringConnectionAccepterOutputReference",
    "VpcPeeringConnectionConfig",
    "VpcPeeringConnectionRequester",
    "VpcPeeringConnectionRequesterOutputReference",
    "VpcPeeringConnectionTimeouts",
    "VpcPeeringConnectionTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__3b3e9b5399f79091e3069ff9ef2de205533a0c8431f1458533f12d355fcfb28f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    peer_vpc_id: builtins.str,
    vpc_id: builtins.str,
    accepter: typing.Optional[typing.Union[VpcPeeringConnectionAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    peer_owner_id: typing.Optional[builtins.str] = None,
    peer_region: typing.Optional[builtins.str] = None,
    requester: typing.Optional[typing.Union[VpcPeeringConnectionRequester, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VpcPeeringConnectionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__45f7aa549029fd2b799c1264a8f5c2f704bc9b2e786bebb0cdd8b0d7713efeaa(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac44dc469b37d3e3dc0eefda24d382092154563e16c218dc19246067c78d2ce(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94fb799803b30f1aa6df98f2caa29b644c80ff4e0d94477d6a9742fa8a4b8b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e8d3d9cfa68a13e63adb8acb274a1ee8ca0fa6ed8a4c933c2a4a0d55bd6231(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d303684b969f0a0aadd43cc3ef60d6a1ee1184845c19f830965a31877a74095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32f104e227f40cd59ae557c1800df7207555fd37826b5a4e81a31e69d3f51c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9dd7dd199f670d467a9757355f19f6133918ea211b8d4e64931ba2b34e61db8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c81234b9305108673db5e5a1a2deefe654e97edd91021ad88576542dd2baa3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7930dd2e9ede9f6d878e745436279c98175cfd4488e2c67f1bd29726437e8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__311101396883c7d8bb39672229f62f158f62fe94712e30fb1c70b5a629d84d71(
    *,
    allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a26ecce1df40cac53216ef447d1d89ff0529257c578bf793c6ddf0b0e3c6ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586adc092ee8c44f8e23add85db5ae6a8fd1801a189a636c70d05107ec12eaf8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe7f4239dcef6f43809adf1e7e97732562a8aba6425ba2bbe2f5362ba2b581b8(
    value: typing.Optional[VpcPeeringConnectionAccepter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0a10519566feaa062037fb51d1f571f252b6d754b983064ce56c843799e90d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    peer_vpc_id: builtins.str,
    vpc_id: builtins.str,
    accepter: typing.Optional[typing.Union[VpcPeeringConnectionAccepter, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_accept: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    peer_owner_id: typing.Optional[builtins.str] = None,
    peer_region: typing.Optional[builtins.str] = None,
    requester: typing.Optional[typing.Union[VpcPeeringConnectionRequester, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VpcPeeringConnectionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b285f6732a019b3ef6715c4da81716ca5e48aba3b5ac47855afa257e198716a4(
    *,
    allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87816d62067813956809ba5c144457f7962fab9617fb655b25a93ac1e6f3c11f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe883c24effe6ae82d3e291205ec77f0356ef2dcecabf1e838a0809cab606cfb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__780a4af7d02040f249a5289236c82be9634ff15a570ba772e65444985366eb0e(
    value: typing.Optional[VpcPeeringConnectionRequester],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300028b5e0144b97a05861264292ae0908dcf08a426ffc278dd526d675e88da7(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbbc58a8ccd5a04ec5a57a76089113d6da5c316b7a53679c62dd2c1754ed3dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d09f7398b48e11f75bfe466a06e1360a083c2600c8240f990a466d356f4acf26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55453936864cc30819f644cf92f5e523ec4d5c7917cc16a0afdd3319f884643b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcaa78fc7ef19a4450886f3c7ddf5dfead4988a412d823675128ff9b931766e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3a060f819318f8f8fb85e4373f3b28176bb24fcfdab04af6305864e0ccc31b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, VpcPeeringConnectionTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
