from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppHistoryJsonBody")


@_attrs_define
class UpdateAppHistoryJsonBody:
    """
    Attributes:
        deployment_msg (Union[Unset, str]):
    """

    deployment_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployment_msg = self.deployment_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_msg is not UNSET:
            field_dict["deployment_msg"] = deployment_msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deployment_msg = d.pop("deployment_msg", UNSET)

        update_app_history_json_body = cls(
            deployment_msg=deployment_msg,
        )

        update_app_history_json_body.additional_properties = d
        return update_app_history_json_body

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
