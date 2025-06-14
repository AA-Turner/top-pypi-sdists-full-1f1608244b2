r'''
# `azurerm_eventgrid_system_topic`

Refer to the Terraform Registry for docs: [`azurerm_eventgrid_system_topic`](https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic).
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


class EventgridSystemTopic(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopic",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic azurerm_eventgrid_system_topic}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        source_arm_resource_id: builtins.str,
        topic_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventgridSystemTopicIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventgridSystemTopicTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic azurerm_eventgrid_system_topic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#location EventgridSystemTopic#location}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#name EventgridSystemTopic#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#resource_group_name EventgridSystemTopic#resource_group_name}.
        :param source_arm_resource_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#source_arm_resource_id EventgridSystemTopic#source_arm_resource_id}.
        :param topic_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#topic_type EventgridSystemTopic#topic_type}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#id EventgridSystemTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity EventgridSystemTopic#identity}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#tags EventgridSystemTopic#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#timeouts EventgridSystemTopic#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f1f22a61039822269760886c457da82d3b62c96133109224a449a92ea208c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventgridSystemTopicConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            source_arm_resource_id=source_arm_resource_id,
            topic_type=topic_type,
            id=id,
            identity=identity,
            tags=tags,
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
        '''Generates CDKTF code for importing a EventgridSystemTopic resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the EventgridSystemTopic to import.
        :param import_from_id: The id of the existing EventgridSystemTopic that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the EventgridSystemTopic to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41a13470f1b2ab8271e970572d6595a79104b225bae37e4db66d36544c72769)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#type EventgridSystemTopic#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity_ids EventgridSystemTopic#identity_ids}.
        '''
        value = EventgridSystemTopicIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#create EventgridSystemTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#delete EventgridSystemTopic#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#read EventgridSystemTopic#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#update EventgridSystemTopic#update}.
        '''
        value = EventgridSystemTopicTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="identity")
    def identity(self) -> "EventgridSystemTopicIdentityOutputReference":
        return typing.cast("EventgridSystemTopicIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="metricArmResourceId")
    def metric_arm_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricArmResourceId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EventgridSystemTopicTimeoutsOutputReference":
        return typing.cast("EventgridSystemTopicTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["EventgridSystemTopicIdentity"]:
        return typing.cast(typing.Optional["EventgridSystemTopicIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceArmResourceIdInput")
    def source_arm_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceArmResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "EventgridSystemTopicTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "EventgridSystemTopicTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicTypeInput")
    def topic_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed68cb3301dce641992088967e7350127eecf852fb14f5834930102b5c24fd0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41bb9ca7f81dba26f9ba649c8d4d65254918ad2178307e854e65dbda057342fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40029d45127b0b022e12b5c2b9f9164b4eb2841edc29c431d756209aa2d0cb96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fb6c1e834fe509a717decddd48dab6ba4b01580dde24ceebd8d23e01315ec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceArmResourceId")
    def source_arm_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceArmResourceId"))

    @source_arm_resource_id.setter
    def source_arm_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0aedcece2e7b2828a780b19091bf85ceac62956f56086ec4e7795dc9d04535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArmResourceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6132f5e1376e776c59831b6e21ddebc3b37958606e76abdf6ea679a00688a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="topicType")
    def topic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topicType"))

    @topic_type.setter
    def topic_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a887c12f44b23acf17eb606376bdcd98517e664d40cb5d6d67de985ff36ba10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicType", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopicConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "source_arm_resource_id": "sourceArmResourceId",
        "topic_type": "topicType",
        "id": "id",
        "identity": "identity",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class EventgridSystemTopicConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        source_arm_resource_id: builtins.str,
        topic_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["EventgridSystemTopicIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EventgridSystemTopicTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#location EventgridSystemTopic#location}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#name EventgridSystemTopic#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#resource_group_name EventgridSystemTopic#resource_group_name}.
        :param source_arm_resource_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#source_arm_resource_id EventgridSystemTopic#source_arm_resource_id}.
        :param topic_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#topic_type EventgridSystemTopic#topic_type}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#id EventgridSystemTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity EventgridSystemTopic#identity}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#tags EventgridSystemTopic#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#timeouts EventgridSystemTopic#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = EventgridSystemTopicIdentity(**identity)
        if isinstance(timeouts, dict):
            timeouts = EventgridSystemTopicTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07c60167ccd3d76ea7ae4533d050a7d9ffa0326529a85cc86e9dcb97c4ace69c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument source_arm_resource_id", value=source_arm_resource_id, expected_type=type_hints["source_arm_resource_id"])
            check_type(argname="argument topic_type", value=topic_type, expected_type=type_hints["topic_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "source_arm_resource_id": source_arm_resource_id,
            "topic_type": topic_type,
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
        if identity is not None:
            self._values["identity"] = identity
        if tags is not None:
            self._values["tags"] = tags
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#location EventgridSystemTopic#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#name EventgridSystemTopic#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#resource_group_name EventgridSystemTopic#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_arm_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#source_arm_resource_id EventgridSystemTopic#source_arm_resource_id}.'''
        result = self._values.get("source_arm_resource_id")
        assert result is not None, "Required property 'source_arm_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#topic_type EventgridSystemTopic#topic_type}.'''
        result = self._values.get("topic_type")
        assert result is not None, "Required property 'topic_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#id EventgridSystemTopic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["EventgridSystemTopicIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity EventgridSystemTopic#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["EventgridSystemTopicIdentity"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#tags EventgridSystemTopic#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EventgridSystemTopicTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#timeouts EventgridSystemTopic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventgridSystemTopicTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopicIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class EventgridSystemTopicIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#type EventgridSystemTopic#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity_ids EventgridSystemTopic#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8518f8be23c4de3f81a365a87e2ec4dfcc0f1c0cba9d26a81dfb819bea7a669d)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#type EventgridSystemTopic#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#identity_ids EventgridSystemTopic#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopicIdentityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5639f1095bfc5291b9af30aeb835fe35e0477a5d4997edf48f76b4a5ed3d46f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1992587b7ca177ec65ef7412cd2c58912d7a5f2e43d5a5797a7d78f28e238db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a585b597f08c76e946bfa55171622480c44c6f0d7fc2fff984aab3e80a7288d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventgridSystemTopicIdentity]:
        return typing.cast(typing.Optional[EventgridSystemTopicIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c2ff2bd513b41ca52e42893f896e90df9da06143b3b5793f20ece0d03d938f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopicTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventgridSystemTopicTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#create EventgridSystemTopic#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#delete EventgridSystemTopic#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#read EventgridSystemTopic#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#update EventgridSystemTopic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dd3c095a2c0c0d0d84aa6ebccd3ee854872d9057f6686a9f7b851bb51f2334b)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#create EventgridSystemTopic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#delete EventgridSystemTopic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#read EventgridSystemTopic#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/4.33.0/docs/resources/eventgrid_system_topic#update EventgridSystemTopic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopic.EventgridSystemTopicTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ae55a2dc1e9719f97b4f3cfbbaa9d39379ba1b35228fe19bfd051c18427babf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6d983b85f24c080c2017cc557b0e537927a2505fd613da10d6e3312dd74fdf3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41e9bd36e46ac8e5558cc098abcf689b2a235a9081a2a8cc63f1a976182dfff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ca70e16a34a71f062586d466e1df0582465d0c931e441f8c9463ec48dbb2e55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c3395ac385ddc3c94a369fa3187d9d775f8be7376782704337b19efad06a03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EventgridSystemTopicTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EventgridSystemTopicTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EventgridSystemTopicTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba69c7bf8db2b08c31828cd5014d0e2f0de69cc83570d2242653a098850b4150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "EventgridSystemTopic",
    "EventgridSystemTopicConfig",
    "EventgridSystemTopicIdentity",
    "EventgridSystemTopicIdentityOutputReference",
    "EventgridSystemTopicTimeouts",
    "EventgridSystemTopicTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__57f1f22a61039822269760886c457da82d3b62c96133109224a449a92ea208c5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    source_arm_resource_id: builtins.str,
    topic_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[EventgridSystemTopicIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[EventgridSystemTopicTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__c41a13470f1b2ab8271e970572d6595a79104b225bae37e4db66d36544c72769(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed68cb3301dce641992088967e7350127eecf852fb14f5834930102b5c24fd0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41bb9ca7f81dba26f9ba649c8d4d65254918ad2178307e854e65dbda057342fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40029d45127b0b022e12b5c2b9f9164b4eb2841edc29c431d756209aa2d0cb96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fb6c1e834fe509a717decddd48dab6ba4b01580dde24ceebd8d23e01315ec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0aedcece2e7b2828a780b19091bf85ceac62956f56086ec4e7795dc9d04535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6132f5e1376e776c59831b6e21ddebc3b37958606e76abdf6ea679a00688a6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a887c12f44b23acf17eb606376bdcd98517e664d40cb5d6d67de985ff36ba10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07c60167ccd3d76ea7ae4533d050a7d9ffa0326529a85cc86e9dcb97c4ace69c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    source_arm_resource_id: builtins.str,
    topic_type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[EventgridSystemTopicIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[EventgridSystemTopicTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8518f8be23c4de3f81a365a87e2ec4dfcc0f1c0cba9d26a81dfb819bea7a669d(
    *,
    type: builtins.str,
    identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5639f1095bfc5291b9af30aeb835fe35e0477a5d4997edf48f76b4a5ed3d46f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1992587b7ca177ec65ef7412cd2c58912d7a5f2e43d5a5797a7d78f28e238db(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a585b597f08c76e946bfa55171622480c44c6f0d7fc2fff984aab3e80a7288d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c2ff2bd513b41ca52e42893f896e90df9da06143b3b5793f20ece0d03d938f2(
    value: typing.Optional[EventgridSystemTopicIdentity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd3c095a2c0c0d0d84aa6ebccd3ee854872d9057f6686a9f7b851bb51f2334b(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ae55a2dc1e9719f97b4f3cfbbaa9d39379ba1b35228fe19bfd051c18427babf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d983b85f24c080c2017cc557b0e537927a2505fd613da10d6e3312dd74fdf3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41e9bd36e46ac8e5558cc098abcf689b2a235a9081a2a8cc63f1a976182dfff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca70e16a34a71f062586d466e1df0582465d0c931e441f8c9463ec48dbb2e55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c3395ac385ddc3c94a369fa3187d9d775f8be7376782704337b19efad06a03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba69c7bf8db2b08c31828cd5014d0e2f0de69cc83570d2242653a098850b4150(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EventgridSystemTopicTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
