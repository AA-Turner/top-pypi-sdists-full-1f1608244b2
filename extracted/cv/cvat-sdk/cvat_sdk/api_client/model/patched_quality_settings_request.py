# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

# CVAT REST API
#
# REST API for Computer Vision Annotation Tool (CVAT)  # noqa: E501
#
# The version of the OpenAPI document: 2.39.0
# Contact: support@cvat.ai
# Generated by: https://openapi-generator.tech


from __future__ import annotations

import typing

import re  # noqa: F401
import sys  # noqa: F401

from cvat_sdk.api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    IModelData,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from cvat_sdk.api_client.exceptions import ApiAttributeError

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # Enable introspection. Can't work normally due to cyclic imports
    from cvat_sdk.api_client.apis import *
    from cvat_sdk.api_client.models import *


def lazy_import():
    from cvat_sdk.api_client.model.quality_point_size_base import QualityPointSizeBase
    from cvat_sdk.api_client.model.quality_target_metric import QualityTargetMetric
    globals()['QualityPointSizeBase'] = QualityPointSizeBase
    globals()['QualityTargetMetric'] = QualityTargetMetric



class IPatchedQualitySettingsRequest(IModelData):
    """
    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    # member type declarations
    job_filter: str # noqa: E501
    """
    [optional]
    A JSON-based logic expression used to filter jobs for quality validation. The filter supports various terms to specify conditions on job: ['assignee', 'id', 'stage', 'state', 'task_id', 'task_name', 'type'] .
    """

    inherit: bool # noqa: E501
    """
    [optional]
    Allow using project settings when computing task quality. Only applicable to task quality settings inside projects .
    """

    target_metric: typing.Union[typing.Any, none_type] # noqa: E501
    """
    [optional]
    The primary metric used for quality estimation  * `accuracy` - ACCURACY * `precision` - PRECISION * `recall` - RECALL.
    """

    target_metric_threshold: float # noqa: E501
    """
    [optional]
    Defines the minimal quality requirements in terms of the selected target metric. .
    """

    max_validations_per_job: int # noqa: E501
    """
    [optional]
    The maximum number of job validation attempts for the job assignee. The job can be automatically accepted if the job quality is above the required threshold, defined by the target threshold parameter. .
    """

    iou_threshold: float # noqa: E501
    """
    [optional, default: 0.4]
    Used for distinction between matched / unmatched shapes.
    """

    oks_sigma: float # noqa: E501
    """
    [optional, default: 0.09]
    Like IoU threshold, but for points. The percent of the bbox side, used as the radius of the circle around the GT point, where the checked point is expected to be. For boxes with different width and height, the \"side\" is computed as a geometric mean of the width and height. Read more: https://cocodataset.org/#keypoints-eval .
    """

    point_size_base: typing.Union[typing.Any, none_type] # noqa: E501
    """
    [optional]
    When comparing point annotations (including both separate points and point groups), the OKS sigma parameter defines matching area for each GT point based to the object size. The point size base parameter allows to configure how to determine the object size. If image_size, the image size is used. Useful if each point annotation represents a separate object or boxes grouped with points do not represent object boundaries. If group_bbox_size, the object size is based on the point group bbox size. Useful if each point group represents an object or there is a bbox grouped with points, representing the object size.   * `image_size` - IMAGE_SIZE * `group_bbox_size` - GROUP_BBOX_SIZE.
    """

    line_thickness: float # noqa: E501
    """
    [optional, default: 0.01]
    Thickness of polylines, relatively to the (image area) ^ 0.5. The distance to the boundary around the GT line, inside of which the checked line points should be .
    """

    low_overlap_threshold: float # noqa: E501
    """
    [optional, default: 0.8]
    Used for distinction between strong / weak (low_overlap) matches .
    """

    compare_line_orientation: bool # noqa: E501
    """
    [optional, default: True]
    Enables or disables polyline orientation comparison.
    """

    line_orientation_threshold: float # noqa: E501
    """
    [optional, default: 0.1]
    The minimal gain in the GT IoU between the given and reversed line directions to consider the line inverted. Only used when the 'compare_line_orientation' parameter is true .
    """

    compare_groups: bool # noqa: E501
    """
    [optional, default: True]
    Enables or disables annotation group checks.
    """

    group_match_threshold: float # noqa: E501
    """
    [optional, default: 0.5]
    Minimal IoU for groups to be considered matching. Only used when the 'compare_groups' parameter is true .
    """

    check_covered_annotations: bool # noqa: E501
    """
    [optional, default: True]
    Check for partially-covered annotations, useful in segmentation tasks .
    """

    object_visibility_threshold: float # noqa: E501
    """
    [optional, default: 0.05]
    Minimal visible area percent of the spatial annotations (polygons, masks) for reporting covered annotations. Only used when the 'object_visibility_threshold' parameter is true .
    """

    panoptic_comparison: bool # noqa: E501
    """
    [optional, default: True]
    Use only the visible part of the masks and polygons in comparisons .
    """

    compare_attributes: bool # noqa: E501
    """
    [optional, default: True]
    Enables or disables annotation attribute comparison.
    """

    empty_is_annotated: bool # noqa: E501
    """
    [optional, default: False]
    Consider empty frames annotated as \"empty\". This affects target metrics like accuracy in cases there are no annotations. If disabled, frames without annotations are counted as not matching (accuracy is 0). If enabled, accuracy will be 1 instead. This will also add virtual annotations to empty frames in the comparison results. .
    """


class PatchedQualitySettingsRequest(ModelNormal, IPatchedQualitySettingsRequest):
    """
    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      job_filter (str): A JSON-based logic expression used to filter jobs for quality validation. The filter supports various terms to specify conditions on job: ['assignee', 'id', 'stage', 'state', 'task_id', 'task_name', 'type'] . [optional]  # noqa: E501

      inherit (bool): Allow using project settings when computing task quality. Only applicable to task quality settings inside projects . [optional]  # noqa: E501

      target_metric (bool, date, datetime, dict, float, int, list, str, none_type): The primary metric used for quality estimation  * `accuracy` - ACCURACY * `precision` - PRECISION * `recall` - RECALL. [optional]  # noqa: E501

      target_metric_threshold (float): Defines the minimal quality requirements in terms of the selected target metric. . [optional]  # noqa: E501

      max_validations_per_job (int): The maximum number of job validation attempts for the job assignee. The job can be automatically accepted if the job quality is above the required threshold, defined by the target threshold parameter. . [optional]  # noqa: E501

      iou_threshold (float): Used for distinction between matched / unmatched shapes. [optional] if omitted the server will use the default value of 0.4  # noqa: E501

      oks_sigma (float): Like IoU threshold, but for points. The percent of the bbox side, used as the radius of the circle around the GT point, where the checked point is expected to be. For boxes with different width and height, the \"side\" is computed as a geometric mean of the width and height. Read more: https://cocodataset.org/#keypoints-eval . [optional] if omitted the server will use the default value of 0.09  # noqa: E501

      point_size_base (bool, date, datetime, dict, float, int, list, str, none_type): When comparing point annotations (including both separate points and point groups), the OKS sigma parameter defines matching area for each GT point based to the object size. The point size base parameter allows to configure how to determine the object size. If image_size, the image size is used. Useful if each point annotation represents a separate object or boxes grouped with points do not represent object boundaries. If group_bbox_size, the object size is based on the point group bbox size. Useful if each point group represents an object or there is a bbox grouped with points, representing the object size.   * `image_size` - IMAGE_SIZE * `group_bbox_size` - GROUP_BBOX_SIZE. [optional]  # noqa: E501

      line_thickness (float): Thickness of polylines, relatively to the (image area) ^ 0.5. The distance to the boundary around the GT line, inside of which the checked line points should be . [optional] if omitted the server will use the default value of 0.01  # noqa: E501

      low_overlap_threshold (float): Used for distinction between strong / weak (low_overlap) matches . [optional] if omitted the server will use the default value of 0.8  # noqa: E501

      compare_line_orientation (bool): Enables or disables polyline orientation comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

      line_orientation_threshold (float): The minimal gain in the GT IoU between the given and reversed line directions to consider the line inverted. Only used when the 'compare_line_orientation' parameter is true . [optional] if omitted the server will use the default value of 0.1  # noqa: E501

      compare_groups (bool): Enables or disables annotation group checks. [optional] if omitted the server will use the default value of True  # noqa: E501

      group_match_threshold (float): Minimal IoU for groups to be considered matching. Only used when the 'compare_groups' parameter is true . [optional] if omitted the server will use the default value of 0.5  # noqa: E501

      check_covered_annotations (bool): Check for partially-covered annotations, useful in segmentation tasks . [optional] if omitted the server will use the default value of True  # noqa: E501

      object_visibility_threshold (float): Minimal visible area percent of the spatial annotations (polygons, masks) for reporting covered annotations. Only used when the 'object_visibility_threshold' parameter is true . [optional] if omitted the server will use the default value of 0.05  # noqa: E501

      panoptic_comparison (bool): Use only the visible part of the masks and polygons in comparisons . [optional] if omitted the server will use the default value of True  # noqa: E501

      compare_attributes (bool): Enables or disables annotation attribute comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

      empty_is_annotated (bool): Consider empty frames annotated as \"empty\". This affects target metrics like accuracy in cases there are no annotations. If disabled, frames without annotations are counted as not matching (accuracy is 0). If enabled, accuracy will be 1 instead. This will also add virtual annotations to empty frames in the comparison results. . [optional] if omitted the server will use the default value of False  # noqa: E501


      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {
    }

    validations = {
        ('job_filter',): {
            'max_length': 1024,
        },
        ('target_metric_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('max_validations_per_job',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('iou_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('oks_sigma',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('line_thickness',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('low_overlap_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('line_orientation_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('group_match_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('object_visibility_threshold',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'job_filter': (str,),  # noqa: E501
            'inherit': (bool,),  # noqa: E501
            'target_metric': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'target_metric_threshold': (float,),  # noqa: E501
            'max_validations_per_job': (int,),  # noqa: E501
            'iou_threshold': (float,),  # noqa: E501
            'oks_sigma': (float,),  # noqa: E501
            'point_size_base': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'line_thickness': (float,),  # noqa: E501
            'low_overlap_threshold': (float,),  # noqa: E501
            'compare_line_orientation': (bool,),  # noqa: E501
            'line_orientation_threshold': (float,),  # noqa: E501
            'compare_groups': (bool,),  # noqa: E501
            'group_match_threshold': (float,),  # noqa: E501
            'check_covered_annotations': (bool,),  # noqa: E501
            'object_visibility_threshold': (float,),  # noqa: E501
            'panoptic_comparison': (bool,),  # noqa: E501
            'compare_attributes': (bool,),  # noqa: E501
            'empty_is_annotated': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'job_filter': 'job_filter',  # noqa: E501
        'inherit': 'inherit',  # noqa: E501
        'target_metric': 'target_metric',  # noqa: E501
        'target_metric_threshold': 'target_metric_threshold',  # noqa: E501
        'max_validations_per_job': 'max_validations_per_job',  # noqa: E501
        'iou_threshold': 'iou_threshold',  # noqa: E501
        'oks_sigma': 'oks_sigma',  # noqa: E501
        'point_size_base': 'point_size_base',  # noqa: E501
        'line_thickness': 'line_thickness',  # noqa: E501
        'low_overlap_threshold': 'low_overlap_threshold',  # noqa: E501
        'compare_line_orientation': 'compare_line_orientation',  # noqa: E501
        'line_orientation_threshold': 'line_orientation_threshold',  # noqa: E501
        'compare_groups': 'compare_groups',  # noqa: E501
        'group_match_threshold': 'group_match_threshold',  # noqa: E501
        'check_covered_annotations': 'check_covered_annotations',  # noqa: E501
        'object_visibility_threshold': 'object_visibility_threshold',  # noqa: E501
        'panoptic_comparison': 'panoptic_comparison',  # noqa: E501
        'compare_attributes': 'compare_attributes',  # noqa: E501
        'empty_is_annotated': 'empty_is_annotated',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PatchedQualitySettingsRequest - a model defined in OpenAPI

        Keyword Args:
            job_filter (str): A JSON-based logic expression used to filter jobs for quality validation. The filter supports various terms to specify conditions on job: ['assignee', 'id', 'stage', 'state', 'task_id', 'task_name', 'type'] . [optional]  # noqa: E501

            inherit (bool): Allow using project settings when computing task quality. Only applicable to task quality settings inside projects . [optional]  # noqa: E501

            target_metric (bool, date, datetime, dict, float, int, list, str, none_type): The primary metric used for quality estimation  * `accuracy` - ACCURACY * `precision` - PRECISION * `recall` - RECALL. [optional]  # noqa: E501

            target_metric_threshold (float): Defines the minimal quality requirements in terms of the selected target metric. . [optional]  # noqa: E501

            max_validations_per_job (int): The maximum number of job validation attempts for the job assignee. The job can be automatically accepted if the job quality is above the required threshold, defined by the target threshold parameter. . [optional]  # noqa: E501

            iou_threshold (float): Used for distinction between matched / unmatched shapes. [optional] if omitted the server will use the default value of 0.4  # noqa: E501

            oks_sigma (float): Like IoU threshold, but for points. The percent of the bbox side, used as the radius of the circle around the GT point, where the checked point is expected to be. For boxes with different width and height, the \"side\" is computed as a geometric mean of the width and height. Read more: https://cocodataset.org/#keypoints-eval . [optional] if omitted the server will use the default value of 0.09  # noqa: E501

            point_size_base (bool, date, datetime, dict, float, int, list, str, none_type): When comparing point annotations (including both separate points and point groups), the OKS sigma parameter defines matching area for each GT point based to the object size. The point size base parameter allows to configure how to determine the object size. If image_size, the image size is used. Useful if each point annotation represents a separate object or boxes grouped with points do not represent object boundaries. If group_bbox_size, the object size is based on the point group bbox size. Useful if each point group represents an object or there is a bbox grouped with points, representing the object size.   * `image_size` - IMAGE_SIZE * `group_bbox_size` - GROUP_BBOX_SIZE. [optional]  # noqa: E501

            line_thickness (float): Thickness of polylines, relatively to the (image area) ^ 0.5. The distance to the boundary around the GT line, inside of which the checked line points should be . [optional] if omitted the server will use the default value of 0.01  # noqa: E501

            low_overlap_threshold (float): Used for distinction between strong / weak (low_overlap) matches . [optional] if omitted the server will use the default value of 0.8  # noqa: E501

            compare_line_orientation (bool): Enables or disables polyline orientation comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

            line_orientation_threshold (float): The minimal gain in the GT IoU between the given and reversed line directions to consider the line inverted. Only used when the 'compare_line_orientation' parameter is true . [optional] if omitted the server will use the default value of 0.1  # noqa: E501

            compare_groups (bool): Enables or disables annotation group checks. [optional] if omitted the server will use the default value of True  # noqa: E501

            group_match_threshold (float): Minimal IoU for groups to be considered matching. Only used when the 'compare_groups' parameter is true . [optional] if omitted the server will use the default value of 0.5  # noqa: E501

            check_covered_annotations (bool): Check for partially-covered annotations, useful in segmentation tasks . [optional] if omitted the server will use the default value of True  # noqa: E501

            object_visibility_threshold (float): Minimal visible area percent of the spatial annotations (polygons, masks) for reporting covered annotations. Only used when the 'object_visibility_threshold' parameter is true . [optional] if omitted the server will use the default value of 0.05  # noqa: E501

            panoptic_comparison (bool): Use only the visible part of the masks and polygons in comparisons . [optional] if omitted the server will use the default value of True  # noqa: E501

            compare_attributes (bool): Enables or disables annotation attribute comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

            empty_is_annotated (bool): Consider empty frames annotated as \"empty\". This affects target metrics like accuracy in cases there are no annotations. If disabled, frames without annotations are counted as not matching (accuracy is 0). If enabled, accuracy will be 1 instead. This will also add virtual annotations to empty frames in the comparison results. . [optional] if omitted the server will use the default value of False  # noqa: E501

            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
"""

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PatchedQualitySettingsRequest - a model defined in OpenAPI

        Keyword Args:
            job_filter (str): A JSON-based logic expression used to filter jobs for quality validation. The filter supports various terms to specify conditions on job: ['assignee', 'id', 'stage', 'state', 'task_id', 'task_name', 'type'] . [optional]  # noqa: E501

            inherit (bool): Allow using project settings when computing task quality. Only applicable to task quality settings inside projects . [optional]  # noqa: E501

            target_metric (bool, date, datetime, dict, float, int, list, str, none_type): The primary metric used for quality estimation  * `accuracy` - ACCURACY * `precision` - PRECISION * `recall` - RECALL. [optional]  # noqa: E501

            target_metric_threshold (float): Defines the minimal quality requirements in terms of the selected target metric. . [optional]  # noqa: E501

            max_validations_per_job (int): The maximum number of job validation attempts for the job assignee. The job can be automatically accepted if the job quality is above the required threshold, defined by the target threshold parameter. . [optional]  # noqa: E501

            iou_threshold (float): Used for distinction between matched / unmatched shapes. [optional] if omitted the server will use the default value of 0.4  # noqa: E501

            oks_sigma (float): Like IoU threshold, but for points. The percent of the bbox side, used as the radius of the circle around the GT point, where the checked point is expected to be. For boxes with different width and height, the \"side\" is computed as a geometric mean of the width and height. Read more: https://cocodataset.org/#keypoints-eval . [optional] if omitted the server will use the default value of 0.09  # noqa: E501

            point_size_base (bool, date, datetime, dict, float, int, list, str, none_type): When comparing point annotations (including both separate points and point groups), the OKS sigma parameter defines matching area for each GT point based to the object size. The point size base parameter allows to configure how to determine the object size. If image_size, the image size is used. Useful if each point annotation represents a separate object or boxes grouped with points do not represent object boundaries. If group_bbox_size, the object size is based on the point group bbox size. Useful if each point group represents an object or there is a bbox grouped with points, representing the object size.   * `image_size` - IMAGE_SIZE * `group_bbox_size` - GROUP_BBOX_SIZE. [optional]  # noqa: E501

            line_thickness (float): Thickness of polylines, relatively to the (image area) ^ 0.5. The distance to the boundary around the GT line, inside of which the checked line points should be . [optional] if omitted the server will use the default value of 0.01  # noqa: E501

            low_overlap_threshold (float): Used for distinction between strong / weak (low_overlap) matches . [optional] if omitted the server will use the default value of 0.8  # noqa: E501

            compare_line_orientation (bool): Enables or disables polyline orientation comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

            line_orientation_threshold (float): The minimal gain in the GT IoU between the given and reversed line directions to consider the line inverted. Only used when the 'compare_line_orientation' parameter is true . [optional] if omitted the server will use the default value of 0.1  # noqa: E501

            compare_groups (bool): Enables or disables annotation group checks. [optional] if omitted the server will use the default value of True  # noqa: E501

            group_match_threshold (float): Minimal IoU for groups to be considered matching. Only used when the 'compare_groups' parameter is true . [optional] if omitted the server will use the default value of 0.5  # noqa: E501

            check_covered_annotations (bool): Check for partially-covered annotations, useful in segmentation tasks . [optional] if omitted the server will use the default value of True  # noqa: E501

            object_visibility_threshold (float): Minimal visible area percent of the spatial annotations (polygons, masks) for reporting covered annotations. Only used when the 'object_visibility_threshold' parameter is true . [optional] if omitted the server will use the default value of 0.05  # noqa: E501

            panoptic_comparison (bool): Use only the visible part of the masks and polygons in comparisons . [optional] if omitted the server will use the default value of True  # noqa: E501

            compare_attributes (bool): Enables or disables annotation attribute comparison. [optional] if omitted the server will use the default value of True  # noqa: E501

            empty_is_annotated (bool): Consider empty frames annotated as \"empty\". This affects target metrics like accuracy in cases there are no annotations. If disabled, frames without annotations are counted as not matching (accuracy is 0). If enabled, accuracy will be 1 instead. This will also add virtual annotations to empty frames in the comparison results. . [optional] if omitted the server will use the default value of False  # noqa: E501

            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
"""

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

