import json
import pandas as pd
from google.cloud.bigquery.table import RowIterator
from google.api_core.exceptions import BadRequest
from typing import Optional, Dict, Union, List
from google.cloud import bigquery
from google.oauth2 import service_account, credentials
from google.auth import load_credentials_from_file
from pathlib import Path
from functools import cached_property
from shipyard_templates import GoogleDatabase, ShipyardLogger, ExitCodeException
from shipyard_bigquery.utils.exceptions import (
    DownloadToGcsError,
    FetchError,
    InvalidSchema,
    QueryError,
    SchemaFormatError,
    SchemaValidationError,
    TempTableCreationError,
)

logger = ShipyardLogger.get_logger()


class BigQueryClient(GoogleDatabase):
    def __init__(
        self,
        service_account: Optional[str] = None,
        access_token: Optional[str] = None,
        project_id: Optional[str] = None,
        location: Optional[str] = None,
    ) -> None:
        if not service_account and not access_token:
            raise ValueError("Either service account or access token must be provided")
        self.service_account = service_account
        self.access_token = access_token
        self.project_id = project_id or None
        self.location = location or None
        super().__init__(service_account, access_token=access_token)

    @cached_property
    def credentials(self):
        if self.access_token:
            return self._credentials_from_access_token()
        elif self.service_account:
            try:
                if self.is_existing_file_path(self.service_account):
                    return self._credentials_from_file()
                elif self._is_json_string(self.service_account):
                    return self._credentials_from_string()
            except json.JSONDecoder:
                raise ExitCodeException(
                    "Invalid JSON string provided for service account",
                    self.EXIT_CODE_INVALID_CREDENTIALS,
                )
            except FileNotFoundError:
                raise ExitCodeException(
                    f"Service account file not found: {self.service_account}",
                    self.EXIT_CODE_INVALID_CREDENTIALS,
                )
        else:
            raise ExitCodeException(
                "Either service account or access token must be provided",
                self.EXIT_CODE_INVALID_CREDENTIALS,
            )

    def _credentials_from_file(self):
        logger.debug(f"Loading credentials from file: {self.service_account}")
        file_path = Path(self.service_account).resolve()
        return load_credentials_from_file(str(file_path))[0]

    def _credentials_from_string(self):
        logger.debug("Loading credentials from string")
        return service_account.Credentials.from_service_account_info(
            json.loads(self.service_account)
        )

    def _credentials_from_access_token(self):
        logger.debug("Loading credentials from access token")
        return credentials.Credentials(
            self.access_token,
            scopes=[
                "https://www.googleapis.com/auth/bigquery",
                "https://www.googleapis.com/auth/bigquery.insertdata",
                "https://www.googleapis.com/auth/devstorage.read_write",
            ],
        )

    @staticmethod
    def is_existing_file_path(string_value: str) -> bool:
        """Checks if the input string is a file path

        Args:
            string_value: The input string to check

        Returns: True if the string is a file path, False otherwise

        """
        return len(string_value) > 4096 and Path(string_value).is_file()

    @staticmethod
    def _is_json_string(string_value: str) -> bool:
        """Checks if the input string is a JSON string
        Args:
            string_value: The input string to check
        Returns: True if the string is a JSON string, False otherwise
        """
        string_value = string_value.strip()
        return bool(
            string_value and string_value[0] in "{[" and string_value[-1] in "}]"
        )

    @property
    def email(self):
        if self.service_account:
            return self.credentials.service_account_email
        else:
            return self.credentials.signer_email

    @cached_property
    def conn(self):
        """Establishes a connection to BigQuery

        Returns: The connection object

        """
        return bigquery.Client(
            credentials=self.credentials,
            project=self.project_id,
            location=self.location,
        )

    def connect(self):
        try:
            self.conn
            return 0
        except Exception as e:
            logger.authtest(f"Error in connecting to BigQuery: {e}")
            return 1

    def execute_query(self, query: str) -> RowIterator:
        """Executes a query and returns the results

        Args:
            query: The query to execute

        Returns: The query results as a pandas dataframe

        """
        try:
            query_job = self.conn.query(query)
            results = query_job.result()
        except Exception as e:
            raise QueryError(f"Error in executing query: {str(e)}")
        else:
            return results

    def fetch(self, query: str) -> pd.DataFrame:
        """Returns the results of a query to a pandas dataframe

        Args:
            query: The query to fetch

        Returns: The query results as a pandas dataframe

        """
        try:
            df = self.conn.query(query).to_dataframe()
        except Exception as e:
            raise FetchError(f"Error in fetching query: {str(e)}")
        else:
            return df

    def upload(
        self,
        file: str,
        dataset: str,
        table: str,
        upload_type: str,
        skip_header_rows: Optional[int] = None,
        schema: Optional[Union[List[List], Dict[str, str]]] = None,
        quoted_newline: bool = False,
    ):
        """Upload a file to a table in BigQuery
        Args:
            file: The file to load
            dataset: The name of the dataset in BigQuery to upload to
            table: The name of the table to write to
            upload_type: Whether to append to or replace the data. Choices are 'overwrite' and 'append'
            schema: The optional schema of the table to be loaded
            skip_header_rows: Whether to skip the header row
            quoted_newline: Whether newline characters should be quoted
        """
        try:
            dataset_ref = bigquery.DatasetReference(
                project=self.conn.project, dataset_id=dataset
            )
            table_ref = bigquery.TableReference(dataset_ref=dataset_ref, table_id=table)
            job_config = bigquery.LoadJobConfig()

            if upload_type == "overwrite":
                job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
            else:
                job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.autodetect = True  # infer the schema
            if skip_header_rows:
                job_config.skip_leading_rows = skip_header_rows
            if schema:
                logger.debug(f"Schema is {schema}")
                job_config.autodetect = False
                job_config.schema = self._format_schema(schema)
            if quoted_newline:
                job_config.allow_quoted_newlines = True
            with open(file, "rb") as source_file:
                job = self.conn.load_table_from_file(
                    source_file, table_ref, job_config=job_config
                )
            job.result()
        except SchemaValidationError:
            raise
        except SchemaFormatError:
            raise
        except InvalidSchema:
            raise
        except BadRequest as br:
            logger.debug(f"The status code is: {br.code}")
            logger.debug(f"The listed errors are {br.errors}")
            raise ExitCodeException(
                f"Bad Request when trying to upload to BigQuery. Message from the API reads: {str(br.message)}",
                exit_code=self.EXIT_CODE_INVALID_UPLOAD_VALUE,
            )

        except Exception as e:
            raise ExitCodeException(
                f"An error occurred when attempting to upload to BigQuery: {str(e)}",
                self.EXIT_CODE_INVALID_UPLOAD_VALUE,
            )

    def download_to_gcs(self, query: str, bucket_name: str, path: Optional[str] = None):
        try:
            project_id, dataset_id, table_id, location = self._create_temp_table(query)
            dataset_ref = bigquery.DatasetReference(
                project=project_id, dataset_id=dataset_id
            )
            table_ref = dataset_ref.table(table_id)
            dest_uri = f"gs://{bucket_name}/{path}"
            self.conn.extract_table(table_ref, dest_uri, location=location).result()
        except TempTableCreationError as te:
            raise DownloadToGcsError(
                f"Error in executing the query and storing in a temp file: {te.message}"
            )
        except Exception as e:
            raise DownloadToGcsError(f"Error downloading file to GCS: {str(e)}")

    @staticmethod
    def _format_schema(
        schema: Union[List[List[str]], Dict[str, List[str]]],
    ) -> List[bigquery.SchemaField]:
        """Helper function to format the schema appropriately for BigQuery

        Args:
            schema: The representation inputted as either a list of lists (for backwards compatibility) or preferably JSON

        Returns: The formatted schema

        """
        formatted_schema = []
        try:
            for item in schema:
                if isinstance(item, list):
                    formatted_schema.append(bigquery.SchemaField(*item))
                elif isinstance(item, dict):
                    formatted_schema.append(bigquery.SchemaField.from_api_repr(item))
                else:
                    raise InvalidSchema(
                        "Format of inputted schema is incorrect, this should preferably be a JSON representation or a List of Lists. For additional information and examples, visit https://cloud.google.com/bigquery/docs/schemas#specifying_a_json_schema_file"
                    )
        except Exception as e:
            raise SchemaFormatError(
                f"Error in preparing the inputted schema to the appropriate BigQuery format: {str(e)}"
            )
        else:
            logger.debug(f"Formatted schema is {formatted_schema}")
            return formatted_schema

    def _create_temp_table(self, query: str):
        """Helper function to execute a query and store the results in a temporary table

        Args:
            query: The query to execute

        Returns: The metadata of the temp table

        """
        try:
            data = self.conn.query(query)
            data.result()
            destination = data.destination
            return (
                destination.project,
                destination.dataset_id,
                destination.table_id,
                destination.location,
            )
        except Exception as e:
            raise TempTableCreationError(
                f"Error in storing query results in temp table: {str(e)}"
            )
