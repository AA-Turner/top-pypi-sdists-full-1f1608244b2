import datetime
from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..extensions import NotPresentError
from ..models.automation_file import AutomationFile
from ..models.automation_input_generator_completed_v2_beta_event_event_type import (
    AutomationInputGeneratorCompletedV2BetaEventEventType,
)
from ..models.event_base_schema import EventBaseSchema
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationInputGeneratorCompletedV2BetaEvent")


@attr.s(auto_attribs=True, repr=False)
class AutomationInputGeneratorCompletedV2BetaEvent:
    """  """

    _automation_input_generator: Union[Unset, AutomationFile] = UNSET
    _event_type: Union[Unset, AutomationInputGeneratorCompletedV2BetaEventEventType] = UNSET
    _created_at: Union[Unset, datetime.datetime] = UNSET
    _deprecated: Union[Unset, bool] = UNSET
    _excluded_properties: Union[Unset, List[str]] = UNSET
    _id: Union[Unset, str] = UNSET
    _schema: Union[Unset, None, EventBaseSchema] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("automation_input_generator={}".format(repr(self._automation_input_generator)))
        fields.append("event_type={}".format(repr(self._event_type)))
        fields.append("created_at={}".format(repr(self._created_at)))
        fields.append("deprecated={}".format(repr(self._deprecated)))
        fields.append("excluded_properties={}".format(repr(self._excluded_properties)))
        fields.append("id={}".format(repr(self._id)))
        fields.append("schema={}".format(repr(self._schema)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "AutomationInputGeneratorCompletedV2BetaEvent({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        automation_input_generator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._automation_input_generator, Unset):
            automation_input_generator = self._automation_input_generator.to_dict()

        event_type: Union[Unset, int] = UNSET
        if not isinstance(self._event_type, Unset):
            event_type = self._event_type.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self._created_at, Unset):
            created_at = self._created_at.isoformat()

        deprecated = self._deprecated
        excluded_properties: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._excluded_properties, Unset):
            excluded_properties = self._excluded_properties

        id = self._id
        schema: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self._schema, Unset):
            schema = self._schema.to_dict() if self._schema else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if automation_input_generator is not UNSET:
            field_dict["automationInputGenerator"] = automation_input_generator
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if excluded_properties is not UNSET:
            field_dict["excludedProperties"] = excluded_properties
        if id is not UNSET:
            field_dict["id"] = id
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_automation_input_generator() -> Union[Unset, AutomationFile]:
            automation_input_generator: Union[Unset, Union[Unset, AutomationFile]] = UNSET
            _automation_input_generator = d.pop("automationInputGenerator")

            if not isinstance(_automation_input_generator, Unset):
                automation_input_generator = AutomationFile.from_dict(_automation_input_generator)

            return automation_input_generator

        try:
            automation_input_generator = get_automation_input_generator()
        except KeyError:
            if strict:
                raise
            automation_input_generator = cast(Union[Unset, AutomationFile], UNSET)

        def get_event_type() -> Union[Unset, AutomationInputGeneratorCompletedV2BetaEventEventType]:
            event_type = UNSET
            _event_type = d.pop("eventType")
            if _event_type is not None and _event_type is not UNSET:
                try:
                    event_type = AutomationInputGeneratorCompletedV2BetaEventEventType(_event_type)
                except ValueError:
                    event_type = AutomationInputGeneratorCompletedV2BetaEventEventType.of_unknown(_event_type)

            return event_type

        try:
            event_type = get_event_type()
        except KeyError:
            if strict:
                raise
            event_type = cast(Union[Unset, AutomationInputGeneratorCompletedV2BetaEventEventType], UNSET)

        def get_created_at() -> Union[Unset, datetime.datetime]:
            created_at: Union[Unset, datetime.datetime] = UNSET
            _created_at = d.pop("createdAt")
            if _created_at is not None and not isinstance(_created_at, Unset):
                created_at = isoparse(cast(str, _created_at))

            return created_at

        try:
            created_at = get_created_at()
        except KeyError:
            if strict:
                raise
            created_at = cast(Union[Unset, datetime.datetime], UNSET)

        def get_deprecated() -> Union[Unset, bool]:
            deprecated = d.pop("deprecated")
            return deprecated

        try:
            deprecated = get_deprecated()
        except KeyError:
            if strict:
                raise
            deprecated = cast(Union[Unset, bool], UNSET)

        def get_excluded_properties() -> Union[Unset, List[str]]:
            excluded_properties = cast(List[str], d.pop("excludedProperties"))

            return excluded_properties

        try:
            excluded_properties = get_excluded_properties()
        except KeyError:
            if strict:
                raise
            excluded_properties = cast(Union[Unset, List[str]], UNSET)

        def get_id() -> Union[Unset, str]:
            id = d.pop("id")
            return id

        try:
            id = get_id()
        except KeyError:
            if strict:
                raise
            id = cast(Union[Unset, str], UNSET)

        def get_schema() -> Union[Unset, None, EventBaseSchema]:
            schema = None
            _schema = d.pop("schema")

            if _schema is not None and not isinstance(_schema, Unset):
                schema = EventBaseSchema.from_dict(_schema)

            return schema

        try:
            schema = get_schema()
        except KeyError:
            if strict:
                raise
            schema = cast(Union[Unset, None, EventBaseSchema], UNSET)

        automation_input_generator_completed_v2_beta_event = cls(
            automation_input_generator=automation_input_generator,
            event_type=event_type,
            created_at=created_at,
            deprecated=deprecated,
            excluded_properties=excluded_properties,
            id=id,
            schema=schema,
        )

        automation_input_generator_completed_v2_beta_event.additional_properties = d
        return automation_input_generator_completed_v2_beta_event

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
    def automation_input_generator(self) -> AutomationFile:
        if isinstance(self._automation_input_generator, Unset):
            raise NotPresentError(self, "automation_input_generator")
        return self._automation_input_generator

    @automation_input_generator.setter
    def automation_input_generator(self, value: AutomationFile) -> None:
        self._automation_input_generator = value

    @automation_input_generator.deleter
    def automation_input_generator(self) -> None:
        self._automation_input_generator = UNSET

    @property
    def event_type(self) -> AutomationInputGeneratorCompletedV2BetaEventEventType:
        if isinstance(self._event_type, Unset):
            raise NotPresentError(self, "event_type")
        return self._event_type

    @event_type.setter
    def event_type(self, value: AutomationInputGeneratorCompletedV2BetaEventEventType) -> None:
        self._event_type = value

    @event_type.deleter
    def event_type(self) -> None:
        self._event_type = UNSET

    @property
    def created_at(self) -> datetime.datetime:
        if isinstance(self._created_at, Unset):
            raise NotPresentError(self, "created_at")
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime.datetime) -> None:
        self._created_at = value

    @created_at.deleter
    def created_at(self) -> None:
        self._created_at = UNSET

    @property
    def deprecated(self) -> bool:
        if isinstance(self._deprecated, Unset):
            raise NotPresentError(self, "deprecated")
        return self._deprecated

    @deprecated.setter
    def deprecated(self, value: bool) -> None:
        self._deprecated = value

    @deprecated.deleter
    def deprecated(self) -> None:
        self._deprecated = UNSET

    @property
    def excluded_properties(self) -> List[str]:
        """These properties have been dropped from the payload due to size."""
        if isinstance(self._excluded_properties, Unset):
            raise NotPresentError(self, "excluded_properties")
        return self._excluded_properties

    @excluded_properties.setter
    def excluded_properties(self, value: List[str]) -> None:
        self._excluded_properties = value

    @excluded_properties.deleter
    def excluded_properties(self) -> None:
        self._excluded_properties = UNSET

    @property
    def id(self) -> str:
        if isinstance(self._id, Unset):
            raise NotPresentError(self, "id")
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @id.deleter
    def id(self) -> None:
        self._id = UNSET

    @property
    def schema(self) -> Optional[EventBaseSchema]:
        if isinstance(self._schema, Unset):
            raise NotPresentError(self, "schema")
        return self._schema

    @schema.setter
    def schema(self, value: Optional[EventBaseSchema]) -> None:
        self._schema = value

    @schema.deleter
    def schema(self) -> None:
        self._schema = UNSET
