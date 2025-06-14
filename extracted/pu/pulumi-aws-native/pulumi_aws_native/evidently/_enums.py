# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import pulumi
from enum import Enum

__all__ = [
    'ExperimentMetricGoalObjectDesiredChange',
    'FeatureEvaluationStrategy',
]


@pulumi.type_token("aws-native:evidently:ExperimentMetricGoalObjectDesiredChange")
class ExperimentMetricGoalObjectDesiredChange(builtins.str, Enum):
    """
    `INCREASE` means that a variation with a higher number for this metric is performing better.

    `DECREASE` means that a variation with a lower number for this metric is performing better.
    """
    INCREASE = "INCREASE"
    DECREASE = "DECREASE"


@pulumi.type_token("aws-native:evidently:FeatureEvaluationStrategy")
class FeatureEvaluationStrategy(builtins.str, Enum):
    """
    Specify `ALL_RULES` to activate the traffic allocation specified by any ongoing launches or experiments. Specify `DEFAULT_VARIATION` to serve the default variation to all users instead.
    """
    ALL_RULES = "ALL_RULES"
    DEFAULT_VARIATION = "DEFAULT_VARIATION"
