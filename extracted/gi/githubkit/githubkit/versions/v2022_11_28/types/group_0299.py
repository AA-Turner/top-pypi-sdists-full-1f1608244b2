"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class GitRefType(TypedDict):
    """Git Reference

    Git references within a repository
    """

    ref: str
    node_id: str
    url: str
    object_: GitRefPropObjectType


class GitRefPropObjectType(TypedDict):
    """GitRefPropObject"""

    type: str
    sha: str
    url: str


__all__ = (
    "GitRefPropObjectType",
    "GitRefType",
)
