# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .sentinel_one_credential import SentinelOneCredential
from .sentinel_one_edr_events_credential import SentinelOneEdrEventsCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EdrSentinelOne(pydantic.BaseModel):
    """
    Configuration for the SentinelOne EDR Provider
    """

    credential: SentinelOneCredential
    edr_events_credential: typing.Optional[SentinelOneEdrEventsCredential] = None
    edr_events_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base URL for the SentinelOne Singularity Data Lake API. This URL is required if you plan to use the EDR Events API.
    """

    url: str = pydantic.Field()
    """
    URL for the SentinelOne Management API. This should be the base URL for the API, without any path components. For example, "https://your_management_url".
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
