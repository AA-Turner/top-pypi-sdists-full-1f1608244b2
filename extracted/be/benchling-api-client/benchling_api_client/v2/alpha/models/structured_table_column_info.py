from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..types import UNSET, Unset

T = TypeVar("T", bound="StructuredTableColumnInfo")


@attr.s(auto_attribs=True, repr=False)
class StructuredTableColumnInfo:
    """  """

    _column_id: Union[Unset, str] = UNSET
    _is_read_only: Union[Unset, bool] = UNSET
    _name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("column_id={}".format(repr(self._column_id)))
        fields.append("is_read_only={}".format(repr(self._is_read_only)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "StructuredTableColumnInfo({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        column_id = self._column_id
        is_read_only = self._is_read_only
        name = self._name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if column_id is not UNSET:
            field_dict["columnId"] = column_id
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_column_id() -> Union[Unset, str]:
            column_id = d.pop("columnId")
            return column_id

        try:
            column_id = get_column_id()
        except KeyError:
            if strict:
                raise
            column_id = cast(Union[Unset, str], UNSET)

        def get_is_read_only() -> Union[Unset, bool]:
            is_read_only = d.pop("isReadOnly")
            return is_read_only

        try:
            is_read_only = get_is_read_only()
        except KeyError:
            if strict:
                raise
            is_read_only = cast(Union[Unset, bool], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        try:
            name = get_name()
        except KeyError:
            if strict:
                raise
            name = cast(Union[Unset, str], UNSET)

        structured_table_column_info = cls(
            column_id=column_id,
            is_read_only=is_read_only,
            name=name,
        )

        structured_table_column_info.additional_properties = d
        return structured_table_column_info

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

    def get(self, key, default=None) -> Optional[Any]:
        return self.additional_properties.get(key, default)

    @property
    def column_id(self) -> str:
        if isinstance(self._column_id, Unset):
            raise NotPresentError(self, "column_id")
        return self._column_id

    @column_id.setter
    def column_id(self, value: str) -> None:
        self._column_id = value

    @column_id.deleter
    def column_id(self) -> None:
        self._column_id = UNSET

    @property
    def is_read_only(self) -> bool:
        if isinstance(self._is_read_only, Unset):
            raise NotPresentError(self, "is_read_only")
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, value: bool) -> None:
        self._is_read_only = value

    @is_read_only.deleter
    def is_read_only(self) -> None:
        self._is_read_only = UNSET

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET
