# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .address import AddressParams
from .vendor_contact import VendorContactParams
from ..types.vendor_status import VendorStatus


class VendorParams(typing_extensions.TypedDict):
    """
    Represents a supplier to a seller.
    """

    id: typing_extensions.NotRequired[str]
    """
    A unique Square-generated ID for the [Vendor](entity:Vendor).
    This field is required when attempting to update a [Vendor](entity:Vendor).
    """

    created_at: typing_extensions.NotRequired[str]
    """
    An RFC 3339-formatted timestamp that indicates when the
    [Vendor](entity:Vendor) was created.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    An RFC 3339-formatted timestamp that indicates when the
    [Vendor](entity:Vendor) was last updated.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the [Vendor](entity:Vendor).
    This field is required when attempting to create or update a [Vendor](entity:Vendor).
    """

    address: typing_extensions.NotRequired[AddressParams]
    """
    The address of the [Vendor](entity:Vendor).
    """

    contacts: typing_extensions.NotRequired[typing.Optional[typing.Sequence[VendorContactParams]]]
    """
    The contacts of the [Vendor](entity:Vendor).
    """

    account_number: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The account number of the [Vendor](entity:Vendor).
    """

    note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A note detailing information about the [Vendor](entity:Vendor).
    """

    version: typing_extensions.NotRequired[int]
    """
    The version of the [Vendor](entity:Vendor).
    """

    status: typing_extensions.NotRequired[VendorStatus]
    """
    The status of the [Vendor](entity:Vendor).
    See [Status](#type-status) for possible values
    """
