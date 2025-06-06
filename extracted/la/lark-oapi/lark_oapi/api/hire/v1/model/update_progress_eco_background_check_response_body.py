# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UpdateProgressEcoBackgroundCheckResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProgressEcoBackgroundCheckResponseBodyBuilder":
        return UpdateProgressEcoBackgroundCheckResponseBodyBuilder()


class UpdateProgressEcoBackgroundCheckResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_progress_eco_background_check_response_body = UpdateProgressEcoBackgroundCheckResponseBody()

    def build(self) -> "UpdateProgressEcoBackgroundCheckResponseBody":
        return self._update_progress_eco_background_check_response_body
