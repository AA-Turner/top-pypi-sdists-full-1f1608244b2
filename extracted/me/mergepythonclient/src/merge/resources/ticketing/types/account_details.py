# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .account_details_category import AccountDetailsCategory


class AccountDetails(UncheckedBaseModel):
    id: typing.Optional[str] = None
    integration: typing.Optional[str] = None
    integration_slug: typing.Optional[str] = None
    category: typing.Optional[AccountDetailsCategory] = None
    end_user_origin_id: typing.Optional[str] = None
    end_user_organization_name: typing.Optional[str] = None
    end_user_email_address: typing.Optional[str] = None
    status: typing.Optional[str] = None
    webhook_listener_url: typing.Optional[str] = None
    is_duplicate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a Production Linked Account's credentials match another existing Production Linked Account. This field is `null` for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets.
    """

    account_type: typing.Optional[str] = None
    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which account completes the linking flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
