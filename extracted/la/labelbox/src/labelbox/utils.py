import datetime
import re

from dateutil.tz import tzoffset
from dateutil.parser import isoparse as dateutil_parse
from dateutil.utils import default_tzinfo

from urllib.parse import urlparse
from pydantic import (
    BaseModel,
    ConfigDict,
    model_serializer,
)
from pydantic.alias_generators import to_camel

UPPERCASE_COMPONENTS = ["uri", "rgb"]
ISO_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DFLT_TZ = tzoffset("UTC", 0000)


def _convert(s, sep, title):
    components = re.findall(r"[A-Z][a-z0-9]*|[a-z][a-z0-9]*", s)
    components = list(map(str.lower, filter(None, components)))
    for i in range(len(components)):
        if components[i] in UPPERCASE_COMPONENTS:
            components[i] = components[i].upper()
        elif title(i):
            components[i] = components[i][0].upper() + components[i][1:]
    return sep.join(components)


def camel_case(s):
    """Converts a string in [snake|camel|title]case to camelCase."""
    return _convert(s, "", lambda i: i > 0)


def title_case(s):
    """Converts a string in [snake|camel|title]case to TitleCase."""
    return _convert(s, "", lambda i: True)


def snake_case(s):
    """Converts a string in [snake|camel|title]case to snake_case."""
    return _convert(s, "_", lambda i: False)


def sentence_case(s: str) -> str:
    """Converts a string in [snake|camel|title]case to Sentence case."""
    # Replace underscores with spaces and convert to lower case
    sentence_str = s.replace("_", " ").lower()
    # Capitalize the first letter of each word
    sentence_str = sentence_str.capitalize()
    return sentence_str


def is_exactly_one_set(*args):
    return sum([bool(arg) for arg in args]) == 1


def is_valid_uri(uri):
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except:
        return False


class _CamelCaseMixin(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        alias_generator=to_camel,
        populate_by_name=True,
    )


class _NoCoercionMixin:
    """
    When using Unions in type annotations, pydantic will try to coerce the type
    of the object to the type of the first Union member. Which results in
    uninteded behavior.

    This mixin uses a class_name discriminator field to prevent pydantic from
    corecing the type of the object. Add a class_name field to the class you
    want to discrimniate and use this mixin class to remove the discriminator
    when serializing the object.

    Example:
        class GenericDataRowData(BaseData, _NoCoercionMixin):
            class_name: Literal["GenericDataRowData"] = "GenericDataRowData"

    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        res = handler(self)
        res.pop("class_name")
        return res


def format_iso_datetime(dt: datetime.datetime) -> str:
    """
    Formats a datetime object into the format: 2011-11-04T00:05:23Z
    Note that datetime.isoformat() outputs 2011-11-04T00:05:23+00:00
    """
    return dt.astimezone(datetime.timezone.utc).strftime(ISO_DATETIME_FORMAT)


def format_iso_from_string(date_string: str) -> datetime.datetime:
    """
    Converts a string even if offset is missing: 2011-11-04T00:05:23Z or 2011-11-04T00:05:23+00:00 or 2011-11-04T00:05:23
    to a datetime object.
    For missing offsets, the default offset is UTC.
    """
    # return datetime.datetime.fromisoformat(date_string)
    return default_tzinfo(dateutil_parse(date_string), DFLT_TZ)
