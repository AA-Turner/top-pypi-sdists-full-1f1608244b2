from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_failure_module import (
        GetSuspendedJobFlowResponse200JobType0FlowStatusFailureModule,
    )
    from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_modules_item import (
        GetSuspendedJobFlowResponse200JobType0FlowStatusModulesItem,
    )
    from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_preprocessor_module import (
        GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule,
    )
    from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_retry import (
        GetSuspendedJobFlowResponse200JobType0FlowStatusRetry,
    )


T = TypeVar("T", bound="GetSuspendedJobFlowResponse200JobType0FlowStatus")


@_attrs_define
class GetSuspendedJobFlowResponse200JobType0FlowStatus:
    """
    Attributes:
        step (int):
        modules (List['GetSuspendedJobFlowResponse200JobType0FlowStatusModulesItem']):
        failure_module (GetSuspendedJobFlowResponse200JobType0FlowStatusFailureModule):
        user_states (Union[Unset, Any]):
        preprocessor_module (Union[Unset, GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule]):
        retry (Union[Unset, GetSuspendedJobFlowResponse200JobType0FlowStatusRetry]):
    """

    step: int
    modules: List["GetSuspendedJobFlowResponse200JobType0FlowStatusModulesItem"]
    failure_module: "GetSuspendedJobFlowResponse200JobType0FlowStatusFailureModule"
    user_states: Union[Unset, Any] = UNSET
    preprocessor_module: Union[Unset, "GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule"] = UNSET
    retry: Union[Unset, "GetSuspendedJobFlowResponse200JobType0FlowStatusRetry"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step = self.step
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        failure_module = self.failure_module.to_dict()

        user_states = self.user_states
        preprocessor_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessor_module, Unset):
            preprocessor_module = self.preprocessor_module.to_dict()

        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "modules": modules,
                "failure_module": failure_module,
            }
        )
        if user_states is not UNSET:
            field_dict["user_states"] = user_states
        if preprocessor_module is not UNSET:
            field_dict["preprocessor_module"] = preprocessor_module
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_failure_module import (
            GetSuspendedJobFlowResponse200JobType0FlowStatusFailureModule,
        )
        from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_modules_item import (
            GetSuspendedJobFlowResponse200JobType0FlowStatusModulesItem,
        )
        from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_preprocessor_module import (
            GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule,
        )
        from ..models.get_suspended_job_flow_response_200_job_type_0_flow_status_retry import (
            GetSuspendedJobFlowResponse200JobType0FlowStatusRetry,
        )

        d = src_dict.copy()
        step = d.pop("step")

        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = GetSuspendedJobFlowResponse200JobType0FlowStatusModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        failure_module = GetSuspendedJobFlowResponse200JobType0FlowStatusFailureModule.from_dict(
            d.pop("failure_module")
        )

        user_states = d.pop("user_states", UNSET)

        _preprocessor_module = d.pop("preprocessor_module", UNSET)
        preprocessor_module: Union[Unset, GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule]
        if isinstance(_preprocessor_module, Unset):
            preprocessor_module = UNSET
        else:
            preprocessor_module = GetSuspendedJobFlowResponse200JobType0FlowStatusPreprocessorModule.from_dict(
                _preprocessor_module
            )

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, GetSuspendedJobFlowResponse200JobType0FlowStatusRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = GetSuspendedJobFlowResponse200JobType0FlowStatusRetry.from_dict(_retry)

        get_suspended_job_flow_response_200_job_type_0_flow_status = cls(
            step=step,
            modules=modules,
            failure_module=failure_module,
            user_states=user_states,
            preprocessor_module=preprocessor_module,
            retry=retry,
        )

        get_suspended_job_flow_response_200_job_type_0_flow_status.additional_properties = d
        return get_suspended_job_flow_response_200_job_type_0_flow_status

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
