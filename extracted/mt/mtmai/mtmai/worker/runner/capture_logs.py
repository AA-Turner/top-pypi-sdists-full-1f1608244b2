import asyncio
import contextvars
import functools
import logging
from io import StringIO
from typing import Any, Coroutine

from loguru import logger
from mtmai.clients.events import EventClient

wr: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "workflow_run_id", default=None
)
sr: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "step_run_id", default=None
)


def copy_context_vars(ctx_vars, func, *args, **kwargs):
    for var, value in ctx_vars:
        var.set(value)
    return func(*args, **kwargs)


class InjectingFilter(logging.Filter):
    # For some reason, only the InjectingFilter has access to the contextvars method sr.get(),
    # otherwise we would use emit within the CustomLogHandler
    def filter(self, record):
        record.workflow_run_id = wr.get()
        record.step_run_id = sr.get()

        # 由于传输日志是本身触发 httpx 请求,这里防止死循环 (可能还需要修正)
        if record.name == "httpx" and record.module == "_client":
            return False
        # if "/PutLog " in record.message:
        #     return False
        return True


class CustomLogHandler(logging.StreamHandler):
    def __init__(self, event_client: EventClient, stream=None):
        super().__init__(stream)
        self.event_client = event_client

    async def _log(self, line: str, step_run_id: str | None):
        try:
            if not step_run_id:
                return
            await self.event_client.log(message=line, step_run_id=step_run_id)
        except Exception as e:
            logger.error(f"Error logging: {str(e)}")

    def emit(self, record):
        super().emit(record)

        log_entry = self.format(record)
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            logger.info("No event loop found, creating a new one")
            loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)

        loop.create_task(self._log(log_entry, record.step_run_id))


def capture_logs(
    logger: logging.Logger,
    event_client: EventClient,
    func: Coroutine[Any, Any, Any],
):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # if not logger:
        #     raise Exception("No logger configured on client")

        log_stream = StringIO()
        custom_handler = CustomLogHandler(event_client, log_stream)
        custom_handler.setLevel(logging.INFO)
        custom_handler.addFilter(InjectingFilter())
        logger.addHandler(custom_handler)

        try:
            result = await func(*args, **kwargs)
        finally:
            custom_handler.flush()
            logger.removeHandler(custom_handler)
            log_stream.close()

        return result

    return wrapper
