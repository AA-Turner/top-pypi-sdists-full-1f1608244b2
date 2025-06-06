"""Data formatter."""
from collections import defaultdict
import json
from functools import singledispatch
import pathlib
import keyword
import warnings
import re
from uuid import UUID
import dateutil.parser
import m2r2


MODEL_IMPORT_TPL = "datadog_api_client.{version}.model.{name}"
PRIMITIVE_TYPES = ["string", "number", "boolean", "integer"]

EDGE_CASES = {}
replacement_file = pathlib.Path(__file__).parent / "replacement.json"
if replacement_file.exists():
    with replacement_file.open() as f:
        EDGE_CASES.update(json.load(f))

API_VERSION = None
WHITELISTED_LIST_MODELS = {
    "v1": (
        "AgentCheck",
        "AzureAccountListResponse",
        "DashboardBulkActionDataList",
        "DistributionPoint",
        "GCPAccountListResponse",
        "HTTPLog",
        "LogsPipelineList",
        "MonitorSearchCount",
        "Point",
        "ServiceChecks",
        "SharedDashboardInvitesDataList",
        "SlackIntegrationChannels",
        "SyntheticsRestrictedRoles",
        "UsageAttributionAggregates",
    ),
    "v2": (
        "CIAppAggregateBucketValueTimeseries",
        "EventsQueryGroupBys",
        "GroupTags",
        "HTTPLog",
        "IncidentTodoAssigneeArray",
        "LogsAggregateBucketValueTimeseries",
        "MetricBulkTagConfigEmailList",
        "MetricBulkTagConfigTagNameList",
        "MetricCustomAggregations",
        "MetricSuggestedAggregations",
        "RUMAggregateBucketValueTimeseries",
        "ScalarFormulaRequestQueries",
        "SecurityMonitoringSignalIncidentIds",
        "SensitiveDataScannerGetConfigIncludedArray",
        "SensitiveDataScannerStandardPatternsResponse",
        "TagsEventAttribute",
        "TeamPermissionSettingValues",
        "TimeseriesFormulaRequestQueries",
        "TimeseriesResponseSeriesList",
        "TimeseriesResponseTimes",
        "TimeseriesResponseValues",
        "TimeseriesResponseValuesList",
    ),
}

KEYWORDS = set(keyword.kwlist)
KEYWORDS.add("property")
KEYWORDS.add("cls")

PATTERN_DOUBLE_UNDERSCORE = re.compile(r"__+")
PATTERN_LEADING_ALPHA = re.compile(r"(.)([A-Z][a-z]+)")
PATTERN_FOLLOWING_ALPHA = re.compile(r"([a-z0-9])([A-Z])")
PATTERN_WHITESPACE = re.compile(r"\W")


def set_api_version(version):
    global API_VERSION
    API_VERSION = version


def is_list_model_whitelisted(name):
    return name in WHITELISTED_LIST_MODELS[API_VERSION]


def snake_case(value):
    s1 = PATTERN_LEADING_ALPHA.sub(r"\1_\2", value)
    s1 = PATTERN_FOLLOWING_ALPHA.sub(r"\1_\2", s1).lower()
    s1 = PATTERN_WHITESPACE.sub("_", s1)
    s1 = s1.rstrip("_")
    return PATTERN_DOUBLE_UNDERSCORE.sub("_", s1)


def class_name(value):
    """
    Convert a string into a valid Python API class name by:
    1. Removing all non-alphanumeric characters 
    2. Appending 'Api' suffix

    Args:
        value (str): The input string to convert

    Returns:
        str: A valid Python class name ending in 'Api'

    Example:
        >>> class_name("On-Call")
        'OnCallApi'
    """
    value = re.sub(r'[^a-zA-Z0-9]', '', value)
    return value + "Api"


def safe_snake_case(value):
    for token, replacement in EDGE_CASES.items():
        value = value.replace(token, replacement)
    return snake_case(value)


def camel_case(value):
    return "".join(x.title() for x in snake_case(value).split("_"))


def escape_reserved_keyword(word):
    """
    Escape reserved language keywords like openapi generator does it
    :param word: Word to escape
    :return: The escaped word if it was a reserved keyword, the word unchanged otherwise
    """
    if word in KEYWORDS:
        return f"_{word}"
    return word


def attribute_name(attribute):
    return escape_reserved_keyword(snake_case(attribute))


def format_value(value, quotes='"'):
    if isinstance(value, str):
        return f"{quotes}{value}{quotes}"
    elif isinstance(value, bool):
        return "true" if value else "false"
    return value


def get_name(schema):
    if hasattr(schema, "__reference__"):
        return schema.__reference__["$ref"].split("/")[-1]


def attribute_path(attribute):
    return ".".join(attribute_name(a) for a in attribute.split("."))


class CustomRenderer(m2r2.RestRenderer):
    def double_emphasis(self, text):
        if "``" in text:
            text = text.replace("\\ ``", "").replace("``\\ ", "")
        if "`_" in text:
            return text
        return "\\ **{}**\\ ".format(text)

    def header(self, text, level, raw=None):
        return "\n{}\n".format(self.double_emphasis(text))


def docstring(text):
    return (
        m2r2.convert(text.replace("\\n", "\\\\n"), renderer=CustomRenderer())[1:-1]
        .replace("\\ ", " ")
        .replace("\\`", "\\\\`")
        .replace("\n\n\n", "\n\n")
    )


def _merge_imports(a, b):
    """Merge second set of imports into first one."""
    for k, v in b.items():
        a[k] |= v
    return a


def format_parameters(kwargs, spec, version, replace_values=None):
    parameters = ""
    imports = defaultdict(set)

    parameters_spec = {p["name"]: p for p in spec.get("parameters", [])}
    if "requestBody" in spec and "multipart/form-data" in spec["requestBody"]["content"]:
        parent = spec["requestBody"]["content"]["multipart/form-data"]["schema"]
        for name, schema in parent["properties"].items():
            parameters_spec[name] = {
                "in": "form",
                "schema": schema,
                "name": name,
                "description": schema.get("description"),
                "required": name in parent.get("required", []),
            }

    parameters = ""
    for p in parameters_spec.values():
        k = p["name"]
        if k not in kwargs:
            continue

        v = kwargs[k]
        value, extra_imports = format_data_with_schema(
            v["value"],
            p["schema"],
            replace_values=replace_values,
            version=version,
        )
        imports = _merge_imports(imports, extra_imports)
        parameters += f"{escape_reserved_keyword(safe_snake_case(k))}={value}, "

    return parameters, imports


def get_name_and_imports(schema, version=None, imports=None):
    assert version is not None
    imports = imports or defaultdict(set)

    name = None
    if hasattr(schema, "__reference__"):
        name = schema.__reference__["$ref"].split("/")[-1]
        if "oneOf" not in schema:
            # do not include parent of oneOf schema
            imports[MODEL_IMPORT_TPL.format(version=version, name=safe_snake_case(name))].add(name)

    return name, imports


def _format_oneof(data, schema, replace_values, version, imports):
    matched = 0
    for sub_schema in schema["oneOf"]:
        try:
            if "items" in sub_schema and not isinstance(data, list):
                continue
            formatted, extra_imports = format_data_with_schema(
                data,
                sub_schema,
                replace_values=replace_values,
                version=version,
            )
            if sub_schema.get("items", {}).get("type") in PRIMITIVE_TYPES:
                return data, imports
            if matched == 0:
                imports = _merge_imports(imports, extra_imports)
                # NOTE we do not support mixed schemas with oneOf
                # parameters += formatted
                parameters = formatted
            matched += 1
        except (KeyError, ValueError) as e:
            print(f"{e}")

    if matched != 1:
        raise ValueError(f"[{matched}] {data} is not valid for schema {schema}")

    return parameters, imports


@singledispatch
def format_data_with_schema(
    data,
    schema,
    replace_values=None,
    default_name=None,
    version=None,
    imports=None,
):
    """Format data with schema."""
    assert version is not None

    name = None
    imports = imports or defaultdict(set)
    nullable = schema.get("nullable", False)

    if schema.get("type") not in {"string", "integer", "boolean"} or schema.get("enum"):
        name, imports = get_name_and_imports(schema, version, imports)
    if schema.get("oneOf"):
        name = None
    if name:
        imports[MODEL_IMPORT_TPL.format(version=version, name=safe_snake_case(name))].add(name)

    if "enum" in schema:
        if nullable and data is None:
            pass
        elif data not in schema["enum"]:
            raise ValueError(f"{data} is not valid enum value {schema['enum']}")

    if replace_values and data in replace_values:
        parameters = replace_values[data]
        if schema.get("format") in ("int32", "int64"):
            parameters = f"int({parameters})"
    elif "enum" in schema:
        if nullable and data is None:
            parameters = repr(data)
            return parameters, imports
        else:
            parameters = schema["x-enum-varnames"][schema["enum"].index(data)]
            return f"{name}.{parameters}", imports
    else:
        if nullable and data is None:
            parameters = repr(data)
            return parameters, imports
        else:

            def format_datetime(x):
                imports["datetime"].add("datetime")
                d = dateutil.parser.isoparse(x)
                result = repr(d)
                if result.startswith("datetime."):
                    result = result[len("datetime.") :]
                if "tzutc" in result:
                    imports["dateutil.tz"].add("tzutc")
                if "tzoffset" in result:
                    imports["dateutil.tz"].add("tzoffset")
                return result
            
            def format_uuid(x):
                imports["uuid"].add("UUID")
                result = repr(UUID(x))
                return result

            formatters = {
                "double": lambda s: repr(float(s)),
                "int32": lambda s: repr(int(s)),
                "int64": lambda s: repr(int(s)),
                "date": format_datetime,
                "date-time": format_datetime,
                "binary": lambda s: f'open("{s}", "rb")',
                "email": repr,
                "uuid": format_uuid,
                None: repr, 
            }
            schema_type = schema.get("type")
            formatter = formatters.get(schema.get("format", schema_type), formatters.get(schema_type)) or repr

            # TODO format date and datetime
            parameters = formatter(data)

    if name:
        return f"{name}({parameters})", imports

    return parameters, imports


@format_data_with_schema.register(list)
def format_data_with_schema_list(
    data,
    schema,
    replace_values=None,
    default_name=None,
    version=None,
    imports=None,
):
    """Format data with schema."""
    assert version is not None
    if not isinstance(schema, dict):
        raise ValueError(f"Schema mismatch for list data: {schema}")

    imports = imports or defaultdict(set)
    name, r_imports = get_name_and_imports(schema, version, None)
    if is_list_model_whitelisted(name):
        imports.update(r_imports)

    if "oneOf" in schema:
        return _format_oneof(data, schema, replace_values, version, imports)

    if schema == True or schema == {}:
        sub_schema = {}
    else:
        sub_schema = schema["items"]

    parameters = ""
    for d in data:
        value, extra_imports = format_data_with_schema(
            d,
            sub_schema,
            replace_values=replace_values,
            version=version,
        )
        parameters += f"{value}, "
        imports = _merge_imports(imports, extra_imports)
    parameters = f"[{parameters}]"

    if name and is_list_model_whitelisted(name):
        return f"{name}({parameters})", imports

    return parameters, imports


@format_data_with_schema.register(dict)
def format_data_with_schema_dict(
    data,
    schema,
    replace_values=None,
    default_name=None,
    version=None,
    imports=None,
):
    """Format data with schema."""
    assert version is not None
    name, imports = get_name_and_imports(schema, version, imports)

    parameters = ""
    if "properties" in schema:
        required_properties = set(schema.get("required", []))
        missing = required_properties - set(data.keys())
        if missing:
            raise ValueError(f"missing required properties: {missing}")
        additional_properties = set(data.keys()) - set(schema["properties"].keys())
        if schema.get("additionalProperties") == False and additional_properties:
            raise ValueError(f"additional properties not allowed: {additional_properties}")

        for k, v in data.items():
            if k in schema["properties"]:
                sub_schema = schema["properties"][k]
            else:
                sub_schema = schema["additionalProperties"]
            value, extra_imports = format_data_with_schema(
                v,
                sub_schema,
                replace_values=replace_values,
                default_name=name + camel_case(k) if name else None,
                version=version,
            )
            parameters += f"{escape_reserved_keyword(safe_snake_case(k))}={value}, "
            imports = _merge_imports(imports, extra_imports)

    if schema.get("additionalProperties") and not schema.get("properties"):
        for k, v in data.items():
            value, extra_imports = format_data_with_schema(
                v,
                schema["additionalProperties"],
                replace_values=replace_values,
                version=version,
            )
            parameters += f"{escape_reserved_keyword(k)}={value}, "
            imports = _merge_imports(imports, extra_imports)

    if "oneOf" in schema:
        return _format_oneof(data, schema, replace_values, version, imports)

    if not name:
        if default_name and not schema.get("additionalProperties") and schema.get("properties"):
            name = default_name
            imports[MODEL_IMPORT_TPL.format(version=version, name=safe_snake_case(name))].add(name)
        else:
            name = "dict"
            warnings.warn(f"Unnamed schema {schema} for {data}")

    if parameters == "" and schema.get("type") == "string":
        raise ValueError(f"No schema matched for {data}")

    if not parameters and data:
        key_val_pairs = ", ".join(f'("{k}", "{v}")' for k, v in data.items())
        parameters = f"[{key_val_pairs}]"

    if name:
        return f"{name}({parameters})", imports

    return parameters, imports
