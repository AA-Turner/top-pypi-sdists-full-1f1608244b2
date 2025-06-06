from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.container_quantity import ContainerQuantity
from ..models.deprecated_container_volume_for_input import DeprecatedContainerVolumeForInput
from ..models.experimental_well_role import ExperimentalWellRole
from ..models.fields import Fields
from ..models.sample_restriction_status import SampleRestrictionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerUpdate")


@attr.s(auto_attribs=True, repr=False)
class ContainerUpdate:
    """  """

    _barcode: Union[Unset, str] = UNSET
    _project_id: Union[Unset, None, str] = UNSET
    _quantity: Union[Unset, ContainerQuantity] = UNSET
    _role: Union[Unset, None, ExperimentalWellRole] = UNSET
    _volume: Union[Unset, DeprecatedContainerVolumeForInput] = UNSET
    _fields: Union[Unset, Fields] = UNSET
    _name: Union[Unset, str] = UNSET
    _parent_storage_id: Union[Unset, str] = UNSET
    _restricted_sample_party_ids: Union[Unset, List[str]] = UNSET
    _restriction_status: Union[Unset, SampleRestrictionStatus] = UNSET
    _sample_owner_ids: Union[Unset, List[str]] = UNSET

    def __repr__(self):
        fields = []
        fields.append("barcode={}".format(repr(self._barcode)))
        fields.append("project_id={}".format(repr(self._project_id)))
        fields.append("quantity={}".format(repr(self._quantity)))
        fields.append("role={}".format(repr(self._role)))
        fields.append("volume={}".format(repr(self._volume)))
        fields.append("fields={}".format(repr(self._fields)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("parent_storage_id={}".format(repr(self._parent_storage_id)))
        fields.append("restricted_sample_party_ids={}".format(repr(self._restricted_sample_party_ids)))
        fields.append("restriction_status={}".format(repr(self._restriction_status)))
        fields.append("sample_owner_ids={}".format(repr(self._sample_owner_ids)))
        return "ContainerUpdate({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        barcode = self._barcode
        project_id = self._project_id
        quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._quantity, Unset):
            quantity = self._quantity.to_dict()

        role: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self._role, Unset):
            role = self._role.to_dict() if self._role else None

        volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._volume, Unset):
            volume = self._volume.to_dict()

        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._fields, Unset):
            fields = self._fields.to_dict()

        name = self._name
        parent_storage_id = self._parent_storage_id
        restricted_sample_party_ids: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._restricted_sample_party_ids, Unset):
            restricted_sample_party_ids = self._restricted_sample_party_ids

        restriction_status: Union[Unset, int] = UNSET
        if not isinstance(self._restriction_status, Unset):
            restriction_status = self._restriction_status.value

        sample_owner_ids: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._sample_owner_ids, Unset):
            sample_owner_ids = self._sample_owner_ids

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if role is not UNSET:
            field_dict["role"] = role
        if volume is not UNSET:
            field_dict["volume"] = volume
        if fields is not UNSET:
            field_dict["fields"] = fields
        if name is not UNSET:
            field_dict["name"] = name
        if parent_storage_id is not UNSET:
            field_dict["parentStorageId"] = parent_storage_id
        if restricted_sample_party_ids is not UNSET:
            field_dict["restrictedSamplePartyIds"] = restricted_sample_party_ids
        if restriction_status is not UNSET:
            field_dict["restrictionStatus"] = restriction_status
        if sample_owner_ids is not UNSET:
            field_dict["sampleOwnerIds"] = sample_owner_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_barcode() -> Union[Unset, str]:
            barcode = d.pop("barcode")
            return barcode

        try:
            barcode = get_barcode()
        except KeyError:
            if strict:
                raise
            barcode = cast(Union[Unset, str], UNSET)

        def get_project_id() -> Union[Unset, None, str]:
            project_id = d.pop("projectId")
            return project_id

        try:
            project_id = get_project_id()
        except KeyError:
            if strict:
                raise
            project_id = cast(Union[Unset, None, str], UNSET)

        def get_quantity() -> Union[Unset, ContainerQuantity]:
            quantity: Union[Unset, Union[Unset, ContainerQuantity]] = UNSET
            _quantity = d.pop("quantity")

            if not isinstance(_quantity, Unset):
                quantity = ContainerQuantity.from_dict(_quantity)

            return quantity

        try:
            quantity = get_quantity()
        except KeyError:
            if strict:
                raise
            quantity = cast(Union[Unset, ContainerQuantity], UNSET)

        def get_role() -> Union[Unset, None, ExperimentalWellRole]:
            role = None
            _role = d.pop("role")

            if _role is not None and not isinstance(_role, Unset):
                role = ExperimentalWellRole.from_dict(_role)

            return role

        try:
            role = get_role()
        except KeyError:
            if strict:
                raise
            role = cast(Union[Unset, None, ExperimentalWellRole], UNSET)

        def get_volume() -> Union[Unset, DeprecatedContainerVolumeForInput]:
            volume: Union[Unset, Union[Unset, DeprecatedContainerVolumeForInput]] = UNSET
            _volume = d.pop("volume")

            if not isinstance(_volume, Unset):
                volume = DeprecatedContainerVolumeForInput.from_dict(_volume)

            return volume

        try:
            volume = get_volume()
        except KeyError:
            if strict:
                raise
            volume = cast(Union[Unset, DeprecatedContainerVolumeForInput], UNSET)

        def get_fields() -> Union[Unset, Fields]:
            fields: Union[Unset, Union[Unset, Fields]] = UNSET
            _fields = d.pop("fields")

            if not isinstance(_fields, Unset):
                fields = Fields.from_dict(_fields)

            return fields

        try:
            fields = get_fields()
        except KeyError:
            if strict:
                raise
            fields = cast(Union[Unset, Fields], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        try:
            name = get_name()
        except KeyError:
            if strict:
                raise
            name = cast(Union[Unset, str], UNSET)

        def get_parent_storage_id() -> Union[Unset, str]:
            parent_storage_id = d.pop("parentStorageId")
            return parent_storage_id

        try:
            parent_storage_id = get_parent_storage_id()
        except KeyError:
            if strict:
                raise
            parent_storage_id = cast(Union[Unset, str], UNSET)

        def get_restricted_sample_party_ids() -> Union[Unset, List[str]]:
            restricted_sample_party_ids = cast(List[str], d.pop("restrictedSamplePartyIds"))

            return restricted_sample_party_ids

        try:
            restricted_sample_party_ids = get_restricted_sample_party_ids()
        except KeyError:
            if strict:
                raise
            restricted_sample_party_ids = cast(Union[Unset, List[str]], UNSET)

        def get_restriction_status() -> Union[Unset, SampleRestrictionStatus]:
            restriction_status = UNSET
            _restriction_status = d.pop("restrictionStatus")
            if _restriction_status is not None and _restriction_status is not UNSET:
                try:
                    restriction_status = SampleRestrictionStatus(_restriction_status)
                except ValueError:
                    restriction_status = SampleRestrictionStatus.of_unknown(_restriction_status)

            return restriction_status

        try:
            restriction_status = get_restriction_status()
        except KeyError:
            if strict:
                raise
            restriction_status = cast(Union[Unset, SampleRestrictionStatus], UNSET)

        def get_sample_owner_ids() -> Union[Unset, List[str]]:
            sample_owner_ids = cast(List[str], d.pop("sampleOwnerIds"))

            return sample_owner_ids

        try:
            sample_owner_ids = get_sample_owner_ids()
        except KeyError:
            if strict:
                raise
            sample_owner_ids = cast(Union[Unset, List[str]], UNSET)

        container_update = cls(
            barcode=barcode,
            project_id=project_id,
            quantity=quantity,
            role=role,
            volume=volume,
            fields=fields,
            name=name,
            parent_storage_id=parent_storage_id,
            restricted_sample_party_ids=restricted_sample_party_ids,
            restriction_status=restriction_status,
            sample_owner_ids=sample_owner_ids,
        )

        return container_update

    @property
    def barcode(self) -> str:
        """Barcode of the container. The barcode must be unique within the registry and cannot be empty."""
        if isinstance(self._barcode, Unset):
            raise NotPresentError(self, "barcode")
        return self._barcode

    @barcode.setter
    def barcode(self, value: str) -> None:
        self._barcode = value

    @barcode.deleter
    def barcode(self) -> None:
        self._barcode = UNSET

    @property
    def project_id(self) -> Optional[str]:
        if isinstance(self._project_id, Unset):
            raise NotPresentError(self, "project_id")
        return self._project_id

    @project_id.setter
    def project_id(self, value: Optional[str]) -> None:
        self._project_id = value

    @project_id.deleter
    def project_id(self) -> None:
        self._project_id = UNSET

    @property
    def quantity(self) -> ContainerQuantity:
        """ Quantity of a container, well, or transfer. Supports mass, volume, and other quantities. """
        if isinstance(self._quantity, Unset):
            raise NotPresentError(self, "quantity")
        return self._quantity

    @quantity.setter
    def quantity(self, value: ContainerQuantity) -> None:
        self._quantity = value

    @quantity.deleter
    def quantity(self) -> None:
        self._quantity = UNSET

    @property
    def role(self) -> Optional[ExperimentalWellRole]:
        if isinstance(self._role, Unset):
            raise NotPresentError(self, "role")
        return self._role

    @role.setter
    def role(self, value: Optional[ExperimentalWellRole]) -> None:
        self._role = value

    @role.deleter
    def role(self) -> None:
        self._role = UNSET

    @property
    def volume(self) -> DeprecatedContainerVolumeForInput:
        """Desired volume for a container, well, or transfer. "volume" type keys are deprecated in API requests; use the more permissive "quantity" type key instead."""
        if isinstance(self._volume, Unset):
            raise NotPresentError(self, "volume")
        return self._volume

    @volume.setter
    def volume(self, value: DeprecatedContainerVolumeForInput) -> None:
        self._volume = value

    @volume.deleter
    def volume(self) -> None:
        self._volume = UNSET

    @property
    def fields(self) -> Fields:
        if isinstance(self._fields, Unset):
            raise NotPresentError(self, "fields")
        return self._fields

    @fields.setter
    def fields(self, value: Fields) -> None:
        self._fields = value

    @fields.deleter
    def fields(self) -> None:
        self._fields = UNSET

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

    @property
    def parent_storage_id(self) -> str:
        """ ID of containing parent inventory, can also specify a coordinate for plates and boxes (e.g. plt_2bAks9dx:a2). """
        if isinstance(self._parent_storage_id, Unset):
            raise NotPresentError(self, "parent_storage_id")
        return self._parent_storage_id

    @parent_storage_id.setter
    def parent_storage_id(self, value: str) -> None:
        self._parent_storage_id = value

    @parent_storage_id.deleter
    def parent_storage_id(self) -> None:
        self._parent_storage_id = UNSET

    @property
    def restricted_sample_party_ids(self) -> List[str]:
        """IDs of users or teams who have access to use a restricted container. Well plate wells and unrestricted containers do not have restricted sample parties."""
        if isinstance(self._restricted_sample_party_ids, Unset):
            raise NotPresentError(self, "restricted_sample_party_ids")
        return self._restricted_sample_party_ids

    @restricted_sample_party_ids.setter
    def restricted_sample_party_ids(self, value: List[str]) -> None:
        self._restricted_sample_party_ids = value

    @restricted_sample_party_ids.deleter
    def restricted_sample_party_ids(self) -> None:
        self._restricted_sample_party_ids = UNSET

    @property
    def restriction_status(self) -> SampleRestrictionStatus:
        if isinstance(self._restriction_status, Unset):
            raise NotPresentError(self, "restriction_status")
        return self._restriction_status

    @restriction_status.setter
    def restriction_status(self, value: SampleRestrictionStatus) -> None:
        self._restriction_status = value

    @restriction_status.deleter
    def restriction_status(self) -> None:
        self._restriction_status = UNSET

    @property
    def sample_owner_ids(self) -> List[str]:
        """IDs of users or teams who are sample owners for the container. Well plate wells do not have sample owners."""
        if isinstance(self._sample_owner_ids, Unset):
            raise NotPresentError(self, "sample_owner_ids")
        return self._sample_owner_ids

    @sample_owner_ids.setter
    def sample_owner_ids(self, value: List[str]) -> None:
        self._sample_owner_ids = value

    @sample_owner_ids.deleter
    def sample_owner_ids(self) -> None:
        self._sample_owner_ids = UNSET
