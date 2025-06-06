# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.http_response import HttpResponse
from ..types.create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper
from ..core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawMobileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateMobileAuthorizationCodeResponse]:
        """
        __Note:__ This endpoint is used by the deprecated Reader SDK.
        Developers should update their integration to use the [Mobile Payments SDK](https://developer.squareup.com/docs/mobile-payments-sdk), which includes its own authorization methods.

        Generates code to authorize a mobile application to connect to a Square card reader.

        Authorization codes are one-time-use codes and expire 60 minutes after being issued.

        The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID that the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMobileAuthorizationCodeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "mobile/authorization-code",
            method="POST",
            json={
                "location_id": location_id,
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
                    CreateMobileAuthorizationCodeResponse,
                    construct_type(
                        type_=CreateMobileAuthorizationCodeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawMobileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateMobileAuthorizationCodeResponse]:
        """
        __Note:__ This endpoint is used by the deprecated Reader SDK.
        Developers should update their integration to use the [Mobile Payments SDK](https://developer.squareup.com/docs/mobile-payments-sdk), which includes its own authorization methods.

        Generates code to authorize a mobile application to connect to a Square card reader.

        Authorization codes are one-time-use codes and expire 60 minutes after being issued.

        The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID that the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMobileAuthorizationCodeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mobile/authorization-code",
            method="POST",
            json={
                "location_id": location_id,
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
                    CreateMobileAuthorizationCodeResponse,
                    construct_type(
                        type_=CreateMobileAuthorizationCodeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
