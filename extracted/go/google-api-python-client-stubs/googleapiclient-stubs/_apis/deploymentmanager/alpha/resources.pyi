import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DeploymentManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CompositeTypesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            compositeType: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            compositeType: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> CompositeTypeHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: CompositeType = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> CompositeTypesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CompositeTypesListResponseHttpRequest,
            previous_response: CompositeTypesListResponse,
        ) -> CompositeTypesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class DeploymentsResource(googleapiclient.discovery.Resource):
        def cancelPreview(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsCancelPreviewRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            deployment: str,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            deployment: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> DeploymentHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            header_bypassBillingFilter: bool = ...,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            header_bypassBillingFilter: bool = ...,
            preview: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> DeploymentsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DeploymentsListResponseHttpRequest,
            previous_response: DeploymentsListResponse,
        ) -> DeploymentsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            header_bypassBillingFilter: bool = ...,
            preview: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def stop(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsStopRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            header_bypassBillingFilter: bool = ...,
            preview: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ManifestsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            deployment: str,
            manifest: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> ManifestHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ManifestsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ManifestsListResponseHttpRequest,
            previous_response: ManifestsListResponse,
        ) -> ManifestsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            operation: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> OperationsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OperationsListResponseHttpRequest,
            previous_response: OperationsListResponse,
        ) -> OperationsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ResourcesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            deployment: str,
            resource: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> ResourceHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ResourcesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ResourcesListResponseHttpRequest,
            previous_response: ResourcesListResponse,
        ) -> ResourcesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class TypeProvidersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            typeProvider: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            typeProvider: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> TypeProviderHttpRequest: ...
        def getType(
            self,
            *,
            project: str,
            typeProvider: str,
            type: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> TypeInfoHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TypeProvider = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> TypeProvidersListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: TypeProvidersListResponseHttpRequest,
            previous_response: TypeProvidersListResponse,
        ) -> TypeProvidersListResponseHttpRequest | None: ...
        def listTypes(
            self,
            *,
            project: str,
            typeProvider: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> TypeProvidersListTypesResponseHttpRequest: ...
        def listTypes_next(
            self,
            previous_request: TypeProvidersListTypesResponseHttpRequest,
            previous_response: TypeProvidersListTypesResponse,
        ) -> TypeProvidersListTypesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class TypesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            type: str,
            header_bypassBillingFilter: bool = ...,
            **kwargs: typing.Any,
        ) -> TypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> TypesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: TypesListResponseHttpRequest,
            previous_response: TypesListResponse,
        ) -> TypesListResponseHttpRequest | None: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def compositeTypes(self) -> CompositeTypesResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def manifests(self) -> ManifestsResource: ...
    def operations(self) -> OperationsResource: ...
    def resources(self) -> ResourcesResource: ...
    def typeProviders(self) -> TypeProvidersResource: ...
    def types(self) -> TypesResource: ...

@typing.type_check_only
class CompositeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CompositeType: ...

@typing.type_check_only
class CompositeTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CompositeTypesListResponse: ...

@typing.type_check_only
class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Deployment: ...

@typing.type_check_only
class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeploymentsListResponse: ...

@typing.type_check_only
class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Manifest: ...

@typing.type_check_only
class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManifestsListResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OperationsListResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Resource: ...

@typing.type_check_only
class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResourcesListResponse: ...

@typing.type_check_only
class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestPermissionsResponse: ...

@typing.type_check_only
class TypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Type: ...

@typing.type_check_only
class TypeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TypeInfo: ...

@typing.type_check_only
class TypeProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TypeProvider: ...

@typing.type_check_only
class TypeProvidersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TypeProvidersListResponse: ...

@typing.type_check_only
class TypeProvidersListTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TypeProvidersListTypesResponse: ...

@typing.type_check_only
class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TypesListResponse: ...
