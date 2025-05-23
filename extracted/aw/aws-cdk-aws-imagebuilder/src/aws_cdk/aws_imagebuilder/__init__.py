'''
# AWS::ImageBuilder Construct Library

<!--BEGIN STABILITY BANNER-->---


![End-of-Support](https://img.shields.io/badge/End--of--Support-critical.svg?style=for-the-badge)

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
>
> For more information on how to migrate, see the [*Migrating to AWS CDK v2* guide](https://docs.aws.amazon.com/cdk/v2/guide/migrating-v2.html).

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_imagebuilder as imagebuilder
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ImageBuilder construct libraries](https://constructs.dev/search?q=imagebuilder)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ImageBuilder resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ImageBuilder.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ImageBuilder](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ImageBuilder.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.core as _aws_cdk_core_f4b25747


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnComponent(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnComponent",
):
    '''A CloudFormation ``AWS::ImageBuilder::Component``.

    Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:

    - Inline, using the ``data`` property in the request body.
    - A URL that points to a YAML document file stored in Amazon S3, using the ``uri`` property in the request body.

    :cloudformationResource: AWS::ImageBuilder::Component
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_component = imagebuilder.CfnComponent(self, "MyCfnComponent",
            name="name",
            platform="platform",
            version="version",
        
            # the properties below are optional
            change_description="changeDescription",
            data="data",
            description="description",
            kms_key_id="kmsKeyId",
            supported_os_versions=["supportedOsVersions"],
            tags={
                "tags_key": "tags"
            },
            uri="uri"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::Component``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the component.
        :param platform: The operating system platform of the component.
        :param version: The component version. For example, ``1.0.0`` .
        :param change_description: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of this component.
        :param data: Component ``data`` contains inline YAML document content for the component. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the contents of the component.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this component.
        :param supported_os_versions: The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
        :param tags: The tags that apply to the component.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1cc496479ca9a7e56302a9fae6564e6463f16f4a3c79d73ae9cb1e516fff30)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComponentProps(
            name=name,
            platform=platform,
            version=version,
            change_description=change_description,
            data=data,
            description=description,
            kms_key_id=kms_key_id,
            supported_os_versions=supported_os_versions,
            tags=tags,
            uri=uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d1d3a4e830d89b8fde7cfd0c5493b5f0d5e0f06b341d1042c38662356d36bfe)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a5bc457d43bc19c97861b09c1fa9214c08d586f5ba7a50fad38481e003fe51e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the component.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEncrypted")
    def attr_encrypted(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''Returns the encryption status of the component.

        For example ``true`` or ``false`` .

        :cloudformationAttribute: Encrypted
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrEncrypted"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the component.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Image Builder determines the component type based on the phases that are defined in the component document.

        If there is only one phase, and its name is "test", then the type is ``TEST`` . For all other components, the type is ``BUILD`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags that apply to the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde1a86ca9e902e1addd2a81110f8233ec96875552eaa8840d74decacfc1d8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''The operating system platform of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba8d97cf8edacc2fadac0834e0d290a3e3bbddb3a1db919ce9572a891afd64f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The component version.

        For example, ``1.0.0`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0257100f3292352bce9185283bc58df048fdd20bee2c0192ffff43dbea6f2e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="changeDescription")
    def change_description(self) -> typing.Optional[builtins.str]:
        '''The change description of the component.

        Describes what change has been made in this version, or what makes this version different from other versions of this component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "changeDescription"))

    @change_description.setter
    def change_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__535c87ef75a121fb96069401cd994baa0b0342fd87d07e8e9a5218dd85cf0fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeDescription", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Optional[builtins.str]:
        '''Component ``data`` contains inline YAML document content for the component.

        Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5a38ca397e02fed2911fab93f0479eccbea9d4e93787bbaa9c19ea89b0acdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the contents of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59c5f389a50bab79a740422a35c62a4da37834083a780b630614629f824141e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d967b4edb058173d8baa35061e6f7a7557fbebbc30763f83981e816304ab2669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="supportedOsVersions")
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The operating system (OS) version supported by the component.

        If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportedOsVersions"))

    @supported_os_versions.setter
    def supported_os_versions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429bf33b064b5cb1813e8319a0f011601ccc7adb3e4a710efde80452630dfad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedOsVersions", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.

        This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.

        Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__004003e5f6aefdef96be33bcaca60db67a172a08069716f8f731a48c01df6ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "platform": "platform",
        "version": "version",
        "change_description": "changeDescription",
        "data": "data",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "supported_os_versions": "supportedOsVersions",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnComponentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnComponent``.

        :param name: The name of the component.
        :param platform: The operating system platform of the component.
        :param version: The component version. For example, ``1.0.0`` .
        :param change_description: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of this component.
        :param data: Component ``data`` contains inline YAML document content for the component. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the contents of the component.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this component.
        :param supported_os_versions: The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
        :param tags: The tags that apply to the component.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_component_props = imagebuilder.CfnComponentProps(
                name="name",
                platform="platform",
                version="version",
            
                # the properties below are optional
                change_description="changeDescription",
                data="data",
                description="description",
                kms_key_id="kmsKeyId",
                supported_os_versions=["supportedOsVersions"],
                tags={
                    "tags_key": "tags"
                },
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd24992bfb80dc6981c6fc6d3f765ee7be888021dca1a6c49802eed1857adaef)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument change_description", value=change_description, expected_type=type_hints["change_description"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument supported_os_versions", value=supported_os_versions, expected_type=type_hints["supported_os_versions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "platform": platform,
            "version": version,
        }
        if change_description is not None:
            self._values["change_description"] = change_description
        if data is not None:
            self._values["data"] = data
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if supported_os_versions is not None:
            self._values["supported_os_versions"] = supported_os_versions
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''The operating system platform of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The component version.

        For example, ``1.0.0`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def change_description(self) -> typing.Optional[builtins.str]:
        '''The change description of the component.

        Describes what change has been made in this version, or what makes this version different from other versions of this component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription
        '''
        result = self._values.get("change_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Component ``data`` contains inline YAML document content for the component.

        Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the contents of the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The operating system (OS) version supported by the component.

        If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions
        '''
        result = self._values.get("supported_os_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that apply to the component.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.

        This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.

        Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnContainerRecipe(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe",
):
    '''A CloudFormation ``AWS::ImageBuilder::ContainerRecipe``.

    Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.

    :cloudformationResource: AWS::ImageBuilder::ContainerRecipe
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_container_recipe = imagebuilder.CfnContainerRecipe(self, "MyCfnContainerRecipe",
            components=[imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                component_arn="componentArn",
                parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )]
            )],
            container_type="containerType",
            name="name",
            parent_image="parentImage",
            target_repository=imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                repository_name="repositoryName",
                service="service"
            ),
            version="version",
        
            # the properties below are optional
            description="description",
            dockerfile_template_data="dockerfileTemplateData",
            dockerfile_template_uri="dockerfileTemplateUri",
            image_os_version_override="imageOsVersionOverride",
            instance_configuration=imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                image="image"
            ),
            kms_key_id="kmsKeyId",
            platform_override="platformOverride",
            tags={
                "tags_key": "tags"
            },
            working_directory="workingDirectory"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.TargetContainerRepositoryProperty", typing.Dict[builtins.str, typing.Any]]],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.InstanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ContainerRecipe``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param components: Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
        :param container_type: Specifies the type of container, such as Docker.
        :param name: The name of the container recipe.
        :param parent_image: The base image for the container recipe.
        :param target_repository: The destination repository for the container image.
        :param version: The semantic version of the container recipe. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01. *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
        :param description: The description of the container recipe.
        :param dockerfile_template_data: Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        :param dockerfile_template_uri: The S3 URI for the Dockerfile that will be used to build your container image.
        :param image_os_version_override: Specifies the operating system version for the base image.
        :param instance_configuration: A group of options that can be used to configure an instance for building and testing container images.
        :param kms_key_id: Identifies which KMS key is used to encrypt the container image for distribution to the target Region.
        :param platform_override: Specifies the operating system platform when you use a custom base image.
        :param tags: Tags that are attached to the container recipe.
        :param working_directory: The working directory for use during build and test workflows.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a7a95c6787ef0de46ea7fc6e498a4f738e8f5e3a649569a79ad578be3a464c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerRecipeProps(
            components=components,
            container_type=container_type,
            name=name,
            parent_image=parent_image,
            target_repository=target_repository,
            version=version,
            description=description,
            dockerfile_template_data=dockerfile_template_data,
            dockerfile_template_uri=dockerfile_template_uri,
            image_os_version_override=image_os_version_override,
            instance_configuration=instance_configuration,
            kms_key_id=kms_key_id,
            platform_override=platform_override,
            tags=tags,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c344ceecb7750044c0ac74df20671951a97b05e5fa5a942e2a195acd0556b1a)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a380b36c2d9e74fed5e73eaa9e86334ab1bc02127337337058474afcdd7e34b0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the container recipe.

        For example, ``arn:aws:imagebuilder:us-east-1:123456789012:container-recipe/mybasicrecipe/2020.12.17`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the container recipe.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''Tags that are attached to the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.ComponentConfigurationProperty"]]]:
        '''Build and test components that are included in the container recipe.

        Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.ComponentConfigurationProperty"]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.ComponentConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd606a5fbad5302ea8b76746496ee9a0e9f765851ef1559ae006a14b8df69e40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="containerType")
    def container_type(self) -> builtins.str:
        '''Specifies the type of container, such as Docker.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype
        '''
        return typing.cast(builtins.str, jsii.get(self, "containerType"))

    @container_type.setter
    def container_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb9cf6b425d2821fd7ba904f31d021c39a45d0945c61cbc01b3ef3b753e40297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8df7c0eb4a7d7ca1930c3a379eda08933ffd70c8ce731411b0ad0d2defd87f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''The base image for the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5447b5e4f0886a01512608136cfb66edacff16c92c150a251e3f9408d823ebc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentImage", value)

    @builtins.property
    @jsii.member(jsii_name="targetRepository")
    def target_repository(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"]:
        '''The destination repository for the container image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"], jsii.get(self, "targetRepository"))

    @target_repository.setter
    def target_repository(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__176e453b4b00bd19c068dd0f245ea5711270097a461acc75037495b40e977d9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRepository", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The semantic version of the container recipe.

        .. epigraph::

           The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them.

           *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

           *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

           *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc638802bcce467ed21456f46af189fee6752d0dbf7736343fc2d098b9c8edcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ad39f5db954328b06d2c5a62a5bac47e5de00790f75f37a736bab86a21d844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside.

        The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateData"))

    @dockerfile_template_data.setter
    def dockerfile_template_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93c1ff944d64647d555a771f9ad14a4cbb4c07af5aa2af349cecabe519100daf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfileTemplateData", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI for the Dockerfile that will be used to build your container image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateUri"))

    @dockerfile_template_uri.setter
    def dockerfile_template_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28c7509cfa85df4c9d9a6a62ba26cd51f5770beaf8d35f90608c559e445064e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfileTemplateUri", value)

    @builtins.property
    @jsii.member(jsii_name="imageOsVersionOverride")
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system version for the base image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageOsVersionOverride"))

    @image_os_version_override.setter
    def image_os_version_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa9007617092d0e02ec42569d32f745b296896b7aa8a7e541a7d89281eea45c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageOsVersionOverride", value)

    @builtins.property
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]]:
        '''A group of options that can be used to configure an instance for building and testing container images.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1e2c3c55656dc0037a081a77759041ff8c48743c5fd4a4cc9735b31c3cde90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifies which KMS key is used to encrypt the container image for distribution to the target Region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__535134592066797e884b78e86fbb290748041c36be000822b69756e9af986b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="platformOverride")
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system platform when you use a custom base image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformOverride"))

    @platform_override.setter
    def platform_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fd5d41217536e9f564911f70cc73f7e433f7b6e6f47abeac8319148a0a2791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformOverride", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory for use during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba6ca6febff34f0df678cb4b2d0d79612dcf6926b329f470402e703da38c326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn", "parameters": "parameters"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.ComponentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration details of the component.

            :param component_arn: The Amazon Resource Name (ARN) of the component.
            :param parameters: ``CfnContainerRecipe.ComponentConfigurationProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                component_configuration_property = imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__99fe9a2266fba31ee5528ce66e321487e8d4d5b672a1e80006f8dc6032bdaa69)
                check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.ComponentParameterProperty"]]]]:
            '''``CfnContainerRecipe.ComponentConfigurationProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.ComponentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.ComponentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ComponentParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnContainerRecipe.ComponentParameterProperty.Name``.
            :param value: ``CfnContainerRecipe.ComponentParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                component_parameter_property = imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c0feaf5f018aacd89766cdaa849154b3566249f697b429f5d7fb9bc4053207fc)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnContainerRecipe.ComponentParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''``CfnContainerRecipe.ComponentParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon EBS-specific block device mapping specifications.

            :param delete_on_termination: Use to configure delete on termination of the associated device.
            :param encrypted: Use to configure device encryption.
            :param iops: Use to configure device IOPS.
            :param kms_key_id: Use to configure the KMS key to use when encrypting the device.
            :param snapshot_id: The snapshot that defines the device contents.
            :param throughput: *For GP3 volumes only* – The throughput in MiB/s that the volume supports.
            :param volume_size: Use to override the device's volume size.
            :param volume_type: Use to override the device's volume type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                ebs_instance_block_device_specification_property = imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__095e4bd8d8ed7fecebf35e2ce1dd0c2c9fc9ef875518bb499f58de181585fa56)
                check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Use to configure delete on termination of the associated device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Use to configure device encryption.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''Use to configure device IOPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''Use to configure the KMS key to use when encrypting the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''The snapshot that defines the device contents.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''*For GP3 volumes only* – The throughput in MiB/s that the volume supports.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''Use to override the device's volume size.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''Use to override the device's volume type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines block device mappings for the instance used to configure your image.

            :param device_name: The device to which these mappings apply.
            :param ebs: Use to manage Amazon EBS-specific configuration for this mapping.
            :param no_device: Use to remove a mapping from the base image.
            :param virtual_name: Use to manage instance ephemeral devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                instance_block_device_mapping_property = imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dcd6756cda3d99b28dbf0f3b48705f560c200b87b369d494233849fe9edf7710)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The device to which these mappings apply.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''Use to manage Amazon EBS-specific configuration for this mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''Use to remove a mapping from the base image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''Use to manage instance ephemeral devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_device_mappings": "blockDeviceMappings",
            "image": "image",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnContainerRecipe.InstanceBlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            image: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a custom base AMI and block device mapping configurations of an instance used for building and testing container images.

            :param block_device_mappings: Defines the block devices to attach for building an instance from this Image Builder AMI.
            :param image: The AMI ID to use as the base image for a container build and test instance. If not specified, Image Builder will use the appropriate ECS-optimized AMI as a base image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                instance_configuration_property = imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                    block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                            delete_on_termination=False,
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            snapshot_id="snapshotId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    image="image"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3c9338383aa0077f1ce17108486e870db44b64a72153672e1109d54992e8d1f)
                check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_device_mappings is not None:
                self._values["block_device_mappings"] = block_device_mappings
            if image is not None:
                self._values["image"] = image

        @builtins.property
        def block_device_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]]:
            '''Defines the block devices to attach for building an instance from this Image Builder AMI.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-blockdevicemappings
            '''
            result = self._values.get("block_device_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]], result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''The AMI ID to use as the base image for a container build and test instance.

            If not specified, Image Builder will use the appropriate ECS-optimized AMI as a base image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_name": "repositoryName", "service": "service"},
    )
    class TargetContainerRepositoryProperty:
        def __init__(
            self,
            *,
            repository_name: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The container repository where the output container image is stored.

            :param repository_name: The name of the container repository where the output container image is stored. This name is prefixed by the repository location.
            :param service: Specifies the service in which this image was registered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                target_container_repository_property = imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7cff2524a5b8bb1cdf483f9a7672b40d72843cb70480fbbedd8ea93fd5db930d)
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
                check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if repository_name is not None:
                self._values["repository_name"] = repository_name
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository where the output container image is stored.

            This name is prefixed by the repository location.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''Specifies the service in which this image was registered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetContainerRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "container_type": "containerType",
        "name": "name",
        "parent_image": "parentImage",
        "target_repository": "targetRepository",
        "version": "version",
        "description": "description",
        "dockerfile_template_data": "dockerfileTemplateData",
        "dockerfile_template_uri": "dockerfileTemplateUri",
        "image_os_version_override": "imageOsVersionOverride",
        "instance_configuration": "instanceConfiguration",
        "kms_key_id": "kmsKeyId",
        "platform_override": "platformOverride",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnContainerRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainerRecipe``.

        :param components: Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
        :param container_type: Specifies the type of container, such as Docker.
        :param name: The name of the container recipe.
        :param parent_image: The base image for the container recipe.
        :param target_repository: The destination repository for the container image.
        :param version: The semantic version of the container recipe. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01. *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
        :param description: The description of the container recipe.
        :param dockerfile_template_data: Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        :param dockerfile_template_uri: The S3 URI for the Dockerfile that will be used to build your container image.
        :param image_os_version_override: Specifies the operating system version for the base image.
        :param instance_configuration: A group of options that can be used to configure an instance for building and testing container images.
        :param kms_key_id: Identifies which KMS key is used to encrypt the container image for distribution to the target Region.
        :param platform_override: Specifies the operating system platform when you use a custom base image.
        :param tags: Tags that are attached to the container recipe.
        :param working_directory: The working directory for use during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_container_recipe_props = imagebuilder.CfnContainerRecipeProps(
                components=[imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )],
                container_type="containerType",
                name="name",
                parent_image="parentImage",
                target_repository=imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                ),
                version="version",
            
                # the properties below are optional
                description="description",
                dockerfile_template_data="dockerfileTemplateData",
                dockerfile_template_uri="dockerfileTemplateUri",
                image_os_version_override="imageOsVersionOverride",
                instance_configuration=imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                    block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                            delete_on_termination=False,
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            snapshot_id="snapshotId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    image="image"
                ),
                kms_key_id="kmsKeyId",
                platform_override="platformOverride",
                tags={
                    "tags_key": "tags"
                },
                working_directory="workingDirectory"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4888e7a655d1e4ca650d34565aaf0a32c53e99340c2dba8ce9191f415b67cb)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument container_type", value=container_type, expected_type=type_hints["container_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument target_repository", value=target_repository, expected_type=type_hints["target_repository"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dockerfile_template_data", value=dockerfile_template_data, expected_type=type_hints["dockerfile_template_data"])
            check_type(argname="argument dockerfile_template_uri", value=dockerfile_template_uri, expected_type=type_hints["dockerfile_template_uri"])
            check_type(argname="argument image_os_version_override", value=image_os_version_override, expected_type=type_hints["image_os_version_override"])
            check_type(argname="argument instance_configuration", value=instance_configuration, expected_type=type_hints["instance_configuration"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument platform_override", value=platform_override, expected_type=type_hints["platform_override"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "components": components,
            "container_type": container_type,
            "name": name,
            "parent_image": parent_image,
            "target_repository": target_repository,
            "version": version,
        }
        if description is not None:
            self._values["description"] = description
        if dockerfile_template_data is not None:
            self._values["dockerfile_template_data"] = dockerfile_template_data
        if dockerfile_template_uri is not None:
            self._values["dockerfile_template_uri"] = dockerfile_template_uri
        if image_os_version_override is not None:
            self._values["image_os_version_override"] = image_os_version_override
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if platform_override is not None:
            self._values["platform_override"] = platform_override
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.ComponentConfigurationProperty]]]:
        '''Build and test components that are included in the container recipe.

        Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.ComponentConfigurationProperty]]], result)

    @builtins.property
    def container_type(self) -> builtins.str:
        '''Specifies the type of container, such as Docker.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype
        '''
        result = self._values.get("container_type")
        assert result is not None, "Required property 'container_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''The base image for the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_repository(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty]:
        '''The destination repository for the container image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository
        '''
        result = self._values.get("target_repository")
        assert result is not None, "Required property 'target_repository' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The semantic version of the container recipe.

        .. epigraph::

           The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them.

           *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

           *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

           *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside.

        The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata
        '''
        result = self._values.get("dockerfile_template_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI for the Dockerfile that will be used to build your container image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri
        '''
        result = self._values.get("dockerfile_template_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system version for the base image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride
        '''
        result = self._values.get("image_os_version_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]]:
        '''A group of options that can be used to configure an instance for building and testing container images.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifies which KMS key is used to encrypt the container image for distribution to the target Region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system platform when you use a custom base image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride
        '''
        result = self._values.get("platform_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags that are attached to the container recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory for use during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnDistributionConfiguration(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration",
):
    '''A CloudFormation ``AWS::ImageBuilder::DistributionConfiguration``.

    A distribution configuration allows you to specify the name and description of your output AMI, authorize other AWS account s to launch the AMI, and replicate the AMI to other AWS Regions . It also allows you to export the AMI to Amazon S3 .

    :cloudformationResource: AWS::ImageBuilder::DistributionConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        # ami_distribution_configuration: Any
        # container_distribution_configuration: Any
        
        cfn_distribution_configuration = imagebuilder.CfnDistributionConfiguration(self, "MyCfnDistributionConfiguration",
            distributions=[imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                region="region",
        
                # the properties below are optional
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                    account_id="accountId",
                    enabled=False,
                    launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        launch_template_version="launchTemplateVersion"
                    ),
                    max_parallel_launches=123,
                    snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                        target_resource_count=123
                    )
                )],
                launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                    account_id="accountId",
                    launch_template_id="launchTemplateId",
                    set_default_version=False
                )],
                license_configuration_arns=["licenseConfigurationArns"]
            )],
            name="name",
        
            # the properties below are optional
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        distributions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.DistributionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::DistributionConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param distributions: The distributions of this distribution configuration formatted as an array of Distribution objects.
        :param name: The name of this distribution configuration.
        :param description: The description of this distribution configuration.
        :param tags: The tags of this distribution configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e59228d22129378d0454490bc22550c10d18ff3eed735ce2b123101693bb81c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDistributionConfigurationProps(
            distributions=distributions, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ca2af01b9dd1d7e6de6c8aa26c4f8a8523399ce7e864989e1011355f3d36ac)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79482d837d799aea2a260d3de49faec1ed9e9fdd92a53207ae2b0de94f31e4c5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of this distribution configuration.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the distribution configuration.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="distributions")
    def distributions(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]]:
        '''The distributions of this distribution configuration formatted as an array of Distribution objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]], jsii.get(self, "distributions"))

    @distributions.setter
    def distributions(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b81ed9c00021fe92738311deb5b887021e8f98696e4b7c1e71ce62cf75bf02d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f0863d3c30e56e5c244cb383bd34cee53611455cbf55d78de598244a4f3e69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c379868868cd3601f6c36eba08f5dda5cdda5f512a8d6870036b507a3750267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.AmiDistributionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ami_tags": "amiTags",
            "description": "description",
            "kms_key_id": "kmsKeyId",
            "launch_permission_configuration": "launchPermissionConfiguration",
            "name": "name",
            "target_account_ids": "targetAccountIds",
        },
    )
    class AmiDistributionConfigurationProperty:
        def __init__(
            self,
            *,
            ami_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            description: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            launch_permission_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.LaunchPermissionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Define and configure the output AMIs of the pipeline.

            :param ami_tags: The tags to apply to AMIs distributed to this Region.
            :param description: The description of the AMI distribution configuration. Minimum and maximum length are in characters.
            :param kms_key_id: The KMS key identifier used to encrypt the distributed image.
            :param launch_permission_configuration: Launch permissions can be used to configure which AWS account s can use the AMI to launch instances.
            :param name: The name of the output AMI.
            :param target_account_ids: The ID of an account to which you want to distribute an image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                ami_distribution_configuration_property = imagebuilder.CfnDistributionConfiguration.AmiDistributionConfigurationProperty(
                    ami_tags={
                        "ami_tags_key": "amiTags"
                    },
                    description="description",
                    kms_key_id="kmsKeyId",
                    launch_permission_configuration=imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty(
                        organizational_unit_arns=["organizationalUnitArns"],
                        organization_arns=["organizationArns"],
                        user_groups=["userGroups"],
                        user_ids=["userIds"]
                    ),
                    name="name",
                    target_account_ids=["targetAccountIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4696db19cc706b6b52ea0766fc521fe4ba2ad1d08dcb804cbfb276dec9e786d8)
                check_type(argname="argument ami_tags", value=ami_tags, expected_type=type_hints["ami_tags"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument launch_permission_configuration", value=launch_permission_configuration, expected_type=type_hints["launch_permission_configuration"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument target_account_ids", value=target_account_ids, expected_type=type_hints["target_account_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ami_tags is not None:
                self._values["ami_tags"] = ami_tags
            if description is not None:
                self._values["description"] = description
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if launch_permission_configuration is not None:
                self._values["launch_permission_configuration"] = launch_permission_configuration
            if name is not None:
                self._values["name"] = name
            if target_account_ids is not None:
                self._values["target_account_ids"] = target_account_ids

        @builtins.property
        def ami_tags(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''The tags to apply to AMIs distributed to this Region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags
            '''
            result = self._values.get("ami_tags")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the AMI distribution configuration.

            Minimum and maximum length are in characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key identifier used to encrypt the distributed image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_permission_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.LaunchPermissionConfigurationProperty"]]:
            '''Launch permissions can be used to configure which AWS account s can use the AMI to launch instances.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration
            '''
            result = self._values.get("launch_permission_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.LaunchPermissionConfigurationProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the output AMI.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ID of an account to which you want to distribute an image.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids
            '''
            result = self._values.get("target_account_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmiDistributionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.ContainerDistributionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "description": "description",
            "target_repository": "targetRepository",
        },
    )
    class ContainerDistributionConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            target_repository: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.TargetContainerRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container distribution settings for encryption, licensing, and sharing in a specific Region.

            :param container_tags: Tags that are attached to the container distribution configuration.
            :param description: The description of the container distribution configuration.
            :param target_repository: The destination repository for the container distribution configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                container_distribution_configuration_property = imagebuilder.CfnDistributionConfiguration.ContainerDistributionConfigurationProperty(
                    container_tags=["containerTags"],
                    description="description",
                    target_repository=imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty(
                        repository_name="repositoryName",
                        service="service"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0b647223a2fcfc4fe6a9e86932938634c98cf68b5c66e1d788f7ee119b2b8f3)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument target_repository", value=target_repository, expected_type=type_hints["target_repository"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if description is not None:
                self._values["description"] = description
            if target_repository is not None:
                self._values["target_repository"] = target_repository

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Tags that are attached to the container distribution configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the container distribution configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_repository(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.TargetContainerRepositoryProperty"]]:
            '''The destination repository for the container distribution configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository
            '''
            result = self._values.get("target_repository")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.TargetContainerRepositoryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDistributionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.DistributionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "ami_distribution_configuration": "amiDistributionConfiguration",
            "container_distribution_configuration": "containerDistributionConfiguration",
            "fast_launch_configurations": "fastLaunchConfigurations",
            "launch_template_configurations": "launchTemplateConfigurations",
            "license_configuration_arns": "licenseConfigurationArns",
        },
    )
    class DistributionProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            ami_distribution_configuration: typing.Any = None,
            container_distribution_configuration: typing.Any = None,
            fast_launch_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.FastLaunchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            launch_template_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.LaunchTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The distribution configuration distribution defines the settings for a specific Region in the Distribution Configuration.

            You must specify whether the distribution is for an AMI or a container image. To do so, include exactly one of the following data types for your distribution:

            - amiDistributionConfiguration
            - containerDistributionConfiguration

            :param region: The target Region for the Distribution Configuration. For example, ``eu-west-1`` .
            :param ami_distribution_configuration: The specific AMI settings, such as launch permissions and AMI tags. For details, see example schema below.
            :param container_distribution_configuration: Container distribution settings for encryption, licensing, and sharing in a specific Region. For details, see example schema below.
            :param fast_launch_configurations: ``CfnDistributionConfiguration.DistributionProperty.FastLaunchConfigurations``.
            :param launch_template_configurations: A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.
            :param license_configuration_arns: The License Manager Configuration to associate with the AMI in the specified Region. For more information, see the `LicenseConfiguration API <https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfiguration.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                # ami_distribution_configuration: Any
                # container_distribution_configuration: Any
                
                distribution_property = imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                    region="region",
                
                    # the properties below are optional
                    ami_distribution_configuration=ami_distribution_configuration,
                    container_distribution_configuration=container_distribution_configuration,
                    fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                        account_id="accountId",
                        enabled=False,
                        launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                            launch_template_id="launchTemplateId",
                            launch_template_name="launchTemplateName",
                            launch_template_version="launchTemplateVersion"
                        ),
                        max_parallel_launches=123,
                        snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                            target_resource_count=123
                        )
                    )],
                    launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                        account_id="accountId",
                        launch_template_id="launchTemplateId",
                        set_default_version=False
                    )],
                    license_configuration_arns=["licenseConfigurationArns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3d9a91ff83814c0c21dd4b48f701bf94a26acff8eb882501718f6efd71f088b)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument ami_distribution_configuration", value=ami_distribution_configuration, expected_type=type_hints["ami_distribution_configuration"])
                check_type(argname="argument container_distribution_configuration", value=container_distribution_configuration, expected_type=type_hints["container_distribution_configuration"])
                check_type(argname="argument fast_launch_configurations", value=fast_launch_configurations, expected_type=type_hints["fast_launch_configurations"])
                check_type(argname="argument launch_template_configurations", value=launch_template_configurations, expected_type=type_hints["launch_template_configurations"])
                check_type(argname="argument license_configuration_arns", value=license_configuration_arns, expected_type=type_hints["license_configuration_arns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if ami_distribution_configuration is not None:
                self._values["ami_distribution_configuration"] = ami_distribution_configuration
            if container_distribution_configuration is not None:
                self._values["container_distribution_configuration"] = container_distribution_configuration
            if fast_launch_configurations is not None:
                self._values["fast_launch_configurations"] = fast_launch_configurations
            if launch_template_configurations is not None:
                self._values["launch_template_configurations"] = launch_template_configurations
            if license_configuration_arns is not None:
                self._values["license_configuration_arns"] = license_configuration_arns

        @builtins.property
        def region(self) -> builtins.str:
            '''The target Region for the Distribution Configuration.

            For example, ``eu-west-1`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ami_distribution_configuration(self) -> typing.Any:
            '''The specific AMI settings, such as launch permissions and AMI tags.

            For details, see example schema below.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration
            '''
            result = self._values.get("ami_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def container_distribution_configuration(self) -> typing.Any:
            '''Container distribution settings for encryption, licensing, and sharing in a specific Region.

            For details, see example schema below.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration
            '''
            result = self._values.get("container_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def fast_launch_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchConfigurationProperty"]]]]:
            '''``CfnDistributionConfiguration.DistributionProperty.FastLaunchConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations
            '''
            result = self._values.get("fast_launch_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchConfigurationProperty"]]]], result)

        @builtins.property
        def launch_template_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]]:
            '''A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations
            '''
            result = self._values.get("launch_template_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]], result)

        @builtins.property
        def license_configuration_arns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The License Manager Configuration to associate with the AMI in the specified Region.

            For more information, see the `LicenseConfiguration API <https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfiguration.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns
            '''
            result = self._values.get("license_configuration_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DistributionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "enabled": "enabled",
            "launch_template": "launchTemplate",
            "max_parallel_launches": "maxParallelLaunches",
            "snapshot_configuration": "snapshotConfiguration",
        },
    )
    class FastLaunchConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            launch_template: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_parallel_launches: typing.Optional[jsii.Number] = None,
            snapshot_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param account_id: ``CfnDistributionConfiguration.FastLaunchConfigurationProperty.AccountId``.
            :param enabled: ``CfnDistributionConfiguration.FastLaunchConfigurationProperty.Enabled``.
            :param launch_template: ``CfnDistributionConfiguration.FastLaunchConfigurationProperty.LaunchTemplate``.
            :param max_parallel_launches: ``CfnDistributionConfiguration.FastLaunchConfigurationProperty.MaxParallelLaunches``.
            :param snapshot_configuration: ``CfnDistributionConfiguration.FastLaunchConfigurationProperty.SnapshotConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                fast_launch_configuration_property = imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                    account_id="accountId",
                    enabled=False,
                    launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        launch_template_version="launchTemplateVersion"
                    ),
                    max_parallel_launches=123,
                    snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                        target_resource_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0b1dab882f80ac23f45f27c3fe430f603469c6fe9ba2ded7d29995b86d4fbb1)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
                check_type(argname="argument max_parallel_launches", value=max_parallel_launches, expected_type=type_hints["max_parallel_launches"])
                check_type(argname="argument snapshot_configuration", value=snapshot_configuration, expected_type=type_hints["snapshot_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if enabled is not None:
                self._values["enabled"] = enabled
            if launch_template is not None:
                self._values["launch_template"] = launch_template
            if max_parallel_launches is not None:
                self._values["max_parallel_launches"] = max_parallel_launches
            if snapshot_configuration is not None:
                self._values["snapshot_configuration"] = snapshot_configuration

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.FastLaunchConfigurationProperty.AccountId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``CfnDistributionConfiguration.FastLaunchConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def launch_template(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty"]]:
            '''``CfnDistributionConfiguration.FastLaunchConfigurationProperty.LaunchTemplate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate
            '''
            result = self._values.get("launch_template")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty"]], result)

        @builtins.property
        def max_parallel_launches(self) -> typing.Optional[jsii.Number]:
            '''``CfnDistributionConfiguration.FastLaunchConfigurationProperty.MaxParallelLaunches``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches
            '''
            result = self._values.get("max_parallel_launches")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def snapshot_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty"]]:
            '''``CfnDistributionConfiguration.FastLaunchConfigurationProperty.SnapshotConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration
            '''
            result = self._values.get("snapshot_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "launch_template_version": "launchTemplateVersion",
        },
    )
    class FastLaunchLaunchTemplateSpecificationProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            launch_template_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param launch_template_id: ``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateId``.
            :param launch_template_name: ``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateName``.
            :param launch_template_version: ``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                fast_launch_launch_template_specification_property = imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    launch_template_version="launchTemplateVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51870bc75f77bdcb19a86273ba148f9679dd280e30a78c1da0991fc7de122b54)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument launch_template_version", value=launch_template_version, expected_type=type_hints["launch_template_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if launch_template_version is not None:
                self._values["launch_template_version"] = launch_template_version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty.LaunchTemplateVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion
            '''
            result = self._values.get("launch_template_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchLaunchTemplateSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_resource_count": "targetResourceCount"},
    )
    class FastLaunchSnapshotConfigurationProperty:
        def __init__(
            self,
            *,
            target_resource_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param target_resource_count: ``CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty.TargetResourceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                fast_launch_snapshot_configuration_property = imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                    target_resource_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac7a7b037906b48fe4178fb30cc1f6546f7d733df567eb99dfdd84f58ae7cb20)
                check_type(argname="argument target_resource_count", value=target_resource_count, expected_type=type_hints["target_resource_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if target_resource_count is not None:
                self._values["target_resource_count"] = target_resource_count

        @builtins.property
        def target_resource_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty.TargetResourceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount
            '''
            result = self._values.get("target_resource_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchSnapshotConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organizational_unit_arns": "organizationalUnitArns",
            "organization_arns": "organizationArns",
            "user_groups": "userGroups",
            "user_ids": "userIds",
        },
    )
    class LaunchPermissionConfigurationProperty:
        def __init__(
            self,
            *,
            organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes the configuration for a launch permission.

            The launch permission modification request is sent to the `Amazon EC2 ModifyImageAttribute <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html>`_ API on behalf of the user for each Region they have selected to distribute the AMI. To make an AMI public, set the launch permission authorized accounts to ``all`` . See the examples for making an AMI public at `Amazon EC2 ModifyImageAttribute <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html>`_ .

            :param organizational_unit_arns: The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for AWS Organizations , see `AWS Organizations terminology and concepts <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html>`_ .
            :param organization_arns: The ARN for an AWS Organization that you want to share your AMI with. For more information, see `What is AWS Organizations ? <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`_ .
            :param user_groups: The name of the group.
            :param user_ids: The AWS account ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                launch_permission_configuration_property = imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty(
                    organizational_unit_arns=["organizationalUnitArns"],
                    organization_arns=["organizationArns"],
                    user_groups=["userGroups"],
                    user_ids=["userIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6adceb2d6e04f430332f3a150aa90805998e7479b29a99011d8f99ab7bb0ea0c)
                check_type(argname="argument organizational_unit_arns", value=organizational_unit_arns, expected_type=type_hints["organizational_unit_arns"])
                check_type(argname="argument organization_arns", value=organization_arns, expected_type=type_hints["organization_arns"])
                check_type(argname="argument user_groups", value=user_groups, expected_type=type_hints["user_groups"])
                check_type(argname="argument user_ids", value=user_ids, expected_type=type_hints["user_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if organizational_unit_arns is not None:
                self._values["organizational_unit_arns"] = organizational_unit_arns
            if organization_arns is not None:
                self._values["organization_arns"] = organization_arns
            if user_groups is not None:
                self._values["user_groups"] = user_groups
            if user_ids is not None:
                self._values["user_ids"] = user_ids

        @builtins.property
        def organizational_unit_arns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with.

            For more information about key concepts for AWS Organizations , see `AWS Organizations terminology and concepts <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns
            '''
            result = self._values.get("organizational_unit_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organization_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ARN for an AWS Organization that you want to share your AMI with.

            For more information, see `What is AWS Organizations ? <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns
            '''
            result = self._values.get("organization_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The name of the group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups
            '''
            result = self._values.get("user_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The AWS account ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids
            '''
            result = self._values.get("user_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchPermissionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "launch_template_id": "launchTemplateId",
            "set_default_version": "setDefaultVersion",
        },
    )
    class LaunchTemplateConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            launch_template_id: typing.Optional[builtins.str] = None,
            set_default_version: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Identifies an Amazon EC2 launch template to use for a specific account.

            :param account_id: The account ID that this configuration applies to.
            :param launch_template_id: Identifies the Amazon EC2 launch template to use.
            :param set_default_version: Set the specified Amazon EC2 launch template as the default launch template for the specified account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                launch_template_configuration_property = imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                    account_id="accountId",
                    launch_template_id="launchTemplateId",
                    set_default_version=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bde3e3da84b4686f1fbf271e67a48e29a8c7328b67bc83bed3136d2da06285bb)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument set_default_version", value=set_default_version, expected_type=type_hints["set_default_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if set_default_version is not None:
                self._values["set_default_version"] = set_default_version

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The account ID that this configuration applies to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''Identifies the Amazon EC2 launch template to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_default_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Set the specified Amazon EC2 launch template as the default launch template for the specified account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-setdefaultversion
            '''
            result = self._values.get("set_default_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_name": "repositoryName", "service": "service"},
    )
    class TargetContainerRepositoryProperty:
        def __init__(
            self,
            *,
            repository_name: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The container repository where the output container image is stored.

            :param repository_name: The name of the container repository where the output container image is stored. This name is prefixed by the repository location.
            :param service: Specifies the service in which this image was registered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                target_container_repository_property = imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c246cba6edbb82685e2d879ac3d9f14e4f8eae6efb38137f6dde1f30bbabbfda)
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
                check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if repository_name is not None:
                self._values["repository_name"] = repository_name
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository where the output container image is stored.

            This name is prefixed by the repository location.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''Specifies the service in which this image was registered.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetContainerRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "distributions": "distributions",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDistributionConfigurationProps:
    def __init__(
        self,
        *,
        distributions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDistributionConfiguration``.

        :param distributions: The distributions of this distribution configuration formatted as an array of Distribution objects.
        :param name: The name of this distribution configuration.
        :param description: The description of this distribution configuration.
        :param tags: The tags of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            # ami_distribution_configuration: Any
            # container_distribution_configuration: Any
            
            cfn_distribution_configuration_props = imagebuilder.CfnDistributionConfigurationProps(
                distributions=[imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                    region="region",
            
                    # the properties below are optional
                    ami_distribution_configuration=ami_distribution_configuration,
                    container_distribution_configuration=container_distribution_configuration,
                    fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                        account_id="accountId",
                        enabled=False,
                        launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                            launch_template_id="launchTemplateId",
                            launch_template_name="launchTemplateName",
                            launch_template_version="launchTemplateVersion"
                        ),
                        max_parallel_launches=123,
                        snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                            target_resource_count=123
                        )
                    )],
                    launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                        account_id="accountId",
                        launch_template_id="launchTemplateId",
                        set_default_version=False
                    )],
                    license_configuration_arns=["licenseConfigurationArns"]
                )],
                name="name",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbb27b2bb605e8a73fa5d268ee917cbaa10c165393c05714c1d0b65435906284)
            check_type(argname="argument distributions", value=distributions, expected_type=type_hints["distributions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distributions": distributions,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def distributions(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDistributionConfiguration.DistributionProperty]]]:
        '''The distributions of this distribution configuration formatted as an array of Distribution objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
        '''
        result = self._values.get("distributions")
        assert result is not None, "Required property 'distributions' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDistributionConfiguration.DistributionProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDistributionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnImage(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImage",
):
    '''A CloudFormation ``AWS::ImageBuilder::Image``.

    An image build version. An image is a customized, secure, and up-to-date “golden” server image that is pre-installed and pre-configured with software and settings to meet specific IT standards.

    :cloudformationResource: AWS::ImageBuilder::Image
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_image = imagebuilder.CfnImage(self, "MyCfnImage",
            infrastructure_configuration_arn="infrastructureConfigurationArn",
        
            # the properties below are optional
            container_recipe_arn="containerRecipeArn",
            distribution_configuration_arn="distributionConfigurationArn",
            enhanced_image_metadata_enabled=False,
            image_recipe_arn="imageRecipeArn",
            image_scanning_configuration=imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                ),
                image_scanning_enabled=False
            ),
            image_tests_configuration=imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                image_tests_enabled=False,
                timeout_minutes=123
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImage.ImageScanningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImage.ImageTestsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::Image``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration.
        :param enhanced_image_metadata_enabled: Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe.
        :param image_scanning_configuration: ``AWS::ImageBuilder::Image.ImageScanningConfiguration``.
        :param image_tests_configuration: The configuration settings for your image test components, which includes a toggle that allows you to turn off tests, and a timeout setting.
        :param tags: The tags of the image.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a4d58d2d1e97b7653ee4cb81132cb037fabb890b3acf1ea6334231ee6be2da9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImageProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            container_recipe_arn=container_recipe_arn,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            image_recipe_arn=image_recipe_arn,
            image_scanning_configuration=image_scanning_configuration,
            image_tests_configuration=image_tests_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca54ec9e2922745d7891670afdb1ef808fe5b5b9aaa4a5861692622feb62f6a7)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1021653e5dbff14f635d082276fcead96b79c7911a0b020365dcf79ef850e84e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the image.

        For example, ``arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrImageId")
    def attr_image_id(self) -> builtins.str:
        '''Returns the AMI ID of the Amazon EC2 AMI in the Region in which you are using Image Builder.

        Values are returned only for AMIs, and not for container images.

        :cloudformationAttribute: ImageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageId"))

    @builtins.property
    @jsii.member(jsii_name="attrImageUri")
    def attr_image_uri(self) -> builtins.str:
        '''Returns a list of URIs for container images created in the context Region.

        Values are returned only for container images, and not for AMIs.

        :cloudformationAttribute: ImageUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageUri"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the image.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags of the image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ccaacc49e138556d172f69bef028686df9391836446a8ba37e4accd93a15dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e59c24ae255477a427c27fb629b12624cf6335721024ce364f650f7ebc00804e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87b8111920fb2b0ab83f5cdb22c77bd1216f9dd969ad8a3040728a90408b4123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9df26b0360093576ce1316ca7acb8611242e5acc171deee61d02a84768960317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09756416b511ca613efb6053df1b66d938d81ecdb78031d21884a7318bb29539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageScanningConfigurationProperty"]]:
        '''``AWS::ImageBuilder::Image.ImageScanningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagescanningconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageScanningConfigurationProperty"]], jsii.get(self, "imageScanningConfiguration"))

    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageScanningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__721f9bae295d919178378c0b726aaa948eb6d06c8287de066afc437a8f4e723b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageScanningConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]]:
        '''The configuration settings for your image test components, which includes a toggle that allows you to turn off tests, and a timeout setting.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48be2c53dd08eeb50acebcb9d409abf0911e460d41f289304be4b10889e9cf6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTestsConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImage.EcrConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "repository_name": "repositoryName",
        },
    )
    class EcrConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            repository_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_tags: ``CfnImage.EcrConfigurationProperty.ContainerTags``.
            :param repository_name: ``CfnImage.EcrConfigurationProperty.RepositoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                ecr_configuration_property = imagebuilder.CfnImage.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe92999e4f6a2192fb4b24e66651f95d96472f26908191a1310b3e0d1839ba8c)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if repository_name is not None:
                self._values["repository_name"] = repository_name

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnImage.EcrConfigurationProperty.ContainerTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''``CfnImage.EcrConfigurationProperty.RepositoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcrConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImage.ImageScanningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_configuration": "ecrConfiguration",
            "image_scanning_enabled": "imageScanningEnabled",
        },
    )
    class ImageScanningConfigurationProperty:
        def __init__(
            self,
            *,
            ecr_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImage.EcrConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''
            :param ecr_configuration: ``CfnImage.ImageScanningConfigurationProperty.EcrConfiguration``.
            :param image_scanning_enabled: ``CfnImage.ImageScanningConfigurationProperty.ImageScanningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                image_scanning_configuration_property = imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cda2321d2389bded10a19240792fca4f703af45d34e988273106b53d92ac350e)
                check_type(argname="argument ecr_configuration", value=ecr_configuration, expected_type=type_hints["ecr_configuration"])
                check_type(argname="argument image_scanning_enabled", value=image_scanning_enabled, expected_type=type_hints["image_scanning_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_configuration is not None:
                self._values["ecr_configuration"] = ecr_configuration
            if image_scanning_enabled is not None:
                self._values["image_scanning_enabled"] = image_scanning_enabled

        @builtins.property
        def ecr_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.EcrConfigurationProperty"]]:
            '''``CfnImage.ImageScanningConfigurationProperty.EcrConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration
            '''
            result = self._values.get("ecr_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImage.EcrConfigurationProperty"]], result)

        @builtins.property
        def image_scanning_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``CfnImage.ImageScanningConfigurationProperty.ImageScanningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled
            '''
            result = self._values.get("image_scanning_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageScanningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImage.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''When you create an image or container recipe with Image Builder , you can add the build or test components that are used to create the final image.

            You must have at least one build component to create a recipe, but test components are not required. If you have added tests, they run after the image is created, to ensure that the target image is functional and can be used reliably for launching Amazon EC2 instances.

            :param image_tests_enabled: Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
            :param timeout_minutes: The maximum time in minutes that tests are permitted to run. .. epigraph:: The timeoutMinutes attribute is not currently active. This value is ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                image_tests_configuration_property = imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c49401811b71b69583348fed8a96e029e152a2f4f7595eccd7ebb26c4ead602)
                check_type(argname="argument image_tests_enabled", value=image_tests_enabled, expected_type=type_hints["image_tests_enabled"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Determines if tests should run after building the image.

            Image Builder defaults to enable tests to run following the image build, before image distribution.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum time in minutes that tests are permitted to run.

            .. epigraph::

               The timeoutMinutes attribute is not currently active. This value is ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnImagePipeline(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline",
):
    '''A CloudFormation ``AWS::ImageBuilder::ImagePipeline``.

    An image pipeline is the automation configuration for building secure OS images on AWS . The Image Builder image pipeline is associated with an image recipe that defines the build, validation, and test phases for an image build lifecycle. An image pipeline can be associated with an infrastructure configuration that defines where your image is built. You can define attributes, such as instance type, subnets, security groups, logging, and other infrastructure-related configurations. You can also associate your image pipeline with a distribution configuration to define how you would like to deploy your image.

    :cloudformationResource: AWS::ImageBuilder::ImagePipeline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_image_pipeline = imagebuilder.CfnImagePipeline(self, "MyCfnImagePipeline",
            infrastructure_configuration_arn="infrastructureConfigurationArn",
            name="name",
        
            # the properties below are optional
            container_recipe_arn="containerRecipeArn",
            description="description",
            distribution_configuration_arn="distributionConfigurationArn",
            enhanced_image_metadata_enabled=False,
            image_recipe_arn="imageRecipeArn",
            image_scanning_configuration=imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                ),
                image_scanning_enabled=False
            ),
            image_tests_configuration=imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                image_tests_enabled=False,
                timeout_minutes=123
            ),
            schedule=imagebuilder.CfnImagePipeline.ScheduleProperty(
                pipeline_execution_start_condition="pipelineExecutionStartCondition",
                schedule_expression="scheduleExpression"
            ),
            status="status",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImagePipeline.ImageScanningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImagePipeline.ImageTestsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImagePipeline.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ImagePipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param name: The name of the image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param description: The description of this image pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
        :param image_scanning_configuration: ``AWS::ImageBuilder::ImagePipeline.ImageScanningConfiguration``.
        :param image_tests_configuration: The configuration of the image tests that run after image creation to ensure the quality of the image that was created.
        :param schedule: The schedule of the image pipeline. A schedule configures how often and when a pipeline automatically creates a new image.
        :param status: The status of the image pipeline.
        :param tags: The tags of this image pipeline.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234e0e6de34d31d2f9ae6047d04d2aee4dadfd493797dafd265219fd64acb7f3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImagePipelineProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            name=name,
            container_recipe_arn=container_recipe_arn,
            description=description,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            image_recipe_arn=image_recipe_arn,
            image_scanning_configuration=image_scanning_configuration,
            image_tests_configuration=image_tests_configuration,
            schedule=schedule,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bf84e55f608e09a7a48ccf48088ba07955cc8d3605bc70b3ebcccff54eea2f)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de8910077232fca1b7111bae85da6107bf6cfdf654a3f125078a59c13dc2328)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the image pipeline.

        For example, ``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the image pipeline.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags of this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24be75e5ae8530bc803c8e5ea3693d6f9727e01fb85472621709339866d06dab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c644ecbfe1a9842f0c0245e80067af982e8a297a161465f8d82e1186295da77e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ffff10d476a34a4911e6a76f042d26c1ac2d50ba99b29614178e86cfb3b23c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb9116215c6f2a98d3f7d9a7a372e4efb0d5ff62af91bf9527718f1f677d26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__574f2608825ab7901201716eaea2dee2169bd3fbe8356bfd85fe0d6c88c6f88a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.

        This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d6854e96c5fc6bd503a7f1f1f5482cf1a66111eaf1170bddf277e31ed82cb31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c498dc3589c2f4e29536fb6e805d86df1fffbb2d20afc6badf0b272f548fe09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageScanningConfigurationProperty"]]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageScanningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageScanningConfigurationProperty"]], jsii.get(self, "imageScanningConfiguration"))

    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageScanningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18fe40aa83d09d013f9efa595fa260a2485ebf0d70d6513ca7fcc66bdaa081f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageScanningConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]]:
        '''The configuration of the image tests that run after image creation to ensure the quality of the image that was created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e649780a7303b07fd34a2aafb520841950de60389e31baefdd56fcaaf021abf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTestsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ScheduleProperty"]]:
        '''The schedule of the image pipeline.

        A schedule configures how often and when a pipeline automatically creates a new image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.ScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882e20d97a475cc5dcd9bbd32c4a10256355c1d1033393c9088e95f81fdcee76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790c03b199485be80c0a4555ee6869329a87509968d856321e2440960103351a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.EcrConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "repository_name": "repositoryName",
        },
    )
    class EcrConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            repository_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param container_tags: ``CfnImagePipeline.EcrConfigurationProperty.ContainerTags``.
            :param repository_name: ``CfnImagePipeline.EcrConfigurationProperty.RepositoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                ecr_configuration_property = imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87b41d1e0c90971c4afe86176c8e4ea79bba53b3b08d32d94331cd82abddaa79)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if repository_name is not None:
                self._values["repository_name"] = repository_name

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnImagePipeline.EcrConfigurationProperty.ContainerTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''``CfnImagePipeline.EcrConfigurationProperty.RepositoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcrConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_configuration": "ecrConfiguration",
            "image_scanning_enabled": "imageScanningEnabled",
        },
    )
    class ImageScanningConfigurationProperty:
        def __init__(
            self,
            *,
            ecr_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImagePipeline.EcrConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''
            :param ecr_configuration: ``CfnImagePipeline.ImageScanningConfigurationProperty.EcrConfiguration``.
            :param image_scanning_enabled: ``CfnImagePipeline.ImageScanningConfigurationProperty.ImageScanningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                image_scanning_configuration_property = imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8682c78304b8b0eedfe960912d0f2abc62bd895b071b193ec735e2699f9e5e64)
                check_type(argname="argument ecr_configuration", value=ecr_configuration, expected_type=type_hints["ecr_configuration"])
                check_type(argname="argument image_scanning_enabled", value=image_scanning_enabled, expected_type=type_hints["image_scanning_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_configuration is not None:
                self._values["ecr_configuration"] = ecr_configuration
            if image_scanning_enabled is not None:
                self._values["image_scanning_enabled"] = image_scanning_enabled

        @builtins.property
        def ecr_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.EcrConfigurationProperty"]]:
            '''``CfnImagePipeline.ImageScanningConfigurationProperty.EcrConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration
            '''
            result = self._values.get("ecr_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImagePipeline.EcrConfigurationProperty"]], result)

        @builtins.property
        def image_scanning_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``CfnImagePipeline.ImageScanningConfigurationProperty.ImageScanningEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled
            '''
            result = self._values.get("image_scanning_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageScanningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''When you create an image or container recipe with Image Builder , you can add the build or test components that your image pipeline uses to create the final image.

            You must have at least one build component to create a recipe, but test components are not required. Your pipeline runs tests after it builds the image, to ensure that the target image is functional and can be used reliably for launching Amazon EC2 instances.

            :param image_tests_enabled: Defines if tests should be executed when building this image. For example, ``true`` or ``false`` .
            :param timeout_minutes: The maximum time in minutes that tests are permitted to run. .. epigraph:: The timeoutMinutes attribute is not currently active. This value is ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                image_tests_configuration_property = imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0210ff7e086b2ebef743ae79e24f2e3180202f9c87f2cca1699fcd79264ebea)
                check_type(argname="argument image_tests_enabled", value=image_tests_enabled, expected_type=type_hints["image_tests_enabled"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Defines if tests should be executed when building this image.

            For example, ``true`` or ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum time in minutes that tests are permitted to run.

            .. epigraph::

               The timeoutMinutes attribute is not currently active. This value is ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pipeline_execution_start_condition": "pipelineExecutionStartCondition",
            "schedule_expression": "scheduleExpression",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            pipeline_execution_start_condition: typing.Optional[builtins.str] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A schedule configures how often and when a pipeline will automatically create a new image.

            :param pipeline_execution_start_condition: The condition configures when the pipeline should trigger a new image build. When the ``pipelineExecutionStartCondition`` is set to ``EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`` , and you use semantic version filters on the base image or components in your image recipe, Image Builder will build a new image only when there are new versions of the image or components in your recipe that match the semantic version filter. When it is set to ``EXPRESSION_MATCH_ONLY`` , it will build a new image every time the CRON expression matches the current time. For semantic version syntax, see `CreateComponent <https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html>`_ in the *Image Builder API Reference* .
            :param schedule_expression: The cron expression determines how often EC2 Image Builder evaluates your ``pipelineExecutionStartCondition`` . For information on how to format a cron expression in Image Builder, see `Use cron expressions in EC2 Image Builder <https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                schedule_property = imagebuilder.CfnImagePipeline.ScheduleProperty(
                    pipeline_execution_start_condition="pipelineExecutionStartCondition",
                    schedule_expression="scheduleExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42c02f9eedf76d7fd90233ef5ec4319c34797859382f1d8a6bbdcf9968f7ebdb)
                check_type(argname="argument pipeline_execution_start_condition", value=pipeline_execution_start_condition, expected_type=type_hints["pipeline_execution_start_condition"])
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pipeline_execution_start_condition is not None:
                self._values["pipeline_execution_start_condition"] = pipeline_execution_start_condition
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression

        @builtins.property
        def pipeline_execution_start_condition(self) -> typing.Optional[builtins.str]:
            '''The condition configures when the pipeline should trigger a new image build.

            When the ``pipelineExecutionStartCondition`` is set to ``EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`` , and you use semantic version filters on the base image or components in your image recipe, Image Builder will build a new image only when there are new versions of the image or components in your recipe that match the semantic version filter. When it is set to ``EXPRESSION_MATCH_ONLY`` , it will build a new image every time the CRON expression matches the current time. For semantic version syntax, see `CreateComponent <https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html>`_ in the *Image Builder API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition
            '''
            result = self._values.get("pipeline_execution_start_condition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''The cron expression determines how often EC2 Image Builder evaluates your ``pipelineExecutionStartCondition`` .

            For information on how to format a cron expression in Image Builder, see `Use cron expressions in EC2 Image Builder <https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "name": "name",
        "container_recipe_arn": "containerRecipeArn",
        "description": "description",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "image_recipe_arn": "imageRecipeArn",
        "image_scanning_configuration": "imageScanningConfiguration",
        "image_tests_configuration": "imageTestsConfiguration",
        "schedule": "schedule",
        "status": "status",
        "tags": "tags",
    },
)
class CfnImagePipelineProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnImagePipeline``.

        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param name: The name of the image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param description: The description of this image pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
        :param image_scanning_configuration: ``AWS::ImageBuilder::ImagePipeline.ImageScanningConfiguration``.
        :param image_tests_configuration: The configuration of the image tests that run after image creation to ensure the quality of the image that was created.
        :param schedule: The schedule of the image pipeline. A schedule configures how often and when a pipeline automatically creates a new image.
        :param status: The status of the image pipeline.
        :param tags: The tags of this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_image_pipeline_props = imagebuilder.CfnImagePipelineProps(
                infrastructure_configuration_arn="infrastructureConfigurationArn",
                name="name",
            
                # the properties below are optional
                container_recipe_arn="containerRecipeArn",
                description="description",
                distribution_configuration_arn="distributionConfigurationArn",
                enhanced_image_metadata_enabled=False,
                image_recipe_arn="imageRecipeArn",
                image_scanning_configuration=imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                ),
                image_tests_configuration=imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                ),
                schedule=imagebuilder.CfnImagePipeline.ScheduleProperty(
                    pipeline_execution_start_condition="pipelineExecutionStartCondition",
                    schedule_expression="scheduleExpression"
                ),
                status="status",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731e06b83e0a9e23d94d5a9c2d78beffc4b74a93b0459548e3bd64feadf87868)
            check_type(argname="argument infrastructure_configuration_arn", value=infrastructure_configuration_arn, expected_type=type_hints["infrastructure_configuration_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument distribution_configuration_arn", value=distribution_configuration_arn, expected_type=type_hints["distribution_configuration_arn"])
            check_type(argname="argument enhanced_image_metadata_enabled", value=enhanced_image_metadata_enabled, expected_type=type_hints["enhanced_image_metadata_enabled"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument image_scanning_configuration", value=image_scanning_configuration, expected_type=type_hints["image_scanning_configuration"])
            check_type(argname="argument image_tests_configuration", value=image_tests_configuration, expected_type=type_hints["image_tests_configuration"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "name": name,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if description is not None:
            self._values["description"] = description
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_scanning_configuration is not None:
            self._values["image_scanning_configuration"] = image_scanning_configuration
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if schedule is not None:
            self._values["schedule"] = schedule
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.

        This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageScanningConfigurationProperty]]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageScanningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration
        '''
        result = self._values.get("image_scanning_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageScanningConfigurationProperty]], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]]:
        '''The configuration of the image tests that run after image creation to ensure the quality of the image that was created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ScheduleProperty]]:
        '''The schedule of the image pipeline.

        A schedule configures how often and when a pipeline automatically creates a new image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ScheduleProperty]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImagePipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "container_recipe_arn": "containerRecipeArn",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "image_recipe_arn": "imageRecipeArn",
        "image_scanning_configuration": "imageScanningConfiguration",
        "image_tests_configuration": "imageTestsConfiguration",
        "tags": "tags",
    },
)
class CfnImageProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnImage``.

        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration.
        :param enhanced_image_metadata_enabled: Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe.
        :param image_scanning_configuration: ``AWS::ImageBuilder::Image.ImageScanningConfiguration``.
        :param image_tests_configuration: The configuration settings for your image test components, which includes a toggle that allows you to turn off tests, and a timeout setting.
        :param tags: The tags of the image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_image_props = imagebuilder.CfnImageProps(
                infrastructure_configuration_arn="infrastructureConfigurationArn",
            
                # the properties below are optional
                container_recipe_arn="containerRecipeArn",
                distribution_configuration_arn="distributionConfigurationArn",
                enhanced_image_metadata_enabled=False,
                image_recipe_arn="imageRecipeArn",
                image_scanning_configuration=imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                ),
                image_tests_configuration=imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e92ddf7c746eba695cafe07b6c3e35f902ddc25d7a8fb518a8172a734e0cdad0)
            check_type(argname="argument infrastructure_configuration_arn", value=infrastructure_configuration_arn, expected_type=type_hints["infrastructure_configuration_arn"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
            check_type(argname="argument distribution_configuration_arn", value=distribution_configuration_arn, expected_type=type_hints["distribution_configuration_arn"])
            check_type(argname="argument enhanced_image_metadata_enabled", value=enhanced_image_metadata_enabled, expected_type=type_hints["enhanced_image_metadata_enabled"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument image_scanning_configuration", value=image_scanning_configuration, expected_type=type_hints["image_scanning_configuration"])
            check_type(argname="argument image_tests_configuration", value=image_tests_configuration, expected_type=type_hints["image_tests_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_scanning_configuration is not None:
            self._values["image_scanning_configuration"] = image_scanning_configuration
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageScanningConfigurationProperty]]:
        '''``AWS::ImageBuilder::Image.ImageScanningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagescanningconfiguration
        '''
        result = self._values.get("image_scanning_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageScanningConfigurationProperty]], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageTestsConfigurationProperty]]:
        '''The configuration settings for your image test components, which includes a toggle that allows you to turn off tests, and a timeout setting.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnImageRecipe(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe",
):
    '''A CloudFormation ``AWS::ImageBuilder::ImageRecipe``.

    An Image Builder image recipe is a document that defines the base image and the components to be applied to the base image to produce the desired configuration for the output image. You can use an image recipe to duplicate builds. Image Builder image recipes can be shared, branched, and edited using the console wizard, the AWS CLI , or the API. You can use image recipes with your version control software to maintain shareable versioned image recipes.

    :cloudformationResource: AWS::ImageBuilder::ImageRecipe
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_image_recipe = imagebuilder.CfnImageRecipe(self, "MyCfnImageRecipe",
            components=[imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                component_arn="componentArn",
                parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )]
            )],
            name="name",
            parent_image="parentImage",
            version="version",
        
            # the properties below are optional
            additional_instance_configuration=imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                    uninstall_after_build=False
                ),
                user_data_override="userDataOverride"
            ),
            block_device_mappings=[imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                device_name="deviceName",
                ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                ),
                no_device="noDevice",
                virtual_name="virtualName"
            )],
            description="description",
            tags={
                "tags_key": "tags"
            },
            working_directory="workingDirectory"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.ComponentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.AdditionalInstanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.InstanceBlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ImageRecipe``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param components: The components of the image recipe. Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.
        :param name: The name of the image recipe.
        :param parent_image: The parent image of the image recipe. The string must be either an Image ARN or an AMI ID.
        :param version: The semantic version of the image recipe.
        :param additional_instance_configuration: Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.
        :param block_device_mappings: The block device mappings to apply when creating images from this recipe.
        :param description: The description of the image recipe.
        :param tags: The tags of the image recipe.
        :param working_directory: The working directory to be used during build and test workflows.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444253fe6d55edb4bf7ea447bb7ae4e287aece7cf12879d2cec9fd026fc452db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImageRecipeProps(
            components=components,
            name=name,
            parent_image=parent_image,
            version=version,
            additional_instance_configuration=additional_instance_configuration,
            block_device_mappings=block_device_mappings,
            description=description,
            tags=tags,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1737d7cd8055449c513cb0b6c75d4bbbf0e2c990987f804b9481e5a5b7754752)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f407445e0c90d81e4130ef65b586b2e625e9b670e70084b6bfb93305d9f9dda)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the image recipe.

        For example, ``arn:aws:imagebuilder:us-east-1:123456789012:image-recipe/mybasicrecipe/2019.12.03`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the image recipe.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]]:
        '''The components of the image recipe.

        Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6478240d70d7cab743cebdef2a111e57c5ea6156be99fe64a85d0e45cd40d5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__039f53e1bf48cd048fd0e73acc0c24d969d52c21dc35219260d193768907a98b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''The parent image of the image recipe.

        The string must be either an Image ARN or an AMI ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35fc17a40f46f1e08100f894cb124eca378668c840e0945decbf6cc2c52992b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentImage", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The semantic version of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__127f7f5729b2d8fd6ad91292e6c32e8a2849c183a7c9dc02035fed2afac03954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="additionalInstanceConfiguration")
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]]:
        '''Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration.

        Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]], jsii.get(self, "additionalInstanceConfiguration"))

    @additional_instance_configuration.setter
    def additional_instance_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__194918df56e0ddcfd7c69eb1d9df029825065e76e83b074b00cb6ac611f8196b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInstanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]]:
        '''The block device mappings to apply when creating images from this recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]], jsii.get(self, "blockDeviceMappings"))

    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd7bb41073650f7f47141a12c480496459dea5cfa0de393466abff7a1ac436e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDeviceMappings", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955c8f1032e3b17c98762952307061cca879bf755f2de0a8cfab5c0e56025b2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory to be used during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60b3837231e0e7542fb5461519ff511e6abb8dabb024377a0bc95135089118a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "systems_manager_agent": "systemsManagerAgent",
            "user_data_override": "userDataOverride",
        },
    )
    class AdditionalInstanceConfigurationProperty:
        def __init__(
            self,
            *,
            systems_manager_agent: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.SystemsManagerAgentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_data_override: typing.Optional[builtins.str] = None,
        ) -> None:
            '''In addition to your infrastructure configuration, these settings provide an extra layer of control over your build instances.

            You can also specify commands to run on launch for all of your build instances.

            Image Builder does not automatically install the Systems Manager agent on Windows instances. If your base image includes the Systems Manager agent, then the AMI that you create will also include the agent. For Linux instances, if the base image does not already include the Systems Manager agent, Image Builder installs it. For Linux instances where Image Builder installs the Systems Manager agent, you can choose whether to keep it for the AMI that you create.

            :param systems_manager_agent: Contains settings for the Systems Manager agent on your build instance.
            :param user_data_override: Use this property to provide commands or a command script to run when you launch your build instance. The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image. .. epigraph:: The user data is always base 64 encoded. For example, the following commands are encoded as ``IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$`` : *#!/bin/bash* mkdir -p /var/bb/ touch /var

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                additional_instance_configuration_property = imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                    systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                        uninstall_after_build=False
                    ),
                    user_data_override="userDataOverride"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b86d218ad75a89474c7b8472e30f8b5d670f2102cffff5c06ea9fe2ecd581e0f)
                check_type(argname="argument systems_manager_agent", value=systems_manager_agent, expected_type=type_hints["systems_manager_agent"])
                check_type(argname="argument user_data_override", value=user_data_override, expected_type=type_hints["user_data_override"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if systems_manager_agent is not None:
                self._values["systems_manager_agent"] = systems_manager_agent
            if user_data_override is not None:
                self._values["user_data_override"] = user_data_override

        @builtins.property
        def systems_manager_agent(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.SystemsManagerAgentProperty"]]:
            '''Contains settings for the Systems Manager agent on your build instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-systemsmanageragent
            '''
            result = self._values.get("systems_manager_agent")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.SystemsManagerAgentProperty"]], result)

        @builtins.property
        def user_data_override(self) -> typing.Optional[builtins.str]:
            '''Use this property to provide commands or a command script to run when you launch your build instance.

            The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.
            .. epigraph::

               The user data is always base 64 encoded. For example, the following commands are encoded as ``IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$`` :

               *#!/bin/bash*

               mkdir -p /var/bb/

               touch /var

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-userdataoverride
            '''
            result = self._values.get("user_data_override")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalInstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn", "parameters": "parameters"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.ComponentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration details of the component.

            :param component_arn: The Amazon Resource Name (ARN) of the component.
            :param parameters: A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                component_configuration_property = imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d307c3e2313eed20e4863c2a3b37ebfa1ad57f124e8630ff91ab7d1b49d79d76)
                check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.ComponentParameterProperty"]]]]:
            '''A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.ComponentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.ComponentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ComponentParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''Contains a key/value pair that sets the named component parameter.

            :param name: The name of the component parameter to set.
            :param value: Sets the value for the named component parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                component_parameter_property = imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4675f76f24894eff2ac3c8be51b10bee3448aa32ffb10be9d3203a118cf25c8)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the component parameter to set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''Sets the value for the named component parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The image recipe EBS instance block device specification includes the Amazon EBS-specific block device mapping specifications for the image.

            :param delete_on_termination: Configures delete on termination of the associated device.
            :param encrypted: Use to configure device encryption.
            :param iops: Use to configure device IOPS.
            :param kms_key_id: Use to configure the KMS key to use when encrypting the device.
            :param snapshot_id: The snapshot that defines the device contents.
            :param throughput: *For GP3 volumes only* – The throughput in MiB/s that the volume supports.
            :param volume_size: Overrides the volume size of the device.
            :param volume_type: Overrides the volume type of the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                ebs_instance_block_device_specification_property = imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35e0326e8ba76e74df3bfc397d1f43e32a74d3273f4025af8ec4d2890865c797)
                check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Configures delete on termination of the associated device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Use to configure device encryption.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''Use to configure device IOPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''Use to configure the KMS key to use when encrypting the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''The snapshot that defines the device contents.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''*For GP3 volumes only* – The throughput in MiB/s that the volume supports.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''Overrides the volume size of the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''Overrides the volume type of the device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines block device mappings for the instance used to configure your image.

            :param device_name: The device to which these mappings apply.
            :param ebs: Use to manage Amazon EBS-specific configuration for this mapping.
            :param no_device: Enter an empty string to remove a mapping from the parent image. The following is an example of an empty string value in the ``NoDevice`` field. ``NoDevice:""``
            :param virtual_name: Manages the instance ephemeral devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                instance_block_device_mapping_property = imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a38c0823d56398b13f25372299475c54d4b5de62b3e944736f0ddafae051aff)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The device to which these mappings apply.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''Use to manage Amazon EBS-specific configuration for this mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''Enter an empty string to remove a mapping from the parent image.

            The following is an example of an empty string value in the ``NoDevice`` field.

            ``NoDevice:""``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''Manages the instance ephemeral devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty",
        jsii_struct_bases=[],
        name_mapping={"uninstall_after_build": "uninstallAfterBuild"},
    )
    class SystemsManagerAgentProperty:
        def __init__(
            self,
            *,
            uninstall_after_build: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Contains settings for the Systems Manager agent on your build instance.

            :param uninstall_after_build: Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                systems_manager_agent_property = imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                    uninstall_after_build=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d06dc767aa97a3ec765b071874ff3d4d7ea4db9b743e6c4628dfd0a99cfba42)
                check_type(argname="argument uninstall_after_build", value=uninstall_after_build, expected_type=type_hints["uninstall_after_build"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if uninstall_after_build is not None:
                self._values["uninstall_after_build"] = uninstall_after_build

        @builtins.property
        def uninstall_after_build(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI.

            If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild
            '''
            result = self._values.get("uninstall_after_build")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemsManagerAgentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "name": "name",
        "parent_image": "parentImage",
        "version": "version",
        "additional_instance_configuration": "additionalInstanceConfiguration",
        "block_device_mappings": "blockDeviceMappings",
        "description": "description",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnImageRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnImageRecipe``.

        :param components: The components of the image recipe. Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.
        :param name: The name of the image recipe.
        :param parent_image: The parent image of the image recipe. The string must be either an Image ARN or an AMI ID.
        :param version: The semantic version of the image recipe.
        :param additional_instance_configuration: Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.
        :param block_device_mappings: The block device mappings to apply when creating images from this recipe.
        :param description: The description of the image recipe.
        :param tags: The tags of the image recipe.
        :param working_directory: The working directory to be used during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_image_recipe_props = imagebuilder.CfnImageRecipeProps(
                components=[imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )],
                name="name",
                parent_image="parentImage",
                version="version",
            
                # the properties below are optional
                additional_instance_configuration=imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                    systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                        uninstall_after_build=False
                    ),
                    user_data_override="userDataOverride"
                ),
                block_device_mappings=[imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                description="description",
                tags={
                    "tags_key": "tags"
                },
                working_directory="workingDirectory"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98899cd9008580cfdbfe650c2ec0c529cda87c890ed4e790bc51c02d54f0b752)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument additional_instance_configuration", value=additional_instance_configuration, expected_type=type_hints["additional_instance_configuration"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "components": components,
            "name": name,
            "parent_image": parent_image,
            "version": version,
        }
        if additional_instance_configuration is not None:
            self._values["additional_instance_configuration"] = additional_instance_configuration
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]]:
        '''The components of the image recipe.

        Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''The parent image of the image recipe.

        The string must be either an Image ARN or an AMI ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The semantic version of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]]:
        '''Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration.

        Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration
        '''
        result = self._values.get("additional_instance_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]]:
        '''The block device mappings to apply when creating images from this recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory to be used during build and test workflows.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnInfrastructureConfiguration(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration",
):
    '''A CloudFormation ``AWS::ImageBuilder::InfrastructureConfiguration``.

    The infrastructure configuration allows you to specify the infrastructure within which to build and test your image. In the infrastructure configuration, you can specify instance types, subnets, and security groups to associate with your instance. You can also associate an Amazon EC2 key pair with the instance used to build your image. This allows you to log on to your instance to troubleshoot if your build fails and you set terminateInstanceOnFailure to false.

    :cloudformationResource: AWS::ImageBuilder::InfrastructureConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_imagebuilder as imagebuilder
        
        cfn_infrastructure_configuration = imagebuilder.CfnInfrastructureConfiguration(self, "MyCfnInfrastructureConfiguration",
            instance_profile_name="instanceProfileName",
            name="name",
        
            # the properties below are optional
            description="description",
            instance_metadata_options=imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                http_put_response_hop_limit=123,
                http_tokens="httpTokens"
            ),
            instance_types=["instanceTypes"],
            key_pair="keyPair",
            logging=imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                    s3_bucket_name="s3BucketName",
                    s3_key_prefix="s3KeyPrefix"
                )
            ),
            resource_tags={
                "resource_tags_key": "resourceTags"
            },
            security_group_ids=["securityGroupIds"],
            sns_topic_arn="snsTopicArn",
            subnet_id="subnetId",
            tags={
                "tags_key": "tags"
            },
            terminate_instance_on_failure=False
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnInfrastructureConfiguration.LoggingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::InfrastructureConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_profile_name: The instance profile of the infrastructure configuration.
        :param name: The name of the infrastructure configuration.
        :param description: The description of the infrastructure configuration.
        :param instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param instance_types: The instance types of the infrastructure configuration.
        :param key_pair: The Amazon EC2 key pair of the infrastructure configuration.
        :param logging: The logging configuration defines where Image Builder uploads your logs.
        :param resource_tags: The tags attached to the resource created by Image Builder.
        :param security_group_ids: The security group IDs of the infrastructure configuration.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.
        :param subnet_id: The subnet ID of the infrastructure configuration.
        :param tags: The tags of the infrastructure configuration.
        :param terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404764d3badf8184430162de19697820ca8d88cb050e59c29f02583f54dee3dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInfrastructureConfigurationProps(
            instance_profile_name=instance_profile_name,
            name=name,
            description=description,
            instance_metadata_options=instance_metadata_options,
            instance_types=instance_types,
            key_pair=key_pair,
            logging=logging,
            resource_tags=resource_tags,
            security_group_ids=security_group_ids,
            sns_topic_arn=sns_topic_arn,
            subnet_id=subnet_id,
            tags=tags,
            terminate_instance_on_failure=terminate_instance_on_failure,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41a050f17b22762fb671990730eeb27d4d21d3ff5555a42ffaa200a518bc18b)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d0d637cffe7f28b38c49c5037619f7c533c148e177800dbeb5a2c6727c4526)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the infrastructure configuration.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the infrastructure configuration.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''The instance profile of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0815f43c976d8d6a1f30601ab95b0523cad9e7df43855e2ca12179f8e7d4d6c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5028af79c2b2e7c6ffd39d64e44274e2814a5923816cb3980407bb29b8cb2d1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98c2e98deb4a3fe5c94a3aba24cf28ad32858dfcde3663e7ab6874a402e4a07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataOptions")
    def instance_metadata_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]]:
        '''The instance metadata option settings for the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]], jsii.get(self, "instanceMetadataOptions"))

    @instance_metadata_options.setter
    def instance_metadata_options(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f0086707afeeb646e3fcbf98a8ac84096ba2e8ce88f8ec191a5929bbf9180b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceMetadataOptions", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The instance types of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a0b482b4a125d8b6784e7f3a4b9afc80a77bde38aa92ddbd6eb064cc7320c33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b719a8aacd378b1d47bd97a6efb05ec076ad95f88135a6316bec2ca009f94ffc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPair", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]]:
        '''The logging configuration defines where Image Builder uploads your logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]], jsii.get(self, "logging"))

    @logging.setter
    def logging(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856905dc4fe9379186d76d9ae51c6b3e472d4ad8821a09ba6e7b01148094838b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''The tags attached to the resource created by Image Builder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e8ebf32a704ad970982d23f29d047c60d9ba1efc705a20e5b9cc5e93d5e33ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The security group IDs of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0f4578f114ee90c11b68a44691151ebf0a1c8c54bf6707e22fcdaa6bc00c85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__368a17bce206b61b9fb3db4d03023a7607023764abce5436c2736fdae627880d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211b6df8460ffbec852c7d285ef03f6d0f8cac89eecac10b46e25744b660be63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''The terminate instance on failure configuration of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "terminateInstanceOnFailure"))

    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3828cd45bc02ab2d8f2d1d7abd5c343d3113e61426e39910543166aa7bb708c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminateInstanceOnFailure", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "http_put_response_hop_limit": "httpPutResponseHopLimit",
            "http_tokens": "httpTokens",
        },
    )
    class InstanceMetadataOptionsProperty:
        def __init__(
            self,
            *,
            http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
            http_tokens: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The instance metadata options that apply to the HTTP requests that pipeline builds use to launch EC2 build and test instances.

            For more information about instance metadata options, see `Configure the instance metadata options <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html>`_ in the **Amazon EC2 User Guide** for Linux instances, or `Configure the instance metadata options <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html>`_ in the **Amazon EC2 Windows Guide** for Windows instances.

            :param http_put_response_hop_limit: Limit the number of hops that an instance metadata request can traverse to reach its destination. The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.
            :param http_tokens: Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows: - *required* – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases. - *optional* – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned. The default setting is *optional* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                instance_metadata_options_property = imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dc6ed0befab37a39cee1e2cd15afa28ff2ec22636fb7a27ad83e59dd59af4469)
                check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
                check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if http_put_response_hop_limit is not None:
                self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
            if http_tokens is not None:
                self._values["http_tokens"] = http_tokens

        @builtins.property
        def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
            '''Limit the number of hops that an instance metadata request can traverse to reach its destination.

            The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit
            '''
            result = self._values.get("http_put_response_hop_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def http_tokens(self) -> typing.Optional[builtins.str]:
            '''Indicates whether a signed token header is required for instance metadata retrieval requests.

            The values affect the response as follows:

            - *required* – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
            - *optional* – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.

            The default setting is *optional* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens
            '''
            result = self._values.get("http_tokens")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceMetadataOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_logs": "s3Logs"},
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            s3_logs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnInfrastructureConfiguration.S3LogsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Logging configuration defines where Image Builder uploads your logs.

            :param s3_logs: The Amazon S3 logging configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                logging_property = imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                    s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                        s3_bucket_name="s3BucketName",
                        s3_key_prefix="s3KeyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ab4ac0be90b35fb589b76b8faf0271c8e974688ec542e4964898ed43018fbfc)
                check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.S3LogsProperty"]]:
            '''The Amazon S3 logging configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInfrastructureConfiguration.S3LogsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class S3LogsProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon S3 logging configuration.

            :param s3_bucket_name: The S3 bucket in which to store the logs.
            :param s3_key_prefix: The Amazon S3 path to the bucket where the logs are stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_imagebuilder as imagebuilder
                
                s3_logs_property = imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                    s3_bucket_name="s3BucketName",
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e0f04c468c4abea45e31991c1dbfe89da17b67119a7f7f57b7e871f501f8c3c)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket in which to store the logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 path to the bucket where the logs are stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_name": "instanceProfileName",
        "name": "name",
        "description": "description",
        "instance_metadata_options": "instanceMetadataOptions",
        "instance_types": "instanceTypes",
        "key_pair": "keyPair",
        "logging": "logging",
        "resource_tags": "resourceTags",
        "security_group_ids": "securityGroupIds",
        "sns_topic_arn": "snsTopicArn",
        "subnet_id": "subnetId",
        "tags": "tags",
        "terminate_instance_on_failure": "terminateInstanceOnFailure",
    },
)
class CfnInfrastructureConfigurationProps:
    def __init__(
        self,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInfrastructureConfiguration``.

        :param instance_profile_name: The instance profile of the infrastructure configuration.
        :param name: The name of the infrastructure configuration.
        :param description: The description of the infrastructure configuration.
        :param instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param instance_types: The instance types of the infrastructure configuration.
        :param key_pair: The Amazon EC2 key pair of the infrastructure configuration.
        :param logging: The logging configuration defines where Image Builder uploads your logs.
        :param resource_tags: The tags attached to the resource created by Image Builder.
        :param security_group_ids: The security group IDs of the infrastructure configuration.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.
        :param subnet_id: The subnet ID of the infrastructure configuration.
        :param tags: The tags of the infrastructure configuration.
        :param terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_imagebuilder as imagebuilder
            
            cfn_infrastructure_configuration_props = imagebuilder.CfnInfrastructureConfigurationProps(
                instance_profile_name="instanceProfileName",
                name="name",
            
                # the properties below are optional
                description="description",
                instance_metadata_options=imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens"
                ),
                instance_types=["instanceTypes"],
                key_pair="keyPair",
                logging=imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                    s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                        s3_bucket_name="s3BucketName",
                        s3_key_prefix="s3KeyPrefix"
                    )
                ),
                resource_tags={
                    "resource_tags_key": "resourceTags"
                },
                security_group_ids=["securityGroupIds"],
                sns_topic_arn="snsTopicArn",
                subnet_id="subnetId",
                tags={
                    "tags_key": "tags"
                },
                terminate_instance_on_failure=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d145e63e7d3092307172ee68644ab688094546acf9c9a6775345d1974edf04)
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument instance_metadata_options", value=instance_metadata_options, expected_type=type_hints["instance_metadata_options"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument terminate_instance_on_failure", value=terminate_instance_on_failure, expected_type=type_hints["terminate_instance_on_failure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_name": instance_profile_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if instance_metadata_options is not None:
            self._values["instance_metadata_options"] = instance_metadata_options
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if logging is not None:
            self._values["logging"] = logging
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if terminate_instance_on_failure is not None:
            self._values["terminate_instance_on_failure"] = terminate_instance_on_failure

    @builtins.property
    def instance_profile_name(self) -> builtins.str:
        '''The instance profile of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        assert result is not None, "Required property 'instance_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]]:
        '''The instance metadata option settings for the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions
        '''
        result = self._values.get("instance_metadata_options")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The instance types of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]]:
        '''The logging configuration defines where Image Builder uploads your logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''The tags attached to the resource created by Image Builder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The security group IDs of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''The terminate instance on failure configuration of the infrastructure configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure
        '''
        result = self._values.get("terminate_instance_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInfrastructureConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponent",
    "CfnComponentProps",
    "CfnContainerRecipe",
    "CfnContainerRecipeProps",
    "CfnDistributionConfiguration",
    "CfnDistributionConfigurationProps",
    "CfnImage",
    "CfnImagePipeline",
    "CfnImagePipelineProps",
    "CfnImageProps",
    "CfnImageRecipe",
    "CfnImageRecipeProps",
    "CfnInfrastructureConfiguration",
    "CfnInfrastructureConfigurationProps",
]

publication.publish()

def _typecheckingstub__fe1cc496479ca9a7e56302a9fae6564e6463f16f4a3c79d73ae9cb1e516fff30(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    platform: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d1d3a4e830d89b8fde7cfd0c5493b5f0d5e0f06b341d1042c38662356d36bfe(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a5bc457d43bc19c97861b09c1fa9214c08d586f5ba7a50fad38481e003fe51e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde1a86ca9e902e1addd2a81110f8233ec96875552eaa8840d74decacfc1d8b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba8d97cf8edacc2fadac0834e0d290a3e3bbddb3a1db919ce9572a891afd64f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0257100f3292352bce9185283bc58df048fdd20bee2c0192ffff43dbea6f2e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535c87ef75a121fb96069401cd994baa0b0342fd87d07e8e9a5218dd85cf0fdb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5a38ca397e02fed2911fab93f0479eccbea9d4e93787bbaa9c19ea89b0acdc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59c5f389a50bab79a740422a35c62a4da37834083a780b630614629f824141e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d967b4edb058173d8baa35061e6f7a7557fbebbc30763f83981e816304ab2669(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429bf33b064b5cb1813e8319a0f011601ccc7adb3e4a710efde80452630dfad7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004003e5f6aefdef96be33bcaca60db67a172a08069716f8f731a48c01df6ffe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd24992bfb80dc6981c6fc6d3f765ee7be888021dca1a6c49802eed1857adaef(
    *,
    name: builtins.str,
    platform: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a7a95c6787ef0de46ea7fc6e498a4f738e8f5e3a649569a79ad578be3a464c(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    container_type: builtins.str,
    name: builtins.str,
    parent_image: builtins.str,
    target_repository: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
    version: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dockerfile_template_data: typing.Optional[builtins.str] = None,
    dockerfile_template_uri: typing.Optional[builtins.str] = None,
    image_os_version_override: typing.Optional[builtins.str] = None,
    instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    platform_override: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c344ceecb7750044c0ac74df20671951a97b05e5fa5a942e2a195acd0556b1a(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a380b36c2d9e74fed5e73eaa9e86334ab1bc02127337337058474afcdd7e34b0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd606a5fbad5302ea8b76746496ee9a0e9f765851ef1559ae006a14b8df69e40(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.ComponentConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb9cf6b425d2821fd7ba904f31d021c39a45d0945c61cbc01b3ef3b753e40297(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8df7c0eb4a7d7ca1930c3a379eda08933ffd70c8ce731411b0ad0d2defd87f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5447b5e4f0886a01512608136cfb66edacff16c92c150a251e3f9408d823ebc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176e453b4b00bd19c068dd0f245ea5711270097a461acc75037495b40e977d9d(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc638802bcce467ed21456f46af189fee6752d0dbf7736343fc2d098b9c8edcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ad39f5db954328b06d2c5a62a5bac47e5de00790f75f37a736bab86a21d844(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c1ff944d64647d555a771f9ad14a4cbb4c07af5aa2af349cecabe519100daf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28c7509cfa85df4c9d9a6a62ba26cd51f5770beaf8d35f90608c559e445064e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa9007617092d0e02ec42569d32f745b296896b7aa8a7e541a7d89281eea45c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1e2c3c55656dc0037a081a77759041ff8c48743c5fd4a4cc9735b31c3cde90(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535134592066797e884b78e86fbb290748041c36be000822b69756e9af986b1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fd5d41217536e9f564911f70cc73f7e433f7b6e6f47abeac8319148a0a2791(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ba6ca6febff34f0df678cb4b2d0d79612dcf6926b329f470402e703da38c326(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fe9a2266fba31ee5528ce66e321487e8d4d5b672a1e80006f8dc6032bdaa69(
    *,
    component_arn: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.ComponentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0feaf5f018aacd89766cdaa849154b3566249f697b429f5d7fb9bc4053207fc(
    *,
    name: builtins.str,
    value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095e4bd8d8ed7fecebf35e2ce1dd0c2c9fc9ef875518bb499f58de181585fa56(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd6756cda3d99b28dbf0f3b48705f560c200b87b369d494233849fe9edf7710(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c9338383aa0077f1ce17108486e870db44b64a72153672e1109d54992e8d1f(
    *,
    block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    image: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cff2524a5b8bb1cdf483f9a7672b40d72843cb70480fbbedd8ea93fd5db930d(
    *,
    repository_name: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4888e7a655d1e4ca650d34565aaf0a32c53e99340c2dba8ce9191f415b67cb(
    *,
    components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    container_type: builtins.str,
    name: builtins.str,
    parent_image: builtins.str,
    target_repository: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
    version: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dockerfile_template_data: typing.Optional[builtins.str] = None,
    dockerfile_template_uri: typing.Optional[builtins.str] = None,
    image_os_version_override: typing.Optional[builtins.str] = None,
    instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    platform_override: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59228d22129378d0454490bc22550c10d18ff3eed735ce2b123101693bb81c7(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    distributions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ca2af01b9dd1d7e6de6c8aa26c4f8a8523399ce7e864989e1011355f3d36ac(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79482d837d799aea2a260d3de49faec1ed9e9fdd92a53207ae2b0de94f31e4c5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b81ed9c00021fe92738311deb5b887021e8f98696e4b7c1e71ce62cf75bf02d(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDistributionConfiguration.DistributionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f0863d3c30e56e5c244cb383bd34cee53611455cbf55d78de598244a4f3e69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c379868868cd3601f6c36eba08f5dda5cdda5f512a8d6870036b507a3750267(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4696db19cc706b6b52ea0766fc521fe4ba2ad1d08dcb804cbfb276dec9e786d8(
    *,
    ami_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    launch_permission_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.LaunchPermissionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b647223a2fcfc4fe6a9e86932938634c98cf68b5c66e1d788f7ee119b2b8f3(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    target_repository: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d9a91ff83814c0c21dd4b48f701bf94a26acff8eb882501718f6efd71f088b(
    *,
    region: builtins.str,
    ami_distribution_configuration: typing.Any = None,
    container_distribution_configuration: typing.Any = None,
    fast_launch_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.FastLaunchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    launch_template_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.LaunchTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b1dab882f80ac23f45f27c3fe430f603469c6fe9ba2ded7d29995b86d4fbb1(
    *,
    account_id: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    launch_template: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_parallel_launches: typing.Optional[jsii.Number] = None,
    snapshot_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51870bc75f77bdcb19a86273ba148f9679dd280e30a78c1da0991fc7de122b54(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    launch_template_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac7a7b037906b48fe4178fb30cc1f6546f7d733df567eb99dfdd84f58ae7cb20(
    *,
    target_resource_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6adceb2d6e04f430332f3a150aa90805998e7479b29a99011d8f99ab7bb0ea0c(
    *,
    organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde3e3da84b4686f1fbf271e67a48e29a8c7328b67bc83bed3136d2da06285bb(
    *,
    account_id: typing.Optional[builtins.str] = None,
    launch_template_id: typing.Optional[builtins.str] = None,
    set_default_version: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c246cba6edbb82685e2d879ac3d9f14e4f8eae6efb38137f6dde1f30bbabbfda(
    *,
    repository_name: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb27b2bb605e8a73fa5d268ee917cbaa10c165393c05714c1d0b65435906284(
    *,
    distributions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4d58d2d1e97b7653ee4cb81132cb037fabb890b3acf1ea6334231ee6be2da9(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    infrastructure_configuration_arn: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca54ec9e2922745d7891670afdb1ef808fe5b5b9aaa4a5861692622feb62f6a7(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1021653e5dbff14f635d082276fcead96b79c7911a0b020365dcf79ef850e84e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ccaacc49e138556d172f69bef028686df9391836446a8ba37e4accd93a15dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59c24ae255477a427c27fb629b12624cf6335721024ce364f650f7ebc00804e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87b8111920fb2b0ab83f5cdb22c77bd1216f9dd969ad8a3040728a90408b4123(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df26b0360093576ce1316ca7acb8611242e5acc171deee61d02a84768960317(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09756416b511ca613efb6053df1b66d938d81ecdb78031d21884a7318bb29539(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__721f9bae295d919178378c0b726aaa948eb6d06c8287de066afc437a8f4e723b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageScanningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48be2c53dd08eeb50acebcb9d409abf0911e460d41f289304be4b10889e9cf6d(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImage.ImageTestsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe92999e4f6a2192fb4b24e66651f95d96472f26908191a1310b3e0d1839ba8c(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda2321d2389bded10a19240792fca4f703af45d34e988273106b53d92ac350e(
    *,
    ecr_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.EcrConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c49401811b71b69583348fed8a96e029e152a2f4f7595eccd7ebb26c4ead602(
    *,
    image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234e0e6de34d31d2f9ae6047d04d2aee4dadfd493797dafd265219fd64acb7f3(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    infrastructure_configuration_arn: builtins.str,
    name: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bf84e55f608e09a7a48ccf48088ba07955cc8d3605bc70b3ebcccff54eea2f(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de8910077232fca1b7111bae85da6107bf6cfdf654a3f125078a59c13dc2328(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24be75e5ae8530bc803c8e5ea3693d6f9727e01fb85472621709339866d06dab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c644ecbfe1a9842f0c0245e80067af982e8a297a161465f8d82e1186295da77e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ffff10d476a34a4911e6a76f042d26c1ac2d50ba99b29614178e86cfb3b23c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb9116215c6f2a98d3f7d9a7a372e4efb0d5ff62af91bf9527718f1f677d26d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__574f2608825ab7901201716eaea2dee2169bd3fbe8356bfd85fe0d6c88c6f88a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6854e96c5fc6bd503a7f1f1f5482cf1a66111eaf1170bddf277e31ed82cb31(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c498dc3589c2f4e29536fb6e805d86df1fffbb2d20afc6badf0b272f548fe09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fe40aa83d09d013f9efa595fa260a2485ebf0d70d6513ca7fcc66bdaa081f2(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageScanningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e649780a7303b07fd34a2aafb520841950de60389e31baefdd56fcaaf021abf9(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882e20d97a475cc5dcd9bbd32c4a10256355c1d1033393c9088e95f81fdcee76(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImagePipeline.ScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790c03b199485be80c0a4555ee6869329a87509968d856321e2440960103351a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87b41d1e0c90971c4afe86176c8e4ea79bba53b3b08d32d94331cd82abddaa79(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8682c78304b8b0eedfe960912d0f2abc62bd895b071b193ec735e2699f9e5e64(
    *,
    ecr_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.EcrConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0210ff7e086b2ebef743ae79e24f2e3180202f9c87f2cca1699fcd79264ebea(
    *,
    image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c02f9eedf76d7fd90233ef5ec4319c34797859382f1d8a6bbdcf9968f7ebdb(
    *,
    pipeline_execution_start_condition: typing.Optional[builtins.str] = None,
    schedule_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731e06b83e0a9e23d94d5a9c2d78beffc4b74a93b0459548e3bd64feadf87868(
    *,
    infrastructure_configuration_arn: builtins.str,
    name: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92ddf7c746eba695cafe07b6c3e35f902ddc25d7a8fb518a8172a734e0cdad0(
    *,
    infrastructure_configuration_arn: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444253fe6d55edb4bf7ea447bb7ae4e287aece7cf12879d2cec9fd026fc452db(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    parent_image: builtins.str,
    version: builtins.str,
    additional_instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1737d7cd8055449c513cb0b6c75d4bbbf0e2c990987f804b9481e5a5b7754752(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f407445e0c90d81e4130ef65b586b2e625e9b670e70084b6bfb93305d9f9dda(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6478240d70d7cab743cebdef2a111e57c5ea6156be99fe64a85d0e45cd40d5c(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__039f53e1bf48cd048fd0e73acc0c24d969d52c21dc35219260d193768907a98b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fc17a40f46f1e08100f894cb124eca378668c840e0945decbf6cc2c52992b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__127f7f5729b2d8fd6ad91292e6c32e8a2849c183a7c9dc02035fed2afac03954(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__194918df56e0ddcfd7c69eb1d9df029825065e76e83b074b00cb6ac611f8196b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd7bb41073650f7f47141a12c480496459dea5cfa0de393466abff7a1ac436e(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955c8f1032e3b17c98762952307061cca879bf755f2de0a8cfab5c0e56025b2f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60b3837231e0e7542fb5461519ff511e6abb8dabb024377a0bc95135089118a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86d218ad75a89474c7b8472e30f8b5d670f2102cffff5c06ea9fe2ecd581e0f(
    *,
    systems_manager_agent: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.SystemsManagerAgentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_data_override: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d307c3e2313eed20e4863c2a3b37ebfa1ad57f124e8630ff91ab7d1b49d79d76(
    *,
    component_arn: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.ComponentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4675f76f24894eff2ac3c8be51b10bee3448aa32ffb10be9d3203a118cf25c8(
    *,
    name: builtins.str,
    value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e0326e8ba76e74df3bfc397d1f43e32a74d3273f4025af8ec4d2890865c797(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a38c0823d56398b13f25372299475c54d4b5de62b3e944736f0ddafae051aff(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d06dc767aa97a3ec765b071874ff3d4d7ea4db9b743e6c4628dfd0a99cfba42(
    *,
    uninstall_after_build: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98899cd9008580cfdbfe650c2ec0c529cda87c890ed4e790bc51c02d54f0b752(
    *,
    components: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    parent_image: builtins.str,
    version: builtins.str,
    additional_instance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    block_device_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404764d3badf8184430162de19697820ca8d88cb050e59c29f02583f54dee3dc(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    instance_profile_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    instance_metadata_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_pair: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41a050f17b22762fb671990730eeb27d4d21d3ff5555a42ffaa200a518bc18b(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d0d637cffe7f28b38c49c5037619f7c533c148e177800dbeb5a2c6727c4526(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0815f43c976d8d6a1f30601ab95b0523cad9e7df43855e2ca12179f8e7d4d6c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5028af79c2b2e7c6ffd39d64e44274e2814a5923816cb3980407bb29b8cb2d1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98c2e98deb4a3fe5c94a3aba24cf28ad32858dfcde3663e7ab6874a402e4a07(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f0086707afeeb646e3fcbf98a8ac84096ba2e8ce88f8ec191a5929bbf9180b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0b482b4a125d8b6784e7f3a4b9afc80a77bde38aa92ddbd6eb064cc7320c33(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b719a8aacd378b1d47bd97a6efb05ec076ad95f88135a6316bec2ca009f94ffc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856905dc4fe9379186d76d9ae51c6b3e472d4ad8821a09ba6e7b01148094838b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8ebf32a704ad970982d23f29d047c60d9ba1efc705a20e5b9cc5e93d5e33ce(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0f4578f114ee90c11b68a44691151ebf0a1c8c54bf6707e22fcdaa6bc00c85(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368a17bce206b61b9fb3db4d03023a7607023764abce5436c2736fdae627880d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211b6df8460ffbec852c7d285ef03f6d0f8cac89eecac10b46e25744b660be63(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3828cd45bc02ab2d8f2d1d7abd5c343d3113e61426e39910543166aa7bb708c(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6ed0befab37a39cee1e2cd15afa28ff2ec22636fb7a27ad83e59dd59af4469(
    *,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab4ac0be90b35fb589b76b8faf0271c8e974688ec542e4964898ed43018fbfc(
    *,
    s3_logs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.S3LogsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0f04c468c4abea45e31991c1dbfe89da17b67119a7f7f57b7e871f501f8c3c(
    *,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d145e63e7d3092307172ee68644ab688094546acf9c9a6775345d1974edf04(
    *,
    instance_profile_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    instance_metadata_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_pair: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
