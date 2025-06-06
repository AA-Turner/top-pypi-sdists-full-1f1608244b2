"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgReposPostBody(GitHubModel):
    """OrgsOrgReposPostBody"""

    name: str = Field(description="The name of the repository.")
    description: Missing[str] = Field(
        default=UNSET, description="A short description of the repository."
    )
    homepage: Missing[str] = Field(
        default=UNSET, description="A URL with more information about the repository."
    )
    private: Missing[bool] = Field(
        default=UNSET, description="Whether the repository is private."
    )
    visibility: Missing[Literal["public", "private", "internal"]] = Field(
        default=UNSET, description="The visibility of the repository."
    )
    has_issues: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable issues for this repository or `false` to disable them.",
    )
    has_projects: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.",
    )
    has_wiki: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to enable the wiki for this repository or `false` to disable it.",
    )
    has_downloads: Missing[bool] = Field(
        default=UNSET, description="Whether downloads are enabled."
    )
    is_template: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to make this repo available as a template repository or `false` to prevent it.",
    )
    team_id: Missing[int] = Field(
        default=UNSET,
        description="The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.",
    )
    auto_init: Missing[bool] = Field(
        default=UNSET,
        description="Pass `true` to create an initial commit with empty README.",
    )
    gitignore_template: Missing[str] = Field(
        default=UNSET,
        description='Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For example, "Haskell".',
    )
    license_template: Missing[str] = Field(
        default=UNSET,
        description='Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://docs.github.com/enterprise-cloud@latest//articles/licensing-a-repository/#searching-github-by-license-type) as the `license_template` string. For example, "mit" or "mpl-2.0".',
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.",
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.",
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.",
    )
    allow_auto_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.",
    )
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion. **The authenticated user must be an organization owner to set this property to `true`.**",
    )
    use_squash_pr_title_as_default: Missing[bool] = Field(
        default=UNSET,
        description="Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. **This property is closing down. Please use `squash_merge_commit_title` instead.",
    )
    squash_merge_commit_title: Missing[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]] = (
        Field(
            default=UNSET,
            description="Required when using `squash_merge_commit_message`.\n\nThe default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
        )
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description="Required when using `merge_commit_message`.\n\nThe default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    custom_properties: Missing[OrgsOrgReposPostBodyPropCustomProperties] = Field(
        default=UNSET,
        description="The custom properties for the new repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )


class OrgsOrgReposPostBodyPropCustomProperties(ExtraGitHubModel):
    """OrgsOrgReposPostBodyPropCustomProperties

    The custom properties for the new repository. The keys are the custom property
    names, and the values are the corresponding custom property values.
    """


model_rebuild(OrgsOrgReposPostBody)
model_rebuild(OrgsOrgReposPostBodyPropCustomProperties)

__all__ = (
    "OrgsOrgReposPostBody",
    "OrgsOrgReposPostBodyPropCustomProperties",
)
