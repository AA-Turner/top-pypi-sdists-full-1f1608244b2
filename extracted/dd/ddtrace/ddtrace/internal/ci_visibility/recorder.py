from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Union
from urllib import parse

import ddtrace
from ddtrace import config as ddconfig
from ddtrace.contrib import trace_utils
from ddtrace.ext import ci
from ddtrace.ext import test
from ddtrace.ext.test_visibility import ITR_SKIPPING_LEVEL
from ddtrace.ext.test_visibility._test_visibility_base import TestSessionId
from ddtrace.ext.test_visibility._test_visibility_base import TestVisibilityItemId
from ddtrace.ext.test_visibility.api import Test
from ddtrace.ext.test_visibility.api import TestBase
from ddtrace.ext.test_visibility.api import TestId
from ddtrace.ext.test_visibility.api import TestModule
from ddtrace.ext.test_visibility.api import TestModuleId
from ddtrace.ext.test_visibility.api import TestSession
from ddtrace.ext.test_visibility.api import TestStatus
from ddtrace.ext.test_visibility.api import TestSuite
from ddtrace.ext.test_visibility.api import TestSuiteId
from ddtrace.internal import agent
from ddtrace.internal import atexit
from ddtrace.internal import core
from ddtrace.internal import telemetry
from ddtrace.internal.ci_visibility._api_client import AgentlessTestVisibilityAPIClient
from ddtrace.internal.ci_visibility._api_client import EarlyFlakeDetectionSettings
from ddtrace.internal.ci_visibility._api_client import EVPProxyTestVisibilityAPIClient
from ddtrace.internal.ci_visibility._api_client import ITRData
from ddtrace.internal.ci_visibility._api_client import TestManagementSettings
from ddtrace.internal.ci_visibility._api_client import TestProperties
from ddtrace.internal.ci_visibility._api_client import TestVisibilityAPISettings
from ddtrace.internal.ci_visibility._api_client import _TestVisibilityAPIClientBase
from ddtrace.internal.ci_visibility.api._module import TestVisibilityModule
from ddtrace.internal.ci_visibility.api._session import TestVisibilitySession
from ddtrace.internal.ci_visibility.api._session import TestVisibilitySessionSettings
from ddtrace.internal.ci_visibility.api._suite import TestVisibilitySuite
from ddtrace.internal.ci_visibility.api._test import TestVisibilityTest
from ddtrace.internal.ci_visibility.constants import AGENTLESS_DEFAULT_SITE
from ddtrace.internal.ci_visibility.constants import CUSTOM_CONFIGURATIONS_PREFIX
from ddtrace.internal.ci_visibility.constants import EVP_PROXY_AGENT_BASE_PATH
from ddtrace.internal.ci_visibility.constants import EVP_PROXY_AGENT_BASE_PATH_V4
from ddtrace.internal.ci_visibility.constants import EVP_SUBDOMAIN_HEADER_EVENT_VALUE
from ddtrace.internal.ci_visibility.constants import EVP_SUBDOMAIN_HEADER_NAME
from ddtrace.internal.ci_visibility.constants import ITR_CORRELATION_ID_TAG_NAME
from ddtrace.internal.ci_visibility.constants import REQUESTS_MODE
from ddtrace.internal.ci_visibility.constants import SUITE
from ddtrace.internal.ci_visibility.constants import TEST
from ddtrace.internal.ci_visibility.constants import TRACER_PARTIAL_FLUSH_MIN_SPANS
from ddtrace.internal.ci_visibility.constants import UNSUPPORTED_PROVIDER
from ddtrace.internal.ci_visibility.context import CIContextProvider
from ddtrace.internal.ci_visibility.coverage import is_coverage_available
from ddtrace.internal.ci_visibility.errors import CIVisibilityAuthenticationException
from ddtrace.internal.ci_visibility.errors import CIVisibilityError
from ddtrace.internal.ci_visibility.filters import TraceCiVisibilityFilter
from ddtrace.internal.ci_visibility.git_client import METADATA_UPLOAD_STATUS
from ddtrace.internal.ci_visibility.git_client import CIVisibilityGitClient
from ddtrace.internal.ci_visibility.git_data import GitData
from ddtrace.internal.ci_visibility.git_data import get_git_data_from_tags
from ddtrace.internal.ci_visibility.utils import _get_test_framework_telemetry_name
from ddtrace.internal.ci_visibility.writer import CIVisibilityEventClient
from ddtrace.internal.ci_visibility.writer import CIVisibilityWriter
from ddtrace.internal.codeowners import Codeowners
from ddtrace.internal.logger import get_logger
from ddtrace.internal.service import Service
from ddtrace.internal.test_visibility._atr_mixins import ATRTestMixin
from ddtrace.internal.test_visibility._atr_mixins import AutoTestRetriesSettings
from ddtrace.internal.test_visibility._attempt_to_fix_mixins import AttemptToFixTestMixin
from ddtrace.internal.test_visibility._benchmark_mixin import BenchmarkTestMixin
from ddtrace.internal.test_visibility._efd_mixins import EFDTestMixin
from ddtrace.internal.test_visibility._efd_mixins import EFDTestStatus
from ddtrace.internal.test_visibility._internal_item_ids import InternalTestId
from ddtrace.internal.test_visibility._itr_mixins import ITRMixin
from ddtrace.internal.test_visibility._library_capabilities import LibraryCapabilities
from ddtrace.internal.test_visibility.api import InternalTest
from ddtrace.internal.test_visibility.coverage_lines import CoverageLines
from ddtrace.internal.utils.formats import asbool
from ddtrace.settings import IntegrationConfig
from ddtrace.settings._agent import config as agent_config
from ddtrace.trace import Span
from ddtrace.trace import Tracer


log = get_logger(__name__)

DEFAULT_TIMEOUT = 15
DEFAULT_ITR_SKIPPABLE_TIMEOUT = 20
UNSUPPORTED = "unsupported"
TELEMETRY_BY_PROVIDER_NAME = {
    "appveyor": "provider:appveyor",
    "azurepipelines": "provider:azp",
    "bitbucket": "provider:bitbucket",
    "buildkite": "provider:buildkite",
    "circleci": "provider:circleci",
    "codefresh": "provider:codefresh",
    "github": "provider:githubactions",
    "gitlab": "provider:gitlab",
    "jenkins": "provider:jenkins",
    "teamcity": "provider:teamcity",
    "travisci": "provider:travisci",
    "bitrise": "provider:bitrise",
    "buddy": "provider:buddyci",
    "awscodepipeline": "provider:aws",
    UNSUPPORTED: UNSUPPORTED_PROVIDER,
}


def _extract_repository_name_from_url(repository_url: str) -> str:
    _REPO_NAME_REGEX = r".*/(?P<repo_name>.*?)(\.git)?$"

    try:
        url_path = parse.urlparse(repository_url).path
        matches = re.match(_REPO_NAME_REGEX, url_path, flags=re.IGNORECASE)
        if matches:
            return matches.group("repo_name")
        log.warning("Cannot extract repository name from unexpected URL path: %s", url_path)
        return repository_url
    except ValueError:
        log.warning("Repository name cannot be parsed from repository_url: %s", repository_url)
        return repository_url


def _get_git_repo() -> Optional[str]:
    # this exists only for the purpose of patching in tests
    return None


def _get_custom_configurations() -> Dict[str, str]:
    custom_configurations = {}
    for tag, value in ddconfig.tags.items():
        if tag.startswith(CUSTOM_CONFIGURATIONS_PREFIX):
            custom_configurations[tag.replace("%s." % CUSTOM_CONFIGURATIONS_PREFIX, "", 1)] = value

    return custom_configurations


class CIVisibilityTracer(Tracer):
    def __init__(self, *args, **kwargs) -> None:
        # Allows for multiple instances of the civis tracer to be created without logging a warning
        super().__init__(*args, **kwargs)


class CIVisibility(Service):
    _instance: Optional["CIVisibility"] = None
    enabled = False

    def __init__(
        self, tracer: Optional[Tracer] = None, config: Optional[IntegrationConfig] = None, service: Optional[str] = None
    ) -> None:
        super().__init__()

        if tracer:
            self.tracer = tracer
        else:
            if asbool(os.getenv("_DD_CIVISIBILITY_USE_CI_CONTEXT_PROVIDER")):
                log.debug("Using DD CI context provider: test traces may be incomplete, telemetry may be inaccurate")
                # Create a new CI tracer, using a specific URL if provided (only useful when testing the tracer itself)
                self.tracer = CIVisibilityTracer()

                env_agent_url = os.getenv("_CI_DD_AGENT_URL")
                if env_agent_url is not None:
                    log.debug("Using _CI_DD_AGENT_URL for CI Visibility tracer: %s", env_agent_url)
                    self.tracer._span_aggregator.writer.intake_url = env_agent_url  # type: ignore[attr-defined]
                self.tracer.context_provider = CIContextProvider()
            else:
                self.tracer = ddtrace.tracer

            # Partial traces are required for ITR to work in suite-level skipping for long test sessions, but we
            # assume that a tracer is already configured if it's been passed in.
            self.tracer._span_aggregator.partial_flush_enabled = True
            self.tracer._span_aggregator.partial_flush_min_spans = TRACER_PARTIAL_FLUSH_MIN_SPANS
            self.tracer._recreate()

        self._api_client: Optional[_TestVisibilityAPIClientBase] = None

        self._configurations = ci._get_runtime_and_os_metadata()
        custom_configurations = _get_custom_configurations()
        if custom_configurations:
            self._configurations["custom"] = custom_configurations

        self._api_key = os.getenv("_CI_DD_API_KEY", os.getenv("DD_API_KEY"))

        self._dd_site = os.getenv("DD_SITE", AGENTLESS_DEFAULT_SITE)
        self.config = config or ddconfig.test_visibility  # type: Optional[IntegrationConfig]
        self._itr_skipping_level: ITR_SKIPPING_LEVEL = ddconfig.test_visibility.itr_skipping_level
        self._itr_skipping_ignore_parameters: bool = ddconfig.test_visibility._itr_skipping_ignore_parameters
        if not isinstance(ddconfig.test_visibility.itr_skipping_level, ITR_SKIPPING_LEVEL):
            log.warning(
                "itr_skipping_level should be of type %s but is of type %s, defaulting to %s",
                ITR_SKIPPING_LEVEL,
                type(ddconfig.test_visibility.itr_skipping_level),
                ITR_SKIPPING_LEVEL.TEST.name,
            )
            self._itr_skipping_level = ITR_SKIPPING_LEVEL.TEST
        self._suite_skipping_mode = ddconfig.test_visibility.itr_skipping_level == ITR_SKIPPING_LEVEL.SUITE
        self._tags: Dict[str, str] = ci.tags(cwd=_get_git_repo())
        self._is_auto_injected = bool(os.getenv("DD_CIVISIBILITY_AUTO_INSTRUMENTATION_PROVIDER", ""))
        self._service = service
        self._codeowners = None
        self._root_dir = None
        self._should_upload_git_metadata = True
        self._itr_meta: Dict[str, Any] = {}
        self._itr_data: Optional[ITRData] = None
        self._known_test_ids: Set[InternalTestId] = set()
        self._test_properties: Dict[InternalTestId, TestProperties] = {}

        self._session: Optional[TestVisibilitySession] = None

        if service is None:
            # Use service if provided to enable() or __init__()
            int_service = None
            if self.config is not None:
                int_service = trace_utils.int_service(None, self.config)
            # check if repository URL detected from environment or .git, and service name unchanged
            if (
                self._tags.get(ci.git.REPOSITORY_URL, None)
                and self.config
                and int_service == self.config._default_service
            ):
                self._service = _extract_repository_name_from_url(self._tags[ci.git.REPOSITORY_URL])
            elif self._service is None and int_service is not None:
                self._service = int_service

        self._git_data: GitData = get_git_data_from_tags(self._tags)

        self._dd_env = os.getenv("_CI_DD_ENV", ddconfig.env)
        dd_env_msg = ""

        if ddconfig._ci_visibility_agentless_enabled:
            # In agentless mode, normalize an unset env to none (this is already done by the backend in most cases, so
            # it does not override default behavior)
            if self._dd_env is None:
                self._dd_env = "none"
                dd_env_msg = " (not set in environment)"
            if not self._api_key:
                raise EnvironmentError(
                    "DD_CIVISIBILITY_AGENTLESS_ENABLED is set, but DD_API_KEY is not set, so ddtrace "
                    "cannot be initialized."
                )
            requests_mode_str = "agentless"
            self._requests_mode = REQUESTS_MODE.AGENTLESS_EVENTS
            self._api_client = AgentlessTestVisibilityAPIClient(
                self._itr_skipping_level,
                self._git_data,
                self._configurations,
                self._api_key,
                self._dd_site,
                ddconfig._ci_visibility_agentless_url if ddconfig._ci_visibility_agentless_url else None,
                self._service,
                self._dd_env,
            )
        elif evp_proxy_base_url := self._agent_evp_proxy_base_url():
            # In EVP-proxy cases, if an env is not provided, we need to get the agent's default env in order to make
            # the correct decision:
            if self._dd_env is None:
                self._dd_env = self._agent_get_default_env()
                dd_env_msg = " (default environment provided by agent)"
            self._requests_mode = REQUESTS_MODE.EVP_PROXY_EVENTS
            requests_mode_str = "EVP Proxy"
            self._api_client = EVPProxyTestVisibilityAPIClient(
                self._itr_skipping_level,
                self._git_data,
                self._configurations,
                self.tracer._agent_url,
                self._service,
                self._dd_env,
                evp_proxy_base_url=evp_proxy_base_url,
            )
        else:
            requests_mode_str = "APM (some features will be disabled)"
            self._requests_mode = REQUESTS_MODE.TRACES
            self._should_upload_git_metadata = False

        if self._should_upload_git_metadata:
            self._git_client = CIVisibilityGitClient(
                api_key=self._api_key or "", requests_mode=self._requests_mode, tracer=self.tracer
            )
            self._git_client.upload_git_metadata(cwd=_get_git_repo())

        self._api_settings = self._check_enabled_features()

        self._collect_coverage_enabled = self._should_collect_coverage(self._api_settings.coverage_enabled)

        self._configure_writer(coverage_enabled=self._collect_coverage_enabled, url=self.tracer._agent_url)

        log.info("Service: %s (env: %s%s)", self._service, self._dd_env, dd_env_msg)
        log.info("Requests mode: %s", requests_mode_str)
        log.info("Git metadata upload enabled: %s", self._should_upload_git_metadata)
        log.info("API-provided settings: coverage collection: %s", self._api_settings.coverage_enabled)
        log.info(
            "API-provided settings: Intelligent Test Runner: %s, test skipping: %s",
            self._api_settings.itr_enabled,
            self._api_settings.skipping_enabled,
        )
        log.info(
            "API-provided settings: Early Flake Detection enabled: %s",
            self._api_settings.early_flake_detection.enabled,
        )
        log.info(
            "API-provided settings: Known Tests enabled: %s",
            self._api_settings.known_tests_enabled,
        )
        log.info("API-provided settings: Auto Test Retries enabled: %s", self._api_settings.flaky_test_retries_enabled)
        log.info("Detected configurations: %s", str(self._configurations))

        try:
            self._codeowners = Codeowners(cwd=self._tags.get(ci.WORKSPACE_PATH))
        except ValueError:
            log.warning("CODEOWNERS file is not available")
        except Exception:
            log.warning("Failed to load CODEOWNERS", exc_info=True)

    @staticmethod
    def _should_collect_coverage(coverage_enabled_by_api):
        if not coverage_enabled_by_api and not asbool(
            os.getenv("_DD_CIVISIBILITY_ITR_FORCE_ENABLE_COVERAGE", default=False)
        ):
            return False
        if not is_coverage_available():
            log.warning(
                "CI Visibility code coverage tracking is enabled, but the `coverage` package is not installed."
                "To use code coverage tracking, please install `coverage` from https://pypi.org/project/coverage/"
            )
            return False
        return True

    def _check_enabled_features(self) -> TestVisibilityAPISettings:
        _error_return_value = TestVisibilityAPISettings()

        if not self._api_client:
            log.warning("API client not initialized, disabling coverage collection and test skipping")
            return _error_return_value

        try:
            settings = self._api_client.fetch_settings()
        except CIVisibilityAuthenticationException:
            # Authentication exception is handled during enable() to prevent the service from being used
            raise
        except Exception:
            log.warning(
                "Error checking Intelligent Test Runner API, disabling coverage collection and test skipping",
                exc_info=True,
            )
            return _error_return_value

        if settings.require_git:
            log.info("Settings API requires git metadata, waiting for git metadata upload to complete")
            try:
                try:
                    if self._git_client.wait_for_metadata_upload_status() == METADATA_UPLOAD_STATUS.FAILED:
                        log.warning("Metadata upload failed, test skipping will be best effort")
                except ValueError:
                    log.warning(
                        "Error waiting for git metadata upload, test skipping will be best effort", exc_info=True
                    )
            except TimeoutError:
                log.warning("Timeout waiting for metadata upload, test skipping will be best effort")

            # The most recent API response overrides the first one
            try:
                settings = self._api_client.fetch_settings()
            except Exception:
                log.warning(
                    "Error checking Intelligent Test Runner API after git metadata upload,"
                    " disabling coverage and test skipping",
                    exc_info=True,
                )
                return _error_return_value
            if settings.require_git:
                log.warning("git metadata upload did not complete in time, test skipping will be best effort")

        return settings

    def _configure_writer(
        self, coverage_enabled: bool = False, requests_mode: Optional[REQUESTS_MODE] = None, url: Optional[str] = None
    ) -> None:
        writer = None
        if requests_mode is None:
            requests_mode = self._requests_mode

        if requests_mode == REQUESTS_MODE.AGENTLESS_EVENTS:
            headers = {"dd-api-key": self._api_key or ""}
            writer = CIVisibilityWriter(
                headers=headers,
                coverage_enabled=coverage_enabled,
                itr_suite_skipping_mode=self._suite_skipping_mode,
                use_gzip=True,
            )
        elif requests_mode == REQUESTS_MODE.EVP_PROXY_EVENTS:
            writer = CIVisibilityWriter(
                intake_url=agent_config.trace_agent_url if url is None else url,
                headers={EVP_SUBDOMAIN_HEADER_NAME: EVP_SUBDOMAIN_HEADER_EVENT_VALUE},
                use_evp=True,
                coverage_enabled=coverage_enabled,
                itr_suite_skipping_mode=self._suite_skipping_mode,
                use_gzip=self._is_gzip_supported_by_agent(),
            )
        if writer is not None:
            self.tracer._span_aggregator.writer = writer
            self.tracer._recreate()

    def _agent_evp_proxy_base_url(self) -> Optional[str]:
        try:
            info = agent.info(self.tracer._agent_url)
        except Exception:
            return None

        if info:
            endpoints = info.get("endpoints", [])
            if endpoints and any(EVP_PROXY_AGENT_BASE_PATH_V4 in endpoint for endpoint in endpoints):
                return EVP_PROXY_AGENT_BASE_PATH_V4
            if endpoints and any(EVP_PROXY_AGENT_BASE_PATH in endpoint for endpoint in endpoints):
                return EVP_PROXY_AGENT_BASE_PATH
        return None

    def _is_gzip_supported_by_agent(self) -> bool:
        return self._agent_evp_proxy_base_url() == EVP_PROXY_AGENT_BASE_PATH_V4

    def _agent_get_default_env(self) -> Optional[str]:
        try:
            info = agent.info(self.tracer._agent_url)
        except Exception:
            return "none"

        if info:
            return info.get("config", {}).get("default_env", "none")
        return "none"

    @classmethod
    def is_itr_enabled(cls) -> bool:
        # cls.enabled guarantees _instance is not None
        if not cls.enabled or cls._instance is None:
            return False

        if not ddconfig._ci_visibility_intelligent_testrunner_enabled:
            log.debug("Intelligent Test Runner is disabled by environment variable")
            return False

        return cls._instance._api_settings.itr_enabled

    @classmethod
    def test_skipping_enabled(cls) -> bool:
        if (
            not cls.enabled
            or cls._instance is None
            or asbool(os.getenv("_DD_CIVISIBILITY_ITR_PREVENT_TEST_SKIPPING", default=False))
        ):
            return False
        return cls._instance._api_settings.skipping_enabled

    @classmethod
    def is_known_tests_enabled(cls) -> bool:
        if cls._instance is None:
            return False
        return cls._instance._api_settings.known_tests_enabled

    @classmethod
    def is_efd_enabled(cls) -> bool:
        if cls._instance is None:
            return False
        return (
            cls._instance._api_settings.known_tests_enabled  # Known Tests Enabled takes precedence over EFD
            and cls._instance._api_settings.early_flake_detection.enabled
            and ddconfig._test_visibility_early_flake_detection_enabled
        )

    @classmethod
    def is_atr_enabled(cls) -> bool:
        if cls._instance is None:
            return False
        return cls._instance._api_settings.flaky_test_retries_enabled and asbool(
            os.getenv("DD_CIVISIBILITY_FLAKY_RETRY_ENABLED", default=True)
        )

    @classmethod
    def is_test_management_enabled(cls) -> bool:
        if cls._instance is None:
            return False
        return cls._instance._api_settings.test_management.enabled and asbool(
            os.getenv("DD_TEST_MANAGEMENT_ENABLED", default=True)
        )

    @classmethod
    def should_collect_coverage(cls) -> bool:
        if cls._instance is None:
            return False
        return cls._instance._api_settings.coverage_enabled or asbool(
            os.getenv("_DD_CIVISIBILITY_ITR_FORCE_ENABLE_COVERAGE", default=False)
        )

    def _fetch_tests_to_skip(self) -> None:
        # Make sure git uploading has finished
        # this will block the thread until that happens
        try:
            try:
                metadata_upload_status = self._git_client.wait_for_metadata_upload_status()
                if metadata_upload_status not in [METADATA_UPLOAD_STATUS.SUCCESS, METADATA_UPLOAD_STATUS.UNNECESSARY]:
                    log.warning("git metadata upload was not successful, some tests may not be skipped")
            except ValueError:
                log.warning(
                    "Error waiting for metadata upload to complete while fetching tests to skip"
                    ", some tests may not be skipped",
                    exc_info=True,
                )
        except TimeoutError:
            log.debug("Timed out waiting for git metadata upload, some tests may not be skipped")

        try:
            if self._api_client is None:
                return
            self._itr_data = self._api_client.fetch_skippable_items(
                ignore_test_parameters=self._itr_skipping_ignore_parameters
            )
            if self._itr_data is not None and self._itr_data.correlation_id is not None:
                self._itr_meta[ITR_CORRELATION_ID_TAG_NAME] = self._itr_data.correlation_id
        except Exception:  # noqa: E722
            log.debug("Error fetching skippable items", exc_info=True)

    def _fetch_known_tests(self) -> Optional[Set[InternalTestId]]:
        try:
            if self._api_client is not None:
                return self._api_client.fetch_known_tests()
            log.warning("API client not initialized, cannot fetch unique tests")
        except Exception:
            log.debug("Error fetching unique tests", exc_info=True)
        return None

    def _fetch_test_management_tests(self) -> Optional[Dict[InternalTestId, TestProperties]]:
        try:
            if self._api_client is not None:
                return self._api_client.fetch_test_management_tests()
            log.warning("API client not initialized, cannot fetch tests from Test Management")
        except Exception:
            log.debug("Error fetching unique tests", exc_info=True)
        return None

    def _should_skip_path(self, path: str, name: str, test_skipping_mode: Optional[str] = None) -> bool:
        """This method supports legacy usage of the CIVisibility service and should be removed

        The conversion of path to InternalTestId or SuiteId is redundant and absent from the new way of getting item
        skipping status. This method has been updated to look for item_ids in a way that matches the previous behavior,
        including questionable use of os.path.relpath.

        Note that in this legacy mode, test parameters are ignored.
        """
        if self._itr_data is None:
            return False
        if test_skipping_mode is None:
            _test_skipping_mode = SUITE if self._suite_skipping_mode else TEST
        else:
            _test_skipping_mode = test_skipping_mode

        module_path, _, suite_name = os.path.relpath(path).rpartition("/")
        module_name = module_path.replace("/", ".")
        suite_id = TestSuiteId(TestModuleId(module_name), suite_name)

        item_id = suite_id if _test_skipping_mode == SUITE else InternalTestId(suite_id, name)

        return item_id in self._itr_data.skippable_items

    @classmethod
    def enable(cls, tracer=None, config=None, service=None) -> None:
        log.debug("Enabling %s", cls.__name__)
        if ddconfig._ci_visibility_agentless_enabled:
            if not os.getenv("_CI_DD_API_KEY", os.getenv("DD_API_KEY")):
                log.critical(
                    "%s disabled: environment variable DD_CIVISIBILITY_AGENTLESS_ENABLED is true but"
                    " DD_API_KEY is not set",
                    cls.__name__,
                )
                cls.enabled = False
                return

        if cls._instance is not None:
            log.debug("%s already enabled", cls.__name__)
            return

        try:
            cls._instance = cls(tracer=tracer, config=config, service=service)
        except CIVisibilityAuthenticationException:
            log.warning("Authentication error, disabling CI Visibility, please check Datadog API key")
            cls.enabled = False
            return

        cls.enabled = True

        cls._instance.start()
        atexit.register(cls.disable)

        log.debug("%s enabled", cls.__name__)
        log.info(
            "Final settings: coverage collection: %s, "
            "test skipping: %s, "
            "Early Flake Detection: %s, "
            "Auto Test Retries: %s, "
            "Flaky Test Management: %s, "
            "Known Tests: %s",
            cls._instance._collect_coverage_enabled,
            CIVisibility.test_skipping_enabled(),
            CIVisibility.is_efd_enabled(),
            CIVisibility.is_atr_enabled(),
            CIVisibility.is_test_management_enabled(),
            CIVisibility.is_known_tests_enabled(),
        )

    @classmethod
    def disable(cls) -> None:
        if cls._instance is None:
            log.debug("%s not enabled", cls.__name__)
            return
        log.debug("Disabling %s", cls.__name__)
        atexit.unregister(cls.disable)

        cls._instance.stop()
        cls._instance = None
        cls.enabled = False

        telemetry.telemetry_writer.periodic(force_flush=True)

        log.debug("%s disabled", cls.__name__)

    def _start_service(self) -> None:
        tracer_filters = self.tracer._user_trace_processors
        if not any(isinstance(tracer_filter, TraceCiVisibilityFilter) for tracer_filter in tracer_filters):
            tracer_filters += [TraceCiVisibilityFilter(self._tags, self._service)]  # type: ignore[arg-type]
            self.tracer.configure(trace_processors=tracer_filters)

        def _task_fetch_tests_to_skip():
            if self.test_skipping_enabled():
                self._fetch_tests_to_skip()
                if self._itr_data is None:
                    log.warning("Failed to fetch skippable items, no tests will be skipped.")
                    return
                log.info("Intelligent Test Runner skipping level: %s", "suite" if self._suite_skipping_mode else "test")
                log.info("Skippable items fetched: %s", len(self._itr_data.skippable_items))
                log.info("ITR correlation ID: %s", self._itr_data.correlation_id)

        def _task_fetch_known_tests():
            if CIVisibility.is_known_tests_enabled():
                known_test_ids = self._fetch_known_tests()
                if known_test_ids is None:
                    log.warning("Failed to fetch known tests for Early Flake Detection")
                else:
                    self._known_test_ids = known_test_ids
                    log.info("Known tests fetched for Early Flake Detection: %s", len(self._known_test_ids))
            else:
                if (
                    self._api_settings.early_flake_detection.enabled
                    and not ddconfig._test_visibility_early_flake_detection_enabled
                ):
                    log.warning(
                        "Early Flake Detection is enabled by API but disabled by "
                        "DD_TEST_VISIBILITY_EARLY_FLAKE_DETECTION_ENABLED environment variable"
                    )

        def _task_fetch_test_management_tests():
            if self._api_settings.test_management.enabled:
                test_properties = self._fetch_test_management_tests()
                if test_properties is None:
                    log.warning("Failed to fetch quarantined tests from Test Management")
                else:
                    self._test_properties = test_properties

        with ThreadPoolExecutor() as pool:
            pool.submit(_task_fetch_tests_to_skip)
            pool.submit(_task_fetch_known_tests)
            pool.submit(_task_fetch_test_management_tests)

        if self._api_settings.flaky_test_retries_enabled and not asbool(
            os.environ.get("DD_CIVISIBILITY_FLAKY_RETRY_ENABLED", True)
        ):
            log.warning(
                "Auto Test Retries is enabled by API but disabled by "
                "DD_CIVISIBILITY_FLAKY_RETRY_ENABLED environment variable"
            )

    def _stop_service(self) -> None:
        if self._should_upload_git_metadata and not self._git_client.metadata_upload_finished():
            log.debug("git metadata upload still in progress, waiting before shutting down")
            try:
                try:
                    self._git_client._wait_for_metadata_upload(timeout=self.tracer.SHUTDOWN_TIMEOUT)
                except ValueError:
                    log.debug("Error waiting for metadata upload to complete during shutdown", exc_info=True)
            except TimeoutError:
                log.debug("Timed out waiting for metadata upload to complete during shutdown.")
        try:
            self.tracer.shutdown()
        except Exception:
            log.warning("Failed to shutdown tracer", exc_info=True)

    @classmethod
    def set_codeowners_of(cls, location, span=None):
        if not cls.enabled or cls._instance is None or cls._instance._codeowners is None or not location:
            return

        span = span or cls._instance.tracer.current_span()
        if span is None:
            return

        try:
            handles = cls._instance._codeowners.of(location)
            if handles:
                span.set_tag(test.CODEOWNERS, json.dumps(handles))
            else:
                log.debug("no matching codeowners for %s", location)
        except Exception:  # noqa: E722
            log.debug("Error setting codeowners for %s", location, exc_info=True)

    @classmethod
    def add_session(cls, session: TestVisibilitySession):
        log.debug("Adding session: %s", session)
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        if cls._instance._session is not None:
            log.warning("Session already exists: %s", cls._instance._session)
            return
        cls._instance._session = session

    @classmethod
    def get_item_by_id(
        cls,
        item_id: TestVisibilityItemId,
    ):
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        if isinstance(item_id, TestSessionId):
            return cls.get_session()
        if isinstance(item_id, TestModuleId):
            return cls.get_module_by_id(item_id)
        if isinstance(item_id, TestSuiteId):
            return cls.get_suite_by_id(item_id)
        if isinstance(item_id, TestId):
            return cls.get_test_by_id(item_id)
        error_msg = f"Unknown item id type: {type(item_id)}"
        log.warning(error_msg)
        raise CIVisibilityError(error_msg)

    @classmethod
    def get_session(cls) -> TestVisibilitySession:
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        if cls._instance._session is None:
            error_msg = "No session exists"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls._instance._session

    @classmethod
    def get_module_by_id(cls, module_id: TestModuleId) -> TestVisibilityModule:
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls.get_session().get_child_by_id(module_id)

    @classmethod
    def get_suite_by_id(cls, suite_id: TestSuiteId) -> TestVisibilitySuite:
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls.get_module_by_id(suite_id.parent_id).get_child_by_id(suite_id)

    @classmethod
    def get_test_by_id(cls, test_id: TestId) -> TestVisibilityTest:
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls.get_suite_by_id(test_id.parent_id).get_child_by_id(test_id)

    @classmethod
    def get_session_settings(cls) -> TestVisibilitySessionSettings:
        if cls._instance is None:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls.get_session().get_session_settings()

    @classmethod
    def get_instance(cls) -> "CIVisibility":
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        if cls._instance is None:
            error_msg = "CI Visibility is enabled but _instance is None"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        return cls._instance

    @classmethod
    def get_tracer(cls) -> Optional[Tracer]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None:
            return None
        return instance.tracer

    @classmethod
    def get_service(cls) -> Optional[str]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None:
            return None
        return instance._service

    @classmethod
    def get_codeowners(cls) -> Optional[Codeowners]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None:
            return None
        return instance._codeowners

    @classmethod
    def get_efd_api_settings(cls) -> Optional[EarlyFlakeDetectionSettings]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None or instance._api_settings is None:
            return None
        return instance._api_settings.early_flake_detection

    @classmethod
    def get_atr_api_settings(cls) -> Optional[AutoTestRetriesSettings]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None or instance._api_settings is None:
            return None

        if instance._api_settings.flaky_test_retries_enabled:
            # NOTE: this is meant to come from integration settings but current plans to rewrite how integration
            # settings are defined make it better for this logic to be temporarily defined here.

            # defaults
            max_retries = 5
            max_session_total_retries = 1000

            env_max_retries = os.environ.get("DD_CIVISIBILITY_FLAKY_RETRY_COUNT")
            if env_max_retries is not None:
                try:
                    max_retries = int(env_max_retries)
                except ValueError:
                    log.warning(
                        "Failed to parse DD_CIVISIBILITY_FLAKY_RETRY_COUNT, using default value: %s", max_retries
                    )

            env_max_session_total_retries = os.environ.get("DD_CIVISIBILITY_TOTAL_FLAKY_RETRY_COUNT")
            if env_max_session_total_retries is not None:
                try:
                    max_session_total_retries = int(env_max_session_total_retries)
                except ValueError:
                    log.warning(
                        "Failed to parse DD_CIVISIBILITY_TOTAL_FLAKY_RETRY_COUNT, using default value: %s",
                        max_session_total_retries,
                    )

            return AutoTestRetriesSettings(
                enabled=True, max_retries=max_retries, max_session_total_retries=max_session_total_retries
            )

        return None

    @classmethod
    def get_test_management_api_settings(cls) -> Optional[TestManagementSettings]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None or instance._api_settings is None:
            return None
        return instance._api_settings.test_management

    @classmethod
    def get_workspace_path(cls) -> Optional[str]:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None:
            return None
        return instance._tags.get(ci.WORKSPACE_PATH)

    @classmethod
    def is_item_itr_skippable(cls, item_id: TestVisibilityItemId) -> bool:
        if not cls.enabled:
            error_msg = "CI Visibility is not enabled"
            log.warning(error_msg)
            raise CIVisibilityError(error_msg)
        instance = cls.get_instance()
        if instance is None or instance._itr_data is None:
            return False

        if isinstance(item_id, TestSuiteId) and not instance._suite_skipping_mode:
            log.debug("Skipping mode is suite, but item is not a suite: %s", item_id)
            return False

        if isinstance(item_id, TestId) and instance._suite_skipping_mode:
            log.debug("Skipping mode is test, but item is not a test: %s", item_id)
            return False
        return item_id in instance._itr_data.skippable_items

    @classmethod
    def is_unknown_ci(cls) -> bool:
        instance = cls.get_instance()
        if instance is None:
            return False

        return instance._tags.get(ci.PROVIDER_NAME) is None

    @classmethod
    def ci_provider_name_for_telemetry(cls) -> str:
        instance = cls.get_instance()
        if instance is None:
            return UNSUPPORTED_PROVIDER
        return TELEMETRY_BY_PROVIDER_NAME.get(instance._tags.get(ci.PROVIDER_NAME, UNSUPPORTED), UNSUPPORTED_PROVIDER)

    @classmethod
    def is_auto_injected(cls) -> bool:
        instance = cls.get_instance()
        if instance is None:
            return False
        return instance._is_auto_injected

    def _get_ci_visibility_event_client(self) -> Optional[CIVisibilityEventClient]:
        writer = self.tracer._span_aggregator.writer
        if isinstance(writer, CIVisibilityWriter):
            for client in writer._clients:
                if isinstance(client, CIVisibilityEventClient):
                    return client

        return None

    @classmethod
    def set_test_session_name(cls, test_command: str) -> None:
        instance = cls.get_instance()
        client = instance._get_ci_visibility_event_client()
        if not client:
            log.debug("Not setting test session name because no CIVisibilityEventClient is active")
            return

        if ddconfig._test_session_name:
            test_session_name = ddconfig._test_session_name
        else:
            job_name = instance._tags.get(ci.JOB_NAME)
            test_session_name = f"{job_name}-{test_command}" if job_name else test_command

        log.debug("Setting test session name: %s", test_session_name)
        client.set_test_session_name(test_session_name)

    @classmethod
    def set_library_capabilities(cls, capabilities: LibraryCapabilities) -> None:
        instance = cls.get_instance()
        client = instance._get_ci_visibility_event_client()
        if not client:
            log.debug("Not setting library capabilities because no CIVisibilityEventClient is active")
            return
        client.set_metadata("test", capabilities.tags())

    @classmethod
    def get_ci_tags(cls):
        instance = cls.get_instance()
        return instance._tags

    @classmethod
    def get_dd_env(cls):
        instance = cls.get_instance()
        return instance._dd_env

    @classmethod
    def is_known_test(cls, test_id: Union[TestId, InternalTestId]) -> bool:
        instance = cls.get_instance()
        if instance is None:
            return False

        # The assumption that we were not able to fetch unique tests properly if the length is 0 is acceptable
        # because the current EFD usage would cause the session to be faulty even if the query was successful but
        # not unique tests exist. In this case, we assume all tests are unique.
        if len(instance._known_test_ids) == 0:
            return True

        return test_id in instance._known_test_ids

    @classmethod
    def get_test_properties(cls, test_id: Union[TestId, InternalTestId]) -> Optional[TestProperties]:
        instance = cls.get_instance()
        if instance is None:
            return None

        return instance._test_properties.get(test_id)


def _requires_civisibility_enabled(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        if not CIVisibility.enabled:
            log.warning("CI Visibility is not enabled")
            raise CIVisibilityError("CI Visibility is not enabled")
        return func(*args, **kwargs)

    return wrapper


@_requires_civisibility_enabled
def _on_discover_session(discover_args: TestSession.DiscoverArgs) -> None:
    log.debug("Handling session discovery")

    # _requires_civisibility_enabled prevents us from getting here, but this makes type checkers happy
    tracer = CIVisibility.get_tracer()
    test_service = CIVisibility.get_service()
    instance = CIVisibility.get_instance()

    if tracer is None or test_service is None:
        error_msg = "Tracer or test service is None"
        log.warning(error_msg)
        raise CIVisibilityError(error_msg)

    # If we're not provided a root directory, try and extract it from workspace, defaulting to CWD
    workspace_path = discover_args.root_dir or Path(CIVisibility.get_workspace_path() or os.getcwd())

    # Prevent high cardinality of test framework telemetry tag by matching with known frameworks
    test_framework_telemetry_name = _get_test_framework_telemetry_name(discover_args.test_framework)

    efd_api_settings = CIVisibility.get_efd_api_settings()
    if efd_api_settings is None or not CIVisibility.is_efd_enabled():
        efd_api_settings = EarlyFlakeDetectionSettings()

    atr_api_settings = CIVisibility.get_atr_api_settings()
    if atr_api_settings is None or not CIVisibility.is_atr_enabled():
        atr_api_settings = AutoTestRetriesSettings()

    test_management_api_settings = CIVisibility.get_test_management_api_settings()
    if test_management_api_settings is None or not CIVisibility.is_test_management_enabled():
        test_management_api_settings = TestManagementSettings()

    session_settings = TestVisibilitySessionSettings(
        tracer=tracer,
        test_service=test_service,
        test_command=discover_args.test_command,
        reject_duplicates=discover_args.reject_duplicates,
        test_framework=discover_args.test_framework,
        test_framework_metric_name=test_framework_telemetry_name,
        test_framework_version=discover_args.test_framework_version,
        session_operation_name=discover_args.session_operation_name,
        module_operation_name=discover_args.module_operation_name,
        suite_operation_name=discover_args.suite_operation_name,
        test_operation_name=discover_args.test_operation_name,
        workspace_path=workspace_path,
        is_unsupported_ci=CIVisibility.is_unknown_ci(),
        itr_enabled=CIVisibility.is_itr_enabled(),
        itr_test_skipping_enabled=CIVisibility.test_skipping_enabled(),
        itr_test_skipping_level=instance._itr_skipping_level,
        itr_correlation_id=instance._itr_meta.get(ITR_CORRELATION_ID_TAG_NAME, ""),
        coverage_enabled=CIVisibility.should_collect_coverage(),
        known_tests_enabled=CIVisibility.is_known_tests_enabled(),
        efd_settings=efd_api_settings,
        atr_settings=atr_api_settings,
        test_management_settings=test_management_api_settings,
        ci_provider_name=CIVisibility.ci_provider_name_for_telemetry(),
        is_auto_injected=CIVisibility.is_auto_injected(),
    )

    session = TestVisibilitySession(
        session_settings,
    )

    CIVisibility.add_session(session)
    CIVisibility.set_test_session_name(test_command=discover_args.test_command)


@_requires_civisibility_enabled
def _on_start_session() -> None:
    log.debug("Handling start session")
    session = CIVisibility.get_session()
    session.start()


@_requires_civisibility_enabled
def _on_finish_session(finish_args: TestSession.FinishArgs) -> None:
    log.debug("Handling finish session")
    session = CIVisibility.get_session()
    session.finish(finish_args.force_finish_children, finish_args.override_status)


@_requires_civisibility_enabled
def _on_session_is_test_skipping_enabled() -> bool:
    log.debug("Handling is test skipping enabled")
    return CIVisibility.test_skipping_enabled()


@_requires_civisibility_enabled
def _on_session_get_workspace_path() -> Optional[Path]:
    log.debug("Handling finish for session id %s")
    path_str = CIVisibility.get_workspace_path()
    return Path(path_str) if path_str is not None else None


@_requires_civisibility_enabled
def _on_session_should_collect_coverage() -> bool:
    log.debug("Handling should collect coverage")
    return CIVisibility.should_collect_coverage()


@_requires_civisibility_enabled
def _on_session_get_codeowners() -> Optional[Codeowners]:
    log.debug("Getting codeowners")
    return CIVisibility.get_codeowners()


@_requires_civisibility_enabled
def _on_session_get_tracer() -> Optional[Tracer]:
    log.debug("Getting tracer")
    return CIVisibility.get_tracer()


@_requires_civisibility_enabled
def _on_session_is_atr_enabled() -> bool:
    log.debug("Getting Auto Test Retries enabled")
    return CIVisibility.is_atr_enabled()


@_requires_civisibility_enabled
def _on_session_is_efd_enabled() -> bool:
    log.debug("Getting Early Flake Detection enabled")
    return CIVisibility.is_efd_enabled()


@_requires_civisibility_enabled
def _on_session_set_covered_lines_pct(coverage_pct) -> None:
    log.debug("Setting coverage percentage for session to %s", coverage_pct)
    CIVisibility.get_session().set_covered_lines_pct(coverage_pct)


@_requires_civisibility_enabled
def _on_session_set_library_capabilities(capabilities: LibraryCapabilities) -> None:
    log.debug("Setting library capabilities")
    CIVisibility.set_library_capabilities(capabilities)


@_requires_civisibility_enabled
def _on_session_get_path_codeowners(path: Path) -> Optional[List[str]]:
    log.debug("Getting codeowners for path %s", path)
    codeowners = CIVisibility.get_codeowners()
    if codeowners is None:
        return None
    return codeowners.of(str(path))


def _register_session_handlers() -> None:
    log.debug("Registering session handlers")
    core.on("test_visibility.session.discover", _on_discover_session)
    core.on("test_visibility.session.start", _on_start_session)
    core.on("test_visibility.session.finish", _on_finish_session)
    core.on("test_visibility.session.get_codeowners", _on_session_get_codeowners, "codeowners")
    core.on("test_visibility.session.get_tracer", _on_session_get_tracer, "tracer")
    core.on("test_visibility.session.get_path_codeowners", _on_session_get_path_codeowners, "path_codeowners")
    core.on("test_visibility.session.get_workspace_path", _on_session_get_workspace_path, "workspace_path")
    core.on("test_visibility.session.is_atr_enabled", _on_session_is_atr_enabled, "is_atr_enabled")
    core.on("test_visibility.session.is_efd_enabled", _on_session_is_efd_enabled, "is_efd_enabled")
    core.on(
        "test_visibility.session.should_collect_coverage",
        _on_session_should_collect_coverage,
        "should_collect_coverage",
    )
    core.on(
        "test_visibility.session.is_test_skipping_enabled",
        _on_session_is_test_skipping_enabled,
        "is_test_skipping_enabled",
    )
    core.on("test_visibility.session.set_covered_lines_pct", _on_session_set_covered_lines_pct)
    core.on("test_visibility.session.set_library_capabilities", _on_session_set_library_capabilities)


@_requires_civisibility_enabled
def _on_discover_module(discover_args: TestModule.DiscoverArgs) -> None:
    log.debug("Handling discovery for module %s", discover_args.module_id)
    session = CIVisibility.get_session()

    session.add_child(
        discover_args.module_id,
        TestVisibilityModule(
            discover_args.module_id.name,
            CIVisibility.get_session_settings(),
            discover_args.module_path,
        ),
    )


@_requires_civisibility_enabled
def _on_start_module(module_id: TestModuleId) -> None:
    log.debug("Handling start for module id %s", module_id)
    CIVisibility.get_module_by_id(module_id).start()


@_requires_civisibility_enabled
def _on_finish_module(finish_args: TestModule.FinishArgs) -> None:
    log.debug("Handling finish for module id %s", finish_args.module_id)
    CIVisibility.get_module_by_id(finish_args.module_id).finish()


def _register_module_handlers() -> None:
    log.debug("Registering module handlers")
    core.on("test_visibility.module.discover", _on_discover_module)
    core.on("test_visibility.module.start", _on_start_module)
    core.on("test_visibility.module.finish", _on_finish_module)


@_requires_civisibility_enabled
def _on_discover_suite(discover_args: TestSuite.DiscoverArgs) -> None:
    log.debug("Handling discovery for suite args %s", discover_args)
    module = CIVisibility.get_module_by_id(discover_args.suite_id.parent_id)

    module.add_child(
        discover_args.suite_id,
        TestVisibilitySuite(
            discover_args.suite_id.name,
            CIVisibility.get_session_settings(),
            discover_args.codeowners,
            discover_args.source_file_info,
        ),
    )


@_requires_civisibility_enabled
def _on_start_suite(suite_id: TestSuiteId) -> None:
    log.debug("Handling start for suite id %s", suite_id)
    CIVisibility.get_suite_by_id(suite_id).start()


@_requires_civisibility_enabled
def _on_finish_suite(finish_args: TestSuite.FinishArgs) -> None:
    log.debug("Handling finish for suite id %s", finish_args.suite_id)
    CIVisibility.get_suite_by_id(finish_args.suite_id).finish(
        finish_args.force_finish_children, finish_args.override_status
    )


def _register_suite_handlers() -> None:
    log.debug("Registering suite handlers")
    core.on("test_visibility.suite.discover", _on_discover_suite)
    core.on("test_visibility.suite.start", _on_start_suite)
    core.on("test_visibility.suite.finish", _on_finish_suite)


@_requires_civisibility_enabled
def _on_discover_test(discover_args: Test.DiscoverArgs) -> None:
    log.debug("Handling discovery for test %s", discover_args.test_id)
    suite = CIVisibility.get_suite_by_id(discover_args.test_id.parent_id)

    # New tests are currently only considered for EFD:
    # - if known tests were fetched properly (enforced by is_known_test)
    # - if they have no parameters
    if CIVisibility.is_known_tests_enabled() and discover_args.test_id.parameters is None:
        is_new = not CIVisibility.is_known_test(discover_args.test_id)
    else:
        is_new = False

    test_properties = None
    if CIVisibility.is_test_management_enabled():
        test_properties = CIVisibility.get_test_properties(discover_args.test_id)

    if not test_properties:
        test_properties = TestProperties()

    suite.add_child(
        discover_args.test_id,
        TestVisibilityTest(
            discover_args.test_id.name,
            CIVisibility.get_session_settings(),
            parameters=discover_args.test_id.parameters,
            codeowners=discover_args.codeowners,
            source_file_info=discover_args.source_file_info,
            resource=discover_args.resource,
            is_new=is_new,
            is_quarantined=test_properties.quarantined,
            is_disabled=test_properties.disabled,
            is_attempt_to_fix=test_properties.attempt_to_fix,
        ),
    )


@_requires_civisibility_enabled
def _on_is_new_test(test_id: Union[TestId, InternalTestId]) -> bool:
    log.debug("Handling is new test for test %s", test_id)
    return CIVisibility.get_test_by_id(test_id).is_new()


@_requires_civisibility_enabled
def _on_is_quarantined_test(test_id: Union[TestId, InternalTestId]) -> bool:
    log.debug("Handling is quarantined test for test %s", test_id)
    return CIVisibility.get_test_by_id(test_id).is_quarantined()


@_requires_civisibility_enabled
def _on_is_disabled_test(test_id: Union[TestId, InternalTestId]) -> bool:
    log.debug("Handling is disabled test for test %s", test_id)
    return CIVisibility.get_test_by_id(test_id).is_disabled()


@_requires_civisibility_enabled
def _on_is_attempt_to_fix(test_id: Union[TestId, InternalTestId]) -> bool:
    log.debug("Handling is attempt to fix for test %s", test_id)
    return CIVisibility.get_test_by_id(test_id).is_attempt_to_fix()


@_requires_civisibility_enabled
def _on_start_test(test_id: TestId) -> None:
    log.debug("Handling start for test id %s", test_id)
    CIVisibility.get_test_by_id(test_id).start()


@_requires_civisibility_enabled
def _on_finish_test(finish_args: Test.FinishArgs) -> None:
    log.debug("Handling finish for test id %s, with status %s", finish_args.test_id, finish_args.status)
    CIVisibility.get_test_by_id(finish_args.test_id).finish_test(
        finish_args.status, finish_args.skip_reason, finish_args.exc_info
    )


@_requires_civisibility_enabled
def _on_set_test_parameters(item_id: TestId, parameters: str) -> None:
    log.debug("Handling set parameters for test id %s, parameters %s", item_id, parameters)
    CIVisibility.get_test_by_id(item_id).set_parameters(parameters)


@_requires_civisibility_enabled
def _on_set_benchmark_data(set_benchmark_data_args: BenchmarkTestMixin.SetBenchmarkDataArgs) -> None:
    item_id = set_benchmark_data_args.test_id
    data = set_benchmark_data_args.benchmark_data
    is_benchmark = set_benchmark_data_args.is_benchmark
    log.debug("Handling set benchmark data for test id %s, data %s, is_benchmark %s", item_id, data, is_benchmark)
    CIVisibility.get_test_by_id(item_id).set_benchmark_data(data, is_benchmark)


@_requires_civisibility_enabled
def _on_test_overwrite_attributes(overwrite_attribute_args: InternalTest.OverwriteAttributesArgs) -> None:
    item_id = overwrite_attribute_args.test_id
    name = overwrite_attribute_args.name
    suite_name = overwrite_attribute_args.suite_name
    parameters = overwrite_attribute_args.parameters
    codeowners = overwrite_attribute_args.codeowners

    log.debug("Handling overwrite attributes: %s", overwrite_attribute_args)
    CIVisibility.get_test_by_id(item_id).overwrite_attributes(name, suite_name, parameters, codeowners)


def _register_test_handlers():
    log.debug("Registering test handlers")
    core.on("test_visibility.test.discover", _on_discover_test)
    core.on("test_visibility.test.is_new", _on_is_new_test, "is_new")
    core.on("test_visibility.test.is_quarantined", _on_is_quarantined_test, "is_quarantined")
    core.on("test_visibility.test.is_disabled", _on_is_disabled_test, "is_disabled")
    core.on("test_visibility.test.is_attempt_to_fix", _on_is_attempt_to_fix, "is_attempt_to_fix")
    core.on("test_visibility.test.start", _on_start_test)
    core.on("test_visibility.test.finish", _on_finish_test)
    core.on("test_visibility.test.set_parameters", _on_set_test_parameters)
    core.on("test_visibility.test.set_benchmark_data", _on_set_benchmark_data)
    core.on("test_visibility.test.overwrite_attributes", _on_test_overwrite_attributes)


@_requires_civisibility_enabled
def _on_item_get_span(item_id: TestVisibilityItemId) -> Optional[Span]:
    log.debug("Handing get_span for item %s", item_id)
    item = CIVisibility.get_item_by_id(item_id)
    return item.get_span()


@_requires_civisibility_enabled
def _on_item_is_finished(item_id: TestVisibilityItemId) -> bool:
    log.debug("Handling is finished for item %s", item_id)
    return CIVisibility.get_item_by_id(item_id).is_finished()


@_requires_civisibility_enabled
def _on_item_stash_set(item_id: TestVisibilityItemId, key: str, value: object) -> None:
    log.debug("Handling stash set for item %s, key %s, value %s", item_id, key, value)
    CIVisibility.get_item_by_id(item_id).stash_set(key, value)


@_requires_civisibility_enabled
def _on_item_stash_get(item_id: TestVisibilityItemId, key: str) -> Optional[object]:
    log.debug("Handling stash get for item %s, key %s", item_id, key)
    return CIVisibility.get_item_by_id(item_id).stash_get(key)


@_requires_civisibility_enabled
def _on_item_stash_delete(item_id: TestVisibilityItemId, key: str) -> None:
    log.debug("Handling stash delete for item %s, key %s", item_id, key)
    CIVisibility.get_item_by_id(item_id).stash_delete(key)


def _register_item_handlers() -> None:
    log.debug("Registering item handlers")
    core.on("test_visibility.item.get_span", _on_item_get_span, "span")
    core.on("test_visibility.item.is_finished", _on_item_is_finished, "is_finished")
    core.on("test_visibility.item.stash_set", _on_item_stash_set)
    core.on("test_visibility.item.stash_get", _on_item_stash_get, "stash_value")
    core.on("test_visibility.item.stash_delete", _on_item_stash_delete)


@_requires_civisibility_enabled
def _on_get_coverage_data(item_id: Union[TestSuiteId, TestId]) -> Optional[Dict[Path, CoverageLines]]:
    log.debug("Handling get coverage data for item %s", item_id)
    return CIVisibility.get_item_by_id(item_id).get_coverage_data()


@_requires_civisibility_enabled
def _on_add_coverage_data(add_coverage_args: ITRMixin.AddCoverageArgs) -> None:
    """Adds coverage data to an item, merging with existing coverage data if necessary"""
    item_id = add_coverage_args.item_id
    coverage_data = add_coverage_args.coverage_data

    log.debug("Handling add coverage data for item id %s", item_id)

    if not isinstance(item_id, (TestSuiteId, TestId)):
        log.warning("Coverage data can only be added to suites and tests, not %s", type(item_id))
        return

    CIVisibility.get_item_by_id(item_id).add_coverage_data(coverage_data)


def _register_coverage_handlers() -> None:
    log.debug("Registering coverage handlers")
    core.on("test_visibility.item.get_coverage_data", _on_get_coverage_data, "coverage_data")
    core.on("test_visibility.item.add_coverage_data", _on_add_coverage_data)


@_requires_civisibility_enabled
def _on_get_tag(get_tag_args: TestBase.GetTagArgs) -> Any:
    item_id = get_tag_args.item_id
    key = get_tag_args.name
    log.debug("Handling get tag for item id %s, key %s", item_id, key)
    return CIVisibility.get_item_by_id(item_id).get_tag(key)


@_requires_civisibility_enabled
def _on_set_tag(set_tag_args: TestBase.SetTagArgs) -> None:
    item_id = set_tag_args.item_id
    key = set_tag_args.name
    value = set_tag_args.value
    log.debug("Handling set tag for item id %s, key %s, value %s", item_id, key, value)
    CIVisibility.get_item_by_id(item_id).set_tag(key, value)


@_requires_civisibility_enabled
def _on_set_tags(set_tags_args: TestBase.SetTagsArgs) -> None:
    item_id = set_tags_args.item_id
    tags = set_tags_args.tags
    log.debug("Handling set tags for item id %s, tags %s", item_id, tags)
    CIVisibility.get_item_by_id(item_id).set_tags(tags)


@_requires_civisibility_enabled
def _on_delete_tag(delete_tag_args: TestBase.DeleteTagArgs) -> None:
    item_id = delete_tag_args.item_id
    key = delete_tag_args.name
    log.debug("Handling delete tag for item id %s, key %s", item_id, key)
    CIVisibility.get_item_by_id(item_id).delete_tag(key)


@_requires_civisibility_enabled
def _on_delete_tags(delete_tags_args: TestBase.DeleteTagsArgs) -> None:
    item_id = delete_tags_args.item_id
    keys = delete_tags_args.names
    log.debug("Handling delete tags for item id %s, keys %s", item_id, keys)
    CIVisibility.get_item_by_id(item_id).delete_tags(keys)


def _register_tag_handlers() -> None:
    log.debug("Registering tag handlers")
    core.on("test_visibility.item.get_tag", _on_get_tag, "tag_value")
    core.on("test_visibility.item.set_tag", _on_set_tag)
    core.on("test_visibility.item.set_tags", _on_set_tags)
    core.on("test_visibility.item.delete_tag", _on_delete_tag)
    core.on("test_visibility.item.delete_tags", _on_delete_tags)


@_requires_civisibility_enabled
def _on_itr_finish_item_skipped(item_id: Union[TestSuiteId, TestId]) -> None:
    log.debug("Handling finish ITR skipped for item id %s", item_id)
    if not isinstance(item_id, (TestSuiteId, TestId)):
        log.warning("Only suites or tests can be skipped, not %s", type(item_id))
        return
    CIVisibility.get_item_by_id(item_id).finish_itr_skipped()


@_requires_civisibility_enabled
def _on_itr_mark_unskippable(item_id: Union[TestSuiteId, TestId]) -> None:
    log.debug("Handling marking %s unskippable", item_id)
    CIVisibility.get_item_by_id(item_id).mark_itr_unskippable()


@_requires_civisibility_enabled
def _on_itr_mark_forced_run(item_id: Union[TestSuiteId, TestId]) -> None:
    log.debug("Handling marking %s as forced run", item_id)
    CIVisibility.get_item_by_id(item_id).mark_itr_forced_run()


@_requires_civisibility_enabled
def _on_itr_was_forced_run(item_id: TestVisibilityItemId) -> bool:
    log.debug("Handling marking %s as forced run", item_id)
    return CIVisibility.get_item_by_id(item_id).was_itr_forced_run()


@_requires_civisibility_enabled
def _on_itr_is_item_skippable(item_id: Union[TestSuiteId, TestId]) -> bool:
    """Skippable items are fetched as part CIVisibility.enable(), so they are assumed to be available."""
    log.debug("Handling is item skippable for item id %s", item_id)

    if not isinstance(item_id, (TestSuiteId, TestId)):
        log.warning("Only suites or tests can be skippable, not %s", type(item_id))
        return False

    if not CIVisibility.test_skipping_enabled():
        log.debug("Test skipping is not enabled")
        return False

    return CIVisibility.is_item_itr_skippable(item_id)


@_requires_civisibility_enabled
def _on_itr_is_item_unskippable(item_id: Union[TestSuiteId, TestId]) -> bool:
    log.debug("Handling is item unskippable for %s", item_id)
    if not isinstance(item_id, (TestSuiteId, TestId)):
        raise CIVisibilityError("Only suites or tests can be unskippable")
    return CIVisibility.get_item_by_id(item_id).is_itr_unskippable()


@_requires_civisibility_enabled
def _on_itr_was_item_skipped(item_id: Union[TestSuiteId, TestId]) -> bool:
    log.debug("Handling was item skipped for %s", item_id)
    return CIVisibility.get_item_by_id(item_id).is_itr_skipped()


def _register_itr_handlers() -> None:
    log.debug("Registering ITR-related handlers")
    core.on("test_visibility.itr.finish_skipped_by_itr", _on_itr_finish_item_skipped)
    core.on("test_visibility.itr.is_item_skippable", _on_itr_is_item_skippable, "is_item_skippable")
    core.on("test_visibility.itr.was_item_skipped", _on_itr_was_item_skipped, "was_item_skipped")

    core.on("test_visibility.itr.is_item_unskippable", _on_itr_is_item_unskippable, "is_item_unskippable")
    core.on("test_visibility.itr.mark_forced_run", _on_itr_mark_forced_run)
    core.on("test_visibility.itr.mark_unskippable", _on_itr_mark_unskippable)
    core.on("test_visibility.itr.was_forced_run", _on_itr_was_forced_run, "was_forced_run")


#
# EFD handlers
#


@_requires_civisibility_enabled
def _on_efd_is_enabled() -> bool:
    return CIVisibility.get_session().efd_is_enabled()


@_requires_civisibility_enabled
def _on_efd_session_is_faulty() -> bool:
    return CIVisibility.get_session().efd_is_faulty_session()


@_requires_civisibility_enabled
def _on_efd_session_has_efd_failed_tests() -> bool:
    return CIVisibility.get_session().efd_has_failed_tests()


@_requires_civisibility_enabled
def _on_efd_should_retry_test(test_id: InternalTestId) -> bool:
    return CIVisibility.get_test_by_id(test_id).efd_should_retry()


@_requires_civisibility_enabled
def _on_efd_add_retry(test_id: InternalTestId, retry_number: int) -> Optional[int]:
    return CIVisibility.get_test_by_id(test_id).efd_add_retry(retry_number)


@_requires_civisibility_enabled
def _on_efd_start_retry(test_id: InternalTestId, retry_number: int) -> None:
    CIVisibility.get_test_by_id(test_id).efd_start_retry(retry_number)


@_requires_civisibility_enabled
def _on_efd_finish_retry(efd_finish_args: EFDTestMixin.EFDRetryFinishArgs) -> None:
    CIVisibility.get_test_by_id(efd_finish_args.test_id).efd_finish_retry(
        efd_finish_args.retry_number, efd_finish_args.status, efd_finish_args.exc_info
    )


@_requires_civisibility_enabled
def _on_efd_get_final_status(test_id: InternalTestId) -> EFDTestStatus:
    return CIVisibility.get_test_by_id(test_id).efd_get_final_status()


def _register_efd_handlers() -> None:
    log.debug("Registering EFD handlers")
    core.on("test_visibility.efd.is_enabled", _on_efd_is_enabled, "is_enabled")
    core.on("test_visibility.efd.session_is_faulty", _on_efd_session_is_faulty, "is_faulty_session")
    core.on("test_visibility.efd.session_has_failed_tests", _on_efd_session_has_efd_failed_tests, "has_failed_tests")
    core.on("test_visibility.efd.should_retry_test", _on_efd_should_retry_test, "should_retry_test")
    core.on("test_visibility.efd.add_retry", _on_efd_add_retry, "retry_number")
    core.on("test_visibility.efd.start_retry", _on_efd_start_retry)
    core.on("test_visibility.efd.finish_retry", _on_efd_finish_retry)
    core.on("test_visibility.efd.get_final_status", _on_efd_get_final_status, "efd_final_status")


@_requires_civisibility_enabled
def _on_atr_is_enabled() -> bool:
    return CIVisibility.is_atr_enabled()


@_requires_civisibility_enabled
def _on_atr_session_has_failed_tests() -> bool:
    return CIVisibility.get_session().atr_has_failed_tests()


@_requires_civisibility_enabled
def _on_atr_should_retry_test(item_id: InternalTestId) -> bool:
    return CIVisibility.get_test_by_id(item_id).atr_should_retry()


@_requires_civisibility_enabled
def _on_atr_add_retry(item_id: InternalTestId, retry_number: int) -> Optional[int]:
    return CIVisibility.get_test_by_id(item_id).atr_add_retry(retry_number)


@_requires_civisibility_enabled
def _on_atr_start_retry(test_id: InternalTestId, retry_number: int) -> None:
    CIVisibility.get_test_by_id(test_id).atr_start_retry(retry_number)


@_requires_civisibility_enabled
def _on_atr_finish_retry(atr_finish_args: ATRTestMixin.ATRRetryFinishArgs) -> None:
    CIVisibility.get_test_by_id(atr_finish_args.test_id).atr_finish_retry(
        atr_finish_args.retry_number, atr_finish_args.status, atr_finish_args.exc_info
    )


@_requires_civisibility_enabled
def _on_atr_get_final_status(test_id: InternalTestId) -> TestStatus:
    return CIVisibility.get_test_by_id(test_id).atr_get_final_status()


def _register_atr_handlers() -> None:
    log.debug("Registering ATR handlers")
    core.on("test_visibility.atr.is_enabled", _on_atr_is_enabled, "is_enabled")
    core.on("test_visibility.atr.session_has_failed_tests", _on_atr_session_has_failed_tests, "has_failed_tests")
    core.on("test_visibility.atr.should_retry_test", _on_atr_should_retry_test, "should_retry_test")
    core.on("test_visibility.atr.add_retry", _on_atr_add_retry, "retry_number")
    core.on("test_visibility.atr.start_retry", _on_atr_start_retry)
    core.on("test_visibility.atr.finish_retry", _on_atr_finish_retry)
    core.on("test_visibility.atr.get_final_status", _on_atr_get_final_status, "atr_final_status")


@_requires_civisibility_enabled
def _on_attempt_to_fix_should_retry_test(item_id: InternalTestId) -> bool:
    return CIVisibility.get_test_by_id(item_id).attempt_to_fix_should_retry()


@_requires_civisibility_enabled
def _on_attempt_to_fix_add_retry(item_id: InternalTestId, retry_number: int) -> Optional[int]:
    return CIVisibility.get_test_by_id(item_id).attempt_to_fix_add_retry(retry_number)


@_requires_civisibility_enabled
def _on_attempt_to_fix_start_retry(test_id: InternalTestId, retry_number: int) -> None:
    CIVisibility.get_test_by_id(test_id).attempt_to_fix_start_retry(retry_number)


@_requires_civisibility_enabled
def _on_attempt_to_fix_finish_retry(
    attempt_to_fix_finish_args: AttemptToFixTestMixin.AttemptToFixRetryFinishArgs,
) -> None:
    CIVisibility.get_test_by_id(attempt_to_fix_finish_args.test_id).attempt_to_fix_finish_retry(
        attempt_to_fix_finish_args.retry_number, attempt_to_fix_finish_args.status, attempt_to_fix_finish_args.exc_info
    )


@_requires_civisibility_enabled
def _on_attempt_to_fix_get_final_status(test_id: InternalTestId) -> TestStatus:
    return CIVisibility.get_test_by_id(test_id).attempt_to_fix_get_final_status()


@_requires_civisibility_enabled
def _on_attempt_to_fix_session_has_failed_tests() -> bool:
    return CIVisibility.get_session().attempt_to_fix_has_failed_tests()


def _register_attempt_to_fix_handlers() -> None:
    log.debug("Registering AttemptToFix handlers")
    core.on(
        "test_visibility.attempt_to_fix.should_retry_test", _on_attempt_to_fix_should_retry_test, "should_retry_test"
    )
    core.on("test_visibility.attempt_to_fix.add_retry", _on_attempt_to_fix_add_retry, "retry_number")
    core.on("test_visibility.attempt_to_fix.start_retry", _on_attempt_to_fix_start_retry)
    core.on("test_visibility.attempt_to_fix.finish_retry", _on_attempt_to_fix_finish_retry)
    core.on(
        "test_visibility.attempt_to_fix.session_has_failed_tests",
        _on_attempt_to_fix_session_has_failed_tests,
        "has_failed_tests",
    )
    core.on(
        "test_visibility.attempt_to_fix.get_final_status",
        _on_attempt_to_fix_get_final_status,
        "attempt_to_fix_final_status",
    )


_register_session_handlers()
_register_module_handlers()
_register_suite_handlers()
_register_test_handlers()
_register_item_handlers()
_register_tag_handlers()
_register_coverage_handlers()
_register_itr_handlers()
_register_efd_handlers()
_register_atr_handlers()
_register_attempt_to_fix_handlers()
