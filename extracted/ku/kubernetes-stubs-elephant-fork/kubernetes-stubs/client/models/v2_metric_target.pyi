import datetime
import typing

import kubernetes.client

class V2MetricTarget:
    average_utilization: typing.Optional[int]
    average_value: typing.Optional[str]
    type: str
    value: typing.Optional[str]
    
    def __init__(self, *, average_utilization: typing.Optional[int] = ..., average_value: typing.Optional[str] = ..., type: str, value: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V2MetricTargetDict:
        ...
class V2MetricTargetDict(typing.TypedDict, total=False):
    averageUtilization: typing.Optional[int]
    averageValue: typing.Optional[str]
    type: str
    value: typing.Optional[str]
