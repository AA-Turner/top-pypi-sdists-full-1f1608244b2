# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_dingtalk.client import Client as GatewayClientClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.calendar_1_0 import models as dingtalkcalendar__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''
        if UtilClient.empty(self._endpoint):
            self._endpoint = 'api.dingtalk.com'

    def add_attendee_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddAttendeeRequest,
        headers: dingtalkcalendar__1__0_models.AddAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.AddAttendeeResponse:
        """
        @summary 新增日程参与人
        
        @param request: AddAttendeeRequest
        @param headers: AddAttendeeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAttendeeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees_to_add):
            body['attendeesToAdd'] = request.attendees_to_add
        if not UtilClient.is_unset(request.chat_notification):
            body['chatNotification'] = request.chat_notification
        if not UtilClient.is_unset(request.push_notification):
            body['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAttendee',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.AddAttendeeResponse(),
            self.execute(params, req, runtime)
        )

    async def add_attendee_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddAttendeeRequest,
        headers: dingtalkcalendar__1__0_models.AddAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.AddAttendeeResponse:
        """
        @summary 新增日程参与人
        
        @param request: AddAttendeeRequest
        @param headers: AddAttendeeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAttendeeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees_to_add):
            body['attendeesToAdd'] = request.attendees_to_add
        if not UtilClient.is_unset(request.chat_notification):
            body['chatNotification'] = request.chat_notification
        if not UtilClient.is_unset(request.push_notification):
            body['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAttendee',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.AddAttendeeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_attendee(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddAttendeeRequest,
    ) -> dingtalkcalendar__1__0_models.AddAttendeeResponse:
        """
        @summary 新增日程参与人
        
        @param request: AddAttendeeRequest
        @return: AddAttendeeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.AddAttendeeHeaders()
        return self.add_attendee_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def add_attendee_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddAttendeeRequest,
    ) -> dingtalkcalendar__1__0_models.AddAttendeeResponse:
        """
        @summary 新增日程参与人
        
        @param request: AddAttendeeRequest
        @return: AddAttendeeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.AddAttendeeHeaders()
        return await self.add_attendee_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def add_meeting_rooms_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddMeetingRoomsRequest,
        headers: dingtalkcalendar__1__0_models.AddMeetingRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.AddMeetingRoomsResponse:
        """
        @summary 添加会议室
        
        @param request: AddMeetingRoomsRequest
        @param headers: AddMeetingRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMeetingRoomsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meeting_rooms_to_add):
            body['meetingRoomsToAdd'] = request.meeting_rooms_to_add
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMeetingRooms',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.AddMeetingRoomsResponse(),
            self.execute(params, req, runtime)
        )

    async def add_meeting_rooms_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddMeetingRoomsRequest,
        headers: dingtalkcalendar__1__0_models.AddMeetingRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.AddMeetingRoomsResponse:
        """
        @summary 添加会议室
        
        @param request: AddMeetingRoomsRequest
        @param headers: AddMeetingRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMeetingRoomsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meeting_rooms_to_add):
            body['meetingRoomsToAdd'] = request.meeting_rooms_to_add
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMeetingRooms',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.AddMeetingRoomsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_meeting_rooms(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddMeetingRoomsRequest,
    ) -> dingtalkcalendar__1__0_models.AddMeetingRoomsResponse:
        """
        @summary 添加会议室
        
        @param request: AddMeetingRoomsRequest
        @return: AddMeetingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.AddMeetingRoomsHeaders()
        return self.add_meeting_rooms_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def add_meeting_rooms_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.AddMeetingRoomsRequest,
    ) -> dingtalkcalendar__1__0_models.AddMeetingRoomsResponse:
        """
        @summary 添加会议室
        
        @param request: AddMeetingRoomsRequest
        @return: AddMeetingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.AddMeetingRoomsHeaders()
        return await self.add_meeting_rooms_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def cancel_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.CancelEventRequest,
        headers: dingtalkcalendar__1__0_models.CancelEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CancelEventResponse:
        """
        @summary 取消指定日程
        
        @param request: CancelEventRequest
        @param headers: CancelEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CancelEventResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.CancelEventRequest,
        headers: dingtalkcalendar__1__0_models.CancelEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CancelEventResponse:
        """
        @summary 取消指定日程
        
        @param request: CancelEventRequest
        @param headers: CancelEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CancelEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.CancelEventRequest,
    ) -> dingtalkcalendar__1__0_models.CancelEventResponse:
        """
        @summary 取消指定日程
        
        @param request: CancelEventRequest
        @return: CancelEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CancelEventHeaders()
        return self.cancel_event_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def cancel_event_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.CancelEventRequest,
    ) -> dingtalkcalendar__1__0_models.CancelEventResponse:
        """
        @summary 取消指定日程
        
        @param request: CancelEventRequest
        @return: CancelEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CancelEventHeaders()
        return await self.cancel_event_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def check_in_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.CheckInHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CheckInResponse:
        """
        @summary 签到
        
        @param headers: CheckInHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CheckIn',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/checkIn',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CheckInResponse(),
            self.execute(params, req, runtime)
        )

    async def check_in_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.CheckInHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CheckInResponse:
        """
        @summary 签到
        
        @param headers: CheckInHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CheckIn',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/checkIn',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CheckInResponse(),
            await self.execute_async(params, req, runtime)
        )

    def check_in(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.CheckInResponse:
        """
        @summary 签到
        
        @return: CheckInResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CheckInHeaders()
        return self.check_in_with_options(user_id, calendar_id, event_id, headers, runtime)

    async def check_in_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.CheckInResponse:
        """
        @summary 签到
        
        @return: CheckInResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CheckInHeaders()
        return await self.check_in_with_options_async(user_id, calendar_id, event_id, headers, runtime)

    def convert_legacy_event_id_with_options(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.ConvertLegacyEventIdRequest,
        headers: dingtalkcalendar__1__0_models.ConvertLegacyEventIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse:
        """
        @summary 转换老版本的eventId
        
        @param request: ConvertLegacyEventIdRequest
        @param headers: ConvertLegacyEventIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertLegacyEventIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.legacy_event_ids):
            body['legacyEventIds'] = request.legacy_event_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertLegacyEventId',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/legacyEventIds/convert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse(),
            self.execute(params, req, runtime)
        )

    async def convert_legacy_event_id_with_options_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.ConvertLegacyEventIdRequest,
        headers: dingtalkcalendar__1__0_models.ConvertLegacyEventIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse:
        """
        @summary 转换老版本的eventId
        
        @param request: ConvertLegacyEventIdRequest
        @param headers: ConvertLegacyEventIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertLegacyEventIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.legacy_event_ids):
            body['legacyEventIds'] = request.legacy_event_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertLegacyEventId',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/legacyEventIds/convert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse(),
            await self.execute_async(params, req, runtime)
        )

    def convert_legacy_event_id(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.ConvertLegacyEventIdRequest,
    ) -> dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse:
        """
        @summary 转换老版本的eventId
        
        @param request: ConvertLegacyEventIdRequest
        @return: ConvertLegacyEventIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ConvertLegacyEventIdHeaders()
        return self.convert_legacy_event_id_with_options(user_id, request, headers, runtime)

    async def convert_legacy_event_id_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.ConvertLegacyEventIdRequest,
    ) -> dingtalkcalendar__1__0_models.ConvertLegacyEventIdResponse:
        """
        @summary 转换老版本的eventId
        
        @param request: ConvertLegacyEventIdRequest
        @return: ConvertLegacyEventIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ConvertLegacyEventIdHeaders()
        return await self.convert_legacy_event_id_with_options_async(user_id, request, headers, runtime)

    def create_acls_with_options(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateAclsRequest,
        headers: dingtalkcalendar__1__0_models.CreateAclsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateAclsResponse:
        """
        @summary 创建访问控制
        
        @param request: CreateAclsRequest
        @param headers: CreateAclsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.privilege):
            body['privilege'] = request.privilege
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.send_msg):
            body['sendMsg'] = request.send_msg
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAcls',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateAclsResponse(),
            self.execute(params, req, runtime)
        )

    async def create_acls_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateAclsRequest,
        headers: dingtalkcalendar__1__0_models.CreateAclsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateAclsResponse:
        """
        @summary 创建访问控制
        
        @param request: CreateAclsRequest
        @param headers: CreateAclsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.privilege):
            body['privilege'] = request.privilege
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.send_msg):
            body['sendMsg'] = request.send_msg
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAcls',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateAclsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_acls(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateAclsRequest,
    ) -> dingtalkcalendar__1__0_models.CreateAclsResponse:
        """
        @summary 创建访问控制
        
        @param request: CreateAclsRequest
        @return: CreateAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateAclsHeaders()
        return self.create_acls_with_options(user_id, calendar_id, request, headers, runtime)

    async def create_acls_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateAclsRequest,
    ) -> dingtalkcalendar__1__0_models.CreateAclsResponse:
        """
        @summary 创建访问控制
        
        @param request: CreateAclsRequest
        @return: CreateAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateAclsHeaders()
        return await self.create_acls_with_options_async(user_id, calendar_id, request, headers, runtime)

    def create_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventRequest,
        headers: dingtalkcalendar__1__0_models.CreateEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateEventResponse:
        """
        @summary 创建日程
        
        @param request: CreateEventRequest
        @param headers: CreateEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.card_instances):
            body['cardInstances'] = request.card_instances
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.free_busy_status):
            body['freeBusyStatus'] = request.free_busy_status
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateEventResponse(),
            self.execute(params, req, runtime)
        )

    async def create_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventRequest,
        headers: dingtalkcalendar__1__0_models.CreateEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateEventResponse:
        """
        @summary 创建日程
        
        @param request: CreateEventRequest
        @param headers: CreateEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.card_instances):
            body['cardInstances'] = request.card_instances
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.free_busy_status):
            body['freeBusyStatus'] = request.free_busy_status
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_event(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventRequest,
    ) -> dingtalkcalendar__1__0_models.CreateEventResponse:
        """
        @summary 创建日程
        
        @param request: CreateEventRequest
        @return: CreateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateEventHeaders()
        return self.create_event_with_options(user_id, calendar_id, request, headers, runtime)

    async def create_event_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventRequest,
    ) -> dingtalkcalendar__1__0_models.CreateEventResponse:
        """
        @summary 创建日程
        
        @param request: CreateEventRequest
        @return: CreateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateEventHeaders()
        return await self.create_event_with_options_async(user_id, calendar_id, request, headers, runtime)

    def create_event_by_me_with_options(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventByMeRequest,
        headers: dingtalkcalendar__1__0_models.CreateEventByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateEventByMeResponse:
        """
        @summary 创建日程(me接口)
        
        @param request: CreateEventByMeRequest
        @param headers: CreateEventByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventByMeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/calendars/{calendar_id}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateEventByMeResponse(),
            self.execute(params, req, runtime)
        )

    async def create_event_by_me_with_options_async(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventByMeRequest,
        headers: dingtalkcalendar__1__0_models.CreateEventByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateEventByMeResponse:
        """
        @summary 创建日程(me接口)
        
        @param request: CreateEventByMeRequest
        @param headers: CreateEventByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventByMeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/calendars/{calendar_id}/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateEventByMeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_event_by_me(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventByMeRequest,
    ) -> dingtalkcalendar__1__0_models.CreateEventByMeResponse:
        """
        @summary 创建日程(me接口)
        
        @param request: CreateEventByMeRequest
        @return: CreateEventByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateEventByMeHeaders()
        return self.create_event_by_me_with_options(calendar_id, request, headers, runtime)

    async def create_event_by_me_async(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.CreateEventByMeRequest,
    ) -> dingtalkcalendar__1__0_models.CreateEventByMeResponse:
        """
        @summary 创建日程(me接口)
        
        @param request: CreateEventByMeRequest
        @return: CreateEventByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateEventByMeHeaders()
        return await self.create_event_by_me_with_options_async(calendar_id, request, headers, runtime)

    def create_subscribed_calendar_with_options(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.CreateSubscribedCalendarRequest,
        headers: dingtalkcalendar__1__0_models.CreateSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse:
        """
        @summary 快速创建订阅日历
        
        @param request: CreateSubscribedCalendarRequest
        @param headers: CreateSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscribedCalendarResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope):
            body['subscribeScope'] = request.subscribe_scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse(),
            self.execute(params, req, runtime)
        )

    async def create_subscribed_calendar_with_options_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.CreateSubscribedCalendarRequest,
        headers: dingtalkcalendar__1__0_models.CreateSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse:
        """
        @summary 快速创建订阅日历
        
        @param request: CreateSubscribedCalendarRequest
        @param headers: CreateSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscribedCalendarResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope):
            body['subscribeScope'] = request.subscribe_scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_subscribed_calendar(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.CreateSubscribedCalendarRequest,
    ) -> dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse:
        """
        @summary 快速创建订阅日历
        
        @param request: CreateSubscribedCalendarRequest
        @return: CreateSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateSubscribedCalendarHeaders()
        return self.create_subscribed_calendar_with_options(user_id, request, headers, runtime)

    async def create_subscribed_calendar_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.CreateSubscribedCalendarRequest,
    ) -> dingtalkcalendar__1__0_models.CreateSubscribedCalendarResponse:
        """
        @summary 快速创建订阅日历
        
        @param request: CreateSubscribedCalendarRequest
        @return: CreateSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.CreateSubscribedCalendarHeaders()
        return await self.create_subscribed_calendar_with_options_async(user_id, request, headers, runtime)

    def delete_acl_with_options(
        self,
        user_id: str,
        calendar_id: str,
        acl_id: str,
        headers: dingtalkcalendar__1__0_models.DeleteAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteAclResponse:
        """
        @summary 删除访问控制
        
        @param headers: DeleteAclHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls/{acl_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteAclResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        acl_id: str,
        headers: dingtalkcalendar__1__0_models.DeleteAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteAclResponse:
        """
        @summary 删除访问控制
        
        @param headers: DeleteAclHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls/{acl_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteAclResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_acl(
        self,
        user_id: str,
        calendar_id: str,
        acl_id: str,
    ) -> dingtalkcalendar__1__0_models.DeleteAclResponse:
        """
        @summary 删除访问控制
        
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteAclHeaders()
        return self.delete_acl_with_options(user_id, calendar_id, acl_id, headers, runtime)

    async def delete_acl_async(
        self,
        user_id: str,
        calendar_id: str,
        acl_id: str,
    ) -> dingtalkcalendar__1__0_models.DeleteAclResponse:
        """
        @summary 删除访问控制
        
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteAclHeaders()
        return await self.delete_acl_with_options_async(user_id, calendar_id, acl_id, headers, runtime)

    def delete_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.DeleteEventRequest,
        headers: dingtalkcalendar__1__0_models.DeleteEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteEventResponse:
        """
        @summary 删除指定日程
        
        @param request: DeleteEventRequest
        @param headers: DeleteEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.push_notification):
            query['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteEventResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.DeleteEventRequest,
        headers: dingtalkcalendar__1__0_models.DeleteEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteEventResponse:
        """
        @summary 删除指定日程
        
        @param request: DeleteEventRequest
        @param headers: DeleteEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.push_notification):
            query['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.DeleteEventRequest,
    ) -> dingtalkcalendar__1__0_models.DeleteEventResponse:
        """
        @summary 删除指定日程
        
        @param request: DeleteEventRequest
        @return: DeleteEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteEventHeaders()
        return self.delete_event_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def delete_event_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.DeleteEventRequest,
    ) -> dingtalkcalendar__1__0_models.DeleteEventResponse:
        """
        @summary 删除指定日程
        
        @param request: DeleteEventRequest
        @return: DeleteEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteEventHeaders()
        return await self.delete_event_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def delete_subscribed_calendar_with_options(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse:
        """
        @summary 删除指定订阅日历
        
        @param headers: DeleteSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubscribedCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_subscribed_calendar_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse:
        """
        @summary 删除指定订阅日历
        
        @param headers: DeleteSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubscribedCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_subscribed_calendar(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse:
        """
        @summary 删除指定订阅日历
        
        @return: DeleteSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders()
        return self.delete_subscribed_calendar_with_options(user_id, calendar_id, headers, runtime)

    async def delete_subscribed_calendar_async(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.DeleteSubscribedCalendarResponse:
        """
        @summary 删除指定订阅日历
        
        @return: DeleteSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders()
        return await self.delete_subscribed_calendar_with_options_async(user_id, calendar_id, headers, runtime)

    def generate_caldav_account_with_options(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GenerateCaldavAccountRequest,
        headers: dingtalkcalendar__1__0_models.GenerateCaldavAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse:
        """
        @summary 生成caldav账户
        
        @param request: GenerateCaldavAccountRequest
        @param headers: GenerateCaldavAccountHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCaldavAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device):
            body['device'] = request.device
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.ding_uid):
            real_headers['dingUid'] = UtilClient.to_jsonstring(headers.ding_uid)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCaldavAccount',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/caldavAccounts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def generate_caldav_account_with_options_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GenerateCaldavAccountRequest,
        headers: dingtalkcalendar__1__0_models.GenerateCaldavAccountHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse:
        """
        @summary 生成caldav账户
        
        @param request: GenerateCaldavAccountRequest
        @param headers: GenerateCaldavAccountHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCaldavAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device):
            body['device'] = request.device
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.ding_uid):
            real_headers['dingUid'] = UtilClient.to_jsonstring(headers.ding_uid)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCaldavAccount',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/caldavAccounts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def generate_caldav_account(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GenerateCaldavAccountRequest,
    ) -> dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse:
        """
        @summary 生成caldav账户
        
        @param request: GenerateCaldavAccountRequest
        @return: GenerateCaldavAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GenerateCaldavAccountHeaders()
        return self.generate_caldav_account_with_options(user_id, request, headers, runtime)

    async def generate_caldav_account_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GenerateCaldavAccountRequest,
    ) -> dingtalkcalendar__1__0_models.GenerateCaldavAccountResponse:
        """
        @summary 生成caldav账户
        
        @param request: GenerateCaldavAccountRequest
        @return: GenerateCaldavAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GenerateCaldavAccountHeaders()
        return await self.generate_caldav_account_with_options_async(user_id, request, headers, runtime)

    def get_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetEventRequest,
        headers: dingtalkcalendar__1__0_models.GetEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetEventResponse:
        """
        @summary 查询日程列表
        
        @param request: GetEventRequest
        @param headers: GetEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetEventResponse(),
            self.execute(params, req, runtime)
        )

    async def get_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetEventRequest,
        headers: dingtalkcalendar__1__0_models.GetEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetEventResponse:
        """
        @summary 查询日程列表
        
        @param request: GetEventRequest
        @param headers: GetEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetEventRequest,
    ) -> dingtalkcalendar__1__0_models.GetEventResponse:
        """
        @summary 查询日程列表
        
        @param request: GetEventRequest
        @return: GetEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetEventHeaders()
        return self.get_event_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def get_event_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetEventRequest,
    ) -> dingtalkcalendar__1__0_models.GetEventResponse:
        """
        @summary 查询日程列表
        
        @param request: GetEventRequest
        @return: GetEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetEventHeaders()
        return await self.get_event_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def get_meeting_rooms_schedule_with_options(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest,
        headers: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse:
        """
        @summary 查询会议室忙闲
        
        @param request: GetMeetingRoomsScheduleRequest
        @param headers: GetMeetingRoomsScheduleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMeetingRoomsScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.room_ids):
            body['roomIds'] = request.room_ids
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMeetingRoomsSchedule',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/meetingRooms/schedules/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse(),
            self.execute(params, req, runtime)
        )

    async def get_meeting_rooms_schedule_with_options_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest,
        headers: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse:
        """
        @summary 查询会议室忙闲
        
        @param request: GetMeetingRoomsScheduleRequest
        @param headers: GetMeetingRoomsScheduleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMeetingRoomsScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.room_ids):
            body['roomIds'] = request.room_ids
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMeetingRoomsSchedule',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/meetingRooms/schedules/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_meeting_rooms_schedule(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest,
    ) -> dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse:
        """
        @summary 查询会议室忙闲
        
        @param request: GetMeetingRoomsScheduleRequest
        @return: GetMeetingRoomsScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders()
        return self.get_meeting_rooms_schedule_with_options(user_id, request, headers, runtime)

    async def get_meeting_rooms_schedule_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest,
    ) -> dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleResponse:
        """
        @summary 查询会议室忙闲
        
        @param request: GetMeetingRoomsScheduleRequest
        @return: GetMeetingRoomsScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders()
        return await self.get_meeting_rooms_schedule_with_options_async(user_id, request, headers, runtime)

    def get_schedule_with_options(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetScheduleRequest,
        headers: dingtalkcalendar__1__0_models.GetScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetScheduleResponse:
        """
        @summary 查询闲忙
        
        @param request: GetScheduleRequest
        @param headers: GetScheduleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSchedule',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/querySchedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetScheduleResponse(),
            self.execute(params, req, runtime)
        )

    async def get_schedule_with_options_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetScheduleRequest,
        headers: dingtalkcalendar__1__0_models.GetScheduleHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetScheduleResponse:
        """
        @summary 查询闲忙
        
        @param request: GetScheduleRequest
        @param headers: GetScheduleHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSchedule',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/querySchedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetScheduleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_schedule(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetScheduleRequest,
    ) -> dingtalkcalendar__1__0_models.GetScheduleResponse:
        """
        @summary 查询闲忙
        
        @param request: GetScheduleRequest
        @return: GetScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetScheduleHeaders()
        return self.get_schedule_with_options(user_id, request, headers, runtime)

    async def get_schedule_async(
        self,
        user_id: str,
        request: dingtalkcalendar__1__0_models.GetScheduleRequest,
    ) -> dingtalkcalendar__1__0_models.GetScheduleResponse:
        """
        @summary 查询闲忙
        
        @param request: GetScheduleRequest
        @return: GetScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetScheduleHeaders()
        return await self.get_schedule_with_options_async(user_id, request, headers, runtime)

    def get_schedule_by_me_with_options(
        self,
        request: dingtalkcalendar__1__0_models.GetScheduleByMeRequest,
        headers: dingtalkcalendar__1__0_models.GetScheduleByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetScheduleByMeResponse:
        """
        @summary 查询闲忙(me接口）
        
        @param request: GetScheduleByMeRequest
        @param headers: GetScheduleByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduleByMeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScheduleByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/schedules/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetScheduleByMeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_schedule_by_me_with_options_async(
        self,
        request: dingtalkcalendar__1__0_models.GetScheduleByMeRequest,
        headers: dingtalkcalendar__1__0_models.GetScheduleByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetScheduleByMeResponse:
        """
        @summary 查询闲忙(me接口）
        
        @param request: GetScheduleByMeRequest
        @param headers: GetScheduleByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduleByMeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScheduleByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/schedules/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetScheduleByMeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_schedule_by_me(
        self,
        request: dingtalkcalendar__1__0_models.GetScheduleByMeRequest,
    ) -> dingtalkcalendar__1__0_models.GetScheduleByMeResponse:
        """
        @summary 查询闲忙(me接口）
        
        @param request: GetScheduleByMeRequest
        @return: GetScheduleByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetScheduleByMeHeaders()
        return self.get_schedule_by_me_with_options(request, headers, runtime)

    async def get_schedule_by_me_async(
        self,
        request: dingtalkcalendar__1__0_models.GetScheduleByMeRequest,
    ) -> dingtalkcalendar__1__0_models.GetScheduleByMeResponse:
        """
        @summary 查询闲忙(me接口）
        
        @param request: GetScheduleByMeRequest
        @return: GetScheduleByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetScheduleByMeHeaders()
        return await self.get_schedule_by_me_with_options_async(request, headers, runtime)

    def get_sign_in_link_with_options(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.GetSignInLinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignInLinkResponse:
        """
        @summary 获取签到链接
        
        @param headers: GetSignInLinkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignInLinkResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSignInLink',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signInLinks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignInLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sign_in_link_with_options_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.GetSignInLinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignInLinkResponse:
        """
        @summary 获取签到链接
        
        @param headers: GetSignInLinkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignInLinkResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSignInLink',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signInLinks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignInLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sign_in_link(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSignInLinkResponse:
        """
        @summary 获取签到链接
        
        @return: GetSignInLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignInLinkHeaders()
        return self.get_sign_in_link_with_options(calendar_id, user_id, event_id, headers, runtime)

    async def get_sign_in_link_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSignInLinkResponse:
        """
        @summary 获取签到链接
        
        @return: GetSignInLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignInLinkHeaders()
        return await self.get_sign_in_link_with_options_async(calendar_id, user_id, event_id, headers, runtime)

    def get_sign_in_list_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignInListRequest,
        headers: dingtalkcalendar__1__0_models.GetSignInListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignInListResponse:
        """
        @summary 获取签到信息详情
        
        @param request: GetSignInListRequest
        @param headers: GetSignInListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignInListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSignInList',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signin',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignInListResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sign_in_list_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignInListRequest,
        headers: dingtalkcalendar__1__0_models.GetSignInListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignInListResponse:
        """
        @summary 获取签到信息详情
        
        @param request: GetSignInListRequest
        @param headers: GetSignInListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignInListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSignInList',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signin',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignInListResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sign_in_list(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignInListRequest,
    ) -> dingtalkcalendar__1__0_models.GetSignInListResponse:
        """
        @summary 获取签到信息详情
        
        @param request: GetSignInListRequest
        @return: GetSignInListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignInListHeaders()
        return self.get_sign_in_list_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def get_sign_in_list_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignInListRequest,
    ) -> dingtalkcalendar__1__0_models.GetSignInListResponse:
        """
        @summary 获取签到信息详情
        
        @param request: GetSignInListRequest
        @return: GetSignInListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignInListHeaders()
        return await self.get_sign_in_list_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def get_sign_out_link_with_options(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.GetSignOutLinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignOutLinkResponse:
        """
        @summary 获取签退链接
        
        @param headers: GetSignOutLinkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignOutLinkResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSignOutLink',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOutLinks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignOutLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sign_out_link_with_options_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.GetSignOutLinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignOutLinkResponse:
        """
        @summary 获取签退链接
        
        @param headers: GetSignOutLinkHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignOutLinkResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSignOutLink',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOutLinks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignOutLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sign_out_link(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSignOutLinkResponse:
        """
        @summary 获取签退链接
        
        @return: GetSignOutLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignOutLinkHeaders()
        return self.get_sign_out_link_with_options(calendar_id, user_id, event_id, headers, runtime)

    async def get_sign_out_link_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSignOutLinkResponse:
        """
        @summary 获取签退链接
        
        @return: GetSignOutLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignOutLinkHeaders()
        return await self.get_sign_out_link_with_options_async(calendar_id, user_id, event_id, headers, runtime)

    def get_sign_out_list_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignOutListRequest,
        headers: dingtalkcalendar__1__0_models.GetSignOutListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignOutListResponse:
        """
        @summary 获取签退信息详情
        
        @param request: GetSignOutListRequest
        @param headers: GetSignOutListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignOutListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSignOutList',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOut',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignOutListResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sign_out_list_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignOutListRequest,
        headers: dingtalkcalendar__1__0_models.GetSignOutListHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSignOutListResponse:
        """
        @summary 获取签退信息详情
        
        @param request: GetSignOutListRequest
        @param headers: GetSignOutListHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSignOutListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSignOutList',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOut',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSignOutListResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sign_out_list(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignOutListRequest,
    ) -> dingtalkcalendar__1__0_models.GetSignOutListResponse:
        """
        @summary 获取签退信息详情
        
        @param request: GetSignOutListRequest
        @return: GetSignOutListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignOutListHeaders()
        return self.get_sign_out_list_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def get_sign_out_list_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.GetSignOutListRequest,
    ) -> dingtalkcalendar__1__0_models.GetSignOutListResponse:
        """
        @summary 获取签退信息详情
        
        @param request: GetSignOutListRequest
        @return: GetSignOutListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSignOutListHeaders()
        return await self.get_sign_out_list_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def get_subscribed_calendar_with_options(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.GetSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse:
        """
        @summary 获取指定订阅日历详情
        
        @param headers: GetSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscribedCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse(),
            self.execute(params, req, runtime)
        )

    async def get_subscribed_calendar_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.GetSubscribedCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse:
        """
        @summary 获取指定订阅日历详情
        
        @param headers: GetSubscribedCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscribedCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSubscribedCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_subscribed_calendar(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse:
        """
        @summary 获取指定订阅日历详情
        
        @return: GetSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSubscribedCalendarHeaders()
        return self.get_subscribed_calendar_with_options(user_id, calendar_id, headers, runtime)

    async def get_subscribed_calendar_async(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.GetSubscribedCalendarResponse:
        """
        @summary 获取指定订阅日历详情
        
        @return: GetSubscribedCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.GetSubscribedCalendarHeaders()
        return await self.get_subscribed_calendar_with_options_async(user_id, calendar_id, headers, runtime)

    def list_acls_with_options(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.ListAclsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListAclsResponse:
        """
        @summary 获取访问控制列表
        
        @param headers: ListAclsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListAclsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_acls_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.ListAclsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListAclsResponse:
        """
        @summary 获取访问控制列表
        
        @param headers: ListAclsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/acls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListAclsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_acls(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.ListAclsResponse:
        """
        @summary 获取访问控制列表
        
        @return: ListAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListAclsHeaders()
        return self.list_acls_with_options(user_id, calendar_id, headers, runtime)

    async def list_acls_async(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.ListAclsResponse:
        """
        @summary 获取访问控制列表
        
        @return: ListAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListAclsHeaders()
        return await self.list_acls_with_options_async(user_id, calendar_id, headers, runtime)

    def list_attendees_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListAttendeesRequest,
        headers: dingtalkcalendar__1__0_models.ListAttendeesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListAttendeesResponse:
        """
        @summary 分页获取参与人列表
        
        @param request: ListAttendeesRequest
        @param headers: ListAttendeesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAttendeesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttendees',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListAttendeesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_attendees_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListAttendeesRequest,
        headers: dingtalkcalendar__1__0_models.ListAttendeesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListAttendeesResponse:
        """
        @summary 分页获取参与人列表
        
        @param request: ListAttendeesRequest
        @param headers: ListAttendeesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAttendeesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttendees',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListAttendeesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_attendees(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListAttendeesRequest,
    ) -> dingtalkcalendar__1__0_models.ListAttendeesResponse:
        """
        @summary 分页获取参与人列表
        
        @param request: ListAttendeesRequest
        @return: ListAttendeesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListAttendeesHeaders()
        return self.list_attendees_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def list_attendees_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListAttendeesRequest,
    ) -> dingtalkcalendar__1__0_models.ListAttendeesResponse:
        """
        @summary 分页获取参与人列表
        
        @param request: ListAttendeesRequest
        @return: ListAttendeesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListAttendeesHeaders()
        return await self.list_attendees_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def list_calendars_with_options(
        self,
        user_id: str,
        headers: dingtalkcalendar__1__0_models.ListCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListCalendarsResponse:
        """
        @summary 日历本查询
        
        @param headers: ListCalendarsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalendarsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCalendars',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListCalendarsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_calendars_with_options_async(
        self,
        user_id: str,
        headers: dingtalkcalendar__1__0_models.ListCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListCalendarsResponse:
        """
        @summary 日历本查询
        
        @param headers: ListCalendarsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalendarsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCalendars',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListCalendarsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_calendars(
        self,
        user_id: str,
    ) -> dingtalkcalendar__1__0_models.ListCalendarsResponse:
        """
        @summary 日历本查询
        
        @return: ListCalendarsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListCalendarsHeaders()
        return self.list_calendars_with_options(user_id, headers, runtime)

    async def list_calendars_async(
        self,
        user_id: str,
    ) -> dingtalkcalendar__1__0_models.ListCalendarsResponse:
        """
        @summary 日历本查询
        
        @return: ListCalendarsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListCalendarsHeaders()
        return await self.list_calendars_with_options_async(user_id, headers, runtime)

    def list_categories_with_options(
        self,
        user_id: str,
        headers: dingtalkcalendar__1__0_models.ListCategoriesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListCategoriesResponse:
        """
        @summary 获取会议类型列表
        
        @param headers: ListCategoriesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoriesResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCategories',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/categories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListCategoriesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        user_id: str,
        headers: dingtalkcalendar__1__0_models.ListCategoriesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListCategoriesResponse:
        """
        @summary 获取会议类型列表
        
        @param headers: ListCategoriesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoriesResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCategories',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/categories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListCategoriesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_categories(
        self,
        user_id: str,
    ) -> dingtalkcalendar__1__0_models.ListCategoriesResponse:
        """
        @summary 获取会议类型列表
        
        @return: ListCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListCategoriesHeaders()
        return self.list_categories_with_options(user_id, headers, runtime)

    async def list_categories_async(
        self,
        user_id: str,
    ) -> dingtalkcalendar__1__0_models.ListCategoriesResponse:
        """
        @summary 获取会议类型列表
        
        @return: ListCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListCategoriesHeaders()
        return await self.list_categories_with_options_async(user_id, headers, runtime)

    def list_events_with_options(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsResponse:
        """
        @summary 查询日程列表
        
        @param request: ListEventsRequest
        @param headers: ListEventsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.series_master_id):
            query['seriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.show_deleted):
            query['showDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.sync_token):
            query['syncToken'] = request.sync_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_events_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsResponse:
        """
        @summary 查询日程列表
        
        @param request: ListEventsRequest
        @param headers: ListEventsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.series_master_id):
            query['seriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.show_deleted):
            query['showDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.sync_token):
            query['syncToken'] = request.sync_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_events(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsResponse:
        """
        @summary 查询日程列表
        
        @param request: ListEventsRequest
        @return: ListEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsHeaders()
        return self.list_events_with_options(user_id, calendar_id, request, headers, runtime)

    async def list_events_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsResponse:
        """
        @summary 查询日程列表
        
        @param request: ListEventsRequest
        @return: ListEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsHeaders()
        return await self.list_events_with_options_async(user_id, calendar_id, request, headers, runtime)

    def list_events_instances_with_options(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsInstancesRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsInstancesResponse:
        """
        @summary 查询同一个循环日程序列下已生成的实例
        
        @param request: ListEventsInstancesRequest
        @param headers: ListEventsInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.series_master_id):
            query['seriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.start_recurrence_id):
            query['startRecurrenceId'] = request.start_recurrence_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsInstances',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsInstancesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_events_instances_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsInstancesRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsInstancesResponse:
        """
        @summary 查询同一个循环日程序列下已生成的实例
        
        @param request: ListEventsInstancesRequest
        @param headers: ListEventsInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.series_master_id):
            query['seriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.start_recurrence_id):
            query['startRecurrenceId'] = request.start_recurrence_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsInstances',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsInstancesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_events_instances(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsInstancesRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsInstancesResponse:
        """
        @summary 查询同一个循环日程序列下已生成的实例
        
        @param request: ListEventsInstancesRequest
        @return: ListEventsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsInstancesHeaders()
        return self.list_events_instances_with_options(user_id, calendar_id, request, headers, runtime)

    async def list_events_instances_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsInstancesRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsInstancesResponse:
        """
        @summary 查询同一个循环日程序列下已生成的实例
        
        @param request: ListEventsInstancesRequest
        @return: ListEventsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsInstancesHeaders()
        return await self.list_events_instances_with_options_async(user_id, calendar_id, request, headers, runtime)

    def list_events_view_with_options(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsViewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程
        
        @param request: ListEventsViewRequest
        @param headers: ListEventsViewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsView',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/eventsview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsViewResponse(),
            self.execute(params, req, runtime)
        )

    async def list_events_view_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsViewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程
        
        @param request: ListEventsViewRequest
        @param headers: ListEventsViewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsView',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/eventsview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_events_view(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程
        
        @param request: ListEventsViewRequest
        @return: ListEventsViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsViewHeaders()
        return self.list_events_view_with_options(user_id, calendar_id, request, headers, runtime)

    async def list_events_view_async(
        self,
        user_id: str,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程
        
        @param request: ListEventsViewRequest
        @return: ListEventsViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsViewHeaders()
        return await self.list_events_view_with_options_async(user_id, calendar_id, request, headers, runtime)

    def list_events_view_by_me_with_options(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewByMeRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsViewByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewByMeResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程(me接口）
        
        @param request: ListEventsViewByMeRequest
        @param headers: ListEventsViewByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsViewByMeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsViewByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/calendars/{calendar_id}/eventsview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsViewByMeResponse(),
            self.execute(params, req, runtime)
        )

    async def list_events_view_by_me_with_options_async(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewByMeRequest,
        headers: dingtalkcalendar__1__0_models.ListEventsViewByMeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewByMeResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程(me接口）
        
        @param request: ListEventsViewByMeRequest
        @param headers: ListEventsViewByMeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventsViewByMeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventsViewByMe',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/me/calendars/{calendar_id}/eventsview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListEventsViewByMeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_events_view_by_me(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewByMeRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewByMeResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程(me接口）
        
        @param request: ListEventsViewByMeRequest
        @return: ListEventsViewByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsViewByMeHeaders()
        return self.list_events_view_by_me_with_options(calendar_id, request, headers, runtime)

    async def list_events_view_by_me_async(
        self,
        calendar_id: str,
        request: dingtalkcalendar__1__0_models.ListEventsViewByMeRequest,
    ) -> dingtalkcalendar__1__0_models.ListEventsViewByMeResponse:
        """
        @summary 查询日程视图列表以查看闲忙，展开循环日程(me接口）
        
        @param request: ListEventsViewByMeRequest
        @return: ListEventsViewByMeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListEventsViewByMeHeaders()
        return await self.list_events_view_by_me_with_options_async(calendar_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListInstancesRequest,
        headers: dingtalkcalendar__1__0_models.ListInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListInstancesResponse:
        """
        @summary 查询循环日程实例列表
        
        @param request: ListInstancesRequest
        @param headers: ListInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListInstancesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListInstancesRequest,
        headers: dingtalkcalendar__1__0_models.ListInstancesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.ListInstancesResponse:
        """
        @summary 查询循环日程实例列表
        
        @param request: ListInstancesRequest
        @param headers: ListInstancesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['maxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            query['timeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            query['timeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.ListInstancesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_instances(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListInstancesRequest,
    ) -> dingtalkcalendar__1__0_models.ListInstancesResponse:
        """
        @summary 查询循环日程实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListInstancesHeaders()
        return self.list_instances_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def list_instances_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.ListInstancesRequest,
    ) -> dingtalkcalendar__1__0_models.ListInstancesResponse:
        """
        @summary 查询循环日程实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.ListInstancesHeaders()
        return await self.list_instances_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def meeting_room_respond_with_options(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        room_id: str,
        request: dingtalkcalendar__1__0_models.MeetingRoomRespondRequest,
        headers: dingtalkcalendar__1__0_models.MeetingRoomRespondHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.MeetingRoomRespondResponse:
        """
        @summary 设置会议室在日程中的响应状态
        
        @param request: MeetingRoomRespondRequest
        @param headers: MeetingRoomRespondHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: MeetingRoomRespondResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.response_status):
            body['responseStatus'] = request.response_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.user_agent):
            real_headers['userAgent'] = UtilClient.to_jsonstring(headers.user_agent)
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MeetingRoomRespond',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms/{room_id}/respond',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.MeetingRoomRespondResponse(),
            self.execute(params, req, runtime)
        )

    async def meeting_room_respond_with_options_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        room_id: str,
        request: dingtalkcalendar__1__0_models.MeetingRoomRespondRequest,
        headers: dingtalkcalendar__1__0_models.MeetingRoomRespondHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.MeetingRoomRespondResponse:
        """
        @summary 设置会议室在日程中的响应状态
        
        @param request: MeetingRoomRespondRequest
        @param headers: MeetingRoomRespondHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: MeetingRoomRespondResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.response_status):
            body['responseStatus'] = request.response_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.user_agent):
            real_headers['userAgent'] = UtilClient.to_jsonstring(headers.user_agent)
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MeetingRoomRespond',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms/{room_id}/respond',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.MeetingRoomRespondResponse(),
            await self.execute_async(params, req, runtime)
        )

    def meeting_room_respond(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        room_id: str,
        request: dingtalkcalendar__1__0_models.MeetingRoomRespondRequest,
    ) -> dingtalkcalendar__1__0_models.MeetingRoomRespondResponse:
        """
        @summary 设置会议室在日程中的响应状态
        
        @param request: MeetingRoomRespondRequest
        @return: MeetingRoomRespondResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.MeetingRoomRespondHeaders()
        return self.meeting_room_respond_with_options(calendar_id, user_id, event_id, room_id, request, headers, runtime)

    async def meeting_room_respond_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        room_id: str,
        request: dingtalkcalendar__1__0_models.MeetingRoomRespondRequest,
    ) -> dingtalkcalendar__1__0_models.MeetingRoomRespondResponse:
        """
        @summary 设置会议室在日程中的响应状态
        
        @param request: MeetingRoomRespondRequest
        @return: MeetingRoomRespondResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.MeetingRoomRespondHeaders()
        return await self.meeting_room_respond_with_options_async(calendar_id, user_id, event_id, room_id, request, headers, runtime)

    def patch_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.PatchEventRequest,
        headers: dingtalkcalendar__1__0_models.PatchEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.PatchEventResponse:
        """
        @summary 修改日程
        
        @param request: PatchEventRequest
        @param headers: PatchEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.card_instances):
            body['cardInstances'] = request.card_instances
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.free_busy_status):
            body['freeBusyStatus'] = request.free_busy_status
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.PatchEventResponse(),
            self.execute(params, req, runtime)
        )

    async def patch_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.PatchEventRequest,
        headers: dingtalkcalendar__1__0_models.PatchEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.PatchEventResponse:
        """
        @summary 修改日程
        
        @param request: PatchEventRequest
        @param headers: PatchEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees):
            body['attendees'] = request.attendees
        if not UtilClient.is_unset(request.card_instances):
            body['cardInstances'] = request.card_instances
        if not UtilClient.is_unset(request.categories):
            body['categories'] = request.categories
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end):
            body['end'] = request.end
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.free_busy_status):
            body['freeBusyStatus'] = request.free_busy_status
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.is_all_day):
            body['isAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.online_meeting_info):
            body['onlineMeetingInfo'] = request.online_meeting_info
        if not UtilClient.is_unset(request.recurrence):
            body['recurrence'] = request.recurrence
        if not UtilClient.is_unset(request.reminders):
            body['reminders'] = request.reminders
        if not UtilClient.is_unset(request.rich_text_description):
            body['richTextDescription'] = request.rich_text_description
        if not UtilClient.is_unset(request.start):
            body['start'] = request.start
        if not UtilClient.is_unset(request.summary):
            body['summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs):
            body['uiConfigs'] = request.ui_configs
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.PatchEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def patch_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.PatchEventRequest,
    ) -> dingtalkcalendar__1__0_models.PatchEventResponse:
        """
        @summary 修改日程
        
        @param request: PatchEventRequest
        @return: PatchEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.PatchEventHeaders()
        return self.patch_event_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def patch_event_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.PatchEventRequest,
    ) -> dingtalkcalendar__1__0_models.PatchEventResponse:
        """
        @summary 修改日程
        
        @param request: PatchEventRequest
        @return: PatchEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.PatchEventHeaders()
        return await self.patch_event_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def remove_attendee_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveAttendeeRequest,
        headers: dingtalkcalendar__1__0_models.RemoveAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RemoveAttendeeResponse:
        """
        @summary 删除日程参与人
        
        @param request: RemoveAttendeeRequest
        @param headers: RemoveAttendeeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAttendeeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees_to_remove):
            body['attendeesToRemove'] = request.attendees_to_remove
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveAttendee',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees/batchRemove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RemoveAttendeeResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_attendee_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveAttendeeRequest,
        headers: dingtalkcalendar__1__0_models.RemoveAttendeeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RemoveAttendeeResponse:
        """
        @summary 删除日程参与人
        
        @param request: RemoveAttendeeRequest
        @param headers: RemoveAttendeeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAttendeeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attendees_to_remove):
            body['attendeesToRemove'] = request.attendees_to_remove
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveAttendee',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attendees/batchRemove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RemoveAttendeeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_attendee(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveAttendeeRequest,
    ) -> dingtalkcalendar__1__0_models.RemoveAttendeeResponse:
        """
        @summary 删除日程参与人
        
        @param request: RemoveAttendeeRequest
        @return: RemoveAttendeeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RemoveAttendeeHeaders()
        return self.remove_attendee_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def remove_attendee_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveAttendeeRequest,
    ) -> dingtalkcalendar__1__0_models.RemoveAttendeeResponse:
        """
        @summary 删除日程参与人
        
        @param request: RemoveAttendeeRequest
        @return: RemoveAttendeeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RemoveAttendeeHeaders()
        return await self.remove_attendee_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def remove_meeting_rooms_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveMeetingRoomsRequest,
        headers: dingtalkcalendar__1__0_models.RemoveMeetingRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse:
        """
        @summary 删除会议室
        
        @param request: RemoveMeetingRoomsRequest
        @param headers: RemoveMeetingRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMeetingRoomsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meeting_rooms_to_remove):
            body['meetingRoomsToRemove'] = request.meeting_rooms_to_remove
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMeetingRooms',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms/batchRemove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_meeting_rooms_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveMeetingRoomsRequest,
        headers: dingtalkcalendar__1__0_models.RemoveMeetingRoomsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse:
        """
        @summary 删除会议室
        
        @param request: RemoveMeetingRoomsRequest
        @param headers: RemoveMeetingRoomsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMeetingRoomsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meeting_rooms_to_remove):
            body['meetingRoomsToRemove'] = request.meeting_rooms_to_remove
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMeetingRooms',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/meetingRooms/batchRemove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_meeting_rooms(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveMeetingRoomsRequest,
    ) -> dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse:
        """
        @summary 删除会议室
        
        @param request: RemoveMeetingRoomsRequest
        @return: RemoveMeetingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RemoveMeetingRoomsHeaders()
        return self.remove_meeting_rooms_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def remove_meeting_rooms_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RemoveMeetingRoomsRequest,
    ) -> dingtalkcalendar__1__0_models.RemoveMeetingRoomsResponse:
        """
        @summary 删除会议室
        
        @param request: RemoveMeetingRoomsRequest
        @return: RemoveMeetingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RemoveMeetingRoomsHeaders()
        return await self.remove_meeting_rooms_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def respond_event_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RespondEventRequest,
        headers: dingtalkcalendar__1__0_models.RespondEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RespondEventResponse:
        """
        @summary 回复日程邀请
        
        @param request: RespondEventRequest
        @param headers: RespondEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RespondEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.response_status):
            body['responseStatus'] = request.response_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RespondEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/respond',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RespondEventResponse(),
            self.execute(params, req, runtime)
        )

    async def respond_event_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RespondEventRequest,
        headers: dingtalkcalendar__1__0_models.RespondEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.RespondEventResponse:
        """
        @summary 回复日程邀请
        
        @param request: RespondEventRequest
        @param headers: RespondEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RespondEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.response_status):
            body['responseStatus'] = request.response_status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RespondEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/respond',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.RespondEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def respond_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RespondEventRequest,
    ) -> dingtalkcalendar__1__0_models.RespondEventResponse:
        """
        @summary 回复日程邀请
        
        @param request: RespondEventRequest
        @return: RespondEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RespondEventHeaders()
        return self.respond_event_with_options(user_id, calendar_id, event_id, request, headers, runtime)

    async def respond_event_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.RespondEventRequest,
    ) -> dingtalkcalendar__1__0_models.RespondEventResponse:
        """
        @summary 回复日程邀请
        
        @param request: RespondEventRequest
        @return: RespondEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.RespondEventHeaders()
        return await self.respond_event_with_options_async(user_id, calendar_id, event_id, request, headers, runtime)

    def sign_in_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.SignInHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SignInResponse:
        """
        @summary 签到
        
        @param headers: SignInHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignInResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SignIn',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signin',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SignInResponse(),
            self.execute(params, req, runtime)
        )

    async def sign_in_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.SignInHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SignInResponse:
        """
        @summary 签到
        
        @param headers: SignInHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignInResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SignIn',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signin',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SignInResponse(),
            await self.execute_async(params, req, runtime)
        )

    def sign_in(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.SignInResponse:
        """
        @summary 签到
        
        @return: SignInResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SignInHeaders()
        return self.sign_in_with_options(user_id, calendar_id, event_id, headers, runtime)

    async def sign_in_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.SignInResponse:
        """
        @summary 签到
        
        @return: SignInResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SignInHeaders()
        return await self.sign_in_with_options_async(user_id, calendar_id, event_id, headers, runtime)

    def sign_out_with_options(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.SignOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SignOutResponse:
        """
        @summary 签退
        
        @param headers: SignOutHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignOutResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SignOut',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SignOutResponse(),
            self.execute(params, req, runtime)
        )

    async def sign_out_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        headers: dingtalkcalendar__1__0_models.SignOutHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SignOutResponse:
        """
        @summary 签退
        
        @param headers: SignOutHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignOutResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SignOut',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/signOut',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SignOutResponse(),
            await self.execute_async(params, req, runtime)
        )

    def sign_out(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.SignOutResponse:
        """
        @summary 签退
        
        @return: SignOutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SignOutHeaders()
        return self.sign_out_with_options(user_id, calendar_id, event_id, headers, runtime)

    async def sign_out_async(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
    ) -> dingtalkcalendar__1__0_models.SignOutResponse:
        """
        @summary 签退
        
        @return: SignOutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SignOutHeaders()
        return await self.sign_out_with_options_async(user_id, calendar_id, event_id, headers, runtime)

    def subscribe_calendar_with_options(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.SubscribeCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SubscribeCalendarResponse:
        """
        @summary 订阅公共日历
        
        @param headers: SubscribeCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SubscribeCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/subscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SubscribeCalendarResponse(),
            self.execute(params, req, runtime)
        )

    async def subscribe_calendar_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.SubscribeCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.SubscribeCalendarResponse:
        """
        @summary 订阅公共日历
        
        @param headers: SubscribeCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='SubscribeCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/subscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='none'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.SubscribeCalendarResponse(),
            await self.execute_async(params, req, runtime)
        )

    def subscribe_calendar(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.SubscribeCalendarResponse:
        """
        @summary 订阅公共日历
        
        @return: SubscribeCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SubscribeCalendarHeaders()
        return self.subscribe_calendar_with_options(user_id, calendar_id, headers, runtime)

    async def subscribe_calendar_async(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.SubscribeCalendarResponse:
        """
        @summary 订阅公共日历
        
        @return: SubscribeCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.SubscribeCalendarHeaders()
        return await self.subscribe_calendar_with_options_async(user_id, calendar_id, headers, runtime)

    def transfer_event_with_options(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.TransferEventRequest,
        headers: dingtalkcalendar__1__0_models.TransferEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.TransferEventResponse:
        """
        @summary 日程转让
        
        @param request: TransferEventRequest
        @param headers: TransferEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_exit_calendar):
            body['isExitCalendar'] = request.is_exit_calendar
        if not UtilClient.is_unset(request.need_notify_via_o2o):
            body['needNotifyViaO2O'] = request.need_notify_via_o2o
        if not UtilClient.is_unset(request.new_organizer_id):
            body['newOrganizerId'] = request.new_organizer_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/transfer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.TransferEventResponse(),
            self.execute(params, req, runtime)
        )

    async def transfer_event_with_options_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.TransferEventRequest,
        headers: dingtalkcalendar__1__0_models.TransferEventHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.TransferEventResponse:
        """
        @summary 日程转让
        
        @param request: TransferEventRequest
        @param headers: TransferEventHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_exit_calendar):
            body['isExitCalendar'] = request.is_exit_calendar
        if not UtilClient.is_unset(request.need_notify_via_o2o):
            body['needNotifyViaO2O'] = request.need_notify_via_o2o
        if not UtilClient.is_unset(request.new_organizer_id):
            body['newOrganizerId'] = request.new_organizer_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_client_token):
            real_headers['x-client-token'] = UtilClient.to_jsonstring(headers.x_client_token)
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferEvent',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/events/{event_id}/transfer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.TransferEventResponse(),
            await self.execute_async(params, req, runtime)
        )

    def transfer_event(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.TransferEventRequest,
    ) -> dingtalkcalendar__1__0_models.TransferEventResponse:
        """
        @summary 日程转让
        
        @param request: TransferEventRequest
        @return: TransferEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.TransferEventHeaders()
        return self.transfer_event_with_options(calendar_id, user_id, event_id, request, headers, runtime)

    async def transfer_event_async(
        self,
        calendar_id: str,
        user_id: str,
        event_id: str,
        request: dingtalkcalendar__1__0_models.TransferEventRequest,
    ) -> dingtalkcalendar__1__0_models.TransferEventResponse:
        """
        @summary 日程转让
        
        @param request: TransferEventRequest
        @return: TransferEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.TransferEventHeaders()
        return await self.transfer_event_with_options_async(calendar_id, user_id, event_id, request, headers, runtime)

    def unsubscribe_calendar_with_options(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.UnsubscribeCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse:
        """
        @summary 取消订阅公共日历
        
        @param headers: UnsubscribeCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnsubscribeCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='UnsubscribeCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/unsubscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse(),
            self.execute(params, req, runtime)
        )

    async def unsubscribe_calendar_with_options_async(
        self,
        user_id: str,
        calendar_id: str,
        headers: dingtalkcalendar__1__0_models.UnsubscribeCalendarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse:
        """
        @summary 取消订阅公共日历
        
        @param headers: UnsubscribeCalendarHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnsubscribeCalendarResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='UnsubscribeCalendar',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/calendars/{calendar_id}/unsubscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse(),
            await self.execute_async(params, req, runtime)
        )

    def unsubscribe_calendar(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse:
        """
        @summary 取消订阅公共日历
        
        @return: UnsubscribeCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.UnsubscribeCalendarHeaders()
        return self.unsubscribe_calendar_with_options(user_id, calendar_id, headers, runtime)

    async def unsubscribe_calendar_async(
        self,
        user_id: str,
        calendar_id: str,
    ) -> dingtalkcalendar__1__0_models.UnsubscribeCalendarResponse:
        """
        @summary 取消订阅公共日历
        
        @return: UnsubscribeCalendarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.UnsubscribeCalendarHeaders()
        return await self.unsubscribe_calendar_with_options_async(user_id, calendar_id, headers, runtime)

    def update_subscribed_calendars_with_options(
        self,
        calendar_id: str,
        user_id: str,
        request: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest,
        headers: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse:
        """
        @summary 更新指定订阅日历
        
        @param request: UpdateSubscribedCalendarsRequest
        @param headers: UpdateSubscribedCalendarsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscribedCalendarsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope):
            body['subscribeScope'] = request.subscribe_scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscribedCalendars',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse(),
            self.execute(params, req, runtime)
        )

    async def update_subscribed_calendars_with_options_async(
        self,
        calendar_id: str,
        user_id: str,
        request: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest,
        headers: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse:
        """
        @summary 更新指定订阅日历
        
        @param request: UpdateSubscribedCalendarsRequest
        @param headers: UpdateSubscribedCalendarsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscribedCalendarsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.managers):
            body['managers'] = request.managers
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope):
            body['subscribeScope'] = request.subscribe_scope
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscribedCalendars',
            version='calendar_1.0',
            protocol='HTTP',
            pathname=f'/v1.0/calendar/users/{user_id}/subscribedCalendars/{calendar_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='none',
            body_type='json'
        )
        return TeaCore.from_map(
            dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_subscribed_calendars(
        self,
        calendar_id: str,
        user_id: str,
        request: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest,
    ) -> dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse:
        """
        @summary 更新指定订阅日历
        
        @param request: UpdateSubscribedCalendarsRequest
        @return: UpdateSubscribedCalendarsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders()
        return self.update_subscribed_calendars_with_options(calendar_id, user_id, request, headers, runtime)

    async def update_subscribed_calendars_async(
        self,
        calendar_id: str,
        user_id: str,
        request: dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest,
    ) -> dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsResponse:
        """
        @summary 更新指定订阅日历
        
        @param request: UpdateSubscribedCalendarsRequest
        @return: UpdateSubscribedCalendarsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders()
        return await self.update_subscribed_calendars_with_options_async(calendar_id, user_id, request, headers, runtime)
