# generated by datamodel-codegen:
#   filename:  governance/workflows/elements/nodeType.json
#   timestamp: 2025-06-12T10:55:12+00:00

from __future__ import annotations

from enum import Enum


class NodeType(Enum):
    automatedTask = 'automatedTask'
    userTask = 'userTask'
    endEvent = 'endEvent'
    startEvent = 'startEvent'
    gateway = 'gateway'
