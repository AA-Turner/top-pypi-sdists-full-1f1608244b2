"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0010 import IntegrationType


class DeploymentStatusType(TypedDict):
    """Deployment Status

    The status of a deployment.
    """

    url: str
    id: int
    node_id: str
    state: Literal[
        "error", "failure", "inactive", "pending", "success", "queued", "in_progress"
    ]
    creator: Union[None, SimpleUserType]
    description: str
    environment: NotRequired[str]
    target_url: str
    created_at: datetime
    updated_at: datetime
    deployment_url: str
    repository_url: str
    environment_url: NotRequired[str]
    log_url: NotRequired[str]
    performed_via_github_app: NotRequired[Union[None, IntegrationType, None]]


__all__ = ("DeploymentStatusType",)
