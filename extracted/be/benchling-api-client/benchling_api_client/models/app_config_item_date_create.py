import datetime
from typing import Any, cast, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..extensions import NotPresentError
from ..models.app_config_item_date_create_type import AppConfigItemDateCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppConfigItemDateCreate")


@attr.s(auto_attribs=True, repr=False)
class AppConfigItemDateCreate:
    """  """

    _type: AppConfigItemDateCreateType
    _app_id: str
    _path: List[str]
    _value: Optional[datetime.date]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("type={}".format(repr(self._type)))
        fields.append("app_id={}".format(repr(self._app_id)))
        fields.append("path={}".format(repr(self._path)))
        fields.append("value={}".format(repr(self._value)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "AppConfigItemDateCreate({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        type = self._type.value

        app_id = self._app_id
        path = self._path

        value = self._value.isoformat() if self._value else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if type is not UNSET:
            field_dict["type"] = type
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_type() -> AppConfigItemDateCreateType:
            _type = d.pop("type")
            try:
                type = AppConfigItemDateCreateType(_type)
            except ValueError:
                type = AppConfigItemDateCreateType.of_unknown(_type)

            return type

        try:
            type = get_type()
        except KeyError:
            if strict:
                raise
            type = cast(AppConfigItemDateCreateType, UNSET)

        def get_app_id() -> str:
            app_id = d.pop("appId")
            return app_id

        try:
            app_id = get_app_id()
        except KeyError:
            if strict:
                raise
            app_id = cast(str, UNSET)

        def get_path() -> List[str]:
            path = cast(List[str], d.pop("path"))

            return path

        try:
            path = get_path()
        except KeyError:
            if strict:
                raise
            path = cast(List[str], UNSET)

        def get_value() -> Optional[datetime.date]:
            value: Optional[datetime.date] = None
            _value = d.pop("value")
            if _value is not None and not isinstance(_value, Unset):
                value = isoparse(cast(str, _value)).date()

            return value

        try:
            value = get_value()
        except KeyError:
            if strict:
                raise
            value = cast(Optional[datetime.date], UNSET)

        app_config_item_date_create = cls(
            type=type,
            app_id=app_id,
            path=path,
            value=value,
        )

        app_config_item_date_create.additional_properties = d
        return app_config_item_date_create

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
    def type(self) -> AppConfigItemDateCreateType:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: AppConfigItemDateCreateType) -> None:
        self._type = value

    @property
    def app_id(self) -> str:
        """ App id to which this config item belongs. """
        if isinstance(self._app_id, Unset):
            raise NotPresentError(self, "app_id")
        return self._app_id

    @app_id.setter
    def app_id(self, value: str) -> None:
        self._app_id = value

    @property
    def path(self) -> List[str]:
        """ Array-based representation of config item's location in the tree in order from top to bottom. """
        if isinstance(self._path, Unset):
            raise NotPresentError(self, "path")
        return self._path

    @path.setter
    def path(self, value: List[str]) -> None:
        self._path = value

    @property
    def value(self) -> Optional[datetime.date]:
        if isinstance(self._value, Unset):
            raise NotPresentError(self, "value")
        return self._value

    @value.setter
    def value(self, value: Optional[datetime.date]) -> None:
        self._value = value
