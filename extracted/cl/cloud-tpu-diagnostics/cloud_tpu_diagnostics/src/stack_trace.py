import faulthandler
import logging
import os
import signal
import sys
import time

from cloud_tpu_diagnostics.src.util import default

_stack_trace_file_obj = None
logger = logging.getLogger(__name__)


def user_signal_handler_wrapper(file_descriptor, interval):
  def user_signal_handler(unused_signum, unused_frame):
    message = (
        "INFO: Not a crash. cloud-tpu-diagnostics emits a"
        f" stack trace snapshot every {interval} seconds.\n"
    )
    if file_descriptor is not sys.stderr:
      message = message.encode()
    file_descriptor.write(message)
    faulthandler.dump_traceback(file_descriptor, all_threads=False)

  return user_signal_handler


def enable_stack_trace_dumping(stack_trace_config):
  """Enables stack trace dumping.

  Enables faulthandler and register SIGSEGV, SIGFPE, SIGABRT,
  SIGBUS, SIGILL and SIGUSR1 to collect stack trace.

  Args:
    stack_trace_config: configuration object for stack trace collection
  """
  try:
    global _stack_trace_file_obj
    if stack_trace_config.stack_trace_to_cloud:
      stack_trace_file = _get_stack_trace_file()
      _stack_trace_file_obj = open(stack_trace_file, "wb")
      logger.info("Stack trace will be written in: %s", stack_trace_file)
    else:
      _stack_trace_file_obj = sys.stderr
      logger.info("Stack trace will be written to the console.")

    # Enables faulthandler for SIGSEGV, SIGFPE, SIGABRT, SIGBUS and SIGILL
    faulthandler.enable(file=_stack_trace_file_obj, all_threads=False)

    # Register SIGUSR1 signal to faulthandler
    faulthandler.register(
        signal.SIGUSR1, all_threads=False, file=_stack_trace_file_obj
    )

    # Register handler for SIGUSR1 to dump traces
    signal.signal(
        signal.SIGUSR1,
        user_signal_handler_wrapper(
            _stack_trace_file_obj,
            stack_trace_config.stack_trace_interval_seconds,
        ),
    )
  except Exception as e:  # pylint: disable=broad-exception-caught
    logger.error("Error in enabling dumping of stack trace.", e)


def disable_stack_trace_dumping(stack_trace_config):
  """Disable faulthandler and unregister user signals.

  Args:
    stack_trace_config: configuration object for stack trace collection
  """
  try:
    global _stack_trace_file_obj
    if (
        stack_trace_config.stack_trace_to_cloud
        and _stack_trace_file_obj is not None
    ):
      _stack_trace_file_obj.close()
      _stack_trace_file_obj = None

    faulthandler.unregister(signal.SIGUSR1)
    faulthandler.disable()
  except Exception as e:  # pylint: disable=broad-exception-caught
    logger.error("Error in disabling dumping of stack trace.", e)


def _get_stack_trace_file():
  """Prefix stack trace file.

  Create a file with prefix as stack_trace_ and current local time in
  '%Y_%m_%d_%H_%M_%S' format inside default.STACK_TRACE_DIR_DEFAULT.

  Returns:
    path of stack trace file
  """
  root_trace_folder = os.path.abspath(default.STACK_TRACE_DIR_DEFAULT)
  if not os.path.exists(root_trace_folder):
    os.makedirs(root_trace_folder)

  current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
  trace_file_name = "stack_trace_" + current_time + ".txt"
  stack_trace_file = os.path.join(root_trace_folder, trace_file_name)
  return stack_trace_file
