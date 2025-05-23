# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ....types.cloud_az_storage_blob_data_source import CloudAzStorageBlobDataSource
from ....types.cloud_box_data_source import CloudBoxDataSource
from ....types.cloud_confluence_data_source import CloudConfluenceDataSource
from ....types.cloud_google_drive_data_source import CloudGoogleDriveDataSource
from ....types.cloud_jira_data_source import CloudJiraDataSource
from ....types.cloud_notion_page_data_source import CloudNotionPageDataSource
from ....types.cloud_one_drive_data_source import CloudOneDriveDataSource
from ....types.cloud_s_3_data_source import CloudS3DataSource
from ....types.cloud_sharepoint_data_source import CloudSharepointDataSource
from ....types.cloud_slack_data_source import CloudSlackDataSource


class DataSourceUpdateComponentOne_AzureStorageBlob(CloudAzStorageBlobDataSource):
    type: typing_extensions.Literal["AZURE_STORAGE_BLOB"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_Box(CloudBoxDataSource):
    type: typing_extensions.Literal["BOX"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_Confluence(CloudConfluenceDataSource):
    type: typing_extensions.Literal["CONFLUENCE"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_GoogleDrive(CloudGoogleDriveDataSource):
    type: typing_extensions.Literal["GOOGLE_DRIVE"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_Jira(CloudJiraDataSource):
    type: typing_extensions.Literal["JIRA"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_MicrosoftOnedrive(CloudOneDriveDataSource):
    type: typing_extensions.Literal["MICROSOFT_ONEDRIVE"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_MicrosoftSharepoint(CloudSharepointDataSource):
    type: typing_extensions.Literal["MICROSOFT_SHAREPOINT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_NotionPage(CloudNotionPageDataSource):
    type: typing_extensions.Literal["NOTION_PAGE"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_S3(CloudS3DataSource):
    type: typing_extensions.Literal["S3"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class DataSourceUpdateComponentOne_Slack(CloudSlackDataSource):
    type: typing_extensions.Literal["SLACK"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


DataSourceUpdateComponentOne = typing.Union[
    DataSourceUpdateComponentOne_AzureStorageBlob,
    DataSourceUpdateComponentOne_Box,
    DataSourceUpdateComponentOne_Confluence,
    DataSourceUpdateComponentOne_GoogleDrive,
    DataSourceUpdateComponentOne_Jira,
    DataSourceUpdateComponentOne_MicrosoftOnedrive,
    DataSourceUpdateComponentOne_MicrosoftSharepoint,
    DataSourceUpdateComponentOne_NotionPage,
    DataSourceUpdateComponentOne_S3,
    DataSourceUpdateComponentOne_Slack,
]
