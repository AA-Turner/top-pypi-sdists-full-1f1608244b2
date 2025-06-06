# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .combined_job_result_default_job_post import CombinedJobResultDefaultJobPost
from .job import Job
from .job_manager import JobManager
from .registration_schema_info import RegistrationSchemaInfo
from .registration_schema_info import RegistrationSchemaInfo
from .target_major_info import TargetMajorInfo
from .registration_schema_info import RegistrationSchemaInfo


class CombinedCreateJobResponseBody(object):
    _types = {
        "default_job_post": CombinedJobResultDefaultJobPost,
        "job": Job,
        "job_manager": JobManager,
        "interview_registration_schema_info": RegistrationSchemaInfo,
        "onboard_registration_schema_info": RegistrationSchemaInfo,
        "target_major_list": List[TargetMajorInfo],
        "portal_website_apply_form_schema_info": RegistrationSchemaInfo,
    }

    def __init__(self, d=None):
        self.default_job_post: Optional[CombinedJobResultDefaultJobPost] = None
        self.job: Optional[Job] = None
        self.job_manager: Optional[JobManager] = None
        self.interview_registration_schema_info: Optional[RegistrationSchemaInfo] = None
        self.onboard_registration_schema_info: Optional[RegistrationSchemaInfo] = None
        self.target_major_list: Optional[List[TargetMajorInfo]] = None
        self.portal_website_apply_form_schema_info: Optional[RegistrationSchemaInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedCreateJobResponseBodyBuilder":
        return CombinedCreateJobResponseBodyBuilder()


class CombinedCreateJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._combined_create_job_response_body = CombinedCreateJobResponseBody()

    def default_job_post(self,
                         default_job_post: CombinedJobResultDefaultJobPost) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.default_job_post = default_job_post
        return self

    def job(self, job: Job) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.job = job
        return self

    def job_manager(self, job_manager: JobManager) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.job_manager = job_manager
        return self

    def interview_registration_schema_info(self,
                                           interview_registration_schema_info: RegistrationSchemaInfo) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.interview_registration_schema_info = interview_registration_schema_info
        return self

    def onboard_registration_schema_info(self,
                                         onboard_registration_schema_info: RegistrationSchemaInfo) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.onboard_registration_schema_info = onboard_registration_schema_info
        return self

    def target_major_list(self, target_major_list: List[TargetMajorInfo]) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.target_major_list = target_major_list
        return self

    def portal_website_apply_form_schema_info(self,
                                              portal_website_apply_form_schema_info: RegistrationSchemaInfo) -> "CombinedCreateJobResponseBodyBuilder":
        self._combined_create_job_response_body.portal_website_apply_form_schema_info = portal_website_apply_form_schema_info
        return self

    def build(self) -> "CombinedCreateJobResponseBody":
        return self._combined_create_job_response_body
