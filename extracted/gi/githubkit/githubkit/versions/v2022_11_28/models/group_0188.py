"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser


class TeamProject(GitHubModel):
    """Team Project

    A team's access to a project.
    """

    owner_url: str = Field()
    url: str = Field()
    html_url: str = Field()
    columns_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    name: str = Field()
    body: Union[str, None] = Field()
    number: int = Field()
    state: str = Field()
    creator: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    created_at: str = Field()
    updated_at: str = Field()
    organization_permission: Missing[str] = Field(
        default=UNSET,
        description="The organization permission for this project. Only present when owner is an organization.",
    )
    private: Missing[bool] = Field(
        default=UNSET,
        description="Whether the project is private or not. Only present when owner is an organization.",
    )
    permissions: TeamProjectPropPermissions = Field()


class TeamProjectPropPermissions(GitHubModel):
    """TeamProjectPropPermissions"""

    read: bool = Field()
    write: bool = Field()
    admin: bool = Field()


model_rebuild(TeamProject)
model_rebuild(TeamProjectPropPermissions)

__all__ = (
    "TeamProject",
    "TeamProjectPropPermissions",
)
