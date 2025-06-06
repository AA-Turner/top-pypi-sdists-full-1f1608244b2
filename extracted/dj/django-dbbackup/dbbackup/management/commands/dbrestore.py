"""
Restore database.
"""

from django.conf import settings
from django.core.management.base import CommandError
from django.db import connection

from ... import utils
from ...db.base import get_connector
from ...storage import StorageError, get_storage
from ._base import BaseDbBackupCommand, make_option


class Command(BaseDbBackupCommand):
    help = "Restore a database backup from storage, encrypted and/or compressed."
    content_type = "db"
    no_drop = False
    pg_options = ""

    option_list = BaseDbBackupCommand.option_list + (
        make_option("-d", "--database", help="Database to restore"),
        make_option("-i", "--input-filename", help="Specify filename to backup from"),
        make_option(
            "-I", "--input-path", help="Specify path on local filesystem to backup from"
        ),
        make_option(
            "-s",
            "--servername",
            help="If backup file is not specified, filter the "
            "existing ones with the given servername",
        ),
        make_option(
            "-c",
            "--decrypt",
            default=False,
            action="store_true",
            help="Decrypt data before restoring",
        ),
        make_option(
            "-p", "--passphrase", help="Passphrase for decrypt file", default=None
        ),
        make_option(
            "-z",
            "--uncompress",
            action="store_true",
            default=False,
            help="Uncompress gzip data before restoring",
        ),
        make_option(
            "-n",
            "--schema",
            action="append",
            default=[],
            help="Specify schema(s) to restore. Can be used multiple times.",
        ),
        make_option(
            "-r",
            "--no-drop",
            action="store_true",
            default=False,
            help="Don't clean (drop) the database. This only works with mongodb and postgresql.",
        ),
        make_option(
            "--pg-options",
            dest="pg_options",
            default="",
            help="Additional pg_restore options, e.g. '--if-exists --no-owner'. Use quotes.",
        ),
    )

    def handle(self, *args, **options):
        """Django command handler."""
        self.verbosity = int(options.get("verbosity"))
        self.quiet = options.get("quiet")
        self._set_logger_level()

        try:
            connection.close()
            self.filename = options.get("input_filename")
            self.path = options.get("input_path")
            self.servername = options.get("servername")
            self.decrypt = options.get("decrypt")
            self.uncompress = options.get("uncompress")
            self.passphrase = options.get("passphrase")
            self.interactive = options.get("interactive")
            self.input_database_name = options.get("database")
            self.database_name, self.database = self._get_database(
                self.input_database_name
            )
            self.storage = get_storage()
            self.no_drop = options.get("no_drop")
            self.pg_options = options.get("pg_options", "")
            self.schemas = options.get("schema")
            self._restore_backup()
        except StorageError as err:
            raise CommandError(err) from err

    def _get_database(self, database_name: str):
        """Get the database to restore."""
        if not database_name:
            if len(settings.DATABASES) > 1:
                errmsg = (
                    "Because this project contains more than one database, you"
                    " must specify the --database option."
                )
                raise CommandError(errmsg)
            database_name = list(settings.DATABASES.keys())[0]
        if database_name not in settings.DATABASES:
            raise CommandError(f"Database {database_name} does not exist.")
        return database_name, settings.DATABASES[database_name]

    def _restore_backup(self):
        """Restore the specified database."""
        input_filename, input_file = self._get_backup_file(
            database=self.input_database_name, servername=self.servername
        )

        self.logger.info(
            "Restoring backup for database '%s' and server '%s'",
            self.database_name,
            self.servername,
        )

        if self.schemas:
            self.logger.info(f"Restoring schemas: {self.schemas}")

        self.logger.info(f"Restoring: {input_filename}")

        if self.decrypt:
            unencrypted_file, input_filename = utils.unencrypt_file(
                input_file, input_filename, self.passphrase
            )
            input_file.close()
            input_file = unencrypted_file
        if self.uncompress:
            uncompressed_file, input_filename = utils.uncompress_file(
                input_file, input_filename
            )
            input_file.close()
            input_file = uncompressed_file

        self.logger.info("Restore tempfile created: %s", utils.handle_size(input_file))
        if self.interactive:
            self._ask_confirmation()

        input_file.seek(0)
        self.connector = get_connector(self.database_name)
        if self.schemas:
            self.connector.schemas = self.schemas
        self.connector.drop = not self.no_drop
        self.connector.pg_options = self.pg_options
        self.connector.restore_dump(input_file)
