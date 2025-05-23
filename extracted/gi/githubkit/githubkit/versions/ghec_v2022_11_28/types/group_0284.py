"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType


class CodeScanningCodeqlDatabaseType(TypedDict):
    """CodeQL Database

    A CodeQL database.
    """

    id: int
    name: str
    language: str
    uploader: SimpleUserType
    content_type: str
    size: int
    created_at: datetime
    updated_at: datetime
    url: str
    commit_oid: NotRequired[Union[str, None]]


__all__ = ("CodeScanningCodeqlDatabaseType",)
