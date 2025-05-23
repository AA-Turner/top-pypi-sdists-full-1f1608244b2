# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ApprovalTask(object):
    _types = {
        "id": str,
        "task_status": str,
        "task_start_time": str,
        "task_end_time": str,
        "form_data": str,
        "approval_logic": str,
        "approvers": List[str],
        "assigners": List[str],
        "task_url": str,
        "task_type": str,
        "free_cc_record": str,
        "add_assignee_record": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.task_status: Optional[str] = None
        self.task_start_time: Optional[str] = None
        self.task_end_time: Optional[str] = None
        self.form_data: Optional[str] = None
        self.approval_logic: Optional[str] = None
        self.approvers: Optional[List[str]] = None
        self.assigners: Optional[List[str]] = None
        self.task_url: Optional[str] = None
        self.task_type: Optional[str] = None
        self.free_cc_record: Optional[str] = None
        self.add_assignee_record: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalTaskBuilder":
        return ApprovalTaskBuilder()


class ApprovalTaskBuilder(object):
    def __init__(self) -> None:
        self._approval_task = ApprovalTask()

    def id(self, id: str) -> "ApprovalTaskBuilder":
        self._approval_task.id = id
        return self

    def task_status(self, task_status: str) -> "ApprovalTaskBuilder":
        self._approval_task.task_status = task_status
        return self

    def task_start_time(self, task_start_time: str) -> "ApprovalTaskBuilder":
        self._approval_task.task_start_time = task_start_time
        return self

    def task_end_time(self, task_end_time: str) -> "ApprovalTaskBuilder":
        self._approval_task.task_end_time = task_end_time
        return self

    def form_data(self, form_data: str) -> "ApprovalTaskBuilder":
        self._approval_task.form_data = form_data
        return self

    def approval_logic(self, approval_logic: str) -> "ApprovalTaskBuilder":
        self._approval_task.approval_logic = approval_logic
        return self

    def approvers(self, approvers: List[str]) -> "ApprovalTaskBuilder":
        self._approval_task.approvers = approvers
        return self

    def assigners(self, assigners: List[str]) -> "ApprovalTaskBuilder":
        self._approval_task.assigners = assigners
        return self

    def task_url(self, task_url: str) -> "ApprovalTaskBuilder":
        self._approval_task.task_url = task_url
        return self

    def task_type(self, task_type: str) -> "ApprovalTaskBuilder":
        self._approval_task.task_type = task_type
        return self

    def free_cc_record(self, free_cc_record: str) -> "ApprovalTaskBuilder":
        self._approval_task.free_cc_record = free_cc_record
        return self

    def add_assignee_record(self, add_assignee_record: str) -> "ApprovalTaskBuilder":
        self._approval_task.add_assignee_record = add_assignee_record
        return self

    def build(self) -> "ApprovalTask":
        return self._approval_task
