from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windmill_file_preview_content_type import WindmillFilePreviewContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindmillFilePreview")


@_attrs_define
class WindmillFilePreview:
    """
    Attributes:
        content_type (WindmillFilePreviewContentType):
        msg (Union[Unset, str]):
        content (Union[Unset, str]):
    """

    content_type: WindmillFilePreviewContentType
    msg: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type.value

        msg = self.msg
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
            }
        )
        if msg is not UNSET:
            field_dict["msg"] = msg
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = WindmillFilePreviewContentType(d.pop("content_type"))

        msg = d.pop("msg", UNSET)

        content = d.pop("content", UNSET)

        windmill_file_preview = cls(
            content_type=content_type,
            msg=msg,
            content=content,
        )

        windmill_file_preview.additional_properties = d
        return windmill_file_preview

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
