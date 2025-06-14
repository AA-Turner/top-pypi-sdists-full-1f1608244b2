# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .avatar import Avatar


class UserWithAvatar(object):
    _types = {
        "id": str,
        "name": str,
        "is_deleted": bool,
        "i18n_name": List[I18n],
        "avatar": Avatar,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.is_deleted: Optional[bool] = None
        self.i18n_name: Optional[List[I18n]] = None
        self.avatar: Optional[Avatar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserWithAvatarBuilder":
        return UserWithAvatarBuilder()


class UserWithAvatarBuilder(object):
    def __init__(self) -> None:
        self._user_with_avatar = UserWithAvatar()

    def id(self, id: str) -> "UserWithAvatarBuilder":
        self._user_with_avatar.id = id
        return self

    def name(self, name: str) -> "UserWithAvatarBuilder":
        self._user_with_avatar.name = name
        return self

    def is_deleted(self, is_deleted: bool) -> "UserWithAvatarBuilder":
        self._user_with_avatar.is_deleted = is_deleted
        return self

    def i18n_name(self, i18n_name: List[I18n]) -> "UserWithAvatarBuilder":
        self._user_with_avatar.i18n_name = i18n_name
        return self

    def avatar(self, avatar: Avatar) -> "UserWithAvatarBuilder":
        self._user_with_avatar.avatar = avatar
        return self

    def build(self) -> "UserWithAvatar":
        return self._user_with_avatar
