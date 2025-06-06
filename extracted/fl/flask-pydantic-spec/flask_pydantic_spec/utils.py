import inspect
import json
import logging
import re
from json import JSONDecodeError

from typing import (
    Callable,
    Mapping,
    Any,
    Tuple,
    Optional,
    List,
    Dict,
    Iterable,
    Type,
)

from werkzeug.datastructures import MultiDict
from pydantic import BaseModel, v1
from werkzeug.routing import Rule

from .constants import OPENAPI_SCHEMA_TEMPLATE
from .types import BaseModelT, BaseModelUnion, Response, RequestBase, Request

logger = logging.getLogger(__name__)

VALID_NAME_REGEX = re.compile(r"[^a-zA-Z0-9._-]")


def get_model_name(model: Type[BaseModelUnion]) -> str:
    """Gets the name of a model name as an OpenAPI 3.1 compatible name

    Replaces any non standard characters in a string with `_`

    >>> format_model_name("AB[C[D]]")
    AB_C_D__
    """
    return VALID_NAME_REGEX.sub("_", model.__name__)


def get_model_schema(model: Type[BaseModelUnion]) -> Dict[str, Any]:
    if issubclass(model, BaseModel):
        return model.model_json_schema(ref_template=OPENAPI_SCHEMA_TEMPLATE)
    elif issubclass(model, v1.BaseModel):
        schema = model.schema(ref_template=OPENAPI_SCHEMA_TEMPLATE)
        if "definitions" in schema:
            # definitions was renamed to $defs
            # https://opis.io/json-schema/2.x/structure.html#defs-keyword
            schema["$defs"] = schema.pop("definitions")
        return schema
    else:
        raise ValueError(f"Unsupported model type: {type(model)}")


def load_model_schema(model: Type[BaseModelT], data: Any) -> BaseModelT:
    if issubclass(model, BaseModel):
        return model.model_validate(data)  # type: ignore[return-value]
    elif issubclass(model, v1.BaseModel):
        return model.parse_obj(data)  # type: ignore[return-value]
    else:
        raise ValueError(f"Unsupported model type: {type(model)}")


def parse_comments(func: Callable) -> Tuple[Optional[str], Optional[str]]:
    """
    parse function comments

    First line of comments will be saved as summary, and the rest
    will be saved as description.
    """
    doc = inspect.getdoc(func)
    if doc is None:
        return None, None
    docs = doc.split("\n", 1)
    if len(docs) == 1:
        return docs[0], None
    return docs[0], docs[1].strip()


def parse_request(func: Callable) -> Mapping[str, Any]:
    """
    Generate spec from body parameter on the view function validation decorator
    """
    if hasattr(func, "body"):
        request_body = getattr(func, "body")
        if isinstance(request_body, RequestBase):
            result: Mapping[str, Any] = request_body.generate_spec()
        elif issubclass(request_body, (BaseModel, v1.BaseModel)):
            result = Request(request_body).generate_spec()
        else:
            result = {}
        return result
    return {}


def parse_params(
    func: Callable,
    params: List[Mapping[str, Any]],
    models: Mapping[str, Any],
) -> List[Mapping[str, Any]]:
    """
    get spec for (query, headers, cookies)
    """
    if hasattr(func, "query"):
        model_name = getattr(func, "query").__name__
        query = models.get(model_name)
        if query is not None:
            for name, schema in query["properties"].items():
                params.append(
                    {
                        "name": name,
                        "in": "query",
                        "schema": schema,
                        "required": name in query.get("required", []),
                    }
                )

    if hasattr(func, "headers"):
        model_name = getattr(func, "headers").__name__
        headers = models.get(model_name)
        if headers is not None:
            for name, schema in headers["properties"].items():
                params.append(
                    {
                        "name": name,
                        "in": "header",
                        "schema": schema,
                        "required": name in headers.get("required", []),
                    }
                )

    if hasattr(func, "cookies"):
        model_name = getattr(func, "cookies").__name__
        cookies = models.get(model_name)
        if cookies is not None:
            for name, schema in cookies["properties"].items():
                params.append(
                    {
                        "name": name,
                        "in": "cookie",
                        "schema": schema,
                        "required": name in cookies.get("required", []),
                    }
                )

    return params


def parse_resp(func: Callable, code: int) -> Mapping[str, Mapping[str, Any]]:
    """
    get the response spec

    If this function does not have explicit ``resp`` but have other models,
    a ``Validation Error`` will be append to the response spec. Since
    this may be triggered in the validation step.
    """
    responses: Dict[str, Any] = {}
    if hasattr(func, "resp"):
        response = getattr(func, "resp")
        if response:
            responses = response.generate_spec()

    if str(code) not in responses and has_model(func):
        responses[str(code)] = {"description": "Validation Error"}

    return responses


def has_model(func: Callable) -> bool:
    """
    return True if this function have ``pydantic.BaseModel``
    """
    if any(hasattr(func, x) for x in ("query", "json", "headers")):
        return True

    if hasattr(func, "resp") and getattr(func, "resp").has_model():
        return True

    return False


def default_before_handler(
    req: Request, resp: Response, req_validation_error: Any, instance: BaseModel
) -> None:
    """
    default handler called before the endpoint function after the request validation

    :param req: request provided by the web framework
    :param resp: response generated by Flask_Pydantic_Spec that will be returned
        if the validation error is not None
    :param req_validation_error: request validation error
    :param instance: class instance if the endpoint function is a class method
    """
    if req_validation_error:
        logger.info(
            "Validation Error",
            extra={
                "spectree_model": req_validation_error.__class__.__name__,
                "spectree_validation": req_validation_error.errors(),
            },
        )


def default_after_handler(
    req: Request, resp: Response, resp_validation_error: Any, instance: BaseModel
) -> None:
    """
    default handler called after the response validation

    :param req: request provided by the web framework
    :param resp: response from the endpoint function (if there is no validation error)
        or response validation error
    :param resp_validation_error: response validation error
    :param instance: class instance if the endpoint function is a class method
    """
    if resp_validation_error:
        logger.info(
            "500 Response Validation Error",
            extra={
                "spectree_model": resp_validation_error.__class__.__name__,
                "spectree_validation": resp_validation_error.errors(),
            },
        )


def parse_multi_dict(input: MultiDict) -> Dict[str, Any]:
    result = {}
    for key, value in input.to_dict(flat=False).items():
        if len(value) == 1:
            try:
                value_to_use = json.loads(value[0])
            except (TypeError, JSONDecodeError):
                value_to_use = value[0]
        else:
            value_to_use = value
        result[key] = value_to_use
    return result


RE_PARSE_RULE = re.compile(
    r"""
    (?P<static>[^<]*)                           # static rule data
    <
    (?:
        (?P<converter>[a-zA-Z_][a-zA-Z0-9_]*)   # converter name
        (?:\((?P<args>.*?)\))?                  # converter arguments
        \:                                      # variable delimiter
    )?
    (?P<variable>[a-zA-Z_][a-zA-Z0-9_]*)        # variable name
    >
    """,
    re.VERBOSE,
)


def parse_rule(rule: Rule) -> Iterable[Tuple[Optional[str], Optional[str], str]]:
    """
    Parse a rule and return it as generator. Each iteration yields tuples in the form
    ``(converter, arguments, variable)``.
    If the converter is `None` it's a static url part, otherwise it's a dynamic one.
    Note: This originally lived in werkzeug.routing.parse_rule until it was
    removed in werkzeug 2.2.0.
    TODO - cgearing - do we really need this?
    """
    rule_str = str(rule)
    pos = 0
    end = len(rule_str)
    do_match = RE_PARSE_RULE.match
    used_names = set()
    while pos < end:
        m = do_match(rule_str, pos)
        if m is None:
            break
        data = m.groupdict()
        if data["static"]:
            yield None, None, data["static"]
        variable = data["variable"]
        converter = data["converter"] or "default"
        if variable in used_names:
            raise ValueError(f"variable name {variable!r} used twice.")
        used_names.add(variable)
        yield converter, data["args"] or None, variable
        pos = m.end()
    if pos < end:
        remaining = rule_str[pos:]
        if ">" in remaining or "<" in remaining:
            raise ValueError(f"malformed url rule: {rule_str!r}")
        yield None, None, remaining
