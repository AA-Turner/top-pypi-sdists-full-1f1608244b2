r'''
# `aws_fsx_openzfs_volume`

Refer to the Terraform Registry for docs: [`aws_fsx_openzfs_volume`](https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume).
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


class FsxOpenzfsVolume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolume",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume aws_fsx_openzfs_volume}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        parent_volume_id: builtins.str,
        copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        data_compression_type: typing.Optional[builtins.str] = None,
        delete_volume_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        nfs_exports: typing.Optional[typing.Union["FsxOpenzfsVolumeNfsExports", typing.Dict[builtins.str, typing.Any]]] = None,
        origin_snapshot: typing.Optional[typing.Union["FsxOpenzfsVolumeOriginSnapshot", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        record_size_kib: typing.Optional[jsii.Number] = None,
        storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
        storage_capacity_reservation_gib: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOpenzfsVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_and_group_quotas: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsVolumeUserAndGroupQuotas", typing.Dict[builtins.str, typing.Any]]]]] = None,
        volume_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume aws_fsx_openzfs_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#name FsxOpenzfsVolume#name}.
        :param parent_volume_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#parent_volume_id FsxOpenzfsVolume#parent_volume_id}.
        :param copy_tags_to_snapshots: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_tags_to_snapshots FsxOpenzfsVolume#copy_tags_to_snapshots}.
        :param data_compression_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#data_compression_type FsxOpenzfsVolume#data_compression_type}.
        :param delete_volume_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete_volume_options FsxOpenzfsVolume#delete_volume_options}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#id FsxOpenzfsVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param nfs_exports: nfs_exports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#nfs_exports FsxOpenzfsVolume#nfs_exports}
        :param origin_snapshot: origin_snapshot block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#origin_snapshot FsxOpenzfsVolume#origin_snapshot}
        :param read_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#read_only FsxOpenzfsVolume#read_only}.
        :param record_size_kib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#record_size_kib FsxOpenzfsVolume#record_size_kib}.
        :param storage_capacity_quota_gib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_quota_gib FsxOpenzfsVolume#storage_capacity_quota_gib}.
        :param storage_capacity_reservation_gib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_reservation_gib FsxOpenzfsVolume#storage_capacity_reservation_gib}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags FsxOpenzfsVolume#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags_all FsxOpenzfsVolume#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#timeouts FsxOpenzfsVolume#timeouts}
        :param user_and_group_quotas: user_and_group_quotas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#user_and_group_quotas FsxOpenzfsVolume#user_and_group_quotas}
        :param volume_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#volume_type FsxOpenzfsVolume#volume_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d252643a4247917897b535036c6a805da8bbfce19054da2b6a3b0e247253e70)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FsxOpenzfsVolumeConfig(
            name=name,
            parent_volume_id=parent_volume_id,
            copy_tags_to_snapshots=copy_tags_to_snapshots,
            data_compression_type=data_compression_type,
            delete_volume_options=delete_volume_options,
            id=id,
            nfs_exports=nfs_exports,
            origin_snapshot=origin_snapshot,
            read_only=read_only,
            record_size_kib=record_size_kib,
            storage_capacity_quota_gib=storage_capacity_quota_gib,
            storage_capacity_reservation_gib=storage_capacity_reservation_gib,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            user_and_group_quotas=user_and_group_quotas,
            volume_type=volume_type,
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
        '''Generates CDKTF code for importing a FsxOpenzfsVolume resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the FsxOpenzfsVolume to import.
        :param import_from_id: The id of the existing FsxOpenzfsVolume that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the FsxOpenzfsVolume to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe5d9a7351918e492234826d9ce084991416e778d6858bd4fd6284548841ccff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putNfsExports")
    def put_nfs_exports(
        self,
        *,
        client_configurations: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsVolumeNfsExportsClientConfigurations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param client_configurations: client_configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#client_configurations FsxOpenzfsVolume#client_configurations}
        '''
        value = FsxOpenzfsVolumeNfsExports(client_configurations=client_configurations)

        return typing.cast(None, jsii.invoke(self, "putNfsExports", [value]))

    @jsii.member(jsii_name="putOriginSnapshot")
    def put_origin_snapshot(
        self,
        *,
        copy_strategy: builtins.str,
        snapshot_arn: builtins.str,
    ) -> None:
        '''
        :param copy_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_strategy FsxOpenzfsVolume#copy_strategy}.
        :param snapshot_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#snapshot_arn FsxOpenzfsVolume#snapshot_arn}.
        '''
        value = FsxOpenzfsVolumeOriginSnapshot(
            copy_strategy=copy_strategy, snapshot_arn=snapshot_arn
        )

        return typing.cast(None, jsii.invoke(self, "putOriginSnapshot", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#create FsxOpenzfsVolume#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete FsxOpenzfsVolume#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#update FsxOpenzfsVolume#update}.
        '''
        value = FsxOpenzfsVolumeTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUserAndGroupQuotas")
    def put_user_and_group_quotas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsVolumeUserAndGroupQuotas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8521f83d6549f152dfe542641cf29b7560204e8f5449783a8bc621da18c699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUserAndGroupQuotas", [value]))

    @jsii.member(jsii_name="resetCopyTagsToSnapshots")
    def reset_copy_tags_to_snapshots(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToSnapshots", []))

    @jsii.member(jsii_name="resetDataCompressionType")
    def reset_data_compression_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataCompressionType", []))

    @jsii.member(jsii_name="resetDeleteVolumeOptions")
    def reset_delete_volume_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteVolumeOptions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNfsExports")
    def reset_nfs_exports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsExports", []))

    @jsii.member(jsii_name="resetOriginSnapshot")
    def reset_origin_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginSnapshot", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRecordSizeKib")
    def reset_record_size_kib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordSizeKib", []))

    @jsii.member(jsii_name="resetStorageCapacityQuotaGib")
    def reset_storage_capacity_quota_gib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCapacityQuotaGib", []))

    @jsii.member(jsii_name="resetStorageCapacityReservationGib")
    def reset_storage_capacity_reservation_gib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCapacityReservationGib", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserAndGroupQuotas")
    def reset_user_and_group_quotas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAndGroupQuotas", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="nfsExports")
    def nfs_exports(self) -> "FsxOpenzfsVolumeNfsExportsOutputReference":
        return typing.cast("FsxOpenzfsVolumeNfsExportsOutputReference", jsii.get(self, "nfsExports"))

    @builtins.property
    @jsii.member(jsii_name="originSnapshot")
    def origin_snapshot(self) -> "FsxOpenzfsVolumeOriginSnapshotOutputReference":
        return typing.cast("FsxOpenzfsVolumeOriginSnapshotOutputReference", jsii.get(self, "originSnapshot"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FsxOpenzfsVolumeTimeoutsOutputReference":
        return typing.cast("FsxOpenzfsVolumeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userAndGroupQuotas")
    def user_and_group_quotas(self) -> "FsxOpenzfsVolumeUserAndGroupQuotasList":
        return typing.cast("FsxOpenzfsVolumeUserAndGroupQuotasList", jsii.get(self, "userAndGroupQuotas"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshotsInput")
    def copy_tags_to_snapshots_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "copyTagsToSnapshotsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCompressionTypeInput")
    def data_compression_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataCompressionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteVolumeOptionsInput")
    def delete_volume_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deleteVolumeOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsExportsInput")
    def nfs_exports_input(self) -> typing.Optional["FsxOpenzfsVolumeNfsExports"]:
        return typing.cast(typing.Optional["FsxOpenzfsVolumeNfsExports"], jsii.get(self, "nfsExportsInput"))

    @builtins.property
    @jsii.member(jsii_name="originSnapshotInput")
    def origin_snapshot_input(
        self,
    ) -> typing.Optional["FsxOpenzfsVolumeOriginSnapshot"]:
        return typing.cast(typing.Optional["FsxOpenzfsVolumeOriginSnapshot"], jsii.get(self, "originSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="parentVolumeIdInput")
    def parent_volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentVolumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSizeKibInput")
    def record_size_kib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recordSizeKibInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGibInput")
    def storage_capacity_quota_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityQuotaGibInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityReservationGibInput")
    def storage_capacity_reservation_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityReservationGibInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "FsxOpenzfsVolumeTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "FsxOpenzfsVolumeTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userAndGroupQuotasInput")
    def user_and_group_quotas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeUserAndGroupQuotas"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeUserAndGroupQuotas"]]], jsii.get(self, "userAndGroupQuotasInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "copyTagsToSnapshots"))

    @copy_tags_to_snapshots.setter
    def copy_tags_to_snapshots(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__762938003fbe8e64eba9b4bd327dab69ec84cfe80c239d34685fc09000884449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToSnapshots", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataCompressionType")
    def data_compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataCompressionType"))

    @data_compression_type.setter
    def data_compression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9c2502f6ca8aac112b0825212da099dd5ec7991f8d886cd1c4bf1572b71271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataCompressionType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deleteVolumeOptions")
    def delete_volume_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deleteVolumeOptions"))

    @delete_volume_options.setter
    def delete_volume_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f3d63e1cecc2302e4f3c7eca2d7723fe5f6a80fd3fe0ef3b93fc39f134143e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteVolumeOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddab894b2aa1867dd415c699adca230ab6686c6cb9475cdccaa07c4fad6c14ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b389c38bed4d3a490ff17796ada08493645b1eaed51b44ae53b96185c7c04e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parentVolumeId")
    def parent_volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentVolumeId"))

    @parent_volume_id.setter
    def parent_volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1898e257e4c838dd7fb348d50aeac5f5cac52f85b6e14ae5bc972655b3b646b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentVolumeId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e70a678ca2f7bb7fed8764f1a68168a17eeab3eea700e264eaecb21242a27f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordSizeKib")
    def record_size_kib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "recordSizeKib"))

    @record_size_kib.setter
    def record_size_kib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c27866c5862ac6d52f2d94cb6f877da0fad805cbb1db50dcec04f7dd512bf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSizeKib", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityQuotaGib"))

    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f8dfe75211c467e6a6888a1980e6924c6f57530f219559178cffef46e87868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityQuotaGib", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCapacityReservationGib")
    def storage_capacity_reservation_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityReservationGib"))

    @storage_capacity_reservation_gib.setter
    def storage_capacity_reservation_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7fc26393fbe31f5aebeef4c2a8d883ec70900d6a4e98f67512d9f27747beed7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityReservationGib", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f50d7b2013e8c451dbcea4cf7e2df8552bdd003abb5e35bf9c171dac1674e59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e3ba73fbf7c0bb593be9f0e9bbc4a8e2ebf0a82806bd19fd942c194392f7e33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b239dd27d70b1766976b3bda0c198a9ba065a60e114b0c2524cbeab1256dcd34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "parent_volume_id": "parentVolumeId",
        "copy_tags_to_snapshots": "copyTagsToSnapshots",
        "data_compression_type": "dataCompressionType",
        "delete_volume_options": "deleteVolumeOptions",
        "id": "id",
        "nfs_exports": "nfsExports",
        "origin_snapshot": "originSnapshot",
        "read_only": "readOnly",
        "record_size_kib": "recordSizeKib",
        "storage_capacity_quota_gib": "storageCapacityQuotaGib",
        "storage_capacity_reservation_gib": "storageCapacityReservationGib",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "user_and_group_quotas": "userAndGroupQuotas",
        "volume_type": "volumeType",
    },
)
class FsxOpenzfsVolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        parent_volume_id: builtins.str,
        copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        data_compression_type: typing.Optional[builtins.str] = None,
        delete_volume_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        nfs_exports: typing.Optional[typing.Union["FsxOpenzfsVolumeNfsExports", typing.Dict[builtins.str, typing.Any]]] = None,
        origin_snapshot: typing.Optional[typing.Union["FsxOpenzfsVolumeOriginSnapshot", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        record_size_kib: typing.Optional[jsii.Number] = None,
        storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
        storage_capacity_reservation_gib: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOpenzfsVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        user_and_group_quotas: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsVolumeUserAndGroupQuotas", typing.Dict[builtins.str, typing.Any]]]]] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#name FsxOpenzfsVolume#name}.
        :param parent_volume_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#parent_volume_id FsxOpenzfsVolume#parent_volume_id}.
        :param copy_tags_to_snapshots: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_tags_to_snapshots FsxOpenzfsVolume#copy_tags_to_snapshots}.
        :param data_compression_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#data_compression_type FsxOpenzfsVolume#data_compression_type}.
        :param delete_volume_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete_volume_options FsxOpenzfsVolume#delete_volume_options}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#id FsxOpenzfsVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param nfs_exports: nfs_exports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#nfs_exports FsxOpenzfsVolume#nfs_exports}
        :param origin_snapshot: origin_snapshot block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#origin_snapshot FsxOpenzfsVolume#origin_snapshot}
        :param read_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#read_only FsxOpenzfsVolume#read_only}.
        :param record_size_kib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#record_size_kib FsxOpenzfsVolume#record_size_kib}.
        :param storage_capacity_quota_gib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_quota_gib FsxOpenzfsVolume#storage_capacity_quota_gib}.
        :param storage_capacity_reservation_gib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_reservation_gib FsxOpenzfsVolume#storage_capacity_reservation_gib}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags FsxOpenzfsVolume#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags_all FsxOpenzfsVolume#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#timeouts FsxOpenzfsVolume#timeouts}
        :param user_and_group_quotas: user_and_group_quotas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#user_and_group_quotas FsxOpenzfsVolume#user_and_group_quotas}
        :param volume_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#volume_type FsxOpenzfsVolume#volume_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(nfs_exports, dict):
            nfs_exports = FsxOpenzfsVolumeNfsExports(**nfs_exports)
        if isinstance(origin_snapshot, dict):
            origin_snapshot = FsxOpenzfsVolumeOriginSnapshot(**origin_snapshot)
        if isinstance(timeouts, dict):
            timeouts = FsxOpenzfsVolumeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c338bb1ca78983822495f586d29396e4a9d49f69c7df6662b8ee2f9d3d148e9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_volume_id", value=parent_volume_id, expected_type=type_hints["parent_volume_id"])
            check_type(argname="argument copy_tags_to_snapshots", value=copy_tags_to_snapshots, expected_type=type_hints["copy_tags_to_snapshots"])
            check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
            check_type(argname="argument delete_volume_options", value=delete_volume_options, expected_type=type_hints["delete_volume_options"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument nfs_exports", value=nfs_exports, expected_type=type_hints["nfs_exports"])
            check_type(argname="argument origin_snapshot", value=origin_snapshot, expected_type=type_hints["origin_snapshot"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument record_size_kib", value=record_size_kib, expected_type=type_hints["record_size_kib"])
            check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
            check_type(argname="argument storage_capacity_reservation_gib", value=storage_capacity_reservation_gib, expected_type=type_hints["storage_capacity_reservation_gib"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_and_group_quotas", value=user_and_group_quotas, expected_type=type_hints["user_and_group_quotas"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "parent_volume_id": parent_volume_id,
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
        if copy_tags_to_snapshots is not None:
            self._values["copy_tags_to_snapshots"] = copy_tags_to_snapshots
        if data_compression_type is not None:
            self._values["data_compression_type"] = data_compression_type
        if delete_volume_options is not None:
            self._values["delete_volume_options"] = delete_volume_options
        if id is not None:
            self._values["id"] = id
        if nfs_exports is not None:
            self._values["nfs_exports"] = nfs_exports
        if origin_snapshot is not None:
            self._values["origin_snapshot"] = origin_snapshot
        if read_only is not None:
            self._values["read_only"] = read_only
        if record_size_kib is not None:
            self._values["record_size_kib"] = record_size_kib
        if storage_capacity_quota_gib is not None:
            self._values["storage_capacity_quota_gib"] = storage_capacity_quota_gib
        if storage_capacity_reservation_gib is not None:
            self._values["storage_capacity_reservation_gib"] = storage_capacity_reservation_gib
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_and_group_quotas is not None:
            self._values["user_and_group_quotas"] = user_and_group_quotas
        if volume_type is not None:
            self._values["volume_type"] = volume_type

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#name FsxOpenzfsVolume#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_volume_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#parent_volume_id FsxOpenzfsVolume#parent_volume_id}.'''
        result = self._values.get("parent_volume_id")
        assert result is not None, "Required property 'parent_volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_tags_to_snapshots(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_tags_to_snapshots FsxOpenzfsVolume#copy_tags_to_snapshots}.'''
        result = self._values.get("copy_tags_to_snapshots")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def data_compression_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#data_compression_type FsxOpenzfsVolume#data_compression_type}.'''
        result = self._values.get("data_compression_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_volume_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete_volume_options FsxOpenzfsVolume#delete_volume_options}.'''
        result = self._values.get("delete_volume_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#id FsxOpenzfsVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nfs_exports(self) -> typing.Optional["FsxOpenzfsVolumeNfsExports"]:
        '''nfs_exports block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#nfs_exports FsxOpenzfsVolume#nfs_exports}
        '''
        result = self._values.get("nfs_exports")
        return typing.cast(typing.Optional["FsxOpenzfsVolumeNfsExports"], result)

    @builtins.property
    def origin_snapshot(self) -> typing.Optional["FsxOpenzfsVolumeOriginSnapshot"]:
        '''origin_snapshot block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#origin_snapshot FsxOpenzfsVolume#origin_snapshot}
        '''
        result = self._values.get("origin_snapshot")
        return typing.cast(typing.Optional["FsxOpenzfsVolumeOriginSnapshot"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#read_only FsxOpenzfsVolume#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def record_size_kib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#record_size_kib FsxOpenzfsVolume#record_size_kib}.'''
        result = self._values.get("record_size_kib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_capacity_quota_gib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_quota_gib FsxOpenzfsVolume#storage_capacity_quota_gib}.'''
        result = self._values.get("storage_capacity_quota_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_capacity_reservation_gib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_reservation_gib FsxOpenzfsVolume#storage_capacity_reservation_gib}.'''
        result = self._values.get("storage_capacity_reservation_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags FsxOpenzfsVolume#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#tags_all FsxOpenzfsVolume#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FsxOpenzfsVolumeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#timeouts FsxOpenzfsVolume#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FsxOpenzfsVolumeTimeouts"], result)

    @builtins.property
    def user_and_group_quotas(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeUserAndGroupQuotas"]]]:
        '''user_and_group_quotas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#user_and_group_quotas FsxOpenzfsVolume#user_and_group_quotas}
        '''
        result = self._values.get("user_and_group_quotas")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeUserAndGroupQuotas"]]], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#volume_type FsxOpenzfsVolume#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeNfsExports",
    jsii_struct_bases=[],
    name_mapping={"client_configurations": "clientConfigurations"},
)
class FsxOpenzfsVolumeNfsExports:
    def __init__(
        self,
        *,
        client_configurations: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsVolumeNfsExportsClientConfigurations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param client_configurations: client_configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#client_configurations FsxOpenzfsVolume#client_configurations}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d251151c6aa590c416ca09e45b6f6061181419b873b4dde01864838c95344e63)
            check_type(argname="argument client_configurations", value=client_configurations, expected_type=type_hints["client_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_configurations": client_configurations,
        }

    @builtins.property
    def client_configurations(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeNfsExportsClientConfigurations"]]:
        '''client_configurations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#client_configurations FsxOpenzfsVolume#client_configurations}
        '''
        result = self._values.get("client_configurations")
        assert result is not None, "Required property 'client_configurations' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["FsxOpenzfsVolumeNfsExportsClientConfigurations"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeNfsExports(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeNfsExportsClientConfigurations",
    jsii_struct_bases=[],
    name_mapping={"clients": "clients", "options": "options"},
)
class FsxOpenzfsVolumeNfsExportsClientConfigurations:
    def __init__(
        self,
        *,
        clients: builtins.str,
        options: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param clients: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#clients FsxOpenzfsVolume#clients}.
        :param options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#options FsxOpenzfsVolume#options}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd058d260203f77f8f071a0283f24d134da19c600080615ddb2ab1aac669eeac)
            check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "clients": clients,
            "options": options,
        }

    @builtins.property
    def clients(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#clients FsxOpenzfsVolume#clients}.'''
        result = self._values.get("clients")
        assert result is not None, "Required property 'clients' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#options FsxOpenzfsVolume#options}.'''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeNfsExportsClientConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsVolumeNfsExportsClientConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeNfsExportsClientConfigurationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e24a2e57f11481a8a088aa47bcac2589bedfb66dc8567b86b6d8bd7a5d25799)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOpenzfsVolumeNfsExportsClientConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16715d8e469549e304a899456dac40e880cd5d2a52f5c7260262ad4f5d5969ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOpenzfsVolumeNfsExportsClientConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4828572d71891023a899690ada45002991e107a753cdc945ed3570ed5a7dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b7479abe365e14cc988667d0950efec13a708b09617939cd9802f215be6022a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d168e9253ea1d0ff33d4a1d5765cca00f5b5330c60081836cb26ca9865b55b8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1e3eaa47ddebbdc0aa62582e0c1795672d98121c4003d2b4b0734828aa5a84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class FsxOpenzfsVolumeNfsExportsClientConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeNfsExportsClientConfigurationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5308b4665273bcf030e54c9b67d364c7bb0c01e39bebf3fe1bf5b1cc6584dcd7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientsInput")
    def clients_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientsInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clients")
    def clients(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clients"))

    @clients.setter
    def clients(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33314d70bf0a1a44ed7a2d6770adf6cb142e5d4c2dc3b088fab02ea9ea10a506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clients", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54400db3edec536ab0322fd733521f48beef9309c3d2cdcfd87dfd37a768a469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeNfsExportsClientConfigurations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeNfsExportsClientConfigurations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeNfsExportsClientConfigurations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abad6366c7c1b3947bcd1987b76b7ce30dae91051fc4b392f5c22faea20747aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class FsxOpenzfsVolumeNfsExportsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeNfsExportsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96f79484dd5a1c0bfe142b6fe10dcddb7a76639806e4fe33515ed11eabdc26ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientConfigurations")
    def put_client_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeNfsExportsClientConfigurations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8f58edec5412b6854c646c27977d7e76d97f4b336403dbe9278335c0b4172b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientConfigurations", [value]))

    @builtins.property
    @jsii.member(jsii_name="clientConfigurations")
    def client_configurations(
        self,
    ) -> FsxOpenzfsVolumeNfsExportsClientConfigurationsList:
        return typing.cast(FsxOpenzfsVolumeNfsExportsClientConfigurationsList, jsii.get(self, "clientConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigurationsInput")
    def client_configurations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]], jsii.get(self, "clientConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FsxOpenzfsVolumeNfsExports]:
        return typing.cast(typing.Optional[FsxOpenzfsVolumeNfsExports], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOpenzfsVolumeNfsExports],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ba5acd8752e721d9b410d8fb93fb9c1b99cf25def77a37cd0925a5f3fb1a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeOriginSnapshot",
    jsii_struct_bases=[],
    name_mapping={"copy_strategy": "copyStrategy", "snapshot_arn": "snapshotArn"},
)
class FsxOpenzfsVolumeOriginSnapshot:
    def __init__(
        self,
        *,
        copy_strategy: builtins.str,
        snapshot_arn: builtins.str,
    ) -> None:
        '''
        :param copy_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_strategy FsxOpenzfsVolume#copy_strategy}.
        :param snapshot_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#snapshot_arn FsxOpenzfsVolume#snapshot_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5df7d836cfac5883c0029cd7ee84d904e5dd9b89f72107a38198885a3126292)
            check_type(argname="argument copy_strategy", value=copy_strategy, expected_type=type_hints["copy_strategy"])
            check_type(argname="argument snapshot_arn", value=snapshot_arn, expected_type=type_hints["snapshot_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "copy_strategy": copy_strategy,
            "snapshot_arn": snapshot_arn,
        }

    @builtins.property
    def copy_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#copy_strategy FsxOpenzfsVolume#copy_strategy}.'''
        result = self._values.get("copy_strategy")
        assert result is not None, "Required property 'copy_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def snapshot_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#snapshot_arn FsxOpenzfsVolume#snapshot_arn}.'''
        result = self._values.get("snapshot_arn")
        assert result is not None, "Required property 'snapshot_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeOriginSnapshot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsVolumeOriginSnapshotOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeOriginSnapshotOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b82c2bd01cc4f3e2f227bbc7bfd6ca246303276977ba8fcdb3fa0091abcd7c4d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="copyStrategyInput")
    def copy_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copyStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotArnInput")
    def snapshot_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotArnInput"))

    @builtins.property
    @jsii.member(jsii_name="copyStrategy")
    def copy_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copyStrategy"))

    @copy_strategy.setter
    def copy_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcbec2b9e7bdd79f2fca5a9755b11281dcbf12b2e41d3c06d2e1fa790f111f67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotArn")
    def snapshot_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotArn"))

    @snapshot_arn.setter
    def snapshot_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48c25a78080247f2bf0963667d41719e686933ea1b99c358b296939897f8b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FsxOpenzfsVolumeOriginSnapshot]:
        return typing.cast(typing.Optional[FsxOpenzfsVolumeOriginSnapshot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOpenzfsVolumeOriginSnapshot],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0df7f33ab895d8a4d317008f3179dabad73f24456166ebb539beb3034c48ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class FsxOpenzfsVolumeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#create FsxOpenzfsVolume#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete FsxOpenzfsVolume#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#update FsxOpenzfsVolume#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a65132c29873ee5541a3b32589a1a5c18029a2d1211300c914672704d75793)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#create FsxOpenzfsVolume#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#delete FsxOpenzfsVolume#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#update FsxOpenzfsVolume#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsVolumeTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a393370166b1d0b545262ac07130f2339f2eff21ce36df52e4a61b4b181207ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa9fc4f9c8752032b3222a94e2c0f7dc24b0bc0d65697d61ccdf7a11b040e235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915fd8230e6f08120889e1cdab53006d92f5647246c0e14e9a9c90c30e2b4f96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be69c0cdbd31b8c7ac0b54b1eb4e74730c70a864404a14a89072f1fa7d2bb615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3600469920217d307dceac8361f0e58060074c7da36ab5533428111666a30a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeUserAndGroupQuotas",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "storage_capacity_quota_gib": "storageCapacityQuotaGib",
        "type": "type",
    },
)
class FsxOpenzfsVolumeUserAndGroupQuotas:
    def __init__(
        self,
        *,
        id: jsii.Number,
        storage_capacity_quota_gib: jsii.Number,
        type: builtins.str,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#id FsxOpenzfsVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_capacity_quota_gib: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_quota_gib FsxOpenzfsVolume#storage_capacity_quota_gib}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#type FsxOpenzfsVolume#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2886f7a2233af4184bfb78c41dd860444fa5bbc9bb9ff7ae101bf2ce774d31)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "storage_capacity_quota_gib": storage_capacity_quota_gib,
            "type": type,
        }

    @builtins.property
    def id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#id FsxOpenzfsVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_capacity_quota_gib(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#storage_capacity_quota_gib FsxOpenzfsVolume#storage_capacity_quota_gib}.'''
        result = self._values.get("storage_capacity_quota_gib")
        assert result is not None, "Required property 'storage_capacity_quota_gib' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.99.1/docs/resources/fsx_openzfs_volume#type FsxOpenzfsVolume#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsVolumeUserAndGroupQuotas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsVolumeUserAndGroupQuotasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeUserAndGroupQuotasList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d133e00b0e09d7d138d01eda51b5c8e1ba35251c2bdf8a547534a6fd60490dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FsxOpenzfsVolumeUserAndGroupQuotasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c17531a7bfc1ca9994ba6ecd68b613e1ce80ee666cc9626d2fbb4f57ebe7600)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOpenzfsVolumeUserAndGroupQuotasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb673027d93fc5c4895688d38b17efec10e6a5cb99148f28f86cb111005b806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2d5c627fa6a08ed0848a10e46c036754f8a4ee06f2323df6478d1a2ad7d8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ae15c15f464cf313115fc4a453350dbfc44e07db615a839fbdd9a37533855a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeUserAndGroupQuotas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeUserAndGroupQuotas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeUserAndGroupQuotas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4c69be61bc48ba2e8c312c633034095db9297f4ef90b312c1c05f91673da2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class FsxOpenzfsVolumeUserAndGroupQuotasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsVolume.FsxOpenzfsVolumeUserAndGroupQuotasOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__231f7b63cca7f9a2f423901f081417c669fb3b3b970462abd3c8d532807cfb5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGibInput")
    def storage_capacity_quota_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityQuotaGibInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de20202930bb13b6001686d805d48897b6d64547dcc890ea83f5abad06fb0e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityQuotaGib"))

    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81a2ba53b1e474be6a0cc2935f8ae7b5c6d4101c5fbab648028407947dce4167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityQuotaGib", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ffa0a1260cae85781f4c14f472a8d3f860b674d22646d675b3fe5ee713dad0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeUserAndGroupQuotas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeUserAndGroupQuotas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeUserAndGroupQuotas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e679b290b16ee45dbf6af424610030b4cf84ca156f9e4c821940c42ce77e6c6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "FsxOpenzfsVolume",
    "FsxOpenzfsVolumeConfig",
    "FsxOpenzfsVolumeNfsExports",
    "FsxOpenzfsVolumeNfsExportsClientConfigurations",
    "FsxOpenzfsVolumeNfsExportsClientConfigurationsList",
    "FsxOpenzfsVolumeNfsExportsClientConfigurationsOutputReference",
    "FsxOpenzfsVolumeNfsExportsOutputReference",
    "FsxOpenzfsVolumeOriginSnapshot",
    "FsxOpenzfsVolumeOriginSnapshotOutputReference",
    "FsxOpenzfsVolumeTimeouts",
    "FsxOpenzfsVolumeTimeoutsOutputReference",
    "FsxOpenzfsVolumeUserAndGroupQuotas",
    "FsxOpenzfsVolumeUserAndGroupQuotasList",
    "FsxOpenzfsVolumeUserAndGroupQuotasOutputReference",
]

publication.publish()

def _typecheckingstub__6d252643a4247917897b535036c6a805da8bbfce19054da2b6a3b0e247253e70(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    parent_volume_id: builtins.str,
    copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    data_compression_type: typing.Optional[builtins.str] = None,
    delete_volume_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    nfs_exports: typing.Optional[typing.Union[FsxOpenzfsVolumeNfsExports, typing.Dict[builtins.str, typing.Any]]] = None,
    origin_snapshot: typing.Optional[typing.Union[FsxOpenzfsVolumeOriginSnapshot, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    record_size_kib: typing.Optional[jsii.Number] = None,
    storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
    storage_capacity_reservation_gib: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxOpenzfsVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_and_group_quotas: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeUserAndGroupQuotas, typing.Dict[builtins.str, typing.Any]]]]] = None,
    volume_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__fe5d9a7351918e492234826d9ce084991416e778d6858bd4fd6284548841ccff(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8521f83d6549f152dfe542641cf29b7560204e8f5449783a8bc621da18c699(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeUserAndGroupQuotas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__762938003fbe8e64eba9b4bd327dab69ec84cfe80c239d34685fc09000884449(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9c2502f6ca8aac112b0825212da099dd5ec7991f8d886cd1c4bf1572b71271(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f3d63e1cecc2302e4f3c7eca2d7723fe5f6a80fd3fe0ef3b93fc39f134143e3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddab894b2aa1867dd415c699adca230ab6686c6cb9475cdccaa07c4fad6c14ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b389c38bed4d3a490ff17796ada08493645b1eaed51b44ae53b96185c7c04e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1898e257e4c838dd7fb348d50aeac5f5cac52f85b6e14ae5bc972655b3b646b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e70a678ca2f7bb7fed8764f1a68168a17eeab3eea700e264eaecb21242a27f0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c27866c5862ac6d52f2d94cb6f877da0fad805cbb1db50dcec04f7dd512bf7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f8dfe75211c467e6a6888a1980e6924c6f57530f219559178cffef46e87868(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7fc26393fbe31f5aebeef4c2a8d883ec70900d6a4e98f67512d9f27747beed7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f50d7b2013e8c451dbcea4cf7e2df8552bdd003abb5e35bf9c171dac1674e59(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e3ba73fbf7c0bb593be9f0e9bbc4a8e2ebf0a82806bd19fd942c194392f7e33(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b239dd27d70b1766976b3bda0c198a9ba065a60e114b0c2524cbeab1256dcd34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c338bb1ca78983822495f586d29396e4a9d49f69c7df6662b8ee2f9d3d148e9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    parent_volume_id: builtins.str,
    copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    data_compression_type: typing.Optional[builtins.str] = None,
    delete_volume_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    nfs_exports: typing.Optional[typing.Union[FsxOpenzfsVolumeNfsExports, typing.Dict[builtins.str, typing.Any]]] = None,
    origin_snapshot: typing.Optional[typing.Union[FsxOpenzfsVolumeOriginSnapshot, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    record_size_kib: typing.Optional[jsii.Number] = None,
    storage_capacity_quota_gib: typing.Optional[jsii.Number] = None,
    storage_capacity_reservation_gib: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[FsxOpenzfsVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    user_and_group_quotas: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeUserAndGroupQuotas, typing.Dict[builtins.str, typing.Any]]]]] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d251151c6aa590c416ca09e45b6f6061181419b873b4dde01864838c95344e63(
    *,
    client_configurations: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeNfsExportsClientConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd058d260203f77f8f071a0283f24d134da19c600080615ddb2ab1aac669eeac(
    *,
    clients: builtins.str,
    options: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e24a2e57f11481a8a088aa47bcac2589bedfb66dc8567b86b6d8bd7a5d25799(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16715d8e469549e304a899456dac40e880cd5d2a52f5c7260262ad4f5d5969ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4828572d71891023a899690ada45002991e107a753cdc945ed3570ed5a7dbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b7479abe365e14cc988667d0950efec13a708b09617939cd9802f215be6022a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d168e9253ea1d0ff33d4a1d5765cca00f5b5330c60081836cb26ca9865b55b8e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1e3eaa47ddebbdc0aa62582e0c1795672d98121c4003d2b4b0734828aa5a84(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeNfsExportsClientConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5308b4665273bcf030e54c9b67d364c7bb0c01e39bebf3fe1bf5b1cc6584dcd7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33314d70bf0a1a44ed7a2d6770adf6cb142e5d4c2dc3b088fab02ea9ea10a506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54400db3edec536ab0322fd733521f48beef9309c3d2cdcfd87dfd37a768a469(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abad6366c7c1b3947bcd1987b76b7ce30dae91051fc4b392f5c22faea20747aa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeNfsExportsClientConfigurations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f79484dd5a1c0bfe142b6fe10dcddb7a76639806e4fe33515ed11eabdc26ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8f58edec5412b6854c646c27977d7e76d97f4b336403dbe9278335c0b4172b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsVolumeNfsExportsClientConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ba5acd8752e721d9b410d8fb93fb9c1b99cf25def77a37cd0925a5f3fb1a96(
    value: typing.Optional[FsxOpenzfsVolumeNfsExports],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5df7d836cfac5883c0029cd7ee84d904e5dd9b89f72107a38198885a3126292(
    *,
    copy_strategy: builtins.str,
    snapshot_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82c2bd01cc4f3e2f227bbc7bfd6ca246303276977ba8fcdb3fa0091abcd7c4d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcbec2b9e7bdd79f2fca5a9755b11281dcbf12b2e41d3c06d2e1fa790f111f67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48c25a78080247f2bf0963667d41719e686933ea1b99c358b296939897f8b05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0df7f33ab895d8a4d317008f3179dabad73f24456166ebb539beb3034c48ed3(
    value: typing.Optional[FsxOpenzfsVolumeOriginSnapshot],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a65132c29873ee5541a3b32589a1a5c18029a2d1211300c914672704d75793(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a393370166b1d0b545262ac07130f2339f2eff21ce36df52e4a61b4b181207ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9fc4f9c8752032b3222a94e2c0f7dc24b0bc0d65697d61ccdf7a11b040e235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915fd8230e6f08120889e1cdab53006d92f5647246c0e14e9a9c90c30e2b4f96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be69c0cdbd31b8c7ac0b54b1eb4e74730c70a864404a14a89072f1fa7d2bb615(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3600469920217d307dceac8361f0e58060074c7da36ab5533428111666a30a90(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeTimeouts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2886f7a2233af4184bfb78c41dd860444fa5bbc9bb9ff7ae101bf2ce774d31(
    *,
    id: jsii.Number,
    storage_capacity_quota_gib: jsii.Number,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d133e00b0e09d7d138d01eda51b5c8e1ba35251c2bdf8a547534a6fd60490dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c17531a7bfc1ca9994ba6ecd68b613e1ce80ee666cc9626d2fbb4f57ebe7600(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb673027d93fc5c4895688d38b17efec10e6a5cb99148f28f86cb111005b806(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2d5c627fa6a08ed0848a10e46c036754f8a4ee06f2323df6478d1a2ad7d8c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ae15c15f464cf313115fc4a453350dbfc44e07db615a839fbdd9a37533855a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4c69be61bc48ba2e8c312c633034095db9297f4ef90b312c1c05f91673da2c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[FsxOpenzfsVolumeUserAndGroupQuotas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__231f7b63cca7f9a2f423901f081417c669fb3b3b970462abd3c8d532807cfb5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de20202930bb13b6001686d805d48897b6d64547dcc890ea83f5abad06fb0e2d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a2ba53b1e474be6a0cc2935f8ae7b5c6d4101c5fbab648028407947dce4167(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ffa0a1260cae85781f4c14f472a8d3f860b674d22646d675b3fe5ee713dad0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e679b290b16ee45dbf6af424610030b4cf84ca156f9e4c821940c42ce77e6c6b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, FsxOpenzfsVolumeUserAndGroupQuotas]],
) -> None:
    """Type checking stubs"""
    pass
