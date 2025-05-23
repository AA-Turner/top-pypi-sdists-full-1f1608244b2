r'''
# `aws_apigatewayv2_domain_name`

Refer to the Terraform Registry for docs: [`aws_apigatewayv2_domain_name`](https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name).
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


class Apigatewayv2DomainName(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainName",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name aws_apigatewayv2_domain_name}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        domain_name_configuration: typing.Union["Apigatewayv2DomainNameDomainNameConfiguration", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["Apigatewayv2DomainNameMutualTlsAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Apigatewayv2DomainNameTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name aws_apigatewayv2_domain_name} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name Apigatewayv2DomainName#domain_name}.
        :param domain_name_configuration: domain_name_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name_configuration Apigatewayv2DomainName#domain_name_configuration}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#id Apigatewayv2DomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#mutual_tls_authentication Apigatewayv2DomainName#mutual_tls_authentication}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags Apigatewayv2DomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags_all Apigatewayv2DomainName#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#timeouts Apigatewayv2DomainName#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91959a4160529f83122e32ef0c0a8e3f9e49fa1ffc8319677e9a1de003b557b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Apigatewayv2DomainNameConfig(
            domain_name=domain_name,
            domain_name_configuration=domain_name_configuration,
            id=id,
            mutual_tls_authentication=mutual_tls_authentication,
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
        '''Generates CDKTF code for importing a Apigatewayv2DomainName resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Apigatewayv2DomainName to import.
        :param import_from_id: The id of the existing Apigatewayv2DomainName that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Apigatewayv2DomainName to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749666d6c798b5a7840858abcc89cb4136198fe2f75cbe348eb435a498bd1010)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putDomainNameConfiguration")
    def put_domain_name_configuration(
        self,
        *,
        certificate_arn: builtins.str,
        endpoint_type: builtins.str,
        security_policy: builtins.str,
        ip_address_type: typing.Optional[builtins.str] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#certificate_arn Apigatewayv2DomainName#certificate_arn}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#endpoint_type Apigatewayv2DomainName#endpoint_type}.
        :param security_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#security_policy Apigatewayv2DomainName#security_policy}.
        :param ip_address_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ip_address_type Apigatewayv2DomainName#ip_address_type}.
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ownership_verification_certificate_arn Apigatewayv2DomainName#ownership_verification_certificate_arn}.
        '''
        value = Apigatewayv2DomainNameDomainNameConfiguration(
            certificate_arn=certificate_arn,
            endpoint_type=endpoint_type,
            security_policy=security_policy,
            ip_address_type=ip_address_type,
            ownership_verification_certificate_arn=ownership_verification_certificate_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDomainNameConfiguration", [value]))

    @jsii.member(jsii_name="putMutualTlsAuthentication")
    def put_mutual_tls_authentication(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_uri Apigatewayv2DomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_version Apigatewayv2DomainName#truststore_version}.
        '''
        value = Apigatewayv2DomainNameMutualTlsAuthentication(
            truststore_uri=truststore_uri, truststore_version=truststore_version
        )

        return typing.cast(None, jsii.invoke(self, "putMutualTlsAuthentication", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#create Apigatewayv2DomainName#create}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#update Apigatewayv2DomainName#update}.
        '''
        value = Apigatewayv2DomainNameTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMutualTlsAuthentication")
    def reset_mutual_tls_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMutualTlsAuthentication", []))

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
    @jsii.member(jsii_name="apiMappingSelectionExpression")
    def api_mapping_selection_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiMappingSelectionExpression"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="domainNameConfiguration")
    def domain_name_configuration(
        self,
    ) -> "Apigatewayv2DomainNameDomainNameConfigurationOutputReference":
        return typing.cast("Apigatewayv2DomainNameDomainNameConfigurationOutputReference", jsii.get(self, "domainNameConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> "Apigatewayv2DomainNameMutualTlsAuthenticationOutputReference":
        return typing.cast("Apigatewayv2DomainNameMutualTlsAuthenticationOutputReference", jsii.get(self, "mutualTlsAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "Apigatewayv2DomainNameTimeoutsOutputReference":
        return typing.cast("Apigatewayv2DomainNameTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="domainNameConfigurationInput")
    def domain_name_configuration_input(
        self,
    ) -> typing.Optional["Apigatewayv2DomainNameDomainNameConfiguration"]:
        return typing.cast(typing.Optional["Apigatewayv2DomainNameDomainNameConfiguration"], jsii.get(self, "domainNameConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthenticationInput")
    def mutual_tls_authentication_input(
        self,
    ) -> typing.Optional["Apigatewayv2DomainNameMutualTlsAuthentication"]:
        return typing.cast(typing.Optional["Apigatewayv2DomainNameMutualTlsAuthentication"], jsii.get(self, "mutualTlsAuthenticationInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "Apigatewayv2DomainNameTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "Apigatewayv2DomainNameTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77c1e3f51c5ecffe2af2bd9534398c066dce4d598e64c32f569136c4d3c4c4f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc16d5d81aeddf5196ffb3df34ccab78d6428c58730c705ca5e7491ad8498fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a368ead9f4401cb678e5b38f3e4c84a5b95a7a2e8b0cf2ffa3b07c2c31f10739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a32d725fe1aa53e76b442659820c275497c72331ad3c09e82b40a8217f11411c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "domain_name_configuration": "domainNameConfiguration",
        "id": "id",
        "mutual_tls_authentication": "mutualTlsAuthentication",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class Apigatewayv2DomainNameConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain_name: builtins.str,
        domain_name_configuration: typing.Union["Apigatewayv2DomainNameDomainNameConfiguration", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["Apigatewayv2DomainNameMutualTlsAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Apigatewayv2DomainNameTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name Apigatewayv2DomainName#domain_name}.
        :param domain_name_configuration: domain_name_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name_configuration Apigatewayv2DomainName#domain_name_configuration}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#id Apigatewayv2DomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#mutual_tls_authentication Apigatewayv2DomainName#mutual_tls_authentication}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags Apigatewayv2DomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags_all Apigatewayv2DomainName#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#timeouts Apigatewayv2DomainName#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(domain_name_configuration, dict):
            domain_name_configuration = Apigatewayv2DomainNameDomainNameConfiguration(**domain_name_configuration)
        if isinstance(mutual_tls_authentication, dict):
            mutual_tls_authentication = Apigatewayv2DomainNameMutualTlsAuthentication(**mutual_tls_authentication)
        if isinstance(timeouts, dict):
            timeouts = Apigatewayv2DomainNameTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9292fc0b0376aefda99a7e9dd8a305a52164805473e81ccdf3715fa3a2e414d9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_name_configuration", value=domain_name_configuration, expected_type=type_hints["domain_name_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "domain_name_configuration": domain_name_configuration,
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
        if mutual_tls_authentication is not None:
            self._values["mutual_tls_authentication"] = mutual_tls_authentication
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
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name Apigatewayv2DomainName#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name_configuration(
        self,
    ) -> "Apigatewayv2DomainNameDomainNameConfiguration":
        '''domain_name_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#domain_name_configuration Apigatewayv2DomainName#domain_name_configuration}
        '''
        result = self._values.get("domain_name_configuration")
        assert result is not None, "Required property 'domain_name_configuration' is missing"
        return typing.cast("Apigatewayv2DomainNameDomainNameConfiguration", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#id Apigatewayv2DomainName#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mutual_tls_authentication(
        self,
    ) -> typing.Optional["Apigatewayv2DomainNameMutualTlsAuthentication"]:
        '''mutual_tls_authentication block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#mutual_tls_authentication Apigatewayv2DomainName#mutual_tls_authentication}
        '''
        result = self._values.get("mutual_tls_authentication")
        return typing.cast(typing.Optional["Apigatewayv2DomainNameMutualTlsAuthentication"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags Apigatewayv2DomainName#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#tags_all Apigatewayv2DomainName#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["Apigatewayv2DomainNameTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#timeouts Apigatewayv2DomainName#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["Apigatewayv2DomainNameTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2DomainNameConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameDomainNameConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "endpoint_type": "endpointType",
        "security_policy": "securityPolicy",
        "ip_address_type": "ipAddressType",
        "ownership_verification_certificate_arn": "ownershipVerificationCertificateArn",
    },
)
class Apigatewayv2DomainNameDomainNameConfiguration:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        endpoint_type: builtins.str,
        security_policy: builtins.str,
        ip_address_type: typing.Optional[builtins.str] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#certificate_arn Apigatewayv2DomainName#certificate_arn}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#endpoint_type Apigatewayv2DomainName#endpoint_type}.
        :param security_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#security_policy Apigatewayv2DomainName#security_policy}.
        :param ip_address_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ip_address_type Apigatewayv2DomainName#ip_address_type}.
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ownership_verification_certificate_arn Apigatewayv2DomainName#ownership_verification_certificate_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c69a4b0eadaa74d6207d24ef731010620fb3e8390223bbfd0d3c0b3d070d166)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument ownership_verification_certificate_arn", value=ownership_verification_certificate_arn, expected_type=type_hints["ownership_verification_certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "endpoint_type": endpoint_type,
            "security_policy": security_policy,
        }
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if ownership_verification_certificate_arn is not None:
            self._values["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#certificate_arn Apigatewayv2DomainName#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#endpoint_type Apigatewayv2DomainName#endpoint_type}.'''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#security_policy Apigatewayv2DomainName#security_policy}.'''
        result = self._values.get("security_policy")
        assert result is not None, "Required property 'security_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ip_address_type Apigatewayv2DomainName#ip_address_type}.'''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ownership_verification_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#ownership_verification_certificate_arn Apigatewayv2DomainName#ownership_verification_certificate_arn}.'''
        result = self._values.get("ownership_verification_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2DomainNameDomainNameConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2DomainNameDomainNameConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameDomainNameConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__519c15ae6e0d31b7bc04e6abdfb6a0897905f8f2573893d35504eff6a632d5f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIpAddressType")
    def reset_ip_address_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddressType", []))

    @jsii.member(jsii_name="resetOwnershipVerificationCertificateArn")
    def reset_ownership_verification_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnershipVerificationCertificateArn", []))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="targetDomainName")
    def target_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDomainName"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTypeInput")
    def endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressTypeInput")
    def ip_address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ownershipVerificationCertificateArnInput")
    def ownership_verification_certificate_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownershipVerificationCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyInput")
    def security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404a264c719b3a44f746e9728e36a704b60515ca50b9014d686c6d47c6e2edc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd7621d9d1d27de61aa52cb64440da1c1c167e64d01dcc15f714b5ba15e7045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905b4665f1d6ddc0fc2ba604ec3897c60352c4a16fd809014b171580e51e05e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownershipVerificationCertificateArn"))

    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ff668eb929bb399fb78f6e2996561ddf836f8539b0ca58688d17a81f5039c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownershipVerificationCertificateArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @security_policy.setter
    def security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2506399065da44d66ef92791dd3bfaf3b6bed6596a4e3e2d42bc61d41b996565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Apigatewayv2DomainNameDomainNameConfiguration]:
        return typing.cast(typing.Optional[Apigatewayv2DomainNameDomainNameConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Apigatewayv2DomainNameDomainNameConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f86da1f007026066b9c541af20541d9a62e8d7141f6b89063a9632efc09271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameMutualTlsAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "truststore_uri": "truststoreUri",
        "truststore_version": "truststoreVersion",
    },
)
class Apigatewayv2DomainNameMutualTlsAuthentication:
    def __init__(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_uri Apigatewayv2DomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_version Apigatewayv2DomainName#truststore_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e63498f21fa49aee32395f3d18d157bbba52739d7133a5171283c905c90764)
            check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
            check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "truststore_uri": truststore_uri,
        }
        if truststore_version is not None:
            self._values["truststore_version"] = truststore_version

    @builtins.property
    def truststore_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_uri Apigatewayv2DomainName#truststore_uri}.'''
        result = self._values.get("truststore_uri")
        assert result is not None, "Required property 'truststore_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def truststore_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#truststore_version Apigatewayv2DomainName#truststore_version}.'''
        result = self._values.get("truststore_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2DomainNameMutualTlsAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2DomainNameMutualTlsAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameMutualTlsAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c722e32d8197ae7485c6ca3350eae4045aa2dd83e76a55816b81708aeab91c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTruststoreVersion")
    def reset_truststore_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststoreVersion", []))

    @builtins.property
    @jsii.member(jsii_name="truststoreUriInput")
    def truststore_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreUriInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreVersionInput")
    def truststore_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreUri")
    def truststore_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreUri"))

    @truststore_uri.setter
    def truststore_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a754be2531ca4cfed6cc8773d158167c03133dda095bd42e64ba86b714e7795e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="truststoreVersion")
    def truststore_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreVersion"))

    @truststore_version.setter
    def truststore_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2e33a1d6d50af38be7f070be82a46feda89bea298aeaab8cf1fec4a35e0655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Apigatewayv2DomainNameMutualTlsAuthentication]:
        return typing.cast(typing.Optional[Apigatewayv2DomainNameMutualTlsAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Apigatewayv2DomainNameMutualTlsAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d540fe836aa0b7dccb820aec1ad54c49727be49506a6c23964a2dc812e59ff76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class Apigatewayv2DomainNameTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#create Apigatewayv2DomainName#create}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#update Apigatewayv2DomainName#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__294eddb1803ee82202f3f7381a4a2e6d43d753b6c02836accf83abba93459d05)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#create Apigatewayv2DomainName#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/apigatewayv2_domain_name#update Apigatewayv2DomainName#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2DomainNameTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2DomainNameTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2DomainName.Apigatewayv2DomainNameTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f0fa01c3f2513bc3e3d55716188b794b062ab4ac87ef4430e01cb3c5457565c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c7f52fa81a0e58a2dd116075d2f76ef241154b2f2bba31fad7698f8ee73b720d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20c5ecfdbb13034bec17cd073bc9726cae213beb01ef2285a2493644f3c8f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, Apigatewayv2DomainNameTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, Apigatewayv2DomainNameTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, Apigatewayv2DomainNameTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ced91ea36850dc6ea64acd168cbb46e9d62782a982b9d4b50d71a95415ae93f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Apigatewayv2DomainName",
    "Apigatewayv2DomainNameConfig",
    "Apigatewayv2DomainNameDomainNameConfiguration",
    "Apigatewayv2DomainNameDomainNameConfigurationOutputReference",
    "Apigatewayv2DomainNameMutualTlsAuthentication",
    "Apigatewayv2DomainNameMutualTlsAuthenticationOutputReference",
    "Apigatewayv2DomainNameTimeouts",
    "Apigatewayv2DomainNameTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__91959a4160529f83122e32ef0c0a8e3f9e49fa1ffc8319677e9a1de003b557b1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_name: builtins.str,
    domain_name_configuration: typing.Union[Apigatewayv2DomainNameDomainNameConfiguration, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[Apigatewayv2DomainNameMutualTlsAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Apigatewayv2DomainNameTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__749666d6c798b5a7840858abcc89cb4136198fe2f75cbe348eb435a498bd1010(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c1e3f51c5ecffe2af2bd9534398c066dce4d598e64c32f569136c4d3c4c4f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc16d5d81aeddf5196ffb3df34ccab78d6428c58730c705ca5e7491ad8498fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a368ead9f4401cb678e5b38f3e4c84a5b95a7a2e8b0cf2ffa3b07c2c31f10739(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32d725fe1aa53e76b442659820c275497c72331ad3c09e82b40a8217f11411c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9292fc0b0376aefda99a7e9dd8a305a52164805473e81ccdf3715fa3a2e414d9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain_name: builtins.str,
    domain_name_configuration: typing.Union[Apigatewayv2DomainNameDomainNameConfiguration, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[Apigatewayv2DomainNameMutualTlsAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Apigatewayv2DomainNameTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c69a4b0eadaa74d6207d24ef731010620fb3e8390223bbfd0d3c0b3d070d166(
    *,
    certificate_arn: builtins.str,
    endpoint_type: builtins.str,
    security_policy: builtins.str,
    ip_address_type: typing.Optional[builtins.str] = None,
    ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__519c15ae6e0d31b7bc04e6abdfb6a0897905f8f2573893d35504eff6a632d5f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404a264c719b3a44f746e9728e36a704b60515ca50b9014d686c6d47c6e2edc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd7621d9d1d27de61aa52cb64440da1c1c167e64d01dcc15f714b5ba15e7045(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905b4665f1d6ddc0fc2ba604ec3897c60352c4a16fd809014b171580e51e05e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ff668eb929bb399fb78f6e2996561ddf836f8539b0ca58688d17a81f5039c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2506399065da44d66ef92791dd3bfaf3b6bed6596a4e3e2d42bc61d41b996565(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f86da1f007026066b9c541af20541d9a62e8d7141f6b89063a9632efc09271(
    value: typing.Optional[Apigatewayv2DomainNameDomainNameConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e63498f21fa49aee32395f3d18d157bbba52739d7133a5171283c905c90764(
    *,
    truststore_uri: builtins.str,
    truststore_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c722e32d8197ae7485c6ca3350eae4045aa2dd83e76a55816b81708aeab91c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a754be2531ca4cfed6cc8773d158167c03133dda095bd42e64ba86b714e7795e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2e33a1d6d50af38be7f070be82a46feda89bea298aeaab8cf1fec4a35e0655(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d540fe836aa0b7dccb820aec1ad54c49727be49506a6c23964a2dc812e59ff76(
    value: typing.Optional[Apigatewayv2DomainNameMutualTlsAuthentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294eddb1803ee82202f3f7381a4a2e6d43d753b6c02836accf83abba93459d05(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f0fa01c3f2513bc3e3d55716188b794b062ab4ac87ef4430e01cb3c5457565c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f52fa81a0e58a2dd116075d2f76ef241154b2f2bba31fad7698f8ee73b720d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20c5ecfdbb13034bec17cd073bc9726cae213beb01ef2285a2493644f3c8f16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced91ea36850dc6ea64acd168cbb46e9d62782a982b9d4b50d71a95415ae93f4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, Apigatewayv2DomainNameTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
