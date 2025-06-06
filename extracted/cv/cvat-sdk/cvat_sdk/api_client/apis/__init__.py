
# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

# CVAT REST API
#
# REST API for Computer Vision Annotation Tool (CVAT)  # noqa: E501
#
# The version of the OpenAPI document: 2.39.0
# Contact: support@cvat.ai
# Generated by: https://openapi-generator.tech


# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from cvat_sdk.api_client.api.assets_api import AssetsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from cvat_sdk.api_client.api.assets_api import AssetsApi
from cvat_sdk.api_client.api.auth_api import AuthApi
from cvat_sdk.api_client.api.cloudstorages_api import CloudstoragesApi
from cvat_sdk.api_client.api.comments_api import CommentsApi
from cvat_sdk.api_client.api.consensus_api import ConsensusApi
from cvat_sdk.api_client.api.events_api import EventsApi
from cvat_sdk.api_client.api.guides_api import GuidesApi
from cvat_sdk.api_client.api.invitations_api import InvitationsApi
from cvat_sdk.api_client.api.issues_api import IssuesApi
from cvat_sdk.api_client.api.jobs_api import JobsApi
from cvat_sdk.api_client.api.labels_api import LabelsApi
from cvat_sdk.api_client.api.lambda_api import LambdaApi
from cvat_sdk.api_client.api.memberships_api import MembershipsApi
from cvat_sdk.api_client.api.organizations_api import OrganizationsApi
from cvat_sdk.api_client.api.projects_api import ProjectsApi
from cvat_sdk.api_client.api.quality_api import QualityApi
from cvat_sdk.api_client.api.requests_api import RequestsApi
from cvat_sdk.api_client.api.schema_api import SchemaApi
from cvat_sdk.api_client.api.server_api import ServerApi
from cvat_sdk.api_client.api.tasks_api import TasksApi
from cvat_sdk.api_client.api.users_api import UsersApi
from cvat_sdk.api_client.api.webhooks_api import WebhooksApi
