# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .additional_information import AdditionalInformation


class ImportAdditionalInformationResponseBody(object):
    _types = {
        "import_record_id": str,
        "additional_informations": List[AdditionalInformation],
    }

    def __init__(self, d=None):
        self.import_record_id: Optional[str] = None
        self.additional_informations: Optional[List[AdditionalInformation]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImportAdditionalInformationResponseBodyBuilder":
        return ImportAdditionalInformationResponseBodyBuilder()


class ImportAdditionalInformationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._import_additional_information_response_body = ImportAdditionalInformationResponseBody()

    def import_record_id(self, import_record_id: str) -> "ImportAdditionalInformationResponseBodyBuilder":
        self._import_additional_information_response_body.import_record_id = import_record_id
        return self

    def additional_informations(self, additional_informations: List[
        AdditionalInformation]) -> "ImportAdditionalInformationResponseBodyBuilder":
        self._import_additional_information_response_body.additional_informations = additional_informations
        return self

    def build(self) -> "ImportAdditionalInformationResponseBody":
        return self._import_additional_information_response_body
