# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode',
    'DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod',
    'DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode',
    'DeliveryStreamAuthenticationConfigurationConnectivity',
    'DeliveryStreamDatabaseSourceConfigurationSslMode',
    'DeliveryStreamDatabaseSourceConfigurationType',
    'DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat',
    'DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod',
    'DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode',
    'DeliveryStreamEncryptionConfigurationInputKeyType',
    'DeliveryStreamEncryptionConfigurationNoEncryptionConfig',
    'DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat',
    'DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode',
    'DeliveryStreamHttpEndpointRequestConfigurationContentEncoding',
    'DeliveryStreamIcebergDestinationConfigurations3BackupMode',
    'DeliveryStreamProcessorType',
    'DeliveryStreamRedshiftDestinationConfigurationS3BackupMode',
    'DeliveryStreamS3DestinationConfigurationCompressionFormat',
    'DeliveryStreamSnowflakeDestinationConfigurationDataLoadingOption',
    'DeliveryStreamSnowflakeDestinationConfigurationS3BackupMode',
    'DeliveryStreamSplunkDestinationConfigurationHecEndpointType',
    'DeliveryStreamType',
]


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode")
class DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
    """
    FAILED_DOCUMENTS_ONLY = "FailedDocumentsOnly"
    ALL_DOCUMENTS = "AllDocuments"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod")
class DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod(builtins.str, Enum):
    """
    The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.
    """
    NO_ROTATION = "NoRotation"
    ONE_HOUR = "OneHour"
    ONE_DAY = "OneDay"
    ONE_WEEK = "OneWeek"
    ONE_MONTH = "OneMonth"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode")
class DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    Defines how documents should be delivered to Amazon S3.
    """
    FAILED_DOCUMENTS_ONLY = "FailedDocumentsOnly"
    ALL_DOCUMENTS = "AllDocuments"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamAuthenticationConfigurationConnectivity")
class DeliveryStreamAuthenticationConfigurationConnectivity(builtins.str, Enum):
    """
    The type of connectivity used to access the Amazon MSK cluster.
    """
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamDatabaseSourceConfigurationSslMode")
class DeliveryStreamDatabaseSourceConfigurationSslMode(builtins.str, Enum):
    """
    The mode to enable or disable SSL when Firehose connects to the database endpoint.

    Amazon Data Firehose is in preview release and is subject to change.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamDatabaseSourceConfigurationType")
class DeliveryStreamDatabaseSourceConfigurationType(builtins.str, Enum):
    """
    The type of database engine. This can be one of the following values.

    - MySQL
    - PostgreSQL

    Amazon Data Firehose is in preview release and is subject to change.
    """
    MY_SQL = "MySQL"
    POSTGRE_SQL = "PostgreSQL"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat")
class DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat(builtins.str, Enum):
    """
    When the `FIREHOSE_DEFAULT` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.

    When the `NO_DOCUMENT_ID` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.
    """
    FIREHOSE_DEFAULT = "FIREHOSE_DEFAULT"
    NO_DOCUMENT_ID = "NO_DOCUMENT_ID"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod")
class DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod(builtins.str, Enum):
    """
    The frequency of Elasticsearch index rotation. If you enable index rotation, Kinesis Data Firehose appends a portion of the UTC arrival timestamp to the specified index name, and rotates the appended timestamp accordingly. For more information, see [Index Rotation for the Amazon ES Destination](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation) in the *Amazon Kinesis Data Firehose Developer Guide* .
    """
    NO_ROTATION = "NoRotation"
    ONE_HOUR = "OneHour"
    ONE_DAY = "OneDay"
    ONE_WEEK = "OneWeek"
    ONE_MONTH = "OneMonth"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode")
class DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    The condition under which Kinesis Data Firehose delivers data to Amazon Simple Storage Service (Amazon S3). You can send Amazon S3 all documents (all data) or only the documents that Kinesis Data Firehose could not deliver to the Amazon ES destination. For more information and valid values, see the `S3BackupMode` content for the [ElasticsearchDestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html) data type in the *Amazon Kinesis Data Firehose API Reference* .
    """
    FAILED_DOCUMENTS_ONLY = "FailedDocumentsOnly"
    ALL_DOCUMENTS = "AllDocuments"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamEncryptionConfigurationInputKeyType")
class DeliveryStreamEncryptionConfigurationInputKeyType(builtins.str, Enum):
    """
    Indicates the type of customer master key (CMK) to use for encryption. The default setting is `AWS_OWNED_CMK` . For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) .

    You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams.

    > To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see [About Symmetric and Asymmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html) in the AWS Key Management Service developer guide.
    """
    AWS_OWNED_CMK = "AWS_OWNED_CMK"
    CUSTOMER_MANAGED_CMK = "CUSTOMER_MANAGED_CMK"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamEncryptionConfigurationNoEncryptionConfig")
class DeliveryStreamEncryptionConfigurationNoEncryptionConfig(builtins.str, Enum):
    """
    Disables encryption. For valid values, see the `NoEncryptionConfig` content for the [EncryptionConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html) data type in the *Amazon Kinesis Data Firehose API Reference* .
    """
    NO_ENCRYPTION = "NoEncryption"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat")
class DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat(builtins.str, Enum):
    """
    The compression format. If no value is specified, the default is `UNCOMPRESSED` .
    """
    UNCOMPRESSED = "UNCOMPRESSED"
    GZIP = "GZIP"
    ZIP = "ZIP"
    SNAPPY = "Snappy"
    HADOOP_SNAPPY = "HADOOP_SNAPPY"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode")
class DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    The Amazon S3 backup mode. After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamHttpEndpointRequestConfigurationContentEncoding")
class DeliveryStreamHttpEndpointRequestConfigurationContentEncoding(builtins.str, Enum):
    """
    Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see Content-Encoding in MDN Web Docs, the official Mozilla documentation.
    """
    NONE = "NONE"
    GZIP = "GZIP"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamIcebergDestinationConfigurations3BackupMode")
class DeliveryStreamIcebergDestinationConfigurations3BackupMode(builtins.str, Enum):
    """
    Describes how Firehose will backup records. Currently,S3 backup only supports `FailedDataOnly` .
    """
    ALL_DATA = "AllData"
    FAILED_DATA_ONLY = "FailedDataOnly"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamProcessorType")
class DeliveryStreamProcessorType(builtins.str, Enum):
    """
    The type of processor. Valid values: `Lambda` .
    """
    RECORD_DE_AGGREGATION = "RecordDeAggregation"
    DECOMPRESSION = "Decompression"
    CLOUD_WATCH_LOG_PROCESSING = "CloudWatchLogProcessing"
    LAMBDA_ = "Lambda"
    METADATA_EXTRACTION = "MetadataExtraction"
    APPEND_DELIMITER_TO_RECORD = "AppendDelimiterToRecord"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamRedshiftDestinationConfigurationS3BackupMode")
class DeliveryStreamRedshiftDestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    The Amazon S3 backup mode. After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamS3DestinationConfigurationCompressionFormat")
class DeliveryStreamS3DestinationConfigurationCompressionFormat(builtins.str, Enum):
    """
    The type of compression that Kinesis Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. For valid values, see the `CompressionFormat` content for the [S3DestinationConfiguration](https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html) data type in the *Amazon Kinesis Data Firehose API Reference* .
    """
    UNCOMPRESSED = "UNCOMPRESSED"
    GZIP = "GZIP"
    ZIP = "ZIP"
    SNAPPY = "Snappy"
    HADOOP_SNAPPY = "HADOOP_SNAPPY"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamSnowflakeDestinationConfigurationDataLoadingOption")
class DeliveryStreamSnowflakeDestinationConfigurationDataLoadingOption(builtins.str, Enum):
    """
    Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
    """
    JSON_MAPPING = "JSON_MAPPING"
    VARIANT_CONTENT_MAPPING = "VARIANT_CONTENT_MAPPING"
    VARIANT_CONTENT_AND_METADATA_MAPPING = "VARIANT_CONTENT_AND_METADATA_MAPPING"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamSnowflakeDestinationConfigurationS3BackupMode")
class DeliveryStreamSnowflakeDestinationConfigurationS3BackupMode(builtins.str, Enum):
    """
    Choose an S3 backup mode
    """
    FAILED_DATA_ONLY = "FailedDataOnly"
    ALL_DATA = "AllData"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamSplunkDestinationConfigurationHecEndpointType")
class DeliveryStreamSplunkDestinationConfigurationHecEndpointType(builtins.str, Enum):
    """
    This type can be either `Raw` or `Event` .
    """
    RAW = "Raw"
    EVENT = "Event"


@pulumi.type_token("aws-native:kinesisfirehose:DeliveryStreamType")
class DeliveryStreamType(builtins.str, Enum):
    """
    The Firehose stream type. This can be one of the following values:

    - `DirectPut` : Provider applications access the Firehose stream directly.
    - `KinesisStreamAsSource` : The Firehose stream uses a Kinesis data stream as a source.
    """
    DATABASE_AS_SOURCE = "DatabaseAsSource"
    DIRECT_PUT = "DirectPut"
    KINESIS_STREAM_AS_SOURCE = "KinesisStreamAsSource"
    MSKAS_SOURCE = "MSKAsSource"
