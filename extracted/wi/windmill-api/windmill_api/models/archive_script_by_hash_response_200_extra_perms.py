from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ArchiveScriptByHashResponse200ExtraPerms")


@_attrs_define
class ArchiveScriptByHashResponse200ExtraPerms:
    """ """

    additional_properties: Dict[str, bool] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archive_script_by_hash_response_200_extra_perms = cls()

        archive_script_by_hash_response_200_extra_perms.additional_properties = d
        return archive_script_by_hash_response_200_extra_perms

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
