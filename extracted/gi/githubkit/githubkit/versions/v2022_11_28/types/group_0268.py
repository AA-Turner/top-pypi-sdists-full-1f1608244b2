"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

from .group_0003 import SimpleUserType


class StatusType(TypedDict):
    """Status

    The status of a commit.
    """

    url: str
    avatar_url: Union[str, None]
    id: int
    node_id: str
    state: str
    description: Union[str, None]
    target_url: Union[str, None]
    context: str
    created_at: str
    updated_at: str
    creator: Union[None, SimpleUserType]


__all__ = ("StatusType",)
