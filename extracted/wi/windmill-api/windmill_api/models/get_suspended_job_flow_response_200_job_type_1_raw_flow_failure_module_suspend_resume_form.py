from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_suspended_job_flow_response_200_job_type_1_raw_flow_failure_module_suspend_resume_form_schema import (
        GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema,
    )


T = TypeVar("T", bound="GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeForm")


@_attrs_define
class GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeForm:
    """
    Attributes:
        schema (Union[Unset, GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema]):
    """

    schema: Union[Unset, "GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_suspended_job_flow_response_200_job_type_1_raw_flow_failure_module_suspend_resume_form_schema import (
            GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema,
        )

        d = src_dict.copy()
        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = GetSuspendedJobFlowResponse200JobType1RawFlowFailureModuleSuspendResumeFormSchema.from_dict(
                _schema
            )

        get_suspended_job_flow_response_200_job_type_1_raw_flow_failure_module_suspend_resume_form = cls(
            schema=schema,
        )

        get_suspended_job_flow_response_200_job_type_1_raw_flow_failure_module_suspend_resume_form.additional_properties = (
            d
        )
        return get_suspended_job_flow_response_200_job_type_1_raw_flow_failure_module_suspend_resume_form

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
