# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .catalog_subscription_plan_variation import CatalogSubscriptionPlanVariation
import pydantic
from .catalog_custom_attribute_value import CatalogCustomAttributeValue
import typing_extensions
from .catalog_v1id import CatalogV1Id
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogObjectSubscriptionPlanVariation(UncheckedBaseModel):
    type: typing.Literal["SUBSCRIPTION_PLAN_VARIATION"] = "SUBSCRIPTION_PLAN_VARIATION"
    subscription_plan_variation_data: typing.Optional[CatalogSubscriptionPlanVariation] = pydantic.Field(default=None)
    """
    Structured data for a `CatalogSubscriptionPlanVariation`, set for CatalogObjects of type `SUBSCRIPTION_PLAN_VARIATION`.
    """

    id: str = pydantic.Field()
    """
    An identifier to reference this object in the catalog. When a new `CatalogObject`
    is inserted, the client should set the id to a temporary identifier starting with
    a "`#`" character. Other objects being inserted or updated within the same request
    may use this identifier to refer to the new object.
    
    When the server receives the new object, it will supply a unique identifier that
    replaces the temporary identifier for all future references.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last modification [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) in RFC 3339 format, e.g., `"2016-08-15T23:59:33.123Z"`
    would indicate the UTC time (denoted by `Z`) of August 15, 2016 at 23:59:33 and 123 milliseconds.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the object. When updating an object, the version supplied
    must match the version in the database, otherwise the write will be rejected as conflicting.
    """

    is_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the object has been deleted from the database. Must be `false` for new objects
    being inserted. When deleted, the `updated_at` field will equal the deletion time.
    """

    custom_attribute_values: typing.Optional[typing.Dict[str, CatalogCustomAttributeValue]] = pydantic.Field(
        default=None
    )
    """
    A map (key-value pairs) of application-defined custom attribute values. The value of a key-value pair
    is a [CatalogCustomAttributeValue](entity:CatalogCustomAttributeValue) object. The key is the `key` attribute
    value defined in the associated [CatalogCustomAttributeDefinition](entity:CatalogCustomAttributeDefinition)
    object defined by the application making the request.
    
    If the `CatalogCustomAttributeDefinition` object is
    defined by another application, the `CatalogCustomAttributeDefinition`'s key attribute value is prefixed by
    the defining application ID. For example, if the `CatalogCustomAttributeDefinition` has a `key` attribute of
    `"cocoa_brand"` and the defining application ID is `"abcd1234"`, the key in the map is `"abcd1234:cocoa_brand"`
    if the application making the request is different from the application defining the custom attribute definition.
    Otherwise, the key used in the map is simply `"cocoa_brand"`.
    
    Application-defined custom attributes are set at a global (location-independent) level.
    Custom attribute values are intended to store additional information about a catalog object
    or associations with an entity in another system. Do not use custom attributes
    to store any sensitive information (personally identifiable information, card details, etc.).
    """

    catalog_v1ids: typing_extensions.Annotated[
        typing.Optional[typing.List[CatalogV1Id]], FieldMetadata(alias="catalog_v1_ids")
    ] = pydantic.Field(default=None)
    """
    The Connect v1 IDs for this object at each location where it is present, where they
    differ from the object's Connect V2 ID. The field will only be present for objects that
    have been created or modified by legacy APIs.
    """

    present_at_all_locations: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, this object is present at all locations (including future locations), except where specified in
    the `absent_at_location_ids` field. If `false`, this object is not present at any locations (including future locations),
    except where specified in the `present_at_location_ids` field. If not specified, defaults to `true`.
    """

    present_at_location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of locations where the object is present, even if `present_at_all_locations` is `false`.
    This can include locations that are deactivated.
    """

    absent_at_location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of locations where the object is not present, even if `present_at_all_locations` is `true`.
    This can include locations that are deactivated.
    """

    image_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the `CatalogImage` attached to this `CatalogObject`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
