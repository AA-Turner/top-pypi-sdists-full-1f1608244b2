# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BlockRole(object):
    _types = {
        "block_id": str,
        "block_perm": int,
        "block_type": str,
    }

    def __init__(self, d=None):
        self.block_id: Optional[str] = None
        self.block_perm: Optional[int] = None
        self.block_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BlockRoleBuilder":
        return BlockRoleBuilder()


class BlockRoleBuilder(object):
    def __init__(self) -> None:
        self._block_role = BlockRole()

    def block_id(self, block_id: str) -> "BlockRoleBuilder":
        self._block_role.block_id = block_id
        return self

    def block_perm(self, block_perm: int) -> "BlockRoleBuilder":
        self._block_role.block_perm = block_perm
        return self

    def block_type(self, block_type: str) -> "BlockRoleBuilder":
        self._block_role.block_type = block_type
        return self

    def build(self) -> "BlockRole":
        return self._block_role
