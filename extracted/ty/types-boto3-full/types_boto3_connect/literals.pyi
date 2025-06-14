"""
Type annotations for connect service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from types_boto3_connect.literals import ActionTypeType

    data: ActionTypeType = "ASSIGN_CONTACT_CATEGORY"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionTypeType",
    "AgentAvailabilityTimerType",
    "AgentStatusStateType",
    "AgentStatusTypeType",
    "AnsweringMachineDetectionStatusType",
    "ArtifactStatusType",
    "BehaviorTypeType",
    "ChannelType",
    "ChatEventTypeType",
    "ComparisonType",
    "ConnectServiceName",
    "ContactFlowModuleStateType",
    "ContactFlowModuleStatusType",
    "ContactFlowStateType",
    "ContactFlowStatusType",
    "ContactFlowTypeType",
    "ContactInitiationMethodType",
    "ContactRecordingTypeType",
    "ContactStateType",
    "CurrentMetricNameType",
    "DateComparisonTypeType",
    "DeviceTypeType",
    "DirectoryTypeType",
    "EmailHeaderTypeType",
    "EncryptionTypeType",
    "EndpointTypeType",
    "EvaluationFormQuestionTypeType",
    "EvaluationFormScoringModeType",
    "EvaluationFormScoringStatusType",
    "EvaluationFormSingleSelectQuestionDisplayModeType",
    "EvaluationFormVersionStatusType",
    "EvaluationStatusType",
    "EventSourceNameType",
    "FailureReasonCodeType",
    "FileStatusTypeType",
    "FileUseCaseTypeType",
    "FlowAssociationResourceTypeType",
    "GetMetricDataPaginatorName",
    "GroupingType",
    "HierarchyGroupMatchTypeType",
    "HistoricalMetricNameType",
    "HoursOfOperationDaysType",
    "InboundMessageSourceTypeType",
    "InitiateAsType",
    "InstanceAttributeTypeType",
    "InstanceReplicationStatusType",
    "InstanceStatusType",
    "InstanceStorageResourceTypeType",
    "IntegrationTypeType",
    "IntervalPeriodType",
    "IvrRecordingTrackType",
    "LexVersionType",
    "ListAgentStatusesPaginatorName",
    "ListApprovedOriginsPaginatorName",
    "ListAuthenticationProfilesPaginatorName",
    "ListBotsPaginatorName",
    "ListContactEvaluationsPaginatorName",
    "ListContactFlowModulesPaginatorName",
    "ListContactFlowVersionsPaginatorName",
    "ListContactFlowsPaginatorName",
    "ListContactReferencesPaginatorName",
    "ListDefaultVocabulariesPaginatorName",
    "ListEvaluationFormVersionsPaginatorName",
    "ListEvaluationFormsPaginatorName",
    "ListFlowAssociationResourceTypeType",
    "ListFlowAssociationsPaginatorName",
    "ListHoursOfOperationOverridesPaginatorName",
    "ListHoursOfOperationsPaginatorName",
    "ListInstanceAttributesPaginatorName",
    "ListInstanceStorageConfigsPaginatorName",
    "ListInstancesPaginatorName",
    "ListIntegrationAssociationsPaginatorName",
    "ListLambdaFunctionsPaginatorName",
    "ListLexBotsPaginatorName",
    "ListPhoneNumbersPaginatorName",
    "ListPhoneNumbersV2PaginatorName",
    "ListPredefinedAttributesPaginatorName",
    "ListPromptsPaginatorName",
    "ListQueueQuickConnectsPaginatorName",
    "ListQueuesPaginatorName",
    "ListQuickConnectsPaginatorName",
    "ListRoutingProfileQueuesPaginatorName",
    "ListRoutingProfilesPaginatorName",
    "ListRulesPaginatorName",
    "ListSecurityKeysPaginatorName",
    "ListSecurityProfileApplicationsPaginatorName",
    "ListSecurityProfilePermissionsPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListTaskTemplatesPaginatorName",
    "ListTrafficDistributionGroupUsersPaginatorName",
    "ListTrafficDistributionGroupsPaginatorName",
    "ListUseCasesPaginatorName",
    "ListUserHierarchyGroupsPaginatorName",
    "ListUserProficienciesPaginatorName",
    "ListUsersPaginatorName",
    "ListViewVersionsPaginatorName",
    "ListViewsPaginatorName",
    "MediaStreamTypeType",
    "MeetingFeatureStatusType",
    "MonitorCapabilityType",
    "NotificationContentTypeType",
    "NotificationDeliveryTypeType",
    "NumberComparisonTypeType",
    "NumericQuestionPropertyAutomationLabelType",
    "OutboundMessageSourceTypeType",
    "OverrideDaysType",
    "PaginatorName",
    "ParticipantRoleType",
    "ParticipantStateType",
    "ParticipantTimerActionType",
    "ParticipantTimerTypeType",
    "ParticipantTypeType",
    "PhoneNumberCountryCodeType",
    "PhoneNumberTypeType",
    "PhoneNumberWorkflowStatusType",
    "PhoneTypeType",
    "QueueStatusType",
    "QueueTypeType",
    "QuickConnectTypeType",
    "RealTimeContactAnalysisOutputTypeType",
    "RealTimeContactAnalysisPostContactSummaryFailureCodeType",
    "RealTimeContactAnalysisPostContactSummaryStatusType",
    "RealTimeContactAnalysisSegmentTypeType",
    "RealTimeContactAnalysisSentimentLabelType",
    "RealTimeContactAnalysisStatusType",
    "RealTimeContactAnalysisSupportedChannelType",
    "RecordingStatusType",
    "ReferenceStatusType",
    "ReferenceTypeType",
    "RegionName",
    "RehydrationTypeType",
    "ResourceServiceName",
    "RoutingCriteriaStepStatusType",
    "RulePublishStatusType",
    "ScreenShareCapabilityType",
    "SearchAgentStatusesPaginatorName",
    "SearchAvailablePhoneNumbersPaginatorName",
    "SearchContactFlowModulesPaginatorName",
    "SearchContactFlowsPaginatorName",
    "SearchContactsMatchTypeType",
    "SearchContactsPaginatorName",
    "SearchContactsTimeRangeTypeType",
    "SearchHoursOfOperationOverridesPaginatorName",
    "SearchHoursOfOperationsPaginatorName",
    "SearchPredefinedAttributesPaginatorName",
    "SearchPromptsPaginatorName",
    "SearchQueuesPaginatorName",
    "SearchQuickConnectsPaginatorName",
    "SearchResourceTagsPaginatorName",
    "SearchRoutingProfilesPaginatorName",
    "SearchSecurityProfilesPaginatorName",
    "SearchUserHierarchyGroupsPaginatorName",
    "SearchUsersPaginatorName",
    "SearchVocabulariesPaginatorName",
    "SearchableQueueTypeType",
    "ServiceName",
    "SingleSelectQuestionRuleCategoryAutomationConditionType",
    "SlaAssignmentTypeType",
    "SlaTypeType",
    "SortOrderType",
    "SortableFieldNameType",
    "SourceTypeType",
    "StatisticType",
    "StatusType",
    "StorageTypeType",
    "StringComparisonTypeType",
    "TargetListTypeType",
    "TaskTemplateFieldTypeType",
    "TaskTemplateStatusType",
    "TimerEligibleParticipantRolesType",
    "TrafficDistributionGroupStatusType",
    "TrafficTypeType",
    "UnitType",
    "UseCaseTypeType",
    "VideoCapabilityType",
    "ViewStatusType",
    "ViewTypeType",
    "VocabularyLanguageCodeType",
    "VocabularyStateType",
    "VoiceRecordingTrackType",
)

ActionTypeType = Literal[
    "ASSIGN_CONTACT_CATEGORY",
    "ASSIGN_SLA",
    "CREATE_CASE",
    "CREATE_TASK",
    "END_ASSOCIATED_TASKS",
    "GENERATE_EVENTBRIDGE_EVENT",
    "SEND_NOTIFICATION",
    "SUBMIT_AUTO_EVALUATION",
    "UPDATE_CASE",
]
AgentAvailabilityTimerType = Literal["TIME_SINCE_LAST_ACTIVITY", "TIME_SINCE_LAST_INBOUND"]
AgentStatusStateType = Literal["DISABLED", "ENABLED"]
AgentStatusTypeType = Literal["CUSTOM", "OFFLINE", "ROUTABLE"]
AnsweringMachineDetectionStatusType = Literal[
    "AMD_ERROR",
    "AMD_NOT_APPLICABLE",
    "AMD_UNANSWERED",
    "AMD_UNRESOLVED",
    "ANSWERED",
    "ERROR",
    "FAX_MACHINE_DETECTED",
    "HUMAN_ANSWERED",
    "SIT_TONE_BUSY",
    "SIT_TONE_DETECTED",
    "SIT_TONE_INVALID_NUMBER",
    "UNDETECTED",
    "VOICEMAIL_BEEP",
    "VOICEMAIL_NO_BEEP",
]
ArtifactStatusType = Literal["APPROVED", "IN_PROGRESS", "REJECTED"]
BehaviorTypeType = Literal["ROUTE_ANY_CHANNEL", "ROUTE_CURRENT_CHANNEL_ONLY"]
ChannelType = Literal["CHAT", "EMAIL", "TASK", "VOICE"]
ChatEventTypeType = Literal["DISCONNECT", "EVENT", "MESSAGE"]
ComparisonType = Literal["LT"]
ContactFlowModuleStateType = Literal["ACTIVE", "ARCHIVED"]
ContactFlowModuleStatusType = Literal["PUBLISHED", "SAVED"]
ContactFlowStateType = Literal["ACTIVE", "ARCHIVED"]
ContactFlowStatusType = Literal["PUBLISHED", "SAVED"]
ContactFlowTypeType = Literal[
    "AGENT_HOLD",
    "AGENT_TRANSFER",
    "AGENT_WHISPER",
    "CAMPAIGN",
    "CONTACT_FLOW",
    "CUSTOMER_HOLD",
    "CUSTOMER_QUEUE",
    "CUSTOMER_WHISPER",
    "OUTBOUND_WHISPER",
    "QUEUE_TRANSFER",
]
ContactInitiationMethodType = Literal[
    "AGENT_REPLY",
    "API",
    "CALLBACK",
    "DISCONNECT",
    "EXTERNAL_OUTBOUND",
    "FLOW",
    "INBOUND",
    "MONITOR",
    "OUTBOUND",
    "QUEUE_TRANSFER",
    "TRANSFER",
    "WEBRTC_API",
]
ContactRecordingTypeType = Literal["AGENT", "IVR", "SCREEN"]
ContactStateType = Literal[
    "CONNECTED",
    "CONNECTED_ONHOLD",
    "CONNECTING",
    "ENDED",
    "ERROR",
    "INCOMING",
    "MISSED",
    "PENDING",
    "REJECTED",
]
CurrentMetricNameType = Literal[
    "AGENTS_AFTER_CONTACT_WORK",
    "AGENTS_AVAILABLE",
    "AGENTS_ERROR",
    "AGENTS_NON_PRODUCTIVE",
    "AGENTS_ONLINE",
    "AGENTS_ON_CALL",
    "AGENTS_ON_CONTACT",
    "AGENTS_STAFFED",
    "CONTACTS_IN_QUEUE",
    "CONTACTS_SCHEDULED",
    "OLDEST_CONTACT_AGE",
    "SLOTS_ACTIVE",
    "SLOTS_AVAILABLE",
]
DateComparisonTypeType = Literal[
    "EQUAL_TO", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO"
]
DeviceTypeType = Literal["APNS", "APNS_SANDBOX", "GCM"]
DirectoryTypeType = Literal["CONNECT_MANAGED", "EXISTING_DIRECTORY", "SAML"]
EmailHeaderTypeType = Literal[
    "IN_REPLY_TO", "MESSAGE_ID", "REFERENCES", "X_SES_SPAM_VERDICT", "X_SES_VIRUS_VERDICT"
]
EncryptionTypeType = Literal["KMS"]
EndpointTypeType = Literal[
    "CONNECT_PHONENUMBER_ARN", "CONTACT_FLOW", "EMAIL_ADDRESS", "TELEPHONE_NUMBER", "VOIP"
]
EvaluationFormQuestionTypeType = Literal["NUMERIC", "SINGLESELECT", "TEXT"]
EvaluationFormScoringModeType = Literal["QUESTION_ONLY", "SECTION_ONLY"]
EvaluationFormScoringStatusType = Literal["DISABLED", "ENABLED"]
EvaluationFormSingleSelectQuestionDisplayModeType = Literal["DROPDOWN", "RADIO"]
EvaluationFormVersionStatusType = Literal["ACTIVE", "DRAFT"]
EvaluationStatusType = Literal["DRAFT", "SUBMITTED"]
EventSourceNameType = Literal[
    "OnCaseCreate",
    "OnCaseUpdate",
    "OnContactEvaluationSubmit",
    "OnMetricDataUpdate",
    "OnPostCallAnalysisAvailable",
    "OnPostChatAnalysisAvailable",
    "OnRealTimeCallAnalysisAvailable",
    "OnRealTimeChatAnalysisAvailable",
    "OnSalesforceCaseCreate",
    "OnSlaBreach",
    "OnZendeskTicketCreate",
    "OnZendeskTicketStatusUpdate",
]
FailureReasonCodeType = Literal[
    "IDEMPOTENCY_EXCEPTION",
    "INTERNAL_ERROR",
    "INVALID_ATTRIBUTE_KEY",
    "INVALID_CUSTOMER_ENDPOINT",
    "INVALID_QUEUE",
    "INVALID_SYSTEM_ENDPOINT",
    "MISSING_CAMPAIGN",
    "MISSING_CUSTOMER_ENDPOINT",
    "MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT",
    "REQUEST_THROTTLED",
]
FileStatusTypeType = Literal["APPROVED", "FAILED", "PROCESSING", "REJECTED"]
FileUseCaseTypeType = Literal["ATTACHMENT", "EMAIL_MESSAGE"]
FlowAssociationResourceTypeType = Literal[
    "ANALYTICS_CONNECTOR",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "SMS_PHONE_NUMBER",
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
]
GetMetricDataPaginatorName = Literal["get_metric_data"]
GroupingType = Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE", "ROUTING_STEP_EXPRESSION"]
HierarchyGroupMatchTypeType = Literal["EXACT", "WITH_CHILD_GROUPS"]
HistoricalMetricNameType = Literal[
    "ABANDON_TIME",
    "AFTER_CONTACT_WORK_TIME",
    "API_CONTACTS_HANDLED",
    "CALLBACK_CONTACTS_HANDLED",
    "CONTACTS_ABANDONED",
    "CONTACTS_AGENT_HUNG_UP_FIRST",
    "CONTACTS_CONSULTED",
    "CONTACTS_HANDLED",
    "CONTACTS_HANDLED_INCOMING",
    "CONTACTS_HANDLED_OUTBOUND",
    "CONTACTS_HOLD_ABANDONS",
    "CONTACTS_MISSED",
    "CONTACTS_QUEUED",
    "CONTACTS_TRANSFERRED_IN",
    "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
    "CONTACTS_TRANSFERRED_OUT",
    "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
    "HANDLE_TIME",
    "HOLD_TIME",
    "INTERACTION_AND_HOLD_TIME",
    "INTERACTION_TIME",
    "OCCUPANCY",
    "QUEUED_TIME",
    "QUEUE_ANSWER_TIME",
    "SERVICE_LEVEL",
]
HoursOfOperationDaysType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
InboundMessageSourceTypeType = Literal["RAW"]
InitiateAsType = Literal["CONNECTED_TO_USER"]
InstanceAttributeTypeType = Literal[
    "AUTO_RESOLVE_BEST_VOICES",
    "CONTACTFLOW_LOGS",
    "CONTACT_LENS",
    "EARLY_MEDIA",
    "ENHANCED_CHAT_MONITORING",
    "ENHANCED_CONTACT_MONITORING",
    "HIGH_VOLUME_OUTBOUND",
    "INBOUND_CALLS",
    "MULTI_PARTY_CHAT_CONFERENCE",
    "MULTI_PARTY_CONFERENCE",
    "OUTBOUND_CALLS",
    "USE_CUSTOM_TTS_VOICES",
]
InstanceReplicationStatusType = Literal[
    "INSTANCE_REPLICATION_COMPLETE",
    "INSTANCE_REPLICATION_DELETION_FAILED",
    "INSTANCE_REPLICATION_FAILED",
    "INSTANCE_REPLICATION_IN_PROGRESS",
    "INSTANCE_REPLICA_DELETING",
    "RESOURCE_REPLICATION_NOT_STARTED",
]
InstanceStatusType = Literal["ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS"]
InstanceStorageResourceTypeType = Literal[
    "AGENT_EVENTS",
    "ATTACHMENTS",
    "CALL_RECORDINGS",
    "CHAT_TRANSCRIPTS",
    "CONTACT_EVALUATIONS",
    "CONTACT_TRACE_RECORDS",
    "EMAIL_MESSAGES",
    "MEDIA_STREAMS",
    "REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS",
    "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
    "REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS",
    "SCHEDULED_REPORTS",
    "SCREEN_RECORDINGS",
]
IntegrationTypeType = Literal[
    "ANALYTICS_CONNECTOR",
    "APPLICATION",
    "CALL_TRANSFER_CONNECTOR",
    "CASES_DOMAIN",
    "COGNITO_USER_POOL",
    "EVENT",
    "FILE_SCANNER",
    "PINPOINT_APP",
    "Q_MESSAGE_TEMPLATES",
    "SES_IDENTITY",
    "VOICE_ID",
    "WISDOM_ASSISTANT",
    "WISDOM_KNOWLEDGE_BASE",
    "WISDOM_QUICK_RESPONSES",
]
IntervalPeriodType = Literal["DAY", "FIFTEEN_MIN", "HOUR", "THIRTY_MIN", "TOTAL", "WEEK"]
IvrRecordingTrackType = Literal["ALL"]
LexVersionType = Literal["V1", "V2"]
ListAgentStatusesPaginatorName = Literal["list_agent_statuses"]
ListApprovedOriginsPaginatorName = Literal["list_approved_origins"]
ListAuthenticationProfilesPaginatorName = Literal["list_authentication_profiles"]
ListBotsPaginatorName = Literal["list_bots"]
ListContactEvaluationsPaginatorName = Literal["list_contact_evaluations"]
ListContactFlowModulesPaginatorName = Literal["list_contact_flow_modules"]
ListContactFlowVersionsPaginatorName = Literal["list_contact_flow_versions"]
ListContactFlowsPaginatorName = Literal["list_contact_flows"]
ListContactReferencesPaginatorName = Literal["list_contact_references"]
ListDefaultVocabulariesPaginatorName = Literal["list_default_vocabularies"]
ListEvaluationFormVersionsPaginatorName = Literal["list_evaluation_form_versions"]
ListEvaluationFormsPaginatorName = Literal["list_evaluation_forms"]
ListFlowAssociationResourceTypeType = Literal[
    "ANALYTICS_CONNECTOR",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "VOICE_PHONE_NUMBER",
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
]
ListFlowAssociationsPaginatorName = Literal["list_flow_associations"]
ListHoursOfOperationOverridesPaginatorName = Literal["list_hours_of_operation_overrides"]
ListHoursOfOperationsPaginatorName = Literal["list_hours_of_operations"]
ListInstanceAttributesPaginatorName = Literal["list_instance_attributes"]
ListInstanceStorageConfigsPaginatorName = Literal["list_instance_storage_configs"]
ListInstancesPaginatorName = Literal["list_instances"]
ListIntegrationAssociationsPaginatorName = Literal["list_integration_associations"]
ListLambdaFunctionsPaginatorName = Literal["list_lambda_functions"]
ListLexBotsPaginatorName = Literal["list_lex_bots"]
ListPhoneNumbersPaginatorName = Literal["list_phone_numbers"]
ListPhoneNumbersV2PaginatorName = Literal["list_phone_numbers_v2"]
ListPredefinedAttributesPaginatorName = Literal["list_predefined_attributes"]
ListPromptsPaginatorName = Literal["list_prompts"]
ListQueueQuickConnectsPaginatorName = Literal["list_queue_quick_connects"]
ListQueuesPaginatorName = Literal["list_queues"]
ListQuickConnectsPaginatorName = Literal["list_quick_connects"]
ListRoutingProfileQueuesPaginatorName = Literal["list_routing_profile_queues"]
ListRoutingProfilesPaginatorName = Literal["list_routing_profiles"]
ListRulesPaginatorName = Literal["list_rules"]
ListSecurityKeysPaginatorName = Literal["list_security_keys"]
ListSecurityProfileApplicationsPaginatorName = Literal["list_security_profile_applications"]
ListSecurityProfilePermissionsPaginatorName = Literal["list_security_profile_permissions"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListTaskTemplatesPaginatorName = Literal["list_task_templates"]
ListTrafficDistributionGroupUsersPaginatorName = Literal["list_traffic_distribution_group_users"]
ListTrafficDistributionGroupsPaginatorName = Literal["list_traffic_distribution_groups"]
ListUseCasesPaginatorName = Literal["list_use_cases"]
ListUserHierarchyGroupsPaginatorName = Literal["list_user_hierarchy_groups"]
ListUserProficienciesPaginatorName = Literal["list_user_proficiencies"]
ListUsersPaginatorName = Literal["list_users"]
ListViewVersionsPaginatorName = Literal["list_view_versions"]
ListViewsPaginatorName = Literal["list_views"]
MediaStreamTypeType = Literal["AUDIO", "VIDEO"]
MeetingFeatureStatusType = Literal["AVAILABLE", "UNAVAILABLE"]
MonitorCapabilityType = Literal["BARGE", "SILENT_MONITOR"]
NotificationContentTypeType = Literal["PLAIN_TEXT"]
NotificationDeliveryTypeType = Literal["EMAIL"]
NumberComparisonTypeType = Literal[
    "EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESSER", "LESSER_OR_EQUAL", "NOT_EQUAL", "RANGE"
]
NumericQuestionPropertyAutomationLabelType = Literal[
    "AGENT_INTERACTION_DURATION",
    "CONTACT_DURATION",
    "CUSTOMER_HOLD_TIME",
    "NON_TALK_TIME",
    "NON_TALK_TIME_PERCENTAGE",
    "NUMBER_OF_INTERRUPTIONS",
    "OVERALL_AGENT_SENTIMENT_SCORE",
    "OVERALL_CUSTOMER_SENTIMENT_SCORE",
]
OutboundMessageSourceTypeType = Literal["RAW", "TEMPLATE"]
OverrideDaysType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
ParticipantRoleType = Literal["AGENT", "CUSTOMER", "CUSTOM_BOT", "SUPERVISOR", "SYSTEM"]
ParticipantStateType = Literal["CONNECTED", "DISCONNECTED", "INITIAL", "MISSED"]
ParticipantTimerActionType = Literal["Unset"]
ParticipantTimerTypeType = Literal["DISCONNECT_NONCUSTOMER", "IDLE"]
ParticipantTypeType = Literal["AGENT", "ALL", "CUSTOMER", "MANAGER", "THIRDPARTY"]
PhoneNumberCountryCodeType = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AN",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BR",
    "BS",
    "BT",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GQ",
    "GR",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]
PhoneNumberTypeType = Literal[
    "DID", "SHARED", "SHORT_CODE", "THIRD_PARTY_DID", "THIRD_PARTY_TF", "TOLL_FREE", "UIFN"
]
PhoneNumberWorkflowStatusType = Literal["CLAIMED", "FAILED", "IN_PROGRESS"]
PhoneTypeType = Literal["DESK_PHONE", "SOFT_PHONE"]
QueueStatusType = Literal["DISABLED", "ENABLED"]
QueueTypeType = Literal["AGENT", "STANDARD"]
QuickConnectTypeType = Literal["PHONE_NUMBER", "QUEUE", "USER"]
RealTimeContactAnalysisOutputTypeType = Literal["Raw", "Redacted"]
RealTimeContactAnalysisPostContactSummaryFailureCodeType = Literal[
    "FAILED_SAFETY_GUIDELINES",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "INTERNAL_ERROR",
    "INVALID_ANALYSIS_CONFIGURATION",
    "QUOTA_EXCEEDED",
]
RealTimeContactAnalysisPostContactSummaryStatusType = Literal["COMPLETED", "FAILED"]
RealTimeContactAnalysisSegmentTypeType = Literal[
    "Attachments", "Categories", "Event", "Issues", "PostContactSummary", "Transcript"
]
RealTimeContactAnalysisSentimentLabelType = Literal["NEGATIVE", "NEUTRAL", "POSITIVE"]
RealTimeContactAnalysisStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
RealTimeContactAnalysisSupportedChannelType = Literal["CHAT", "VOICE"]
RecordingStatusType = Literal["AVAILABLE", "DELETED"]
ReferenceStatusType = Literal[
    "APPROVED", "AVAILABLE", "DELETED", "FAILED", "PROCESSING", "REJECTED"
]
ReferenceTypeType = Literal[
    "ATTACHMENT", "CONTACT_ANALYSIS", "DATE", "EMAIL", "EMAIL_MESSAGE", "NUMBER", "STRING", "URL"
]
RehydrationTypeType = Literal["ENTIRE_PAST_SESSION", "FROM_SEGMENT"]
RoutingCriteriaStepStatusType = Literal["ACTIVE", "EXPIRED", "INACTIVE", "JOINED"]
RulePublishStatusType = Literal["DRAFT", "PUBLISHED"]
ScreenShareCapabilityType = Literal["SEND"]
SearchAgentStatusesPaginatorName = Literal["search_agent_statuses"]
SearchAvailablePhoneNumbersPaginatorName = Literal["search_available_phone_numbers"]
SearchContactFlowModulesPaginatorName = Literal["search_contact_flow_modules"]
SearchContactFlowsPaginatorName = Literal["search_contact_flows"]
SearchContactsMatchTypeType = Literal["MATCH_ALL", "MATCH_ANY"]
SearchContactsPaginatorName = Literal["search_contacts"]
SearchContactsTimeRangeTypeType = Literal[
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
]
SearchHoursOfOperationOverridesPaginatorName = Literal["search_hours_of_operation_overrides"]
SearchHoursOfOperationsPaginatorName = Literal["search_hours_of_operations"]
SearchPredefinedAttributesPaginatorName = Literal["search_predefined_attributes"]
SearchPromptsPaginatorName = Literal["search_prompts"]
SearchQueuesPaginatorName = Literal["search_queues"]
SearchQuickConnectsPaginatorName = Literal["search_quick_connects"]
SearchResourceTagsPaginatorName = Literal["search_resource_tags"]
SearchRoutingProfilesPaginatorName = Literal["search_routing_profiles"]
SearchSecurityProfilesPaginatorName = Literal["search_security_profiles"]
SearchUserHierarchyGroupsPaginatorName = Literal["search_user_hierarchy_groups"]
SearchUsersPaginatorName = Literal["search_users"]
SearchVocabulariesPaginatorName = Literal["search_vocabularies"]
SearchableQueueTypeType = Literal["STANDARD"]
SingleSelectQuestionRuleCategoryAutomationConditionType = Literal["NOT_PRESENT", "PRESENT"]
SlaAssignmentTypeType = Literal["CASES"]
SlaTypeType = Literal["CaseField"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SortableFieldNameType = Literal[
    "CHANNEL",
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "INITIATION_METHOD",
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
]
SourceTypeType = Literal["CASES", "SALESFORCE", "ZENDESK"]
StatisticType = Literal["AVG", "MAX", "SUM"]
StatusType = Literal["COMPLETE", "DELETED", "IN_PROGRESS"]
StorageTypeType = Literal["KINESIS_FIREHOSE", "KINESIS_STREAM", "KINESIS_VIDEO_STREAM", "S3"]
StringComparisonTypeType = Literal["CONTAINS", "EXACT", "STARTS_WITH"]
TargetListTypeType = Literal["PROFICIENCIES"]
TaskTemplateFieldTypeType = Literal[
    "BOOLEAN",
    "DATE_TIME",
    "DESCRIPTION",
    "EMAIL",
    "EXPIRY_DURATION",
    "NAME",
    "NUMBER",
    "QUICK_CONNECT",
    "SCHEDULED_TIME",
    "SELF_ASSIGN",
    "SINGLE_SELECT",
    "TEXT",
    "TEXT_AREA",
    "URL",
]
TaskTemplateStatusType = Literal["ACTIVE", "INACTIVE"]
TimerEligibleParticipantRolesType = Literal["AGENT", "CUSTOMER"]
TrafficDistributionGroupStatusType = Literal[
    "ACTIVE",
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "DELETION_FAILED",
    "PENDING_DELETION",
    "UPDATE_IN_PROGRESS",
]
TrafficTypeType = Literal["CAMPAIGN", "GENERAL"]
UnitType = Literal["COUNT", "PERCENT", "SECONDS"]
UseCaseTypeType = Literal["CONNECT_CAMPAIGNS", "RULES_EVALUATION"]
VideoCapabilityType = Literal["SEND"]
ViewStatusType = Literal["PUBLISHED", "SAVED"]
ViewTypeType = Literal["AWS_MANAGED", "CUSTOMER_MANAGED"]
VocabularyLanguageCodeType = Literal[
    "ar-AE",
    "ca-ES",
    "da-DK",
    "de-CH",
    "de-DE",
    "en-AB",
    "en-AU",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-WL",
    "en-ZA",
    "es-ES",
    "es-US",
    "fi-FI",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "ms-MY",
    "nl-NL",
    "no-NO",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "sv-SE",
    "tl-PH",
    "zh-CN",
]
VocabularyStateType = Literal[
    "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
]
VoiceRecordingTrackType = Literal["ALL", "FROM_AGENT", "TO_AGENT"]
ConnectServiceName = Literal["connect"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupsearch",
    "batch",
    "bcm-data-exports",
    "bcm-pricing-calculator",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-data-automation",
    "bedrock-data-automation-runtime",
    "bedrock-runtime",
    "billing",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcampaignsv2",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "ds-data",
    "dsql",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "evs",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "gameliftstreams",
    "geo-maps",
    "geo-places",
    "geo-routes",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "invoicing",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot-managed-integrations",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplace-reporting",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkflowmonitor",
    "networkmanager",
    "networkmonitor",
    "notifications",
    "notificationscontacts",
    "oam",
    "observabilityadmin",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "partnercentral-selling",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "pcs",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "proton",
    "qapps",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "s3tables",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "security-ir",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "snow-device-management",
    "snowball",
    "sns",
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-guiconnect",
    "ssm-incidents",
    "ssm-quicksetup",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "get_metric_data",
    "list_agent_statuses",
    "list_approved_origins",
    "list_authentication_profiles",
    "list_bots",
    "list_contact_evaluations",
    "list_contact_flow_modules",
    "list_contact_flow_versions",
    "list_contact_flows",
    "list_contact_references",
    "list_default_vocabularies",
    "list_evaluation_form_versions",
    "list_evaluation_forms",
    "list_flow_associations",
    "list_hours_of_operation_overrides",
    "list_hours_of_operations",
    "list_instance_attributes",
    "list_instance_storage_configs",
    "list_instances",
    "list_integration_associations",
    "list_lambda_functions",
    "list_lex_bots",
    "list_phone_numbers",
    "list_phone_numbers_v2",
    "list_predefined_attributes",
    "list_prompts",
    "list_queue_quick_connects",
    "list_queues",
    "list_quick_connects",
    "list_routing_profile_queues",
    "list_routing_profiles",
    "list_rules",
    "list_security_keys",
    "list_security_profile_applications",
    "list_security_profile_permissions",
    "list_security_profiles",
    "list_task_templates",
    "list_traffic_distribution_group_users",
    "list_traffic_distribution_groups",
    "list_use_cases",
    "list_user_hierarchy_groups",
    "list_user_proficiencies",
    "list_users",
    "list_view_versions",
    "list_views",
    "search_agent_statuses",
    "search_available_phone_numbers",
    "search_contact_flow_modules",
    "search_contact_flows",
    "search_contacts",
    "search_hours_of_operation_overrides",
    "search_hours_of_operations",
    "search_predefined_attributes",
    "search_prompts",
    "search_queues",
    "search_quick_connects",
    "search_resource_tags",
    "search_routing_profiles",
    "search_security_profiles",
    "search_user_hierarchy_groups",
    "search_users",
    "search_vocabularies",
]
RegionName = Literal[
    "af-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-2",
    "us-east-1",
    "us-west-2",
]
