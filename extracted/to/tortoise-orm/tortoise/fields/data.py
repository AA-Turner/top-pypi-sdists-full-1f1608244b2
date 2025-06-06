from __future__ import annotations

import datetime
import functools
import json
import warnings
from collections.abc import Callable
from decimal import Decimal
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID, uuid4

from pypika_tortoise import functions
from pypika_tortoise.enums import SqlTypes
from pypika_tortoise.terms import Term

from tortoise import timezone
from tortoise.exceptions import ConfigurationError, FieldError
from tortoise.fields.base import Field
from tortoise.timezone import get_default_timezone, get_timezone, get_use_tz, localtime
from tortoise.validators import MaxLengthValidator

try:
    from ciso8601 import parse_datetime
except ImportError:  # pragma: nocoverage
    from iso8601 import parse_date

    parse_datetime = functools.partial(parse_date, default_timezone=None)

if TYPE_CHECKING:  # pragma: nocoverage
    from tortoise.models import Model

__all__ = (
    "BigIntField",
    "BinaryField",
    "BooleanField",
    "CharEnumField",
    "CharField",
    "DateField",
    "DatetimeField",
    "DecimalField",
    "FloatField",
    "IntEnumField",
    "IntField",
    "JSONField",
    "SmallIntField",
    "TextField",
    "TimeDeltaField",
    "TimeField",
    "UUIDField",
)

T = TypeVar("T")

# Doing this we can replace json dumps/loads with different implementations
JsonDumpsFunc = Callable[[Any], str]
JsonLoadsFunc = Callable[[Union[str, bytes]], Any]
JSON_DUMPS: JsonDumpsFunc = functools.partial(json.dumps, separators=(",", ":"))
JSON_LOADS: JsonLoadsFunc = json.loads

try:
    # Use orjson as an optional accelerator
    import orjson

    JSON_DUMPS = lambda x: orjson.dumps(x).decode()  # noqa: E731
    JSON_LOADS = orjson.loads
except ImportError:  # pragma: nocoverage
    pass


class IntField(Field[int], int):
    """
    Integer field. (32-bit signed)

    ``primary_key`` (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "INT"
    allows_generated = True

    def __init__(self, primary_key: bool | None = None, **kwargs: Any) -> None:
        if primary_key or kwargs.get("pk"):
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(primary_key=primary_key, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": -2147483648,
            "le": 2147483647,
        }

    class _db_postgres:
        GENERATED_SQL = "SERIAL NOT NULL PRIMARY KEY"

    class _db_sqlite:
        GENERATED_SQL = "INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL"

    class _db_mysql:
        GENERATED_SQL = "INT NOT NULL PRIMARY KEY AUTO_INCREMENT"

    class _db_mssql:
        GENERATED_SQL = "INT IDENTITY(1,1) NOT NULL PRIMARY KEY"

    class _db_oracle:
        GENERATED_SQL = "INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL"


class BigIntField(IntField):
    """
    Big integer field. (64-bit signed)

    ``primary_key`` (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "BIGINT"

    @property
    def constraints(self) -> dict:
        return {
            "ge": -9223372036854775808,
            "le": 9223372036854775807,
        }

    class _db_postgres:
        GENERATED_SQL = "BIGSERIAL NOT NULL PRIMARY KEY"

    class _db_mysql:
        GENERATED_SQL = "BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT"

    class _db_mssql:
        GENERATED_SQL = "BIGINT IDENTITY(1,1) NOT NULL PRIMARY KEY"

    class _db_oracle:
        SQL_TYPE = "INT"
        GENERATED_SQL = "INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL"


class SmallIntField(IntField):
    """
    Small integer field. (16-bit signed)

    ``primary_key`` (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "SMALLINT"

    @property
    def constraints(self) -> dict:
        return {
            "ge": -32768,
            "le": 32767,
        }

    class _db_postgres:
        GENERATED_SQL = "SMALLSERIAL NOT NULL PRIMARY KEY"

    class _db_mysql:
        GENERATED_SQL = "SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT"

    class _db_mssql:
        GENERATED_SQL = "SMALLINT IDENTITY(1,1) NOT NULL PRIMARY KEY"

    class _db_oracle:
        GENERATED_SQL = "SMALLINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL"


class CharField(Field[str]):
    """
    Character field.

    You must provide the following:

    ``max_length`` (int):
        Maximum length of the field in characters.
    """

    field_type = str

    def __init__(self, max_length: int, **kwargs: Any) -> None:
        if int(max_length) < 1:
            raise ConfigurationError("'max_length' must be >= 1")
        self.max_length = int(max_length)
        super().__init__(**kwargs)
        self.validators.append(MaxLengthValidator(self.max_length))

    @property
    def constraints(self) -> dict:
        return {
            "max_length": self.max_length,
        }

    @property
    def SQL_TYPE(self) -> str:  # type: ignore
        return f"VARCHAR({self.max_length})"

    class _db_oracle:
        def __init__(self, field: CharField) -> None:
            self.field = field

        @property
        def SQL_TYPE(self) -> str:
            return f"NVARCHAR2({self.field.max_length})"


class TextField(Field[str], str):  # type: ignore
    """
    Large Text field.
    """

    indexable = False
    SQL_TYPE = "TEXT"

    def __init__(
        self,
        primary_key: bool | None = None,
        unique: bool = False,
        db_index: bool = False,
        **kwargs: Any,
    ) -> None:
        if primary_key or kwargs.get("pk"):
            warnings.warn(
                "TextField as a PrimaryKey is Deprecated, use CharField instead",
                DeprecationWarning,
                stacklevel=2,
            )
        if unique:
            raise ConfigurationError(
                "TextField doesn't support unique indexes, consider CharField or another strategy"
            )
        if db_index or kwargs.get("index"):
            raise ConfigurationError("TextField can't be indexed, consider CharField")

        super().__init__(primary_key=primary_key, **kwargs)

    class _db_mysql:
        SQL_TYPE = "LONGTEXT"

    class _db_mssql:
        SQL_TYPE = "NVARCHAR(MAX)"

    class _db_oracle:
        SQL_TYPE = "NCLOB"


class BooleanField(Field[bool]):
    """
    Boolean field.
    """

    # Bool is not subclassable, so we specify type here
    field_type = bool
    SQL_TYPE = "BOOL"

    class _db_sqlite:
        SQL_TYPE = "INT"

    class _db_mssql:
        SQL_TYPE = "BIT"

    class _db_oracle:
        SQL_TYPE = "NUMBER(1)"


class DecimalField(Field[Decimal], Decimal):
    """
    Accurate decimal field.

    You must provide the following:

    ``max_digits`` (int):
        Max digits of significance of the decimal field.
    ``decimal_places`` (int):
        How many of those significant digits is after the decimal point.
    """

    skip_to_python_if_native = True

    def __init__(self, max_digits: int, decimal_places: int, **kwargs: Any) -> None:
        if int(max_digits) < 1:
            raise ConfigurationError("'max_digits' must be >= 1")
        if int(decimal_places) < 0:
            raise ConfigurationError("'decimal_places' must be >= 0")
        super().__init__(**kwargs)
        self.max_digits = max_digits
        self.decimal_places = decimal_places
        self.quant = Decimal("1" if decimal_places == 0 else f"1.{('0' * decimal_places)}")

    def to_python_value(self, value: Any) -> Decimal | None:
        if value is not None:
            value = Decimal(value).quantize(self.quant).normalize()
        return value

    @property
    def SQL_TYPE(self) -> str:  # type: ignore
        return f"DECIMAL({self.max_digits},{self.decimal_places})"

    class _db_sqlite:
        SQL_TYPE = "VARCHAR(40)"

        def function_cast(self, term: Term) -> Term:
            return functions.Cast(term, SqlTypes.NUMERIC)


# In case of queryset with filter `__year`/`__month`/`__day` ..., value can be int, float or str. Example:
# `await MyModel.filter(created_at__year=2024)`
# `await MyModel.filter(created_at__year=2024.0)`
# `await MyModel.filter(created_at__year='2024')`
DatetimeFieldQueryValueType = TypeVar(
    "DatetimeFieldQueryValueType", datetime.datetime, int, float, str
)


class DatetimeField(Field[datetime.datetime], datetime.datetime):
    """
    Datetime field.

    ``auto_now`` and ``auto_now_add`` is exclusive.
    You can opt to set neither or only ONE of them.

    ``auto_now`` (bool):
        Always set to ``datetime.utcnow()`` on save.
    ``auto_now_add`` (bool):
        Set to ``datetime.utcnow()`` on first save only.
    """

    SQL_TYPE = "TIMESTAMP"

    class _db_mysql:
        SQL_TYPE = "DATETIME(6)"

    class _db_postgres:
        SQL_TYPE = "TIMESTAMPTZ"

    class _db_mssql:
        SQL_TYPE = "DATETIME2"

    class _db_oracle:
        SQL_TYPE = "TIMESTAMP WITH TIME ZONE"

    def __init__(self, auto_now: bool = False, auto_now_add: bool = False, **kwargs: Any) -> None:
        if auto_now_add and auto_now:
            raise ConfigurationError("You can choose only 'auto_now' or 'auto_now_add'")
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self.auto_now_add = auto_now | auto_now_add

    def to_python_value(self, value: Any) -> datetime.datetime | None:
        if value is not None:
            if isinstance(value, datetime.datetime):
                value = value
            elif isinstance(value, int):
                value = datetime.datetime.fromtimestamp(value)
            else:
                value = parse_datetime(value)
            if timezone.is_naive(value):
                value = timezone.make_aware(value, get_timezone())
            else:
                value = localtime(value)
        return value

    def to_db_value(
        self, value: DatetimeFieldQueryValueType | None, instance: type[Model] | Model
    ) -> DatetimeFieldQueryValueType | None:
        # Only do this if it is a Model instance, not class. Test for guaranteed instance var
        if hasattr(instance, "_saved_in_db") and (
            self.auto_now
            or (self.auto_now_add and getattr(instance, self.model_field_name) is None)
        ):
            now = timezone.now()
            setattr(instance, self.model_field_name, now)
            return now  # type:ignore[return-value]
        if value is not None:
            if isinstance(value, datetime.datetime) and get_use_tz():
                if timezone.is_naive(value):
                    warnings.warn(
                        f"DateTimeField {self.model_field_name} received a naive datetime ({value})"
                        " while time zone support is active.",
                        RuntimeWarning,
                    )
                    value = timezone.make_aware(value, "UTC")
        self.validate(value)
        return value

    @property
    def constraints(self) -> dict:
        data = {}
        if self.auto_now_add:
            data["readOnly"] = True
        return data

    def describe(self, serializable: bool) -> dict:
        desc = super().describe(serializable)
        desc["auto_now_add"] = self.auto_now_add
        desc["auto_now"] = self.auto_now
        return desc


class DateField(Field[datetime.date], datetime.date):
    """
    Date field.
    """

    skip_to_python_if_native = True
    SQL_TYPE = "DATE"

    def to_python_value(self, value: Any) -> datetime.date | None:
        if value is not None and not isinstance(value, datetime.date):
            value = parse_datetime(value).date()
        return value

    def to_db_value(
        self, value: datetime.date | str | None, instance: type[Model] | Model
    ) -> datetime.date | None:
        if value is not None and not isinstance(value, datetime.date):
            value = parse_datetime(value).date()
        self.validate(value)
        return value


class TimeField(Field[datetime.time], datetime.time):
    """
    Time field.
    """

    skip_to_python_if_native = True
    SQL_TYPE = "TIME"

    class _db_oracle:
        SQL_TYPE = "NVARCHAR2(8)"

    def __init__(self, auto_now: bool = False, auto_now_add: bool = False, **kwargs: Any) -> None:
        if auto_now_add and auto_now:
            raise ConfigurationError("You can choose only 'auto_now' or 'auto_now_add'")
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self.auto_now_add = auto_now | auto_now_add

    def to_python_value(self, value: Any) -> datetime.time | datetime.timedelta | None:
        if value is not None:
            if isinstance(value, str):
                value = datetime.time.fromisoformat(value)
            if isinstance(value, datetime.timedelta):
                return value
            if timezone.is_naive(value):
                value = value.replace(tzinfo=get_default_timezone())
        return value

    def to_db_value(
        self,
        value: datetime.time | datetime.timedelta | None,
        instance: type[Model] | Model,
    ) -> datetime.time | datetime.timedelta | None:
        # Only do this if it is a Model instance, not class. Test for guaranteed instance var
        if hasattr(instance, "_saved_in_db") and (
            self.auto_now
            or (self.auto_now_add and getattr(instance, self.model_field_name) is None)
        ):
            now = timezone.now().time()
            setattr(instance, self.model_field_name, now)
            return now
        if value is not None:
            if isinstance(value, datetime.timedelta):
                return value
            if get_use_tz():
                if timezone.is_naive(value):
                    warnings.warn(
                        f"TimeField {self.model_field_name} received a naive time ({value})"
                        " while time zone support is active.",
                        RuntimeWarning,
                    )
                    value = value.replace(tzinfo=get_default_timezone())
        self.validate(value)
        return value

    class _db_mysql:
        SQL_TYPE = "TIME(6)"

    class _db_postgres:
        SQL_TYPE = "TIMETZ"


class TimeDeltaField(Field[datetime.timedelta]):
    """
    A field for storing time differences.
    """

    field_type = datetime.timedelta
    SQL_TYPE = "BIGINT"

    class _db_oracle:
        SQL_TYPE = "NUMBER(19)"

    def to_python_value(self, value: Any) -> datetime.timedelta | None:
        if value is None or isinstance(value, datetime.timedelta):
            return value
        return datetime.timedelta(microseconds=value)

    def to_db_value(
        self, value: datetime.timedelta | None, instance: type[Model] | Model
    ) -> int | None:
        self.validate(value)

        if value is None:
            return None
        return (value.days * 86400000000) + (value.seconds * 1000000) + value.microseconds


class FloatField(Field[float], float):
    """
    Float (double) field.
    """

    SQL_TYPE = "DOUBLE PRECISION"

    class _db_sqlite:
        SQL_TYPE = "REAL"

    class _db_mysql:
        SQL_TYPE = "DOUBLE"


class JSONField(Field[T], dict, list):  # type: ignore
    """
    JSON field.

    This field can store dictionaries or lists of any JSON-compliant structure.

    You can use generics to make static checking more friendly. Example: ``JSONField[dict[str, str]]``

    You can specify your own custom JSON encoder/decoder, leaving at the default should work well.
    If you have ``orjson`` installed, we default to using that,
    else the default ``json`` module will be used.

    ``encoder``:
        The custom JSON encoder.
    ``decoder``:
        The custom JSON decoder.

    If you want to use Pydantic model as the field type for generating a better OpenAPI documentation, you can use ``field_type`` to specify the type of the field.

    ``field_type``:
        The Pydantic model class.

    """

    SQL_TYPE = "JSON"
    indexable = False

    class _db_postgres:
        SQL_TYPE = "JSONB"

    class _db_mssql:
        SQL_TYPE = "NVARCHAR(MAX)"

    class _db_oracle:
        SQL_TYPE = "NCLOB"

    def __init__(
        self,
        encoder: JsonDumpsFunc = JSON_DUMPS,
        decoder: JsonLoadsFunc = JSON_LOADS,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder
        if field_type := kwargs.get("field_type"):
            self.field_type = field_type

    def to_db_value(
        self,
        value: T | dict | list | str | bytes | None,
        instance: type[Model] | Model,
    ) -> str | None:
        self.validate(value)
        if value is None:
            return None

        if isinstance(value, (str, bytes)):
            try:
                self.decoder(value)
            except Exception:
                raise FieldError(f"Value {value!r} is invalid json value.")
            if isinstance(value, bytes):
                return value.decode()
            return value

        try:
            from pydantic import BaseModel

            if isinstance(value, BaseModel):
                value = value.model_dump()
        except ImportError:
            pass

        return self.encoder(value)

    def to_python_value(
        self, value: T | str | bytes | dict | list | None
    ) -> T | dict | list | None:
        if isinstance(value, (str, bytes)):
            try:
                data = self.decoder(value)

                try:
                    from pydantic._internal._model_construction import ModelMetaclass

                    if isinstance(self.field_type, ModelMetaclass) and not isinstance(data, list):
                        return self.field_type(**data)
                except ImportError:
                    pass

                return data
            except Exception:
                raise FieldError(
                    f"Value {value if isinstance(value, str) else value.decode()} is invalid json value."
                )

        return value


class UUIDField(Field[UUID], UUID):
    """
    UUID Field

    This field can store uuid value.

    If used as a primary key, it will auto-generate a UUID4 by default.
    """

    SQL_TYPE = "CHAR(36)"

    class _db_postgres:
        SQL_TYPE = "UUID"

    def __init__(self, **kwargs: Any) -> None:
        if (kwargs.get("primary_key") or kwargs.get("pk", False)) and "default" not in kwargs:
            kwargs["default"] = uuid4
        super().__init__(**kwargs)

    def to_db_value(self, value: Any, instance: type[Model] | Model) -> str | None:
        return value and str(value)

    def to_python_value(self, value: Any) -> UUID | None:
        if value is None or isinstance(value, UUID):
            return value
        return UUID(value)


class BinaryField(Field[bytes], bytes):  # type: ignore
    """
    Binary field.

    This is for storing ``bytes`` objects.
    Note that filter or queryset-update operations are not supported.
    """

    indexable = False
    SQL_TYPE = "BLOB"

    class _db_postgres:
        SQL_TYPE = "BYTEA"

    class _db_mysql:
        SQL_TYPE = "LONGBLOB"

    class _db_mssql:
        SQL_TYPE = "VARBINARY(MAX)"


class IntEnumFieldInstance(SmallIntField):
    def __init__(
        self,
        enum_type: type[IntEnum],
        description: str | None = None,
        generated: bool = False,
        **kwargs: Any,
    ) -> None:
        # Validate values
        minimum = 1 if generated else -32768
        for item in enum_type:
            try:
                value = int(item.value)
            except ValueError:
                raise ConfigurationError("IntEnumField only supports integer enums!")
            if not minimum <= value < 32768:
                raise ConfigurationError(
                    f"The valid range of IntEnumField's values is {minimum}..32767!"
                )

        # Automatic description for the field if not specified by the user
        if description is None:
            description = "\n".join([f"{e.name}: {int(e.value)}" for e in enum_type])[:2048]

        super().__init__(description=description, **kwargs)
        self.enum_type = enum_type

    def to_python_value(self, value: int | None) -> IntEnum | None:
        value = self.enum_type(value) if value is not None else None
        return value

    def to_db_value(self, value: IntEnum | None | int, instance: type[Model] | Model) -> int | None:
        if isinstance(value, IntEnum):
            value = int(value.value)
        if isinstance(value, int):
            value = int(self.enum_type(value))
        self.validate(value)
        return value


IntEnumType = TypeVar("IntEnumType", bound=IntEnum)


def IntEnumField(
    enum_type: type[IntEnumType],
    description: str | None = None,
    **kwargs: Any,
) -> IntEnumType:
    """
    Enum Field

    A field representing an integer enumeration.

    The description of the field is set automatically if not specified to a multiline list of
    "name: value" pairs.

    **Note**: Valid int value of ``enum_type`` is acceptable.

    ``enum_type``:
        The enum class
    ``description``:
        The description of the field. It is set automatically if not specified to a multiline list
        of "name: value" pairs.

    """
    return IntEnumFieldInstance(enum_type, description, **kwargs)  # type: ignore


class CharEnumFieldInstance(CharField):
    def __init__(
        self,
        enum_type: type[Enum],
        description: str | None = None,
        max_length: int = 0,
        **kwargs: Any,
    ) -> None:
        # Automatic description for the field if not specified by the user
        if description is None:
            description = "\n".join([f"{e.name}: {str(e.value)}" for e in enum_type])[:2048]

        # Automatic CharField max_length
        if max_length == 0:
            for item in enum_type:
                item_len = len(str(item.value))
                if item_len > max_length:
                    max_length = item_len

        super().__init__(description=description, max_length=max_length, **kwargs)
        self.enum_type = enum_type

    def to_python_value(self, value: str | None) -> Enum | None:
        return self.enum_type(value) if value is not None else None

    def to_db_value(self, value: Enum | None | str, instance: type[Model] | Model) -> str | None:
        self.validate(value)
        if isinstance(value, Enum):
            return str(value.value)
        if isinstance(value, str):
            return str(self.enum_type(value).value)
        return value


CharEnumType = TypeVar("CharEnumType", bound=Enum)


def CharEnumField(
    enum_type: type[CharEnumType],
    description: str | None = None,
    max_length: int = 0,
    **kwargs: Any,
) -> CharEnumType:
    """
    Char Enum Field

    A field representing a character enumeration.

    **Warning**: If ``max_length`` is not specified or equals to zero, the size of represented
    char fields is automatically detected. So if later you update the enum, you need to update your
    table schema as well.

    **Note**: Valid str value of ``enum_type`` is acceptable.

    ``enum_type``:
        The enum class
    ``description``:
        The description of the field. It is set automatically if not specified to a multiline list
        of "name: value" pairs.
    ``max_length``:
        The length of the created CharField. If it is zero it is automatically detected from
        enum_type.

    """

    return CharEnumFieldInstance(enum_type, description, max_length, **kwargs)  # type: ignore
