# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Atlan Pte. Ltd.


from __future__ import annotations

from typing import ClassVar, List, Optional

from pydantic.v1 import Field, validator

from pyatlan.model.enums import ModelCardinalityType
from pyatlan.model.fields.atlan_fields import KeywordField, NumericField, RelationField

from .model import Model


class ModelEntityAssociation(Model):
    """Description"""

    type_name: str = Field(default="ModelEntityAssociation", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "ModelEntityAssociation":
            raise ValueError("must be ModelEntityAssociation")
        return v

    def __setattr__(self, name, value):
        if name in ModelEntityAssociation._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    MODEL_ENTITY_ASSOCIATION_CARDINALITY: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationCardinality", "modelEntityAssociationCardinality"
    )
    """
    (Deprecated) Cardinality of the data entity association.
    """
    MODEL_ENTITY_ASSOCIATION_LABEL: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationLabel", "modelEntityAssociationLabel"
    )
    """
    (Deprecated) Label of the data entity association.
    """
    MODEL_ENTITY_ASSOCIATION_TO_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationToQualifiedName", "modelEntityAssociationToQualifiedName"
    )
    """
    Unique name of the association to which this entity is related.
    """
    MODEL_ENTITY_ASSOCIATION_TO_LABEL: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationToLabel", "modelEntityAssociationToLabel"
    )
    """
    Label when read from the association to which this entity is related.
    """
    MODEL_ENTITY_ASSOCIATION_TO_MIN_CARDINALITY: ClassVar[NumericField] = NumericField(
        "modelEntityAssociationToMinCardinality",
        "modelEntityAssociationToMinCardinality",
    )
    """
    Minimum cardinality of the data entity to which the association exists.
    """
    MODEL_ENTITY_ASSOCIATION_TO_MAX_CARDINALITY: ClassVar[NumericField] = NumericField(
        "modelEntityAssociationToMaxCardinality",
        "modelEntityAssociationToMaxCardinality",
    )
    """
    Maximum cardinality of the data entity to which the association exists.
    """
    MODEL_ENTITY_ASSOCIATION_FROM_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationFromQualifiedName",
        "modelEntityAssociationFromQualifiedName",
    )
    """
    Unique name of the association from which this entity is related.
    """
    MODEL_ENTITY_ASSOCIATION_FROM_LABEL: ClassVar[KeywordField] = KeywordField(
        "modelEntityAssociationFromLabel", "modelEntityAssociationFromLabel"
    )
    """
    Label when read from the association from which this entity is related.
    """
    MODEL_ENTITY_ASSOCIATION_FROM_MIN_CARDINALITY: ClassVar[NumericField] = (
        NumericField(
            "modelEntityAssociationFromMinCardinality",
            "modelEntityAssociationFromMinCardinality",
        )
    )
    """
    Minimum cardinality of the data entity from which the association exists.
    """
    MODEL_ENTITY_ASSOCIATION_FROM_MAX_CARDINALITY: ClassVar[NumericField] = (
        NumericField(
            "modelEntityAssociationFromMaxCardinality",
            "modelEntityAssociationFromMaxCardinality",
        )
    )
    """
    Maximum cardinality of the data entity from which the association exists.
    """

    MODEL_ENTITY_ASSOCIATION_TO: ClassVar[RelationField] = RelationField(
        "modelEntityAssociationTo"
    )
    """
    TBC
    """
    MODEL_ENTITY_ASSOCIATION_FROM: ClassVar[RelationField] = RelationField(
        "modelEntityAssociationFrom"
    )
    """
    TBC
    """

    _convenience_properties: ClassVar[List[str]] = [
        "model_entity_association_cardinality",
        "model_entity_association_label",
        "model_entity_association_to_qualified_name",
        "model_entity_association_to_label",
        "model_entity_association_to_min_cardinality",
        "model_entity_association_to_max_cardinality",
        "model_entity_association_from_qualified_name",
        "model_entity_association_from_label",
        "model_entity_association_from_min_cardinality",
        "model_entity_association_from_max_cardinality",
        "model_entity_association_to",
        "model_entity_association_from",
    ]

    @property
    def model_entity_association_cardinality(self) -> Optional[ModelCardinalityType]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_cardinality
        )

    @model_entity_association_cardinality.setter
    def model_entity_association_cardinality(
        self, model_entity_association_cardinality: Optional[ModelCardinalityType]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_cardinality = (
            model_entity_association_cardinality
        )

    @property
    def model_entity_association_label(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_label
        )

    @model_entity_association_label.setter
    def model_entity_association_label(
        self, model_entity_association_label: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_label = model_entity_association_label

    @property
    def model_entity_association_to_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_to_qualified_name
        )

    @model_entity_association_to_qualified_name.setter
    def model_entity_association_to_qualified_name(
        self, model_entity_association_to_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_to_qualified_name = (
            model_entity_association_to_qualified_name
        )

    @property
    def model_entity_association_to_label(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_to_label
        )

    @model_entity_association_to_label.setter
    def model_entity_association_to_label(
        self, model_entity_association_to_label: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_to_label = (
            model_entity_association_to_label
        )

    @property
    def model_entity_association_to_min_cardinality(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_to_min_cardinality
        )

    @model_entity_association_to_min_cardinality.setter
    def model_entity_association_to_min_cardinality(
        self, model_entity_association_to_min_cardinality: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_to_min_cardinality = (
            model_entity_association_to_min_cardinality
        )

    @property
    def model_entity_association_to_max_cardinality(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_to_max_cardinality
        )

    @model_entity_association_to_max_cardinality.setter
    def model_entity_association_to_max_cardinality(
        self, model_entity_association_to_max_cardinality: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_to_max_cardinality = (
            model_entity_association_to_max_cardinality
        )

    @property
    def model_entity_association_from_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_from_qualified_name
        )

    @model_entity_association_from_qualified_name.setter
    def model_entity_association_from_qualified_name(
        self, model_entity_association_from_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_from_qualified_name = (
            model_entity_association_from_qualified_name
        )

    @property
    def model_entity_association_from_label(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_from_label
        )

    @model_entity_association_from_label.setter
    def model_entity_association_from_label(
        self, model_entity_association_from_label: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_from_label = (
            model_entity_association_from_label
        )

    @property
    def model_entity_association_from_min_cardinality(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_from_min_cardinality
        )

    @model_entity_association_from_min_cardinality.setter
    def model_entity_association_from_min_cardinality(
        self, model_entity_association_from_min_cardinality: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_from_min_cardinality = (
            model_entity_association_from_min_cardinality
        )

    @property
    def model_entity_association_from_max_cardinality(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_from_max_cardinality
        )

    @model_entity_association_from_max_cardinality.setter
    def model_entity_association_from_max_cardinality(
        self, model_entity_association_from_max_cardinality: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_from_max_cardinality = (
            model_entity_association_from_max_cardinality
        )

    @property
    def model_entity_association_to(self) -> Optional[ModelEntity]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_to
        )

    @model_entity_association_to.setter
    def model_entity_association_to(
        self, model_entity_association_to: Optional[ModelEntity]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_to = model_entity_association_to

    @property
    def model_entity_association_from(self) -> Optional[ModelEntity]:
        return (
            None
            if self.attributes is None
            else self.attributes.model_entity_association_from
        )

    @model_entity_association_from.setter
    def model_entity_association_from(
        self, model_entity_association_from: Optional[ModelEntity]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.model_entity_association_from = model_entity_association_from

    class Attributes(Model.Attributes):
        model_entity_association_cardinality: Optional[ModelCardinalityType] = Field(
            default=None, description=""
        )
        model_entity_association_label: Optional[str] = Field(
            default=None, description=""
        )
        model_entity_association_to_qualified_name: Optional[str] = Field(
            default=None, description=""
        )
        model_entity_association_to_label: Optional[str] = Field(
            default=None, description=""
        )
        model_entity_association_to_min_cardinality: Optional[int] = Field(
            default=None, description=""
        )
        model_entity_association_to_max_cardinality: Optional[int] = Field(
            default=None, description=""
        )
        model_entity_association_from_qualified_name: Optional[str] = Field(
            default=None, description=""
        )
        model_entity_association_from_label: Optional[str] = Field(
            default=None, description=""
        )
        model_entity_association_from_min_cardinality: Optional[int] = Field(
            default=None, description=""
        )
        model_entity_association_from_max_cardinality: Optional[int] = Field(
            default=None, description=""
        )
        model_entity_association_to: Optional[ModelEntity] = Field(
            default=None, description=""
        )  # relationship
        model_entity_association_from: Optional[ModelEntity] = Field(
            default=None, description=""
        )  # relationship

    attributes: ModelEntityAssociation.Attributes = Field(
        default_factory=lambda: ModelEntityAssociation.Attributes(),
        description=(
            "Map of attributes in the instance and their values. "
            "The specific keys of this map will vary by type, "
            "so are described in the sub-types of this schema."
        ),
    )


from .model_entity import ModelEntity  # noqa: E402, F401
