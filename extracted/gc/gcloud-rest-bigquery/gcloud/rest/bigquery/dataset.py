from typing import Any
from typing import AnyStr
from typing import Dict
from typing import IO
from typing import Optional
from typing import Union

from gcloud.rest.auth import BUILD_GCLOUD_REST  # pylint: disable=no-name-in-module
from gcloud.rest.auth import Token  # pylint: disable=no-name-in-module

from .bigquery import BigqueryBase

# Selectively load libraries based on the package
if BUILD_GCLOUD_REST:
    from requests import Session
else:
    from aiohttp import ClientSession as Session  # type: ignore[assignment]


class Dataset(BigqueryBase):
    def __init__(
            self, dataset_name: Optional[str] = None,
            project: Optional[str] = None,
            service_file: Optional[Union[str, IO[AnyStr]]] = None,
            session: Optional[Session] = None, token: Optional[Token] = None,
            api_root: Optional[str] = None,
    ) -> None:
        self.dataset_name = dataset_name
        super().__init__(
            project=project, service_file=service_file,
            session=session, token=token, api_root=api_root,
        )

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/list
    def list_tables(
            self, session: Optional[Session] = None,
            timeout: int = 60,
            params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """List tables in a dataset."""
        project = self.project()
        if not self.dataset_name:
            raise ValueError(
                'could not determine dataset,'
                ' please set it manually',
            )

        url = (
            f'{self._api_root}/projects/{project}/datasets/'
            f'{self.dataset_name}/tables'
        )
        return self._get_url(url, session, timeout, params=params)

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/list
    def list_datasets(
            self, session: Optional[Session] = None,
            timeout: int = 60,
            params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """List datasets in current project."""
        project = self.project()

        url = f'{self._api_root}/projects/{project}/datasets'
        return self._get_url(url, session, timeout, params=params)

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/get
    def get(
        self, session: Optional[Session] = None,
        timeout: int = 60,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get a specific dataset in current project."""
        project = self.project()
        if not self.dataset_name:
            raise ValueError(
                'could not determine dataset,'
                ' please set it manually',
            )

        url = (
            f'{self._api_root}/projects/{project}/datasets/'
            f'{self.dataset_name}'
        )
        return self._get_url(url, session, timeout, params=params)

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/insert
    def insert(
        self, dataset: Dict[str, Any],
        session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Create datasets in current project."""
        project = self.project()

        url = f'{self._api_root}/projects/{project}/datasets'
        return self._post_json(url, dataset, session, timeout)

    # https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/delete
    def delete(
        self, dataset_name: Optional[str] = None,
        session: Optional[Session] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """Delete datasets in current project."""
        project = self.project()
        dataset_name = dataset_name or self.dataset_name

        url = f'{self._api_root}/projects/{project}/datasets/{dataset_name}'
        return self._delete(url, session, timeout)
