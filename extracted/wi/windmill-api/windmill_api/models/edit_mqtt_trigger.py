from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_mqtt_trigger_client_version import EditMqttTriggerClientVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_mqtt_trigger_subscribe_topics_item import EditMqttTriggerSubscribeTopicsItem
    from ..models.edit_mqtt_trigger_v3_config import EditMqttTriggerV3Config
    from ..models.edit_mqtt_trigger_v5_config import EditMqttTriggerV5Config


T = TypeVar("T", bound="EditMqttTrigger")


@_attrs_define
class EditMqttTrigger:
    """
    Attributes:
        mqtt_resource_path (str):
        subscribe_topics (List['EditMqttTriggerSubscribeTopicsItem']):
        path (str):
        script_path (str):
        is_flow (bool):
        enabled (bool):
        client_id (Union[Unset, str]):
        v3_config (Union[Unset, EditMqttTriggerV3Config]):
        v5_config (Union[Unset, EditMqttTriggerV5Config]):
        client_version (Union[Unset, EditMqttTriggerClientVersion]):
    """

    mqtt_resource_path: str
    subscribe_topics: List["EditMqttTriggerSubscribeTopicsItem"]
    path: str
    script_path: str
    is_flow: bool
    enabled: bool
    client_id: Union[Unset, str] = UNSET
    v3_config: Union[Unset, "EditMqttTriggerV3Config"] = UNSET
    v5_config: Union[Unset, "EditMqttTriggerV5Config"] = UNSET
    client_version: Union[Unset, EditMqttTriggerClientVersion] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mqtt_resource_path = self.mqtt_resource_path
        subscribe_topics = []
        for subscribe_topics_item_data in self.subscribe_topics:
            subscribe_topics_item = subscribe_topics_item_data.to_dict()

            subscribe_topics.append(subscribe_topics_item)

        path = self.path
        script_path = self.script_path
        is_flow = self.is_flow
        enabled = self.enabled
        client_id = self.client_id
        v3_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.v3_config, Unset):
            v3_config = self.v3_config.to_dict()

        v5_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.v5_config, Unset):
            v5_config = self.v5_config.to_dict()

        client_version: Union[Unset, str] = UNSET
        if not isinstance(self.client_version, Unset):
            client_version = self.client_version.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mqtt_resource_path": mqtt_resource_path,
                "subscribe_topics": subscribe_topics,
                "path": path,
                "script_path": script_path,
                "is_flow": is_flow,
                "enabled": enabled,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if v3_config is not UNSET:
            field_dict["v3_config"] = v3_config
        if v5_config is not UNSET:
            field_dict["v5_config"] = v5_config
        if client_version is not UNSET:
            field_dict["client_version"] = client_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edit_mqtt_trigger_subscribe_topics_item import EditMqttTriggerSubscribeTopicsItem
        from ..models.edit_mqtt_trigger_v3_config import EditMqttTriggerV3Config
        from ..models.edit_mqtt_trigger_v5_config import EditMqttTriggerV5Config

        d = src_dict.copy()
        mqtt_resource_path = d.pop("mqtt_resource_path")

        subscribe_topics = []
        _subscribe_topics = d.pop("subscribe_topics")
        for subscribe_topics_item_data in _subscribe_topics:
            subscribe_topics_item = EditMqttTriggerSubscribeTopicsItem.from_dict(subscribe_topics_item_data)

            subscribe_topics.append(subscribe_topics_item)

        path = d.pop("path")

        script_path = d.pop("script_path")

        is_flow = d.pop("is_flow")

        enabled = d.pop("enabled")

        client_id = d.pop("client_id", UNSET)

        _v3_config = d.pop("v3_config", UNSET)
        v3_config: Union[Unset, EditMqttTriggerV3Config]
        if isinstance(_v3_config, Unset):
            v3_config = UNSET
        else:
            v3_config = EditMqttTriggerV3Config.from_dict(_v3_config)

        _v5_config = d.pop("v5_config", UNSET)
        v5_config: Union[Unset, EditMqttTriggerV5Config]
        if isinstance(_v5_config, Unset):
            v5_config = UNSET
        else:
            v5_config = EditMqttTriggerV5Config.from_dict(_v5_config)

        _client_version = d.pop("client_version", UNSET)
        client_version: Union[Unset, EditMqttTriggerClientVersion]
        if isinstance(_client_version, Unset):
            client_version = UNSET
        else:
            client_version = EditMqttTriggerClientVersion(_client_version)

        edit_mqtt_trigger = cls(
            mqtt_resource_path=mqtt_resource_path,
            subscribe_topics=subscribe_topics,
            path=path,
            script_path=script_path,
            is_flow=is_flow,
            enabled=enabled,
            client_id=client_id,
            v3_config=v3_config,
            v5_config=v5_config,
            client_version=client_version,
        )

        edit_mqtt_trigger.additional_properties = d
        return edit_mqtt_trigger

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
