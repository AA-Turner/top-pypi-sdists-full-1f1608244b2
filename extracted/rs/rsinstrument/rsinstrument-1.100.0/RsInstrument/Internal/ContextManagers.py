"""Context managers for common SCPI tasks."""

from .Instrument import Instrument
from .InstrumentErrors import assert_no_instrument_status_errors, TimeoutException, StatusException
from typing import List, Tuple
from pyvisa import VisaIOError


class InstrErrorSuppressor:
	"""Context-manager class to suppress exception coming from the instrument's status system.
	Other exceptions types are still raised.
	On entering the context, this class clears all the instrument status errors.
	:param io: RsInstrument session instance.
	:param visa_tout_ms: VISA Timeout in milliseconds, that is set for this context.
		Afterward, it is changed back. Default value: do-not-change.
	:param suppress_only_codes: You can enter a code or list of codes for errors to be suppressed.
		Other errors will be reported. Example: If you enter -113 here, only the 'Undefined Header' error will be suppressed.
		Default value: suppress-all-errors."""

	def __init__(self, io: Instrument, visa_tout_ms: int = 0, suppress_only_codes: int or List[int] = None):
		self._io: Instrument = io
		self._old_query_instr_status: bool = False
		self._old_visa_tout_ms: int = 0
		self._errors: List = []
		self._suppress_only_codes = suppress_only_codes
		self._exited: bool = False

		if visa_tout_ms > 0:
			self._old_visa_tout_ms = io.visa_timeout
			io.visa_timeout = visa_tout_ms

	def __enter__(self) -> 'InstrErrorSuppressor':
		"""Stuff to do when entering the context.
		Remember the old instrument status checking setting."""
		self._old_query_instr_status = self._io.query_instr_status
		self._io.query_instr_status = False
		self._io.clear_status()
		return self

	def __exit__(self, exc_type, value, traceback):
		"""Stuff to do when leaving the context.
				- Reads all the errors from the error queue.
				- Sets the Instrument Status Checking flag to the original value.
				- Sets the VISA Timeout to the original value.
			:returns: True, if the exception in the block should be suppressed."""
		self._io.query_instr_status = self._old_query_instr_status

		if self._old_visa_tout_ms > 0:
			self._io.visa_timeout = self._old_visa_tout_ms

		self.get_errors_occurred()
		self._exited = True

		# Even if the instrument status was switched OFF,
		#  the StatusException can happen when you query an invalid command.
		if isinstance(value, StatusException):
			suppressed = self._add_or_suppress_new_errors(value.errors_list)
			if suppressed:
				self._errors.extend(suppressed)
				return True  # Suppress this exception

		return False

	def get_errors_occurred(self) -> bool:
		"""Inside the context: Returns True, if any new errors occurred since the last call of this method.
		Outside the context: Returns True, if the accumulated error list contains errors."""
		if self._exited:
			return len(self._errors) > 0

		new_errors = self._io.query_all_syst_errors()
		suppressed = self._add_or_suppress_new_errors(new_errors)

		if suppressed:
			self._errors.extend(suppressed)
			return True

		return False

	def get_all_errors(self, incl_codes: bool = False) -> List[str] or List[Tuple[int, str]] or None:
		"""Returns all the errors accumulated during the call of this context.
		If no errors occurred, the method returns 'None'."""
		self.get_errors_occurred()
		if len(self._errors) == 0:
			return None
		if incl_codes:
			return self._errors
		return [x[1] for x in self._errors]

	def _add_or_suppress_new_errors(self, errors: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
		"""Internal method, that takes the entered list of errors and checks whether they should be suppressed.
		Suppressed errors are added to the self._errors, and not suppresses are raised as StatusException."""
		if not errors:
			return errors

		if not self._suppress_only_codes:
			return errors

		# For cases where the _suppress_only_codes contain single value or list of values,
		# we have to suppress selectively.
		report: List[Tuple[int, str]] = []
		suppressed: List[Tuple[int, str]] = []
		for err in errors:
			suppress = False
			if isinstance(self._suppress_only_codes, int):
				suppress = err[0] == self._suppress_only_codes
			elif isinstance(self._suppress_only_codes, list):
				suppress = err[0] in self._suppress_only_codes
			if suppress:
				suppressed.append(err)
			else:
				# The error code should not be suppressed, add it to the list
				report.append(err)

		assert_no_instrument_status_errors(self._io.resource_name, report, "InstrErrorSuppressor context -")
		return suppressed


class VisaTimeoutSuppressor:
	"""Context-manager class to suppress exception caused by the VISA Timeout.
	Careful!!!: The VisaTimeoutSuppressor only suppresses the very first VISA Timeout exception,
	and afterward it ends. Therefore, use only one command per context manager,
	if you do not want to skip the following ones.
	:param io: RsInstrument session instance.
	:param visa_tout_ms: VISA Timeout in milliseconds, that is set for this context.
	"""
	def __init__(self, io: Instrument, visa_tout_ms: int = 0):
		self._io: Instrument = io
		self._old_visa_tout_ms: int = 0

		self._timeout_occurred: bool = False

		if visa_tout_ms > 0:
			self._old_visa_tout_ms = io.visa_timeout
			io.visa_timeout = visa_tout_ms

	def __enter__(self) -> 'VisaTimeoutSuppressor':
		"""Stuff to do when entering the context.
		Currently, do not do anything."""
		return self

	def __exit__(self, exc_type, value, traceback):
		"""Stuff to do when leaving the context:
				- Sets the VISA Timeout to the original value.
				- Sets the query_instr_status to the original value.
			:returns: True, if the exception in the block should be suppressed."""
		if self._old_visa_tout_ms > 0:
			self._io.visa_timeout = self._old_visa_tout_ms

		# Was it straight timeout exception?
		if isinstance(value, TimeoutException):
			self._timeout_occurred = True
			if self._io.query_instr_status is False:
				# If the instrument status checking is OFF, clear the error queue
				try:
					self._instrument_errors = self._io.query_all_syst_errors(False)
				except VisaIOError:
					pass

			return True

		# Instrument status exception, but caused primarily by timeout exception
		if isinstance(value, StatusException):
			if value.first_exc is not None and value.first_exc is TimeoutException:
				self._timeout_occurred = True
				if self._io.query_instr_status is False:
					# If the instrument status checking is OFF, clear the error queue
					try:
						self._instrument_errors = self._io.query_all_syst_errors(False)
					except VisaIOError:
						pass

				return True

		if isinstance(value, VisaIOError) and hasattr(value, 'source'):
			# check for the source _narrow_down_tout_error
			if value.source == '_narrow_down_io_tout_error':
				self._timeout_occurred = True
				return True

		return False

	def get_timeout_occurred(self) -> bool:
		"""Returns True, if the VISA timeout occurred in the context."""
		return self._timeout_occurred
