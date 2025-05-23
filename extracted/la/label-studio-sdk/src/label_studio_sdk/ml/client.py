# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ml_backend import MlBackend
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.ml_create_request_auth_method import MlCreateRequestAuthMethod
from .types.ml_create_response import MlCreateResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.ml_update_request_auth_method import MlUpdateRequestAuthMethod
from .types.ml_update_response import MlUpdateResponse
from ..errors.internal_server_error import InternalServerError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MlBackend]:
        """

        List all configured Machine Learning (ML) backends for a specific project by ID. For more information about ML backends, see [Machine learning integration](https://labelstud.io/guide/ml).


        You will need to provide the project ID. This can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MlBackend]


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[MlBackend],
                    parse_obj_as(
                        type_=typing.List[MlBackend],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlCreateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlCreateResponse:
        """

        Add an ML backend to a project. For more information about what you need to configure when adding an ML backend, see [Connect the model to Label studio](https://labelstud.io/guide/ml#Connect-the-model-to-Label-Studio).

        <Note>If you are using Docker Compose, you may need to adjust your ML backend URL. See [localhost and Docker containers](https://labelstud.io/guide/ml#localhost-and-Docker-containers).</Note>

        <Note>If you are using files that are located in the cloud, local storage, or uploaded to Label Studio, you must configure your environment variables to allow the ML backend to interact with those files. See [Allow the ML backend to access Label Studio](https://labelstud.io/guide/ml#Allow-the-ML-backend-to-access-Label-Studio-data).</Note>

        Parameters
        ----------
        url : typing.Optional[str]
            ML backend URL

        project : typing.Optional[int]
            Project ID

        is_interactive : typing.Optional[bool]
            Is interactive

        title : typing.Optional[str]
            Title

        description : typing.Optional[str]
            Description

        auth_method : typing.Optional[MlCreateRequestAuthMethod]
            Auth method

        basic_auth_user : typing.Optional[str]
            Basic auth user

        basic_auth_pass : typing.Optional[str]
            Basic auth password

        extra_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Extra parameters

        timeout : typing.Optional[int]
            Response model timeout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlCreateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="POST",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlCreateResponse,
                    parse_obj_as(
                        type_=MlCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> MlBackend:
        """

        Get details about a specific ML backend. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlBackend


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlBackend,
                    parse_obj_as(
                        type_=MlBackend,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Remove an existing ML backend connection. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlUpdateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlUpdateResponse:
        """

        Update the ML backend parameters. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        url : typing.Optional[str]
            ML backend URL

        project : typing.Optional[int]
            Project ID

        is_interactive : typing.Optional[bool]
            Is interactive

        title : typing.Optional[str]
            Title

        description : typing.Optional[str]
            Description

        auth_method : typing.Optional[MlUpdateRequestAuthMethod]
            Auth method

        basic_auth_user : typing.Optional[str]
            Basic auth user

        basic_auth_pass : typing.Optional[str]
            Basic auth password

        extra_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Extra parameters

        timeout : typing.Optional[int]
            Response model timeout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlUpdateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlUpdateResponse,
                    parse_obj_as(
                        type_=MlUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def predict_interactive(
        self,
        id: int,
        *,
        task: int,
        context: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Enable interactive pre-annotations for a specific task.

        ML-assisted labeling with interactive pre-annotations works with image segmentation and object detection tasks using rectangles, ellipses, polygons, brush masks, and keypoints, as well as with HTML and text named entity recognition tasks. Your ML backend must support the type of labeling that you’re performing, recognize the input that you create, and be able to respond with the relevant output for a prediction. For more information, see [Interactive pre-annotations](https://labelstud.io/guide/ml.html#Interactive-pre-annotations).

        Before you can use interactive annotations, it must be enabled for you ML backend connection (`"is_interactive": true`).

        You will need the task ID and the ML backend connection ID. The task ID is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](../tasks/list). The ML backend connection ID is available via [List ML backends](list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        task : int
            ID of task to annotate

        context : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Context for ML model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.predict_interactive(
            id=1,
            task=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/interactive-annotating",
            method="POST",
            json={
                "task": task,
                "context": context,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def train(
        self,
        id: int,
        *,
        use_ground_truth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        After you connect a model to Label Studio as a machine learning backend and annotate at least one task, you can start training the model. Training logs appear in stdout and the console.

        For more information, see [Model training](https://labelstud.io/guide/ml.html#Model-training).

        You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        use_ground_truth : typing.Optional[bool]
            Whether to include ground truth annotations in training

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.train(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/train",
            method="POST",
            json={
                "use_ground_truth": use_ground_truth,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_model_versions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Get available versions of the model. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.list_model_versions(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MlBackend]:
        """

        List all configured Machine Learning (ML) backends for a specific project by ID. For more information about ML backends, see [Machine learning integration](https://labelstud.io/guide/ml).


        You will need to provide the project ID. This can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MlBackend]


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[MlBackend],
                    parse_obj_as(
                        type_=typing.List[MlBackend],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlCreateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlCreateResponse:
        """

        Add an ML backend to a project. For more information about what you need to configure when adding an ML backend, see [Connect the model to Label studio](https://labelstud.io/guide/ml#Connect-the-model-to-Label-Studio).

        <Note>If you are using Docker Compose, you may need to adjust your ML backend URL. See [localhost and Docker containers](https://labelstud.io/guide/ml#localhost-and-Docker-containers).</Note>

        <Note>If you are using files that are located in the cloud, local storage, or uploaded to Label Studio, you must configure your environment variables to allow the ML backend to interact with those files. See [Allow the ML backend to access Label Studio](https://labelstud.io/guide/ml#Allow-the-ML-backend-to-access-Label-Studio-data).</Note>

        Parameters
        ----------
        url : typing.Optional[str]
            ML backend URL

        project : typing.Optional[int]
            Project ID

        is_interactive : typing.Optional[bool]
            Is interactive

        title : typing.Optional[str]
            Title

        description : typing.Optional[str]
            Description

        auth_method : typing.Optional[MlCreateRequestAuthMethod]
            Auth method

        basic_auth_user : typing.Optional[str]
            Basic auth user

        basic_auth_pass : typing.Optional[str]
            Basic auth password

        extra_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Extra parameters

        timeout : typing.Optional[int]
            Response model timeout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlCreateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="POST",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlCreateResponse,
                    parse_obj_as(
                        type_=MlCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> MlBackend:
        """

        Get details about a specific ML backend. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlBackend


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.get(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlBackend,
                    parse_obj_as(
                        type_=MlBackend,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Remove an existing ML backend connection. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: int,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlUpdateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlUpdateResponse:
        """

        Update the ML backend parameters. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        For more information, see [Machine learning integration](https://labelstud.io/guide/ml).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        url : typing.Optional[str]
            ML backend URL

        project : typing.Optional[int]
            Project ID

        is_interactive : typing.Optional[bool]
            Is interactive

        title : typing.Optional[str]
            Title

        description : typing.Optional[str]
            Description

        auth_method : typing.Optional[MlUpdateRequestAuthMethod]
            Auth method

        basic_auth_user : typing.Optional[str]
            Basic auth user

        basic_auth_pass : typing.Optional[str]
            Basic auth password

        extra_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Extra parameters

        timeout : typing.Optional[int]
            Response model timeout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlUpdateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.update(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MlUpdateResponse,
                    parse_obj_as(
                        type_=MlUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def predict_interactive(
        self,
        id: int,
        *,
        task: int,
        context: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Enable interactive pre-annotations for a specific task.

        ML-assisted labeling with interactive pre-annotations works with image segmentation and object detection tasks using rectangles, ellipses, polygons, brush masks, and keypoints, as well as with HTML and text named entity recognition tasks. Your ML backend must support the type of labeling that you’re performing, recognize the input that you create, and be able to respond with the relevant output for a prediction. For more information, see [Interactive pre-annotations](https://labelstud.io/guide/ml.html#Interactive-pre-annotations).

        Before you can use interactive annotations, it must be enabled for you ML backend connection (`"is_interactive": true`).

        You will need the task ID and the ML backend connection ID. The task ID is available from the Label Studio URL when viewing the task, or you can retrieve it programmatically with [Get task list](../tasks/list). The ML backend connection ID is available via [List ML backends](list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        task : int
            ID of task to annotate

        context : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Context for ML model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.predict_interactive(
                id=1,
                task=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/interactive-annotating",
            method="POST",
            json={
                "task": task,
                "context": context,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def train(
        self,
        id: int,
        *,
        use_ground_truth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        After you connect a model to Label Studio as a machine learning backend and annotate at least one task, you can start training the model. Training logs appear in stdout and the console.

        For more information, see [Model training](https://labelstud.io/guide/ml.html#Model-training).

        You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        use_ground_truth : typing.Optional[bool]
            Whether to include ground truth annotations in training

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.train(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/train",
            method="POST",
            json={
                "use_ground_truth": use_ground_truth,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_model_versions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Get available versions of the model. You will need to specify an ID for the backend connection. You can find this using [List ML backends](list).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ml.list_model_versions(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
