# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .dimension_info import DimensionInfo
from .workforce_plan_eai_detail import WorkforcePlanEaiDetail


class WorkforcePlanDetail(object):
    _types = {
        "workforce_plan_detail_id": str,
        "department": DimensionInfo,
        "employee_type": DimensionInfo,
        "work_location": DimensionInfo,
        "job_family": DimensionInfo,
        "job_level": DimensionInfo,
        "job": DimensionInfo,
        "cost_center": DimensionInfo,
        "workforce_plan": str,
        "active_individuals": str,
        "individuals_to_be_added": str,
        "individuals_to_be_removed": str,
        "vacancy": str,
        "vacancy_including_individuals_to_be_added_and_removed": str,
        "fulfillment_rate": str,
        "fulfillment_rate_including_individuals_to_be_added_and_removed": str,
        "estimated_active_individuals_detail": List[WorkforcePlanEaiDetail],
        "is_missing_dimension": bool,
    }

    def __init__(self, d=None):
        self.workforce_plan_detail_id: Optional[str] = None
        self.department: Optional[DimensionInfo] = None
        self.employee_type: Optional[DimensionInfo] = None
        self.work_location: Optional[DimensionInfo] = None
        self.job_family: Optional[DimensionInfo] = None
        self.job_level: Optional[DimensionInfo] = None
        self.job: Optional[DimensionInfo] = None
        self.cost_center: Optional[DimensionInfo] = None
        self.workforce_plan: Optional[str] = None
        self.active_individuals: Optional[str] = None
        self.individuals_to_be_added: Optional[str] = None
        self.individuals_to_be_removed: Optional[str] = None
        self.vacancy: Optional[str] = None
        self.vacancy_including_individuals_to_be_added_and_removed: Optional[str] = None
        self.fulfillment_rate: Optional[str] = None
        self.fulfillment_rate_including_individuals_to_be_added_and_removed: Optional[str] = None
        self.estimated_active_individuals_detail: Optional[List[WorkforcePlanEaiDetail]] = None
        self.is_missing_dimension: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkforcePlanDetailBuilder":
        return WorkforcePlanDetailBuilder()


class WorkforcePlanDetailBuilder(object):
    def __init__(self) -> None:
        self._workforce_plan_detail = WorkforcePlanDetail()

    def workforce_plan_detail_id(self, workforce_plan_detail_id: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.workforce_plan_detail_id = workforce_plan_detail_id
        return self

    def department(self, department: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.department = department
        return self

    def employee_type(self, employee_type: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.employee_type = employee_type
        return self

    def work_location(self, work_location: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.work_location = work_location
        return self

    def job_family(self, job_family: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.job_family = job_family
        return self

    def job_level(self, job_level: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.job_level = job_level
        return self

    def job(self, job: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.job = job
        return self

    def cost_center(self, cost_center: DimensionInfo) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.cost_center = cost_center
        return self

    def workforce_plan(self, workforce_plan: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.workforce_plan = workforce_plan
        return self

    def active_individuals(self, active_individuals: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.active_individuals = active_individuals
        return self

    def individuals_to_be_added(self, individuals_to_be_added: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.individuals_to_be_added = individuals_to_be_added
        return self

    def individuals_to_be_removed(self, individuals_to_be_removed: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.individuals_to_be_removed = individuals_to_be_removed
        return self

    def vacancy(self, vacancy: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.vacancy = vacancy
        return self

    def vacancy_including_individuals_to_be_added_and_removed(self,
                                                              vacancy_including_individuals_to_be_added_and_removed: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.vacancy_including_individuals_to_be_added_and_removed = vacancy_including_individuals_to_be_added_and_removed
        return self

    def fulfillment_rate(self, fulfillment_rate: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.fulfillment_rate = fulfillment_rate
        return self

    def fulfillment_rate_including_individuals_to_be_added_and_removed(self,
                                                                       fulfillment_rate_including_individuals_to_be_added_and_removed: str) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.fulfillment_rate_including_individuals_to_be_added_and_removed = fulfillment_rate_including_individuals_to_be_added_and_removed
        return self

    def estimated_active_individuals_detail(self, estimated_active_individuals_detail: List[
        WorkforcePlanEaiDetail]) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.estimated_active_individuals_detail = estimated_active_individuals_detail
        return self

    def is_missing_dimension(self, is_missing_dimension: bool) -> "WorkforcePlanDetailBuilder":
        self._workforce_plan_detail.is_missing_dimension = is_missing_dimension
        return self

    def build(self) -> "WorkforcePlanDetail":
        return self._workforce_plan_detail
