from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_app_raw_multipart_data_app_policy_triggerables_additional_property import (
        UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty,
    )


T = TypeVar("T", bound="UpdateAppRawMultipartDataAppPolicyTriggerables")


@_attrs_define
class UpdateAppRawMultipartDataAppPolicyTriggerables:
    """ """

    additional_properties: Dict[str, "UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_app_raw_multipart_data_app_policy_triggerables_additional_property import (
            UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty,
        )

        d = src_dict.copy()
        update_app_raw_multipart_data_app_policy_triggerables = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        update_app_raw_multipart_data_app_policy_triggerables.additional_properties = additional_properties
        return update_app_raw_multipart_data_app_policy_triggerables

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "UpdateAppRawMultipartDataAppPolicyTriggerablesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
