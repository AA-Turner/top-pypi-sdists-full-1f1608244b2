import dataclasses
import json
import os
import re
import traceback
from pathlib import Path
from typing import List, Optional, Union

from chalk._lsp.error_builder import LSPErrorBuilder
from chalk._monitoring.Chart import Chart
from chalk._monitoring.gql_conversion import convert_chart
from chalk._version import __version__
from chalk.config.project_config import ProjectSettings, load_project_config
from chalk.features import FeatureSetBase
from chalk.features.resolver import RESOLVER_REGISTRY
from chalk.importer import CHALK_IMPORTER, FailedImport
from chalk.parsed._graph_validation import validate_graph
from chalk.parsed.duplicate_input_gql import (
    ChalkPYInfo,
    CreateChartGQL,
    EnvironmentSettingsGQL,
    FeatureClassGQL,
    FeatureSettings,
    LspGQL,
    MetadataSettings,
    ProjectSettingsGQL,
    PublishDiagnosticsParams,
    ResolverSettings,
    UpsertCronQueryGQL,
    UpsertGraphGQL,
    UpsertNamedQueryGQL,
    UpsertResolverGQL,
    UpsertSinkResolverGQL,
    UpsertSQLSourceGQL,
    UpsertStreamResolverGQL,
    ValidationSettings,
)
from chalk.parsed.json_conversions import convert_type_to_gql, gather_cdc_sources
from chalk.queries.named_query import NAMED_QUERY_REGISTRY
from chalk.queries.scheduled_query import CRON_QUERY_REGISTRY
from chalk.sql._internal.sql_source import BaseSQLSource
from chalk.utils import paths
from chalk.utils.paths import get_directory_root


def _is_relative_to(x: Path, other: Path) -> bool:
    try:
        x.relative_to(other)
        return True
    except ValueError:
        return False


def project_settings_to_gql(config: ProjectSettings) -> ProjectSettingsGQL:
    def read_packages(filename: str) -> Optional[List[str]]:
        reqs = list()
        try:
            with open(filename) as f:
                for r in f.readlines():
                    cleaned = re.sub("#.*", "", r).rstrip("\n").strip()
                    if cleaned != "":
                        reqs.append(cleaned)
            return reqs
        except OSError:
            return None

    return ProjectSettingsGQL(
        project=config.project,
        environments=(
            None
            if config.environments is None
            else [
                EnvironmentSettingsGQL(
                    id=i,
                    runtime=e.runtime,
                    requirements=e.requirements,
                    dockerfile=e.dockerfile,
                    requiresPackages=(
                        None
                        if e.requirements is None
                        else read_packages(
                            os.path.join(
                                os.path.dirname(config.local_path),
                                e.requirements,
                            )
                        )
                    ),
                    platformVersion=e.platform_version,
                )
                for i, e in config.environments.items()
            ]
        ),
        validation=(
            ValidationSettings(
                feature=(
                    FeatureSettings(
                        metadata=(
                            [
                                MetadataSettings(name=m.name, missing=m.missing)
                                for m in config.validation.feature.metadata
                            ]
                            if config.validation.feature.metadata
                            else None
                        )
                    )
                    if config.validation.feature
                    else None
                ),
                resolver=(
                    ResolverSettings(
                        metadata=(
                            [
                                MetadataSettings(name=m.name, missing=m.missing)
                                for m in config.validation.resolver.metadata
                            ]
                            if config.validation.resolver.metadata
                            else None
                        )
                    )
                    if config.validation.resolver
                    else None
                ),
            )
            if config.validation
            else None
        ),
    )


def get_registered_types(scope_to: Path, failed: List[FailedImport]) -> UpsertGraphGQL:
    features = []
    feature_classes: list[FeatureClassGQL] = []
    for x in FeatureSetBase.registry.values():
        cls_path = paths.get_classpath(x)
        if cls_path is not None and _is_relative_to(cls_path, scope_to):
            try:
                feature_classes.append(convert_type_to_gql(x))
            except Exception as e:
                failed.append(build_failed_import(e, f"feature class '{x.namespace}'"))
                continue
            try:
                for feature in x.features:
                    if not feature.is_autogenerated and not feature.no_display:
                        try:
                            converted = convert_type_to_gql(feature)
                            features.append(converted)
                        except Exception as e:
                            if not LSPErrorBuilder.promote_exception(e):
                                failed.append(build_failed_import(e, f"feature '{feature.fqn}'"))
            except Exception as e:
                if not LSPErrorBuilder.promote_exception(e):
                    failed.append(build_failed_import(e, f"feature class '{x.namespace}'"))
    project_path = get_directory_root()
    path_prefix_to_remove = project_path.as_posix() if project_path is not None else None

    stream_resolvers: list[UpsertStreamResolverGQL] = []
    for stream in RESOLVER_REGISTRY.get_stream_resolvers():
        if _is_relative_to(Path(stream.filename), scope_to):
            try:
                stream_resolvers.append(convert_type_to_gql(stream, path_prefix=path_prefix_to_remove))
            except Exception as e:
                failed.append(build_failed_import(e, f"streaming resolver '{stream.fqn}'"))

    resolvers: list[UpsertResolverGQL] = []
    for resolver in RESOLVER_REGISTRY.get_online_and_offline_resolvers():
        if _is_relative_to(Path(resolver.filename), scope_to):
            try:
                resolvers.append(convert_type_to_gql(resolver, path_prefix=path_prefix_to_remove))
            except Exception as e:
                if not LSPErrorBuilder.promote_exception(e):
                    failed.append(build_failed_import(e, f"resolver '{resolver.fqn}'"))

    sink_resolvers: list[UpsertSinkResolverGQL] = []
    for sink in RESOLVER_REGISTRY.get_sink_resolvers():
        if _is_relative_to(Path(sink.filename), scope_to):
            try:
                sink_resolvers.append(convert_type_to_gql(sink, path_prefix=path_prefix_to_remove))
            except Exception as e:
                failed.append(build_failed_import(e, f"sink resolver '{sink.fqn}'"))

    cron_queries: list[UpsertCronQueryGQL] = []
    for cron_query in CRON_QUERY_REGISTRY.values():
        if _is_relative_to(Path(cron_query.filename), scope_to):
            try:
                cron_queries.append(convert_type_to_gql(cron_query, path_prefix=path_prefix_to_remove))
            except Exception as e:
                failed.append(build_failed_import(e, f"cron query '{cron_query.name}'"))

    named_queries: list[UpsertNamedQueryGQL] = []
    for named_query in NAMED_QUERY_REGISTRY.values():
        named_query.input
        named_query.output
        if named_query.filename and _is_relative_to(Path(named_query.filename), scope_to):
            try:
                named_queries.append(convert_type_to_gql(named_query, path_prefix=path_prefix_to_remove))
            except Exception as e:
                failed.append(build_failed_import(e, f"named query '{named_query.name}'"))

    charts: list[CreateChartGQL] = []
    for chart in Chart.registry:
        try:
            charts.append(convert_chart(chart))
        except Exception as e:
            failed.append(build_failed_import(e, f"chart ' {chart.name}'"))

    config = load_project_config()
    if config is not None:
        config = project_settings_to_gql(config)

    graph = UpsertGraphGQL(
        streams=stream_resolvers,
        sinks=sink_resolvers,
        features=features,
        config=config,
        failed=failed,
        resolvers=resolvers,
        cronQueries=cron_queries,
        namedQueries=named_queries,
        charts=charts,
        chalkpy=ChalkPYInfo(
            version=__version__,
        ),
        cdcSources=gather_cdc_sources(),
        sqlSources=[
            UpsertSQLSourceGQL(
                name=source.name,
                kind=source.kind,
            )
            for source in BaseSQLSource.registry
        ],
        featureClasses=feature_classes,
    )
    errors = validate_graph(graph)
    graph.errors = errors

    # Validating the graph produces errors, so do this part last.
    lsp = get_lsp_gql()
    if LSPErrorBuilder.lsp:
        try:
            lsp.diagnostics = CHALK_IMPORTER.supplement_diagnostics(failed_imports=failed, diagnostics=lsp.diagnostics)
        except Exception as e:
            if len(lsp.diagnostics) == 0 and len(failed) == 0:
                raise e

    graph.lsp = lsp

    return graph


def get_lsp_gql() -> LspGQL:
    return LspGQL(
        diagnostics=[
            PublishDiagnosticsParams(
                uri=filename,
                diagnostics=diagnostics,
            )
            for filename, diagnostics in LSPErrorBuilder.all_errors.items()
        ],
        actions=LSPErrorBuilder.all_edits,
    )


def build_failed_import(error: Union[Exception, str], description: str) -> FailedImport:
    try:
        formatted_tb = error if isinstance(error, str) else "\n".join(traceback.format_exception(error))
    except:
        formatted_tb = (
            error
            if isinstance(error, str)
            else "\n".join(
                traceback.format_exception(
                    type(error),
                    value=error,
                    tb=None,
                )
            )
        )

    return FailedImport(
        filename="",
        module="",
        traceback=f"EXCEPTION in parsing {description}:\n{formatted_tb}",
    )


def get_registered_types_as_json(scope_to: Path, failed: List[FailedImport], indent: int = 2) -> str:
    return json.dumps(
        dataclasses.asdict(get_registered_types(scope_to, failed)),
        indent=indent,
    )
