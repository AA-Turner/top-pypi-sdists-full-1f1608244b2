from ..api import DAPClient
from ..dap_types import Credentials
from ..integration.database import DatabaseConnection
from ..replicator.sql import SQLReplicator


async def init_db(
    base_url: str,
    credentials: Credentials,
    connection_string: str,
    namespace: str,
    table_names: str,
) -> None:
    db_connection = DatabaseConnection(connection_string)
    async with DAPClient(base_url, credentials) as session:
        sql_replicator = SQLReplicator(session, db_connection)

        await sql_replicator.version_upgrade()

        async def replicate_table_fn(namespace: str, table: str) -> None:
            await sql_replicator.initialize(namespace, table)

        await session.execute_operation_on_tables(
            namespace, table_names, "export", replicate_table_fn
        )
