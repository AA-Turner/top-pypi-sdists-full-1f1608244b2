from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetFlowByPathWithDraftResponse200DraftValueModulesItemSkipIf")


@_attrs_define
class GetFlowByPathWithDraftResponse200DraftValueModulesItemSkipIf:
    """
    Attributes:
        expr (str):
    """

    expr: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expr = self.expr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expr": expr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expr = d.pop("expr")

        get_flow_by_path_with_draft_response_200_draft_value_modules_item_skip_if = cls(
            expr=expr,
        )

        get_flow_by_path_with_draft_response_200_draft_value_modules_item_skip_if.additional_properties = d
        return get_flow_by_path_with_draft_response_200_draft_value_modules_item_skip_if

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
