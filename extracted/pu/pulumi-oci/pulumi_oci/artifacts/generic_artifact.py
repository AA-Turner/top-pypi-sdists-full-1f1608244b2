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

__all__ = ['GenericArtifactArgs', 'GenericArtifact']

@pulumi.input_type
class GenericArtifactArgs:
    def __init__(__self__, *,
                 artifact_id: pulumi.Input[builtins.str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a GenericArtifact resource.
        :param pulumi.Input[builtins.str] artifact_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "artifact_id", artifact_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Input[builtins.str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        """
        return pulumi.get(self, "artifact_id")

    @artifact_id.setter
    def artifact_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "artifact_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _GenericArtifactState:
    def __init__(__self__, *,
                 artifact_id: Optional[pulumi.Input[builtins.str]] = None,
                 artifact_path: Optional[pulumi.Input[builtins.str]] = None,
                 compartment_id: Optional[pulumi.Input[builtins.str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 display_name: Optional[pulumi.Input[builtins.str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 repository_id: Optional[pulumi.Input[builtins.str]] = None,
                 sha256: Optional[pulumi.Input[builtins.str]] = None,
                 size_in_bytes: Optional[pulumi.Input[builtins.str]] = None,
                 state: Optional[pulumi.Input[builtins.str]] = None,
                 time_created: Optional[pulumi.Input[builtins.str]] = None,
                 version: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering GenericArtifact resources.
        :param pulumi.Input[builtins.str] artifact_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        :param pulumi.Input[builtins.str] artifact_path: A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.  Example: `project01/my-web-app/artifact-abc`
        :param pulumi.Input[builtins.str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository's compartment.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[builtins.str] display_name: The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.  Example: `project01/my-web-app/artifact-abc:1.0.0`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[builtins.str] repository_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository.
        :param pulumi.Input[builtins.str] sha256: The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.
        :param pulumi.Input[builtins.str] size_in_bytes: The size of the artifact in bytes.
        :param pulumi.Input[builtins.str] state: The current state of the artifact.
        :param pulumi.Input[builtins.str] time_created: An RFC 3339 timestamp indicating when the repository was created.
        :param pulumi.Input[builtins.str] version: A user-defined string to describe the artifact version.  Example: `1.1.0` or `1.2-beta-2`
        """
        if artifact_id is not None:
            pulumi.set(__self__, "artifact_id", artifact_id)
        if artifact_path is not None:
            pulumi.set(__self__, "artifact_path", artifact_path)
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if repository_id is not None:
            pulumi.set(__self__, "repository_id", repository_id)
        if sha256 is not None:
            pulumi.set(__self__, "sha256", sha256)
        if size_in_bytes is not None:
            pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        """
        return pulumi.get(self, "artifact_id")

    @artifact_id.setter
    def artifact_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "artifact_id", value)

    @property
    @pulumi.getter(name="artifactPath")
    def artifact_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.  Example: `project01/my-web-app/artifact-abc`
        """
        return pulumi.get(self, "artifact_path")

    @artifact_path.setter
    def artifact_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "artifact_path", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.  Example: `project01/my-web-app/artifact-abc:1.0.0`
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository.
        """
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "repository_id", value)

    @property
    @pulumi.getter
    def sha256(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.
        """
        return pulumi.get(self, "sha256")

    @sha256.setter
    def sha256(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "sha256", value)

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The size of the artifact in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @size_in_bytes.setter
    def size_in_bytes(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "size_in_bytes", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The current state of the artifact.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        An RFC 3339 timestamp indicating when the repository was created.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A user-defined string to describe the artifact version.  Example: `1.1.0` or `1.2-beta-2`
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version", value)


@pulumi.type_token("oci:Artifacts/genericArtifact:GenericArtifact")
class GenericArtifact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_id: Optional[pulumi.Input[builtins.str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        This resource provides the Generic Artifact resource in Oracle Cloud Infrastructure Artifacts service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_generic_artifact = oci.artifacts.GenericArtifact("test_generic_artifact",
            artifact_id=test_artifact["id"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        GenericArtifacts can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Artifacts/genericArtifact:GenericArtifact test_generic_artifact "generic/artifacts/{artifactId}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] artifact_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GenericArtifactArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Generic Artifact resource in Oracle Cloud Infrastructure Artifacts service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_generic_artifact = oci.artifacts.GenericArtifact("test_generic_artifact",
            artifact_id=test_artifact["id"],
            defined_tags={
                "Operations.CostCenter": "42",
            },
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        GenericArtifacts can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Artifacts/genericArtifact:GenericArtifact test_generic_artifact "generic/artifacts/{artifactId}"
        ```

        :param str resource_name: The name of the resource.
        :param GenericArtifactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GenericArtifactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_id: Optional[pulumi.Input[builtins.str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GenericArtifactArgs.__new__(GenericArtifactArgs)

            if artifact_id is None and not opts.urn:
                raise TypeError("Missing required property 'artifact_id'")
            __props__.__dict__["artifact_id"] = artifact_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["artifact_path"] = None
            __props__.__dict__["compartment_id"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["repository_id"] = None
            __props__.__dict__["sha256"] = None
            __props__.__dict__["size_in_bytes"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["version"] = None
        super(GenericArtifact, __self__).__init__(
            'oci:Artifacts/genericArtifact:GenericArtifact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            artifact_id: Optional[pulumi.Input[builtins.str]] = None,
            artifact_path: Optional[pulumi.Input[builtins.str]] = None,
            compartment_id: Optional[pulumi.Input[builtins.str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            display_name: Optional[pulumi.Input[builtins.str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            repository_id: Optional[pulumi.Input[builtins.str]] = None,
            sha256: Optional[pulumi.Input[builtins.str]] = None,
            size_in_bytes: Optional[pulumi.Input[builtins.str]] = None,
            state: Optional[pulumi.Input[builtins.str]] = None,
            time_created: Optional[pulumi.Input[builtins.str]] = None,
            version: Optional[pulumi.Input[builtins.str]] = None) -> 'GenericArtifact':
        """
        Get an existing GenericArtifact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] artifact_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        :param pulumi.Input[builtins.str] artifact_path: A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.  Example: `project01/my-web-app/artifact-abc`
        :param pulumi.Input[builtins.str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository's compartment.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[builtins.str] display_name: The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.  Example: `project01/my-web-app/artifact-abc:1.0.0`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[builtins.str] repository_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository.
        :param pulumi.Input[builtins.str] sha256: The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.
        :param pulumi.Input[builtins.str] size_in_bytes: The size of the artifact in bytes.
        :param pulumi.Input[builtins.str] state: The current state of the artifact.
        :param pulumi.Input[builtins.str] time_created: An RFC 3339 timestamp indicating when the repository was created.
        :param pulumi.Input[builtins.str] version: A user-defined string to describe the artifact version.  Example: `1.1.0` or `1.2-beta-2`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GenericArtifactState.__new__(_GenericArtifactState)

        __props__.__dict__["artifact_id"] = artifact_id
        __props__.__dict__["artifact_path"] = artifact_path
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["repository_id"] = repository_id
        __props__.__dict__["sha256"] = sha256
        __props__.__dict__["size_in_bytes"] = size_in_bytes
        __props__.__dict__["state"] = state
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["version"] = version
        return GenericArtifact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> pulumi.Output[builtins.str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.  Example: `ocid1.genericartifact.oc1..exampleuniqueID`
        """
        return pulumi.get(self, "artifact_id")

    @property
    @pulumi.getter(name="artifactPath")
    def artifact_path(self) -> pulumi.Output[builtins.str]:
        """
        A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.  Example: `project01/my-web-app/artifact-abc`
        """
        return pulumi.get(self, "artifact_path")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[builtins.str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository's compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, builtins.str]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[builtins.str]:
        """
        The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.  Example: `project01/my-web-app/artifact-abc:1.0.0`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, builtins.str]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[builtins.str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository.
        """
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter
    def sha256(self) -> pulumi.Output[builtins.str]:
        """
        The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.
        """
        return pulumi.get(self, "sha256")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[builtins.str]:
        """
        The size of the artifact in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[builtins.str]:
        """
        The current state of the artifact.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[builtins.str]:
        """
        An RFC 3339 timestamp indicating when the repository was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[builtins.str]:
        """
        A user-defined string to describe the artifact version.  Example: `1.1.0` or `1.2-beta-2`
        """
        return pulumi.get(self, "version")

