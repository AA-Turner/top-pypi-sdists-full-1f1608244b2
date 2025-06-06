from typing import Any, cast, Dict, List, Type, TypeVar

import attr

from ..extensions import NotPresentError
from ..models.custom_entity_bulk_upsert_request import CustomEntityBulkUpsertRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomEntitiesBulkUpsertRequest")


@attr.s(auto_attribs=True, repr=False)
class CustomEntitiesBulkUpsertRequest:
    """  """

    _custom_entities: List[CustomEntityBulkUpsertRequest]

    def __repr__(self):
        fields = []
        fields.append("custom_entities={}".format(repr(self._custom_entities)))
        return "CustomEntitiesBulkUpsertRequest({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        custom_entities = []
        for custom_entities_item_data in self._custom_entities:
            custom_entities_item = custom_entities_item_data.to_dict()

            custom_entities.append(custom_entities_item)

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if custom_entities is not UNSET:
            field_dict["customEntities"] = custom_entities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_custom_entities() -> List[CustomEntityBulkUpsertRequest]:
            custom_entities = []
            _custom_entities = d.pop("customEntities")
            for custom_entities_item_data in _custom_entities:
                custom_entities_item = CustomEntityBulkUpsertRequest.from_dict(
                    custom_entities_item_data, strict=False
                )

                custom_entities.append(custom_entities_item)

            return custom_entities

        try:
            custom_entities = get_custom_entities()
        except KeyError:
            if strict:
                raise
            custom_entities = cast(List[CustomEntityBulkUpsertRequest], UNSET)

        custom_entities_bulk_upsert_request = cls(
            custom_entities=custom_entities,
        )

        return custom_entities_bulk_upsert_request

    @property
    def custom_entities(self) -> List[CustomEntityBulkUpsertRequest]:
        if isinstance(self._custom_entities, Unset):
            raise NotPresentError(self, "custom_entities")
        return self._custom_entities

    @custom_entities.setter
    def custom_entities(self, value: List[CustomEntityBulkUpsertRequest]) -> None:
        self._custom_entities = value
