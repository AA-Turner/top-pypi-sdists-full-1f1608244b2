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
from . import outputs
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 generate_secret_string: Optional[pulumi.Input['SecretGenerateSecretStringArgs']] = None,
                 kms_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 replica_regions: Optional[pulumi.Input[Sequence[pulumi.Input['SecretReplicaRegionArgs']]]] = None,
                 secret_string: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Secret resource.
        :param pulumi.Input[builtins.str] description: The description of the secret.
        :param pulumi.Input['SecretGenerateSecretStringArgs'] generate_secret_string: A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use ``SecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
                We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
        :param pulumi.Input[builtins.str] kms_key_id: The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by ``alias/``, for example ``alias/aws/secretsmanager``. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
                To use a KMS key in a different account, use the key ARN or the alias ARN.
                If you don't specify this value, then Secrets Manager uses the key ``aws/secretsmanager``. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.
                If the secret is in a different AWS account from the credentials calling the API, then you can't use ``aws/secretsmanager`` to encrypt the secret, and you must create and use a customer managed KMS key.
        :param pulumi.Input[builtins.str] name: The name of the new secret.
                The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-
                Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.
        :param pulumi.Input[Sequence[pulumi.Input['SecretReplicaRegionArgs']]] replica_regions: A custom type that specifies a ``Region`` and the ``KmsKeyId`` for a replica secret.
        :param pulumi.Input[builtins.str] secret_string: The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use ``GenerateSecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:
                 ``[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`` 
                Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".
                Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. 
                If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an ``Access Denied`` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secrets' tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2).
                For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
                The following restrictions apply to tags:
                 +  Maximum number of tags per secret: 50
                 +  Maximum key length: 127 Unicode characters in UTF-8
                 +  Maximum value length: 255 Unicode characters in UTF-8
                 +  Tag keys and values are case sensitive.
                 +  Do not use the ``aws:`` prefix in your tag names or values because AWS reserves it for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.
                 +  If you use your tagging schema across multiple services and resources, other services might have restrictions on allowed characters. Generally allowed characters: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if generate_secret_string is not None:
            pulumi.set(__self__, "generate_secret_string", generate_secret_string)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if replica_regions is not None:
            pulumi.set(__self__, "replica_regions", replica_regions)
        if secret_string is not None:
            pulumi.set(__self__, "secret_string", secret_string)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the secret.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="generateSecretString")
    def generate_secret_string(self) -> Optional[pulumi.Input['SecretGenerateSecretStringArgs']]:
        """
        A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use ``SecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
         We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
        """
        return pulumi.get(self, "generate_secret_string")

    @generate_secret_string.setter
    def generate_secret_string(self, value: Optional[pulumi.Input['SecretGenerateSecretStringArgs']]):
        pulumi.set(self, "generate_secret_string", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by ``alias/``, for example ``alias/aws/secretsmanager``. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
         To use a KMS key in a different account, use the key ARN or the alias ARN.
         If you don't specify this value, then Secrets Manager uses the key ``aws/secretsmanager``. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.
         If the secret is in a different AWS account from the credentials calling the API, then you can't use ``aws/secretsmanager`` to encrypt the secret, and you must create and use a customer managed KMS key.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the new secret.
         The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-
         Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="replicaRegions")
    def replica_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecretReplicaRegionArgs']]]]:
        """
        A custom type that specifies a ``Region`` and the ``KmsKeyId`` for a replica secret.
        """
        return pulumi.get(self, "replica_regions")

    @replica_regions.setter
    def replica_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecretReplicaRegionArgs']]]]):
        pulumi.set(self, "replica_regions", value)

    @property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use ``GenerateSecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
        """
        return pulumi.get(self, "secret_string")

    @secret_string.setter
    def secret_string(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "secret_string", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:
          ``[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`` 
         Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".
         Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. 
         If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an ``Access Denied`` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secrets' tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2).
         For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
         The following restrictions apply to tags:
          +  Maximum number of tags per secret: 50
          +  Maximum key length: 127 Unicode characters in UTF-8
          +  Maximum value length: 255 Unicode characters in UTF-8
          +  Tag keys and values are case sensitive.
          +  Do not use the ``aws:`` prefix in your tag names or values because AWS reserves it for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.
          +  If you use your tagging schema across multiple services and resources, other services might have restrictions on allowed characters. Generally allowed characters: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.type_token("aws-native:secretsmanager:Secret")
class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 generate_secret_string: Optional[pulumi.Input[Union['SecretGenerateSecretStringArgs', 'SecretGenerateSecretStringArgsDict']]] = None,
                 kms_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 replica_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SecretReplicaRegionArgs', 'SecretReplicaRegionArgsDict']]]]] = None,
                 secret_string: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        """
        Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.
         For RDS master user credentials, see [AWS::RDS::DBCluster MasterUserSecret](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html).
         For RS admin user credentials, see [AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html).
         To retrieve a secret in a CFNshort template, use a *dynamic reference*. For more information, see [Retrieve a secret in an resource](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html).
         For information about creating a secret in the console, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html). For information about creating a secret using the CLI or SDK, see [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html).
         For information about retrieving a secret in code, see [Retrieve secrets from Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html).

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_redshift_secret = aws_native.secretsmanager.Secret("myRedshiftSecret",
            description="This is a Secrets Manager secret for a Redshift cluster",
            generate_secret_string={
                "secret_string_template": "{\\"username\\": \\"admin\\"}",
                "generate_string_key": "password",
                "password_length": 16,
                "exclude_characters": "\\"'@/\\\\",
            })
        my_redshift_cluster = aws_native.redshift.Cluster("myRedshiftCluster",
            db_name="myjsondb",
            master_username=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::username}}}}"),
            master_user_password=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::password}}}}"),
            node_type="ds2.xlarge",
            cluster_type="single-node")
        secret_redshift_attachment = aws_native.secretsmanager.SecretTargetAttachment("secretRedshiftAttachment",
            secret_id=my_redshift_secret.id,
            target_id=my_redshift_cluster.id,
            target_type="AWS::Redshift::Cluster")

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_redshift_secret = aws_native.secretsmanager.Secret("myRedshiftSecret",
            description="This is a Secrets Manager secret for a Redshift cluster",
            generate_secret_string={
                "secret_string_template": "{\\"username\\": \\"admin\\"}",
                "generate_string_key": "password",
                "password_length": 16,
                "exclude_characters": "\\"'@/\\\\",
            })
        my_redshift_cluster = aws_native.redshift.Cluster("myRedshiftCluster",
            db_name="myjsondb",
            master_username=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::username}}}}"),
            master_user_password=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::password}}}}"),
            node_type="ds2.xlarge",
            cluster_type="single-node")
        secret_redshift_attachment = aws_native.secretsmanager.SecretTargetAttachment("secretRedshiftAttachment",
            secret_id=my_redshift_secret.id,
            target_id=my_redshift_cluster.id,
            target_type="AWS::Redshift::Cluster")

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the secret.
        :param pulumi.Input[Union['SecretGenerateSecretStringArgs', 'SecretGenerateSecretStringArgsDict']] generate_secret_string: A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use ``SecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
                We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
        :param pulumi.Input[builtins.str] kms_key_id: The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by ``alias/``, for example ``alias/aws/secretsmanager``. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
                To use a KMS key in a different account, use the key ARN or the alias ARN.
                If you don't specify this value, then Secrets Manager uses the key ``aws/secretsmanager``. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.
                If the secret is in a different AWS account from the credentials calling the API, then you can't use ``aws/secretsmanager`` to encrypt the secret, and you must create and use a customer managed KMS key.
        :param pulumi.Input[builtins.str] name: The name of the new secret.
                The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-
                Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SecretReplicaRegionArgs', 'SecretReplicaRegionArgsDict']]]] replica_regions: A custom type that specifies a ``Region`` and the ``KmsKeyId`` for a replica secret.
        :param pulumi.Input[builtins.str] secret_string: The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use ``GenerateSecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]] tags: A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:
                 ``[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`` 
                Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".
                Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. 
                If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an ``Access Denied`` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secrets' tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2).
                For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
                The following restrictions apply to tags:
                 +  Maximum number of tags per secret: 50
                 +  Maximum key length: 127 Unicode characters in UTF-8
                 +  Maximum value length: 255 Unicode characters in UTF-8
                 +  Tag keys and values are case sensitive.
                 +  Do not use the ``aws:`` prefix in your tag names or values because AWS reserves it for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.
                 +  If you use your tagging schema across multiple services and resources, other services might have restrictions on allowed characters. Generally allowed characters: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SecretArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.
         For RDS master user credentials, see [AWS::RDS::DBCluster MasterUserSecret](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html).
         For RS admin user credentials, see [AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html).
         To retrieve a secret in a CFNshort template, use a *dynamic reference*. For more information, see [Retrieve a secret in an resource](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html).
         For information about creating a secret in the console, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html). For information about creating a secret using the CLI or SDK, see [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html).
         For information about retrieving a secret in code, see [Retrieve secrets from Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html).

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_redshift_secret = aws_native.secretsmanager.Secret("myRedshiftSecret",
            description="This is a Secrets Manager secret for a Redshift cluster",
            generate_secret_string={
                "secret_string_template": "{\\"username\\": \\"admin\\"}",
                "generate_string_key": "password",
                "password_length": 16,
                "exclude_characters": "\\"'@/\\\\",
            })
        my_redshift_cluster = aws_native.redshift.Cluster("myRedshiftCluster",
            db_name="myjsondb",
            master_username=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::username}}}}"),
            master_user_password=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::password}}}}"),
            node_type="ds2.xlarge",
            cluster_type="single-node")
        secret_redshift_attachment = aws_native.secretsmanager.SecretTargetAttachment("secretRedshiftAttachment",
            secret_id=my_redshift_secret.id,
            target_id=my_redshift_cluster.id,
            target_type="AWS::Redshift::Cluster")

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_redshift_secret = aws_native.secretsmanager.Secret("myRedshiftSecret",
            description="This is a Secrets Manager secret for a Redshift cluster",
            generate_secret_string={
                "secret_string_template": "{\\"username\\": \\"admin\\"}",
                "generate_string_key": "password",
                "password_length": 16,
                "exclude_characters": "\\"'@/\\\\",
            })
        my_redshift_cluster = aws_native.redshift.Cluster("myRedshiftCluster",
            db_name="myjsondb",
            master_username=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::username}}}}"),
            master_user_password=my_redshift_secret.id.apply(lambda id: f"{{{{resolve:secretsmanager:{id}::password}}}}"),
            node_type="ds2.xlarge",
            cluster_type="single-node")
        secret_redshift_attachment = aws_native.secretsmanager.SecretTargetAttachment("secretRedshiftAttachment",
            secret_id=my_redshift_secret.id,
            target_id=my_redshift_cluster.id,
            target_type="AWS::Redshift::Cluster")

        ```

        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 generate_secret_string: Optional[pulumi.Input[Union['SecretGenerateSecretStringArgs', 'SecretGenerateSecretStringArgsDict']]] = None,
                 kms_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 replica_regions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SecretReplicaRegionArgs', 'SecretReplicaRegionArgsDict']]]]] = None,
                 secret_string: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_root_inputs.TagArgs', '_root_inputs.TagArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretArgs.__new__(SecretArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["generate_secret_string"] = generate_secret_string
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["name"] = name
            __props__.__dict__["replica_regions"] = replica_regions
            __props__.__dict__["secret_string"] = secret_string
            __props__.__dict__["tags"] = tags
            __props__.__dict__["aws_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Secret, __self__).__init__(
            'aws-native:secretsmanager:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecretArgs.__new__(SecretArgs)

        __props__.__dict__["aws_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["generate_secret_string"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["replica_regions"] = None
        __props__.__dict__["secret_string"] = None
        __props__.__dict__["tags"] = None
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[builtins.str]:
        """
        The ARN of the secret.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the secret.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="generateSecretString")
    def generate_secret_string(self) -> pulumi.Output[Optional['outputs.SecretGenerateSecretString']]:
        """
        A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use ``SecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
         We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
        """
        return pulumi.get(self, "generate_secret_string")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by ``alias/``, for example ``alias/aws/secretsmanager``. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
         To use a KMS key in a different account, use the key ARN or the alias ARN.
         If you don't specify this value, then Secrets Manager uses the key ``aws/secretsmanager``. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.
         If the secret is in a different AWS account from the credentials calling the API, then you can't use ``aws/secretsmanager`` to encrypt the secret, and you must create and use a customer managed KMS key.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The name of the new secret.
         The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-
         Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="replicaRegions")
    def replica_regions(self) -> pulumi.Output[Optional[Sequence['outputs.SecretReplicaRegion']]]:
        """
        A custom type that specifies a ``Region`` and the ``KmsKeyId`` for a replica secret.
        """
        return pulumi.get(self, "replica_regions")

    @property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use ``GenerateSecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.
        """
        return pulumi.get(self, "secret_string")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:
          ``[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`` 
         Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".
         Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. 
         If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an ``Access Denied`` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secrets' tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2).
         For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
         The following restrictions apply to tags:
          +  Maximum number of tags per secret: 50
          +  Maximum key length: 127 Unicode characters in UTF-8
          +  Maximum value length: 255 Unicode characters in UTF-8
          +  Tag keys and values are case sensitive.
          +  Do not use the ``aws:`` prefix in your tag names or values because AWS reserves it for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.
          +  If you use your tagging schema across multiple services and resources, other services might have restrictions on allowed characters. Generally allowed characters: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
        """
        return pulumi.get(self, "tags")

