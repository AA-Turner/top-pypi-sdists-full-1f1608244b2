from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditWorkspaceDefaultAppJsonBody")


@_attrs_define
class EditWorkspaceDefaultAppJsonBody:
    """
    Attributes:
        default_app_path (Union[Unset, str]):
    """

    default_app_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_app_path = self.default_app_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_app_path is not UNSET:
            field_dict["default_app_path"] = default_app_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_app_path = d.pop("default_app_path", UNSET)

        edit_workspace_default_app_json_body = cls(
            default_app_path=default_app_path,
        )

        edit_workspace_default_app_json_body.additional_properties = d
        return edit_workspace_default_app_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
