"""
Type annotations for connect service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_connect.client import ConnectClient

    session = get_session()
    async with session.create_client("connect") as client:
        client: ConnectClient
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
    GetMetricDataPaginator,
    ListAgentStatusesPaginator,
    ListApprovedOriginsPaginator,
    ListAuthenticationProfilesPaginator,
    ListBotsPaginator,
    ListContactEvaluationsPaginator,
    ListContactFlowModulesPaginator,
    ListContactFlowsPaginator,
    ListContactFlowVersionsPaginator,
    ListContactReferencesPaginator,
    ListDefaultVocabulariesPaginator,
    ListEvaluationFormsPaginator,
    ListEvaluationFormVersionsPaginator,
    ListFlowAssociationsPaginator,
    ListHoursOfOperationOverridesPaginator,
    ListHoursOfOperationsPaginator,
    ListInstanceAttributesPaginator,
    ListInstancesPaginator,
    ListInstanceStorageConfigsPaginator,
    ListIntegrationAssociationsPaginator,
    ListLambdaFunctionsPaginator,
    ListLexBotsPaginator,
    ListPhoneNumbersPaginator,
    ListPhoneNumbersV2Paginator,
    ListPredefinedAttributesPaginator,
    ListPromptsPaginator,
    ListQueueQuickConnectsPaginator,
    ListQueuesPaginator,
    ListQuickConnectsPaginator,
    ListRoutingProfileQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListRulesPaginator,
    ListSecurityKeysPaginator,
    ListSecurityProfileApplicationsPaginator,
    ListSecurityProfilePermissionsPaginator,
    ListSecurityProfilesPaginator,
    ListTaskTemplatesPaginator,
    ListTrafficDistributionGroupsPaginator,
    ListTrafficDistributionGroupUsersPaginator,
    ListUseCasesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUserProficienciesPaginator,
    ListUsersPaginator,
    ListViewsPaginator,
    ListViewVersionsPaginator,
    SearchAgentStatusesPaginator,
    SearchAvailablePhoneNumbersPaginator,
    SearchContactFlowModulesPaginator,
    SearchContactFlowsPaginator,
    SearchContactsPaginator,
    SearchHoursOfOperationOverridesPaginator,
    SearchHoursOfOperationsPaginator,
    SearchPredefinedAttributesPaginator,
    SearchPromptsPaginator,
    SearchQueuesPaginator,
    SearchQuickConnectsPaginator,
    SearchResourceTagsPaginator,
    SearchRoutingProfilesPaginator,
    SearchSecurityProfilesPaginator,
    SearchUserHierarchyGroupsPaginator,
    SearchUsersPaginator,
    SearchVocabulariesPaginator,
)
from .type_defs import (
    ActivateEvaluationFormRequestTypeDef,
    ActivateEvaluationFormResponseTypeDef,
    AssociateAnalyticsDataSetRequestTypeDef,
    AssociateAnalyticsDataSetResponseTypeDef,
    AssociateApprovedOriginRequestTypeDef,
    AssociateBotRequestTypeDef,
    AssociateDefaultVocabularyRequestTypeDef,
    AssociateFlowRequestTypeDef,
    AssociateInstanceStorageConfigRequestTypeDef,
    AssociateInstanceStorageConfigResponseTypeDef,
    AssociateLambdaFunctionRequestTypeDef,
    AssociateLexBotRequestTypeDef,
    AssociatePhoneNumberContactFlowRequestTypeDef,
    AssociateQueueQuickConnectsRequestTypeDef,
    AssociateRoutingProfileQueuesRequestTypeDef,
    AssociateSecurityKeyRequestTypeDef,
    AssociateSecurityKeyResponseTypeDef,
    AssociateTrafficDistributionGroupUserRequestTypeDef,
    AssociateUserProficienciesRequestTypeDef,
    BatchAssociateAnalyticsDataSetRequestTypeDef,
    BatchAssociateAnalyticsDataSetResponseTypeDef,
    BatchDisassociateAnalyticsDataSetRequestTypeDef,
    BatchDisassociateAnalyticsDataSetResponseTypeDef,
    BatchGetAttachedFileMetadataRequestTypeDef,
    BatchGetAttachedFileMetadataResponseTypeDef,
    BatchGetFlowAssociationRequestTypeDef,
    BatchGetFlowAssociationResponseTypeDef,
    BatchPutContactRequestTypeDef,
    BatchPutContactResponseTypeDef,
    ClaimPhoneNumberRequestTypeDef,
    ClaimPhoneNumberResponseTypeDef,
    CompleteAttachedFileUploadRequestTypeDef,
    CreateAgentStatusRequestTypeDef,
    CreateAgentStatusResponseTypeDef,
    CreateContactFlowModuleRequestTypeDef,
    CreateContactFlowModuleResponseTypeDef,
    CreateContactFlowRequestTypeDef,
    CreateContactFlowResponseTypeDef,
    CreateContactFlowVersionRequestTypeDef,
    CreateContactFlowVersionResponseTypeDef,
    CreateContactRequestTypeDef,
    CreateContactResponseTypeDef,
    CreateEmailAddressRequestTypeDef,
    CreateEmailAddressResponseTypeDef,
    CreateEvaluationFormRequestTypeDef,
    CreateEvaluationFormResponseTypeDef,
    CreateHoursOfOperationOverrideRequestTypeDef,
    CreateHoursOfOperationOverrideResponseTypeDef,
    CreateHoursOfOperationRequestTypeDef,
    CreateHoursOfOperationResponseTypeDef,
    CreateInstanceRequestTypeDef,
    CreateInstanceResponseTypeDef,
    CreateIntegrationAssociationRequestTypeDef,
    CreateIntegrationAssociationResponseTypeDef,
    CreateParticipantRequestTypeDef,
    CreateParticipantResponseTypeDef,
    CreatePersistentContactAssociationRequestTypeDef,
    CreatePersistentContactAssociationResponseTypeDef,
    CreatePredefinedAttributeRequestTypeDef,
    CreatePromptRequestTypeDef,
    CreatePromptResponseTypeDef,
    CreatePushNotificationRegistrationRequestTypeDef,
    CreatePushNotificationRegistrationResponseTypeDef,
    CreateQueueRequestTypeDef,
    CreateQueueResponseTypeDef,
    CreateQuickConnectRequestTypeDef,
    CreateQuickConnectResponseTypeDef,
    CreateRoutingProfileRequestTypeDef,
    CreateRoutingProfileResponseTypeDef,
    CreateRuleRequestTypeDef,
    CreateRuleResponseTypeDef,
    CreateSecurityProfileRequestTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateTaskTemplateRequestTypeDef,
    CreateTaskTemplateResponseTypeDef,
    CreateTrafficDistributionGroupRequestTypeDef,
    CreateTrafficDistributionGroupResponseTypeDef,
    CreateUseCaseRequestTypeDef,
    CreateUseCaseResponseTypeDef,
    CreateUserHierarchyGroupRequestTypeDef,
    CreateUserHierarchyGroupResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResponseTypeDef,
    CreateViewRequestTypeDef,
    CreateViewResponseTypeDef,
    CreateViewVersionRequestTypeDef,
    CreateViewVersionResponseTypeDef,
    CreateVocabularyRequestTypeDef,
    CreateVocabularyResponseTypeDef,
    DeactivateEvaluationFormRequestTypeDef,
    DeactivateEvaluationFormResponseTypeDef,
    DeleteAttachedFileRequestTypeDef,
    DeleteContactEvaluationRequestTypeDef,
    DeleteContactFlowModuleRequestTypeDef,
    DeleteContactFlowRequestTypeDef,
    DeleteContactFlowVersionRequestTypeDef,
    DeleteEmailAddressRequestTypeDef,
    DeleteEvaluationFormRequestTypeDef,
    DeleteHoursOfOperationOverrideRequestTypeDef,
    DeleteHoursOfOperationRequestTypeDef,
    DeleteInstanceRequestTypeDef,
    DeleteIntegrationAssociationRequestTypeDef,
    DeletePredefinedAttributeRequestTypeDef,
    DeletePromptRequestTypeDef,
    DeletePushNotificationRegistrationRequestTypeDef,
    DeleteQueueRequestTypeDef,
    DeleteQuickConnectRequestTypeDef,
    DeleteRoutingProfileRequestTypeDef,
    DeleteRuleRequestTypeDef,
    DeleteSecurityProfileRequestTypeDef,
    DeleteTaskTemplateRequestTypeDef,
    DeleteTrafficDistributionGroupRequestTypeDef,
    DeleteUseCaseRequestTypeDef,
    DeleteUserHierarchyGroupRequestTypeDef,
    DeleteUserRequestTypeDef,
    DeleteViewRequestTypeDef,
    DeleteViewVersionRequestTypeDef,
    DeleteVocabularyRequestTypeDef,
    DeleteVocabularyResponseTypeDef,
    DescribeAgentStatusRequestTypeDef,
    DescribeAgentStatusResponseTypeDef,
    DescribeAuthenticationProfileRequestTypeDef,
    DescribeAuthenticationProfileResponseTypeDef,
    DescribeContactEvaluationRequestTypeDef,
    DescribeContactEvaluationResponseTypeDef,
    DescribeContactFlowModuleRequestTypeDef,
    DescribeContactFlowModuleResponseTypeDef,
    DescribeContactFlowRequestTypeDef,
    DescribeContactFlowResponseTypeDef,
    DescribeContactRequestTypeDef,
    DescribeContactResponseTypeDef,
    DescribeEmailAddressRequestTypeDef,
    DescribeEmailAddressResponseTypeDef,
    DescribeEvaluationFormRequestTypeDef,
    DescribeEvaluationFormResponseTypeDef,
    DescribeHoursOfOperationOverrideRequestTypeDef,
    DescribeHoursOfOperationOverrideResponseTypeDef,
    DescribeHoursOfOperationRequestTypeDef,
    DescribeHoursOfOperationResponseTypeDef,
    DescribeInstanceAttributeRequestTypeDef,
    DescribeInstanceAttributeResponseTypeDef,
    DescribeInstanceRequestTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribeInstanceStorageConfigRequestTypeDef,
    DescribeInstanceStorageConfigResponseTypeDef,
    DescribePhoneNumberRequestTypeDef,
    DescribePhoneNumberResponseTypeDef,
    DescribePredefinedAttributeRequestTypeDef,
    DescribePredefinedAttributeResponseTypeDef,
    DescribePromptRequestTypeDef,
    DescribePromptResponseTypeDef,
    DescribeQueueRequestTypeDef,
    DescribeQueueResponseTypeDef,
    DescribeQuickConnectRequestTypeDef,
    DescribeQuickConnectResponseTypeDef,
    DescribeRoutingProfileRequestTypeDef,
    DescribeRoutingProfileResponseTypeDef,
    DescribeRuleRequestTypeDef,
    DescribeRuleResponseTypeDef,
    DescribeSecurityProfileRequestTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeTrafficDistributionGroupRequestTypeDef,
    DescribeTrafficDistributionGroupResponseTypeDef,
    DescribeUserHierarchyGroupRequestTypeDef,
    DescribeUserHierarchyGroupResponseTypeDef,
    DescribeUserHierarchyStructureRequestTypeDef,
    DescribeUserHierarchyStructureResponseTypeDef,
    DescribeUserRequestTypeDef,
    DescribeUserResponseTypeDef,
    DescribeViewRequestTypeDef,
    DescribeViewResponseTypeDef,
    DescribeVocabularyRequestTypeDef,
    DescribeVocabularyResponseTypeDef,
    DisassociateAnalyticsDataSetRequestTypeDef,
    DisassociateApprovedOriginRequestTypeDef,
    DisassociateBotRequestTypeDef,
    DisassociateFlowRequestTypeDef,
    DisassociateInstanceStorageConfigRequestTypeDef,
    DisassociateLambdaFunctionRequestTypeDef,
    DisassociateLexBotRequestTypeDef,
    DisassociatePhoneNumberContactFlowRequestTypeDef,
    DisassociateQueueQuickConnectsRequestTypeDef,
    DisassociateRoutingProfileQueuesRequestTypeDef,
    DisassociateSecurityKeyRequestTypeDef,
    DisassociateTrafficDistributionGroupUserRequestTypeDef,
    DisassociateUserProficienciesRequestTypeDef,
    DismissUserContactRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAttachedFileRequestTypeDef,
    GetAttachedFileResponseTypeDef,
    GetContactAttributesRequestTypeDef,
    GetContactAttributesResponseTypeDef,
    GetCurrentMetricDataRequestTypeDef,
    GetCurrentMetricDataResponseTypeDef,
    GetCurrentUserDataRequestTypeDef,
    GetCurrentUserDataResponseTypeDef,
    GetEffectiveHoursOfOperationsRequestTypeDef,
    GetEffectiveHoursOfOperationsResponseTypeDef,
    GetFederationTokenRequestTypeDef,
    GetFederationTokenResponseTypeDef,
    GetFlowAssociationRequestTypeDef,
    GetFlowAssociationResponseTypeDef,
    GetMetricDataRequestTypeDef,
    GetMetricDataResponseTypeDef,
    GetMetricDataV2RequestTypeDef,
    GetMetricDataV2ResponseTypeDef,
    GetPromptFileRequestTypeDef,
    GetPromptFileResponseTypeDef,
    GetTaskTemplateRequestTypeDef,
    GetTaskTemplateResponseTypeDef,
    GetTrafficDistributionRequestTypeDef,
    GetTrafficDistributionResponseTypeDef,
    ImportPhoneNumberRequestTypeDef,
    ImportPhoneNumberResponseTypeDef,
    ListAgentStatusRequestTypeDef,
    ListAgentStatusResponseTypeDef,
    ListAnalyticsDataAssociationsRequestTypeDef,
    ListAnalyticsDataAssociationsResponseTypeDef,
    ListAnalyticsDataLakeDataSetsRequestTypeDef,
    ListAnalyticsDataLakeDataSetsResponseTypeDef,
    ListApprovedOriginsRequestTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListAssociatedContactsRequestTypeDef,
    ListAssociatedContactsResponseTypeDef,
    ListAuthenticationProfilesRequestTypeDef,
    ListAuthenticationProfilesResponseTypeDef,
    ListBotsRequestTypeDef,
    ListBotsResponseTypeDef,
    ListContactEvaluationsRequestTypeDef,
    ListContactEvaluationsResponseTypeDef,
    ListContactFlowModulesRequestTypeDef,
    ListContactFlowModulesResponseTypeDef,
    ListContactFlowsRequestTypeDef,
    ListContactFlowsResponseTypeDef,
    ListContactFlowVersionsRequestTypeDef,
    ListContactFlowVersionsResponseTypeDef,
    ListContactReferencesRequestTypeDef,
    ListContactReferencesResponseTypeDef,
    ListDefaultVocabulariesRequestTypeDef,
    ListDefaultVocabulariesResponseTypeDef,
    ListEvaluationFormsRequestTypeDef,
    ListEvaluationFormsResponseTypeDef,
    ListEvaluationFormVersionsRequestTypeDef,
    ListEvaluationFormVersionsResponseTypeDef,
    ListFlowAssociationsRequestTypeDef,
    ListFlowAssociationsResponseTypeDef,
    ListHoursOfOperationOverridesRequestTypeDef,
    ListHoursOfOperationOverridesResponseTypeDef,
    ListHoursOfOperationsRequestTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesRequestTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesRequestTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsRequestTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsRequestTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsRequestTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsRequestTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersRequestTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPhoneNumbersV2RequestTypeDef,
    ListPhoneNumbersV2ResponseTypeDef,
    ListPredefinedAttributesRequestTypeDef,
    ListPredefinedAttributesResponseTypeDef,
    ListPromptsRequestTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsRequestTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesRequestTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsRequestTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRealtimeContactAnalysisSegmentsV2RequestTypeDef,
    ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef,
    ListRoutingProfileQueuesRequestTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesRequestTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListRulesRequestTypeDef,
    ListRulesResponseTypeDef,
    ListSecurityKeysRequestTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfileApplicationsRequestTypeDef,
    ListSecurityProfileApplicationsResponseTypeDef,
    ListSecurityProfilePermissionsRequestTypeDef,
    ListSecurityProfilePermissionsResponseTypeDef,
    ListSecurityProfilesRequestTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskTemplatesRequestTypeDef,
    ListTaskTemplatesResponseTypeDef,
    ListTrafficDistributionGroupsRequestTypeDef,
    ListTrafficDistributionGroupsResponseTypeDef,
    ListTrafficDistributionGroupUsersRequestTypeDef,
    ListTrafficDistributionGroupUsersResponseTypeDef,
    ListUseCasesRequestTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsRequestTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUserProficienciesRequestTypeDef,
    ListUserProficienciesResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    ListViewsRequestTypeDef,
    ListViewsResponseTypeDef,
    ListViewVersionsRequestTypeDef,
    ListViewVersionsResponseTypeDef,
    MonitorContactRequestTypeDef,
    MonitorContactResponseTypeDef,
    PauseContactRequestTypeDef,
    PutUserStatusRequestTypeDef,
    ReleasePhoneNumberRequestTypeDef,
    ReplicateInstanceRequestTypeDef,
    ReplicateInstanceResponseTypeDef,
    ResumeContactRecordingRequestTypeDef,
    ResumeContactRequestTypeDef,
    SearchAgentStatusesRequestTypeDef,
    SearchAgentStatusesResponseTypeDef,
    SearchAvailablePhoneNumbersRequestTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SearchContactFlowModulesRequestTypeDef,
    SearchContactFlowModulesResponseTypeDef,
    SearchContactFlowsRequestTypeDef,
    SearchContactFlowsResponseTypeDef,
    SearchContactsRequestTypeDef,
    SearchContactsResponseTypeDef,
    SearchEmailAddressesRequestTypeDef,
    SearchEmailAddressesResponseTypeDef,
    SearchHoursOfOperationOverridesRequestTypeDef,
    SearchHoursOfOperationOverridesResponseTypeDef,
    SearchHoursOfOperationsRequestTypeDef,
    SearchHoursOfOperationsResponseTypeDef,
    SearchPredefinedAttributesRequestTypeDef,
    SearchPredefinedAttributesResponseTypeDef,
    SearchPromptsRequestTypeDef,
    SearchPromptsResponseTypeDef,
    SearchQueuesRequestTypeDef,
    SearchQueuesResponseTypeDef,
    SearchQuickConnectsRequestTypeDef,
    SearchQuickConnectsResponseTypeDef,
    SearchResourceTagsRequestTypeDef,
    SearchResourceTagsResponseTypeDef,
    SearchRoutingProfilesRequestTypeDef,
    SearchRoutingProfilesResponseTypeDef,
    SearchSecurityProfilesRequestTypeDef,
    SearchSecurityProfilesResponseTypeDef,
    SearchUserHierarchyGroupsRequestTypeDef,
    SearchUserHierarchyGroupsResponseTypeDef,
    SearchUsersRequestTypeDef,
    SearchUsersResponseTypeDef,
    SearchVocabulariesRequestTypeDef,
    SearchVocabulariesResponseTypeDef,
    SendChatIntegrationEventRequestTypeDef,
    SendChatIntegrationEventResponseTypeDef,
    SendOutboundEmailRequestTypeDef,
    StartAttachedFileUploadRequestTypeDef,
    StartAttachedFileUploadResponseTypeDef,
    StartChatContactRequestTypeDef,
    StartChatContactResponseTypeDef,
    StartContactEvaluationRequestTypeDef,
    StartContactEvaluationResponseTypeDef,
    StartContactRecordingRequestTypeDef,
    StartContactStreamingRequestTypeDef,
    StartContactStreamingResponseTypeDef,
    StartEmailContactRequestTypeDef,
    StartEmailContactResponseTypeDef,
    StartOutboundChatContactRequestTypeDef,
    StartOutboundChatContactResponseTypeDef,
    StartOutboundEmailContactRequestTypeDef,
    StartOutboundEmailContactResponseTypeDef,
    StartOutboundVoiceContactRequestTypeDef,
    StartOutboundVoiceContactResponseTypeDef,
    StartScreenSharingRequestTypeDef,
    StartTaskContactRequestTypeDef,
    StartTaskContactResponseTypeDef,
    StartWebRTCContactRequestTypeDef,
    StartWebRTCContactResponseTypeDef,
    StopContactRecordingRequestTypeDef,
    StopContactRequestTypeDef,
    StopContactStreamingRequestTypeDef,
    SubmitContactEvaluationRequestTypeDef,
    SubmitContactEvaluationResponseTypeDef,
    SuspendContactRecordingRequestTypeDef,
    TagContactRequestTypeDef,
    TagResourceRequestTypeDef,
    TransferContactRequestTypeDef,
    TransferContactResponseTypeDef,
    UntagContactRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAgentStatusRequestTypeDef,
    UpdateAuthenticationProfileRequestTypeDef,
    UpdateContactAttributesRequestTypeDef,
    UpdateContactEvaluationRequestTypeDef,
    UpdateContactEvaluationResponseTypeDef,
    UpdateContactFlowContentRequestTypeDef,
    UpdateContactFlowMetadataRequestTypeDef,
    UpdateContactFlowModuleContentRequestTypeDef,
    UpdateContactFlowModuleMetadataRequestTypeDef,
    UpdateContactFlowNameRequestTypeDef,
    UpdateContactRequestTypeDef,
    UpdateContactRoutingDataRequestTypeDef,
    UpdateContactScheduleRequestTypeDef,
    UpdateEmailAddressMetadataRequestTypeDef,
    UpdateEmailAddressMetadataResponseTypeDef,
    UpdateEvaluationFormRequestTypeDef,
    UpdateEvaluationFormResponseTypeDef,
    UpdateHoursOfOperationOverrideRequestTypeDef,
    UpdateHoursOfOperationRequestTypeDef,
    UpdateInstanceAttributeRequestTypeDef,
    UpdateInstanceStorageConfigRequestTypeDef,
    UpdateParticipantAuthenticationRequestTypeDef,
    UpdateParticipantRoleConfigRequestTypeDef,
    UpdatePhoneNumberMetadataRequestTypeDef,
    UpdatePhoneNumberRequestTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdatePredefinedAttributeRequestTypeDef,
    UpdatePromptRequestTypeDef,
    UpdatePromptResponseTypeDef,
    UpdateQueueHoursOfOperationRequestTypeDef,
    UpdateQueueMaxContactsRequestTypeDef,
    UpdateQueueNameRequestTypeDef,
    UpdateQueueOutboundCallerConfigRequestTypeDef,
    UpdateQueueOutboundEmailConfigRequestTypeDef,
    UpdateQueueStatusRequestTypeDef,
    UpdateQuickConnectConfigRequestTypeDef,
    UpdateQuickConnectNameRequestTypeDef,
    UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef,
    UpdateRoutingProfileConcurrencyRequestTypeDef,
    UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef,
    UpdateRoutingProfileNameRequestTypeDef,
    UpdateRoutingProfileQueuesRequestTypeDef,
    UpdateRuleRequestTypeDef,
    UpdateSecurityProfileRequestTypeDef,
    UpdateTaskTemplateRequestTypeDef,
    UpdateTaskTemplateResponseTypeDef,
    UpdateTrafficDistributionRequestTypeDef,
    UpdateUserHierarchyGroupNameRequestTypeDef,
    UpdateUserHierarchyRequestTypeDef,
    UpdateUserHierarchyStructureRequestTypeDef,
    UpdateUserIdentityInfoRequestTypeDef,
    UpdateUserPhoneConfigRequestTypeDef,
    UpdateUserProficienciesRequestTypeDef,
    UpdateUserRoutingProfileRequestTypeDef,
    UpdateUserSecurityProfilesRequestTypeDef,
    UpdateViewContentRequestTypeDef,
    UpdateViewContentResponseTypeDef,
    UpdateViewMetadataRequestTypeDef,
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

__all__ = ("ConnectClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConditionalOperationFailedException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ContactFlowNotPublishedException: Type[BotocoreClientError]
    ContactNotFoundException: Type[BotocoreClientError]
    DestinationNotAllowedException: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidContactFlowException: Type[BotocoreClientError]
    InvalidContactFlowModuleException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MaximumResultReturnedException: Type[BotocoreClientError]
    OutboundContactNotPermittedException: Type[BotocoreClientError]
    OutputTypeNotFoundException: Type[BotocoreClientError]
    PropertyValidationException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]

class ConnectClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#generate_presigned_url)
        """

    async def activate_evaluation_form(
        self, **kwargs: Unpack[ActivateEvaluationFormRequestTypeDef]
    ) -> ActivateEvaluationFormResponseTypeDef:
        """
        Activates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/activate_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#activate_evaluation_form)
        """

    async def associate_analytics_data_set(
        self, **kwargs: Unpack[AssociateAnalyticsDataSetRequestTypeDef]
    ) -> AssociateAnalyticsDataSetResponseTypeDef:
        """
        Associates the specified dataset for a Amazon Connect instance with the target
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_analytics_data_set.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_analytics_data_set)
        """

    async def associate_approved_origin(
        self, **kwargs: Unpack[AssociateApprovedOriginRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_approved_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_approved_origin)
        """

    async def associate_bot(
        self, **kwargs: Unpack[AssociateBotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_bot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_bot)
        """

    async def associate_default_vocabulary(
        self, **kwargs: Unpack[AssociateDefaultVocabularyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an existing vocabulary as the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_default_vocabulary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_default_vocabulary)
        """

    async def associate_flow(self, **kwargs: Unpack[AssociateFlowRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates a connect resource to a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_flow)
        """

    async def associate_instance_storage_config(
        self, **kwargs: Unpack[AssociateInstanceStorageConfigRequestTypeDef]
    ) -> AssociateInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_instance_storage_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_instance_storage_config)
        """

    async def associate_lambda_function(
        self, **kwargs: Unpack[AssociateLambdaFunctionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_lambda_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_lambda_function)
        """

    async def associate_lex_bot(
        self, **kwargs: Unpack[AssociateLexBotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_lex_bot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_lex_bot)
        """

    async def associate_phone_number_contact_flow(
        self, **kwargs: Unpack[AssociatePhoneNumberContactFlowRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a flow with a phone number claimed to your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_phone_number_contact_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_phone_number_contact_flow)
        """

    async def associate_queue_quick_connects(
        self, **kwargs: Unpack[AssociateQueueQuickConnectsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_queue_quick_connects.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_queue_quick_connects)
        """

    async def associate_routing_profile_queues(
        self, **kwargs: Unpack[AssociateRoutingProfileQueuesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a set of queues with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_routing_profile_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_routing_profile_queues)
        """

    async def associate_security_key(
        self, **kwargs: Unpack[AssociateSecurityKeyRequestTypeDef]
    ) -> AssociateSecurityKeyResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_security_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_security_key)
        """

    async def associate_traffic_distribution_group_user(
        self, **kwargs: Unpack[AssociateTrafficDistributionGroupUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an agent with a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_traffic_distribution_group_user.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_traffic_distribution_group_user)
        """

    async def associate_user_proficiencies(
        self, **kwargs: Unpack[AssociateUserProficienciesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a set of proficiencies with a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/associate_user_proficiencies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#associate_user_proficiencies)
        """

    async def batch_associate_analytics_data_set(
        self, **kwargs: Unpack[BatchAssociateAnalyticsDataSetRequestTypeDef]
    ) -> BatchAssociateAnalyticsDataSetResponseTypeDef:
        """
        Associates a list of analytics datasets for a given Amazon Connect instance to
        a target account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/batch_associate_analytics_data_set.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#batch_associate_analytics_data_set)
        """

    async def batch_disassociate_analytics_data_set(
        self, **kwargs: Unpack[BatchDisassociateAnalyticsDataSetRequestTypeDef]
    ) -> BatchDisassociateAnalyticsDataSetResponseTypeDef:
        """
        Removes a list of analytics datasets associated with a given Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/batch_disassociate_analytics_data_set.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#batch_disassociate_analytics_data_set)
        """

    async def batch_get_attached_file_metadata(
        self, **kwargs: Unpack[BatchGetAttachedFileMetadataRequestTypeDef]
    ) -> BatchGetAttachedFileMetadataResponseTypeDef:
        """
        Allows you to retrieve metadata about multiple attached files on an associated
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/batch_get_attached_file_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#batch_get_attached_file_metadata)
        """

    async def batch_get_flow_association(
        self, **kwargs: Unpack[BatchGetFlowAssociationRequestTypeDef]
    ) -> BatchGetFlowAssociationResponseTypeDef:
        """
        Retrieve the flow associations for the given resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/batch_get_flow_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#batch_get_flow_association)
        """

    async def batch_put_contact(
        self, **kwargs: Unpack[BatchPutContactRequestTypeDef]
    ) -> BatchPutContactResponseTypeDef:
        """
        Only the Amazon Connect outbound campaigns service principal is allowed to
        assume a role in your account and call this API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/batch_put_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#batch_put_contact)
        """

    async def claim_phone_number(
        self, **kwargs: Unpack[ClaimPhoneNumberRequestTypeDef]
    ) -> ClaimPhoneNumberResponseTypeDef:
        """
        Claims an available phone number to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/claim_phone_number.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#claim_phone_number)
        """

    async def complete_attached_file_upload(
        self, **kwargs: Unpack[CompleteAttachedFileUploadRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Allows you to confirm that the attached file has been uploaded using the
        pre-signed URL provided in the StartAttachedFileUpload API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/complete_attached_file_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#complete_attached_file_upload)
        """

    async def create_agent_status(
        self, **kwargs: Unpack[CreateAgentStatusRequestTypeDef]
    ) -> CreateAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_agent_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_agent_status)
        """

    async def create_contact(
        self, **kwargs: Unpack[CreateContactRequestTypeDef]
    ) -> CreateContactResponseTypeDef:
        """
        Only the EMAIL and VOICE channels are supported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_contact)
        """

    async def create_contact_flow(
        self, **kwargs: Unpack[CreateContactFlowRequestTypeDef]
    ) -> CreateContactFlowResponseTypeDef:
        """
        Creates a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_contact_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_contact_flow)
        """

    async def create_contact_flow_module(
        self, **kwargs: Unpack[CreateContactFlowModuleRequestTypeDef]
    ) -> CreateContactFlowModuleResponseTypeDef:
        """
        Creates a flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_contact_flow_module.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_contact_flow_module)
        """

    async def create_contact_flow_version(
        self, **kwargs: Unpack[CreateContactFlowVersionRequestTypeDef]
    ) -> CreateContactFlowVersionResponseTypeDef:
        """
        Publishes a new version of the flow provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_contact_flow_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_contact_flow_version)
        """

    async def create_email_address(
        self, **kwargs: Unpack[CreateEmailAddressRequestTypeDef]
    ) -> CreateEmailAddressResponseTypeDef:
        """
        Create new email address in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_email_address.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_email_address)
        """

    async def create_evaluation_form(
        self, **kwargs: Unpack[CreateEvaluationFormRequestTypeDef]
    ) -> CreateEvaluationFormResponseTypeDef:
        """
        Creates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_evaluation_form)
        """

    async def create_hours_of_operation(
        self, **kwargs: Unpack[CreateHoursOfOperationRequestTypeDef]
    ) -> CreateHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_hours_of_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_hours_of_operation)
        """

    async def create_hours_of_operation_override(
        self, **kwargs: Unpack[CreateHoursOfOperationOverrideRequestTypeDef]
    ) -> CreateHoursOfOperationOverrideResponseTypeDef:
        """
        Creates an hours of operation override in an Amazon Connect hours of operation
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_hours_of_operation_override.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_hours_of_operation_override)
        """

    async def create_instance(
        self, **kwargs: Unpack[CreateInstanceRequestTypeDef]
    ) -> CreateInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_instance)
        """

    async def create_integration_association(
        self, **kwargs: Unpack[CreateIntegrationAssociationRequestTypeDef]
    ) -> CreateIntegrationAssociationResponseTypeDef:
        """
        Creates an Amazon Web Services resource association with an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_integration_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_integration_association)
        """

    async def create_participant(
        self, **kwargs: Unpack[CreateParticipantRequestTypeDef]
    ) -> CreateParticipantResponseTypeDef:
        """
        Adds a new participant into an on-going chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_participant.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_participant)
        """

    async def create_persistent_contact_association(
        self, **kwargs: Unpack[CreatePersistentContactAssociationRequestTypeDef]
    ) -> CreatePersistentContactAssociationResponseTypeDef:
        """
        Enables rehydration of chats for the lifespan of a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_persistent_contact_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_persistent_contact_association)
        """

    async def create_predefined_attribute(
        self, **kwargs: Unpack[CreatePredefinedAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a new predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_predefined_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_predefined_attribute)
        """

    async def create_prompt(
        self, **kwargs: Unpack[CreatePromptRequestTypeDef]
    ) -> CreatePromptResponseTypeDef:
        """
        Creates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_prompt.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_prompt)
        """

    async def create_push_notification_registration(
        self, **kwargs: Unpack[CreatePushNotificationRegistrationRequestTypeDef]
    ) -> CreatePushNotificationRegistrationResponseTypeDef:
        """
        Creates registration for a device token and a chat contact to receive real-time
        push notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_push_notification_registration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_push_notification_registration)
        """

    async def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestTypeDef]
    ) -> CreateQueueResponseTypeDef:
        """
        Creates a new queue for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_queue)
        """

    async def create_quick_connect(
        self, **kwargs: Unpack[CreateQuickConnectRequestTypeDef]
    ) -> CreateQuickConnectResponseTypeDef:
        """
        Creates a quick connect for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_quick_connect.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_quick_connect)
        """

    async def create_routing_profile(
        self, **kwargs: Unpack[CreateRoutingProfileRequestTypeDef]
    ) -> CreateRoutingProfileResponseTypeDef:
        """
        Creates a new routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_routing_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_routing_profile)
        """

    async def create_rule(
        self, **kwargs: Unpack[CreateRuleRequestTypeDef]
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_rule)
        """

    async def create_security_profile(
        self, **kwargs: Unpack[CreateSecurityProfileRequestTypeDef]
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        Creates a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_security_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_security_profile)
        """

    async def create_task_template(
        self, **kwargs: Unpack[CreateTaskTemplateRequestTypeDef]
    ) -> CreateTaskTemplateResponseTypeDef:
        """
        Creates a new task template in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_task_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_task_template)
        """

    async def create_traffic_distribution_group(
        self, **kwargs: Unpack[CreateTrafficDistributionGroupRequestTypeDef]
    ) -> CreateTrafficDistributionGroupResponseTypeDef:
        """
        Creates a traffic distribution group given an Amazon Connect instance that has
        been replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_traffic_distribution_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_traffic_distribution_group)
        """

    async def create_use_case(
        self, **kwargs: Unpack[CreateUseCaseRequestTypeDef]
    ) -> CreateUseCaseResponseTypeDef:
        """
        Creates a use case for an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_use_case.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_use_case)
        """

    async def create_user(
        self, **kwargs: Unpack[CreateUserRequestTypeDef]
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user account for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_user.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_user)
        """

    async def create_user_hierarchy_group(
        self, **kwargs: Unpack[CreateUserHierarchyGroupRequestTypeDef]
    ) -> CreateUserHierarchyGroupResponseTypeDef:
        """
        Creates a new user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_user_hierarchy_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_user_hierarchy_group)
        """

    async def create_view(
        self, **kwargs: Unpack[CreateViewRequestTypeDef]
    ) -> CreateViewResponseTypeDef:
        """
        Creates a new view with the possible status of <code>SAVED</code> or
        <code>PUBLISHED</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_view.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_view)
        """

    async def create_view_version(
        self, **kwargs: Unpack[CreateViewVersionRequestTypeDef]
    ) -> CreateViewVersionResponseTypeDef:
        """
        Publishes a new version of the view identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_view_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_view_version)
        """

    async def create_vocabulary(
        self, **kwargs: Unpack[CreateVocabularyRequestTypeDef]
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a custom vocabulary associated with your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/create_vocabulary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#create_vocabulary)
        """

    async def deactivate_evaluation_form(
        self, **kwargs: Unpack[DeactivateEvaluationFormRequestTypeDef]
    ) -> DeactivateEvaluationFormResponseTypeDef:
        """
        Deactivates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/deactivate_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#deactivate_evaluation_form)
        """

    async def delete_attached_file(
        self, **kwargs: Unpack[DeleteAttachedFileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an attached file along with the underlying S3 Object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_attached_file.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_attached_file)
        """

    async def delete_contact_evaluation(
        self, **kwargs: Unpack[DeleteContactEvaluationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_contact_evaluation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_contact_evaluation)
        """

    async def delete_contact_flow(
        self, **kwargs: Unpack[DeleteContactFlowRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_contact_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_contact_flow)
        """

    async def delete_contact_flow_module(
        self, **kwargs: Unpack[DeleteContactFlowModuleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_contact_flow_module.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_contact_flow_module)
        """

    async def delete_contact_flow_version(
        self, **kwargs: Unpack[DeleteContactFlowVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the particular version specified in flow version identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_contact_flow_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_contact_flow_version)
        """

    async def delete_email_address(
        self, **kwargs: Unpack[DeleteEmailAddressRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes email address from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_email_address.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_email_address)
        """

    async def delete_evaluation_form(
        self, **kwargs: Unpack[DeleteEvaluationFormRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_evaluation_form)
        """

    async def delete_hours_of_operation(
        self, **kwargs: Unpack[DeleteHoursOfOperationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_hours_of_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_hours_of_operation)
        """

    async def delete_hours_of_operation_override(
        self, **kwargs: Unpack[DeleteHoursOfOperationOverrideRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an hours of operation override in an Amazon Connect hours of operation
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_hours_of_operation_override.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_hours_of_operation_override)
        """

    async def delete_instance(
        self, **kwargs: Unpack[DeleteInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_instance)
        """

    async def delete_integration_association(
        self, **kwargs: Unpack[DeleteIntegrationAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Web Services resource association from an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_integration_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_integration_association)
        """

    async def delete_predefined_attribute(
        self, **kwargs: Unpack[DeletePredefinedAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a predefined attribute from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_predefined_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_predefined_attribute)
        """

    async def delete_prompt(
        self, **kwargs: Unpack[DeletePromptRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_prompt.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_prompt)
        """

    async def delete_push_notification_registration(
        self, **kwargs: Unpack[DeletePushNotificationRegistrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes registration for a device token and a chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_push_notification_registration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_push_notification_registration)
        """

    async def delete_queue(
        self, **kwargs: Unpack[DeleteQueueRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_queue)
        """

    async def delete_quick_connect(
        self, **kwargs: Unpack[DeleteQuickConnectRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_quick_connect.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_quick_connect)
        """

    async def delete_routing_profile(
        self, **kwargs: Unpack[DeleteRoutingProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_routing_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_routing_profile)
        """

    async def delete_rule(
        self, **kwargs: Unpack[DeleteRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_rule)
        """

    async def delete_security_profile(
        self, **kwargs: Unpack[DeleteSecurityProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_security_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_security_profile)
        """

    async def delete_task_template(
        self, **kwargs: Unpack[DeleteTaskTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the task template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_task_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_task_template)
        """

    async def delete_traffic_distribution_group(
        self, **kwargs: Unpack[DeleteTrafficDistributionGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_traffic_distribution_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_traffic_distribution_group)
        """

    async def delete_use_case(
        self, **kwargs: Unpack[DeleteUseCaseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a use case from an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_use_case.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_use_case)
        """

    async def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user account from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_user.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_user)
        """

    async def delete_user_hierarchy_group(
        self, **kwargs: Unpack[DeleteUserHierarchyGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_user_hierarchy_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_user_hierarchy_group)
        """

    async def delete_view(self, **kwargs: Unpack[DeleteViewRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the view entirely.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_view.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_view)
        """

    async def delete_view_version(
        self, **kwargs: Unpack[DeleteViewVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the particular version specified in <code>ViewVersion</code> identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_view_version.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_view_version)
        """

    async def delete_vocabulary(
        self, **kwargs: Unpack[DeleteVocabularyRequestTypeDef]
    ) -> DeleteVocabularyResponseTypeDef:
        """
        Deletes the vocabulary that has the given identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/delete_vocabulary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#delete_vocabulary)
        """

    async def describe_agent_status(
        self, **kwargs: Unpack[DescribeAgentStatusRequestTypeDef]
    ) -> DescribeAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_agent_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_agent_status)
        """

    async def describe_authentication_profile(
        self, **kwargs: Unpack[DescribeAuthenticationProfileRequestTypeDef]
    ) -> DescribeAuthenticationProfileResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_authentication_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_authentication_profile)
        """

    async def describe_contact(
        self, **kwargs: Unpack[DescribeContactRequestTypeDef]
    ) -> DescribeContactResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_contact)
        """

    async def describe_contact_evaluation(
        self, **kwargs: Unpack[DescribeContactEvaluationRequestTypeDef]
    ) -> DescribeContactEvaluationResponseTypeDef:
        """
        Describes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_contact_evaluation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_contact_evaluation)
        """

    async def describe_contact_flow(
        self, **kwargs: Unpack[DescribeContactFlowRequestTypeDef]
    ) -> DescribeContactFlowResponseTypeDef:
        """
        Describes the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_contact_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_contact_flow)
        """

    async def describe_contact_flow_module(
        self, **kwargs: Unpack[DescribeContactFlowModuleRequestTypeDef]
    ) -> DescribeContactFlowModuleResponseTypeDef:
        """
        Describes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_contact_flow_module.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_contact_flow_module)
        """

    async def describe_email_address(
        self, **kwargs: Unpack[DescribeEmailAddressRequestTypeDef]
    ) -> DescribeEmailAddressResponseTypeDef:
        """
        Describe email address form the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_email_address.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_email_address)
        """

    async def describe_evaluation_form(
        self, **kwargs: Unpack[DescribeEvaluationFormRequestTypeDef]
    ) -> DescribeEvaluationFormResponseTypeDef:
        """
        Describes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_evaluation_form)
        """

    async def describe_hours_of_operation(
        self, **kwargs: Unpack[DescribeHoursOfOperationRequestTypeDef]
    ) -> DescribeHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_hours_of_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_hours_of_operation)
        """

    async def describe_hours_of_operation_override(
        self, **kwargs: Unpack[DescribeHoursOfOperationOverrideRequestTypeDef]
    ) -> DescribeHoursOfOperationOverrideResponseTypeDef:
        """
        Describes the hours of operation override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_hours_of_operation_override.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_hours_of_operation_override)
        """

    async def describe_instance(
        self, **kwargs: Unpack[DescribeInstanceRequestTypeDef]
    ) -> DescribeInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_instance)
        """

    async def describe_instance_attribute(
        self, **kwargs: Unpack[DescribeInstanceAttributeRequestTypeDef]
    ) -> DescribeInstanceAttributeResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_instance_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_instance_attribute)
        """

    async def describe_instance_storage_config(
        self, **kwargs: Unpack[DescribeInstanceStorageConfigRequestTypeDef]
    ) -> DescribeInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_instance_storage_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_instance_storage_config)
        """

    async def describe_phone_number(
        self, **kwargs: Unpack[DescribePhoneNumberRequestTypeDef]
    ) -> DescribePhoneNumberResponseTypeDef:
        """
        Gets details and status of a phone number that's claimed to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_phone_number.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_phone_number)
        """

    async def describe_predefined_attribute(
        self, **kwargs: Unpack[DescribePredefinedAttributeRequestTypeDef]
    ) -> DescribePredefinedAttributeResponseTypeDef:
        """
        Describes a predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_predefined_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_predefined_attribute)
        """

    async def describe_prompt(
        self, **kwargs: Unpack[DescribePromptRequestTypeDef]
    ) -> DescribePromptResponseTypeDef:
        """
        Describes the prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_prompt.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_prompt)
        """

    async def describe_queue(
        self, **kwargs: Unpack[DescribeQueueRequestTypeDef]
    ) -> DescribeQueueResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_queue)
        """

    async def describe_quick_connect(
        self, **kwargs: Unpack[DescribeQuickConnectRequestTypeDef]
    ) -> DescribeQuickConnectResponseTypeDef:
        """
        Describes the quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_quick_connect.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_quick_connect)
        """

    async def describe_routing_profile(
        self, **kwargs: Unpack[DescribeRoutingProfileRequestTypeDef]
    ) -> DescribeRoutingProfileResponseTypeDef:
        """
        Describes the specified routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_routing_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_routing_profile)
        """

    async def describe_rule(
        self, **kwargs: Unpack[DescribeRuleRequestTypeDef]
    ) -> DescribeRuleResponseTypeDef:
        """
        Describes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_rule)
        """

    async def describe_security_profile(
        self, **kwargs: Unpack[DescribeSecurityProfileRequestTypeDef]
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        Gets basic information about the security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_security_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_security_profile)
        """

    async def describe_traffic_distribution_group(
        self, **kwargs: Unpack[DescribeTrafficDistributionGroupRequestTypeDef]
    ) -> DescribeTrafficDistributionGroupResponseTypeDef:
        """
        Gets details and status of a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_traffic_distribution_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_traffic_distribution_group)
        """

    async def describe_user(
        self, **kwargs: Unpack[DescribeUserRequestTypeDef]
    ) -> DescribeUserResponseTypeDef:
        """
        Describes the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_user.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_user)
        """

    async def describe_user_hierarchy_group(
        self, **kwargs: Unpack[DescribeUserHierarchyGroupRequestTypeDef]
    ) -> DescribeUserHierarchyGroupResponseTypeDef:
        """
        Describes the specified hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_user_hierarchy_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_user_hierarchy_group)
        """

    async def describe_user_hierarchy_structure(
        self, **kwargs: Unpack[DescribeUserHierarchyStructureRequestTypeDef]
    ) -> DescribeUserHierarchyStructureResponseTypeDef:
        """
        Describes the hierarchy structure of the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_user_hierarchy_structure.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_user_hierarchy_structure)
        """

    async def describe_view(
        self, **kwargs: Unpack[DescribeViewRequestTypeDef]
    ) -> DescribeViewResponseTypeDef:
        """
        Retrieves the view for the specified Amazon Connect instance and view
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_view.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_view)
        """

    async def describe_vocabulary(
        self, **kwargs: Unpack[DescribeVocabularyRequestTypeDef]
    ) -> DescribeVocabularyResponseTypeDef:
        """
        Describes the specified vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/describe_vocabulary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#describe_vocabulary)
        """

    async def disassociate_analytics_data_set(
        self, **kwargs: Unpack[DisassociateAnalyticsDataSetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the dataset ID associated with a given Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_analytics_data_set.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_analytics_data_set)
        """

    async def disassociate_approved_origin(
        self, **kwargs: Unpack[DisassociateApprovedOriginRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_approved_origin.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_approved_origin)
        """

    async def disassociate_bot(
        self, **kwargs: Unpack[DisassociateBotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_bot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_bot)
        """

    async def disassociate_flow(
        self, **kwargs: Unpack[DisassociateFlowRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a connect resource from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_flow)
        """

    async def disassociate_instance_storage_config(
        self, **kwargs: Unpack[DisassociateInstanceStorageConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_instance_storage_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_instance_storage_config)
        """

    async def disassociate_lambda_function(
        self, **kwargs: Unpack[DisassociateLambdaFunctionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_lambda_function.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_lambda_function)
        """

    async def disassociate_lex_bot(
        self, **kwargs: Unpack[DisassociateLexBotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_lex_bot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_lex_bot)
        """

    async def disassociate_phone_number_contact_flow(
        self, **kwargs: Unpack[DisassociatePhoneNumberContactFlowRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the flow association from a phone number claimed to your Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_phone_number_contact_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_phone_number_contact_flow)
        """

    async def disassociate_queue_quick_connects(
        self, **kwargs: Unpack[DisassociateQueueQuickConnectsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_queue_quick_connects.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_queue_quick_connects)
        """

    async def disassociate_routing_profile_queues(
        self, **kwargs: Unpack[DisassociateRoutingProfileQueuesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a set of queues from a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_routing_profile_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_routing_profile_queues)
        """

    async def disassociate_security_key(
        self, **kwargs: Unpack[DisassociateSecurityKeyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_security_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_security_key)
        """

    async def disassociate_traffic_distribution_group_user(
        self, **kwargs: Unpack[DisassociateTrafficDistributionGroupUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates an agent from a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_traffic_distribution_group_user.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_traffic_distribution_group_user)
        """

    async def disassociate_user_proficiencies(
        self, **kwargs: Unpack[DisassociateUserProficienciesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a set of proficiencies from a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/disassociate_user_proficiencies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#disassociate_user_proficiencies)
        """

    async def dismiss_user_contact(
        self, **kwargs: Unpack[DismissUserContactRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Dismisses contacts from an agent's CCP and returns the agent to an available
        state, which allows the agent to receive a new routed contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/dismiss_user_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#dismiss_user_contact)
        """

    async def get_attached_file(
        self, **kwargs: Unpack[GetAttachedFileRequestTypeDef]
    ) -> GetAttachedFileResponseTypeDef:
        """
        Provides a pre-signed URL for download of an approved attached file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_attached_file.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_attached_file)
        """

    async def get_contact_attributes(
        self, **kwargs: Unpack[GetContactAttributesRequestTypeDef]
    ) -> GetContactAttributesResponseTypeDef:
        """
        Retrieves the contact attributes for the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_contact_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_contact_attributes)
        """

    async def get_current_metric_data(
        self, **kwargs: Unpack[GetCurrentMetricDataRequestTypeDef]
    ) -> GetCurrentMetricDataResponseTypeDef:
        """
        Gets the real-time metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_current_metric_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_current_metric_data)
        """

    async def get_current_user_data(
        self, **kwargs: Unpack[GetCurrentUserDataRequestTypeDef]
    ) -> GetCurrentUserDataResponseTypeDef:
        """
        Gets the real-time active user data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_current_user_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_current_user_data)
        """

    async def get_effective_hours_of_operations(
        self, **kwargs: Unpack[GetEffectiveHoursOfOperationsRequestTypeDef]
    ) -> GetEffectiveHoursOfOperationsResponseTypeDef:
        """
        Get the hours of operations with the effective override applied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_effective_hours_of_operations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_effective_hours_of_operations)
        """

    async def get_federation_token(
        self, **kwargs: Unpack[GetFederationTokenRequestTypeDef]
    ) -> GetFederationTokenResponseTypeDef:
        """
        Supports SAML sign-in for Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_federation_token.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_federation_token)
        """

    async def get_flow_association(
        self, **kwargs: Unpack[GetFlowAssociationRequestTypeDef]
    ) -> GetFlowAssociationResponseTypeDef:
        """
        Retrieves the flow associated for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_flow_association.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_flow_association)
        """

    async def get_metric_data(
        self, **kwargs: Unpack[GetMetricDataRequestTypeDef]
    ) -> GetMetricDataResponseTypeDef:
        """
        Gets historical metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_metric_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_metric_data)
        """

    async def get_metric_data_v2(
        self, **kwargs: Unpack[GetMetricDataV2RequestTypeDef]
    ) -> GetMetricDataV2ResponseTypeDef:
        """
        Gets metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_metric_data_v2.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_metric_data_v2)
        """

    async def get_prompt_file(
        self, **kwargs: Unpack[GetPromptFileRequestTypeDef]
    ) -> GetPromptFileResponseTypeDef:
        """
        Gets the prompt file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_prompt_file.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_prompt_file)
        """

    async def get_task_template(
        self, **kwargs: Unpack[GetTaskTemplateRequestTypeDef]
    ) -> GetTaskTemplateResponseTypeDef:
        """
        Gets details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_task_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_task_template)
        """

    async def get_traffic_distribution(
        self, **kwargs: Unpack[GetTrafficDistributionRequestTypeDef]
    ) -> GetTrafficDistributionResponseTypeDef:
        """
        Retrieves the current traffic distribution for a given traffic distribution
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_traffic_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_traffic_distribution)
        """

    async def import_phone_number(
        self, **kwargs: Unpack[ImportPhoneNumberRequestTypeDef]
    ) -> ImportPhoneNumberResponseTypeDef:
        """
        Imports a claimed phone number from an external service, such as Amazon Web
        Services End User Messaging, into an Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/import_phone_number.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#import_phone_number)
        """

    async def list_agent_statuses(
        self, **kwargs: Unpack[ListAgentStatusRequestTypeDef]
    ) -> ListAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_agent_statuses.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_agent_statuses)
        """

    async def list_analytics_data_associations(
        self, **kwargs: Unpack[ListAnalyticsDataAssociationsRequestTypeDef]
    ) -> ListAnalyticsDataAssociationsResponseTypeDef:
        """
        Lists the association status of requested dataset ID for a given Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_analytics_data_associations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_analytics_data_associations)
        """

    async def list_analytics_data_lake_data_sets(
        self, **kwargs: Unpack[ListAnalyticsDataLakeDataSetsRequestTypeDef]
    ) -> ListAnalyticsDataLakeDataSetsResponseTypeDef:
        """
        Lists the data lake datasets available to associate with for a given Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_analytics_data_lake_data_sets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_analytics_data_lake_data_sets)
        """

    async def list_approved_origins(
        self, **kwargs: Unpack[ListApprovedOriginsRequestTypeDef]
    ) -> ListApprovedOriginsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_approved_origins.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_approved_origins)
        """

    async def list_associated_contacts(
        self, **kwargs: Unpack[ListAssociatedContactsRequestTypeDef]
    ) -> ListAssociatedContactsResponseTypeDef:
        """
        Provides information about contact tree, a list of associated contacts with a
        unique identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_associated_contacts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_associated_contacts)
        """

    async def list_authentication_profiles(
        self, **kwargs: Unpack[ListAuthenticationProfilesRequestTypeDef]
    ) -> ListAuthenticationProfilesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_authentication_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_authentication_profiles)
        """

    async def list_bots(self, **kwargs: Unpack[ListBotsRequestTypeDef]) -> ListBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_bots.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_bots)
        """

    async def list_contact_evaluations(
        self, **kwargs: Unpack[ListContactEvaluationsRequestTypeDef]
    ) -> ListContactEvaluationsResponseTypeDef:
        """
        Lists contact evaluations in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_contact_evaluations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_contact_evaluations)
        """

    async def list_contact_flow_modules(
        self, **kwargs: Unpack[ListContactFlowModulesRequestTypeDef]
    ) -> ListContactFlowModulesResponseTypeDef:
        """
        Provides information about the flow modules for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_contact_flow_modules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_contact_flow_modules)
        """

    async def list_contact_flow_versions(
        self, **kwargs: Unpack[ListContactFlowVersionsRequestTypeDef]
    ) -> ListContactFlowVersionsResponseTypeDef:
        """
        Returns all the available versions for the specified Amazon Connect instance
        and flow identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_contact_flow_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_contact_flow_versions)
        """

    async def list_contact_flows(
        self, **kwargs: Unpack[ListContactFlowsRequestTypeDef]
    ) -> ListContactFlowsResponseTypeDef:
        """
        Provides information about the flows for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_contact_flows.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_contact_flows)
        """

    async def list_contact_references(
        self, **kwargs: Unpack[ListContactReferencesRequestTypeDef]
    ) -> ListContactReferencesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_contact_references.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_contact_references)
        """

    async def list_default_vocabularies(
        self, **kwargs: Unpack[ListDefaultVocabulariesRequestTypeDef]
    ) -> ListDefaultVocabulariesResponseTypeDef:
        """
        Lists the default vocabularies for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_default_vocabularies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_default_vocabularies)
        """

    async def list_evaluation_form_versions(
        self, **kwargs: Unpack[ListEvaluationFormVersionsRequestTypeDef]
    ) -> ListEvaluationFormVersionsResponseTypeDef:
        """
        Lists versions of an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_evaluation_form_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_evaluation_form_versions)
        """

    async def list_evaluation_forms(
        self, **kwargs: Unpack[ListEvaluationFormsRequestTypeDef]
    ) -> ListEvaluationFormsResponseTypeDef:
        """
        Lists evaluation forms in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_evaluation_forms.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_evaluation_forms)
        """

    async def list_flow_associations(
        self, **kwargs: Unpack[ListFlowAssociationsRequestTypeDef]
    ) -> ListFlowAssociationsResponseTypeDef:
        """
        List the flow association based on the filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_flow_associations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_flow_associations)
        """

    async def list_hours_of_operation_overrides(
        self, **kwargs: Unpack[ListHoursOfOperationOverridesRequestTypeDef]
    ) -> ListHoursOfOperationOverridesResponseTypeDef:
        """
        List the hours of operation overrides.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_hours_of_operation_overrides.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_hours_of_operation_overrides)
        """

    async def list_hours_of_operations(
        self, **kwargs: Unpack[ListHoursOfOperationsRequestTypeDef]
    ) -> ListHoursOfOperationsResponseTypeDef:
        """
        Provides information about the hours of operation for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_hours_of_operations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_hours_of_operations)
        """

    async def list_instance_attributes(
        self, **kwargs: Unpack[ListInstanceAttributesRequestTypeDef]
    ) -> ListInstanceAttributesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_instance_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_instance_attributes)
        """

    async def list_instance_storage_configs(
        self, **kwargs: Unpack[ListInstanceStorageConfigsRequestTypeDef]
    ) -> ListInstanceStorageConfigsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_instance_storage_configs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_instance_storage_configs)
        """

    async def list_instances(
        self, **kwargs: Unpack[ListInstancesRequestTypeDef]
    ) -> ListInstancesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_instances.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_instances)
        """

    async def list_integration_associations(
        self, **kwargs: Unpack[ListIntegrationAssociationsRequestTypeDef]
    ) -> ListIntegrationAssociationsResponseTypeDef:
        """
        Provides summary information about the Amazon Web Services resource
        associations for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_integration_associations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_integration_associations)
        """

    async def list_lambda_functions(
        self, **kwargs: Unpack[ListLambdaFunctionsRequestTypeDef]
    ) -> ListLambdaFunctionsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_lambda_functions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_lambda_functions)
        """

    async def list_lex_bots(
        self, **kwargs: Unpack[ListLexBotsRequestTypeDef]
    ) -> ListLexBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_lex_bots.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_lex_bots)
        """

    async def list_phone_numbers(
        self, **kwargs: Unpack[ListPhoneNumbersRequestTypeDef]
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Provides information about the phone numbers for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_phone_numbers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_phone_numbers)
        """

    async def list_phone_numbers_v2(
        self, **kwargs: Unpack[ListPhoneNumbersV2RequestTypeDef]
    ) -> ListPhoneNumbersV2ResponseTypeDef:
        """
        Lists phone numbers claimed to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_phone_numbers_v2.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_phone_numbers_v2)
        """

    async def list_predefined_attributes(
        self, **kwargs: Unpack[ListPredefinedAttributesRequestTypeDef]
    ) -> ListPredefinedAttributesResponseTypeDef:
        """
        Lists predefined attributes for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_predefined_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_predefined_attributes)
        """

    async def list_prompts(
        self, **kwargs: Unpack[ListPromptsRequestTypeDef]
    ) -> ListPromptsResponseTypeDef:
        """
        Provides information about the prompts for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_prompts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_prompts)
        """

    async def list_queue_quick_connects(
        self, **kwargs: Unpack[ListQueueQuickConnectsRequestTypeDef]
    ) -> ListQueueQuickConnectsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_queue_quick_connects.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_queue_quick_connects)
        """

    async def list_queues(
        self, **kwargs: Unpack[ListQueuesRequestTypeDef]
    ) -> ListQueuesResponseTypeDef:
        """
        Provides information about the queues for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_queues)
        """

    async def list_quick_connects(
        self, **kwargs: Unpack[ListQuickConnectsRequestTypeDef]
    ) -> ListQuickConnectsResponseTypeDef:
        """
        Provides information about the quick connects for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_quick_connects.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_quick_connects)
        """

    async def list_realtime_contact_analysis_segments_v2(
        self, **kwargs: Unpack[ListRealtimeContactAnalysisSegmentsV2RequestTypeDef]
    ) -> ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef:
        """
        Provides a list of analysis segments for a real-time chat analysis session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_realtime_contact_analysis_segments_v2.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_realtime_contact_analysis_segments_v2)
        """

    async def list_routing_profile_queues(
        self, **kwargs: Unpack[ListRoutingProfileQueuesRequestTypeDef]
    ) -> ListRoutingProfileQueuesResponseTypeDef:
        """
        Lists the queues associated with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_routing_profile_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_routing_profile_queues)
        """

    async def list_routing_profiles(
        self, **kwargs: Unpack[ListRoutingProfilesRequestTypeDef]
    ) -> ListRoutingProfilesResponseTypeDef:
        """
        Provides summary information about the routing profiles for the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_routing_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_routing_profiles)
        """

    async def list_rules(
        self, **kwargs: Unpack[ListRulesRequestTypeDef]
    ) -> ListRulesResponseTypeDef:
        """
        List all rules for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_rules)
        """

    async def list_security_keys(
        self, **kwargs: Unpack[ListSecurityKeysRequestTypeDef]
    ) -> ListSecurityKeysResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_security_keys.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_security_keys)
        """

    async def list_security_profile_applications(
        self, **kwargs: Unpack[ListSecurityProfileApplicationsRequestTypeDef]
    ) -> ListSecurityProfileApplicationsResponseTypeDef:
        """
        Returns a list of third-party applications in a specific security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_security_profile_applications.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_security_profile_applications)
        """

    async def list_security_profile_permissions(
        self, **kwargs: Unpack[ListSecurityProfilePermissionsRequestTypeDef]
    ) -> ListSecurityProfilePermissionsResponseTypeDef:
        """
        Lists the permissions granted to a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_security_profile_permissions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_security_profile_permissions)
        """

    async def list_security_profiles(
        self, **kwargs: Unpack[ListSecurityProfilesRequestTypeDef]
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        Provides summary information about the security profiles for the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_security_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_security_profiles)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_tags_for_resource)
        """

    async def list_task_templates(
        self, **kwargs: Unpack[ListTaskTemplatesRequestTypeDef]
    ) -> ListTaskTemplatesResponseTypeDef:
        """
        Lists task templates for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_task_templates.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_task_templates)
        """

    async def list_traffic_distribution_group_users(
        self, **kwargs: Unpack[ListTrafficDistributionGroupUsersRequestTypeDef]
    ) -> ListTrafficDistributionGroupUsersResponseTypeDef:
        """
        Lists traffic distribution group users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_traffic_distribution_group_users.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_traffic_distribution_group_users)
        """

    async def list_traffic_distribution_groups(
        self, **kwargs: Unpack[ListTrafficDistributionGroupsRequestTypeDef]
    ) -> ListTrafficDistributionGroupsResponseTypeDef:
        """
        Lists traffic distribution groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_traffic_distribution_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_traffic_distribution_groups)
        """

    async def list_use_cases(
        self, **kwargs: Unpack[ListUseCasesRequestTypeDef]
    ) -> ListUseCasesResponseTypeDef:
        """
        Lists the use cases for the integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_use_cases.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_use_cases)
        """

    async def list_user_hierarchy_groups(
        self, **kwargs: Unpack[ListUserHierarchyGroupsRequestTypeDef]
    ) -> ListUserHierarchyGroupsResponseTypeDef:
        """
        Provides summary information about the hierarchy groups for the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_user_hierarchy_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_user_hierarchy_groups)
        """

    async def list_user_proficiencies(
        self, **kwargs: Unpack[ListUserProficienciesRequestTypeDef]
    ) -> ListUserProficienciesResponseTypeDef:
        """
        Lists proficiencies associated with a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_user_proficiencies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_user_proficiencies)
        """

    async def list_users(
        self, **kwargs: Unpack[ListUsersRequestTypeDef]
    ) -> ListUsersResponseTypeDef:
        """
        Provides summary information about the users for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_users.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_users)
        """

    async def list_view_versions(
        self, **kwargs: Unpack[ListViewVersionsRequestTypeDef]
    ) -> ListViewVersionsResponseTypeDef:
        """
        Returns all the available versions for the specified Amazon Connect instance
        and view identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_view_versions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_view_versions)
        """

    async def list_views(
        self, **kwargs: Unpack[ListViewsRequestTypeDef]
    ) -> ListViewsResponseTypeDef:
        """
        Returns views in the given instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/list_views.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#list_views)
        """

    async def monitor_contact(
        self, **kwargs: Unpack[MonitorContactRequestTypeDef]
    ) -> MonitorContactResponseTypeDef:
        """
        Initiates silent monitoring of a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/monitor_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#monitor_contact)
        """

    async def pause_contact(self, **kwargs: Unpack[PauseContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Allows pausing an ongoing task contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/pause_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#pause_contact)
        """

    async def put_user_status(
        self, **kwargs: Unpack[PutUserStatusRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the current status of a user or agent in Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/put_user_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#put_user_status)
        """

    async def release_phone_number(
        self, **kwargs: Unpack[ReleasePhoneNumberRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Releases a phone number previously claimed to an Amazon Connect instance or
        traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/release_phone_number.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#release_phone_number)
        """

    async def replicate_instance(
        self, **kwargs: Unpack[ReplicateInstanceRequestTypeDef]
    ) -> ReplicateInstanceResponseTypeDef:
        """
        Replicates an Amazon Connect instance in the specified Amazon Web Services
        Region and copies configuration information for Amazon Connect resources across
        Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/replicate_instance.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#replicate_instance)
        """

    async def resume_contact(self, **kwargs: Unpack[ResumeContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Allows resuming a task contact in a paused state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/resume_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#resume_contact)
        """

    async def resume_contact_recording(
        self, **kwargs: Unpack[ResumeContactRecordingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, and the recording has been suspended using
        SuspendContactRecording, this API resumes recording whatever recording is
        selected in the flow configuration: call, screen, or both.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/resume_contact_recording.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#resume_contact_recording)
        """

    async def search_agent_statuses(
        self, **kwargs: Unpack[SearchAgentStatusesRequestTypeDef]
    ) -> SearchAgentStatusesResponseTypeDef:
        """
        Searches AgentStatuses in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_agent_statuses.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_agent_statuses)
        """

    async def search_available_phone_numbers(
        self, **kwargs: Unpack[SearchAvailablePhoneNumbersRequestTypeDef]
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches for available phone numbers that you can claim to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_available_phone_numbers.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_available_phone_numbers)
        """

    async def search_contact_flow_modules(
        self, **kwargs: Unpack[SearchContactFlowModulesRequestTypeDef]
    ) -> SearchContactFlowModulesResponseTypeDef:
        """
        Searches the flow modules in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_contact_flow_modules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_contact_flow_modules)
        """

    async def search_contact_flows(
        self, **kwargs: Unpack[SearchContactFlowsRequestTypeDef]
    ) -> SearchContactFlowsResponseTypeDef:
        """
        Searches the flows in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_contact_flows.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_contact_flows)
        """

    async def search_contacts(
        self, **kwargs: Unpack[SearchContactsRequestTypeDef]
    ) -> SearchContactsResponseTypeDef:
        """
        Searches contacts in an Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_contacts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_contacts)
        """

    async def search_email_addresses(
        self, **kwargs: Unpack[SearchEmailAddressesRequestTypeDef]
    ) -> SearchEmailAddressesResponseTypeDef:
        """
        Searches email address in an instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_email_addresses.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_email_addresses)
        """

    async def search_hours_of_operation_overrides(
        self, **kwargs: Unpack[SearchHoursOfOperationOverridesRequestTypeDef]
    ) -> SearchHoursOfOperationOverridesResponseTypeDef:
        """
        Searches the hours of operation overrides.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_hours_of_operation_overrides.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_hours_of_operation_overrides)
        """

    async def search_hours_of_operations(
        self, **kwargs: Unpack[SearchHoursOfOperationsRequestTypeDef]
    ) -> SearchHoursOfOperationsResponseTypeDef:
        """
        Searches the hours of operation in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_hours_of_operations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_hours_of_operations)
        """

    async def search_predefined_attributes(
        self, **kwargs: Unpack[SearchPredefinedAttributesRequestTypeDef]
    ) -> SearchPredefinedAttributesResponseTypeDef:
        """
        Searches predefined attributes that meet certain criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_predefined_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_predefined_attributes)
        """

    async def search_prompts(
        self, **kwargs: Unpack[SearchPromptsRequestTypeDef]
    ) -> SearchPromptsResponseTypeDef:
        """
        Searches prompts in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_prompts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_prompts)
        """

    async def search_queues(
        self, **kwargs: Unpack[SearchQueuesRequestTypeDef]
    ) -> SearchQueuesResponseTypeDef:
        """
        Searches queues in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_queues)
        """

    async def search_quick_connects(
        self, **kwargs: Unpack[SearchQuickConnectsRequestTypeDef]
    ) -> SearchQuickConnectsResponseTypeDef:
        """
        Searches quick connects in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_quick_connects.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_quick_connects)
        """

    async def search_resource_tags(
        self, **kwargs: Unpack[SearchResourceTagsRequestTypeDef]
    ) -> SearchResourceTagsResponseTypeDef:
        """
        Searches tags used in an Amazon Connect instance using optional search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_resource_tags.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_resource_tags)
        """

    async def search_routing_profiles(
        self, **kwargs: Unpack[SearchRoutingProfilesRequestTypeDef]
    ) -> SearchRoutingProfilesResponseTypeDef:
        """
        Searches routing profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_routing_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_routing_profiles)
        """

    async def search_security_profiles(
        self, **kwargs: Unpack[SearchSecurityProfilesRequestTypeDef]
    ) -> SearchSecurityProfilesResponseTypeDef:
        """
        Searches security profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_security_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_security_profiles)
        """

    async def search_user_hierarchy_groups(
        self, **kwargs: Unpack[SearchUserHierarchyGroupsRequestTypeDef]
    ) -> SearchUserHierarchyGroupsResponseTypeDef:
        """
        Searches UserHierarchyGroups in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_user_hierarchy_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_user_hierarchy_groups)
        """

    async def search_users(
        self, **kwargs: Unpack[SearchUsersRequestTypeDef]
    ) -> SearchUsersResponseTypeDef:
        """
        Searches users in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_users.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_users)
        """

    async def search_vocabularies(
        self, **kwargs: Unpack[SearchVocabulariesRequestTypeDef]
    ) -> SearchVocabulariesResponseTypeDef:
        """
        Searches for vocabularies within a specific Amazon Connect instance using
        <code>State</code>, <code>NameStartsWith</code>, and <code>LanguageCode</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/search_vocabularies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#search_vocabularies)
        """

    async def send_chat_integration_event(
        self, **kwargs: Unpack[SendChatIntegrationEventRequestTypeDef]
    ) -> SendChatIntegrationEventResponseTypeDef:
        """
        Processes chat integration events from Amazon Web Services or external
        integrations to Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/send_chat_integration_event.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#send_chat_integration_event)
        """

    async def send_outbound_email(
        self, **kwargs: Unpack[SendOutboundEmailRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Send outbound email for outbound campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/send_outbound_email.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#send_outbound_email)
        """

    async def start_attached_file_upload(
        self, **kwargs: Unpack[StartAttachedFileUploadRequestTypeDef]
    ) -> StartAttachedFileUploadResponseTypeDef:
        """
        Provides a pre-signed Amazon S3 URL in response for uploading your content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_attached_file_upload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_attached_file_upload)
        """

    async def start_chat_contact(
        self, **kwargs: Unpack[StartChatContactRequestTypeDef]
    ) -> StartChatContactResponseTypeDef:
        """
        Initiates a flow to start a new chat for the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_chat_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_chat_contact)
        """

    async def start_contact_evaluation(
        self, **kwargs: Unpack[StartContactEvaluationRequestTypeDef]
    ) -> StartContactEvaluationResponseTypeDef:
        """
        Starts an empty evaluation in the specified Amazon Connect instance, using the
        given evaluation form for the particular contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_contact_evaluation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_contact_evaluation)
        """

    async def start_contact_recording(
        self, **kwargs: Unpack[StartContactRecordingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts recording the contact:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_contact_recording.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_contact_recording)
        """

    async def start_contact_streaming(
        self, **kwargs: Unpack[StartContactStreamingRequestTypeDef]
    ) -> StartContactStreamingResponseTypeDef:
        """
        Initiates real-time message streaming for a new chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_contact_streaming.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_contact_streaming)
        """

    async def start_email_contact(
        self, **kwargs: Unpack[StartEmailContactRequestTypeDef]
    ) -> StartEmailContactResponseTypeDef:
        """
        Creates an inbound email contact and initiates a flow to start the email
        contact for the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_email_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_email_contact)
        """

    async def start_outbound_chat_contact(
        self, **kwargs: Unpack[StartOutboundChatContactRequestTypeDef]
    ) -> StartOutboundChatContactResponseTypeDef:
        """
        Initiates a new outbound SMS contact to a customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_outbound_chat_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_outbound_chat_contact)
        """

    async def start_outbound_email_contact(
        self, **kwargs: Unpack[StartOutboundEmailContactRequestTypeDef]
    ) -> StartOutboundEmailContactResponseTypeDef:
        """
        Initiates a flow to send an agent reply or outbound email contact (created from
        the CreateContact API) to a customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_outbound_email_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_outbound_email_contact)
        """

    async def start_outbound_voice_contact(
        self, **kwargs: Unpack[StartOutboundVoiceContactRequestTypeDef]
    ) -> StartOutboundVoiceContactResponseTypeDef:
        """
        Places an outbound call to a contact, and then initiates the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_outbound_voice_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_outbound_voice_contact)
        """

    async def start_screen_sharing(
        self, **kwargs: Unpack[StartScreenSharingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts screen sharing for a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_screen_sharing.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_screen_sharing)
        """

    async def start_task_contact(
        self, **kwargs: Unpack[StartTaskContactRequestTypeDef]
    ) -> StartTaskContactResponseTypeDef:
        """
        Initiates a flow to start a new task contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_task_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_task_contact)
        """

    async def start_web_rtc_contact(
        self, **kwargs: Unpack[StartWebRTCContactRequestTypeDef]
    ) -> StartWebRTCContactResponseTypeDef:
        """
        Places an inbound in-app, web, or video call to a contact, and then initiates
        the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/start_web_rtc_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#start_web_rtc_contact)
        """

    async def stop_contact(self, **kwargs: Unpack[StopContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Ends the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/stop_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#stop_contact)
        """

    async def stop_contact_recording(
        self, **kwargs: Unpack[StopContactRecordingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops recording a call when a contact is being recorded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/stop_contact_recording.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#stop_contact_recording)
        """

    async def stop_contact_streaming(
        self, **kwargs: Unpack[StopContactStreamingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Ends message streaming on a specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/stop_contact_streaming.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#stop_contact_streaming)
        """

    async def submit_contact_evaluation(
        self, **kwargs: Unpack[SubmitContactEvaluationRequestTypeDef]
    ) -> SubmitContactEvaluationResponseTypeDef:
        """
        Submits a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/submit_contact_evaluation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#submit_contact_evaluation)
        """

    async def suspend_contact_recording(
        self, **kwargs: Unpack[SuspendContactRecordingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, this API suspends recording whatever is
        selected in the flow configuration: call (IVR or agent), screen, or both.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/suspend_contact_recording.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#suspend_contact_recording)
        """

    async def tag_contact(self, **kwargs: Unpack[TagContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the contact resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/tag_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#tag_contact)
        """

    async def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#tag_resource)
        """

    async def transfer_contact(
        self, **kwargs: Unpack[TransferContactRequestTypeDef]
    ) -> TransferContactResponseTypeDef:
        """
        Transfers <code>TASK</code> or <code>EMAIL</code> contacts from one agent or
        queue to another agent or queue at any point after a contact is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/transfer_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#transfer_contact)
        """

    async def untag_contact(self, **kwargs: Unpack[UntagContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the contact resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/untag_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#untag_contact)
        """

    async def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#untag_resource)
        """

    async def update_agent_status(
        self, **kwargs: Unpack[UpdateAgentStatusRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_agent_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_agent_status)
        """

    async def update_authentication_profile(
        self, **kwargs: Unpack[UpdateAuthenticationProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_authentication_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_authentication_profile)
        """

    async def update_contact(self, **kwargs: Unpack[UpdateContactRequestTypeDef]) -> Dict[str, Any]:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact)
        """

    async def update_contact_attributes(
        self, **kwargs: Unpack[UpdateContactAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates user-defined contact attributes associated with the
        specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_attributes)
        """

    async def update_contact_evaluation(
        self, **kwargs: Unpack[UpdateContactEvaluationRequestTypeDef]
    ) -> UpdateContactEvaluationResponseTypeDef:
        """
        Updates details about a contact evaluation in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_evaluation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_evaluation)
        """

    async def update_contact_flow_content(
        self, **kwargs: Unpack[UpdateContactFlowContentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_flow_content.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_flow_content)
        """

    async def update_contact_flow_metadata(
        self, **kwargs: Unpack[UpdateContactFlowMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_flow_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_flow_metadata)
        """

    async def update_contact_flow_module_content(
        self, **kwargs: Unpack[UpdateContactFlowModuleContentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates specified flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_flow_module_content.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_flow_module_content)
        """

    async def update_contact_flow_module_metadata(
        self, **kwargs: Unpack[UpdateContactFlowModuleMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_flow_module_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_flow_module_metadata)
        """

    async def update_contact_flow_name(
        self, **kwargs: Unpack[UpdateContactFlowNameRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The name of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_flow_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_flow_name)
        """

    async def update_contact_routing_data(
        self, **kwargs: Unpack[UpdateContactRoutingDataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates routing priority and age on the contact (<b>QueuePriority</b> and
        <b>QueueTimeAdjustmentInSeconds</b>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_routing_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_routing_data)
        """

    async def update_contact_schedule(
        self, **kwargs: Unpack[UpdateContactScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the scheduled time of a task contact that is already scheduled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_contact_schedule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_contact_schedule)
        """

    async def update_email_address_metadata(
        self, **kwargs: Unpack[UpdateEmailAddressMetadataRequestTypeDef]
    ) -> UpdateEmailAddressMetadataResponseTypeDef:
        """
        Updates an email address metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_email_address_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_email_address_metadata)
        """

    async def update_evaluation_form(
        self, **kwargs: Unpack[UpdateEvaluationFormRequestTypeDef]
    ) -> UpdateEvaluationFormResponseTypeDef:
        """
        Updates details about a specific evaluation form version in the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_evaluation_form.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_evaluation_form)
        """

    async def update_hours_of_operation(
        self, **kwargs: Unpack[UpdateHoursOfOperationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_hours_of_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_hours_of_operation)
        """

    async def update_hours_of_operation_override(
        self, **kwargs: Unpack[UpdateHoursOfOperationOverrideRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the hours of operation override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_hours_of_operation_override.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_hours_of_operation_override)
        """

    async def update_instance_attribute(
        self, **kwargs: Unpack[UpdateInstanceAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_instance_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_instance_attribute)
        """

    async def update_instance_storage_config(
        self, **kwargs: Unpack[UpdateInstanceStorageConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_instance_storage_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_instance_storage_config)
        """

    async def update_participant_authentication(
        self, **kwargs: Unpack[UpdateParticipantAuthenticationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Instructs Amazon Connect to resume the authentication process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_participant_authentication.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_participant_authentication)
        """

    async def update_participant_role_config(
        self, **kwargs: Unpack[UpdateParticipantRoleConfigRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates timeouts for when human chat participants are to be considered idle,
        and when agents are automatically disconnected from a chat due to idleness.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_participant_role_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_participant_role_config)
        """

    async def update_phone_number(
        self, **kwargs: Unpack[UpdatePhoneNumberRequestTypeDef]
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates your claimed phone number from its current Amazon Connect instance or
        traffic distribution group to another Amazon Connect instance or traffic
        distribution group in the same Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_phone_number.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_phone_number)
        """

    async def update_phone_number_metadata(
        self, **kwargs: Unpack[UpdatePhoneNumberMetadataRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a phone number's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_phone_number_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_phone_number_metadata)
        """

    async def update_predefined_attribute(
        self, **kwargs: Unpack[UpdatePredefinedAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_predefined_attribute.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_predefined_attribute)
        """

    async def update_prompt(
        self, **kwargs: Unpack[UpdatePromptRequestTypeDef]
    ) -> UpdatePromptResponseTypeDef:
        """
        Updates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_prompt.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_prompt)
        """

    async def update_queue_hours_of_operation(
        self, **kwargs: Unpack[UpdateQueueHoursOfOperationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_hours_of_operation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_hours_of_operation)
        """

    async def update_queue_max_contacts(
        self, **kwargs: Unpack[UpdateQueueMaxContactsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_max_contacts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_max_contacts)
        """

    async def update_queue_name(
        self, **kwargs: Unpack[UpdateQueueNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_name)
        """

    async def update_queue_outbound_caller_config(
        self, **kwargs: Unpack[UpdateQueueOutboundCallerConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_outbound_caller_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_outbound_caller_config)
        """

    async def update_queue_outbound_email_config(
        self, **kwargs: Unpack[UpdateQueueOutboundEmailConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the outbound email address Id for a specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_outbound_email_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_outbound_email_config)
        """

    async def update_queue_status(
        self, **kwargs: Unpack[UpdateQueueStatusRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_queue_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_queue_status)
        """

    async def update_quick_connect_config(
        self, **kwargs: Unpack[UpdateQuickConnectConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the configuration settings for the specified quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_quick_connect_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_quick_connect_config)
        """

    async def update_quick_connect_name(
        self, **kwargs: Unpack[UpdateQuickConnectNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and description of a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_quick_connect_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_quick_connect_name)
        """

    async def update_routing_profile_agent_availability_timer(
        self, **kwargs: Unpack[UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Whether agents with this routing profile will have their routing order
        calculated based on <i>time since their last inbound contact</i> or <i>longest
        idle time</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_routing_profile_agent_availability_timer.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_routing_profile_agent_availability_timer)
        """

    async def update_routing_profile_concurrency(
        self, **kwargs: Unpack[UpdateRoutingProfileConcurrencyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the channels that agents can handle in the Contact Control Panel (CCP)
        for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_routing_profile_concurrency.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_routing_profile_concurrency)
        """

    async def update_routing_profile_default_outbound_queue(
        self, **kwargs: Unpack[UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the default outbound queue of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_routing_profile_default_outbound_queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_routing_profile_default_outbound_queue)
        """

    async def update_routing_profile_name(
        self, **kwargs: Unpack[UpdateRoutingProfileNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and description of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_routing_profile_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_routing_profile_name)
        """

    async def update_routing_profile_queues(
        self, **kwargs: Unpack[UpdateRoutingProfileQueuesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the properties associated with a set of queues for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_routing_profile_queues.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_routing_profile_queues)
        """

    async def update_rule(
        self, **kwargs: Unpack[UpdateRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_rule)
        """

    async def update_security_profile(
        self, **kwargs: Unpack[UpdateSecurityProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_security_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_security_profile)
        """

    async def update_task_template(
        self, **kwargs: Unpack[UpdateTaskTemplateRequestTypeDef]
    ) -> UpdateTaskTemplateResponseTypeDef:
        """
        Updates details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_task_template.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_task_template)
        """

    async def update_traffic_distribution(
        self, **kwargs: Unpack[UpdateTrafficDistributionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the traffic distribution for a given traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_traffic_distribution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_traffic_distribution)
        """

    async def update_user_hierarchy(
        self, **kwargs: Unpack[UpdateUserHierarchyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified hierarchy group to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_hierarchy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_hierarchy)
        """

    async def update_user_hierarchy_group_name(
        self, **kwargs: Unpack[UpdateUserHierarchyGroupNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name of the user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_hierarchy_group_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_hierarchy_group_name)
        """

    async def update_user_hierarchy_structure(
        self, **kwargs: Unpack[UpdateUserHierarchyStructureRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the user hierarchy structure: add, remove, and rename user hierarchy
        levels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_hierarchy_structure.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_hierarchy_structure)
        """

    async def update_user_identity_info(
        self, **kwargs: Unpack[UpdateUserIdentityInfoRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the identity information for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_identity_info.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_identity_info)
        """

    async def update_user_phone_config(
        self, **kwargs: Unpack[UpdateUserPhoneConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the phone configuration settings for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_phone_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_phone_config)
        """

    async def update_user_proficiencies(
        self, **kwargs: Unpack[UpdateUserProficienciesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the properties associated with the proficiencies of a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_proficiencies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_proficiencies)
        """

    async def update_user_routing_profile(
        self, **kwargs: Unpack[UpdateUserRoutingProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified routing profile to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_routing_profile.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_routing_profile)
        """

    async def update_user_security_profiles(
        self, **kwargs: Unpack[UpdateUserSecurityProfilesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified security profiles to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_user_security_profiles.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_user_security_profiles)
        """

    async def update_view_content(
        self, **kwargs: Unpack[UpdateViewContentRequestTypeDef]
    ) -> UpdateViewContentResponseTypeDef:
        """
        Updates the view content of the given view identifier in the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_view_content.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_view_content)
        """

    async def update_view_metadata(
        self, **kwargs: Unpack[UpdateViewMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the view metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/update_view_metadata.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#update_view_metadata)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_metric_data"]
    ) -> GetMetricDataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_statuses"]
    ) -> ListAgentStatusesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_approved_origins"]
    ) -> ListApprovedOriginsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_authentication_profiles"]
    ) -> ListAuthenticationProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bots"]
    ) -> ListBotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_evaluations"]
    ) -> ListContactEvaluationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_flow_modules"]
    ) -> ListContactFlowModulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_flow_versions"]
    ) -> ListContactFlowVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_flows"]
    ) -> ListContactFlowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_references"]
    ) -> ListContactReferencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_default_vocabularies"]
    ) -> ListDefaultVocabulariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_evaluation_form_versions"]
    ) -> ListEvaluationFormVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_evaluation_forms"]
    ) -> ListEvaluationFormsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_associations"]
    ) -> ListFlowAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hours_of_operation_overrides"]
    ) -> ListHoursOfOperationOverridesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> ListHoursOfOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_attributes"]
    ) -> ListInstanceAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_storage_configs"]
    ) -> ListInstanceStorageConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instances"]
    ) -> ListInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_integration_associations"]
    ) -> ListIntegrationAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lambda_functions"]
    ) -> ListLambdaFunctionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lex_bots"]
    ) -> ListLexBotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_phone_numbers"]
    ) -> ListPhoneNumbersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_phone_numbers_v2"]
    ) -> ListPhoneNumbersV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_predefined_attributes"]
    ) -> ListPredefinedAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_prompts"]
    ) -> ListPromptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queue_quick_connects"]
    ) -> ListQueueQuickConnectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queues"]
    ) -> ListQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_quick_connects"]
    ) -> ListQuickConnectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_routing_profile_queues"]
    ) -> ListRoutingProfileQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_routing_profiles"]
    ) -> ListRoutingProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_keys"]
    ) -> ListSecurityKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_profile_applications"]
    ) -> ListSecurityProfileApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_profile_permissions"]
    ) -> ListSecurityProfilePermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_task_templates"]
    ) -> ListTaskTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_traffic_distribution_group_users"]
    ) -> ListTrafficDistributionGroupUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_traffic_distribution_groups"]
    ) -> ListTrafficDistributionGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_use_cases"]
    ) -> ListUseCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> ListUserHierarchyGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_proficiencies"]
    ) -> ListUserProficienciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_view_versions"]
    ) -> ListViewVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_views"]
    ) -> ListViewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_agent_statuses"]
    ) -> SearchAgentStatusesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_available_phone_numbers"]
    ) -> SearchAvailablePhoneNumbersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_contact_flow_modules"]
    ) -> SearchContactFlowModulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_contact_flows"]
    ) -> SearchContactFlowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_contacts"]
    ) -> SearchContactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_hours_of_operation_overrides"]
    ) -> SearchHoursOfOperationOverridesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_hours_of_operations"]
    ) -> SearchHoursOfOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_predefined_attributes"]
    ) -> SearchPredefinedAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_prompts"]
    ) -> SearchPromptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_queues"]
    ) -> SearchQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_quick_connects"]
    ) -> SearchQuickConnectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_resource_tags"]
    ) -> SearchResourceTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_routing_profiles"]
    ) -> SearchRoutingProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_security_profiles"]
    ) -> SearchSecurityProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_user_hierarchy_groups"]
    ) -> SearchUserHierarchyGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_users"]
    ) -> SearchUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_vocabularies"]
    ) -> SearchVocabulariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/client/)
        """
