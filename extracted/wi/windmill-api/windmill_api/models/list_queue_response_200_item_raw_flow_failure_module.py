from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_queue_response_200_item_raw_flow_failure_module_mock import (
        ListQueueResponse200ItemRawFlowFailureModuleMock,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_retry import (
        ListQueueResponse200ItemRawFlowFailureModuleRetry,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_skip_if import (
        ListQueueResponse200ItemRawFlowFailureModuleSkipIf,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_sleep_type_0 import (
        ListQueueResponse200ItemRawFlowFailureModuleSleepType0,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_sleep_type_1 import (
        ListQueueResponse200ItemRawFlowFailureModuleSleepType1,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_stop_after_all_iters_if import (
        ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_stop_after_if import (
        ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf,
    )
    from ..models.list_queue_response_200_item_raw_flow_failure_module_suspend import (
        ListQueueResponse200ItemRawFlowFailureModuleSuspend,
    )


T = TypeVar("T", bound="ListQueueResponse200ItemRawFlowFailureModule")


@_attrs_define
class ListQueueResponse200ItemRawFlowFailureModule:
    """
    Attributes:
        id (str):
        value (Any):
        stop_after_if (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf]):
        stop_after_all_iters_if (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf]):
        skip_if (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSkipIf]):
        sleep (Union['ListQueueResponse200ItemRawFlowFailureModuleSleepType0',
            'ListQueueResponse200ItemRawFlowFailureModuleSleepType1', Unset]):
        cache_ttl (Union[Unset, float]):
        timeout (Union[Unset, float]):
        delete_after_use (Union[Unset, bool]):
        summary (Union[Unset, str]):
        mock (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleMock]):
        suspend (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSuspend]):
        priority (Union[Unset, float]):
        continue_on_error (Union[Unset, bool]):
        retry (Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleRetry]):
    """

    id: str
    value: Any
    stop_after_if: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf"] = UNSET
    stop_after_all_iters_if: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf"] = UNSET
    skip_if: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleSkipIf"] = UNSET
    sleep: Union[
        "ListQueueResponse200ItemRawFlowFailureModuleSleepType0",
        "ListQueueResponse200ItemRawFlowFailureModuleSleepType1",
        Unset,
    ] = UNSET
    cache_ttl: Union[Unset, float] = UNSET
    timeout: Union[Unset, float] = UNSET
    delete_after_use: Union[Unset, bool] = UNSET
    summary: Union[Unset, str] = UNSET
    mock: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleMock"] = UNSET
    suspend: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleSuspend"] = UNSET
    priority: Union[Unset, float] = UNSET
    continue_on_error: Union[Unset, bool] = UNSET
    retry: Union[Unset, "ListQueueResponse200ItemRawFlowFailureModuleRetry"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.list_queue_response_200_item_raw_flow_failure_module_sleep_type_0 import (
            ListQueueResponse200ItemRawFlowFailureModuleSleepType0,
        )

        id = self.id
        value = self.value
        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        stop_after_all_iters_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_all_iters_if, Unset):
            stop_after_all_iters_if = self.stop_after_all_iters_if.to_dict()

        skip_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skip_if, Unset):
            skip_if = self.skip_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET

        elif isinstance(self.sleep, ListQueueResponse200ItemRawFlowFailureModuleSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        cache_ttl = self.cache_ttl
        timeout = self.timeout
        delete_after_use = self.delete_after_use
        summary = self.summary
        mock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mock, Unset):
            mock = self.mock.to_dict()

        suspend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suspend, Unset):
            suspend = self.suspend.to_dict()

        priority = self.priority
        continue_on_error = self.continue_on_error
        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if stop_after_all_iters_if is not UNSET:
            field_dict["stop_after_all_iters_if"] = stop_after_all_iters_if
        if skip_if is not UNSET:
            field_dict["skip_if"] = skip_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if cache_ttl is not UNSET:
            field_dict["cache_ttl"] = cache_ttl
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if delete_after_use is not UNSET:
            field_dict["delete_after_use"] = delete_after_use
        if summary is not UNSET:
            field_dict["summary"] = summary
        if mock is not UNSET:
            field_dict["mock"] = mock
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if priority is not UNSET:
            field_dict["priority"] = priority
        if continue_on_error is not UNSET:
            field_dict["continue_on_error"] = continue_on_error
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_queue_response_200_item_raw_flow_failure_module_mock import (
            ListQueueResponse200ItemRawFlowFailureModuleMock,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_retry import (
            ListQueueResponse200ItemRawFlowFailureModuleRetry,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_skip_if import (
            ListQueueResponse200ItemRawFlowFailureModuleSkipIf,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_sleep_type_0 import (
            ListQueueResponse200ItemRawFlowFailureModuleSleepType0,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_sleep_type_1 import (
            ListQueueResponse200ItemRawFlowFailureModuleSleepType1,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_stop_after_all_iters_if import (
            ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_stop_after_if import (
            ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf,
        )
        from ..models.list_queue_response_200_item_raw_flow_failure_module_suspend import (
            ListQueueResponse200ItemRawFlowFailureModuleSuspend,
        )

        d = src_dict.copy()
        id = d.pop("id")

        value = d.pop("value")

        _stop_after_if = d.pop("stop_after_if", UNSET)
        stop_after_if: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf]
        if isinstance(_stop_after_if, Unset):
            stop_after_if = UNSET
        else:
            stop_after_if = ListQueueResponse200ItemRawFlowFailureModuleStopAfterIf.from_dict(_stop_after_if)

        _stop_after_all_iters_if = d.pop("stop_after_all_iters_if", UNSET)
        stop_after_all_iters_if: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf]
        if isinstance(_stop_after_all_iters_if, Unset):
            stop_after_all_iters_if = UNSET
        else:
            stop_after_all_iters_if = ListQueueResponse200ItemRawFlowFailureModuleStopAfterAllItersIf.from_dict(
                _stop_after_all_iters_if
            )

        _skip_if = d.pop("skip_if", UNSET)
        skip_if: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSkipIf]
        if isinstance(_skip_if, Unset):
            skip_if = UNSET
        else:
            skip_if = ListQueueResponse200ItemRawFlowFailureModuleSkipIf.from_dict(_skip_if)

        def _parse_sleep(
            data: object,
        ) -> Union[
            "ListQueueResponse200ItemRawFlowFailureModuleSleepType0",
            "ListQueueResponse200ItemRawFlowFailureModuleSleepType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sleep_type_0 = data
                sleep_type_0: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSleepType0]
                if isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = UNSET
                else:
                    sleep_type_0 = ListQueueResponse200ItemRawFlowFailureModuleSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _sleep_type_1 = data
            sleep_type_1: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSleepType1]
            if isinstance(_sleep_type_1, Unset):
                sleep_type_1 = UNSET
            else:
                sleep_type_1 = ListQueueResponse200ItemRawFlowFailureModuleSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        cache_ttl = d.pop("cache_ttl", UNSET)

        timeout = d.pop("timeout", UNSET)

        delete_after_use = d.pop("delete_after_use", UNSET)

        summary = d.pop("summary", UNSET)

        _mock = d.pop("mock", UNSET)
        mock: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleMock]
        if isinstance(_mock, Unset):
            mock = UNSET
        else:
            mock = ListQueueResponse200ItemRawFlowFailureModuleMock.from_dict(_mock)

        _suspend = d.pop("suspend", UNSET)
        suspend: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleSuspend]
        if isinstance(_suspend, Unset):
            suspend = UNSET
        else:
            suspend = ListQueueResponse200ItemRawFlowFailureModuleSuspend.from_dict(_suspend)

        priority = d.pop("priority", UNSET)

        continue_on_error = d.pop("continue_on_error", UNSET)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, ListQueueResponse200ItemRawFlowFailureModuleRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = ListQueueResponse200ItemRawFlowFailureModuleRetry.from_dict(_retry)

        list_queue_response_200_item_raw_flow_failure_module = cls(
            id=id,
            value=value,
            stop_after_if=stop_after_if,
            stop_after_all_iters_if=stop_after_all_iters_if,
            skip_if=skip_if,
            sleep=sleep,
            cache_ttl=cache_ttl,
            timeout=timeout,
            delete_after_use=delete_after_use,
            summary=summary,
            mock=mock,
            suspend=suspend,
            priority=priority,
            continue_on_error=continue_on_error,
            retry=retry,
        )

        list_queue_response_200_item_raw_flow_failure_module.additional_properties = d
        return list_queue_response_200_item_raw_flow_failure_module

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
