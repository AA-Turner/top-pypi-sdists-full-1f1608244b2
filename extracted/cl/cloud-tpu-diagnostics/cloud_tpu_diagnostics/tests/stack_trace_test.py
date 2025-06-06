import faulthandler
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import textwrap
import unittest
from absl.testing import absltest
from cloud_tpu_diagnostics.src.config import stack_trace_configuration
from cloud_tpu_diagnostics.src.stack_trace import disable_stack_trace_dumping
from cloud_tpu_diagnostics.src.stack_trace import enable_stack_trace_dumping
from cloud_tpu_diagnostics.src.stack_trace import user_signal_handler_wrapper
from cloud_tpu_diagnostics.src.util import default

class StackTraceTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    package_dir = '/'.join(os.path.dirname(__file__).split('/')[:-1])
    # Used to run test with blaze/bazel
    self.test_binary = os.path.join(package_dir, 'stack_trace_test_util')
    # Used to run test with unittest `python3 -m unittest stack_trace_test.py`
    self.test_file = os.path.join(
        package_dir, 'src/util/stack_trace_test_util.py'
    )
    self.stack_trace_module = os.path.join(package_dir, 'src/stack_trace.py')

  def tearDown(self):
    super().tearDown()
    if os.path.exists(default.STACK_TRACE_DIR_DEFAULT):
      shutil.rmtree(default.STACK_TRACE_DIR_DEFAULT)

  @unittest.skipIf(not hasattr(signal, 'SIGSEGV'), 'Missing signal.SIGSEGV')
  def testSigsegvCollectStackTraceTrueTraceCollectedOnCloud(self):
    error = 'Fatal Python error: Segmentation fault'
    self.check_fatal_error(52, error, 'SIGSEGV', True)

  @unittest.skipIf(not hasattr(signal, 'SIGABRT'), 'Missing signal.SIGABRT')
  def testSigabrtCollectStackTraceTrueTraceCollectedOnCloud(self):
    error = 'Fatal Python error: Aborted'
    self.check_fatal_error(55, error, 'SIGABRT', True)

  @unittest.skipIf(not hasattr(signal, 'SIGFPE'), 'Missing signal.SIGFPE')
  def testSigfpeCollectStackTraceTrueTraceCollectedOnCloud(self):
    error = 'Fatal Python error: Floating point exception'
    self.check_fatal_error(58, error, 'SIGFPE', True)

  @unittest.skipIf(not hasattr(signal, 'SIGILL'), 'Missing signal.SIGILL')
  def testSigillCollectStackTraceTrueTraceCollectedOnCloud(self):
    error = 'Fatal Python error: Illegal instruction'
    self.check_fatal_error(61, error, 'SIGILL', True)

  @unittest.skipIf(not hasattr(signal, 'SIGBUS'), 'Missing signal.SIGBUS')
  def testSigbusCollectStackTraceTrueTraceCollectedOnCloud(self):
    error = 'Fatal Python error: Bus error'
    self.check_fatal_error(64, error, 'SIGBUS', True)

  @unittest.skipIf(not hasattr(signal, 'SIGUSR1'), 'Missing signal.SIGUSR1')
  def testSigusrCollectStackTraceTrueTraceCollectedOnCloud(self):
    self.check_fatal_error(67, '', 'SIGUSR1', True)

  def testCollectStackTraceFalseNoTraceDirCreated(self):
    process = self.run_python_code('', False, True)
    _, stderr = process.communicate()
    self.assertFalse(os.path.exists(default.STACK_TRACE_DIR_DEFAULT))
    self.assertEmpty(stderr)

  @unittest.skipIf(not hasattr(signal, 'SIGUSR1'), 'Missing signal.SIGUSR1')
  def testCollectStackTraceToConsole(self):
    self.check_fatal_error(67, '', 'SIGUSR1', False)

  def testCollectStackTraceFalseNoTraceCollectedOnConsole(self):
    process = self.run_python_code('', False, False)
    _, stderr = process.communicate()
    self.assertEmpty(stderr)

  def testEnableStackTraceDumpingFaulthandlerEnabled(self):
    stack_trace_config = stack_trace_configuration.StackTraceConfig(
        collect_stack_trace=True, stack_trace_to_cloud=True
    )
    with self.assertLogs(level='INFO') as log:
      enable_stack_trace_dumping(stack_trace_config)
    self.assertEqual(faulthandler.is_enabled(), True)
    self.assertRegex(
        log.output[0], 'Stack trace will be written in: /tmp/debugging/'
    )

  def testDisableStackTraceDumpingFaulthandlerDisabled(self):
    stack_trace_config = stack_trace_configuration.StackTraceConfig(
        collect_stack_trace=True, stack_trace_to_cloud=True
    )
    enable_stack_trace_dumping(stack_trace_config)
    disable_stack_trace_dumping(stack_trace_config)
    self.assertEqual(faulthandler.is_enabled(), False)

  def testUserSignalHandlerForStderr(self):
    file_obj = tempfile.NamedTemporaryFile('r+')
    sys.stderr = file_obj
    user_signal_handler = user_signal_handler_wrapper(sys.stderr, 30)
    user_signal_handler(signal.SIGUSR1, None)
    with open(file_obj.name, 'rb') as f:
      data = f.readlines()
      self.assertEqual(
          data[0],
          b'INFO: Not a crash. cloud-tpu-diagnostics emits a stack trace'
          b' snapshot every 30 seconds.\n',
      )

  def testUserSignalHandlerForFile(self):
    file_obj = tempfile.NamedTemporaryFile('rb+')
    user_signal_handler = user_signal_handler_wrapper(file_obj, 30)
    user_signal_handler(signal.SIGUSR1, None)
    with open(file_obj.name, 'rb') as f:
      data = f.readlines()
      self.assertEqual(
          data[0],
          b'INFO: Not a crash. cloud-tpu-diagnostics emits a stack trace'
          b' snapshot every 30 seconds.\n',
      )

  def check_fatal_error(self, line_number, error, signal_name, log_to_cloud):
    if error:
      header = r'Stack \(most recent call first\)'
      regex = """
          {error}
          
          {header}:
            File "{filename}", line {line_number} in <module>
          """
    else:
      header = (
          r'INFO: Not a crash. cloud\-tpu\-diagnostics emits a stack trace'
          r' snapshot every 1 seconds.\n'
          r'Stack \(most recent call first\)'
      )
      regex = """
          {header}:
            File "{stack_trace_module}", line 23 in user_signal_handler
            File "{filename}", line {line_number} in <module>
          """
    regex = (
        textwrap.dedent(regex)
        .format(
            error=error,
            header=header,
            filename=self.test_file,
            stack_trace_module=self.stack_trace_module,
            line_number=line_number,
        )
        .strip()
    )

    output, stderr = self.get_output(signal_name, True, log_to_cloud)
    if log_to_cloud:
      self.assertRegex(output, regex)
      self.assertEmpty(stderr)
    else:
      self.assertRegex(stderr, regex)
      self.assertEmpty(output)

  def get_output(self, signal_name, collect_stack_trace, log_to_cloud):
    process = self.run_python_code(
        signal_name, collect_stack_trace, log_to_cloud
    )
    _, stderr = process.communicate()
    stderr = stderr.decode('ascii', 'backslashreplace')
    output = ''
    if log_to_cloud:
      trace_file = os.listdir(default.STACK_TRACE_DIR_DEFAULT)
      if trace_file:
        stack_trace_file = default.STACK_TRACE_DIR_DEFAULT + trace_file[0]
        with open(stack_trace_file, 'rb') as fp:
          output = fp.read().decode('ascii', 'backslashreplace')
    return output, stderr

  def run_python_code(self, signal_name, collect_stack_trace, log_to_cloud):
    args = [
        '--signal=' + signal_name,
        '--collect_stack_trace=' + str(collect_stack_trace),
        '--log_to_cloud=' + str(log_to_cloud),
    ]
    if sys.executable is not None:
      code = [sys.executable, self.test_file]
    else:
      code = [self.test_binary]
    return subprocess.Popen(
        code + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=os.environ.copy(),
    )


if __name__ == '__main__':
  absltest.main()
