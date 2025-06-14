# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.create_employees_international_assignment_request import CreateEmployeesInternationalAssignmentRequest
from ..model.create_employees_international_assignment_response import CreateEmployeesInternationalAssignmentResponse
from ..model.delete_employees_international_assignment_request import DeleteEmployeesInternationalAssignmentRequest
from ..model.delete_employees_international_assignment_response import DeleteEmployeesInternationalAssignmentResponse
from ..model.list_employees_international_assignment_request import ListEmployeesInternationalAssignmentRequest
from ..model.list_employees_international_assignment_response import ListEmployeesInternationalAssignmentResponse
from ..model.patch_employees_international_assignment_request import PatchEmployeesInternationalAssignmentRequest
from ..model.patch_employees_international_assignment_response import PatchEmployeesInternationalAssignmentResponse


class EmployeesInternationalAssignment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateEmployeesInternationalAssignmentRequest,
               option: Optional[RequestOption] = None) -> CreateEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                  CreateEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateEmployeesInternationalAssignmentRequest,
                      option: Optional[RequestOption] = None) -> CreateEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                  CreateEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteEmployeesInternationalAssignmentRequest,
               option: Optional[RequestOption] = None) -> DeleteEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                  DeleteEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteEmployeesInternationalAssignmentRequest,
                      option: Optional[RequestOption] = None) -> DeleteEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                  DeleteEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    def list(self, request: ListEmployeesInternationalAssignmentRequest,
             option: Optional[RequestOption] = None) -> ListEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                ListEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListEmployeesInternationalAssignmentRequest,
                    option: Optional[RequestOption] = None) -> ListEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                ListEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchEmployeesInternationalAssignmentRequest,
              option: Optional[RequestOption] = None) -> PatchEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                 PatchEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchEmployeesInternationalAssignmentRequest,
                     option: Optional[RequestOption] = None) -> PatchEmployeesInternationalAssignmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchEmployeesInternationalAssignmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                 PatchEmployeesInternationalAssignmentResponse)
        response.raw = resp

        return response
