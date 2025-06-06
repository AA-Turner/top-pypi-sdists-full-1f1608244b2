# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

import json
from dataclasses import is_dataclass
from decimal import Decimal
from enum import Enum
from collections.abc import Iterable
from typing import Any, ClassVar, Optional, Type, TypeVar, Union, cast

import yaml
from pydantic import BaseModel
from pydantic import ValidationError as PydanticValidationError
from pydantic_core import ErrorDetails, InitErrorDetails

from ._errors import DecodeValidationError
from ._types import EnvironmentTemplate, JobTemplate, OpenJDModel, TemplateSpecificationVersion
from ._convert_pydantic_error import pydantic_validationerrors_to_str
from .v2023_09 import JobTemplate as JobTemplate_2023_09
from .v2023_09 import EnvironmentTemplate as EnvironmentTemplate_2023_09

__all__ = (
    "parse_model",
    "document_string_to_object",
    "DocumentType",
    "decode_template",
    "decode_job_template",
    "decode_environment_template",
)


class DocumentType(str, Enum):
    JSON = "JSON"
    YAML = "YAML"


# Pydantic injects a __pydantic_model__ attribute into all dataclasses. To be able to parse
# dataclass models we need to be able to invoke Model.__pydantic_model__.model_validate(), but
# type checkers do not realize that pydantic dataclasses have a __pydantic_model__ attribute.
# So, we type-cast into this class to invoke that method.
class PydanticDataclass:
    # See: https://github.com/pydantic/pydantic/blob/b0215d175ace2a3db76307c5f18819b021f48ab5/pydantic/dataclasses.py#L68
    __pydantic_model__: ClassVar[Type[BaseModel]]


T = TypeVar("T", bound=OpenJDModel)


def _parse_model(*, model: Type[T], obj: Any, context: Any = None) -> T:
    if context is None:
        context = model.model_parsing_context_type()
    if is_dataclass(model):
        return cast(
            T,
            cast(PydanticDataclass, model).__pydantic_model__.model_validate(obj, context=context),
        )
    else:
        prevalidator_error: Optional[PydanticValidationError] = None
        if hasattr(model, "_root_template_prevalidator"):
            try:
                getattr(model, "_root_template_prevalidator")(obj, context=context)
            except PydanticValidationError as exc:
                prevalidator_error = exc
        try:
            result = model.model_validate(obj, context=context)  # type: ignore
        except PydanticValidationError as exc:
            if prevalidator_error is not None:
                errors = list[InitErrorDetails]()
                for error_details in exc.errors() + prevalidator_error.errors():
                    init_error_details = {
                        key: value for key, value in error_details.items() if key != "msg"
                    }
                    errors.append(cast(InitErrorDetails, init_error_details))
                raise PydanticValidationError.from_exception_data(
                    title=exc.title, line_errors=errors
                )
            else:
                raise
        if prevalidator_error is not None:
            raise prevalidator_error
        return result


def parse_model(
    *, model: Type[T], obj: Any, supported_extensions: Optional[Iterable[str]] = None
) -> T:
    try:
        return _parse_model(
            model=model,
            obj=obj,
            context=model.model_parsing_context_type(supported_extensions=supported_extensions),
        )
    except PydanticValidationError as exc:
        errors: list[ErrorDetails] = exc.errors()
        raise DecodeValidationError(pydantic_validationerrors_to_str(model, errors))


def document_string_to_object(*, document: str, document_type: DocumentType) -> dict[str, Any]:
    """
    Converts the YAML or JSON encoded document into a python dictionary.

    Arguments:
        document (str): A string containing a JSON or YAML encoded document.

    Returns:
        dict[str, Any]: The decoded document.

    Raises:
        DecodeValidationError
    """
    try:
        if document_type == DocumentType.JSON:
            parsed_document = json.loads(document)
        else:  # YAML
            parsed_document = yaml.safe_load(document)
        if not isinstance(parsed_document, dict):
            raise ValueError()
        return parsed_document
    except (ValueError, json.decoder.JSONDecodeError, yaml.YAMLError):
        raise DecodeValidationError(
            f"The document is not a valid {document_type.value} document consisting of key-value pairs."
        )


def model_to_object(*, model: OpenJDModel) -> dict[str, Any]:
    """Given a model from this package, encode it as a dictionary such that it could
    be written to a JSON/YAML document."""

    as_dict = model.model_dump()

    # Some of the values in the model can be type 'Decimal', which doesn't
    # encode into json/yaml without special handling. So, we convert those in to
    # strings.
    def decimal_to_str(data: Union[dict[str, Any], list[Any]]) -> None:
        if isinstance(data, list):
            for i, item in enumerate(data):
                if isinstance(item, Decimal):
                    data[i] = str(item)
                elif isinstance(item, (dict, list)):
                    decimal_to_str(item)
        else:
            delete_keys: list[str] = []
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = str(v)
                elif isinstance(v, (dict, list)):
                    decimal_to_str(v)
                elif v is None:
                    delete_keys.append(k)
            for k in delete_keys:
                del data[k]

    decimal_to_str(as_dict)
    return as_dict


def decode_job_template(
    *, template: dict[str, Any], supported_extensions: Optional[Iterable[str]] = None
) -> JobTemplate:
    """Given a dictionary containing a Job Template, this will decode the template, run validation checks on it,
    and then return the decoded template.

    This function places no restriction on the version of the specification. The caller
    can inspect the `specificationVersion` property of the returned object to validate this.

    By default, no extensions are supported. The caller can opt in to specific extensions,
    by providing them as a list.

    Args:
        template (dict[str, Any]): A Job Template as a dictionary object.
        supported_extensions (Optional[Iterable[str]]): A list of extension names to support. This list is intersected
            with the extensions names supported by the implementation before processing.

    Returns:
        JobTemplate: The decoded job template.

    Raises:
        DecodeValidationError
        NotImplementedError
    """
    try:
        # Raises: KeyError
        document_version = template["specificationVersion"]
        # Raises: ValueError
        schema_version = TemplateSpecificationVersion(document_version)
    except KeyError:
        # Unable to get 'specificationVersion' key from the document
        raise DecodeValidationError(
            "Template is missing Open Job Description schema version key: specificationVersion"
        )
    except ValueError:
        # Value of the schema version is not one we know.
        values_allowed = ", ".join(
            str(s.value) for s in TemplateSpecificationVersion.job_template_versions()
        )
        raise DecodeValidationError(
            (
                f"Unknown template version: {document_version}. "
                f"Values allowed for 'specificationVersion' in Job Templates are: {values_allowed}"
            )
        )

    if not TemplateSpecificationVersion.is_job_template(schema_version):
        values_allowed = ", ".join(
            str(s.value) for s in TemplateSpecificationVersion.job_template_versions()
        )
        raise DecodeValidationError(
            (
                f"Specification version '{document_version}' is not a Job Template version. "
                f"Values allowed for 'specificationVersion' in Job Templates are: {values_allowed}"
            )
        )

    if schema_version == TemplateSpecificationVersion.JOBTEMPLATE_v2023_09:
        return parse_model(
            model=JobTemplate_2023_09, obj=template, supported_extensions=supported_extensions
        )
    else:
        raise NotImplementedError(
            f"Template decode for schema {schema_version.value} is not yet implemented."
        )


def decode_template(*, template: dict[str, Any]) -> JobTemplate:
    """THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use
    decode_job_template() instead.
    """
    return decode_job_template(template=template)


def decode_environment_template(
    *, template: dict[str, Any], supported_extensions: Optional[Iterable[str]] = None
) -> EnvironmentTemplate:
    """Given a dictionary containing an Environment Template, this will decode the template, run validation checks on it,
    and then return the decoded template.

    This function places no restriction on the version of the specification. The caller
    can inspect the `specificationVersion` property of the returned object to validate this.

    By default, no extensions are supported. The caller can opt in to specific extensions,
    by providing them as a list.

    Args:
        template (dict[str, Any]): An Environment Template as a dictionary object.
        supported_extensions (Optional[Iterable[str]]): A list of extension names to support. This list is intersected
            with the extensions names supported by the implementation before processing.

    Returns:
        EnvironmentTemplate: The decoded environment template.

    Raises:
        DecodeValidationError
        NotImplementedError
    """
    try:
        # Raises: KeyError
        document_version = template["specificationVersion"]
        # Raises: ValueError
        schema_version = TemplateSpecificationVersion(document_version)
    except KeyError:
        # Unable to get 'specificationVersion' key from the document
        raise DecodeValidationError(
            "Template is missing Open Job Description schema version key: specificationVersion"
        )
    except ValueError:
        # Value of the schema version is not one we know.
        values_allowed = ", ".join(
            str(s.value) for s in TemplateSpecificationVersion.environment_template_versions()
        )
        raise DecodeValidationError(
            f"Unknown template version: {document_version}. Allowed values are: {values_allowed}"
        )

    if not TemplateSpecificationVersion.is_environment_template(schema_version):
        values_allowed = ", ".join(
            str(s.value) for s in TemplateSpecificationVersion.environment_template_versions()
        )
        raise DecodeValidationError(
            f"Specification version '{document_version}' is not an Environment Template version. "
            f"Allowed values for 'specificationVersion' are: {values_allowed}"
        )

    if schema_version == TemplateSpecificationVersion.ENVIRONMENT_v2023_09:
        return parse_model(
            model=EnvironmentTemplate_2023_09,
            obj=template,
            supported_extensions=supported_extensions,
        )
    else:
        raise NotImplementedError(
            f"Template decode for schema {schema_version.value} is not yet implemented."
        )
