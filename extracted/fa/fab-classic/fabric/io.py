import re
import sys
import socket
import time
from select import select
from collections import deque

from fabric.state import env, output, win32
from fabric.auth import get_password, set_password
import fabric.network
from fabric.network import ssh, normalize
from fabric.exceptions import CommandTimeout

if win32:
    import msvcrt


def _endswith(char_list, substring):
    if len(substring) > len(char_list):
        return False

    for i in range(len(substring)):
        if char_list[-1 - i] != substring[-1 - i]:
            return False

    return True


def _has_newline(bytelist):
    return '\r' in bytelist or '\n' in bytelist


def output_loop(*args, **kwargs):
    OutputLooper(*args, **kwargs).loop()


class OutputLooper(object):
    def __init__(self, chan, attr, stream, capture, timeout):
        self.chan = chan
        self.stream = stream
        self.capture = capture
        self.timeout = timeout
        self.read_func = getattr(chan, attr)
        self.prefix = "[%s] %s: " % (
            env.host_string,
            "out" if attr == 'recv' else "err"
        )
        self.printing = getattr(output, 'stdout' if (attr == 'recv') else 'stderr')
        self.linewise = (env.linewise or env.parallel)
        self.reprompt = False
        self.read_size = 4096
        self.write_buffer = deque(maxlen=len(self.prefix))

    def _flush(self, text):
        self.stream.write(text)
        # Actually only flush if not in linewise mode.
        # When linewise is set (e.g. in parallel mode) flushing makes
        # doubling-up of line prefixes, and other mixed output, more likely.
        if not env.linewise:
            self.stream.flush()
        self.write_buffer.extend(text)

    def loop(self):
        """
        Loop, reading from <chan>.<attr>(), writing to <stream> and buffering to <capture>.

        Will raise `~fabric.exceptions.CommandTimeout` if network timeouts
        continue to be seen past the defined ``self.timeout`` threshold.
        (Timeouts before then are considered part of normal short-timeout fast
        network reading; see Fabric issue #733 for background.)
        """
        # Initialize loop variables
        initial_prefix_printed = False
        seen_cr = False
        line = []
        py3_buffer = b''

        # Allow prefix to be turned off.
        if not env.output_prefix:
            self.prefix = ""

        start = time.time()
        while True:
            # Handle actual read
            try:
                bytelist = self.read_func(self.read_size)
            except socket.timeout:
                elapsed = time.time() - start
                if self.timeout is not None and elapsed > self.timeout:
                    raise CommandTimeout(timeout=self.timeout)
                continue

            if isinstance(bytelist, bytes):
                # Note that we have to decode this right away, even if an error
                # is thrown only later in the code, because e.g. '' != b'' (see
                # first if below).
                py3_buffer += bytelist
                try:
                    bytelist = py3_buffer.decode('utf-8')
                except UnicodeDecodeError:
                    # Go back and grab more bytes so we hopefully get a
                    # complete and valid Python string.
                    # Might hang here if remote server sends garbage but unsure
                    # if it's worth switching to processing byte by byte ...
                    continue
                else:
                    # Reset the buffer as we succeeded
                    py3_buffer = b''

            # Empty byte == EOS
            if bytelist == '':
                # If linewise, ensure we flush any leftovers in the buffer.
                if self.linewise and line:
                    self._flush(self.prefix)
                    self._flush("".join(line))
                break

            # A None capture variable implies that we're in open_shell()
            if self.capture is None:
                # Just print directly -- no prefixes, no capturing, nada
                # And since we know we're using a pty in this mode, just go
                # straight to stdout.
                self._flush(bytelist)
            # Otherwise, we're in run/sudo and need to handle capturing and
            # prompts.
            else:
                # Print to user
                if self.printing:
                    printable_bytes = bytelist
                    # Small state machine to eat \n after \r
                    if printable_bytes[-1] == "\r":
                        seen_cr = True
                    if printable_bytes[0] == "\n" and seen_cr:
                        printable_bytes = printable_bytes[1:]
                        seen_cr = False

                    while _has_newline(printable_bytes) and printable_bytes != "":
                        # at most 1 split !
                        cr = re.search("(\r\n|\r|\n)", printable_bytes)
                        if cr is None:
                            break
                        end_of_line = printable_bytes[:cr.start(0)]
                        printable_bytes = printable_bytes[cr.end(0):]

                        if not initial_prefix_printed:
                            self._flush(self.prefix)

                        if _has_newline(end_of_line):
                            end_of_line = ''

                        if self.linewise:
                            self._flush("".join(line) + end_of_line + "\n")
                            line = []
                        else:
                            self._flush(end_of_line + "\n")
                        initial_prefix_printed = False

                    if self.linewise:
                        line += [printable_bytes]
                    else:
                        if not initial_prefix_printed:
                            self._flush(self.prefix)
                            initial_prefix_printed = True
                        self._flush(printable_bytes)

                # Now we have handled printing, handle interactivity
                read_lines = re.split(r"(\r|\n|\r\n)", bytelist)
                for fragment in read_lines:
                    # Store in capture buffer
                    self.capture += fragment
                    # Handle prompts
                    expected, response = self._get_prompt_response()
                    if expected:
                        del list(self.capture)[-1 * len(expected):]
                        self.chan.sendall(str(response) + '\n')
                    else:
                        prompt = _endswith(self.capture, env.sudo_prompt)
                        try_again = (_endswith(self.capture, env.again_prompt + '\n')
                            or _endswith(self.capture, env.again_prompt + '\r\n'))
                        if prompt:
                            self.prompt()
                        elif try_again:
                            self.try_again()

        # Print trailing new line if the last thing we printed was our line
        # prefix.
        if self.prefix and "".join(self.write_buffer) == self.prefix:
            self._flush('\n')

    def prompt(self):
        # Obtain cached password, if any
        password = get_password(*normalize(env.host_string))
        # Remove the prompt itself from the capture buffer. This is
        # backwards compatible with Fabric 0.9.x behavior; the user
        # will still see the prompt on their screen (no way to avoid
        # this) but at least it won't clutter up the captured text.

        # NOTE: Yes, the original RingBuffer from Fabric can do this more elegantly.
        #       This removes the last N elements from the list.
        _pop_count = min(len(self.capture), len(env.sudo_prompt))
        for i in range(0, _pop_count):
            self.capture.pop()

        # If the password we just tried was bad, prompt the user again.
        if (not password) or self.reprompt:
            # Print the prompt and/or the "try again" notice if
            # output is being hidden. In other words, since we need
            # the user's input, they need to see why we're
            # prompting them.
            if not self.printing:
                self._flush(self.prefix)
                if self.reprompt:
                    self._flush(env.again_prompt + '\n' + self.prefix)
                self._flush(env.sudo_prompt)
            # Prompt for, and store, password. Give empty prompt so the
            # initial display "hides" just after the actually-displayed
            # prompt from the remote end.
            self.chan.input_enabled = False
            password = fabric.network.prompt_for_password(
                prompt=" ", no_colon=True, stream=self.stream
            )
            self.chan.input_enabled = True
            # Update env.password, env.passwords if necessary
            user, host, port = normalize(env.host_string)
            # TODO: in 2.x, make sure to only update sudo-specific password
            # config values, not login ones.
            set_password(user, host, port, password)
            # Reset reprompt flag
            self.reprompt = False
        # Send current password down the pipe
        self.chan.sendall(password + '\n')

    def try_again(self):
        # Remove text from capture buffer
        self.capture = list(self.capture)[:len(env.again_prompt)]
        # Set state so we re-prompt the user at the next prompt.
        self.reprompt = True

    def _get_prompt_response(self):
        """
        Iterate through the request prompts dict and return the response and
        original request if we find a match
        """
        for tup in env.prompts.items():
            if _endswith(self.capture, tup[0]):
                return tup
        return None, None


def input_loop(chan, f, using_pty):
    is_stdin = f == sys.stdin
    waitable = True
    if win32:
        waitable = False
    else:
        try:
            f.fileno()
        except ValueError:
            waitable = False

    while not chan.exit_status_ready():
        byte = None
        if not chan.input_enabled:
            pass
        elif win32 and is_stdin:
            if msvcrt.kbhit():
                byte = msvcrt.getch()
        elif waitable:
            r, w, x = select([f], [], [], 0.0)
            if f in r:
                byte = f.read(1)
        else:
            byte = f.read(1)

        if byte:
            chan.sendall(byte)
            # Optionally echo locally, if needed.
            if (not using_pty) and is_stdin and env.echo_stdin:
                # Not using fastprint() here -- it prints as 'user'
                # output level, don't want it to be accidentally hidden
                sys.stdout.write(byte)
                sys.stdout.flush()

        elif byte == '':  # EOF
            chan.shutdown_write()
            break
        else:
            time.sleep(ssh.io_sleep)
