"""
Type annotations for inspector2 service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_inspector2.client import Inspector2Client

    session = get_session()
    async with session.create_client("inspector2") as client:
        client: Inspector2Client
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
    GetCisScanResultDetailsPaginator,
    ListAccountPermissionsPaginator,
    ListCisScanConfigurationsPaginator,
    ListCisScanResultsAggregatedByChecksPaginator,
    ListCisScanResultsAggregatedByTargetResourcePaginator,
    ListCisScansPaginator,
    ListCoveragePaginator,
    ListCoverageStatisticsPaginator,
    ListDelegatedAdminAccountsPaginator,
    ListFiltersPaginator,
    ListFindingAggregationsPaginator,
    ListFindingsPaginator,
    ListMembersPaginator,
    ListUsageTotalsPaginator,
    SearchVulnerabilitiesPaginator,
)
from .type_defs import (
    AssociateMemberRequestTypeDef,
    AssociateMemberResponseTypeDef,
    BatchGetAccountStatusRequestTypeDef,
    BatchGetAccountStatusResponseTypeDef,
    BatchGetCodeSnippetRequestTypeDef,
    BatchGetCodeSnippetResponseTypeDef,
    BatchGetFindingDetailsRequestTypeDef,
    BatchGetFindingDetailsResponseTypeDef,
    BatchGetFreeTrialInfoRequestTypeDef,
    BatchGetFreeTrialInfoResponseTypeDef,
    BatchGetMemberEc2DeepInspectionStatusRequestTypeDef,
    BatchGetMemberEc2DeepInspectionStatusResponseTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef,
    CancelFindingsReportRequestTypeDef,
    CancelFindingsReportResponseTypeDef,
    CancelSbomExportRequestTypeDef,
    CancelSbomExportResponseTypeDef,
    CreateCisScanConfigurationRequestTypeDef,
    CreateCisScanConfigurationResponseTypeDef,
    CreateFilterRequestTypeDef,
    CreateFilterResponseTypeDef,
    CreateFindingsReportRequestTypeDef,
    CreateFindingsReportResponseTypeDef,
    CreateSbomExportRequestTypeDef,
    CreateSbomExportResponseTypeDef,
    DeleteCisScanConfigurationRequestTypeDef,
    DeleteCisScanConfigurationResponseTypeDef,
    DeleteFilterRequestTypeDef,
    DeleteFilterResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DisableDelegatedAdminAccountRequestTypeDef,
    DisableDelegatedAdminAccountResponseTypeDef,
    DisableRequestTypeDef,
    DisableResponseTypeDef,
    DisassociateMemberRequestTypeDef,
    DisassociateMemberResponseTypeDef,
    EnableDelegatedAdminAccountRequestTypeDef,
    EnableDelegatedAdminAccountResponseTypeDef,
    EnableRequestTypeDef,
    EnableResponseTypeDef,
    GetCisScanReportRequestTypeDef,
    GetCisScanReportResponseTypeDef,
    GetCisScanResultDetailsRequestTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    GetConfigurationResponseTypeDef,
    GetDelegatedAdminAccountResponseTypeDef,
    GetEc2DeepInspectionConfigurationResponseTypeDef,
    GetEncryptionKeyRequestTypeDef,
    GetEncryptionKeyResponseTypeDef,
    GetFindingsReportStatusRequestTypeDef,
    GetFindingsReportStatusResponseTypeDef,
    GetMemberRequestTypeDef,
    GetMemberResponseTypeDef,
    GetSbomExportRequestTypeDef,
    GetSbomExportResponseTypeDef,
    ListAccountPermissionsRequestTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsRequestTypeDef,
    ListCisScanConfigurationsResponseTypeDef,
    ListCisScanResultsAggregatedByChecksRequestTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceRequestTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansRequestTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageRequestTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsRequestTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsRequestTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersRequestTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsRequestTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsRequestTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersRequestTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageTotalsRequestTypeDef,
    ListUsageTotalsResponseTypeDef,
    ResetEncryptionKeyRequestTypeDef,
    SearchVulnerabilitiesRequestTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SendCisSessionHealthRequestTypeDef,
    SendCisSessionTelemetryRequestTypeDef,
    StartCisSessionRequestTypeDef,
    StopCisSessionRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCisScanConfigurationRequestTypeDef,
    UpdateCisScanConfigurationResponseTypeDef,
    UpdateConfigurationRequestTypeDef,
    UpdateEc2DeepInspectionConfigurationRequestTypeDef,
    UpdateEc2DeepInspectionConfigurationResponseTypeDef,
    UpdateEncryptionKeyRequestTypeDef,
    UpdateFilterRequestTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateOrganizationConfigurationRequestTypeDef,
    UpdateOrganizationConfigurationResponseTypeDef,
    UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef,
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


__all__ = ("Inspector2Client",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Inspector2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Inspector2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#generate_presigned_url)
        """

    async def associate_member(
        self, **kwargs: Unpack[AssociateMemberRequestTypeDef]
    ) -> AssociateMemberResponseTypeDef:
        """
        Associates an Amazon Web Services account with an Amazon Inspector delegated
        administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/associate_member.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#associate_member)
        """

    async def batch_get_account_status(
        self, **kwargs: Unpack[BatchGetAccountStatusRequestTypeDef]
    ) -> BatchGetAccountStatusResponseTypeDef:
        """
        Retrieves the Amazon Inspector status of multiple Amazon Web Services accounts
        within your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_get_account_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_account_status)
        """

    async def batch_get_code_snippet(
        self, **kwargs: Unpack[BatchGetCodeSnippetRequestTypeDef]
    ) -> BatchGetCodeSnippetResponseTypeDef:
        """
        Retrieves code snippets from findings that Amazon Inspector detected code
        vulnerabilities in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_get_code_snippet.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_code_snippet)
        """

    async def batch_get_finding_details(
        self, **kwargs: Unpack[BatchGetFindingDetailsRequestTypeDef]
    ) -> BatchGetFindingDetailsResponseTypeDef:
        """
        Gets vulnerability details for findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_get_finding_details.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_finding_details)
        """

    async def batch_get_free_trial_info(
        self, **kwargs: Unpack[BatchGetFreeTrialInfoRequestTypeDef]
    ) -> BatchGetFreeTrialInfoResponseTypeDef:
        """
        Gets free trial status for multiple Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_get_free_trial_info.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_free_trial_info)
        """

    async def batch_get_member_ec2_deep_inspection_status(
        self, **kwargs: Unpack[BatchGetMemberEc2DeepInspectionStatusRequestTypeDef]
    ) -> BatchGetMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Retrieves Amazon Inspector deep inspection activation status of multiple member
        accounts within your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_get_member_ec2_deep_inspection_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_member_ec2_deep_inspection_status)
        """

    async def batch_update_member_ec2_deep_inspection_status(
        self, **kwargs: Unpack[BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef]
    ) -> BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Activates or deactivates Amazon Inspector deep inspection for the provided
        member accounts in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/batch_update_member_ec2_deep_inspection_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_update_member_ec2_deep_inspection_status)
        """

    async def cancel_findings_report(
        self, **kwargs: Unpack[CancelFindingsReportRequestTypeDef]
    ) -> CancelFindingsReportResponseTypeDef:
        """
        Cancels the given findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/cancel_findings_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#cancel_findings_report)
        """

    async def cancel_sbom_export(
        self, **kwargs: Unpack[CancelSbomExportRequestTypeDef]
    ) -> CancelSbomExportResponseTypeDef:
        """
        Cancels a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/cancel_sbom_export.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#cancel_sbom_export)
        """

    async def create_cis_scan_configuration(
        self, **kwargs: Unpack[CreateCisScanConfigurationRequestTypeDef]
    ) -> CreateCisScanConfigurationResponseTypeDef:
        """
        Creates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/create_cis_scan_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_cis_scan_configuration)
        """

    async def create_filter(
        self, **kwargs: Unpack[CreateFilterRequestTypeDef]
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a filter resource using specified filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/create_filter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_filter)
        """

    async def create_findings_report(
        self, **kwargs: Unpack[CreateFindingsReportRequestTypeDef]
    ) -> CreateFindingsReportResponseTypeDef:
        """
        Creates a finding report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/create_findings_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_findings_report)
        """

    async def create_sbom_export(
        self, **kwargs: Unpack[CreateSbomExportRequestTypeDef]
    ) -> CreateSbomExportResponseTypeDef:
        """
        Creates a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/create_sbom_export.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_sbom_export)
        """

    async def delete_cis_scan_configuration(
        self, **kwargs: Unpack[DeleteCisScanConfigurationRequestTypeDef]
    ) -> DeleteCisScanConfigurationResponseTypeDef:
        """
        Deletes a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/delete_cis_scan_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#delete_cis_scan_configuration)
        """

    async def delete_filter(
        self, **kwargs: Unpack[DeleteFilterRequestTypeDef]
    ) -> DeleteFilterResponseTypeDef:
        """
        Deletes a filter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/delete_filter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#delete_filter)
        """

    async def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Describe Amazon Inspector configuration settings for an Amazon Web Services
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/describe_organization_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#describe_organization_configuration)
        """

    async def disable(self, **kwargs: Unpack[DisableRequestTypeDef]) -> DisableResponseTypeDef:
        """
        Disables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/disable.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disable)
        """

    async def disable_delegated_admin_account(
        self, **kwargs: Unpack[DisableDelegatedAdminAccountRequestTypeDef]
    ) -> DisableDelegatedAdminAccountResponseTypeDef:
        """
        Disables the Amazon Inspector delegated administrator for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/disable_delegated_admin_account.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disable_delegated_admin_account)
        """

    async def disassociate_member(
        self, **kwargs: Unpack[DisassociateMemberRequestTypeDef]
    ) -> DisassociateMemberResponseTypeDef:
        """
        Disassociates a member account from an Amazon Inspector delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/disassociate_member.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disassociate_member)
        """

    async def enable(self, **kwargs: Unpack[EnableRequestTypeDef]) -> EnableResponseTypeDef:
        """
        Enables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/enable.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#enable)
        """

    async def enable_delegated_admin_account(
        self, **kwargs: Unpack[EnableDelegatedAdminAccountRequestTypeDef]
    ) -> EnableDelegatedAdminAccountResponseTypeDef:
        """
        Enables the Amazon Inspector delegated administrator for your Organizations
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/enable_delegated_admin_account.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#enable_delegated_admin_account)
        """

    async def get_cis_scan_report(
        self, **kwargs: Unpack[GetCisScanReportRequestTypeDef]
    ) -> GetCisScanReportResponseTypeDef:
        """
        Retrieves a CIS scan report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_cis_scan_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_cis_scan_report)
        """

    async def get_cis_scan_result_details(
        self, **kwargs: Unpack[GetCisScanResultDetailsRequestTypeDef]
    ) -> GetCisScanResultDetailsResponseTypeDef:
        """
        Retrieves CIS scan result details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_cis_scan_result_details.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_cis_scan_result_details)
        """

    async def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves setting configurations for Inspector scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_configuration)
        """

    async def get_delegated_admin_account(self) -> GetDelegatedAdminAccountResponseTypeDef:
        """
        Retrieves information about the Amazon Inspector delegated administrator for
        your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_delegated_admin_account.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_delegated_admin_account)
        """

    async def get_ec2_deep_inspection_configuration(
        self,
    ) -> GetEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Retrieves the activation status of Amazon Inspector deep inspection and custom
        paths associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_ec2_deep_inspection_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_ec2_deep_inspection_configuration)
        """

    async def get_encryption_key(
        self, **kwargs: Unpack[GetEncryptionKeyRequestTypeDef]
    ) -> GetEncryptionKeyResponseTypeDef:
        """
        Gets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_encryption_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_encryption_key)
        """

    async def get_findings_report_status(
        self, **kwargs: Unpack[GetFindingsReportStatusRequestTypeDef]
    ) -> GetFindingsReportStatusResponseTypeDef:
        """
        Gets the status of a findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_findings_report_status.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_findings_report_status)
        """

    async def get_member(
        self, **kwargs: Unpack[GetMemberRequestTypeDef]
    ) -> GetMemberResponseTypeDef:
        """
        Gets member information for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_member.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_member)
        """

    async def get_sbom_export(
        self, **kwargs: Unpack[GetSbomExportRequestTypeDef]
    ) -> GetSbomExportResponseTypeDef:
        """
        Gets details of a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_sbom_export.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_sbom_export)
        """

    async def list_account_permissions(
        self, **kwargs: Unpack[ListAccountPermissionsRequestTypeDef]
    ) -> ListAccountPermissionsResponseTypeDef:
        """
        Lists the permissions an account has to configure Amazon Inspector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_account_permissions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_account_permissions)
        """

    async def list_cis_scan_configurations(
        self, **kwargs: Unpack[ListCisScanConfigurationsRequestTypeDef]
    ) -> ListCisScanConfigurationsResponseTypeDef:
        """
        Lists CIS scan configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_cis_scan_configurations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_configurations)
        """

    async def list_cis_scan_results_aggregated_by_checks(
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByChecksRequestTypeDef]
    ) -> ListCisScanResultsAggregatedByChecksResponseTypeDef:
        """
        Lists scan results aggregated by checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_cis_scan_results_aggregated_by_checks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_results_aggregated_by_checks)
        """

    async def list_cis_scan_results_aggregated_by_target_resource(
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByTargetResourceRequestTypeDef]
    ) -> ListCisScanResultsAggregatedByTargetResourceResponseTypeDef:
        """
        Lists scan results aggregated by a target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_cis_scan_results_aggregated_by_target_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_results_aggregated_by_target_resource)
        """

    async def list_cis_scans(
        self, **kwargs: Unpack[ListCisScansRequestTypeDef]
    ) -> ListCisScansResponseTypeDef:
        """
        Returns a CIS scan list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_cis_scans.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scans)
        """

    async def list_coverage(
        self, **kwargs: Unpack[ListCoverageRequestTypeDef]
    ) -> ListCoverageResponseTypeDef:
        """
        Lists coverage details for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_coverage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_coverage)
        """

    async def list_coverage_statistics(
        self, **kwargs: Unpack[ListCoverageStatisticsRequestTypeDef]
    ) -> ListCoverageStatisticsResponseTypeDef:
        """
        Lists Amazon Inspector coverage statistics for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_coverage_statistics.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_coverage_statistics)
        """

    async def list_delegated_admin_accounts(
        self, **kwargs: Unpack[ListDelegatedAdminAccountsRequestTypeDef]
    ) -> ListDelegatedAdminAccountsResponseTypeDef:
        """
        Lists information about the Amazon Inspector delegated administrator of your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_delegated_admin_accounts.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_delegated_admin_accounts)
        """

    async def list_filters(
        self, **kwargs: Unpack[ListFiltersRequestTypeDef]
    ) -> ListFiltersResponseTypeDef:
        """
        Lists the filters associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_filters.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_filters)
        """

    async def list_finding_aggregations(
        self, **kwargs: Unpack[ListFindingAggregationsRequestTypeDef]
    ) -> ListFindingAggregationsResponseTypeDef:
        """
        Lists aggregated finding data for your environment based on specific criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_finding_aggregations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_finding_aggregations)
        """

    async def list_findings(
        self, **kwargs: Unpack[ListFindingsRequestTypeDef]
    ) -> ListFindingsResponseTypeDef:
        """
        Lists findings for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_findings.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_findings)
        """

    async def list_members(
        self, **kwargs: Unpack[ListMembersRequestTypeDef]
    ) -> ListMembersResponseTypeDef:
        """
        List members associated with the Amazon Inspector delegated administrator for
        your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_members.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_members)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_tags_for_resource)
        """

    async def list_usage_totals(
        self, **kwargs: Unpack[ListUsageTotalsRequestTypeDef]
    ) -> ListUsageTotalsResponseTypeDef:
        """
        Lists the Amazon Inspector usage totals over the last 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/list_usage_totals.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_usage_totals)
        """

    async def reset_encryption_key(
        self, **kwargs: Unpack[ResetEncryptionKeyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/reset_encryption_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#reset_encryption_key)
        """

    async def search_vulnerabilities(
        self, **kwargs: Unpack[SearchVulnerabilitiesRequestTypeDef]
    ) -> SearchVulnerabilitiesResponseTypeDef:
        """
        Lists Amazon Inspector coverage details for a specific vulnerability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/search_vulnerabilities.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#search_vulnerabilities)
        """

    async def send_cis_session_health(
        self, **kwargs: Unpack[SendCisSessionHealthRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a CIS session health.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/send_cis_session_health.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#send_cis_session_health)
        """

    async def send_cis_session_telemetry(
        self, **kwargs: Unpack[SendCisSessionTelemetryRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a CIS session telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/send_cis_session_telemetry.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#send_cis_session_telemetry)
        """

    async def start_cis_session(
        self, **kwargs: Unpack[StartCisSessionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/start_cis_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#start_cis_session)
        """

    async def stop_cis_session(
        self, **kwargs: Unpack[StopCisSessionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/stop_cis_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#stop_cis_session)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#untag_resource)
        """

    async def update_cis_scan_configuration(
        self, **kwargs: Unpack[UpdateCisScanConfigurationRequestTypeDef]
    ) -> UpdateCisScanConfigurationResponseTypeDef:
        """
        Updates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_cis_scan_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_cis_scan_configuration)
        """

    async def update_configuration(
        self, **kwargs: Unpack[UpdateConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates setting configurations for your Amazon Inspector account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_configuration)
        """

    async def update_ec2_deep_inspection_configuration(
        self, **kwargs: Unpack[UpdateEc2DeepInspectionConfigurationRequestTypeDef]
    ) -> UpdateEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Activates, deactivates Amazon Inspector deep inspection, or updates custom
        paths for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_ec2_deep_inspection_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_ec2_deep_inspection_configuration)
        """

    async def update_encryption_key(
        self, **kwargs: Unpack[UpdateEncryptionKeyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_encryption_key.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_encryption_key)
        """

    async def update_filter(
        self, **kwargs: Unpack[UpdateFilterRequestTypeDef]
    ) -> UpdateFilterResponseTypeDef:
        """
        Specifies the action that is to be applied to the findings that match the
        filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_filter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_filter)
        """

    async def update_org_ec2_deep_inspection_configuration(
        self, **kwargs: Unpack[UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the Amazon Inspector deep inspection custom paths for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_org_ec2_deep_inspection_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_org_ec2_deep_inspection_configuration)
        """

    async def update_organization_configuration(
        self, **kwargs: Unpack[UpdateOrganizationConfigurationRequestTypeDef]
    ) -> UpdateOrganizationConfigurationResponseTypeDef:
        """
        Updates the configurations for your Amazon Inspector organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/update_organization_configuration.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_organization_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_cis_scan_result_details"]
    ) -> GetCisScanResultDetailsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_permissions"]
    ) -> ListAccountPermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cis_scan_configurations"]
    ) -> ListCisScanConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_checks"]
    ) -> ListCisScanResultsAggregatedByChecksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_target_resource"]
    ) -> ListCisScanResultsAggregatedByTargetResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cis_scans"]
    ) -> ListCisScansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_coverage"]
    ) -> ListCoveragePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_coverage_statistics"]
    ) -> ListCoverageStatisticsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_delegated_admin_accounts"]
    ) -> ListDelegatedAdminAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_filters"]
    ) -> ListFiltersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_finding_aggregations"]
    ) -> ListFindingAggregationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_findings"]
    ) -> ListFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_members"]
    ) -> ListMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_usage_totals"]
    ) -> ListUsageTotalsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_vulnerabilities"]
    ) -> SearchVulnerabilitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
        """
