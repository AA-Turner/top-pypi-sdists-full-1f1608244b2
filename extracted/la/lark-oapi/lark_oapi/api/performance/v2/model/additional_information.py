# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AdditionalInformation(object):
    _types = {
        "item_id": int,
        "external_id": str,
        "reviewee_user_id": str,
        "item": str,
        "time": str,
        "detailed_description": str,
    }

    def __init__(self, d=None):
        self.item_id: Optional[int] = None
        self.external_id: Optional[str] = None
        self.reviewee_user_id: Optional[str] = None
        self.item: Optional[str] = None
        self.time: Optional[str] = None
        self.detailed_description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AdditionalInformationBuilder":
        return AdditionalInformationBuilder()


class AdditionalInformationBuilder(object):
    def __init__(self) -> None:
        self._additional_information = AdditionalInformation()

    def item_id(self, item_id: int) -> "AdditionalInformationBuilder":
        self._additional_information.item_id = item_id
        return self

    def external_id(self, external_id: str) -> "AdditionalInformationBuilder":
        self._additional_information.external_id = external_id
        return self

    def reviewee_user_id(self, reviewee_user_id: str) -> "AdditionalInformationBuilder":
        self._additional_information.reviewee_user_id = reviewee_user_id
        return self

    def item(self, item: str) -> "AdditionalInformationBuilder":
        self._additional_information.item = item
        return self

    def time(self, time: str) -> "AdditionalInformationBuilder":
        self._additional_information.time = time
        return self

    def detailed_description(self, detailed_description: str) -> "AdditionalInformationBuilder":
        self._additional_information.detailed_description = detailed_description
        return self

    def build(self) -> "AdditionalInformation":
        return self._additional_information
