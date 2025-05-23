#  Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import json

import luigi

from servicecatalog_puppet import aws, constants, serialisation_utils
from servicecatalog_puppet.workflow.launch import provision_product_task


class ProvisionProductDryRunTask(provision_product_task.ProvisionProductTask):
    def output(self):
        return luigi.LocalTarget(self.output_location)

    @property
    def output_location(self):
        return f"output/{self.task_reference}.json"

    def run(self):
        details = self.load_from_input("details")
        product_id = details.get("product_details").get("ProductId")
        version_id = details.get("version_details").get("Id")

        self.info(f"starting deploy try {self.try_count} of {self.retry_count}")

        all_params = self.get_parameter_values()
        with self.spoke_regional_client("servicecatalog") as service_catalog:
            self.info(f"looking for previous failures")
            path_name = self.portfolio

            response = service_catalog.scan_provisioned_products_single_page(
                AccessLevelFilter={"Key": "Account", "Value": "self"},
            )

            provisioned_product_id = False
            provisioning_artifact_id = None
            current_status = "NOT_PROVISIONED"
            for r in response.get("ProvisionedProducts", []):
                if r.get("Name") == self.launch_name:
                    current_status = r.get("Status")
                    if current_status in ["AVAILABLE", "TAINTED"]:
                        provisioned_product_id = r.get("Id")
                        provisioning_artifact_id = r.get("ProvisioningArtifactId")

            if provisioning_artifact_id is None:
                self.info(f"params unchanged")
                self.write_result(
                    current_version="-",
                    new_version=self.version,
                    effect=constants.CHANGE,
                    current_status="NOT_PROVISIONED",
                    active="N/A",
                    notes="New provisioning",
                )
            else:
                self.info(
                    f"pp_id: {provisioned_product_id}, paid : {provisioning_artifact_id}"
                )
                current_version_details = self.get_current_version(
                    provisioning_artifact_id, product_id, service_catalog
                )

                with self.spoke_regional_client("cloudformation") as cloudformation:
                    self.info(
                        f"checking {product_id} {version_id} {path_name} in {self.account_id} {self.region}"
                    )

                    with self.input().get("provisioning_artifact_parameters").open(
                        "r"
                    ) as f:
                        provisioning_artifact_parameters = (
                            serialisation_utils.json_loads(f.read())
                        )

                    params_to_use = {}
                    for p in provisioning_artifact_parameters:
                        param_name = p.get("ParameterKey")
                        params_to_use[param_name] = all_params.get(
                            param_name, p.get("DefaultValue")
                        )

                    if provisioning_artifact_id == version_id:
                        self.info(f"found previous good provision")
                        if provisioned_product_id:
                            self.info(f"checking params for diffs")
                            pp_stack_name = aws.get_stack_name_for_pp_id(
                                service_catalog, provisioned_product_id
                            )
                            provisioned_parameters = aws.get_parameters_for_stack(
                                cloudformation,
                                pp_stack_name,
                            )
                            self.info(f"current params: {provisioned_parameters}")
                            self.info(f"new params: {params_to_use}")

                            if provisioned_parameters == params_to_use:
                                self.info(f"params unchanged")
                                self.write_result(
                                    current_version=self.version,
                                    new_version=self.version,
                                    effect=constants.NO_CHANGE,
                                    current_status=current_status,
                                    active=current_version_details.get("Active"),
                                    notes="Versions and params are the same",
                                )
                            else:
                                self.write_result(
                                    current_version=self.version,
                                    new_version=self.version,
                                    effect=constants.CHANGE,
                                    current_status=current_status,
                                    active=current_version_details.get("Active"),
                                    notes="Versions are the same but the params are different",
                                )
                    else:
                        if provisioning_artifact_id:
                            current_version = current_version_details.get("Name")
                            active = current_version_details.get("Active")
                        else:
                            current_version = ""
                            active = False
                        self.write_result(
                            current_version=current_version,
                            new_version=self.version,
                            effect=constants.CHANGE,
                            current_status=current_status,
                            active=active,
                            notes="Version change",
                        )

    def get_current_version(
        self, provisioning_artifact_id, product_id, service_catalog
    ):
        return service_catalog.describe_provisioning_artifact(
            ProvisioningArtifactId=provisioning_artifact_id,
            ProductId=product_id,
        ).get("ProvisioningArtifactDetail")

    def write_result(
        self, current_version, new_version, effect, current_status, active, notes=""
    ):
        with self.output().open("w") as f:
            f.write(
                json.dumps(
                    {
                        "current_version": current_version,
                        "new_version": new_version,
                        "effect": effect,
                        "current_status": current_status,
                        "active": active,
                        "notes": notes,
                        "params": self.param_kwargs,
                    },
                    indent=4,
                    default=str,
                )
            )
