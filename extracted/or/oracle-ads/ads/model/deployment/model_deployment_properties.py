#!/usr/bin/env python
# -*- coding: utf-8; -*-

# Copyright (c) 2021, 2023 Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/
from typing import Any, Dict, Optional, Union
import warnings

import oci.data_science.models as data_science_models
from ads.common import utils
from ads.common.oci_datascience import OCIDataScienceMixin

from .common.utils import OCIClientManager

import warnings

warnings.warn(
    (
        "The `ads.model.deployment.model_deployment_properties` is deprecated in `oracle-ads 2.8.6` and will be removed in `oracle-ads 3.0`."
        "Use `ModelDeploymentInfrastructure` and `ModelDeploymentRuntime` classes in `ads.model.deployment` module for configuring model deployment. "
        "Check https://accelerated-data-science.readthedocs.io/en/latest/user_guide/model_registration/introduction.html"
    ),
    DeprecationWarning,
    stacklevel=2,
)


class ModelDeploymentProperties(
    OCIDataScienceMixin, data_science_models.ModelDeployment
):
    """Represents the details for a model deployment

    Attributes
    ----------
    swagger_types : dict
        The property names and the corresponding types of OCI ModelDeployment model.
    model_id : str
        The model artifact OCID in model catalog.
    model_uri : str
        uri to model files, can be local or in cloud storage.

    Methods
    -------
    with_prop(property_name, value)
        Set the model deployment details `property_name` attribute to `value`
    with_instance_configuration(config)
        Set the configuration of VM instance.
    with_access_log(log_group_id, log_id)
        Config the access log with OCI logging service
    with_predict_log(log_group_id, log_id)
        Config the predict log with OCI logging service
    build()
        Return an instance of CreateModelDeploymentDetails for creating the deployment.
    """

    # These properties are supported by ModelDeploymentProperties but are not top-level attributes of ModelDeployment
    sub_properties = [
        "instance_shape",
        "instance_count",
        "bandwidth_mbps",
        "access_log_group_id",
        "access_log_id",
        "predict_log_group_id",
        "predict_log_id",
        "memory_in_gbs",
        "ocpus",
    ]

    def __init__(
        self,
        model_id: Optional[str] = None,
        model_uri: Optional[str] = None,
        oci_model_deployment: Union[
            data_science_models.ModelDeployment,
            data_science_models.CreateModelDeploymentDetails,
            data_science_models.UpdateModelDeploymentDetails,
            Dict,
        ] = None,
        config: dict = None,
        **kwargs,
    ):
        """Initialize a ModelDeploymentProperties object by specifying one of the followings:

        Parameters
        ----------
        model_id: (str, optiona). Defaults to None.
            Model Artifact OCID. The model_id must be specified either
            explicitly or as an attribute of the OCI object.
        model_uri: (str, optiona). Defaults to None.
            Uri to model files, can be local or in cloud storage.
        oci_model_deployment: (Union[ModelDeployment, CreateModelDeploymentDetails, UpdateModelDeploymentDetails, Dict], optional). Defaults to None.
            An OCI model or Dict containing model deployment details.
            The OCI model can be an instance of either `ModelDeployment`,
            `CreateModelDeploymentDetails` or `UpdateModelConfigurationDetails`.
        config : (Dict, optional). Defaults to None.
            ADS auth dictionary for OCI authentication.
            This can be generated by calling ads.common.auth.api_keys() or
            ads.common.auth.resource_principal().
            If this is None, ads.common.default_signer(client_kwargs) will be used.
        kwargs:
            Users can also initialize the object by using keyword arguments.
            The following keyword arguments are supported by `oci.data_science.models.data_science_models.ModelDeployment`:

            - `display_name`,
            - `description`,
            - `project_id`,
            - `compartment_id`,
            - `model_deployment_configuration_details`,
            - `category_log_details`,
            - `freeform_tags`,
            - `defined_tags`.

            If display_name is not specified, a randomly generated easy to remember name will be generated,
            like 'strange-spider-2022-08-17-23:55.02'.

            ModelDeploymentProperties also supports the following additional
            keyward arguments:

            - `instance_shape`,
            - `instance_count`,
            - `bandwidth_mbps`,
            - `access_log_group_id`,
            - `access_log_id`,
            - `predict_log_group_id`,
            - `predict_log_id`,
            - `memory_in_gbs`,
            - `ocpus`.

            These additional arguments will be saved into appropriate properties
            in the OCI model.

        Raises
        ------
        ValueError
            model_id is None AND not specified in
            oci_model_deployment.model_deployment_configuration_details.model_configuration_details.
        """
        if config:
            warnings.warn(
                "`config` will be deprecated in 3.0.0 and will be ignored now."
            )

        self.model_id = model_id
        self.model_uri = model_uri

        oci_kwargs = {}
        self.oci_model_deployment = oci_model_deployment
        if oci_model_deployment:
            # User specified oci_model_deployment, which could be an OCI model object or a dict
            if isinstance(oci_model_deployment, dict):
                oci_kwargs = oci_model_deployment
                # If user specified properties defined in the sub_properties in oci_model_deployment (as dict),
                # move them to the kwargs so that they can be processed correctly.
                for key in list(oci_kwargs.keys()):
                    if key in self.sub_properties and not key in kwargs:
                        kwargs[key] = oci_kwargs.pop(key)
            else:
                # Extract properties from OCI model as a dict
                if hasattr(oci_model_deployment, "swagger_types"):
                    oci_kwargs = {
                        k: getattr(oci_model_deployment, k)
                        for k in oci_model_deployment.swagger_types.keys()
                    }
                elif oci_model_deployment:
                    raise ValueError(
                        "Invalid value for oci_model_deployment when initializing ModelDeploymentProperties: "
                        f"{oci_model_deployment}. "
                        "ModelDeploymentProperties should be initialized with an instance of OCI data science model, "
                        "a dictionary or keyword arguments."
                    )

        # Use kwargs to initialize OCI ModelDeployment attributes
        super().__init__(**oci_kwargs)

        # Get model ID from OCI object
        if self.model_id is None:
            try:
                self.model_id = (
                    self.model_deployment_configuration_details.model_configuration_details.model_id
                )
            except:
                self.model_id = None

        if self.model_id:
            self._config_model_id()

        # Process additional kwargs
        # Convert all keys to lower case
        kwargs = {str(k).lower(): v for k, v in kwargs.items()}

        # Set default display_name if not specified - randomly generated easy to remember name generated
        if "display_name" not in kwargs or kwargs["display_name"] is None:
            kwargs["display_name"] = utils.get_random_name_for_resource()

        # Set ModelDeployment properties
        for key, val in kwargs.items():
            if key in self.swagger_types.keys():
                self.with_prop(key, val)

        # Config instance
        instance_config = {}
        for key in [
            "instance_shape",
            "instance_count",
            "bandwidth_mbps",
            "memory_in_gbs",
            "ocpus",
        ]:
            if key in kwargs:
                instance_config[key] = kwargs[key]
        if instance_config:
            self.with_instance_configuration(config=instance_config)

        # Config logging
        if "access_log_group_id" in kwargs or "access_log_id" in kwargs:
            if not ("access_log_group_id" in kwargs and "access_log_id" in kwargs):
                raise ValueError(
                    "access_log_group_id and access_log_id must be specified at the same time."
                )
            self.with_access_log(kwargs["access_log_group_id"], kwargs["access_log_id"])

        if "predict_log_group_id" in kwargs or "predict_log_id" in kwargs:
            if not ("predict_log_group_id" in kwargs and "predict_log_id" in kwargs):
                raise ValueError(
                    "predict_log_group_id and predict_log_id must be specified at the same time."
                )
            self.with_predict_log(
                kwargs["predict_log_group_id"], kwargs["predict_log_id"]
            )

    def with_instance_configuration(self, config):
        """with_instance_configuration creates a ModelDeploymentDetails object with a specific config

        Parameters
        ----------
        config : dict
            dictionary containing instance configuration about the deployment.
            The following keys are supported:

            - instance_shape: str,
            - instance_count: int,
            - bandwidth_mbps: int,
            - memory_in_gbs: float,
            - ocpus: float

            The instance_shape and instance_count are required when creating a new deployment.
            They are optional when updating an existing deployment.

        Returns
        -------
        ModelDeploymentProperties
            self

        """
        # Convert all keys to lower case for backward compatibility
        config = {str(k).lower(): v for k, v in config.items()}

        single_type_model_deployment_object = (
            data_science_models.SingleModelDeploymentConfigurationDetails()
        )

        model_configuration_details_object = (
            data_science_models.ModelConfigurationDetails()
        )
        model_configuration_details_object.model_id = self.model_id

        # instance_configuration is required even though it can be initialized with empty values
        instance_configuration_object = data_science_models.InstanceConfiguration()
        if "instance_shape" in config:
            instance_configuration_object.instance_shape_name = config["instance_shape"]

        if config.get("memory_in_gbs") or config.get("ocpus"):
            instance_shape_config_details = (
                data_science_models.ModelDeploymentInstanceShapeConfigDetails(
                    memory_in_gbs=config.pop("memory_in_gbs", None),
                    ocpus=config.pop("ocpus", None),
                )
            )
            instance_configuration_object.model_deployment_instance_shape_config_details = (
                instance_shape_config_details
            )

        model_configuration_details_object.instance_configuration = (
            instance_configuration_object
        )

        # scaling_policy is required even though it can be initialized with empty values
        scaling_policy_object = data_science_models.FixedSizeScalingPolicy()
        if "instance_count" in config:
            scaling_policy_object.instance_count = int(config["instance_count"])
        model_configuration_details_object.scaling_policy = scaling_policy_object

        if "bandwidth_mbps" in config:
            model_configuration_details_object.bandwidth_mbps = config["bandwidth_mbps"]

        single_type_model_deployment_object.model_configuration_details = (
            model_configuration_details_object
        )
        self.model_deployment_configuration_details = (
            single_type_model_deployment_object
        )
        return self

    def with_category_log(self, log_type: str, group_id: str, log_id: str):
        """Adds category log configuration

        Parameters
        ----------
        log_type : str
            The type of logging to be configured. Must be "access" or "predict"
        group_id : str
            Log group ID of OCI logging service
        log_id : str
            Log ID of OCI logging service

        Returns
        -------
        ModelDeploymentProperties
            self

        Raises
        ------
        ValueError
            When log_type is invalid

        """
        if log_type not in ["access", "predict"]:
            raise ValueError(
                f'Invalid log type: {log_type}. Must be "access" or "predict".'
            )
        if not self.category_log_details:
            self.category_log_details = data_science_models.CategoryLogDetails()
        log_details = data_science_models.LogDetails()
        log_details.log_group_id = group_id
        log_details.log_id = log_id
        setattr(self.category_log_details, log_type, log_details)
        return self

    def with_access_log(self, log_group_id: str, log_id: str):
        """Adds access log config

        Parameters
        ----------
        group_id : str
            Log group ID of OCI logging service
        log_id : str
            Log ID of OCI logging service

        Returns
        -------
        ModelDeploymentProperties
            self

        """
        return self.with_category_log("access", log_group_id, log_id)

    def with_predict_log(self, log_group_id: str, log_id: str):
        """Adds predict log config

        Parameters
        ----------
        group_id : str
            Log group ID of OCI logging service
        log_id : str
            Log ID of OCI logging service

        Returns
        -------
        ModelDeploymentProperties
            self

        """
        return self.with_category_log("predict", log_group_id, log_id)

    def with_logging_configuration(
        self,
        access_log_group_id: str,
        access_log_id: str,
        predict_log_group_id: Optional[str] = None,
        predict_log_id: Optional[str] = None,
    ):
        """Adds OCI logging configurations for OCI logging service

        Parameters
        ----------
        access_log_group_id : str
            Log group ID of OCI logging service for access log
        access_log_id : str
            Log ID of OCI logging service for access log
        predict_log_group_id : str
            Log group ID of OCI logging service for predict log
        predict_log_id : str
            Log ID of OCI logging service for predict log

        Returns
        -------
        ModelDeploymentProperties
            self

        """
        self.with_access_log(access_log_group_id, access_log_id)
        if predict_log_group_id and predict_log_id:
            self.with_predict_log(predict_log_group_id, predict_log_id)
        return self

    def with_prop(self, property_name: str, value: Any):
        """Sets model deployment's `property_name` attribute to `value`

        Parameters
        ----------
        property_name : str
            Name of a model deployment property.
        value :
            New value for property attribute.

        Returns
        -------
        ModelDeploymentProperties
            self

        """
        if property_name not in self.swagger_types:
            raise AttributeError(
                f"OCI ModelDeployment does not have the attribute {property_name}"
            )
        setattr(self, property_name, value)
        return self

    def _config_model_id(self):
        """Sets the model ID in the model configuration details using the value of self.model_id
        This method should be called before preparing the payload for OCI API.
        """
        if (
            self.model_deployment_configuration_details
            and self.model_deployment_configuration_details.model_configuration_details
        ):
            self.model_deployment_configuration_details.model_configuration_details.model_id = (
                self.model_id
            )
        else:
            self.with_instance_configuration({})

    def to_oci_model(self, oci_model):
        """Convert properties into an OCI data model

        Parameters
        ----------
        oci_model : class
            The class of OCI data model, e.g., oci.data_science_models.CreateModelDeploymentDetails

        """
        if self.model_id:
            self._config_model_id()

        return super().to_oci_model(oci_model)

    def build(self) -> data_science_models.CreateModelDeploymentDetails:
        """Converts the deployment properties to OCI CreateModelDeploymentDetails object.
        Converts a model URI into a model OCID if user passed in a URI.

        Returns
        -------
        CreateModelDeploymentDetails
            A CreateModelDeploymentDetails instance ready for OCI API.

        """
        if self.model_uri:
            self.model_id = OCIClientManager().prepare_artifact(
                model_uri=self.model_uri,
                properties=dict(
                    display_name="testing",
                    project_id=self.project_id,
                    compartment_id=self.compartment_id,
                ),
            )
            self.model_deployment_configuration_details.model_configuration_details.model_id = (
                self.model_id
            )
        return self.to_oci_model(data_science_models.CreateModelDeploymentDetails)

    def to_update_deployment(self) -> data_science_models.UpdateModelDeploymentDetails:
        """Converts the deployment properties to OCI UpdateModelDeploymentDetails object.

        Returns
        -------
        CreateModelDeploymentDetails
            An UpdateModelDeploymentDetails instance ready for OCI API.

        """
        return self.to_oci_model(data_science_models.UpdateModelDeploymentDetails)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
