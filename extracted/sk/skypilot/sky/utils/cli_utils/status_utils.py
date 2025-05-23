"""Utilities for sky status."""
import typing
from typing import Any, Callable, Dict, List, Optional

import click
import colorama

from sky import backends
from sky.utils import common_utils
from sky.utils import controller_utils
from sky.utils import log_utils
from sky.utils import resources_utils
from sky.utils import status_lib

if typing.TYPE_CHECKING:
    from sky.provision.kubernetes import utils as kubernetes_utils

if typing.TYPE_CHECKING:
    from sky.provision.kubernetes import utils as kubernetes_utils

COMMAND_TRUNC_LENGTH = 25
NUM_COST_REPORT_LINES = 5

# A record in global_user_state's 'clusters' table.
_ClusterRecord = Dict[str, Any]
# A record returned by core.cost_report(); see its docstr for all fields.
_ClusterCostReportRecord = Dict[str, Any]


class StatusColumn:
    """One column of the displayed cluster table"""

    def __init__(self,
                 name: str,
                 calc_func: Callable,
                 trunc_length: int = 0,
                 show_by_default: bool = True):
        self.name = name
        self.calc_func = calc_func
        self.trunc_length = trunc_length
        self.show_by_default = show_by_default

    def calc(self, record):
        val = self.calc_func(record)
        if self.trunc_length != 0:
            val = common_utils.truncate_long_string(str(val), self.trunc_length)
        return val


def show_status_table(cluster_records: List[_ClusterRecord],
                      show_all: bool,
                      show_user: bool,
                      query_clusters: Optional[List[str]] = None) -> int:
    """Compute cluster table values and display.

    Returns:
        Number of pending auto{stop,down} clusters that are not already
        STOPPED.
    """
    # TODO(zhwu): Update the information for autostop clusters.

    status_columns = [
        StatusColumn('NAME', _get_name),
    ]
    if show_user:
        status_columns.append(StatusColumn('USER', _get_user_name))
        status_columns.append(
            StatusColumn('USER_ID', _get_user_hash, show_by_default=False))

    status_columns += [
        StatusColumn('LAUNCHED', _get_launched),
        StatusColumn('RESOURCES',
                     _get_resources,
                     trunc_length=70 if not show_all else 0),
        StatusColumn('REGION', _get_region, show_by_default=False),
        StatusColumn('ZONE', _get_zone, show_by_default=False),
        StatusColumn('STATUS', _get_status_colored),
        StatusColumn('AUTOSTOP', _get_autostop),
        StatusColumn('HEAD_IP', _get_head_ip, show_by_default=False),
        StatusColumn('COMMAND',
                     _get_command,
                     trunc_length=COMMAND_TRUNC_LENGTH if not show_all else 0),
    ]

    columns = []
    for status_column in status_columns:
        if status_column.show_by_default or show_all:
            columns.append(status_column.name)
    cluster_table = log_utils.create_table(columns)

    num_pending_autostop = 0
    for record in cluster_records:
        row = []
        for status_column in status_columns:
            if status_column.show_by_default or show_all:
                row.append(status_column.calc(record))
        cluster_table.add_row(row)
        num_pending_autostop += _is_pending_autostop(record)

    if cluster_records:
        click.echo(cluster_table)

    if query_clusters:
        cluster_names = {record['name'] for record in cluster_records}
        not_found_clusters = [
            repr(cluster)
            for cluster in query_clusters
            if cluster not in cluster_names
        ]
        cluster_str = 'Cluster'
        if len(not_found_clusters) > 1:
            cluster_str += 's'
        cluster_str += ' '
        cluster_str += ', '.join(not_found_clusters)
        click.echo(f'{cluster_str} not found.')
    elif not cluster_records:
        click.echo('No existing clusters.')
    return num_pending_autostop


def get_total_cost_of_displayed_records(
        cluster_records: List[_ClusterCostReportRecord], display_all: bool):
    """Compute total cost of records to be displayed in cost report."""
    cluster_records.sort(
        key=lambda report: -_get_status_value_for_cost_report(report))

    displayed_records = cluster_records[:NUM_COST_REPORT_LINES]
    if display_all:
        displayed_records = cluster_records

    total_cost = sum(record['total_cost'] for record in displayed_records)
    return total_cost


def show_cost_report_table(cluster_records: List[_ClusterCostReportRecord],
                           show_all: bool,
                           controller_name: Optional[str] = None):
    """Compute cluster table values and display for cost report.

    For each cluster, this shows: cluster name, resources, launched time,
    duration that cluster was up, and total estimated cost.

    The estimated cost column indicates the price for the cluster based on the
    type of resources being used and the duration of use up until now. This
    means if the cluster is UP, successive calls to cost-report will show
    increasing price.

    The estimated cost is calculated based on the local cache of the cluster
    status, and may not be accurate for:

      - clusters with autostop/use_spot set; or

      - clusters that were terminated/stopped on the cloud console.

    Returns:
        Number of pending auto{stop,down} clusters.
    """
    # TODO(zhwu): Update the information for autostop clusters.

    status_columns = [
        StatusColumn('NAME', _get_name),
        StatusColumn('LAUNCHED', _get_launched),
        StatusColumn('DURATION', _get_duration, trunc_length=20),
        StatusColumn('RESOURCES',
                     _get_resources_for_cost_report,
                     trunc_length=70 if not show_all else 0),
        StatusColumn('STATUS',
                     _get_status_for_cost_report,
                     show_by_default=True),
        StatusColumn('COST/hr',
                     _get_price_for_cost_report,
                     show_by_default=True),
        StatusColumn('COST (est.)',
                     _get_estimated_cost_for_cost_report,
                     show_by_default=True),
    ]

    columns = []
    for status_column in status_columns:
        if status_column.show_by_default or show_all:
            columns.append(status_column.name)
    cluster_table = log_utils.create_table(columns)

    num_lines_to_display = NUM_COST_REPORT_LINES
    if show_all:
        num_lines_to_display = len(cluster_records)

    # prioritize showing non-terminated clusters in table
    cluster_records.sort(
        key=lambda report: -_get_status_value_for_cost_report(report))

    for record in cluster_records[:num_lines_to_display]:
        row = []
        for status_column in status_columns:
            if status_column.show_by_default or show_all:
                row.append(status_column.calc(record))
        cluster_table.add_row(row)

    if cluster_records:
        if controller_name is not None:
            controller = controller_utils.Controllers.from_name(controller_name)
            if controller is None:
                raise ValueError(f'Controller {controller_name} not found.')
            controller_handle: backends.CloudVmRayResourceHandle = (
                cluster_records[0]['handle'])
            autostop_config = (
                controller_handle.launched_resources.autostop_config)
            if autostop_config is not None:
                autostop_str = (f'{colorama.Style.DIM} (will be autostopped if '
                                f'idle for {autostop_config.idle_minutes}min)'
                                f'{colorama.Style.RESET_ALL}')
            click.echo(f'\n{colorama.Fore.CYAN}{colorama.Style.BRIGHT}'
                       f'{controller_name}{colorama.Style.RESET_ALL}'
                       f'{autostop_str}')
        else:
            click.echo(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}Clusters'
                       f'{colorama.Style.RESET_ALL}')
        click.echo(cluster_table)


# Some of these lambdas are invoked on both _ClusterRecord and
# _ClusterCostReportRecord, which is okay as we guarantee the queried fields
# exist in those cases.
_get_name = (lambda cluster_record: cluster_record['name'])
_get_user_hash = (lambda cluster_record: cluster_record['user_hash'])
_get_user_name = (lambda cluster_record: cluster_record.get('user_name', '-'))
_get_launched = (lambda cluster_record: log_utils.readable_time_duration(
    cluster_record['launched_at']))
_get_region = (
    lambda clusters_status: clusters_status['handle'].launched_resources.region)
_get_command = (lambda cluster_record: cluster_record['last_use'])
_get_duration = (lambda cluster_record: log_utils.readable_time_duration(
    0, cluster_record['duration'], absolute=True))


def _get_status(cluster_record: _ClusterRecord) -> status_lib.ClusterStatus:
    return cluster_record['status']


def _get_status_colored(cluster_record: _ClusterRecord) -> str:
    return _get_status(cluster_record).colored_str()


def _get_resources(cluster_record: _ClusterRecord) -> str:
    if 'resources_str' in cluster_record:
        return cluster_record['resources_str']
    handle = cluster_record['handle']
    if isinstance(handle, backends.LocalDockerResourceHandle):
        resources_str = 'docker'
    elif isinstance(handle, backends.CloudVmRayResourceHandle):
        resources_str = resources_utils.get_readable_resources_repr(handle)
    else:
        raise ValueError(f'Unknown handle type {type(handle)} encountered.')
    return resources_str


def _get_zone(cluster_record: _ClusterRecord) -> str:
    zone_str = cluster_record['handle'].launched_resources.zone
    if zone_str is None:
        zone_str = '-'
    return zone_str


def _get_autostop(cluster_record: _ClusterRecord) -> str:
    autostop_str = ''
    separation = ''
    if cluster_record['autostop'] >= 0:
        # TODO(zhwu): check the status of the autostop cluster.
        autostop_str = str(cluster_record['autostop']) + 'm'
        separation = ' '

    if cluster_record['to_down']:
        autostop_str += f'{separation}(down)'
    if autostop_str == '':
        autostop_str = '-'
    return autostop_str


def _get_head_ip(cluster_record: _ClusterRecord) -> str:
    handle = cluster_record['handle']
    if not isinstance(handle, backends.CloudVmRayResourceHandle):
        return '-'
    if handle.head_ip is None:
        return '-'
    return handle.head_ip


def _is_pending_autostop(cluster_record: _ClusterRecord) -> bool:
    # autostop < 0 means nothing scheduled.
    return cluster_record['autostop'] >= 0 and _get_status(
        cluster_record) != status_lib.ClusterStatus.STOPPED


# ---- 'sky cost-report' helper functions below ----


def _get_status_value_for_cost_report(
        cluster_cost_report_record: _ClusterCostReportRecord) -> int:
    status = cluster_cost_report_record['status']
    if status is None:
        return -1
    return 1


def _get_status_for_cost_report(
        cluster_cost_report_record: _ClusterCostReportRecord) -> str:
    status = cluster_cost_report_record['status']
    if status is None:
        return f'{colorama.Style.DIM}TERMINATED{colorama.Style.RESET_ALL}'
    return status.colored_str()


def _get_resources_for_cost_report(
        cluster_cost_report_record: _ClusterCostReportRecord) -> str:
    launched_nodes = cluster_cost_report_record['num_nodes']
    launched_resources = cluster_cost_report_record['resources']

    launched_resource_str = str(launched_resources)
    resources_str = (f'{launched_nodes}x '
                     f'{launched_resource_str}')

    return resources_str


def _get_price_for_cost_report(
        cluster_cost_report_record: _ClusterCostReportRecord) -> str:
    launched_nodes = cluster_cost_report_record['num_nodes']
    launched_resources = cluster_cost_report_record['resources']

    hourly_cost = (launched_resources.get_cost(3600) * launched_nodes)
    price_str = f'$ {hourly_cost:.2f}'
    return price_str


def _get_estimated_cost_for_cost_report(
        cluster_cost_report_record: _ClusterCostReportRecord) -> str:
    cost = cluster_cost_report_record['total_cost']

    if not cost:
        return '-'

    return f'$ {cost:.2f}'


def show_kubernetes_cluster_status_table(
        clusters: List['kubernetes_utils.KubernetesSkyPilotClusterInfo'],
        show_all: bool) -> None:
    """Compute cluster table values and display for Kubernetes clusters."""
    status_columns = [
        StatusColumn('USER', lambda c: c.user),
        StatusColumn('NAME', lambda c: c.cluster_name),
        StatusColumn('LAUNCHED',
                     lambda c: log_utils.readable_time_duration(c.launched_at)),
        StatusColumn('RESOURCES',
                     lambda c: c.resources_str,
                     trunc_length=70 if not show_all else 0),
        StatusColumn('STATUS', lambda c: c.status.colored_str()),
        # TODO(romilb): We should consider adding POD_NAME field here when --all
        #  is passed to help users fetch pod name programmatically.
    ]

    columns = [
        col.name for col in status_columns if col.show_by_default or show_all
    ]
    cluster_table = log_utils.create_table(columns)

    # Sort table by user, then by cluster name
    sorted_clusters = sorted(clusters, key=lambda c: (c.user, c.cluster_name))

    for cluster in sorted_clusters:
        row = []
        for status_column in status_columns:
            if status_column.show_by_default or show_all:
                row.append(status_column.calc(cluster))
        cluster_table.add_row(row)

    if clusters:
        click.echo(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}'
                   f'SkyPilot clusters'
                   f'{colorama.Style.RESET_ALL}')
        click.echo(cluster_table)
    else:
        click.echo('No SkyPilot resources found in the '
                   'active Kubernetes context.')
