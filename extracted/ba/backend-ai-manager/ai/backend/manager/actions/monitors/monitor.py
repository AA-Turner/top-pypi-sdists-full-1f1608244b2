from abc import ABC

from ..action import BaseAction, BaseActionTriggerMeta, ProcessResult


class ActionMonitor(ABC):
    async def prepare(self, action: BaseAction, meta: BaseActionTriggerMeta) -> None:
        pass

    async def done(self, action: BaseAction, result: ProcessResult) -> None:
        pass
