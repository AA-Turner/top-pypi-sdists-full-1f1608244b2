from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTeamsCommandJsonBody")


@_attrs_define
class EditTeamsCommandJsonBody:
    """
    Attributes:
        slack_command_script (Union[Unset, str]):
    """

    slack_command_script: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slack_command_script = self.slack_command_script

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slack_command_script is not UNSET:
            field_dict["slack_command_script"] = slack_command_script

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slack_command_script = d.pop("slack_command_script", UNSET)

        edit_teams_command_json_body = cls(
            slack_command_script=slack_command_script,
        )

        edit_teams_command_json_body.additional_properties = d
        return edit_teams_command_json_body

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
