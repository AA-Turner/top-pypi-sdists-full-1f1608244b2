import io
import json
from typing import Any  # noqa:F401
from typing import Dict  # noqa:F401
from typing import List  # noqa:F401
from typing import Mapping  # noqa:F401
from typing import Text  # noqa:F401
from typing import Union  # noqa:F401

import django
from django.utils.functional import SimpleLazyObject
from wrapt import FunctionWrapper
import xmltodict

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.django.compat import get_resolver
from ddtrace.contrib.internal.django.compat import user_is_authenticated
from ddtrace.ext import SpanTypes
from ddtrace.ext import user as _user
from ddtrace.internal import compat
from ddtrace.internal import core
from ddtrace.internal.logger import get_logger
from ddtrace.internal.utils.formats import stringify_cache_args
from ddtrace.internal.utils.http import parse_form_multipart
from ddtrace.internal.utils.http import parse_form_params
from ddtrace.internal.utils.importlib import func_name
from ddtrace.propagation._utils import from_wsgi_header
from ddtrace.trace import Span


try:
    from json import JSONDecodeError
except ImportError:
    # handling python 2.X import error
    JSONDecodeError = ValueError  # type: ignore


log = get_logger(__name__)

if django.VERSION < (1, 10, 0):
    Resolver404 = django.core.urlresolvers.Resolver404
else:
    Resolver404 = django.urls.exceptions.Resolver404


DJANGO22 = django.VERSION >= (2, 2, 0)

REQUEST_DEFAULT_RESOURCE = "__django_request"
_BODY_METHODS = {"POST", "PUT", "DELETE", "PATCH"}

_quantize_text = Union[Text, bytes]
_quantize_param = Union[_quantize_text, List[_quantize_text], Dict[_quantize_text, Any], Any]


def resource_from_cache_prefix(resource, cache):
    """
    Combine the resource name with the cache prefix (if any)
    """
    if getattr(cache, "key_prefix", None):
        name = " ".join((resource, cache.key_prefix))
    else:
        name = resource

    # enforce lowercase to make the output nicer to read
    return name.lower()


def quantize_key_values(keys):
    # type: (_quantize_param) -> Text
    """
    Used for Django cache key normalization.

    If a dict is provided we return a list of keys as text.

    If a list or tuple is provided we convert each element to text.

    If text is provided we convert to text.
    """
    args = []  # type: List[Union[Text, bytes, Any]]

    # Normalize input values into a List[Text, bytes]
    if isinstance(keys, dict):
        args = list(keys.keys())
    elif isinstance(keys, (list, tuple)):
        args = keys
    else:
        args = [keys]

    return stringify_cache_args(args)


def get_django_2_route(request, resolver_match):
    # Try to use `resolver_match.route` if available
    # Otherwise, look for `resolver.pattern.regex.pattern`
    route = resolver_match.route
    if route:
        return route

    resolver = get_resolver(getattr(request, "urlconf", None))
    if resolver:
        try:
            return resolver.pattern.regex.pattern
        except AttributeError:
            pass

    return None


def set_tag_array(span, prefix, value):
    """Helper to set a span tag as a single value or an array"""
    if not value:
        return

    if len(value) == 1:
        if value[0]:
            span.set_tag_str(prefix, value[0])
    else:
        for i, v in enumerate(value, start=0):
            if v:
                span.set_tag_str("".join((prefix, ".", str(i))), v)


def get_request_uri(request):
    """
    Helper to rebuild the original request url

    query string or fragments are not included.
    """
    # DEV: Use django.http.request.HttpRequest._get_raw_host() when available
    # otherwise back-off to PEP 333 as done in django 1.8.x
    if hasattr(request, "_get_raw_host"):
        host = request._get_raw_host()
    else:
        try:
            # Try to build host how Django would have
            # https://github.com/django/django/blob/e8d0d2a5efc8012dcc8bf1809dec065ebde64c81/django/http/request.py#L85-L102
            if "HTTP_HOST" in request.META:
                host = request.META["HTTP_HOST"]
            else:
                host = request.META["SERVER_NAME"]
                port = str(request.META["SERVER_PORT"])
                if port != ("443" if request.is_secure() else "80"):
                    host = "".join((host, ":", port))
        except Exception:
            # This really shouldn't ever happen, but lets guard here just in case
            log.debug("Failed to build Django request host", exc_info=True)
            host = "unknown"

    # If request scheme is missing, possible in case where wsgi.url_scheme
    # environ has not been set, return None and skip providing a uri
    if request.scheme is None:
        return

    # Build request url from the information available
    # DEV: We are explicitly omitting query strings since they may contain sensitive information
    urlparts = {"scheme": request.scheme, "netloc": host, "path": request.path}

    # If any url part is a SimpleLazyObject, use its __class__ property to cast
    # str/bytes and allow for _setup() to execute
    for k, v in urlparts.items():
        if isinstance(v, SimpleLazyObject):
            if issubclass(v.__class__, str):
                v = str(v)
            elif issubclass(v.__class__, bytes):
                v = bytes(v)
            else:
                # lazy object that is not str or bytes should not happen here
                # but if it does skip providing a uri
                log.debug(
                    "Skipped building Django request uri, %s is SimpleLazyObject wrapping a %s class",
                    k,
                    v.__class__.__name__,
                )
                return None
        urlparts[k] = compat.ensure_text(v)

    return "".join((urlparts["scheme"], "://", urlparts["netloc"], urlparts["path"]))


def _set_resolver_tags(pin, span, request):
    # Default to just the HTTP method when we cannot determine a reasonable resource
    resource = request.method

    try:
        # Get resolver match result and build resource name pieces
        resolver_match = request.resolver_match
        if not resolver_match:
            # The request quite likely failed (e.g. 404) so we do the resolution anyway.
            resolver = get_resolver(getattr(request, "urlconf", None))
            resolver_match = resolver.resolve(request.path_info)

        if hasattr(resolver_match[0], "view_class"):
            # In django==4.0, view.__name__ defaults to <module>.views.view
            # Accessing view.view_class is required for django>4.0 to get the name of underlying view
            handler = func_name(resolver_match[0].view_class)
        else:
            handler = func_name(resolver_match[0])

        route = None
        # In Django >= 2.2.0 we can access the original route or regex pattern
        # TODO: Validate if `resolver.pattern.regex.pattern` is available on django<2.2
        if DJANGO22:
            # Determine the resolver and resource name for this request
            route = get_django_2_route(request, resolver_match)
            if route:
                span.set_tag_str("http.route", route)

        if config.django.use_handler_resource_format:
            resource = " ".join((request.method, handler))
        elif config.django.use_legacy_resource_format:
            resource = handler
        else:
            if route:
                resource = " ".join((request.method, route))
            else:
                if config.django.use_handler_with_url_name_resource_format:
                    # Append url name in order to distinguish different routes of the same ViewSet
                    url_name = resolver_match.url_name
                    if url_name:
                        handler = ".".join([handler, url_name])

                resource = " ".join((request.method, handler))

        span.set_tag_str("django.view", resolver_match.view_name)
        set_tag_array(span, "django.namespace", resolver_match.namespaces)

        # Django >= 2.0.0
        if hasattr(resolver_match, "app_names"):
            set_tag_array(span, "django.app", resolver_match.app_names)

    except Resolver404:
        # Normalize all 404 requests into a single resource name
        # DEV: This is for potential cardinality issues
        resource = " ".join((request.method, "404"))
    except Exception:
        log.debug(
            "Failed to resolve request path %r with path info %r",
            request,
            getattr(request, "path_info", "not-set"),
            exc_info=True,
        )
    finally:
        # Only update the resource name if it was not explicitly set
        # by anyone during the request lifetime
        if span.resource == REQUEST_DEFAULT_RESOURCE:
            span.resource = resource


def _before_request_tags(pin, span, request):
    # DEV: Do not set `span.resource` here, leave it as `None`
    #      until `_set_resolver_tags` so we can know if the user
    #      has explicitly set it during the request lifetime
    span.service = trace_utils.int_service(pin, config.django)
    span.span_type = SpanTypes.WEB
    span._metrics[_SPAN_MEASURED_KEY] = 1

    span.set_tag_str("django.request.class", func_name(request))


def _extract_body(request):
    # DEV: Do not use request.POST or request.data, this could prevent custom parser to be used after
    if request.method in _BODY_METHODS:
        req_body = None
        content_type = request.content_type if hasattr(request, "content_type") else request.META.get("CONTENT_TYPE")
        headers = core.dispatch_with_results("django.extract_body").headers.value
        try:
            if content_type == "application/x-www-form-urlencoded":
                req_body = parse_form_params(request.body.decode("UTF-8", errors="ignore"))
            elif content_type == "multipart/form-data":
                req_body = parse_form_multipart(request.body.decode("UTF-8", errors="ignore"), headers)
            elif content_type in ("application/json", "text/json"):
                req_body = json.loads(request.body.decode("UTF-8", errors="ignore"))
            elif content_type in ("application/xml", "text/xml"):
                req_body = xmltodict.parse(request.body.decode("UTF-8", errors="ignore"))
            else:  # text/plain, others: don't use them
                req_body = None
        except Exception:
            log.debug("Failed to parse request body", exc_info=True)
        return req_body


def _remake_body(request):
    # some libs that utilize django (Spyne) require the body stream to be unread or else will throw errors
    # see: https://github.com/arskom/spyne/blob/f105ec2f41495485fef1211fe73394231b3f76e5/spyne/server/wsgi.py#L538
    if request.method in _BODY_METHODS and getattr(request, "_body", None):
        try:
            unread_body = io.BytesIO(request._body)
            if unread_body.seekable():
                unread_body.seek(0)
                request.META["wsgi.input"] = unread_body
        except Exception:
            log.debug("Failed to remake Django request body", exc_info=True)


def _get_request_headers(request):
    # type: (Any) -> Mapping[str, str]
    if DJANGO22:
        request_headers = request.headers  # type: Mapping[str, str]
    else:
        request_headers = {}  # type: Mapping[str, str]
        for header, value in request.META.items():
            name = from_wsgi_header(header)
            if name:
                request_headers[name] = value

    return request_headers


def _after_request_tags(pin, span: Span, request, response):
    # Response can be None in the event that the request failed
    # We still want to set additional request tags that are resolved
    # during the request.
    try:
        user = getattr(request, "user", None)
        if user is not None:
            # Note: getattr calls to user / user_is_authenticated may result in ImproperlyConfigured exceptions from
            # Django's get_user_model():
            # https://github.com/django/django/blob/a464ead29db8bf6a27a5291cad9eb3f0f3f0472b/django/contrib/auth/__init__.py
            #
            # FIXME: getattr calls to user fail in async contexts.
            # Sample Error: django.core.exceptions.SynchronousOnlyOperation: You cannot call this from an async context
            # - use a thread or sync_to_async.
            try:
                if hasattr(user, "is_authenticated"):
                    span.set_tag_str("django.user.is_authenticated", str(user_is_authenticated(user)))

                uid = getattr(user, "pk", None)
                if uid and isinstance(uid, int):
                    span.set_tag_str("django.user.id", str(uid))
                    span.set_tag_str(_user.ID, str(uid))
                if config.django.include_user_name:
                    username = getattr(user, "username", None)
                    if username:
                        span.set_tag_str("django.user.name", username)
            except Exception:
                log.debug("Error retrieving authentication information for user", exc_info=True)

        # DEV: Resolve the view and resource name at the end of the request in case
        #      urlconf changes at any point during the request
        _set_resolver_tags(pin, span, request)
        if response:
            status = response.status_code
            span.set_tag_str("django.response.class", func_name(response))
            if hasattr(response, "template_name"):
                # template_name is a bit of a misnomer, as it could be any of:
                # a list of strings, a tuple of strings, a single string, or an instance of Template
                # for more detail, see:
                # https://docs.djangoproject.com/en/3.0/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name
                template = response.template_name

                if isinstance(template, str):
                    template_names = [template]
                elif isinstance(
                    template,
                    (
                        list,
                        tuple,
                    ),
                ):
                    template_names = template
                elif hasattr(template, "template"):
                    # ^ checking by attribute here because
                    # django backend implementations don't have a common base
                    # `.template` is also the most consistent across django versions
                    template_names = [template.template.name]
                else:
                    template_names = None

                set_tag_array(span, "django.response.template", template_names)

            url = get_request_uri(request)

            request_headers = core.dispatch_with_results("django.after_request_headers").headers.value
            if not request_headers:
                request_headers = _get_request_headers(request)

            response_headers = dict(response.items()) if response else {}

            response_cookies = {}
            if response.cookies:
                for k, v in response.cookies.items():
                    # `v` is a http.cookies.Morsel class instance in some scenarios:
                    # 'cookie_key=cookie_value; HttpOnly; Path=/; SameSite=Strict'
                    try:
                        i = 0
                        result = ""
                        for element in v.OutputString().split(";"):
                            if i == 0:
                                # split cookie_key="cookie_value"
                                key, value = element.split("=", 1)
                                # Remove quotes "cookie_value"
                                result = value[1:-1] if value.startswith('"') and value[-1] == '"' else value
                            else:
                                result += ";" + element
                            i += 1
                        response_cookies[k] = result
                    except Exception:
                        # parse cookies by the old way
                        response_cookies[k] = v.OutputString()

            raw_uri = url
            if raw_uri and request.META.get("QUERY_STRING"):
                raw_uri += "?" + request.META["QUERY_STRING"]

            core.dispatch(
                "django.after_request_headers.post",
                (
                    request_headers,
                    response_headers,
                    span,
                    config.django,
                    request,
                    url,
                    raw_uri,
                    status,
                    response_cookies,
                ),
            )
            content = getattr(response, "content", None)
            if content is None:
                content = getattr(response, "streaming_content", None)
            core.dispatch("django.after_request_headers.finalize", (content, None))
    finally:
        if span.resource == REQUEST_DEFAULT_RESOURCE:
            span.resource = request.method


class DjangoViewProxy(FunctionWrapper):
    """
    This custom function wrapper is used to wrap the callback passed to django views handlers (path/re_path/url).
    This allows us to distinguish between wrapped django views and wrapped asgi applications in django channels.
    """

    @property
    def __module__(self):
        """
        DjangoViewProxy.__module__ defaults to ddtrace.contrib.internal.django when a wrapped function does not have
        a __module__ attribute. This method ensures that DjangoViewProxy.__module__ always returns the module
        attribute of the wrapped function or an empty string if this attribute is not available.
        The function Django.urls.path() does not have a __module__ attribute and would require this override
        to resolve the correct module name.
        """
        return self.__wrapped__.__module__
