"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class RuleSuiteType(TypedDict):
    """Rule Suite

    Response
    """

    id: NotRequired[int]
    actor_id: NotRequired[Union[int, None]]
    actor_name: NotRequired[Union[str, None]]
    before_sha: NotRequired[str]
    after_sha: NotRequired[str]
    ref: NotRequired[str]
    repository_id: NotRequired[int]
    repository_name: NotRequired[str]
    pushed_at: NotRequired[datetime]
    result: NotRequired[Literal["pass", "fail", "bypass"]]
    evaluation_result: NotRequired[Union[None, Literal["pass", "fail", "bypass"]]]
    rule_evaluations: NotRequired[list[RuleSuitePropRuleEvaluationsItemsType]]


class RuleSuitePropRuleEvaluationsItemsType(TypedDict):
    """RuleSuitePropRuleEvaluationsItems"""

    rule_source: NotRequired[RuleSuitePropRuleEvaluationsItemsPropRuleSourceType]
    enforcement: NotRequired[Literal["active", "evaluate", "deleted ruleset"]]
    result: NotRequired[Literal["pass", "fail"]]
    rule_type: NotRequired[str]
    details: NotRequired[Union[str, None]]


class RuleSuitePropRuleEvaluationsItemsPropRuleSourceType(TypedDict):
    """RuleSuitePropRuleEvaluationsItemsPropRuleSource"""

    type: NotRequired[str]
    id: NotRequired[Union[int, None]]
    name: NotRequired[Union[str, None]]


__all__ = (
    "RuleSuitePropRuleEvaluationsItemsPropRuleSourceType",
    "RuleSuitePropRuleEvaluationsItemsType",
    "RuleSuiteType",
)
