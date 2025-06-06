"""Configuration of logging."""

import logging
import logging.config
import sys
from sys import stderr
from typing import Optional

from loguru import logger


def setup_logging(
    console_log_level: str = "INFO",
    log_file: Optional[str] = None,
    file_log_level: str = "ERROR",
) -> None:
    """Setup logging configuration. Intercepts standard logging and outputs
    errors to a file.

    Args:
        console_log_level (str): Log level to use for console output. Defaults to INFO.
        log_file (Optional[str]): Path of log file. Defaults to None (No log file).
        file_log_level (str): Log level to use for console output. Defaults to ERROR.

    Returns:
        None
    """
    logger.remove()
    logger.add(
        stderr,
        level=console_log_level,
        colorize=True,
        backtrace=True,
        diagnose=True,
    )
    if log_file:
        logger.add(
            log_file,
            level=file_log_level,
            mode="w",
            backtrace=True,
            diagnose=True,
        )

    class InterceptHandler(logging.Handler):
        def emit(self, record):
            # Get corresponding Loguru level if it exists.
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            # Find caller from where originated the logged message.
            frame, depth = sys._getframe(6), 6
            while frame and frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1

            msg = record.getMessage()
            try:
                logger.opt(colors=True, depth=depth, exception=record.exc_info).log(
                    level, msg
                )
            except ValueError:
                logger.opt(colors=False, depth=depth, exception=record.exc_info).log(
                    level, msg
                )

    root_logger = logging.getLogger()
    while root_logger.hasHandlers():
        root_logger.removeHandler(root_logger.handlers[0])
    root_logger.setLevel(logging.NOTSET)
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
