from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_websocket_trigger_json_body_initial_messages_item_type_1_runnable_result import (
        UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1RunnableResult,
    )


T = TypeVar("T", bound="UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1")


@_attrs_define
class UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1:
    """
    Attributes:
        runnable_result (UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1RunnableResult):
    """

    runnable_result: "UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1RunnableResult"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        runnable_result = self.runnable_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runnable_result": runnable_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_websocket_trigger_json_body_initial_messages_item_type_1_runnable_result import (
            UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1RunnableResult,
        )

        d = src_dict.copy()
        runnable_result = UpdateWebsocketTriggerJsonBodyInitialMessagesItemType1RunnableResult.from_dict(
            d.pop("runnable_result")
        )

        update_websocket_trigger_json_body_initial_messages_item_type_1 = cls(
            runnable_result=runnable_result,
        )

        update_websocket_trigger_json_body_initial_messages_item_type_1.additional_properties = d
        return update_websocket_trigger_json_body_initial_messages_item_type_1

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
