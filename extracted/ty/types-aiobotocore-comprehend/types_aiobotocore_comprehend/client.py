"""
Type annotations for comprehend service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_comprehend.client import ComprehendClient

    session = get_session()
    async with session.create_client("comprehend") as client:
        client: ComprehendClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEndpointsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
    ListPiiEntitiesDetectionJobsPaginator,
    ListSentimentDetectionJobsPaginator,
    ListTopicsDetectionJobsPaginator,
)
from .type_defs import (
    BatchDetectDominantLanguageRequestTypeDef,
    BatchDetectDominantLanguageResponseTypeDef,
    BatchDetectEntitiesRequestTypeDef,
    BatchDetectEntitiesResponseTypeDef,
    BatchDetectKeyPhrasesRequestTypeDef,
    BatchDetectKeyPhrasesResponseTypeDef,
    BatchDetectSentimentRequestTypeDef,
    BatchDetectSentimentResponseTypeDef,
    BatchDetectSyntaxRequestTypeDef,
    BatchDetectSyntaxResponseTypeDef,
    BatchDetectTargetedSentimentRequestTypeDef,
    BatchDetectTargetedSentimentResponseTypeDef,
    ClassifyDocumentRequestTypeDef,
    ClassifyDocumentResponseTypeDef,
    ContainsPiiEntitiesRequestTypeDef,
    ContainsPiiEntitiesResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDocumentClassifierRequestTypeDef,
    CreateDocumentClassifierResponseTypeDef,
    CreateEndpointRequestTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEntityRecognizerRequestTypeDef,
    CreateEntityRecognizerResponseTypeDef,
    CreateFlywheelRequestTypeDef,
    CreateFlywheelResponseTypeDef,
    DeleteDocumentClassifierRequestTypeDef,
    DeleteEndpointRequestTypeDef,
    DeleteEntityRecognizerRequestTypeDef,
    DeleteFlywheelRequestTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDocumentClassificationJobRequestTypeDef,
    DescribeDocumentClassificationJobResponseTypeDef,
    DescribeDocumentClassifierRequestTypeDef,
    DescribeDocumentClassifierResponseTypeDef,
    DescribeDominantLanguageDetectionJobRequestTypeDef,
    DescribeDominantLanguageDetectionJobResponseTypeDef,
    DescribeEndpointRequestTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEntitiesDetectionJobRequestTypeDef,
    DescribeEntitiesDetectionJobResponseTypeDef,
    DescribeEntityRecognizerRequestTypeDef,
    DescribeEntityRecognizerResponseTypeDef,
    DescribeEventsDetectionJobRequestTypeDef,
    DescribeEventsDetectionJobResponseTypeDef,
    DescribeFlywheelIterationRequestTypeDef,
    DescribeFlywheelIterationResponseTypeDef,
    DescribeFlywheelRequestTypeDef,
    DescribeFlywheelResponseTypeDef,
    DescribeKeyPhrasesDetectionJobRequestTypeDef,
    DescribeKeyPhrasesDetectionJobResponseTypeDef,
    DescribePiiEntitiesDetectionJobRequestTypeDef,
    DescribePiiEntitiesDetectionJobResponseTypeDef,
    DescribeResourcePolicyRequestTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeSentimentDetectionJobRequestTypeDef,
    DescribeSentimentDetectionJobResponseTypeDef,
    DescribeTargetedSentimentDetectionJobRequestTypeDef,
    DescribeTargetedSentimentDetectionJobResponseTypeDef,
    DescribeTopicsDetectionJobRequestTypeDef,
    DescribeTopicsDetectionJobResponseTypeDef,
    DetectDominantLanguageRequestTypeDef,
    DetectDominantLanguageResponseTypeDef,
    DetectEntitiesRequestTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectKeyPhrasesRequestTypeDef,
    DetectKeyPhrasesResponseTypeDef,
    DetectPiiEntitiesRequestTypeDef,
    DetectPiiEntitiesResponseTypeDef,
    DetectSentimentRequestTypeDef,
    DetectSentimentResponseTypeDef,
    DetectSyntaxRequestTypeDef,
    DetectSyntaxResponseTypeDef,
    DetectTargetedSentimentRequestTypeDef,
    DetectTargetedSentimentResponseTypeDef,
    DetectToxicContentRequestTypeDef,
    DetectToxicContentResponseTypeDef,
    ImportModelRequestTypeDef,
    ImportModelResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListDocumentClassificationJobsRequestTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersRequestTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDocumentClassifierSummariesRequestTypeDef,
    ListDocumentClassifierSummariesResponseTypeDef,
    ListDominantLanguageDetectionJobsRequestTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsRequestTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsRequestTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersRequestTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListEntityRecognizerSummariesRequestTypeDef,
    ListEntityRecognizerSummariesResponseTypeDef,
    ListEventsDetectionJobsRequestTypeDef,
    ListEventsDetectionJobsResponseTypeDef,
    ListFlywheelIterationHistoryRequestTypeDef,
    ListFlywheelIterationHistoryResponseTypeDef,
    ListFlywheelsRequestTypeDef,
    ListFlywheelsResponseTypeDef,
    ListKeyPhrasesDetectionJobsRequestTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListPiiEntitiesDetectionJobsRequestTypeDef,
    ListPiiEntitiesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsRequestTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetedSentimentDetectionJobsRequestTypeDef,
    ListTargetedSentimentDetectionJobsResponseTypeDef,
    ListTopicsDetectionJobsRequestTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartDocumentClassificationJobRequestTypeDef,
    StartDocumentClassificationJobResponseTypeDef,
    StartDominantLanguageDetectionJobRequestTypeDef,
    StartDominantLanguageDetectionJobResponseTypeDef,
    StartEntitiesDetectionJobRequestTypeDef,
    StartEntitiesDetectionJobResponseTypeDef,
    StartEventsDetectionJobRequestTypeDef,
    StartEventsDetectionJobResponseTypeDef,
    StartFlywheelIterationRequestTypeDef,
    StartFlywheelIterationResponseTypeDef,
    StartKeyPhrasesDetectionJobRequestTypeDef,
    StartKeyPhrasesDetectionJobResponseTypeDef,
    StartPiiEntitiesDetectionJobRequestTypeDef,
    StartPiiEntitiesDetectionJobResponseTypeDef,
    StartSentimentDetectionJobRequestTypeDef,
    StartSentimentDetectionJobResponseTypeDef,
    StartTargetedSentimentDetectionJobRequestTypeDef,
    StartTargetedSentimentDetectionJobResponseTypeDef,
    StartTopicsDetectionJobRequestTypeDef,
    StartTopicsDetectionJobResponseTypeDef,
    StopDominantLanguageDetectionJobRequestTypeDef,
    StopDominantLanguageDetectionJobResponseTypeDef,
    StopEntitiesDetectionJobRequestTypeDef,
    StopEntitiesDetectionJobResponseTypeDef,
    StopEventsDetectionJobRequestTypeDef,
    StopEventsDetectionJobResponseTypeDef,
    StopKeyPhrasesDetectionJobRequestTypeDef,
    StopKeyPhrasesDetectionJobResponseTypeDef,
    StopPiiEntitiesDetectionJobRequestTypeDef,
    StopPiiEntitiesDetectionJobResponseTypeDef,
    StopSentimentDetectionJobRequestTypeDef,
    StopSentimentDetectionJobResponseTypeDef,
    StopTargetedSentimentDetectionJobRequestTypeDef,
    StopTargetedSentimentDetectionJobResponseTypeDef,
    StopTrainingDocumentClassifierRequestTypeDef,
    StopTrainingEntityRecognizerRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateEndpointRequestTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateFlywheelRequestTypeDef,
    UpdateFlywheelResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("ComprehendClient",)


class Exceptions(BaseClientExceptions):
    BatchSizeLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobNotFoundException: Type[BotocoreClientError]
    KmsKeyValidationException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedLanguageException: Type[BotocoreClientError]


class ComprehendClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComprehendClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#generate_presigned_url)
        """

    async def batch_detect_dominant_language(
        self, **kwargs: Unpack[BatchDetectDominantLanguageRequestTypeDef]
    ) -> BatchDetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text for a batch of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_dominant_language.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_dominant_language)
        """

    async def batch_detect_entities(
        self, **kwargs: Unpack[BatchDetectEntitiesRequestTypeDef]
    ) -> BatchDetectEntitiesResponseTypeDef:
        """
        Inspects the text of a batch of documents for named entities and returns
        information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_entities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_entities)
        """

    async def batch_detect_key_phrases(
        self, **kwargs: Unpack[BatchDetectKeyPhrasesRequestTypeDef]
    ) -> BatchDetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in a batch of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_key_phrases.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_key_phrases)
        """

    async def batch_detect_sentiment(
        self, **kwargs: Unpack[BatchDetectSentimentRequestTypeDef]
    ) -> BatchDetectSentimentResponseTypeDef:
        """
        Inspects a batch of documents and returns an inference of the prevailing
        sentiment, <code>POSITIVE</code>, <code>NEUTRAL</code>, <code>MIXED</code>, or
        <code>NEGATIVE</code>, in each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_sentiment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_sentiment)
        """

    async def batch_detect_syntax(
        self, **kwargs: Unpack[BatchDetectSyntaxRequestTypeDef]
    ) -> BatchDetectSyntaxResponseTypeDef:
        """
        Inspects the text of a batch of documents for the syntax and part of speech of
        the words in the document and returns information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_syntax.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_syntax)
        """

    async def batch_detect_targeted_sentiment(
        self, **kwargs: Unpack[BatchDetectTargetedSentimentRequestTypeDef]
    ) -> BatchDetectTargetedSentimentResponseTypeDef:
        """
        Inspects a batch of documents and returns a sentiment analysis for each entity
        identified in the documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/batch_detect_targeted_sentiment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#batch_detect_targeted_sentiment)
        """

    async def classify_document(
        self, **kwargs: Unpack[ClassifyDocumentRequestTypeDef]
    ) -> ClassifyDocumentResponseTypeDef:
        """
        Creates a classification request to analyze a single document in real-time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/classify_document.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#classify_document)
        """

    async def contains_pii_entities(
        self, **kwargs: Unpack[ContainsPiiEntitiesRequestTypeDef]
    ) -> ContainsPiiEntitiesResponseTypeDef:
        """
        Analyzes input text for the presence of personally identifiable information
        (PII) and returns the labels of identified PII entity types such as name,
        address, bank account number, or phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/contains_pii_entities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#contains_pii_entities)
        """

    async def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a dataset to upload training or test data for a model associated with a
        flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/create_dataset.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#create_dataset)
        """

    async def create_document_classifier(
        self, **kwargs: Unpack[CreateDocumentClassifierRequestTypeDef]
    ) -> CreateDocumentClassifierResponseTypeDef:
        """
        Creates a new document classifier that you can use to categorize documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/create_document_classifier.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#create_document_classifier)
        """

    async def create_endpoint(
        self, **kwargs: Unpack[CreateEndpointRequestTypeDef]
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates a model-specific endpoint for synchronous inference for a previously
        trained custom model For information about endpoints, see <a
        href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing
        endpoints</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/create_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#create_endpoint)
        """

    async def create_entity_recognizer(
        self, **kwargs: Unpack[CreateEntityRecognizerRequestTypeDef]
    ) -> CreateEntityRecognizerResponseTypeDef:
        """
        Creates an entity recognizer using submitted files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/create_entity_recognizer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#create_entity_recognizer)
        """

    async def create_flywheel(
        self, **kwargs: Unpack[CreateFlywheelRequestTypeDef]
    ) -> CreateFlywheelResponseTypeDef:
        """
        A flywheel is an Amazon Web Services resource that orchestrates the ongoing
        training of a model for custom classification or custom entity recognition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/create_flywheel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#create_flywheel)
        """

    async def delete_document_classifier(
        self, **kwargs: Unpack[DeleteDocumentClassifierRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a previously created document classifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/delete_document_classifier.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#delete_document_classifier)
        """

    async def delete_endpoint(
        self, **kwargs: Unpack[DeleteEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a model-specific endpoint for a previously-trained custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/delete_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#delete_endpoint)
        """

    async def delete_entity_recognizer(
        self, **kwargs: Unpack[DeleteEntityRecognizerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an entity recognizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/delete_entity_recognizer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#delete_entity_recognizer)
        """

    async def delete_flywheel(
        self, **kwargs: Unpack[DeleteFlywheelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/delete_flywheel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#delete_flywheel)
        """

    async def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource-based policy that is attached to a custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/delete_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#delete_resource_policy)
        """

    async def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Returns information about the dataset that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_dataset.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_dataset)
        """

    async def describe_document_classification_job(
        self, **kwargs: Unpack[DescribeDocumentClassificationJobRequestTypeDef]
    ) -> DescribeDocumentClassificationJobResponseTypeDef:
        """
        Gets the properties associated with a document classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_document_classification_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_document_classification_job)
        """

    async def describe_document_classifier(
        self, **kwargs: Unpack[DescribeDocumentClassifierRequestTypeDef]
    ) -> DescribeDocumentClassifierResponseTypeDef:
        """
        Gets the properties associated with a document classifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_document_classifier.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_document_classifier)
        """

    async def describe_dominant_language_detection_job(
        self, **kwargs: Unpack[DescribeDominantLanguageDetectionJobRequestTypeDef]
    ) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a dominant language detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_dominant_language_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_dominant_language_detection_job)
        """

    async def describe_endpoint(
        self, **kwargs: Unpack[DescribeEndpointRequestTypeDef]
    ) -> DescribeEndpointResponseTypeDef:
        """
        Gets the properties associated with a specific endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_endpoint)
        """

    async def describe_entities_detection_job(
        self, **kwargs: Unpack[DescribeEntitiesDetectionJobRequestTypeDef]
    ) -> DescribeEntitiesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with an entities detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_entities_detection_job)
        """

    async def describe_entity_recognizer(
        self, **kwargs: Unpack[DescribeEntityRecognizerRequestTypeDef]
    ) -> DescribeEntityRecognizerResponseTypeDef:
        """
        Provides details about an entity recognizer including status, S3 buckets
        containing training data, recognizer metadata, metrics, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_entity_recognizer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_entity_recognizer)
        """

    async def describe_events_detection_job(
        self, **kwargs: Unpack[DescribeEventsDetectionJobRequestTypeDef]
    ) -> DescribeEventsDetectionJobResponseTypeDef:
        """
        Gets the status and details of an events detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_events_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_events_detection_job)
        """

    async def describe_flywheel(
        self, **kwargs: Unpack[DescribeFlywheelRequestTypeDef]
    ) -> DescribeFlywheelResponseTypeDef:
        """
        Provides configuration information about the flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_flywheel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_flywheel)
        """

    async def describe_flywheel_iteration(
        self, **kwargs: Unpack[DescribeFlywheelIterationRequestTypeDef]
    ) -> DescribeFlywheelIterationResponseTypeDef:
        """
        Retrieve the configuration properties of a flywheel iteration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_flywheel_iteration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_flywheel_iteration)
        """

    async def describe_key_phrases_detection_job(
        self, **kwargs: Unpack[DescribeKeyPhrasesDetectionJobRequestTypeDef]
    ) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a key phrases detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_key_phrases_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_key_phrases_detection_job)
        """

    async def describe_pii_entities_detection_job(
        self, **kwargs: Unpack[DescribePiiEntitiesDetectionJobRequestTypeDef]
    ) -> DescribePiiEntitiesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a PII entities detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_pii_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_pii_entities_detection_job)
        """

    async def describe_resource_policy(
        self, **kwargs: Unpack[DescribeResourcePolicyRequestTypeDef]
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Gets the details of a resource-based policy that is attached to a custom model,
        including the JSON body of the policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_resource_policy)
        """

    async def describe_sentiment_detection_job(
        self, **kwargs: Unpack[DescribeSentimentDetectionJobRequestTypeDef]
    ) -> DescribeSentimentDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a sentiment detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_sentiment_detection_job)
        """

    async def describe_targeted_sentiment_detection_job(
        self, **kwargs: Unpack[DescribeTargetedSentimentDetectionJobRequestTypeDef]
    ) -> DescribeTargetedSentimentDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a targeted sentiment detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_targeted_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_targeted_sentiment_detection_job)
        """

    async def describe_topics_detection_job(
        self, **kwargs: Unpack[DescribeTopicsDetectionJobRequestTypeDef]
    ) -> DescribeTopicsDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a topic detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/describe_topics_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#describe_topics_detection_job)
        """

    async def detect_dominant_language(
        self, **kwargs: Unpack[DetectDominantLanguageRequestTypeDef]
    ) -> DetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_dominant_language.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_dominant_language)
        """

    async def detect_entities(
        self, **kwargs: Unpack[DetectEntitiesRequestTypeDef]
    ) -> DetectEntitiesResponseTypeDef:
        """
        Detects named entities in input text when you use the pre-trained model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_entities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_entities)
        """

    async def detect_key_phrases(
        self, **kwargs: Unpack[DetectKeyPhrasesRequestTypeDef]
    ) -> DetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in the text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_key_phrases.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_key_phrases)
        """

    async def detect_pii_entities(
        self, **kwargs: Unpack[DetectPiiEntitiesRequestTypeDef]
    ) -> DetectPiiEntitiesResponseTypeDef:
        """
        Inspects the input text for entities that contain personally identifiable
        information (PII) and returns information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_pii_entities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_pii_entities)
        """

    async def detect_sentiment(
        self, **kwargs: Unpack[DetectSentimentRequestTypeDef]
    ) -> DetectSentimentResponseTypeDef:
        """
        Inspects text and returns an inference of the prevailing sentiment
        (<code>POSITIVE</code>, <code>NEUTRAL</code>, <code>MIXED</code>, or
        <code>NEGATIVE</code>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_sentiment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_sentiment)
        """

    async def detect_syntax(
        self, **kwargs: Unpack[DetectSyntaxRequestTypeDef]
    ) -> DetectSyntaxResponseTypeDef:
        """
        Inspects text for syntax and the part of speech of words in the document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_syntax.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_syntax)
        """

    async def detect_targeted_sentiment(
        self, **kwargs: Unpack[DetectTargetedSentimentRequestTypeDef]
    ) -> DetectTargetedSentimentResponseTypeDef:
        """
        Inspects the input text and returns a sentiment analysis for each entity
        identified in the text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_targeted_sentiment.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_targeted_sentiment)
        """

    async def detect_toxic_content(
        self, **kwargs: Unpack[DetectToxicContentRequestTypeDef]
    ) -> DetectToxicContentResponseTypeDef:
        """
        Performs toxicity analysis on the list of text strings that you provide as
        input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/detect_toxic_content.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#detect_toxic_content)
        """

    async def import_model(
        self, **kwargs: Unpack[ImportModelRequestTypeDef]
    ) -> ImportModelResponseTypeDef:
        """
        Creates a new custom model that replicates a source custom model that you
        import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/import_model.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#import_model)
        """

    async def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        List the datasets that you have configured in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_datasets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_datasets)
        """

    async def list_document_classification_jobs(
        self, **kwargs: Unpack[ListDocumentClassificationJobsRequestTypeDef]
    ) -> ListDocumentClassificationJobsResponseTypeDef:
        """
        Gets a list of the documentation classification jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_document_classification_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_document_classification_jobs)
        """

    async def list_document_classifier_summaries(
        self, **kwargs: Unpack[ListDocumentClassifierSummariesRequestTypeDef]
    ) -> ListDocumentClassifierSummariesResponseTypeDef:
        """
        Gets a list of summaries of the document classifiers that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_document_classifier_summaries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_document_classifier_summaries)
        """

    async def list_document_classifiers(
        self, **kwargs: Unpack[ListDocumentClassifiersRequestTypeDef]
    ) -> ListDocumentClassifiersResponseTypeDef:
        """
        Gets a list of the document classifiers that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_document_classifiers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_document_classifiers)
        """

    async def list_dominant_language_detection_jobs(
        self, **kwargs: Unpack[ListDominantLanguageDetectionJobsRequestTypeDef]
    ) -> ListDominantLanguageDetectionJobsResponseTypeDef:
        """
        Gets a list of the dominant language detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_dominant_language_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_dominant_language_detection_jobs)
        """

    async def list_endpoints(
        self, **kwargs: Unpack[ListEndpointsRequestTypeDef]
    ) -> ListEndpointsResponseTypeDef:
        """
        Gets a list of all existing endpoints that you've created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_endpoints.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_endpoints)
        """

    async def list_entities_detection_jobs(
        self, **kwargs: Unpack[ListEntitiesDetectionJobsRequestTypeDef]
    ) -> ListEntitiesDetectionJobsResponseTypeDef:
        """
        Gets a list of the entity detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_entities_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_entities_detection_jobs)
        """

    async def list_entity_recognizer_summaries(
        self, **kwargs: Unpack[ListEntityRecognizerSummariesRequestTypeDef]
    ) -> ListEntityRecognizerSummariesResponseTypeDef:
        """
        Gets a list of summaries for the entity recognizers that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_entity_recognizer_summaries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_entity_recognizer_summaries)
        """

    async def list_entity_recognizers(
        self, **kwargs: Unpack[ListEntityRecognizersRequestTypeDef]
    ) -> ListEntityRecognizersResponseTypeDef:
        """
        Gets a list of the properties of all entity recognizers that you created,
        including recognizers currently in training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_entity_recognizers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_entity_recognizers)
        """

    async def list_events_detection_jobs(
        self, **kwargs: Unpack[ListEventsDetectionJobsRequestTypeDef]
    ) -> ListEventsDetectionJobsResponseTypeDef:
        """
        Gets a list of the events detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_events_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_events_detection_jobs)
        """

    async def list_flywheel_iteration_history(
        self, **kwargs: Unpack[ListFlywheelIterationHistoryRequestTypeDef]
    ) -> ListFlywheelIterationHistoryResponseTypeDef:
        """
        Information about the history of a flywheel iteration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_flywheel_iteration_history.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_flywheel_iteration_history)
        """

    async def list_flywheels(
        self, **kwargs: Unpack[ListFlywheelsRequestTypeDef]
    ) -> ListFlywheelsResponseTypeDef:
        """
        Gets a list of the flywheels that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_flywheels.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_flywheels)
        """

    async def list_key_phrases_detection_jobs(
        self, **kwargs: Unpack[ListKeyPhrasesDetectionJobsRequestTypeDef]
    ) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        Get a list of key phrase detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_key_phrases_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_key_phrases_detection_jobs)
        """

    async def list_pii_entities_detection_jobs(
        self, **kwargs: Unpack[ListPiiEntitiesDetectionJobsRequestTypeDef]
    ) -> ListPiiEntitiesDetectionJobsResponseTypeDef:
        """
        Gets a list of the PII entity detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_pii_entities_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_pii_entities_detection_jobs)
        """

    async def list_sentiment_detection_jobs(
        self, **kwargs: Unpack[ListSentimentDetectionJobsRequestTypeDef]
    ) -> ListSentimentDetectionJobsResponseTypeDef:
        """
        Gets a list of sentiment detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_sentiment_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_sentiment_detection_jobs)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_tags_for_resource)
        """

    async def list_targeted_sentiment_detection_jobs(
        self, **kwargs: Unpack[ListTargetedSentimentDetectionJobsRequestTypeDef]
    ) -> ListTargetedSentimentDetectionJobsResponseTypeDef:
        """
        Gets a list of targeted sentiment detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_targeted_sentiment_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_targeted_sentiment_detection_jobs)
        """

    async def list_topics_detection_jobs(
        self, **kwargs: Unpack[ListTopicsDetectionJobsRequestTypeDef]
    ) -> ListTopicsDetectionJobsResponseTypeDef:
        """
        Gets a list of the topic detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/list_topics_detection_jobs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#list_topics_detection_jobs)
        """

    async def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Attaches a resource-based policy to a custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/put_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#put_resource_policy)
        """

    async def start_document_classification_job(
        self, **kwargs: Unpack[StartDocumentClassificationJobRequestTypeDef]
    ) -> StartDocumentClassificationJobResponseTypeDef:
        """
        Starts an asynchronous document classification job using a custom
        classification model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_document_classification_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_document_classification_job)
        """

    async def start_dominant_language_detection_job(
        self, **kwargs: Unpack[StartDominantLanguageDetectionJobRequestTypeDef]
    ) -> StartDominantLanguageDetectionJobResponseTypeDef:
        """
        Starts an asynchronous dominant language detection job for a collection of
        documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_dominant_language_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_dominant_language_detection_job)
        """

    async def start_entities_detection_job(
        self, **kwargs: Unpack[StartEntitiesDetectionJobRequestTypeDef]
    ) -> StartEntitiesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous entity detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_entities_detection_job)
        """

    async def start_events_detection_job(
        self, **kwargs: Unpack[StartEventsDetectionJobRequestTypeDef]
    ) -> StartEventsDetectionJobResponseTypeDef:
        """
        Starts an asynchronous event detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_events_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_events_detection_job)
        """

    async def start_flywheel_iteration(
        self, **kwargs: Unpack[StartFlywheelIterationRequestTypeDef]
    ) -> StartFlywheelIterationResponseTypeDef:
        """
        Start the flywheel iteration.This operation uses any new datasets to train a
        new model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_flywheel_iteration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_flywheel_iteration)
        """

    async def start_key_phrases_detection_job(
        self, **kwargs: Unpack[StartKeyPhrasesDetectionJobRequestTypeDef]
    ) -> StartKeyPhrasesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous key phrase detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_key_phrases_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_key_phrases_detection_job)
        """

    async def start_pii_entities_detection_job(
        self, **kwargs: Unpack[StartPiiEntitiesDetectionJobRequestTypeDef]
    ) -> StartPiiEntitiesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous PII entity detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_pii_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_pii_entities_detection_job)
        """

    async def start_sentiment_detection_job(
        self, **kwargs: Unpack[StartSentimentDetectionJobRequestTypeDef]
    ) -> StartSentimentDetectionJobResponseTypeDef:
        """
        Starts an asynchronous sentiment detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_sentiment_detection_job)
        """

    async def start_targeted_sentiment_detection_job(
        self, **kwargs: Unpack[StartTargetedSentimentDetectionJobRequestTypeDef]
    ) -> StartTargetedSentimentDetectionJobResponseTypeDef:
        """
        Starts an asynchronous targeted sentiment detection job for a collection of
        documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_targeted_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_targeted_sentiment_detection_job)
        """

    async def start_topics_detection_job(
        self, **kwargs: Unpack[StartTopicsDetectionJobRequestTypeDef]
    ) -> StartTopicsDetectionJobResponseTypeDef:
        """
        Starts an asynchronous topic detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/start_topics_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#start_topics_detection_job)
        """

    async def stop_dominant_language_detection_job(
        self, **kwargs: Unpack[StopDominantLanguageDetectionJobRequestTypeDef]
    ) -> StopDominantLanguageDetectionJobResponseTypeDef:
        """
        Stops a dominant language detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_dominant_language_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_dominant_language_detection_job)
        """

    async def stop_entities_detection_job(
        self, **kwargs: Unpack[StopEntitiesDetectionJobRequestTypeDef]
    ) -> StopEntitiesDetectionJobResponseTypeDef:
        """
        Stops an entities detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_entities_detection_job)
        """

    async def stop_events_detection_job(
        self, **kwargs: Unpack[StopEventsDetectionJobRequestTypeDef]
    ) -> StopEventsDetectionJobResponseTypeDef:
        """
        Stops an events detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_events_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_events_detection_job)
        """

    async def stop_key_phrases_detection_job(
        self, **kwargs: Unpack[StopKeyPhrasesDetectionJobRequestTypeDef]
    ) -> StopKeyPhrasesDetectionJobResponseTypeDef:
        """
        Stops a key phrases detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_key_phrases_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_key_phrases_detection_job)
        """

    async def stop_pii_entities_detection_job(
        self, **kwargs: Unpack[StopPiiEntitiesDetectionJobRequestTypeDef]
    ) -> StopPiiEntitiesDetectionJobResponseTypeDef:
        """
        Stops a PII entities detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_pii_entities_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_pii_entities_detection_job)
        """

    async def stop_sentiment_detection_job(
        self, **kwargs: Unpack[StopSentimentDetectionJobRequestTypeDef]
    ) -> StopSentimentDetectionJobResponseTypeDef:
        """
        Stops a sentiment detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_sentiment_detection_job)
        """

    async def stop_targeted_sentiment_detection_job(
        self, **kwargs: Unpack[StopTargetedSentimentDetectionJobRequestTypeDef]
    ) -> StopTargetedSentimentDetectionJobResponseTypeDef:
        """
        Stops a targeted sentiment detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_targeted_sentiment_detection_job.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_targeted_sentiment_detection_job)
        """

    async def stop_training_document_classifier(
        self, **kwargs: Unpack[StopTrainingDocumentClassifierRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a document classifier training job while in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_training_document_classifier.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_training_document_classifier)
        """

    async def stop_training_entity_recognizer(
        self, **kwargs: Unpack[StopTrainingEntityRecognizerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an entity recognizer training job while in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/stop_training_entity_recognizer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#stop_training_entity_recognizer)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates a specific tag with an Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a specific tag associated with an Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#untag_resource)
        """

    async def update_endpoint(
        self, **kwargs: Unpack[UpdateEndpointRequestTypeDef]
    ) -> UpdateEndpointResponseTypeDef:
        """
        Updates information about the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/update_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#update_endpoint)
        """

    async def update_flywheel(
        self, **kwargs: Unpack[UpdateFlywheelRequestTypeDef]
    ) -> UpdateFlywheelResponseTypeDef:
        """
        Update the configuration information for an existing flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/update_flywheel.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#update_flywheel)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> ListDocumentClassificationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_document_classifiers"]
    ) -> ListDocumentClassifiersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> ListDominantLanguageDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_endpoints"]
    ) -> ListEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> ListEntitiesDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> ListEntityRecognizersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> ListKeyPhrasesDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pii_entities_detection_jobs"]
    ) -> ListPiiEntitiesDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> ListSentimentDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> ListTopicsDetectionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/client/)
        """
