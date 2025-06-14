# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictFloat, StrictInt, StrictStr, ValidationError, field_validator
from typing import Optional, Tuple, Union
from wandelbots_api_client.models.array_input import ArrayInput
from wandelbots_api_client.models.capture import Capture
from wandelbots_api_client.models.point_cloud import PointCloud
from wandelbots_api_client.models.pyjectory_datatypes_serializer_orientation import PyjectoryDatatypesSerializerOrientation
from wandelbots_api_client.models.pyjectory_datatypes_serializer_pose import PyjectoryDatatypesSerializerPose
from wandelbots_api_client.models.pyjectory_datatypes_serializer_position import PyjectoryDatatypesSerializerPosition
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

VALUE_ANY_OF_SCHEMAS = ["ArrayInput", "Capture", "PointCloud", "PyjectoryDatatypesSerializerOrientation", "PyjectoryDatatypesSerializerPose", "PyjectoryDatatypesSerializerPosition", "bytearray", "float", "int", "str"]

class Value(BaseModel):
    """
    Value
    """

    # data type: float
    anyof_schema_1_validator: Optional[Union[StrictFloat, StrictInt]] = None
    # data type: int
    anyof_schema_2_validator: Optional[StrictInt] = None
    # data type: str
    anyof_schema_3_validator: Optional[StrictStr] = None
    # data type: bytearray
    anyof_schema_4_validator: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]] = None
    # data type: PyjectoryDatatypesSerializerPose
    anyof_schema_5_validator: Optional[PyjectoryDatatypesSerializerPose] = None
    # data type: PyjectoryDatatypesSerializerPosition
    anyof_schema_6_validator: Optional[PyjectoryDatatypesSerializerPosition] = None
    # data type: PyjectoryDatatypesSerializerOrientation
    anyof_schema_7_validator: Optional[PyjectoryDatatypesSerializerOrientation] = None
    # data type: Capture
    anyof_schema_8_validator: Optional[Capture] = None
    # data type: PointCloud
    anyof_schema_9_validator: Optional[PointCloud] = None
    # data type: ArrayInput
    anyof_schema_10_validator: Optional[ArrayInput] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ArrayInput, Capture, PointCloud, PyjectoryDatatypesSerializerOrientation, PyjectoryDatatypesSerializerPose, PyjectoryDatatypesSerializerPosition, bytearray, float, int, str]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "ArrayInput", "Capture", "PointCloud", "PyjectoryDatatypesSerializerOrientation", "PyjectoryDatatypesSerializerPose", "PyjectoryDatatypesSerializerPosition", "bytearray", "float", "int", "str" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = Value.model_construct()
        error_messages = []
        # validate data type: float
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: int
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: str
        try:
            instance.anyof_schema_3_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: bytearray
        try:
            instance.anyof_schema_4_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: PyjectoryDatatypesSerializerPose
        if not isinstance(v, PyjectoryDatatypesSerializerPose):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyjectoryDatatypesSerializerPose`")
        else:
            return v

        # validate data type: PyjectoryDatatypesSerializerPosition
        if not isinstance(v, PyjectoryDatatypesSerializerPosition):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyjectoryDatatypesSerializerPosition`")
        else:
            return v

        # validate data type: PyjectoryDatatypesSerializerOrientation
        if not isinstance(v, PyjectoryDatatypesSerializerOrientation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyjectoryDatatypesSerializerOrientation`")
        else:
            return v

        # validate data type: Capture
        if not isinstance(v, Capture):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Capture`")
        else:
            return v

        # validate data type: PointCloud
        if not isinstance(v, PointCloud):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PointCloud`")
        else:
            return v

        # validate data type: ArrayInput
        if not isinstance(v, ArrayInput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArrayInput`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Value with anyOf schemas: ArrayInput, Capture, PointCloud, PyjectoryDatatypesSerializerOrientation, PyjectoryDatatypesSerializerPose, PyjectoryDatatypesSerializerPosition, bytearray, float, int, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # deserialize data into float
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into int
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_3_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into bytearray
        try:
            # validation
            instance.anyof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_4_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[PyjectoryDatatypesSerializerPose] = None
        try:
            instance.actual_instance = PyjectoryDatatypesSerializerPose.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[PyjectoryDatatypesSerializerPosition] = None
        try:
            instance.actual_instance = PyjectoryDatatypesSerializerPosition.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[PyjectoryDatatypesSerializerOrientation] = None
        try:
            instance.actual_instance = PyjectoryDatatypesSerializerOrientation.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[Capture] = None
        try:
            instance.actual_instance = Capture.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[PointCloud] = None
        try:
            instance.actual_instance = PointCloud.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_10_validator: Optional[ArrayInput] = None
        try:
            instance.actual_instance = ArrayInput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Value with anyOf schemas: ArrayInput, Capture, PointCloud, PyjectoryDatatypesSerializerOrientation, PyjectoryDatatypesSerializerPose, PyjectoryDatatypesSerializerPosition, bytearray, float, int, str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ArrayInput, Capture, PointCloud, PyjectoryDatatypesSerializerOrientation, PyjectoryDatatypesSerializerPose, PyjectoryDatatypesSerializerPosition, bytearray, float, int, str]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


