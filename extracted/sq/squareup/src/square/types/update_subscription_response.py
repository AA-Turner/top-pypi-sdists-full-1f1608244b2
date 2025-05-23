# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .subscription import Subscription
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateSubscriptionResponse(UncheckedBaseModel):
    """
    Defines output parameters in a response from the
    [UpdateSubscription](api-endpoint:Subscriptions-UpdateSubscription) endpoint.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors encountered during the request.
    """

    subscription: typing.Optional[Subscription] = pydantic.Field(default=None)
    """
    The updated subscription.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
