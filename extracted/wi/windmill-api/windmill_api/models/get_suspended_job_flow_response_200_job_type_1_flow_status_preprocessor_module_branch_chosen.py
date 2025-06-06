from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_suspended_job_flow_response_200_job_type_1_flow_status_preprocessor_module_branch_chosen_type import (
    GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosenType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosen")


@_attrs_define
class GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosen:
    """
    Attributes:
        type (GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosenType):
        branch (Union[Unset, int]):
    """

    type: GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosenType
    branch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        branch = self.branch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = GetSuspendedJobFlowResponse200JobType1FlowStatusPreprocessorModuleBranchChosenType(d.pop("type"))

        branch = d.pop("branch", UNSET)

        get_suspended_job_flow_response_200_job_type_1_flow_status_preprocessor_module_branch_chosen = cls(
            type=type,
            branch=branch,
        )

        get_suspended_job_flow_response_200_job_type_1_flow_status_preprocessor_module_branch_chosen.additional_properties = (
            d
        )
        return get_suspended_job_flow_response_200_job_type_1_flow_status_preprocessor_module_branch_chosen

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
