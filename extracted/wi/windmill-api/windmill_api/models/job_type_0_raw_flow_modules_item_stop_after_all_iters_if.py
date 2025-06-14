from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobType0RawFlowModulesItemStopAfterAllItersIf")


@_attrs_define
class JobType0RawFlowModulesItemStopAfterAllItersIf:
    """
    Attributes:
        expr (str):
        skip_if_stopped (Union[Unset, bool]):
        error_message (Union[Unset, str]):
    """

    expr: str
    skip_if_stopped: Union[Unset, bool] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expr = self.expr
        skip_if_stopped = self.skip_if_stopped
        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expr": expr,
            }
        )
        if skip_if_stopped is not UNSET:
            field_dict["skip_if_stopped"] = skip_if_stopped
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expr = d.pop("expr")

        skip_if_stopped = d.pop("skip_if_stopped", UNSET)

        error_message = d.pop("error_message", UNSET)

        job_type_0_raw_flow_modules_item_stop_after_all_iters_if = cls(
            expr=expr,
            skip_if_stopped=skip_if_stopped,
            error_message=error_message,
        )

        job_type_0_raw_flow_modules_item_stop_after_all_iters_if.additional_properties = d
        return job_type_0_raw_flow_modules_item_stop_after_all_iters_if

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
