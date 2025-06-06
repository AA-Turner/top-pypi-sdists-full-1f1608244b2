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

__all__ = [
    'EventActionAction',
    'EventActionActionExportRevisionToS3',
    'EventActionActionExportRevisionToS3Encryption',
    'EventActionActionExportRevisionToS3RevisionDestination',
    'EventActionEvent',
    'EventActionEventRevisionPublished',
    'RevisionAssetsAsset',
    'RevisionAssetsAssetCreateS3DataAccessFromS3Bucket',
    'RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource',
    'RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant',
    'RevisionAssetsAssetImportAssetsFromS3',
    'RevisionAssetsAssetImportAssetsFromS3AssetSource',
    'RevisionAssetsAssetImportAssetsFromSignedUrl',
    'RevisionAssetsTimeouts',
]

@pulumi.output_type
class EventActionAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "exportRevisionToS3":
            suggest = "export_revision_to_s3"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 export_revision_to_s3: Optional['outputs.EventActionActionExportRevisionToS3'] = None):
        """
        :param 'EventActionActionExportRevisionToS3Args' export_revision_to_s3: Configuration for an Export Revision to S3 action.
               Described in `export_revision_to_s3` Configuration Block
        """
        if export_revision_to_s3 is not None:
            pulumi.set(__self__, "export_revision_to_s3", export_revision_to_s3)

    @property
    @pulumi.getter(name="exportRevisionToS3")
    def export_revision_to_s3(self) -> Optional['outputs.EventActionActionExportRevisionToS3']:
        """
        Configuration for an Export Revision to S3 action.
        Described in `export_revision_to_s3` Configuration Block
        """
        return pulumi.get(self, "export_revision_to_s3")


@pulumi.output_type
class EventActionActionExportRevisionToS3(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "revisionDestination":
            suggest = "revision_destination"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionActionExportRevisionToS3. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionActionExportRevisionToS3.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionActionExportRevisionToS3.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption: Optional['outputs.EventActionActionExportRevisionToS3Encryption'] = None,
                 revision_destination: Optional['outputs.EventActionActionExportRevisionToS3RevisionDestination'] = None):
        """
        :param 'EventActionActionExportRevisionToS3EncryptionArgs' encryption: Configures server-side encryption of the exported revision.
               Described in `encryption` Configuration Block below.
        :param 'EventActionActionExportRevisionToS3RevisionDestinationArgs' revision_destination: Configures the S3 destination of the exported revision.
               Described in `revision_destination` Configuration Block below.
        """
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if revision_destination is not None:
            pulumi.set(__self__, "revision_destination", revision_destination)

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EventActionActionExportRevisionToS3Encryption']:
        """
        Configures server-side encryption of the exported revision.
        Described in `encryption` Configuration Block below.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="revisionDestination")
    def revision_destination(self) -> Optional['outputs.EventActionActionExportRevisionToS3RevisionDestination']:
        """
        Configures the S3 destination of the exported revision.
        Described in `revision_destination` Configuration Block below.
        """
        return pulumi.get(self, "revision_destination")


@pulumi.output_type
class EventActionActionExportRevisionToS3Encryption(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyArn":
            suggest = "kms_key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionActionExportRevisionToS3Encryption. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionActionExportRevisionToS3Encryption.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionActionExportRevisionToS3Encryption.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key_arn: Optional[builtins.str] = None,
                 type: Optional[builtins.str] = None):
        """
        :param builtins.str kms_key_arn: ARN of the KMS key used for encryption.
        :param builtins.str type: Type of server-side encryption.
               Valid values are `aws:kms` or `aws:s3`.
        """
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[builtins.str]:
        """
        ARN of the KMS key used for encryption.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter
    def type(self) -> Optional[builtins.str]:
        """
        Type of server-side encryption.
        Valid values are `aws:kms` or `aws:s3`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class EventActionActionExportRevisionToS3RevisionDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyPattern":
            suggest = "key_pattern"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionActionExportRevisionToS3RevisionDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionActionExportRevisionToS3RevisionDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionActionExportRevisionToS3RevisionDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket: builtins.str,
                 key_pattern: Optional[builtins.str] = None):
        """
        :param builtins.str bucket: The S3 bucket where the revision will be exported.
        :param builtins.str key_pattern: Pattern for naming revisions in the S3 bucket.
               Defaults to `${Revision.CreatedAt}/${Asset.Name}`.
        """
        pulumi.set(__self__, "bucket", bucket)
        if key_pattern is not None:
            pulumi.set(__self__, "key_pattern", key_pattern)

    @property
    @pulumi.getter
    def bucket(self) -> builtins.str:
        """
        The S3 bucket where the revision will be exported.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="keyPattern")
    def key_pattern(self) -> Optional[builtins.str]:
        """
        Pattern for naming revisions in the S3 bucket.
        Defaults to `${Revision.CreatedAt}/${Asset.Name}`.
        """
        return pulumi.get(self, "key_pattern")


@pulumi.output_type
class EventActionEvent(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "revisionPublished":
            suggest = "revision_published"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionEvent. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionEvent.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionEvent.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 revision_published: Optional['outputs.EventActionEventRevisionPublished'] = None):
        """
        :param 'EventActionEventRevisionPublishedArgs' revision_published: Configuration for a Revision Published event.
               Described in `revision_published` Configuration Block below.
        """
        if revision_published is not None:
            pulumi.set(__self__, "revision_published", revision_published)

    @property
    @pulumi.getter(name="revisionPublished")
    def revision_published(self) -> Optional['outputs.EventActionEventRevisionPublished']:
        """
        Configuration for a Revision Published event.
        Described in `revision_published` Configuration Block below.
        """
        return pulumi.get(self, "revision_published")


@pulumi.output_type
class EventActionEventRevisionPublished(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataSetId":
            suggest = "data_set_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EventActionEventRevisionPublished. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EventActionEventRevisionPublished.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EventActionEventRevisionPublished.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_set_id: builtins.str):
        """
        :param builtins.str data_set_id: The ID of the data set to monitor for revision publications.
               Changing this value will recreate the resource.
        """
        pulumi.set(__self__, "data_set_id", data_set_id)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> builtins.str:
        """
        The ID of the data set to monitor for revision publications.
        Changing this value will recreate the resource.
        """
        return pulumi.get(self, "data_set_id")


@pulumi.output_type
class RevisionAssetsAsset(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createS3DataAccessFromS3Bucket":
            suggest = "create_s3_data_access_from_s3_bucket"
        elif key == "createdAt":
            suggest = "created_at"
        elif key == "importAssetsFromS3":
            suggest = "import_assets_from_s3"
        elif key == "importAssetsFromSignedUrl":
            suggest = "import_assets_from_signed_url"
        elif key == "updatedAt":
            suggest = "updated_at"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RevisionAssetsAsset. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RevisionAssetsAsset.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RevisionAssetsAsset.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 arn: Optional[builtins.str] = None,
                 create_s3_data_access_from_s3_bucket: Optional['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3Bucket'] = None,
                 created_at: Optional[builtins.str] = None,
                 id: Optional[builtins.str] = None,
                 import_assets_from_s3: Optional['outputs.RevisionAssetsAssetImportAssetsFromS3'] = None,
                 import_assets_from_signed_url: Optional['outputs.RevisionAssetsAssetImportAssetsFromSignedUrl'] = None,
                 name: Optional[builtins.str] = None,
                 updated_at: Optional[builtins.str] = None):
        """
        :param builtins.str arn: The ARN of the Data Exchange Revision Assets.
        :param 'RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgs' create_s3_data_access_from_s3_bucket: A block to create S3 data access from an S3 bucket. See Create S3 Data Access from S3 Bucket for more details.
        :param builtins.str created_at: The timestamp when the revision was created, in RFC3339 format.
        :param builtins.str id: The unique identifier for the revision.
        :param 'RevisionAssetsAssetImportAssetsFromS3Args' import_assets_from_s3: A block to import assets from S3. See Import Assets from S3 for more details.
        :param 'RevisionAssetsAssetImportAssetsFromSignedUrlArgs' import_assets_from_signed_url: A block to import assets from a signed URL. See Import Assets from Signed URL for more details.
        :param builtins.str updated_at: The timestamp when the revision was last updated, in RFC3339 format.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if create_s3_data_access_from_s3_bucket is not None:
            pulumi.set(__self__, "create_s3_data_access_from_s3_bucket", create_s3_data_access_from_s3_bucket)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if import_assets_from_s3 is not None:
            pulumi.set(__self__, "import_assets_from_s3", import_assets_from_s3)
        if import_assets_from_signed_url is not None:
            pulumi.set(__self__, "import_assets_from_signed_url", import_assets_from_signed_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def arn(self) -> Optional[builtins.str]:
        """
        The ARN of the Data Exchange Revision Assets.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createS3DataAccessFromS3Bucket")
    def create_s3_data_access_from_s3_bucket(self) -> Optional['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3Bucket']:
        """
        A block to create S3 data access from an S3 bucket. See Create S3 Data Access from S3 Bucket for more details.
        """
        return pulumi.get(self, "create_s3_data_access_from_s3_bucket")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[builtins.str]:
        """
        The timestamp when the revision was created, in RFC3339 format.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        The unique identifier for the revision.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="importAssetsFromS3")
    def import_assets_from_s3(self) -> Optional['outputs.RevisionAssetsAssetImportAssetsFromS3']:
        """
        A block to import assets from S3. See Import Assets from S3 for more details.
        """
        return pulumi.get(self, "import_assets_from_s3")

    @property
    @pulumi.getter(name="importAssetsFromSignedUrl")
    def import_assets_from_signed_url(self) -> Optional['outputs.RevisionAssetsAssetImportAssetsFromSignedUrl']:
        """
        A block to import assets from a signed URL. See Import Assets from Signed URL for more details.
        """
        return pulumi.get(self, "import_assets_from_signed_url")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[builtins.str]:
        """
        The timestamp when the revision was last updated, in RFC3339 format.
        """
        return pulumi.get(self, "updated_at")


@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3Bucket(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessPointAlias":
            suggest = "access_point_alias"
        elif key == "accessPointArn":
            suggest = "access_point_arn"
        elif key == "assetSource":
            suggest = "asset_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RevisionAssetsAssetCreateS3DataAccessFromS3Bucket. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3Bucket.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3Bucket.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_point_alias: Optional[builtins.str] = None,
                 access_point_arn: Optional[builtins.str] = None,
                 asset_source: Optional['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource'] = None):
        """
        :param 'RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgs' asset_source: A block specifying the source bucket for the asset. This block supports the following:
        """
        if access_point_alias is not None:
            pulumi.set(__self__, "access_point_alias", access_point_alias)
        if access_point_arn is not None:
            pulumi.set(__self__, "access_point_arn", access_point_arn)
        if asset_source is not None:
            pulumi.set(__self__, "asset_source", asset_source)

    @property
    @pulumi.getter(name="accessPointAlias")
    def access_point_alias(self) -> Optional[builtins.str]:
        return pulumi.get(self, "access_point_alias")

    @property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> Optional[builtins.str]:
        return pulumi.get(self, "access_point_arn")

    @property
    @pulumi.getter(name="assetSource")
    def asset_source(self) -> Optional['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource']:
        """
        A block specifying the source bucket for the asset. This block supports the following:
        """
        return pulumi.get(self, "asset_source")


@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyPrefixes":
            suggest = "key_prefixes"
        elif key == "kmsKeysToGrants":
            suggest = "kms_keys_to_grants"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket: builtins.str,
                 key_prefixes: Optional[Sequence[builtins.str]] = None,
                 keys: Optional[Sequence[builtins.str]] = None,
                 kms_keys_to_grants: Optional[Sequence['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant']] = None):
        """
        :param builtins.str bucket: The name of the S3 bucket.
        :param Sequence[builtins.str] key_prefixes: List of key prefixes in the S3 bucket.
        :param Sequence[builtins.str] keys: List of object keys in the S3 bucket.
        """
        pulumi.set(__self__, "bucket", bucket)
        if key_prefixes is not None:
            pulumi.set(__self__, "key_prefixes", key_prefixes)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if kms_keys_to_grants is not None:
            pulumi.set(__self__, "kms_keys_to_grants", kms_keys_to_grants)

    @property
    @pulumi.getter
    def bucket(self) -> builtins.str:
        """
        The name of the S3 bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="keyPrefixes")
    def key_prefixes(self) -> Optional[Sequence[builtins.str]]:
        """
        List of key prefixes in the S3 bucket.
        """
        return pulumi.get(self, "key_prefixes")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[builtins.str]]:
        """
        List of object keys in the S3 bucket.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="kmsKeysToGrants")
    def kms_keys_to_grants(self) -> Optional[Sequence['outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant']]:
        return pulumi.get(self, "kms_keys_to_grants")


@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsKeyArn":
            suggest = "kms_key_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_key_arn: builtins.str):
        """
        :param builtins.str kms_key_arn: The ARN of the KMS key.
        """
        pulumi.set(__self__, "kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        """
        The ARN of the KMS key.
        """
        return pulumi.get(self, "kms_key_arn")


@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromS3(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assetSource":
            suggest = "asset_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RevisionAssetsAssetImportAssetsFromS3. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RevisionAssetsAssetImportAssetsFromS3.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RevisionAssetsAssetImportAssetsFromS3.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 asset_source: Optional['outputs.RevisionAssetsAssetImportAssetsFromS3AssetSource'] = None):
        """
        :param 'RevisionAssetsAssetImportAssetsFromS3AssetSourceArgs' asset_source: A block specifying the source bucket and key for the asset. This block supports the following:
        """
        if asset_source is not None:
            pulumi.set(__self__, "asset_source", asset_source)

    @property
    @pulumi.getter(name="assetSource")
    def asset_source(self) -> Optional['outputs.RevisionAssetsAssetImportAssetsFromS3AssetSource']:
        """
        A block specifying the source bucket and key for the asset. This block supports the following:
        """
        return pulumi.get(self, "asset_source")


@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromS3AssetSource(dict):
    def __init__(__self__, *,
                 bucket: builtins.str,
                 key: builtins.str):
        """
        :param builtins.str bucket: The name of the S3 bucket.
        :param builtins.str key: The key of the object in the S3 bucket.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def bucket(self) -> builtins.str:
        """
        The name of the S3 bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def key(self) -> builtins.str:
        """
        The key of the object in the S3 bucket.
        """
        return pulumi.get(self, "key")


@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromSignedUrl(dict):
    def __init__(__self__, *,
                 filename: builtins.str):
        """
        :param builtins.str filename: The name of the file to import.
        """
        pulumi.set(__self__, "filename", filename)

    @property
    @pulumi.getter
    def filename(self) -> builtins.str:
        """
        The name of the file to import.
        """
        return pulumi.get(self, "filename")


@pulumi.output_type
class RevisionAssetsTimeouts(dict):
    def __init__(__self__, *,
                 create: Optional[builtins.str] = None):
        """
        :param builtins.str create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)

    @property
    @pulumi.getter
    def create(self) -> Optional[builtins.str]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "create")


