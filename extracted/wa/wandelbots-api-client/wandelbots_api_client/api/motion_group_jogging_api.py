# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from furl import furl
import json
import humps
import re
import warnings
import websockets
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, AsyncGenerator, Callable, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from urllib.parse import quote

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from wandelbots_api_client.models.direction_jogging_request import DirectionJoggingRequest
from wandelbots_api_client.models.jogging_response import JoggingResponse
from wandelbots_api_client.models.jogging_service_capabilities import JoggingServiceCapabilities
from wandelbots_api_client.models.joint_jogging_request import JointJoggingRequest

from wandelbots_api_client.api_client import ApiClient, RequestSerialized
from wandelbots_api_client.api_response import ApiResponse
from wandelbots_api_client.rest import RESTResponseType

class MotionGroupJoggingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def direction_jogging(self, cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")], client_request_generator: Callable[[AsyncGenerator[JoggingResponse, None]], AsyncGenerator[DirectionJoggingRequest, None]]) -> None:  # noqa: E501
        """Stream Cartesian  # noqa: E501

        Move TCP along/around a specified direction vector with a specified velocity via a websocket.  The purpose of a direction jogging motion is to move a device in exactly one direction with a specified maximum velocity. The sign of the velocity determines the direction of the movement: Positive [+] or Negative [-]. The velocity is given in [mm/s]. In contrast to a planned motion, a jogging motion can be changed dynamically while the motion group is in motion.  Only one single client at a time can jog a particular motion group. If another client tries to jog the same motion group at the same time, the second call will fail.  The movement of the motion group will start as soon as: * the motion group is not in motion * the websocket connection is established * the first request has been sent  As long as the jogging motion is ongoing, responses will be sent continuously and contain the current state of the motion group. The responses will be sent with the specified rate according to the *response_rate* parameter of the initial websocket request. While in motion, the desired direction and velocity can be changed by sending a new request to the same websocket. The motion and sending of the replies will stop when: * a [stopJogging](stopJogging) request was received, processed, and the movement stopped   The motion group state will be published in the original command stream until the motion group has stopped. * the client cancels the stream (not recommended, because final stopping position will not be returned from the stream)  When a physical limit (e.g. workspace boundary) is reached, the motion group will stop moving in the desired direction. The stream, howewer, will continue to send the state until the client cancels the stream or sends the [stopJogging](stopJogging) request.  Singularities are avoided during a jogging motion. This avoidance can result in deviations from the specified direction. The amount of deviation depends on the robot type and current velocity. These mechanisms can lead to a small deviation from the specified direction. The size of deviation is depending on robot type and current velocity.   **Usage example:**  1. Open a websocket via python and start the jogging motion: ```bash > python -m websockets \"ws://<IP of Wandelbots NOVA API>/api/v1/cells/<your cell id>/motion-groups/move-tcp\" ``` 2. Send the following message to the server to move current TCP 2 parts up in z direction and one part in negative y direction with 0.2 mm/s along the specified direction vector: ```json {   \"motion_group\": \"<your motion group id>\",   \"position_direction\": {     \"y\": -0.5,     \"z\": 1   },   \"rotation_direction\": {},   \"position_velocity\": 0.2,   \"response_rate\": 500 } ``` The NOVA API clients support jogging motions without the need to manually open a websocket.  > **NOTE** > > If the jogging movement is stopped immediately, ensure that > > - A websocket connection is established. Websockets can be kept open until the robot's movement is done as opposed to a simple HTTP GET request. > > - The motion group is not in motion by another jogging movement or a planned movement.   > **NOTE** > > If the robot does not move, ensure that > > - The joint velocity values are not zero, > > - The motion group is not in a state where it cannot move further (e.g. joint limit reached).  > **NOTE** > > If the specified velocities are higher than the maximum allowed by the robot controller, the motion group will move with the maximum allowed velocities.   # noqa: E501
        :param client_request_generator: An AsyncGenerator that yields request of type DirectionJoggingRequest and takes an AsyncGenerator of JoggingResponse as an input argument (required)
        :info All responses from the server will be yielded to client_request_generator through the (AsyncGenerator[JoggingResponse, None])
        :type AsyncGenerator[DirectionJoggingRequest, None]
        """
        def format_path_parameters(path):
            # Find all substrings that are enclosed in brackets
            bracket_contents = re.findall(r'\{(.*?)\}', path)

            # For each found substring, alter it to match the python variable name
            for content in bracket_contents:
                content = "{" + content + "}"
                modified_content = humps.dekebabize(content)
                path = path.replace(content, modified_content)

            return path

        async def iterate_responses(ws) -> AsyncGenerator[JoggingResponse, None]:
            async for response in ws:
                if "Cancelled on the server side" in response:
                    break
                response_data = json.loads(response)
                if "result" not in response_data:
                    raise Exception(response_data)
                yield JoggingResponse.from_dict(response_data["result"])

        path = format_path_parameters("/cells/{cell}/motion-groups/move-tcp")
        path = path.format(cell=cell,)

        headers = websockets.Headers()
        tmp_host = self.api_client.configuration.host
        if self.api_client.configuration.host.startswith("https://"):
            # Basic Auth
            if self.api_client.configuration.username:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{self.api_client.configuration.username}:{self.api_client.configuration.password}@{tmp_host}"

            # OAuth2
            elif self.api_client.configuration.access_token:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{tmp_host}"
                headers = websockets.Headers([
                    ("Authorization", f"Bearer {self.api_client.configuration.access_token}")
                ])
        else:
            tmp_host = tmp_host.replace("http://", "ws://")

        full_url = furl(tmp_host + path)

        async with websockets.connect(full_url.url, open_timeout=10, additional_headers=headers) as websocket:
            async for request in client_request_generator(iterate_responses(websocket)):
                await websocket.send(request.to_json())


    @validate_call
    async def get_jogging_capabilities(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> JoggingServiceCapabilities:
        """Capabilities

        Shows the options the motion group offers in regard to jogging. Some motion groups may not provide all information services, e.g. it is physically not possible to move a one-axis-turntable in a linear way.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_jogging_capabilities_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "JoggingServiceCapabilities",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_jogging_capabilities_with_http_info(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[JoggingServiceCapabilities]:
        """Capabilities

        Shows the options the motion group offers in regard to jogging. Some motion groups may not provide all information services, e.g. it is physically not possible to move a one-axis-turntable in a linear way.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_jogging_capabilities_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "JoggingServiceCapabilities",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_jogging_capabilities_without_preload_content(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Capabilities

        Shows the options the motion group offers in regard to jogging. Some motion groups may not provide all information services, e.g. it is physically not possible to move a one-axis-turntable in a linear way.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_jogging_capabilities_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "JoggingServiceCapabilities",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_jogging_capabilities_serialize(
        self,
        cell,
        motion_group,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cell is not None:
            _path_params['cell'] = cell
        if motion_group is not None:
            _path_params['motion-group'] = motion_group
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'BasicAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/cells/{cell}/motion-groups/{motion-group}/jogging-capabilities',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



    @validate_call
    async def joint_jogging(self, cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")], client_request_generator: Callable[[AsyncGenerator[JoggingResponse, None]], AsyncGenerator[JointJoggingRequest, None]]) -> None:  # noqa: E501
        """Stream Joints  # noqa: E501

        Move one or more joints of a motion group with specified velocities via a websocket.  The purpose of a joint jogging motion is to maneuver a motion group in one or more joints with a specified velocity for each joint. The sign of the velocity determines the direction of the joint movement. The velocity is given in [rad/s]. In contrast to a planned motion, a jogging motion can be changed dynamically while the motion group is in motion.  Only one single client at a time can jog a particular motion group. If another client tries to jog the same motion group at the same time, the second call will fail.  The movement of the motion group will start as soon as: * the motion group is not in motion * the websocket connection is established * the first request has been sent  As long as the jogging motion is ongoing, responses will be sent continuously and contain the current state of the motion group. The responses will be sent with the specified rate according to the *response_rate* parameter of the initial websocket request. While in motion, the desired joint velocity can be changed by sending a new request to the same websocket. The motion and sending of the replies will stop when: * a [stopJogging](stopJogging) request was received, processed, and the movement stopped   Motion group state will be published in the original command stream until the motion group has fully stopped. * the client cancels the stream (not recommended, because final stopping position will not be returned from the stream)  When a physical limit (e.g. joint limit) is reached, the motion group will stop moving in the desired direction. The stream, howewer, will continue to send the state until the client cancels the stream or sends the [stopJogging](stopJogging) request.  **Usage example:**  1. Open a websocket via python and start the jogging motion: ```bash > python -m websockets \"ws://<IP of Wandelbots NOVA API>/api/v1/cells/<your cell id>/motion-groups/move-joint\" ``` 2. Send the following message to move with a velocity of 0.1 rad/s (negative) for joint 5 and 0.2 rad/s for joint 6: ```json {   \"motion_group\": \"<your motion group id>\",   \"joint_velocities\": [0, 0, 0, 0, -0.1, 0.2],   \"response_rate\": 500 } ``` The provided NOVA API clients also natively support jogging motions, without the need to manually open a websocket.  > **NOTE** > > If the jogging movement is stopped immediately, ensure that > > - A websocket connection is established. Websockets can be kept open until the robot's movement is done as opposed to a simple HTTP GET request. > > - The motion group is not in motion by another jogging movement or a planned movement.   > **NOTE** > > If the robot does not move, ensure that > > - The joint velocity values are not zero, > > - The motion group is not in a state where it cannot move further (e.g. joint limit reached).  > **NOTE** > > If the specified velocities are higher than the maximum allowed by the robot controller, the motion group will move with the maximum allowed velocities.   # noqa: E501
        :param client_request_generator: An AsyncGenerator that yields request of type JointJoggingRequest and takes an AsyncGenerator of JoggingResponse as an input argument (required)
        :info All responses from the server will be yielded to client_request_generator through the (AsyncGenerator[JoggingResponse, None])
        :type AsyncGenerator[JointJoggingRequest, None]
        """
        def format_path_parameters(path):
            # Find all substrings that are enclosed in brackets
            bracket_contents = re.findall(r'\{(.*?)\}', path)

            # For each found substring, alter it to match the python variable name
            for content in bracket_contents:
                content = "{" + content + "}"
                modified_content = humps.dekebabize(content)
                path = path.replace(content, modified_content)

            return path

        async def iterate_responses(ws) -> AsyncGenerator[JoggingResponse, None]:
            async for response in ws:
                if "Cancelled on the server side" in response:
                    break
                response_data = json.loads(response)
                if "result" not in response_data:
                    raise Exception(response_data)
                yield JoggingResponse.from_dict(response_data["result"])

        path = format_path_parameters("/cells/{cell}/motion-groups/move-joint")
        path = path.format(cell=cell,)

        headers = websockets.Headers()
        tmp_host = self.api_client.configuration.host
        if self.api_client.configuration.host.startswith("https://"):
            # Basic Auth
            if self.api_client.configuration.username:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{self.api_client.configuration.username}:{self.api_client.configuration.password}@{tmp_host}"

            # OAuth2
            elif self.api_client.configuration.access_token:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{tmp_host}"
                headers = websockets.Headers([
                    ("Authorization", f"Bearer {self.api_client.configuration.access_token}")
                ])
        else:
            tmp_host = tmp_host.replace("http://", "ws://")

        full_url = furl(tmp_host + path)

        async with websockets.connect(full_url.url, open_timeout=10, additional_headers=headers) as websocket:
            async for request in client_request_generator(iterate_responses(websocket)):
                await websocket.send(request.to_json())


    @validate_call
    async def stop_jogging(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Stop

        Stops an ongoing jogging movement as fast as possible. Until the motion group reaches standstill, it decelerates and keeps the last specified direction.  This call will immediately return even if the deceleration is still in progress. After a stop request has been received, no further updates to the ongoing jogging movement are possible.  State responses will be sent via the jogging stream until the motion group reaches standstill. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_jogging_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def stop_jogging_with_http_info(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Stop

        Stops an ongoing jogging movement as fast as possible. Until the motion group reaches standstill, it decelerates and keeps the last specified direction.  This call will immediately return even if the deceleration is still in progress. After a stop request has been received, no further updates to the ongoing jogging movement are possible.  State responses will be sent via the jogging stream until the motion group reaches standstill. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_jogging_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def stop_jogging_without_preload_content(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        motion_group: Annotated[StrictStr, Field(description="The motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Stop

        Stops an ongoing jogging movement as fast as possible. Until the motion group reaches standstill, it decelerates and keeps the last specified direction.  This call will immediately return even if the deceleration is still in progress. After a stop request has been received, no further updates to the ongoing jogging movement are possible.  State responses will be sent via the jogging stream until the motion group reaches standstill. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param motion_group: The motion-group id. (required)
        :type motion_group: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._stop_jogging_serialize(
            cell=cell,
            motion_group=motion_group,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _stop_jogging_serialize(
        self,
        cell,
        motion_group,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cell is not None:
            _path_params['cell'] = cell
        if motion_group is not None:
            _path_params['motion-group'] = motion_group
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'BasicAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/cells/{cell}/motion-groups/{motion-group}/stop',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


