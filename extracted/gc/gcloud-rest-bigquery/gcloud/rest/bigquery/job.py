from typing import Any
from typing import AnyStr
from typing import Dict
from typing import IO
from typing import Optional
from typing import Union

from gcloud.rest.auth import BUILD_GCLOUD_REST  # pylint: disable=no-name-in-module
from gcloud.rest.auth import Token  # pylint: disable=no-name-in-module

from .bigquery import BigqueryBase
from .bigquery import Disposition

# Selectively load libraries based on the package
if BUILD_GCLOUD_REST:
    from requests import Session
else:
    from aiohttp import ClientSession as Session  # type: ignore[assignment]


class Job(BigqueryBase):
    def __init__(
            self, job_id: Optional[str] = None, project: Optional[str] = None,
            service_file: Optional[Union[str, IO[AnyStr]]] = None,
            session: Optional[Session] = None, token: Optional[Token] = None,
            api_root: Optional[str] = None,
            location: Optional[str] = None,
    ) -> None:
        self.job_id = job_id
        self.location = location
        super().__init__(
            project=project, service_file=service_file,
            session=session, token=token, api_root=api_root,
        )

    @staticmethod
    def _make_query_body(
            query: str,
            write_disposition: Disposition,
            use_query_cache: bool,
            dry_run: bool, use_legacy_sql: bool,
            destination_table: Optional[Any],
    ) -> Dict[str, Any]:
        return {
            'configuration': {
                'query': {
                    'query': query,
                    'writeDisposition': write_disposition.value,
                    'destinationTable': {
                        'projectId': destination_table.project,
                        'datasetId': destination_table.dataset_name,
                        'tableId': destination_table.table_name,
                    } if destination_table else destination_table,
                    'useQueryCache': use_query_cache,
                    'useLegacySql': use_legacy_sql,
                },
                'dryRun': dry_run,
            },
        }

    def _config_params(
        self, params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        params = params.copy() if params else {}
        if self.location:
            params['location'] = params.get('location', self.location)
        return params

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get
    def get_job(
        self, session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Get the specified job resource by job ID."""

        project = self.project()
        url = f'{self._api_root}/projects/{project}/jobs/{self.job_id}'

        return self._get_url(url, session, timeout,
                                   self._config_params())

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults
    def get_query_results(
        self, session: Optional[Session] = None,
        timeout: int = 60,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get the specified jobQueryResults by job ID."""

        project = self.project()
        url = f'{self._api_root}/projects/{project}/queries/{self.job_id}'

        return self._get_url(url, session, timeout,
                                   self._config_params(params))

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel
    def cancel(
        self, session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Cancel the specified job by job ID."""

        project = self.project()
        url = (
            f'{self._api_root}/projects/{project}/jobs/{self.job_id}'
            '/cancel'
        )

        return self._post_json(url, {}, session, timeout,
                                     self._config_params())

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
    def query(
        self, query_request: Dict[str, Any],
        session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Runs a query synchronously and returns query results if completes
        within a specified timeout."""
        project = self.project()
        url = f'{self._api_root}/projects/{project}/queries'

        return self._post_json(url, query_request, session, timeout)

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert
    def insert(
        self, job: Dict[str, Any],
        session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Insert a new asynchronous job."""
        project = self.project()
        url = f'{self._api_root}/projects/{project}/jobs'

        response = self._post_json(url, job, session, timeout)
        if response['jobReference'].get('jobId'):
            self.job_id = response['jobReference']['jobId']
        return response

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert
    # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationQuery
    def insert_via_query(
            self, query: str, session: Optional[Session] = None,
            write_disposition: Disposition = Disposition.WRITE_EMPTY,
            timeout: int = 60, use_query_cache: bool = True,
            dry_run: bool = False, use_legacy_sql: bool = True,
            destination_table: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """Create table as a result of the query"""
        project = self.project()
        url = f'{self._api_root}/projects/{project}/jobs'

        body = self._make_query_body(
            query=query,
            write_disposition=write_disposition,
            use_query_cache=use_query_cache,
            dry_run=dry_run,
            use_legacy_sql=use_legacy_sql,
            destination_table=destination_table,
        )
        response = self._post_json(url, body, session, timeout)
        if not dry_run:
            self.job_id = response['jobReference']['jobId']
        return response

    def result(
        self,
        session: Optional[Session] = None,
    ) -> Dict[str, Any]:
        data = self.get_job(session)
        status = data.get('status', {})
        if status.get('state') == 'DONE':
            if 'errorResult' in status:
                raise Exception('Job finished with errors', status['errors'])
            return data

        raise OSError('Job results are still pending')

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/delete
    def delete(
        self, session: Optional[Session] = None,
        job_id: Optional[str] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Delete the specified job by job ID."""
        project = self.project()
        job_id = job_id or self.job_id
        url = f'{self._api_root}/projects/{project}/jobs/{job_id}/delete'

        return self._delete(url, session, timeout, self._config_params())
