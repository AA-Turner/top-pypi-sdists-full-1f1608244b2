r'''
# `google_dataplex_zone_iam_binding`

Refer to the Terraform Registry for docs: [`google_dataplex_zone_iam_binding`](https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding).
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


class DataplexZoneIamBinding(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dataplexZoneIamBinding.DataplexZoneIamBinding",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding google_dataplex_zone_iam_binding}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        dataplex_zone: builtins.str,
        lake: builtins.str,
        members: typing.Sequence[builtins.str],
        role: builtins.str,
        condition: typing.Optional[typing.Union["DataplexZoneIamBindingCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding google_dataplex_zone_iam_binding} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataplex_zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#dataplex_zone DataplexZoneIamBinding#dataplex_zone}.
        :param lake: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#lake DataplexZoneIamBinding#lake}.
        :param members: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#members DataplexZoneIamBinding#members}.
        :param role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#role DataplexZoneIamBinding#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#condition DataplexZoneIamBinding#condition}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#id DataplexZoneIamBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#location DataplexZoneIamBinding#location}.
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#project DataplexZoneIamBinding#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10dc9d8938bdc06084308be876f35e9c64222cd11d4f9352e4ab91be4afa04d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataplexZoneIamBindingConfig(
            dataplex_zone=dataplex_zone,
            lake=lake,
            members=members,
            role=role,
            condition=condition,
            id=id,
            location=location,
            project=project,
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
        '''Generates CDKTF code for importing a DataplexZoneIamBinding resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataplexZoneIamBinding to import.
        :param import_from_id: The id of the existing DataplexZoneIamBinding that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataplexZoneIamBinding to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__141ec764b41328600b85f4fa3c9e6ca8455be17fb950dc18e674d174dee7121e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#expression DataplexZoneIamBinding#expression}.
        :param title: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#title DataplexZoneIamBinding#title}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#description DataplexZoneIamBinding#description}.
        '''
        value = DataplexZoneIamBindingCondition(
            expression=expression, title=title, description=description
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="condition")
    def condition(self) -> "DataplexZoneIamBindingConditionOutputReference":
        return typing.cast("DataplexZoneIamBindingConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional["DataplexZoneIamBindingCondition"]:
        return typing.cast(typing.Optional["DataplexZoneIamBindingCondition"], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataplexZoneInput")
    def dataplex_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataplexZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lakeInput")
    def lake_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lakeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="dataplexZone")
    def dataplex_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataplexZone"))

    @dataplex_zone.setter
    def dataplex_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d49ee0fcb46240f4feccf422e9b2a944dd6e06484ffa97a7e192993b402236d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataplexZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5281dbb64f98a50f6359f2d959a7cc3b696f1d26748b513970dfb741eeeeb67d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lake")
    def lake(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lake"))

    @lake.setter
    def lake(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7b32064917b5a17554d7c28495df9dd32d0eea6b442b9611073e63d96399fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lake", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff0b80e48bdf0472ce7299d3021ac8884f4b2e448d7b6a545462e51d330bc95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60e95992d28355299f96f85627eb6f36d40cc4b6ac3521ebeab2339ad0810c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e8dd74553ab2a19d39d6b992c30485dde9a99b6c84a07d214c2f440e0b734e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c2a993ac1cbcca83daf491841310b94ce33e1d095c18845d4fbb39d25f9e7b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dataplexZoneIamBinding.DataplexZoneIamBindingCondition",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "title": "title",
        "description": "description",
    },
)
class DataplexZoneIamBindingCondition:
    def __init__(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#expression DataplexZoneIamBinding#expression}.
        :param title: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#title DataplexZoneIamBinding#title}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#description DataplexZoneIamBinding#description}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c87ea25cd609c48edcc065b97a2d09ac183b05e518d67968646000428bf6438)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#expression DataplexZoneIamBinding#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#title DataplexZoneIamBinding#title}.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#description DataplexZoneIamBinding#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataplexZoneIamBindingCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataplexZoneIamBindingConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dataplexZoneIamBinding.DataplexZoneIamBindingConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc82896f720e42673f70e6052d6351c2d0c51e4931c14349a350a7fd9691bafd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a1160353c6c492306f5ac5df02ee4e880fef734ea99c7dbc6da2f4a1a540017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9286534ba8abfda93326d57bbaa687962eb4d3d1eb836acad9092458d4028dd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39f427908953ba2710066bfc6f58a4575a48ee8270ebf55e126bfe7438d8aba1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataplexZoneIamBindingCondition]:
        return typing.cast(typing.Optional[DataplexZoneIamBindingCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataplexZoneIamBindingCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ae722dabaced40024624bcc1b564bc56152a1052dcda39c3c48790c62098dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dataplexZoneIamBinding.DataplexZoneIamBindingConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataplex_zone": "dataplexZone",
        "lake": "lake",
        "members": "members",
        "role": "role",
        "condition": "condition",
        "id": "id",
        "location": "location",
        "project": "project",
    },
)
class DataplexZoneIamBindingConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        dataplex_zone: builtins.str,
        lake: builtins.str,
        members: typing.Sequence[builtins.str],
        role: builtins.str,
        condition: typing.Optional[typing.Union[DataplexZoneIamBindingCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataplex_zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#dataplex_zone DataplexZoneIamBinding#dataplex_zone}.
        :param lake: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#lake DataplexZoneIamBinding#lake}.
        :param members: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#members DataplexZoneIamBinding#members}.
        :param role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#role DataplexZoneIamBinding#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#condition DataplexZoneIamBinding#condition}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#id DataplexZoneIamBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#location DataplexZoneIamBinding#location}.
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#project DataplexZoneIamBinding#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = DataplexZoneIamBindingCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a012440eab89234e4311342fe26fc02a68fba92c536b68742a52760a1e2462b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataplex_zone", value=dataplex_zone, expected_type=type_hints["dataplex_zone"])
            check_type(argname="argument lake", value=lake, expected_type=type_hints["lake"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataplex_zone": dataplex_zone,
            "lake": lake,
            "members": members,
            "role": role,
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
        if condition is not None:
            self._values["condition"] = condition
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project

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
    def dataplex_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#dataplex_zone DataplexZoneIamBinding#dataplex_zone}.'''
        result = self._values.get("dataplex_zone")
        assert result is not None, "Required property 'dataplex_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lake(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#lake DataplexZoneIamBinding#lake}.'''
        result = self._values.get("lake")
        assert result is not None, "Required property 'lake' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def members(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#members DataplexZoneIamBinding#members}.'''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#role DataplexZoneIamBinding#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[DataplexZoneIamBindingCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#condition DataplexZoneIamBinding#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[DataplexZoneIamBindingCondition], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#id DataplexZoneIamBinding#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#location DataplexZoneIamBinding#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.39.0/docs/resources/dataplex_zone_iam_binding#project DataplexZoneIamBinding#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataplexZoneIamBindingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataplexZoneIamBinding",
    "DataplexZoneIamBindingCondition",
    "DataplexZoneIamBindingConditionOutputReference",
    "DataplexZoneIamBindingConfig",
]

publication.publish()

def _typecheckingstub__d10dc9d8938bdc06084308be876f35e9c64222cd11d4f9352e4ab91be4afa04d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    dataplex_zone: builtins.str,
    lake: builtins.str,
    members: typing.Sequence[builtins.str],
    role: builtins.str,
    condition: typing.Optional[typing.Union[DataplexZoneIamBindingCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__141ec764b41328600b85f4fa3c9e6ca8455be17fb950dc18e674d174dee7121e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d49ee0fcb46240f4feccf422e9b2a944dd6e06484ffa97a7e192993b402236d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5281dbb64f98a50f6359f2d959a7cc3b696f1d26748b513970dfb741eeeeb67d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7b32064917b5a17554d7c28495df9dd32d0eea6b442b9611073e63d96399fb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff0b80e48bdf0472ce7299d3021ac8884f4b2e448d7b6a545462e51d330bc95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60e95992d28355299f96f85627eb6f36d40cc4b6ac3521ebeab2339ad0810c8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e8dd74553ab2a19d39d6b992c30485dde9a99b6c84a07d214c2f440e0b734e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2a993ac1cbcca83daf491841310b94ce33e1d095c18845d4fbb39d25f9e7b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c87ea25cd609c48edcc065b97a2d09ac183b05e518d67968646000428bf6438(
    *,
    expression: builtins.str,
    title: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc82896f720e42673f70e6052d6351c2d0c51e4931c14349a350a7fd9691bafd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1160353c6c492306f5ac5df02ee4e880fef734ea99c7dbc6da2f4a1a540017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9286534ba8abfda93326d57bbaa687962eb4d3d1eb836acad9092458d4028dd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39f427908953ba2710066bfc6f58a4575a48ee8270ebf55e126bfe7438d8aba1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae722dabaced40024624bcc1b564bc56152a1052dcda39c3c48790c62098dc0(
    value: typing.Optional[DataplexZoneIamBindingCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a012440eab89234e4311342fe26fc02a68fba92c536b68742a52760a1e2462b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dataplex_zone: builtins.str,
    lake: builtins.str,
    members: typing.Sequence[builtins.str],
    role: builtins.str,
    condition: typing.Optional[typing.Union[DataplexZoneIamBindingCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
