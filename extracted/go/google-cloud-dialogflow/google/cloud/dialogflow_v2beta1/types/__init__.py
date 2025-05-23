# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from .agent import (
    Agent,
    DeleteAgentRequest,
    ExportAgentRequest,
    ExportAgentResponse,
    GetAgentRequest,
    GetValidationResultRequest,
    ImportAgentRequest,
    RestoreAgentRequest,
    SearchAgentsRequest,
    SearchAgentsResponse,
    SetAgentRequest,
    SubAgent,
    TrainAgentRequest,
)
from .answer_record import (
    AgentAssistantFeedback,
    AgentAssistantRecord,
    AnswerFeedback,
    AnswerRecord,
    GetAnswerRecordRequest,
    ListAnswerRecordsRequest,
    ListAnswerRecordsResponse,
    UpdateAnswerRecordRequest,
)
from .audio_config import (
    AudioEncoding,
    BargeInConfig,
    InputAudioConfig,
    OutputAudioConfig,
    OutputAudioEncoding,
    SpeechContext,
    SpeechModelVariant,
    SpeechToTextConfig,
    SpeechWordInfo,
    SsmlVoiceGender,
    SynthesizeSpeechConfig,
    TelephonyDtmf,
    TelephonyDtmfEvents,
    VoiceSelectionParams,
)
from .context import (
    Context,
    CreateContextRequest,
    DeleteAllContextsRequest,
    DeleteContextRequest,
    GetContextRequest,
    ListContextsRequest,
    ListContextsResponse,
    UpdateContextRequest,
)
from .conversation import (
    BatchCreateMessagesRequest,
    BatchCreateMessagesResponse,
    CompleteConversationRequest,
    Conversation,
    ConversationPhoneNumber,
    CreateConversationRequest,
    CreateMessageRequest,
    GenerateStatelessSuggestionRequest,
    GenerateStatelessSuggestionResponse,
    GenerateStatelessSummaryRequest,
    GenerateStatelessSummaryResponse,
    GenerateSuggestionsRequest,
    GetConversationRequest,
    IngestContextReferencesRequest,
    IngestContextReferencesResponse,
    ListConversationsRequest,
    ListConversationsResponse,
    ListMessagesRequest,
    ListMessagesResponse,
    SearchKnowledgeAnswer,
    SearchKnowledgeRequest,
    SearchKnowledgeResponse,
    SuggestConversationSummaryRequest,
    SuggestConversationSummaryResponse,
)
from .conversation_event import ConversationEvent
from .conversation_profile import (
    AutomatedAgentConfig,
    ClearSuggestionFeatureConfigOperationMetadata,
    ClearSuggestionFeatureConfigRequest,
    ConversationProfile,
    CreateConversationProfileRequest,
    DeleteConversationProfileRequest,
    GetConversationProfileRequest,
    HumanAgentAssistantConfig,
    HumanAgentHandoffConfig,
    ListConversationProfilesRequest,
    ListConversationProfilesResponse,
    LoggingConfig,
    NotificationConfig,
    SetSuggestionFeatureConfigOperationMetadata,
    SetSuggestionFeatureConfigRequest,
    UpdateConversationProfileRequest,
)
from .document import (
    CreateDocumentRequest,
    DeleteDocumentRequest,
    Document,
    ExportOperationMetadata,
    GetDocumentRequest,
    ImportDocumentsRequest,
    ImportDocumentsResponse,
    ImportDocumentTemplate,
    KnowledgeOperationMetadata,
    ListDocumentsRequest,
    ListDocumentsResponse,
    ReloadDocumentRequest,
    UpdateDocumentRequest,
)
from .encryption_spec import (
    EncryptionSpec,
    GetEncryptionSpecRequest,
    InitializeEncryptionSpecMetadata,
    InitializeEncryptionSpecRequest,
    InitializeEncryptionSpecResponse,
)
from .entity_type import (
    BatchCreateEntitiesRequest,
    BatchDeleteEntitiesRequest,
    BatchDeleteEntityTypesRequest,
    BatchUpdateEntitiesRequest,
    BatchUpdateEntityTypesRequest,
    BatchUpdateEntityTypesResponse,
    CreateEntityTypeRequest,
    DeleteEntityTypeRequest,
    EntityType,
    EntityTypeBatch,
    GetEntityTypeRequest,
    ListEntityTypesRequest,
    ListEntityTypesResponse,
    UpdateEntityTypeRequest,
)
from .environment import (
    CreateEnvironmentRequest,
    DeleteEnvironmentRequest,
    Environment,
    EnvironmentHistory,
    GetEnvironmentHistoryRequest,
    GetEnvironmentRequest,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    TextToSpeechSettings,
    UpdateEnvironmentRequest,
)
from .fulfillment import Fulfillment, GetFulfillmentRequest, UpdateFulfillmentRequest
from .gcs import GcsDestination, GcsSource, GcsSources
from .generator import (
    ConversationContext,
    CreateGeneratorRequest,
    DeleteGeneratorRequest,
    FewShotExample,
    FreeFormContext,
    FreeFormSuggestion,
    Generator,
    GeneratorSuggestion,
    GetGeneratorRequest,
    InferenceParameter,
    ListGeneratorsRequest,
    ListGeneratorsResponse,
    MessageEntry,
    SummarizationContext,
    SummarizationSection,
    SummarizationSectionList,
    SummarySuggestion,
    TriggerEvent,
    UpdateGeneratorRequest,
)
from .human_agent_assistant_event import HumanAgentAssistantEvent
from .intent import (
    BatchDeleteIntentsRequest,
    BatchUpdateIntentsRequest,
    BatchUpdateIntentsResponse,
    CreateIntentRequest,
    DeleteIntentRequest,
    GetIntentRequest,
    Intent,
    IntentBatch,
    IntentView,
    ListIntentsRequest,
    ListIntentsResponse,
    UpdateIntentRequest,
)
from .knowledge_base import (
    CreateKnowledgeBaseRequest,
    DeleteKnowledgeBaseRequest,
    GetKnowledgeBaseRequest,
    KnowledgeBase,
    ListKnowledgeBasesRequest,
    ListKnowledgeBasesResponse,
    UpdateKnowledgeBaseRequest,
)
from .participant import (
    AnalyzeContentRequest,
    AnalyzeContentResponse,
    AnnotatedMessagePart,
    ArticleAnswer,
    AssistQueryParameters,
    AudioInput,
    AutomatedAgentReply,
    CompileSuggestionRequest,
    CompileSuggestionResponse,
    CreateParticipantRequest,
    DialogflowAssistAnswer,
    DtmfParameters,
    FaqAnswer,
    GenerateSuggestionsResponse,
    GetParticipantRequest,
    InputTextConfig,
    IntentInput,
    IntentSuggestion,
    KnowledgeAssistAnswer,
    ListParticipantsRequest,
    ListParticipantsResponse,
    ListSuggestionsRequest,
    ListSuggestionsResponse,
    Message,
    MessageAnnotation,
    OutputAudio,
    Participant,
    ResponseMessage,
    SmartReplyAnswer,
    StreamingAnalyzeContentRequest,
    StreamingAnalyzeContentResponse,
    SuggestArticlesRequest,
    SuggestArticlesResponse,
    SuggestDialogflowAssistsResponse,
    SuggestFaqAnswersRequest,
    SuggestFaqAnswersResponse,
    Suggestion,
    SuggestionFeature,
    SuggestionInput,
    SuggestionResult,
    SuggestKnowledgeAssistRequest,
    SuggestKnowledgeAssistResponse,
    SuggestSmartRepliesRequest,
    SuggestSmartRepliesResponse,
    UpdateParticipantRequest,
)
from .phone_number import (
    DeletePhoneNumberRequest,
    ListPhoneNumbersRequest,
    ListPhoneNumbersResponse,
    PhoneNumber,
    UndeletePhoneNumberRequest,
    UpdatePhoneNumberRequest,
)
from .session import (
    CloudConversationDebuggingInfo,
    DetectIntentRequest,
    DetectIntentResponse,
    EventInput,
    KnowledgeAnswers,
    QueryInput,
    QueryParameters,
    QueryResult,
    Sentiment,
    SentimentAnalysisRequestConfig,
    SentimentAnalysisResult,
    StreamingDetectIntentRequest,
    StreamingDetectIntentResponse,
    StreamingRecognitionResult,
    TextInput,
)
from .session_entity_type import (
    CreateSessionEntityTypeRequest,
    DeleteSessionEntityTypeRequest,
    GetSessionEntityTypeRequest,
    ListSessionEntityTypesRequest,
    ListSessionEntityTypesResponse,
    SessionEntityType,
    UpdateSessionEntityTypeRequest,
)
from .sip_trunk import (
    Connection,
    CreateSipTrunkRequest,
    DeleteSipTrunkRequest,
    GetSipTrunkRequest,
    ListSipTrunksRequest,
    ListSipTrunksResponse,
    SipTrunk,
    UpdateSipTrunkRequest,
)
from .validation_result import ValidationError, ValidationResult
from .version import (
    CreateVersionRequest,
    DeleteVersionRequest,
    GetVersionRequest,
    ListVersionsRequest,
    ListVersionsResponse,
    UpdateVersionRequest,
    Version,
)
from .webhook import OriginalDetectIntentRequest, WebhookRequest, WebhookResponse

__all__ = (
    "Agent",
    "DeleteAgentRequest",
    "ExportAgentRequest",
    "ExportAgentResponse",
    "GetAgentRequest",
    "GetValidationResultRequest",
    "ImportAgentRequest",
    "RestoreAgentRequest",
    "SearchAgentsRequest",
    "SearchAgentsResponse",
    "SetAgentRequest",
    "SubAgent",
    "TrainAgentRequest",
    "AgentAssistantFeedback",
    "AgentAssistantRecord",
    "AnswerFeedback",
    "AnswerRecord",
    "GetAnswerRecordRequest",
    "ListAnswerRecordsRequest",
    "ListAnswerRecordsResponse",
    "UpdateAnswerRecordRequest",
    "BargeInConfig",
    "InputAudioConfig",
    "OutputAudioConfig",
    "SpeechContext",
    "SpeechToTextConfig",
    "SpeechWordInfo",
    "SynthesizeSpeechConfig",
    "TelephonyDtmfEvents",
    "VoiceSelectionParams",
    "AudioEncoding",
    "OutputAudioEncoding",
    "SpeechModelVariant",
    "SsmlVoiceGender",
    "TelephonyDtmf",
    "Context",
    "CreateContextRequest",
    "DeleteAllContextsRequest",
    "DeleteContextRequest",
    "GetContextRequest",
    "ListContextsRequest",
    "ListContextsResponse",
    "UpdateContextRequest",
    "BatchCreateMessagesRequest",
    "BatchCreateMessagesResponse",
    "CompleteConversationRequest",
    "Conversation",
    "ConversationPhoneNumber",
    "CreateConversationRequest",
    "CreateMessageRequest",
    "GenerateStatelessSuggestionRequest",
    "GenerateStatelessSuggestionResponse",
    "GenerateStatelessSummaryRequest",
    "GenerateStatelessSummaryResponse",
    "GenerateSuggestionsRequest",
    "GetConversationRequest",
    "IngestContextReferencesRequest",
    "IngestContextReferencesResponse",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListMessagesRequest",
    "ListMessagesResponse",
    "SearchKnowledgeAnswer",
    "SearchKnowledgeRequest",
    "SearchKnowledgeResponse",
    "SuggestConversationSummaryRequest",
    "SuggestConversationSummaryResponse",
    "ConversationEvent",
    "AutomatedAgentConfig",
    "ClearSuggestionFeatureConfigOperationMetadata",
    "ClearSuggestionFeatureConfigRequest",
    "ConversationProfile",
    "CreateConversationProfileRequest",
    "DeleteConversationProfileRequest",
    "GetConversationProfileRequest",
    "HumanAgentAssistantConfig",
    "HumanAgentHandoffConfig",
    "ListConversationProfilesRequest",
    "ListConversationProfilesResponse",
    "LoggingConfig",
    "NotificationConfig",
    "SetSuggestionFeatureConfigOperationMetadata",
    "SetSuggestionFeatureConfigRequest",
    "UpdateConversationProfileRequest",
    "CreateDocumentRequest",
    "DeleteDocumentRequest",
    "Document",
    "ExportOperationMetadata",
    "GetDocumentRequest",
    "ImportDocumentsRequest",
    "ImportDocumentsResponse",
    "ImportDocumentTemplate",
    "KnowledgeOperationMetadata",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ReloadDocumentRequest",
    "UpdateDocumentRequest",
    "EncryptionSpec",
    "GetEncryptionSpecRequest",
    "InitializeEncryptionSpecMetadata",
    "InitializeEncryptionSpecRequest",
    "InitializeEncryptionSpecResponse",
    "BatchCreateEntitiesRequest",
    "BatchDeleteEntitiesRequest",
    "BatchDeleteEntityTypesRequest",
    "BatchUpdateEntitiesRequest",
    "BatchUpdateEntityTypesRequest",
    "BatchUpdateEntityTypesResponse",
    "CreateEntityTypeRequest",
    "DeleteEntityTypeRequest",
    "EntityType",
    "EntityTypeBatch",
    "GetEntityTypeRequest",
    "ListEntityTypesRequest",
    "ListEntityTypesResponse",
    "UpdateEntityTypeRequest",
    "CreateEnvironmentRequest",
    "DeleteEnvironmentRequest",
    "Environment",
    "EnvironmentHistory",
    "GetEnvironmentHistoryRequest",
    "GetEnvironmentRequest",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "TextToSpeechSettings",
    "UpdateEnvironmentRequest",
    "Fulfillment",
    "GetFulfillmentRequest",
    "UpdateFulfillmentRequest",
    "GcsDestination",
    "GcsSource",
    "GcsSources",
    "ConversationContext",
    "CreateGeneratorRequest",
    "DeleteGeneratorRequest",
    "FewShotExample",
    "FreeFormContext",
    "FreeFormSuggestion",
    "Generator",
    "GeneratorSuggestion",
    "GetGeneratorRequest",
    "InferenceParameter",
    "ListGeneratorsRequest",
    "ListGeneratorsResponse",
    "MessageEntry",
    "SummarizationContext",
    "SummarizationSection",
    "SummarizationSectionList",
    "SummarySuggestion",
    "UpdateGeneratorRequest",
    "TriggerEvent",
    "HumanAgentAssistantEvent",
    "BatchDeleteIntentsRequest",
    "BatchUpdateIntentsRequest",
    "BatchUpdateIntentsResponse",
    "CreateIntentRequest",
    "DeleteIntentRequest",
    "GetIntentRequest",
    "Intent",
    "IntentBatch",
    "ListIntentsRequest",
    "ListIntentsResponse",
    "UpdateIntentRequest",
    "IntentView",
    "CreateKnowledgeBaseRequest",
    "DeleteKnowledgeBaseRequest",
    "GetKnowledgeBaseRequest",
    "KnowledgeBase",
    "ListKnowledgeBasesRequest",
    "ListKnowledgeBasesResponse",
    "UpdateKnowledgeBaseRequest",
    "AnalyzeContentRequest",
    "AnalyzeContentResponse",
    "AnnotatedMessagePart",
    "ArticleAnswer",
    "AssistQueryParameters",
    "AudioInput",
    "AutomatedAgentReply",
    "CompileSuggestionRequest",
    "CompileSuggestionResponse",
    "CreateParticipantRequest",
    "DialogflowAssistAnswer",
    "DtmfParameters",
    "FaqAnswer",
    "GenerateSuggestionsResponse",
    "GetParticipantRequest",
    "InputTextConfig",
    "IntentInput",
    "IntentSuggestion",
    "KnowledgeAssistAnswer",
    "ListParticipantsRequest",
    "ListParticipantsResponse",
    "ListSuggestionsRequest",
    "ListSuggestionsResponse",
    "Message",
    "MessageAnnotation",
    "OutputAudio",
    "Participant",
    "ResponseMessage",
    "SmartReplyAnswer",
    "StreamingAnalyzeContentRequest",
    "StreamingAnalyzeContentResponse",
    "SuggestArticlesRequest",
    "SuggestArticlesResponse",
    "SuggestDialogflowAssistsResponse",
    "SuggestFaqAnswersRequest",
    "SuggestFaqAnswersResponse",
    "Suggestion",
    "SuggestionFeature",
    "SuggestionInput",
    "SuggestionResult",
    "SuggestKnowledgeAssistRequest",
    "SuggestKnowledgeAssistResponse",
    "SuggestSmartRepliesRequest",
    "SuggestSmartRepliesResponse",
    "UpdateParticipantRequest",
    "DeletePhoneNumberRequest",
    "ListPhoneNumbersRequest",
    "ListPhoneNumbersResponse",
    "PhoneNumber",
    "UndeletePhoneNumberRequest",
    "UpdatePhoneNumberRequest",
    "CloudConversationDebuggingInfo",
    "DetectIntentRequest",
    "DetectIntentResponse",
    "EventInput",
    "KnowledgeAnswers",
    "QueryInput",
    "QueryParameters",
    "QueryResult",
    "Sentiment",
    "SentimentAnalysisRequestConfig",
    "SentimentAnalysisResult",
    "StreamingDetectIntentRequest",
    "StreamingDetectIntentResponse",
    "StreamingRecognitionResult",
    "TextInput",
    "CreateSessionEntityTypeRequest",
    "DeleteSessionEntityTypeRequest",
    "GetSessionEntityTypeRequest",
    "ListSessionEntityTypesRequest",
    "ListSessionEntityTypesResponse",
    "SessionEntityType",
    "UpdateSessionEntityTypeRequest",
    "Connection",
    "CreateSipTrunkRequest",
    "DeleteSipTrunkRequest",
    "GetSipTrunkRequest",
    "ListSipTrunksRequest",
    "ListSipTrunksResponse",
    "SipTrunk",
    "UpdateSipTrunkRequest",
    "ValidationError",
    "ValidationResult",
    "CreateVersionRequest",
    "DeleteVersionRequest",
    "GetVersionRequest",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "UpdateVersionRequest",
    "Version",
    "OriginalDetectIntentRequest",
    "WebhookRequest",
    "WebhookResponse",
)
