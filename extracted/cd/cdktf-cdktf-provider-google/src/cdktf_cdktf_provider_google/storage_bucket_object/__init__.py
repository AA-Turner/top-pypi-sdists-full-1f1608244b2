r'''
# `google_storage_bucket_object`

Refer to the Terraform Registry for docs: [`google_storage_bucket_object`](https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object).
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


class StorageBucketObject(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObject",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object google_storage_bucket_object}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        name: builtins.str,
        cache_control: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        customer_encryption: typing.Optional[typing.Union["StorageBucketObjectCustomerEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        detect_md5_hash: typing.Optional[builtins.str] = None,
        event_based_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_name: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        retention: typing.Optional[typing.Union["StorageBucketObjectRetention", typing.Dict[builtins.str, typing.Any]]] = None,
        source: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
        temporary_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["StorageBucketObjectTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object google_storage_bucket_object} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: The name of the containing bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#bucket StorageBucketObject#bucket}
        :param name: The name of the object. If you're interpolating the name of this object, see output_name instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#name StorageBucketObject#name}
        :param cache_control: Cache-Control directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600 Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#cache_control StorageBucketObject#cache_control}
        :param content: Data as string to be uploaded. Must be defined if source is not. Note: The content field is marked as sensitive. To view the raw contents of the object, please define an output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content StorageBucketObject#content}
        :param content_disposition: Content-Disposition of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_disposition StorageBucketObject#content_disposition}
        :param content_encoding: Content-Encoding of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_encoding StorageBucketObject#content_encoding}
        :param content_language: Content-Language of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_language StorageBucketObject#content_language}
        :param content_type: Content-Type of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_type StorageBucketObject#content_type}
        :param customer_encryption: customer_encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#customer_encryption StorageBucketObject#customer_encryption}
        :param detect_md5_hash: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#detect_md5hash StorageBucketObject#detect_md5hash}.
        :param event_based_hold: Whether an object is under event-based hold. Event-based hold is a way to retain objects until an event occurs, which is signified by the hold's release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#event_based_hold StorageBucketObject#event_based_hold}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#id StorageBucketObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_name: Resource name of the Cloud KMS key that will be used to encrypt the object. Overrides the object metadata's kmsKeyName value, if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#kms_key_name StorageBucketObject#kms_key_name}
        :param metadata: User-provided metadata, in key/value pairs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#metadata StorageBucketObject#metadata}
        :param retention: retention block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retention StorageBucketObject#retention}
        :param source: A path to the data you want to upload. Must be defined if content is not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#source StorageBucketObject#source}
        :param storage_class: The StorageClass of the new bucket object. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. If not provided, this defaults to the bucket's default storage class or to a standard class. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#storage_class StorageBucketObject#storage_class}
        :param temporary_hold: Whether an object is under temporary hold. While this flag is set to true, the object is protected against deletion and overwrites. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#temporary_hold StorageBucketObject#temporary_hold}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#timeouts StorageBucketObject#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__794434aadd39d927edec7ebaee61a263728272b226a97e54076ff7f1d5d1cf90)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageBucketObjectConfig(
            bucket=bucket,
            name=name,
            cache_control=cache_control,
            content=content,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            customer_encryption=customer_encryption,
            detect_md5_hash=detect_md5_hash,
            event_based_hold=event_based_hold,
            id=id,
            kms_key_name=kms_key_name,
            metadata=metadata,
            retention=retention,
            source=source,
            storage_class=storage_class,
            temporary_hold=temporary_hold,
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
        '''Generates CDKTF code for importing a StorageBucketObject resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the StorageBucketObject to import.
        :param import_from_id: The id of the existing StorageBucketObject that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the StorageBucketObject to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4e30195d7cfb2ef2d47bb939660dcf5cdf50251fac22181a29525b2e78c382)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCustomerEncryption")
    def put_customer_encryption(
        self,
        *,
        encryption_key: builtins.str,
        encryption_algorithm: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_key: Base64 encoded customer supplied encryption key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_key StorageBucketObject#encryption_key}
        :param encryption_algorithm: The encryption algorithm. Default: AES256. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_algorithm StorageBucketObject#encryption_algorithm}
        '''
        value = StorageBucketObjectCustomerEncryption(
            encryption_key=encryption_key, encryption_algorithm=encryption_algorithm
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerEncryption", [value]))

    @jsii.member(jsii_name="putRetention")
    def put_retention(
        self,
        *,
        mode: builtins.str,
        retain_until_time: builtins.str,
    ) -> None:
        '''
        :param mode: The object retention mode. Supported values include: "Unlocked", "Locked". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#mode StorageBucketObject#mode}
        :param retain_until_time: Time in RFC 3339 (e.g. 2030-01-01T02:03:04Z) until which object retention protects this object. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retain_until_time StorageBucketObject#retain_until_time}
        '''
        value = StorageBucketObjectRetention(
            mode=mode, retain_until_time=retain_until_time
        )

        return typing.cast(None, jsii.invoke(self, "putRetention", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#create StorageBucketObject#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#delete StorageBucketObject#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#update StorageBucketObject#update}.
        '''
        value = StorageBucketObjectTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCacheControl")
    def reset_cache_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheControl", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentDisposition")
    def reset_content_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentDisposition", []))

    @jsii.member(jsii_name="resetContentEncoding")
    def reset_content_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentEncoding", []))

    @jsii.member(jsii_name="resetContentLanguage")
    def reset_content_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentLanguage", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomerEncryption")
    def reset_customer_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerEncryption", []))

    @jsii.member(jsii_name="resetDetectMd5Hash")
    def reset_detect_md5_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetectMd5Hash", []))

    @jsii.member(jsii_name="resetEventBasedHold")
    def reset_event_based_hold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBasedHold", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyName")
    def reset_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyName", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetRetention")
    def reset_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetention", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @jsii.member(jsii_name="resetTemporaryHold")
    def reset_temporary_hold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemporaryHold", []))

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
    @jsii.member(jsii_name="crc32C")
    def crc32_c(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crc32C"))

    @builtins.property
    @jsii.member(jsii_name="customerEncryption")
    def customer_encryption(
        self,
    ) -> "StorageBucketObjectCustomerEncryptionOutputReference":
        return typing.cast("StorageBucketObjectCustomerEncryptionOutputReference", jsii.get(self, "customerEncryption"))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="md5Hash")
    def md5_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "md5Hash"))

    @builtins.property
    @jsii.member(jsii_name="md5Hexhash")
    def md5_hexhash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "md5Hexhash"))

    @builtins.property
    @jsii.member(jsii_name="mediaLink")
    def media_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediaLink"))

    @builtins.property
    @jsii.member(jsii_name="outputName")
    def output_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputName"))

    @builtins.property
    @jsii.member(jsii_name="retention")
    def retention(self) -> "StorageBucketObjectRetentionOutputReference":
        return typing.cast("StorageBucketObjectRetentionOutputReference", jsii.get(self, "retention"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageBucketObjectTimeoutsOutputReference":
        return typing.cast("StorageBucketObjectTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheControlInput")
    def cache_control_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheControlInput"))

    @builtins.property
    @jsii.member(jsii_name="contentDispositionInput")
    def content_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncodingInput")
    def content_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentLanguageInput")
    def content_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customerEncryptionInput")
    def customer_encryption_input(
        self,
    ) -> typing.Optional["StorageBucketObjectCustomerEncryption"]:
        return typing.cast(typing.Optional["StorageBucketObjectCustomerEncryption"], jsii.get(self, "customerEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="detectMd5HashInput")
    def detect_md5_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectMd5HashInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBasedHoldInput")
    def event_based_hold_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "eventBasedHoldInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInput")
    def retention_input(self) -> typing.Optional["StorageBucketObjectRetention"]:
        return typing.cast(typing.Optional["StorageBucketObjectRetention"], jsii.get(self, "retentionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="temporaryHoldInput")
    def temporary_hold_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "temporaryHoldInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "StorageBucketObjectTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "StorageBucketObjectTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__201fb6995c5efddb79e41043dba33ce0c445f3fa97898b38c44e0287f248c63e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cacheControl")
    def cache_control(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheControl"))

    @cache_control.setter
    def cache_control(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5408371e18f306fb4448de197de7daa49f9409a0745a1c1da2b009f793ca017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheControl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3281cdf7a7c76cf0a998112c6d95add81c2ed0c6c5553ee06e40332295699976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentDisposition")
    def content_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentDisposition"))

    @content_disposition.setter
    def content_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9feb1c51a6013a85f0f79f91399f230ceeb12ae4d37ee7cf2603849a314cb42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentDisposition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentEncoding")
    def content_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentEncoding"))

    @content_encoding.setter
    def content_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34cfebabc068fa2ab36b60a0be86fd7546599bd9ea97b2d973f32d83ed9dff8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentEncoding", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentLanguage")
    def content_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentLanguage"))

    @content_language.setter
    def content_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc93aec6c221f6bdd6c05fb4b2f5fe3a784856f8cdafe3f8ea8412167816956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentLanguage", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0416de40d08906645dafa52c777b5060682dc6f97857f856a394988b26cc49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="detectMd5Hash")
    def detect_md5_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectMd5Hash"))

    @detect_md5_hash.setter
    def detect_md5_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e688f5b45d1fcc9c8ca6dad1d1322d69e979c20ae3e67bfeef0ac7a471849b02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectMd5Hash", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventBasedHold")
    def event_based_hold(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "eventBasedHold"))

    @event_based_hold.setter
    def event_based_hold(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2df5584ff695486260479c3e50950ad15bd8cc25fd1a1587c98d3cf73403d2c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBasedHold", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa631608c2859fe34c418bbac3b2d505546321ad18d49d52c78943949937a74e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2dee5a572d80993ee057f35102cb7c5e86b52d6a9cd29ecec102b4ef288ffad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879cc7195ac0a9b30f706696708b120259d6fc3e2bb2a665bd7785b5b72b01ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3313c9af3f622184231a7b08d4f9f5676b5b1535eabb2199a96c3f485ad474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8782314f9e3ac95f650ac0bc4992d774a8c1f185b7fd5cd37e0eb15329cf20cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2319204cd3ea22e84c1f84c6129771770c521bfd44b915ce153f1169d71d570a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="temporaryHold")
    def temporary_hold(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "temporaryHold"))

    @temporary_hold.setter
    def temporary_hold(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f7f5963a7da8cbfb42af8cab9126b505956bdd38b96bfb3ece3b6cece0a5f33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "temporaryHold", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "name": "name",
        "cache_control": "cacheControl",
        "content": "content",
        "content_disposition": "contentDisposition",
        "content_encoding": "contentEncoding",
        "content_language": "contentLanguage",
        "content_type": "contentType",
        "customer_encryption": "customerEncryption",
        "detect_md5_hash": "detectMd5Hash",
        "event_based_hold": "eventBasedHold",
        "id": "id",
        "kms_key_name": "kmsKeyName",
        "metadata": "metadata",
        "retention": "retention",
        "source": "source",
        "storage_class": "storageClass",
        "temporary_hold": "temporaryHold",
        "timeouts": "timeouts",
    },
)
class StorageBucketObjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        name: builtins.str,
        cache_control: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        customer_encryption: typing.Optional[typing.Union["StorageBucketObjectCustomerEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        detect_md5_hash: typing.Optional[builtins.str] = None,
        event_based_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_name: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        retention: typing.Optional[typing.Union["StorageBucketObjectRetention", typing.Dict[builtins.str, typing.Any]]] = None,
        source: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
        temporary_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["StorageBucketObjectTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: The name of the containing bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#bucket StorageBucketObject#bucket}
        :param name: The name of the object. If you're interpolating the name of this object, see output_name instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#name StorageBucketObject#name}
        :param cache_control: Cache-Control directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600 Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#cache_control StorageBucketObject#cache_control}
        :param content: Data as string to be uploaded. Must be defined if source is not. Note: The content field is marked as sensitive. To view the raw contents of the object, please define an output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content StorageBucketObject#content}
        :param content_disposition: Content-Disposition of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_disposition StorageBucketObject#content_disposition}
        :param content_encoding: Content-Encoding of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_encoding StorageBucketObject#content_encoding}
        :param content_language: Content-Language of the object data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_language StorageBucketObject#content_language}
        :param content_type: Content-Type of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_type StorageBucketObject#content_type}
        :param customer_encryption: customer_encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#customer_encryption StorageBucketObject#customer_encryption}
        :param detect_md5_hash: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#detect_md5hash StorageBucketObject#detect_md5hash}.
        :param event_based_hold: Whether an object is under event-based hold. Event-based hold is a way to retain objects until an event occurs, which is signified by the hold's release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#event_based_hold StorageBucketObject#event_based_hold}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#id StorageBucketObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_name: Resource name of the Cloud KMS key that will be used to encrypt the object. Overrides the object metadata's kmsKeyName value, if any. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#kms_key_name StorageBucketObject#kms_key_name}
        :param metadata: User-provided metadata, in key/value pairs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#metadata StorageBucketObject#metadata}
        :param retention: retention block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retention StorageBucketObject#retention}
        :param source: A path to the data you want to upload. Must be defined if content is not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#source StorageBucketObject#source}
        :param storage_class: The StorageClass of the new bucket object. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. If not provided, this defaults to the bucket's default storage class or to a standard class. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#storage_class StorageBucketObject#storage_class}
        :param temporary_hold: Whether an object is under temporary hold. While this flag is set to true, the object is protected against deletion and overwrites. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#temporary_hold StorageBucketObject#temporary_hold}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#timeouts StorageBucketObject#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(customer_encryption, dict):
            customer_encryption = StorageBucketObjectCustomerEncryption(**customer_encryption)
        if isinstance(retention, dict):
            retention = StorageBucketObjectRetention(**retention)
        if isinstance(timeouts, dict):
            timeouts = StorageBucketObjectTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003ceab1734545ef35a4a1a63c0b18a5bdfa1d4f740e4a54c709bb88d6c9091c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cache_control", value=cache_control, expected_type=type_hints["cache_control"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_disposition", value=content_disposition, expected_type=type_hints["content_disposition"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            check_type(argname="argument content_language", value=content_language, expected_type=type_hints["content_language"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument customer_encryption", value=customer_encryption, expected_type=type_hints["customer_encryption"])
            check_type(argname="argument detect_md5_hash", value=detect_md5_hash, expected_type=type_hints["detect_md5_hash"])
            check_type(argname="argument event_based_hold", value=event_based_hold, expected_type=type_hints["event_based_hold"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument temporary_hold", value=temporary_hold, expected_type=type_hints["temporary_hold"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "name": name,
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
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if content is not None:
            self._values["content"] = content
        if content_disposition is not None:
            self._values["content_disposition"] = content_disposition
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding
        if content_language is not None:
            self._values["content_language"] = content_language
        if content_type is not None:
            self._values["content_type"] = content_type
        if customer_encryption is not None:
            self._values["customer_encryption"] = customer_encryption
        if detect_md5_hash is not None:
            self._values["detect_md5_hash"] = detect_md5_hash
        if event_based_hold is not None:
            self._values["event_based_hold"] = event_based_hold
        if id is not None:
            self._values["id"] = id
        if kms_key_name is not None:
            self._values["kms_key_name"] = kms_key_name
        if metadata is not None:
            self._values["metadata"] = metadata
        if retention is not None:
            self._values["retention"] = retention
        if source is not None:
            self._values["source"] = source
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if temporary_hold is not None:
            self._values["temporary_hold"] = temporary_hold
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
    def bucket(self) -> builtins.str:
        '''The name of the containing bucket.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#bucket StorageBucketObject#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the object. If you're interpolating the name of this object, see output_name instead.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#name StorageBucketObject#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_control(self) -> typing.Optional[builtins.str]:
        '''Cache-Control directive to specify caching behavior of object data.

        If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#cache_control StorageBucketObject#cache_control}
        '''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Data as string to be uploaded.

        Must be defined if source is not. Note: The content field is marked as sensitive. To view the raw contents of the object, please define an output.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content StorageBucketObject#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_disposition(self) -> typing.Optional[builtins.str]:
        '''Content-Disposition of the object data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_disposition StorageBucketObject#content_disposition}
        '''
        result = self._values.get("content_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''Content-Encoding of the object data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_encoding StorageBucketObject#content_encoding}
        '''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_language(self) -> typing.Optional[builtins.str]:
        '''Content-Language of the object data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_language StorageBucketObject#content_language}
        '''
        result = self._values.get("content_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Content-Type of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#content_type StorageBucketObject#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_encryption(
        self,
    ) -> typing.Optional["StorageBucketObjectCustomerEncryption"]:
        '''customer_encryption block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#customer_encryption StorageBucketObject#customer_encryption}
        '''
        result = self._values.get("customer_encryption")
        return typing.cast(typing.Optional["StorageBucketObjectCustomerEncryption"], result)

    @builtins.property
    def detect_md5_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#detect_md5hash StorageBucketObject#detect_md5hash}.'''
        result = self._values.get("detect_md5_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_based_hold(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether an object is under event-based hold.

        Event-based hold is a way to retain objects until an event occurs, which is signified by the hold's release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#event_based_hold StorageBucketObject#event_based_hold}
        '''
        result = self._values.get("event_based_hold")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#id StorageBucketObject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_name(self) -> typing.Optional[builtins.str]:
        '''Resource name of the Cloud KMS key that will be used to encrypt the object.

        Overrides the object metadata's kmsKeyName value, if any.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#kms_key_name StorageBucketObject#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-provided metadata, in key/value pairs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#metadata StorageBucketObject#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def retention(self) -> typing.Optional["StorageBucketObjectRetention"]:
        '''retention block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retention StorageBucketObject#retention}
        '''
        result = self._values.get("retention")
        return typing.cast(typing.Optional["StorageBucketObjectRetention"], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''A path to the data you want to upload. Must be defined if content is not.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#source StorageBucketObject#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The StorageClass of the new bucket object.

        Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. If not provided, this defaults to the bucket's default storage class or to a standard class.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#storage_class StorageBucketObject#storage_class}
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temporary_hold(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether an object is under temporary hold.

        While this flag is set to true, the object is protected against deletion and overwrites.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#temporary_hold StorageBucketObject#temporary_hold}
        '''
        result = self._values.get("temporary_hold")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageBucketObjectTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#timeouts StorageBucketObject#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageBucketObjectTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBucketObjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectCustomerEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_key": "encryptionKey",
        "encryption_algorithm": "encryptionAlgorithm",
    },
)
class StorageBucketObjectCustomerEncryption:
    def __init__(
        self,
        *,
        encryption_key: builtins.str,
        encryption_algorithm: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_key: Base64 encoded customer supplied encryption key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_key StorageBucketObject#encryption_key}
        :param encryption_algorithm: The encryption algorithm. Default: AES256. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_algorithm StorageBucketObject#encryption_algorithm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011e310636edd47dc12206cabd4e6340d136449a504de44897c1aca44dc71192)
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument encryption_algorithm", value=encryption_algorithm, expected_type=type_hints["encryption_algorithm"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_key": encryption_key,
        }
        if encryption_algorithm is not None:
            self._values["encryption_algorithm"] = encryption_algorithm

    @builtins.property
    def encryption_key(self) -> builtins.str:
        '''Base64 encoded customer supplied encryption key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_key StorageBucketObject#encryption_key}
        '''
        result = self._values.get("encryption_key")
        assert result is not None, "Required property 'encryption_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_algorithm(self) -> typing.Optional[builtins.str]:
        '''The encryption algorithm. Default: AES256.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#encryption_algorithm StorageBucketObject#encryption_algorithm}
        '''
        result = self._values.get("encryption_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBucketObjectCustomerEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBucketObjectCustomerEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectCustomerEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbaccd7aa28f031f86c56ae8adeee4a60f84c7521ee3a566c0133113bdb63e11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEncryptionAlgorithm")
    def reset_encryption_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAlgorithm", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithmInput")
    def encryption_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyInput")
    def encryption_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithm")
    def encryption_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionAlgorithm"))

    @encryption_algorithm.setter
    def encryption_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59329e048a63fddc38b41fe6a27a96b909f225a81234e1ca3aa9aecb5e90b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAlgorithm", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dda6f87fa33c8b694dd472d4d03fd0bc0ade2ab7aaa8a2da412a71d31e7b51c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageBucketObjectCustomerEncryption]:
        return typing.cast(typing.Optional[StorageBucketObjectCustomerEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageBucketObjectCustomerEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d561625048f0f37253901a72c5ecb1fd6d1deddfbe71148f0818dd7d1c8affa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectRetention",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "retain_until_time": "retainUntilTime"},
)
class StorageBucketObjectRetention:
    def __init__(self, *, mode: builtins.str, retain_until_time: builtins.str) -> None:
        '''
        :param mode: The object retention mode. Supported values include: "Unlocked", "Locked". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#mode StorageBucketObject#mode}
        :param retain_until_time: Time in RFC 3339 (e.g. 2030-01-01T02:03:04Z) until which object retention protects this object. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retain_until_time StorageBucketObject#retain_until_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d758485e6a11d02ffb44fdad5247b896e231ccc46c385a9fa78a6800e189592e)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument retain_until_time", value=retain_until_time, expected_type=type_hints["retain_until_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
            "retain_until_time": retain_until_time,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''The object retention mode. Supported values include: "Unlocked", "Locked".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#mode StorageBucketObject#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retain_until_time(self) -> builtins.str:
        '''Time in RFC 3339 (e.g. 2030-01-01T02:03:04Z) until which object retention protects this object.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#retain_until_time StorageBucketObject#retain_until_time}
        '''
        result = self._values.get("retain_until_time")
        assert result is not None, "Required property 'retain_until_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBucketObjectRetention(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBucketObjectRetentionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectRetentionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64bac120467f68e38fb314bd96f374957d4d2eca299d1409b7387076b0d7b2f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="retainUntilTimeInput")
    def retain_until_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retainUntilTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3606fab23af56c52bd55d2e4e616e2a45525ba439cabce2adb323ebe3d312e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retainUntilTime")
    def retain_until_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retainUntilTime"))

    @retain_until_time.setter
    def retain_until_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34255997de4b5aefa07d3507b12c42efe8eaa6790e5e0e2a8c2a191d5c705f29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainUntilTime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageBucketObjectRetention]:
        return typing.cast(typing.Optional[StorageBucketObjectRetention], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageBucketObjectRetention],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f33bd24a166f342d624de176a5aa63ce19a84dfa2924892c684636538f50ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class StorageBucketObjectTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#create StorageBucketObject#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#delete StorageBucketObject#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#update StorageBucketObject#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459f0971bc8f9a343bda38d44c558d0a9cc69466a7f6ef3ae94978378dd97aac)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#create StorageBucketObject#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#delete StorageBucketObject#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/6.38.0/docs/resources/storage_bucket_object#update StorageBucketObject#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBucketObjectTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBucketObjectTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.storageBucketObject.StorageBucketObjectTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5c680dd8b565a7e96f2f0a03e1353f1e7897db1492202c9defdc9b11297ffef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__373814d9b349a8d85b4653246ae27e436266758198e4d8e1607364feebb2dbaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa04adfcc36f6aa91d46f588ff45d2f3b80e7be0125ca852b142e2a7852089eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90fbe717a10c0c74d60c301abadaa3329f328511faec4f22557280586f6c6c99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageBucketObjectTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageBucketObjectTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageBucketObjectTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66289a1b19ebd17d0edffeed47e3fed6e4a5bfe46bbf40ef62d8df6c07bf6cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "StorageBucketObject",
    "StorageBucketObjectConfig",
    "StorageBucketObjectCustomerEncryption",
    "StorageBucketObjectCustomerEncryptionOutputReference",
    "StorageBucketObjectRetention",
    "StorageBucketObjectRetentionOutputReference",
    "StorageBucketObjectTimeouts",
    "StorageBucketObjectTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__794434aadd39d927edec7ebaee61a263728272b226a97e54076ff7f1d5d1cf90(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    name: builtins.str,
    cache_control: typing.Optional[builtins.str] = None,
    content: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    customer_encryption: typing.Optional[typing.Union[StorageBucketObjectCustomerEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    detect_md5_hash: typing.Optional[builtins.str] = None,
    event_based_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_name: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    retention: typing.Optional[typing.Union[StorageBucketObjectRetention, typing.Dict[builtins.str, typing.Any]]] = None,
    source: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
    temporary_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[StorageBucketObjectTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7e4e30195d7cfb2ef2d47bb939660dcf5cdf50251fac22181a29525b2e78c382(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201fb6995c5efddb79e41043dba33ce0c445f3fa97898b38c44e0287f248c63e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5408371e18f306fb4448de197de7daa49f9409a0745a1c1da2b009f793ca017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3281cdf7a7c76cf0a998112c6d95add81c2ed0c6c5553ee06e40332295699976(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9feb1c51a6013a85f0f79f91399f230ceeb12ae4d37ee7cf2603849a314cb42f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34cfebabc068fa2ab36b60a0be86fd7546599bd9ea97b2d973f32d83ed9dff8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc93aec6c221f6bdd6c05fb4b2f5fe3a784856f8cdafe3f8ea8412167816956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0416de40d08906645dafa52c777b5060682dc6f97857f856a394988b26cc49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e688f5b45d1fcc9c8ca6dad1d1322d69e979c20ae3e67bfeef0ac7a471849b02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df5584ff695486260479c3e50950ad15bd8cc25fd1a1587c98d3cf73403d2c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa631608c2859fe34c418bbac3b2d505546321ad18d49d52c78943949937a74e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2dee5a572d80993ee057f35102cb7c5e86b52d6a9cd29ecec102b4ef288ffad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879cc7195ac0a9b30f706696708b120259d6fc3e2bb2a665bd7785b5b72b01ec(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3313c9af3f622184231a7b08d4f9f5676b5b1535eabb2199a96c3f485ad474(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8782314f9e3ac95f650ac0bc4992d774a8c1f185b7fd5cd37e0eb15329cf20cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2319204cd3ea22e84c1f84c6129771770c521bfd44b915ce153f1169d71d570a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7f5963a7da8cbfb42af8cab9126b505956bdd38b96bfb3ece3b6cece0a5f33(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003ceab1734545ef35a4a1a63c0b18a5bdfa1d4f740e4a54c709bb88d6c9091c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    name: builtins.str,
    cache_control: typing.Optional[builtins.str] = None,
    content: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    customer_encryption: typing.Optional[typing.Union[StorageBucketObjectCustomerEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    detect_md5_hash: typing.Optional[builtins.str] = None,
    event_based_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_name: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    retention: typing.Optional[typing.Union[StorageBucketObjectRetention, typing.Dict[builtins.str, typing.Any]]] = None,
    source: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
    temporary_hold: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[StorageBucketObjectTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011e310636edd47dc12206cabd4e6340d136449a504de44897c1aca44dc71192(
    *,
    encryption_key: builtins.str,
    encryption_algorithm: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbaccd7aa28f031f86c56ae8adeee4a60f84c7521ee3a566c0133113bdb63e11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59329e048a63fddc38b41fe6a27a96b909f225a81234e1ca3aa9aecb5e90b44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda6f87fa33c8b694dd472d4d03fd0bc0ade2ab7aaa8a2da412a71d31e7b51c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d561625048f0f37253901a72c5ecb1fd6d1deddfbe71148f0818dd7d1c8affa(
    value: typing.Optional[StorageBucketObjectCustomerEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d758485e6a11d02ffb44fdad5247b896e231ccc46c385a9fa78a6800e189592e(
    *,
    mode: builtins.str,
    retain_until_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64bac120467f68e38fb314bd96f374957d4d2eca299d1409b7387076b0d7b2f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3606fab23af56c52bd55d2e4e616e2a45525ba439cabce2adb323ebe3d312e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34255997de4b5aefa07d3507b12c42efe8eaa6790e5e0e2a8c2a191d5c705f29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f33bd24a166f342d624de176a5aa63ce19a84dfa2924892c684636538f50ab3(
    value: typing.Optional[StorageBucketObjectRetention],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459f0971bc8f9a343bda38d44c558d0a9cc69466a7f6ef3ae94978378dd97aac(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c680dd8b565a7e96f2f0a03e1353f1e7897db1492202c9defdc9b11297ffef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373814d9b349a8d85b4653246ae27e436266758198e4d8e1607364feebb2dbaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa04adfcc36f6aa91d46f588ff45d2f3b80e7be0125ca852b142e2a7852089eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90fbe717a10c0c74d60c301abadaa3329f328511faec4f22557280586f6c6c99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66289a1b19ebd17d0edffeed47e3fed6e4a5bfe46bbf40ef62d8df6c07bf6cda(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageBucketObjectTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
