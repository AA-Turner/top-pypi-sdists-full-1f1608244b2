from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Optional, Union

from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from advanced_alchemy._listeners import set_async_context
from advanced_alchemy.config.common import (
    GenericAlembicConfig,
    GenericSessionConfig,
    GenericSQLAlchemyConfig,
)
from advanced_alchemy.utils.dataclass import Empty

if TYPE_CHECKING:
    from typing import Callable

    from sqlalchemy.orm import Session

    from advanced_alchemy.utils.dataclass import EmptyType

__all__ = (
    "AlembicAsyncConfig",
    "AsyncSessionConfig",
    "SQLAlchemyAsyncConfig",
)


@dataclass
class AsyncSessionConfig(GenericSessionConfig[AsyncConnection, AsyncEngine, AsyncSession]):
    """SQLAlchemy async session config."""

    sync_session_class: "Optional[Union[type[Session], EmptyType]]" = Empty
    """A :class:`Session <sqlalchemy.orm.Session>` subclass or other callable which will be used to construct the
    :class:`Session <sqlalchemy.orm.Session>` which will be proxied. This parameter may be used to provide custom
    :class:`Session <sqlalchemy.orm.Session>` subclasses. Defaults to the
    :attr:`AsyncSession.sync_session_class <sqlalchemy.ext.asyncio.AsyncSession.sync_session_class>` class-level
    attribute."""


@dataclass
class AlembicAsyncConfig(GenericAlembicConfig):
    """Configuration for an Async Alembic's Config class.

    .. seealso::
        https://alembic.sqlalchemy.org/en/latest/api/config.html
    """


@dataclass
class SQLAlchemyAsyncConfig(GenericSQLAlchemyConfig[AsyncEngine, AsyncSession, async_sessionmaker[AsyncSession]]):
    """Async SQLAlchemy Configuration.

    Note:
        The alembic configuration options are documented in the Alembic documentation.
    """

    create_engine_callable: "Callable[[str], AsyncEngine]" = create_async_engine
    """Callable that creates an :class:`AsyncEngine <sqlalchemy.ext.asyncio.AsyncEngine>` instance or instance of its
    subclass.
    """
    session_config: AsyncSessionConfig = field(default_factory=AsyncSessionConfig)  # pyright: ignore[reportIncompatibleVariableOverride]
    """Configuration options for the :class:`async_sessionmaker<sqlalchemy.ext.asyncio.async_sessionmaker>`."""
    session_maker_class: "type[async_sessionmaker[AsyncSession]]" = async_sessionmaker  # pyright: ignore[reportIncompatibleVariableOverride]
    """Sessionmaker class to use."""
    alembic_config: "AlembicAsyncConfig" = field(default_factory=AlembicAsyncConfig)
    """Configuration for the SQLAlchemy Alembic migrations.

    The configuration options are documented in the Alembic documentation.
    """

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)

    @asynccontextmanager
    async def get_session(
        self,
    ) -> AsyncGenerator[AsyncSession, None]:
        """Get a session from the session maker.

        Yields:
            AsyncGenerator[AsyncSession, None]: An async context manager that yields an AsyncSession.
        """
        session_maker = self.create_session_maker()
        set_async_context(True)  # Set context for standalone usage
        async with session_maker() as session:
            yield session
