from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListJobsResponse200ItemType1FlowStatusModulesItemApproversItem")


@_attrs_define
class ListJobsResponse200ItemType1FlowStatusModulesItemApproversItem:
    """
    Attributes:
        resume_id (int):
        approver (str):
    """

    resume_id: int
    approver: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resume_id = self.resume_id
        approver = self.approver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resume_id": resume_id,
                "approver": approver,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resume_id = d.pop("resume_id")

        approver = d.pop("approver")

        list_jobs_response_200_item_type_1_flow_status_modules_item_approvers_item = cls(
            resume_id=resume_id,
            approver=approver,
        )

        list_jobs_response_200_item_type_1_flow_status_modules_item_approvers_item.additional_properties = d
        return list_jobs_response_200_item_type_1_flow_status_modules_item_approvers_item

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
