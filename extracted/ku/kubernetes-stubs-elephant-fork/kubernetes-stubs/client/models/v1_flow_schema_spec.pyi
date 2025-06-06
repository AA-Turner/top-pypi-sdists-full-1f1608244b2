import datetime
import typing

import kubernetes.client

class V1FlowSchemaSpec:
    distinguisher_method: typing.Optional[kubernetes.client.V1FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes.client.V1PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes.client.V1PolicyRulesWithSubjects]]
    
    def __init__(self, *, distinguisher_method: typing.Optional[kubernetes.client.V1FlowDistinguisherMethod] = ..., matching_precedence: typing.Optional[int] = ..., priority_level_configuration: kubernetes.client.V1PriorityLevelConfigurationReference, rules: typing.Optional[list[kubernetes.client.V1PolicyRulesWithSubjects]] = ...) -> None:
        ...
    def to_dict(self) -> V1FlowSchemaSpecDict:
        ...
class V1FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[kubernetes.client.V1FlowDistinguisherMethodDict]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: kubernetes.client.V1PriorityLevelConfigurationReferenceDict
    rules: typing.Optional[list[kubernetes.client.V1PolicyRulesWithSubjectsDict]]
