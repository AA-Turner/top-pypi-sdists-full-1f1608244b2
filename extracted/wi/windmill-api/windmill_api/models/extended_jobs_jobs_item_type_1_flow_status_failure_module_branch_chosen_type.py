from enum import Enum


class ExtendedJobsJobsItemType1FlowStatusFailureModuleBranchChosenType(str, Enum):
    BRANCH = "branch"
    DEFAULT = "default"

    def __str__(self) -> str:
        return str(self.value)
