# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210731

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('dashboard_group.dashboard_service_service_group.command_name', 'dashboard-service'), cls=CommandGroupWithAlias, help=cli_util.override('dashboard_group.dashboard_service_service_group.help', """Use the Oracle Cloud Infrastructure Dashboards service API to manage dashboards in the Console.
Dashboards provide an organized and customizable view of resources and their metrics in the Console.
For more information, see [Dashboards].

**Important:** Resources for the Dashboards service are created in the tenacy's home region.
Although it is possible to create dashboard and dashboard group resources in regions other than the home region,
you won't be able to view those resources in the Console.
Therefore, creating resources outside of the home region is not recommended."""), short_help=cli_util.override('dashboard_group.dashboard_service_service_group.short_help', """Dashboards API"""))
@cli_util.help_option_group
def dashboard_service_service_group():
    pass
