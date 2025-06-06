# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.
import json
import logging
import re
from collections import defaultdict
from typing import Dict, List, Optional

from pcluster import imagebuilder_utils
from pcluster.aws.aws_api import AWSApi, KeyPairInfo
from pcluster.aws.aws_resources import CapacityReservationInfo
from pcluster.aws.common import AWSClientError
from pcluster.config.common import CapacityType
from pcluster.constants import NVIDIA_OPENRM_UNSUPPORTED_INSTANCE_TYPES, UNSUPPORTED_OSES_FOR_MICRO_NANO
from pcluster.utils import get_resource_name_from_resource_arn
from pcluster.validators.common import FailureLevel, Validator

LOGGER = logging.getLogger(__name__)


class InstanceTypePlacementGroupValidator(Validator):
    """
    EC2 Instance Type Placement Group validator.

    Not all EC2 Instance Type can be launched in a Placement Group.
    """

    def _validate(self, instance_type: str, instance_type_data: dict, placement_group_enabled: bool):
        if placement_group_enabled:
            placement_group_supported_strategies = instance_type_data.get("PlacementGroupInfo", {}).get(
                "SupportedStrategies", []
            )
            if "cluster" not in placement_group_supported_strategies:
                self._add_failure(
                    f"The instance type '{instance_type}' doesn't support being launched in a cluster placement group. "
                    f"Please either disable the placement group or remove the instance type from the compute resource.",
                    FailureLevel.ERROR,
                )


class InstanceTypeAcceleratorManufacturerValidator(Validator):
    """
    EC2 Instance Type Accelerator Manufacturer validator.

    ParallelCluster only support specific Accelerator Manufacturer.
    """

    def _validate(self, instance_type: str, instance_type_data: dict):
        gpu_info = instance_type_data.get("GpuInfo", {})
        if gpu_info:
            gpu_manufacturers = list({gpu.get("Manufacturer", "") for gpu in gpu_info.get("Gpus", [])})

            # Only one GPU manufacturer is associated with each Instance Type's GPU
            manufacturer = gpu_manufacturers[0] if gpu_manufacturers else ""
            if manufacturer.upper() != "NVIDIA":
                self._add_failure(
                    f"The accelerator manufacturer '{manufacturer}' for instance type '{instance_type}' is "
                    "not supported. Please make sure to use a custom AMI with the appropriate drivers in order to "
                    "leverage the accelerator functionalities",
                    FailureLevel.WARNING,
                )
                LOGGER.warning(
                    "ParallelCluster offers native support for NVIDIA manufactured GPUs only. "
                    "InstanceType (%s) GPU Info: %s. "
                    "Please make sure to use a custom AMI with the appropriate drivers in order to leverage the "
                    "GPUs functionalities",
                    instance_type,
                    json.dumps(gpu_info),
                )

        inference_accelerator_info = instance_type_data.get("InferenceAcceleratorInfo", {})
        if inference_accelerator_info:
            inference_accelerator_manufacturers = list(
                {
                    accelerator.get("Manufacturer", "")
                    for accelerator in inference_accelerator_info.get("Accelerators", [])
                }
            )

            # Only one accelerator manufacturer is associated with each Instance Type's accelerator
            manufacturer = inference_accelerator_manufacturers[0] if inference_accelerator_manufacturers else ""
            if manufacturer.upper() != "AWS":
                self._add_failure(
                    f"The accelerator manufacturer '{manufacturer}' for instance type '{instance_type}' is "
                    "not supported. Please make sure to use a custom AMI with the appropriate drivers in order to "
                    "leverage the accelerator functionalities",
                    FailureLevel.WARNING,
                )
                LOGGER.warning(
                    "ParallelCluster offers native support for 'AWS' manufactured Inference Accelerators only. "
                    "InstanceType (%s) accelerator info: %s. "
                    "Please make sure to use a custom AMI with the appropriate drivers in order to leverage the "
                    "accelerators functionalities.",
                    instance_type,
                    json.dumps(inference_accelerator_info),
                )


class InstanceTypeValidator(Validator):
    """
    EC2 Instance type validator.

    Verify the given instance type is a supported one.
    """

    def _validate(self, instance_type: str):
        if instance_type not in AWSApi.instance().ec2.list_instance_types():
            self._add_failure(f"The instance type '{instance_type}' is not supported.", FailureLevel.ERROR)


class InstanceTypeMemoryInfoValidator(Validator):
    """
    EC2 Instance Type MemoryInfo validator.

    Verify that EC2 provides the necessary memory information about an instance type.
    """

    def _validate(self, instance_type: str, instance_type_data: dict):
        size_in_mib = instance_type_data.get("MemoryInfo", {}).get("SizeInMiB")
        if size_in_mib is None:
            self._add_failure(
                f"EC2 does not provide memory information for instance type '{instance_type}'.",
                FailureLevel.ERROR,
            )


class InstanceTypeBaseAMICompatibleValidator(Validator):
    """EC2 Instance type and base ami compatibility validator."""

    def _validate(self, instance_type: str, image: str):
        image_info = self._validate_base_ami(image)
        instance_architectures = self._validate_instance_type(instance_type)
        if image_info and instance_architectures:
            ami_architecture = image_info.architecture
            if ami_architecture not in instance_architectures:
                self._add_failure(
                    "AMI {0}'s architecture ({1}) is incompatible with the architecture supported by the "
                    "instance type {2} chosen ({3}). Use either a different AMI or a different instance type.".format(
                        image_info.id, ami_architecture, instance_type, instance_architectures
                    ),
                    FailureLevel.ERROR,
                )

        if (
            image_info
            and image_info.description
            and "AWS ParallelCluster AMI" in image_info.description
            and instance_type.split(".")[0] in NVIDIA_OPENRM_UNSUPPORTED_INSTANCE_TYPES
        ):
            self._add_failure(
                f"The instance type '{instance_type}' is not supported by NVIDIA OpenRM drivers. "
                f"OpenRM can only be used on any Turing or later GPU architectures. "
                f"Please consider building a custom AMI with closed source NVIDIA drivers "
                f"and then suppress this validator or using a different instance type.",
                FailureLevel.ERROR,
            )

    def _validate_base_ami(self, image: str):
        try:
            ami_id = imagebuilder_utils.get_ami_id(image)
            image_info = AWSApi.instance().ec2.describe_image(ami_id=ami_id)
            return image_info
        except AWSClientError:
            self._add_failure(f"Invalid image '{image}'.", FailureLevel.ERROR)
            return None

    def _validate_instance_type(self, instance_type: str):
        if instance_type not in AWSApi.instance().ec2.list_instance_types():
            self._add_failure(
                f"The instance type '{instance_type}' is not supported.",
                FailureLevel.ERROR,
            )
            return []
        return AWSApi.instance().ec2.get_supported_architectures(instance_type)


class InstanceTypeOSCompatibleValidator(Validator):
    """EC2 Instance type and os compatibility validator."""

    def _validate(self, instance_type: str, os: str):
        if os in UNSUPPORTED_OSES_FOR_MICRO_NANO:
            if re.search(r"(micro)|(nano)", instance_type):
                self._add_failure(
                    "It is not recommended to use instance type {0} with {1}. If you want to use "
                    "{1} it is recommended to use an instance type with at least 1.7 GB of memory.".format(
                        instance_type, os
                    ),
                    FailureLevel.WARNING,
                )


class KeyPairValidator(Validator):
    """
    EC2 key pair validator.

    Verify the given key pair is correct.
    """

    def _validate(self, key_name: str, os: str):
        if key_name:
            try:
                key_pair = KeyPairInfo(key_name)
                if os in ["ubuntu2204", "ubuntu2404"] and key_pair.key_type == "rsa":
                    self._add_failure(
                        f"{os} does not support RSA keys. Please generate and use an ed25519 key",
                        FailureLevel.ERROR,
                    )
            except AWSClientError as e:
                self._add_failure(str(e), FailureLevel.ERROR)
        else:
            self._add_failure(
                "If you do not specify a key pair, you can't connect to the instance unless you choose an AMI "
                "that is configured to allow users another way to log in",
                FailureLevel.WARNING,
            )


class PlacementGroupNamingValidator(Validator):
    """Placement group naming validator."""

    def _validate(self, placement_group):
        if placement_group.id and placement_group.name:
            self._add_failure(
                "PlacementGroup Id cannot be set when setting PlacementGroup Name.  Please "
                "set either Id or Name but not both.",
                FailureLevel.ERROR,
            )
        identifier = placement_group.name or placement_group.id
        if identifier:
            if placement_group.enabled is False:
                self._add_failure(
                    "The PlacementGroup feature must be enabled (Enabled: true) in order "
                    "to assign a Name or Id parameter.  Please either remove the Name/Id parameter to disable the "
                    "feature, set Enabled: true to enable it, or remove the Enabled parameter to imply it is enabled "
                    "with the Name/Id given",
                    FailureLevel.ERROR,
                )
            else:
                try:
                    AWSApi.instance().ec2.describe_placement_group(identifier)
                except AWSClientError as e:
                    self._add_failure(str(e), FailureLevel.ERROR)


class CapacityTypeValidator(Validator):
    """Compute type validator. Verify that specified compute type is compatible with specified instance type."""

    @staticmethod
    def _get_supported_usage_class_from_capacity_type(capacity_type):
        """
        Return value to search in SupportedUsageClasses according to capacity type.

        SupportedUsageClasses is an attribute of instance type that can be retrieved by describe-instance-types call.
        """
        capacity_type_to_supported_usage_class_map = {"CAPACITY_BLOCK": "capacity-block"}
        return capacity_type_to_supported_usage_class_map.get(capacity_type.value, capacity_type.value.lower())

    def _validate(self, capacity_type: CapacityType, instance_type: str, capacity_reservation_id: Optional[str]):
        compute_type_value = self._get_supported_usage_class_from_capacity_type(capacity_type)
        supported_usage_classes = AWSApi.instance().ec2.get_instance_type_info(instance_type).supported_usage_classes()

        # Be sure to have a Capacity reservation id when using capacity block
        if capacity_type == CapacityType.CAPACITY_BLOCK and not capacity_reservation_id:
            self._add_failure(
                "Capacity Reservation id is required when using CAPACITY_BLOCK as capacity type.",
                FailureLevel.ERROR,
            )

        # Verify capacity type is supported by the given instance type
        if not supported_usage_classes:
            self._add_failure(
                f"Could not check support for usage class '{compute_type_value}' with instance type '{instance_type}'",
                FailureLevel.WARNING,
            )
        elif compute_type_value not in supported_usage_classes:
            self._add_failure(
                f"Usage type '{compute_type_value}' not supported with instance type '{instance_type}'",
                FailureLevel.ERROR,
            )


class AmiOsCompatibleValidator(Validator):
    """
    node AMI and OS compatibility validator.

    If image has tag of OS, compare AMI OS with cluster OS, else print out a warning message.
    """

    def _validate(self, os: str, image_id: str):
        image_info = AWSApi.instance().ec2.describe_image(ami_id=image_id)
        image_os = image_info.image_os
        if image_os:
            if image_os != os:
                self._add_failure(
                    f"The OS of node AMI {image_id} is {image_os}, it is not compatible with cluster OS {os}.",
                    FailureLevel.ERROR,
                )
        else:
            self._add_failure(
                f"Could not check node AMI {image_id} OS and cluster OS {os} compatibility, please make sure "
                f"they are compatible before cluster creation and update operations.",
                FailureLevel.WARNING,
            )


class CapacityReservationValidator(Validator):
    """Validate capacity reservation can be used with the instance type and subnet."""

    @staticmethod
    def _get_reservation_type_from_capacity_type(capacity_type: CapacityType):
        """
        Return value to search in ReservationType according to capacity type.

        ReservationType is an attribute of capacity block that can be retrieved by describe-capacity-reservations call.
        """
        capacity_type_to_reservation_type_class_map = {"CAPACITY_BLOCK": "capacity-block"}
        return capacity_type_to_reservation_type_class_map.get(capacity_type.value, capacity_type.value.lower())

    def _validate(
        self,
        capacity_reservation_id: str,
        instance_types: List[str],
        is_flexible: bool,
        subnet: str,
        capacity_type: CapacityType,
    ):
        if capacity_reservation_id:
            capacity_reservation = AWSApi.instance().ec2.describe_capacity_reservations([capacity_reservation_id])[0]

            if not instance_types:
                # If the instance type doesn't exist, this is an invalid config,
                # this cannot happen because instance type is automatically retrieved.
                self._add_failure(
                    "Unexpected failure. InstanceType parameter cannot be empty when using CapacityReservationId.",
                    FailureLevel.ERROR,
                )
            elif is_flexible:
                # CapacityReservationId is not supported by create-fleet (FlexibleComputeResource)
                self._add_failure(
                    (
                        "CapacityReservationId parameter cannot be used with Instances parameter."
                        "CapacityReservationId can only be used with the InstanceType parameter "
                        "(https://docs.aws.amazon.com/parallelcluster/latest/ug/Scheduling-v3.html#yaml-"
                        "Scheduling-SlurmQueues-ComputeResources-InstanceType)."
                    ),
                    FailureLevel.ERROR,
                )
            else:
                instance_type = instance_types[0]
                if capacity_reservation.instance_type() != instance_type:
                    self._add_failure(
                        f"Capacity reservation {capacity_reservation_id} must have the same instance type "
                        f"as {instance_type}.",
                        FailureLevel.ERROR,
                    )

            if capacity_reservation.availability_zone() != AWSApi.instance().ec2.get_subnet_avail_zone(subnet):
                self._add_failure(
                    f"Capacity reservation {capacity_reservation_id} must use the same availability zone "
                    f"as subnet {subnet}.",
                    FailureLevel.ERROR,
                )

            reservation_type = capacity_reservation.reservation_type()
            if (
                capacity_type == CapacityType.CAPACITY_BLOCK
                and reservation_type != self._get_reservation_type_from_capacity_type(capacity_type)
            ):
                self._add_failure(
                    (
                        f"Capacity reservation {capacity_reservation_id} is not a Capacity Block reservation. "
                        f"It cannot be used when specifying CapacityType: {capacity_type.value}."
                    ),
                    FailureLevel.ERROR,
                )


class CapacityReservationSizeValidator(Validator):
    """Validate capacity reservation size is not overloaded by max count in the queues/compute resource settings."""

    def _validate(self, capacity_reservation_id: str, num_of_instances: int):
        if capacity_reservation_id:
            capacity_reservation = AWSApi.instance().ec2.describe_capacity_reservations([capacity_reservation_id])[0]

            # total_instance_count is available for standard ODCR, incremental_requested_quantity for Capacity Block
            reserved_instances = max(
                capacity_reservation.total_instance_count(), capacity_reservation.incremental_requested_quantity()
            )
            if num_of_instances > reserved_instances:
                self._add_failure(
                    (
                        f"Number of instances configured for Capacity Reservation {capacity_reservation_id}: "
                        f"{num_of_instances} is exceeding the total instances count available for the "
                        f"Capacity Reservation: {reserved_instances}"
                    ),
                    FailureLevel.ERROR,
                )


def get_capacity_reservations(capacity_reservation_resource_group_arn: str):
    """Get capacity reservations info for a given Reservation Resource Group Arn."""
    capacity_reservation_ids = AWSApi.instance().resource_groups.get_capacity_reservation_ids_from_group_resources(
        capacity_reservation_resource_group_arn
    )
    return AWSApi.instance().ec2.describe_capacity_reservations(capacity_reservation_ids)


def capacity_reservation_matches_instance(capacity_reservation: CapacityReservationInfo, instance_type: str) -> bool:
    return capacity_reservation.instance_type() == instance_type


def capacity_reservation_matches_avail_zone(capacity_reservation: CapacityReservationInfo, subnet_id: str) -> bool:
    return capacity_reservation.availability_zone() == AWSApi.instance().ec2.get_subnet_avail_zone(subnet_id)


def capacity_reservation_resource_group_is_service_linked_group(capacity_reservation_resource_group_arn: str):
    try:
        group_config = AWSApi.instance().resource_groups.get_group_configuration(
            group=capacity_reservation_resource_group_arn
        )
        is_cr_pool = False
        for config in group_config["GroupConfiguration"]["Configuration"]:
            if "CapacityReservationPool" in config["Type"]:
                is_cr_pool = True
        return is_cr_pool
    except AWSClientError:
        return False


def get_capacity_reservations_per_az(
    capacity_reservations: List[CapacityReservationInfo],
) -> Dict[str, List[CapacityReservationInfo]]:
    """Create a mapping of an AZ and its related Capacity Reservations."""
    capacity_reservations_per_az = defaultdict(list)
    for capacity_reservation in capacity_reservations:
        capacity_reservations_per_az[capacity_reservation.availability_zone()].append(capacity_reservation)
    return capacity_reservations_per_az


class CapacityReservationResourceGroupValidator(Validator):
    """Validate capacity reservation group is can be used with existing instance types and subnets.

    - When using multiple instance types:
        - At least one capacity reservation in the resource group can be used with one of the instances
    - When using multiple subnets
        - At least one capacity reservation in the resource group can be used with one of the subnets
    """

    def _validate(
        self,
        capacity_reservation_resource_group_arn: str,
        instance_types: List[str],
        subnet_ids: List[str],
        queue_name: str,
        subnet_id_az_mapping: Dict[str, str],
    ):
        if capacity_reservation_resource_group_arn:
            if not capacity_reservation_resource_group_is_service_linked_group(capacity_reservation_resource_group_arn):
                self._add_failure(
                    f"Capacity reservation resource group ({capacity_reservation_resource_group_arn}) must be a "
                    "Service Linked Group created from the AWS CLI.  See "
                    f"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html for more details.",
                    FailureLevel.ERROR,
                )
            else:
                capacity_reservations = get_capacity_reservations(capacity_reservation_resource_group_arn)
                self._validate_unreserved_instance_types_for_azs(
                    capacity_reservations,
                    capacity_reservation_resource_group_arn,
                    {subnet_id_az_mapping[subnet_id] for subnet_id in subnet_ids},
                    instance_types,
                )
                self._validate_with_subnets(
                    queue_name,
                    capacity_reservation_resource_group_arn,
                    capacity_reservations,
                    subnet_ids,
                    subnet_id_az_mapping,
                )

    def _validate_unreserved_instance_types_for_azs(
        self,
        capacity_reservations: List[CapacityReservationInfo],
        capacity_reservation_resource_group_arn,
        availability_zones,
        instance_types,
    ):
        capacity_reservations_per_az = get_capacity_reservations_per_az(capacity_reservations)
        unreserved_instance_types_per_az = defaultdict(list)
        for instance_type in instance_types:
            found_reservation_for_instance_type_in_group = False
            for availability_zone in availability_zones:
                found_reservation_for_instance_type_in_az = False
                for capacity_reservation in capacity_reservations_per_az.get(availability_zone, []):
                    if capacity_reservation_matches_instance(capacity_reservation, instance_type):
                        found_reservation_for_instance_type_in_az = found_reservation_for_instance_type_in_group = True
                        break
                if not found_reservation_for_instance_type_in_az:
                    unreserved_instance_types_per_az[availability_zone].append(instance_type)
            if not found_reservation_for_instance_type_in_group:
                self._add_failure(
                    f"Capacity reservation resource group {capacity_reservation_resource_group_arn} must have "
                    f"at least one capacity reservation for {instance_type}.",
                    FailureLevel.ERROR,
                )

        if unreserved_instance_types_per_az:
            self._add_failure(
                "The Capacity Reservation Resource Group '{crrg_arn}' has reservations for these InstanceTypes and "
                "Availability Zones: '{cr_instance_az}'. Please consider that the cluster can launch instances in these"
                " Availability Zones that have no capacity reservations in the Resource Group for the given "
                "instance types: '{unreserved_instance_types}'.".format(
                    crrg_arn=capacity_reservation_resource_group_arn,
                    cr_instance_az=", ".join(
                        ["(%s: %s)" % (cr.instance_type(), cr.availability_zone()) for cr in capacity_reservations]
                    ),
                    unreserved_instance_types=", ".join(
                        "{%s: %s}" % (az, instance_types)
                        for az, instance_types in sorted(unreserved_instance_types_per_az.items())
                    ),
                ),
                FailureLevel.WARNING,
            )

    def _validate_with_subnets(
        self,
        queue_name,
        cr_group_arn,
        capacity_reservations: List[CapacityReservationInfo],
        subnet_ids,
        subnet_id_az_mapping: Dict[str, str],
    ):
        subnets_without_reservations = []
        found_qualified_capacity_reservation = False

        capacity_reservation_availability_zones = [
            capacity_reservation.availability_zone() for capacity_reservation in capacity_reservations
        ]
        for subnet_id in subnet_ids:
            subnet_az = subnet_id_az_mapping[subnet_id]
            if subnet_az not in capacity_reservation_availability_zones:
                subnets_without_reservations.append(subnet_id)
            else:
                found_qualified_capacity_reservation = True

        if not found_qualified_capacity_reservation:
            self._add_failure(
                "Queue '{queue}' has a subnet configuration mapping to the following availability zones: "
                "'{subnet_azs_without_reservations}' but the Capacity Reservation Resource Group '{cr_group_arn}' "
                "has reservations in these availability zones: '{cr_azs}'. You can either add a capacity reservation "
                "in the availability zones that the subnets are in or remove the Capacity Reservation from the "
                "Cluster Configuration.".format(
                    queue=queue_name,
                    subnet_azs_without_reservations=", ".join(
                        f"({subnet_id}: {subnet_id_az_mapping[subnet_id]})"
                        for subnet_id in subnets_without_reservations
                    ),
                    cr_group_arn=cr_group_arn,
                    cr_azs=", ".join(capacity_reservation_availability_zones),
                ),
                FailureLevel.ERROR,
            )
        if found_qualified_capacity_reservation and subnets_without_reservations:
            self._add_failure(
                "Queue '{queue}' has a subnet configuration mapping to the following availability zones: "
                "'{subnet_azs_without_reservations}' but the Capacity Reservation Group '{cr_group_arn}' reserves "
                "capacity in these availability zones: '{cr_azs}'. Consider adding capacity reservations in all the "
                "availability zones covered by the queue.".format(
                    queue=queue_name,
                    subnet_azs_without_reservations=", ".join(
                        [subnet_id_az_mapping[subnet_id] for subnet_id in subnets_without_reservations]
                    ),
                    cr_group_arn=cr_group_arn,
                    cr_azs=", ".join(capacity_reservation_availability_zones),
                ),
                FailureLevel.WARNING,
            )


class PlacementGroupCapacityTypeValidator(Validator):
    """Validate the placement group is compatible with the capacity type."""

    def _validate(self, capacity_type: str, placement_group_enabled: bool):
        if capacity_type == CapacityType.CAPACITY_BLOCK and placement_group_enabled:
            self._add_failure(
                "When using a capacity block reservation, a placement group constraint should not be set "
                "as insufficient capacity errors may occur due to placement constraints outside of the "
                "reservation even if the capacity reservation has remaining capacity. "
                "Please remove the placement group for the compute resource.",
                FailureLevel.WARNING,
            )


class PlacementGroupCapacityReservationValidator(Validator):
    """Validate the placement group is compatible with the capacity reservation target."""

    def _validate_chosen_pg(
        self, subnet, instance_types, capacity_reservations: List[CapacityReservationInfo], chosen_pg
    ):
        pg_match, open_or_targeted = False, False
        for instance_type in instance_types:
            for capacity_reservation in capacity_reservations:
                if capacity_reservation_matches_instance(
                    capacity_reservation=capacity_reservation, instance_type=instance_type
                ) and capacity_reservation_matches_avail_zone(
                    capacity_reservation=capacity_reservation, subnet_id=subnet
                ):
                    odcr_pg = get_resource_name_from_resource_arn(capacity_reservation.placement_group_arn())
                    if odcr_pg:
                        if odcr_pg == chosen_pg:
                            pg_match = True
                    else:
                        open_or_targeted = True
            if not (pg_match or open_or_targeted):
                self._add_failure(
                    f"The placement group provided '{chosen_pg}' targets the '{instance_type}' instance type but there "
                    f"are no ODCRs included in the resource group that target that instance type.",
                    FailureLevel.ERROR,
                )
            elif open_or_targeted:
                self._add_failure(
                    "When using an open or targeted capacity reservation with an unrelated placement group, "
                    "insufficient capacity errors may occur due to placement constraints outside of the "
                    "reservation even if the capacity reservation has remaining capacity. Please consider either "
                    "not using a placement group for the compute resource or creating a new capacity reservation "
                    "in a related placement group.",
                    FailureLevel.WARNING,
                )

    def _validate_no_pg(
        self, instance_types, capacity_reservations: List[CapacityReservationInfo], subnet, subnet_id_az_mapping
    ):
        for instance_type in instance_types:
            odcr_without_pg = False
            for capacity_reservation in capacity_reservations:
                odcr_pg = get_resource_name_from_resource_arn(capacity_reservation.placement_group_arn())
                # search for a capacity reservation without a placement group and matching instance type and avail zone
                if not odcr_pg and (
                    capacity_reservation_matches_instance(
                        capacity_reservation=capacity_reservation, instance_type=instance_type
                    )
                    and capacity_reservation_matches_avail_zone(
                        capacity_reservation=capacity_reservation, subnet_id=subnet
                    )
                ):
                    odcr_without_pg = True
            if not odcr_without_pg:
                self._add_failure(
                    f"There are no open or targeted ODCRs that match the instance_type '{instance_type}' in "
                    f"'{subnet_id_az_mapping[subnet]}' and no placement group provided. Please either provide a "
                    f"placement group or add an ODCR that does not target a placement group and targets the "
                    f"instance type.",
                    FailureLevel.ERROR,
                )

    def _validate(self, placement_group, odcr, subnet, instance_types, multi_az_enabled, subnet_id_az_mapping):
        if not multi_az_enabled:
            odcr_id = getattr(odcr, "capacity_reservation_id", None)
            odcr_arn = getattr(odcr, "capacity_reservation_resource_group_arn", None)
            if odcr_id:
                capacity_reservations = AWSApi.instance().ec2.describe_capacity_reservations([odcr_id])
            elif odcr_arn:
                capacity_reservations = get_capacity_reservations(odcr_arn)
            else:
                capacity_reservations = None
            if capacity_reservations:
                if placement_group:
                    self._validate_chosen_pg(
                        subnet=subnet,
                        instance_types=instance_types,
                        capacity_reservations=capacity_reservations,
                        chosen_pg=placement_group,
                    )
                else:
                    self._validate_no_pg(
                        subnet=subnet,
                        instance_types=instance_types,
                        capacity_reservations=capacity_reservations,
                        subnet_id_az_mapping=subnet_id_az_mapping,
                    )
