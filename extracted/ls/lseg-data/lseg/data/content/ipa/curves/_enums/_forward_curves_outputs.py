from enum import unique

from ....._base_enum import StrEnum


@unique
class ForwardCurvesOutputs(StrEnum):
    CONSTITUENTS = "Constituents"
