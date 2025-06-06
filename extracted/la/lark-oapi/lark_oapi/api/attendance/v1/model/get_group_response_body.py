# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .anti_cheat_config import AntiCheatConfig
from .machine import Machine
from .location import Location
from .free_punch_cfg import FreePunchCfg
from .punch_special_date_shift import PunchSpecialDateShift
from .punch_special_date_shift import PunchSpecialDateShift
from .member_status_change import MemberStatusChange
from .leave_need_punch_cfg import LeaveNeedPunchCfg
from .leave_need_punch_cfg import LeaveNeedPunchCfg
from .leave_need_punch_cfg import LeaveNeedPunchCfg
from .punch_member import PunchMember
from .punch_member import PunchMember
from .overtime_clock_cfg import OvertimeClockCfg
from .clock_in_abnormal_settings import ClockInAbnormalSettings


class GetGroupResponseBody(object):
    _types = {
        "group_id": str,
        "group_name": str,
        "time_zone": str,
        "bind_dept_ids": List[str],
        "except_dept_ids": List[str],
        "bind_user_ids": List[str],
        "except_user_ids": List[str],
        "group_leader_ids": List[str],
        "sub_group_leader_ids": List[str],
        "allow_out_punch": bool,
        "out_punch_need_approval": bool,
        "out_punch_need_post_approval": bool,
        "out_punch_need_remark": bool,
        "out_punch_need_photo": bool,
        "out_punch_allowed_hide_addr": bool,
        "out_punch_allowed_adjust_addr": bool,
        "adjust_range": int,
        "allow_pc_punch": bool,
        "allow_remedy": bool,
        "remedy_limit": bool,
        "remedy_limit_count": int,
        "remedy_date_limit": bool,
        "remedy_date_num": int,
        "allow_remedy_type_lack": bool,
        "allow_remedy_type_late": bool,
        "allow_remedy_type_early": bool,
        "allow_remedy_type_normal": bool,
        "show_cumulative_time": bool,
        "show_over_time": bool,
        "hide_staff_punch_time": bool,
        "hide_clock_in_rule": bool,
        "face_punch": bool,
        "face_punch_cfg": int,
        "face_live_need_action": bool,
        "face_downgrade": bool,
        "replace_basic_pic": bool,
        "anti_cheat_punch_config": AntiCheatConfig,
        "machines": List[Machine],
        "gps_range": int,
        "locations": List[Location],
        "group_type": int,
        "punch_day_shift_ids": List[str],
        "free_punch_cfg": FreePunchCfg,
        "calendar_id": int,
        "need_punch_special_days": List[PunchSpecialDateShift],
        "no_need_punch_special_days": List[PunchSpecialDateShift],
        "work_day_no_punch_as_lack": bool,
        "remedy_period_type": int,
        "remedy_period_custom_date": int,
        "punch_type": int,
        "effect_time": str,
        "fixshift_effect_time": str,
        "member_effect_time": str,
        "rest_clock_in_need_approval": bool,
        "clock_in_need_photo": bool,
        "member_status_change": MemberStatusChange,
        "leave_need_punch": bool,
        "leave_need_punch_cfg": LeaveNeedPunchCfg,
        "go_out_need_punch": int,
        "go_out_need_punch_cfg": LeaveNeedPunchCfg,
        "travel_need_punch": int,
        "travel_need_punch_cfg": LeaveNeedPunchCfg,
        "need_punch_members": List[PunchMember],
        "no_need_punch_members": List[PunchMember],
        "save_auto_changes": bool,
        "org_change_auto_adjust": bool,
        "bind_default_dept_ids": List[str],
        "bind_default_user_ids": List[str],
        "overtime_clock_cfg": OvertimeClockCfg,
        "new_calendar_id": str,
        "allow_apply_punch": bool,
        "clock_in_abnormal_settings": ClockInAbnormalSettings,
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.group_name: Optional[str] = None
        self.time_zone: Optional[str] = None
        self.bind_dept_ids: Optional[List[str]] = None
        self.except_dept_ids: Optional[List[str]] = None
        self.bind_user_ids: Optional[List[str]] = None
        self.except_user_ids: Optional[List[str]] = None
        self.group_leader_ids: Optional[List[str]] = None
        self.sub_group_leader_ids: Optional[List[str]] = None
        self.allow_out_punch: Optional[bool] = None
        self.out_punch_need_approval: Optional[bool] = None
        self.out_punch_need_post_approval: Optional[bool] = None
        self.out_punch_need_remark: Optional[bool] = None
        self.out_punch_need_photo: Optional[bool] = None
        self.out_punch_allowed_hide_addr: Optional[bool] = None
        self.out_punch_allowed_adjust_addr: Optional[bool] = None
        self.adjust_range: Optional[int] = None
        self.allow_pc_punch: Optional[bool] = None
        self.allow_remedy: Optional[bool] = None
        self.remedy_limit: Optional[bool] = None
        self.remedy_limit_count: Optional[int] = None
        self.remedy_date_limit: Optional[bool] = None
        self.remedy_date_num: Optional[int] = None
        self.allow_remedy_type_lack: Optional[bool] = None
        self.allow_remedy_type_late: Optional[bool] = None
        self.allow_remedy_type_early: Optional[bool] = None
        self.allow_remedy_type_normal: Optional[bool] = None
        self.show_cumulative_time: Optional[bool] = None
        self.show_over_time: Optional[bool] = None
        self.hide_staff_punch_time: Optional[bool] = None
        self.hide_clock_in_rule: Optional[bool] = None
        self.face_punch: Optional[bool] = None
        self.face_punch_cfg: Optional[int] = None
        self.face_live_need_action: Optional[bool] = None
        self.face_downgrade: Optional[bool] = None
        self.replace_basic_pic: Optional[bool] = None
        self.anti_cheat_punch_config: Optional[AntiCheatConfig] = None
        self.machines: Optional[List[Machine]] = None
        self.gps_range: Optional[int] = None
        self.locations: Optional[List[Location]] = None
        self.group_type: Optional[int] = None
        self.punch_day_shift_ids: Optional[List[str]] = None
        self.free_punch_cfg: Optional[FreePunchCfg] = None
        self.calendar_id: Optional[int] = None
        self.need_punch_special_days: Optional[List[PunchSpecialDateShift]] = None
        self.no_need_punch_special_days: Optional[List[PunchSpecialDateShift]] = None
        self.work_day_no_punch_as_lack: Optional[bool] = None
        self.remedy_period_type: Optional[int] = None
        self.remedy_period_custom_date: Optional[int] = None
        self.punch_type: Optional[int] = None
        self.effect_time: Optional[str] = None
        self.fixshift_effect_time: Optional[str] = None
        self.member_effect_time: Optional[str] = None
        self.rest_clock_in_need_approval: Optional[bool] = None
        self.clock_in_need_photo: Optional[bool] = None
        self.member_status_change: Optional[MemberStatusChange] = None
        self.leave_need_punch: Optional[bool] = None
        self.leave_need_punch_cfg: Optional[LeaveNeedPunchCfg] = None
        self.go_out_need_punch: Optional[int] = None
        self.go_out_need_punch_cfg: Optional[LeaveNeedPunchCfg] = None
        self.travel_need_punch: Optional[int] = None
        self.travel_need_punch_cfg: Optional[LeaveNeedPunchCfg] = None
        self.need_punch_members: Optional[List[PunchMember]] = None
        self.no_need_punch_members: Optional[List[PunchMember]] = None
        self.save_auto_changes: Optional[bool] = None
        self.org_change_auto_adjust: Optional[bool] = None
        self.bind_default_dept_ids: Optional[List[str]] = None
        self.bind_default_user_ids: Optional[List[str]] = None
        self.overtime_clock_cfg: Optional[OvertimeClockCfg] = None
        self.new_calendar_id: Optional[str] = None
        self.allow_apply_punch: Optional[bool] = None
        self.clock_in_abnormal_settings: Optional[ClockInAbnormalSettings] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetGroupResponseBodyBuilder":
        return GetGroupResponseBodyBuilder()


class GetGroupResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_group_response_body = GetGroupResponseBody()

    def group_id(self, group_id: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group_id = group_id
        return self

    def group_name(self, group_name: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group_name = group_name
        return self

    def time_zone(self, time_zone: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.time_zone = time_zone
        return self

    def bind_dept_ids(self, bind_dept_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.bind_dept_ids = bind_dept_ids
        return self

    def except_dept_ids(self, except_dept_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.except_dept_ids = except_dept_ids
        return self

    def bind_user_ids(self, bind_user_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.bind_user_ids = bind_user_ids
        return self

    def except_user_ids(self, except_user_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.except_user_ids = except_user_ids
        return self

    def group_leader_ids(self, group_leader_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group_leader_ids = group_leader_ids
        return self

    def sub_group_leader_ids(self, sub_group_leader_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.sub_group_leader_ids = sub_group_leader_ids
        return self

    def allow_out_punch(self, allow_out_punch: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_out_punch = allow_out_punch
        return self

    def out_punch_need_approval(self, out_punch_need_approval: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_need_approval = out_punch_need_approval
        return self

    def out_punch_need_post_approval(self, out_punch_need_post_approval: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_need_post_approval = out_punch_need_post_approval
        return self

    def out_punch_need_remark(self, out_punch_need_remark: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_need_remark = out_punch_need_remark
        return self

    def out_punch_need_photo(self, out_punch_need_photo: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_need_photo = out_punch_need_photo
        return self

    def out_punch_allowed_hide_addr(self, out_punch_allowed_hide_addr: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_allowed_hide_addr = out_punch_allowed_hide_addr
        return self

    def out_punch_allowed_adjust_addr(self, out_punch_allowed_adjust_addr: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.out_punch_allowed_adjust_addr = out_punch_allowed_adjust_addr
        return self

    def adjust_range(self, adjust_range: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.adjust_range = adjust_range
        return self

    def allow_pc_punch(self, allow_pc_punch: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_pc_punch = allow_pc_punch
        return self

    def allow_remedy(self, allow_remedy: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_remedy = allow_remedy
        return self

    def remedy_limit(self, remedy_limit: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_limit = remedy_limit
        return self

    def remedy_limit_count(self, remedy_limit_count: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_limit_count = remedy_limit_count
        return self

    def remedy_date_limit(self, remedy_date_limit: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_date_limit = remedy_date_limit
        return self

    def remedy_date_num(self, remedy_date_num: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_date_num = remedy_date_num
        return self

    def allow_remedy_type_lack(self, allow_remedy_type_lack: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_remedy_type_lack = allow_remedy_type_lack
        return self

    def allow_remedy_type_late(self, allow_remedy_type_late: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_remedy_type_late = allow_remedy_type_late
        return self

    def allow_remedy_type_early(self, allow_remedy_type_early: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_remedy_type_early = allow_remedy_type_early
        return self

    def allow_remedy_type_normal(self, allow_remedy_type_normal: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_remedy_type_normal = allow_remedy_type_normal
        return self

    def show_cumulative_time(self, show_cumulative_time: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.show_cumulative_time = show_cumulative_time
        return self

    def show_over_time(self, show_over_time: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.show_over_time = show_over_time
        return self

    def hide_staff_punch_time(self, hide_staff_punch_time: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.hide_staff_punch_time = hide_staff_punch_time
        return self

    def hide_clock_in_rule(self, hide_clock_in_rule: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.hide_clock_in_rule = hide_clock_in_rule
        return self

    def face_punch(self, face_punch: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.face_punch = face_punch
        return self

    def face_punch_cfg(self, face_punch_cfg: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.face_punch_cfg = face_punch_cfg
        return self

    def face_live_need_action(self, face_live_need_action: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.face_live_need_action = face_live_need_action
        return self

    def face_downgrade(self, face_downgrade: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.face_downgrade = face_downgrade
        return self

    def replace_basic_pic(self, replace_basic_pic: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.replace_basic_pic = replace_basic_pic
        return self

    def anti_cheat_punch_config(self, anti_cheat_punch_config: AntiCheatConfig) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.anti_cheat_punch_config = anti_cheat_punch_config
        return self

    def machines(self, machines: List[Machine]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.machines = machines
        return self

    def gps_range(self, gps_range: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.gps_range = gps_range
        return self

    def locations(self, locations: List[Location]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.locations = locations
        return self

    def group_type(self, group_type: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group_type = group_type
        return self

    def punch_day_shift_ids(self, punch_day_shift_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.punch_day_shift_ids = punch_day_shift_ids
        return self

    def free_punch_cfg(self, free_punch_cfg: FreePunchCfg) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.free_punch_cfg = free_punch_cfg
        return self

    def calendar_id(self, calendar_id: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.calendar_id = calendar_id
        return self

    def need_punch_special_days(self,
                                need_punch_special_days: List[PunchSpecialDateShift]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.need_punch_special_days = need_punch_special_days
        return self

    def no_need_punch_special_days(self, no_need_punch_special_days: List[
        PunchSpecialDateShift]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.no_need_punch_special_days = no_need_punch_special_days
        return self

    def work_day_no_punch_as_lack(self, work_day_no_punch_as_lack: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.work_day_no_punch_as_lack = work_day_no_punch_as_lack
        return self

    def remedy_period_type(self, remedy_period_type: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_period_type = remedy_period_type
        return self

    def remedy_period_custom_date(self, remedy_period_custom_date: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.remedy_period_custom_date = remedy_period_custom_date
        return self

    def punch_type(self, punch_type: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.punch_type = punch_type
        return self

    def effect_time(self, effect_time: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.effect_time = effect_time
        return self

    def fixshift_effect_time(self, fixshift_effect_time: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.fixshift_effect_time = fixshift_effect_time
        return self

    def member_effect_time(self, member_effect_time: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.member_effect_time = member_effect_time
        return self

    def rest_clock_in_need_approval(self, rest_clock_in_need_approval: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.rest_clock_in_need_approval = rest_clock_in_need_approval
        return self

    def clock_in_need_photo(self, clock_in_need_photo: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.clock_in_need_photo = clock_in_need_photo
        return self

    def member_status_change(self, member_status_change: MemberStatusChange) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.member_status_change = member_status_change
        return self

    def leave_need_punch(self, leave_need_punch: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.leave_need_punch = leave_need_punch
        return self

    def leave_need_punch_cfg(self, leave_need_punch_cfg: LeaveNeedPunchCfg) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.leave_need_punch_cfg = leave_need_punch_cfg
        return self

    def go_out_need_punch(self, go_out_need_punch: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.go_out_need_punch = go_out_need_punch
        return self

    def go_out_need_punch_cfg(self, go_out_need_punch_cfg: LeaveNeedPunchCfg) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.go_out_need_punch_cfg = go_out_need_punch_cfg
        return self

    def travel_need_punch(self, travel_need_punch: int) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.travel_need_punch = travel_need_punch
        return self

    def travel_need_punch_cfg(self, travel_need_punch_cfg: LeaveNeedPunchCfg) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.travel_need_punch_cfg = travel_need_punch_cfg
        return self

    def need_punch_members(self, need_punch_members: List[PunchMember]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.need_punch_members = need_punch_members
        return self

    def no_need_punch_members(self, no_need_punch_members: List[PunchMember]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.no_need_punch_members = no_need_punch_members
        return self

    def save_auto_changes(self, save_auto_changes: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.save_auto_changes = save_auto_changes
        return self

    def org_change_auto_adjust(self, org_change_auto_adjust: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.org_change_auto_adjust = org_change_auto_adjust
        return self

    def bind_default_dept_ids(self, bind_default_dept_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.bind_default_dept_ids = bind_default_dept_ids
        return self

    def bind_default_user_ids(self, bind_default_user_ids: List[str]) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.bind_default_user_ids = bind_default_user_ids
        return self

    def overtime_clock_cfg(self, overtime_clock_cfg: OvertimeClockCfg) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.overtime_clock_cfg = overtime_clock_cfg
        return self

    def new_calendar_id(self, new_calendar_id: str) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.new_calendar_id = new_calendar_id
        return self

    def allow_apply_punch(self, allow_apply_punch: bool) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.allow_apply_punch = allow_apply_punch
        return self

    def clock_in_abnormal_settings(self,
                                   clock_in_abnormal_settings: ClockInAbnormalSettings) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.clock_in_abnormal_settings = clock_in_abnormal_settings
        return self

    def build(self) -> "GetGroupResponseBody":
        return self._get_group_response_body
