# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class StandardReferenceObject(object):
    _types = {
        "id": str,
        "api_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.api_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StandardReferenceObjectBuilder":
        return StandardReferenceObjectBuilder()


class StandardReferenceObjectBuilder(object):
    def __init__(self) -> None:
        self._standard_reference_object = StandardReferenceObject()

    def id(self, id: str) -> "StandardReferenceObjectBuilder":
        self._standard_reference_object.id = id
        return self

    def api_name(self, api_name: str) -> "StandardReferenceObjectBuilder":
        self._standard_reference_object.api_name = api_name
        return self

    def build(self) -> "StandardReferenceObject":
        return self._standard_reference_object
