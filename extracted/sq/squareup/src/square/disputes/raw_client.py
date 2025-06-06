# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.http_response import HttpResponse
from ..types.get_dispute_response import GetDisputeResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.accept_dispute_response import AcceptDisputeResponse
from ..requests.create_dispute_evidence_file_request import CreateDisputeEvidenceFileRequestParams
from .. import core
from ..types.create_dispute_evidence_file_response import CreateDisputeEvidenceFileResponse
import json
from ..types.dispute_evidence_type import DisputeEvidenceType
from ..types.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from ..types.submit_evidence_response import SubmitEvidenceResponse
from ..core.client_wrapper import AsyncClientWrapper
from ..core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawDisputesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDisputeResponse]:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDisputeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDisputeResponse,
                    construct_type(
                        type_=GetDisputeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def accept(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AcceptDisputeResponse]:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AcceptDisputeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AcceptDisputeResponse,
                    construct_type(
                        type_=AcceptDisputeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_evidence_file(
        self,
        dispute_id: str,
        *,
        request: typing.Optional[CreateDisputeEvidenceFileRequestParams] = OMIT,
        image_file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDisputeEvidenceFileResponse]:
        """
        Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP
        multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to upload evidence.

        request : typing.Optional[CreateDisputeEvidenceFileRequestParams]

        image_file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDisputeEvidenceFileResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-files",
            method="POST",
            data={},
            files={
                **(
                    {"request": (None, json.dumps(jsonable_encoder(request)), "application/json; charset=utf-8")}
                    if request is not OMIT
                    else {}
                ),
                **(
                    {"image_file": core.with_content_type(file=image_file, default_content_type="image/jpeg")}
                    if image_file is not None
                    else {}
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDisputeEvidenceFileResponse,
                    construct_type(
                        type_=CreateDisputeEvidenceFileResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_evidence_text(
        self,
        dispute_id: str,
        *,
        idempotency_key: str,
        evidence_text: str,
        evidence_type: typing.Optional[DisputeEvidenceType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDisputeEvidenceTextResponse]:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to upload evidence.

        idempotency_key : str
            A unique key identifying the request. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_text : str
            The evidence string.

        evidence_type : typing.Optional[DisputeEvidenceType]
            The type of evidence you are uploading.
            See [DisputeEvidenceType](#type-disputeevidencetype) for possible values

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDisputeEvidenceTextResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-text",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "evidence_type": evidence_type,
                "evidence_text": evidence_text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDisputeEvidenceTextResponse,
                    construct_type(
                        type_=CreateDisputeEvidenceTextResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubmitEvidenceResponse]:
        """
        Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded
        using the [CreateDisputeEvidenceFile](api-endpoint:Disputes-CreateDisputeEvidenceFile) and
        [CreateDisputeEvidenceText](api-endpoint:Disputes-CreateDisputeEvidenceText) endpoints and
        evidence automatically provided by Square, when available. Evidence cannot be removed from
        a dispute after submission.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to submit evidence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubmitEvidenceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/submit-evidence",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubmitEvidenceResponse,
                    construct_type(
                        type_=SubmitEvidenceResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawDisputesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDisputeResponse]:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDisputeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDisputeResponse,
                    construct_type(
                        type_=GetDisputeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def accept(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AcceptDisputeResponse]:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AcceptDisputeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AcceptDisputeResponse,
                    construct_type(
                        type_=AcceptDisputeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_evidence_file(
        self,
        dispute_id: str,
        *,
        request: typing.Optional[CreateDisputeEvidenceFileRequestParams] = OMIT,
        image_file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDisputeEvidenceFileResponse]:
        """
        Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP
        multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to upload evidence.

        request : typing.Optional[CreateDisputeEvidenceFileRequestParams]

        image_file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDisputeEvidenceFileResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-files",
            method="POST",
            data={},
            files={
                **(
                    {"request": (None, json.dumps(jsonable_encoder(request)), "application/json; charset=utf-8")}
                    if request is not OMIT
                    else {}
                ),
                **(
                    {"image_file": core.with_content_type(file=image_file, default_content_type="image/jpeg")}
                    if image_file is not None
                    else {}
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDisputeEvidenceFileResponse,
                    construct_type(
                        type_=CreateDisputeEvidenceFileResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_evidence_text(
        self,
        dispute_id: str,
        *,
        idempotency_key: str,
        evidence_text: str,
        evidence_type: typing.Optional[DisputeEvidenceType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDisputeEvidenceTextResponse]:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to upload evidence.

        idempotency_key : str
            A unique key identifying the request. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_text : str
            The evidence string.

        evidence_type : typing.Optional[DisputeEvidenceType]
            The type of evidence you are uploading.
            See [DisputeEvidenceType](#type-disputeevidencetype) for possible values

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDisputeEvidenceTextResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-text",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "evidence_type": evidence_type,
                "evidence_text": evidence_text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDisputeEvidenceTextResponse,
                    construct_type(
                        type_=CreateDisputeEvidenceTextResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubmitEvidenceResponse]:
        """
        Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded
        using the [CreateDisputeEvidenceFile](api-endpoint:Disputes-CreateDisputeEvidenceFile) and
        [CreateDisputeEvidenceText](api-endpoint:Disputes-CreateDisputeEvidenceText) endpoints and
        evidence automatically provided by Square, when available. Evidence cannot be removed from
        a dispute after submission.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute for which you want to submit evidence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubmitEvidenceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/submit-evidence",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubmitEvidenceResponse,
                    construct_type(
                        type_=SubmitEvidenceResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
