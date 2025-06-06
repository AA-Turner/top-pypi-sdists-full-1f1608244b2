from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from dbt_semantic_interfaces.protocols.metric import MetricTimeWindow
from dbt_semantic_interfaces.type_enums.time_granularity import TimeGranularity
from metricflow_semantics.assert_one_arg import assert_exactly_one_arg_set
from metricflow_semantics.sql.sql_exprs import (
    SqlColumnReference,
    SqlColumnReferenceExpression,
    SqlComparison,
    SqlComparisonExpression,
    SqlDateTruncExpression,
    SqlIsNullExpression,
    SqlLogicalExpression,
    SqlLogicalOperator,
    SqlSubtractTimeIntervalExpression,
)
from metricflow_semantics.sql.sql_join_type import SqlJoinType

from metricflow.dataflow.nodes.join_conversion_events import JoinConversionEventsNode
from metricflow.dataflow.nodes.join_over_time import JoinOverTimeRangeNode
from metricflow.dataflow.nodes.join_to_base import JoinDescription
from metricflow.dataflow.nodes.join_to_time_spine import JoinToTimeSpineNode
from metricflow.dataset.sql_dataset import AnnotatedSqlDataSet
from metricflow.plan_conversion.sql_expression_builders import make_coalesced_expr
from metricflow.sql.sql_plan import SqlExpressionNode, SqlJoinDescription, SqlSelectStatementNode


@dataclass(frozen=True)
class ColumnEqualityDescription:
    """Helper class to enumerate columns that should be equal between sources in a join.

    The `treat_nulls_as_equal` property determines what to do with null valued inputs. By default SQL returns
    NULL for any equality comparison with a NULL on either side, which means `NULL = NULL` returns NULL, which
    evaluates to False in the join comparison. If that parameter is overridden to True, then the column comparison
    will be rendered as:

        `(left_column_alias = right_column_alias OR (left_column_alias IS NULL AND right_column_alias IS NULL))`
    """

    left_column_alias: str
    right_column_alias: str
    treat_nulls_as_equal: bool = False


class SqlPlanJoinBuilder:
    """Helper class for constructing various join components in a SqlQueryPlan."""

    @staticmethod
    def make_column_equality_sql_join_description(
        right_source_node: SqlSelectStatementNode,
        left_source_alias: str,
        right_source_alias: str,
        column_equality_descriptions: Sequence[ColumnEqualityDescription],
        join_type: SqlJoinType,
        additional_on_conditions: Sequence[SqlExpressionNode] = tuple(),
    ) -> SqlJoinDescription:
        """Make a join description where the base condition is a set of equality comparisons between columns.

        Typically the columns in column_equality_descriptions are entities we are trying to match,
        although they may include things like dimension partitions or time dimension columns where an
        equality is expected.

        Since the framework currently supports join keys OR condition-free cross joins, this helper will require
        either a non-empty set of column equality conditions or a CROSS JOIN.

        Args:
            right_source_node: node representing the join target, may be either a table or subquery
            left_source_alias: string alias entity for the join source
            right_source_alias: string alias entity for the join target
            column_equality_descriptions: set of equality constraints for the ON statement
            join_type: type of SQL join, e.g., LEFT, INNER, etc.
            additional_on_conditions: set of additional constraints to add in the ON statement (via AND)
        """
        assert (
            len(column_equality_descriptions) > 0 or join_type is SqlJoinType.CROSS_JOIN
        ), f"No column equality conditions specified for join with type {join_type} - this may render invalid SQL!"

        and_conditions: List[SqlExpressionNode] = []
        for column_equality_description in column_equality_descriptions:
            left_column = SqlColumnReferenceExpression.create(
                SqlColumnReference(
                    table_alias=left_source_alias,
                    column_name=column_equality_description.left_column_alias,
                )
            )
            right_column = SqlColumnReferenceExpression.create(
                SqlColumnReference(
                    table_alias=right_source_alias,
                    column_name=column_equality_description.right_column_alias,
                )
            )
            column_equality_expression = SqlComparisonExpression.create(
                left_expr=left_column,
                comparison=SqlComparison.EQUALS,
                right_expr=right_column,
            )
            if column_equality_description.treat_nulls_as_equal:
                null_comparison_expression = SqlLogicalExpression.create(
                    operator=SqlLogicalOperator.AND,
                    args=(SqlIsNullExpression.create(arg=left_column), SqlIsNullExpression.create(arg=right_column)),
                )
                and_conditions.append(
                    SqlLogicalExpression.create(
                        operator=SqlLogicalOperator.OR, args=(column_equality_expression, null_comparison_expression)
                    )
                )
            else:
                and_conditions.append(column_equality_expression)

        and_conditions += additional_on_conditions

        on_condition: Optional[SqlExpressionNode]
        if len(and_conditions) == 0:
            on_condition = None
        elif len(and_conditions) == 1:
            on_condition = and_conditions[0]
        else:
            on_condition = SqlLogicalExpression.create(operator=SqlLogicalOperator.AND, args=tuple(and_conditions))

        return SqlJoinDescription(
            right_source=right_source_node,
            right_source_alias=right_source_alias,
            on_condition=on_condition,
            join_type=join_type,
        )

    @staticmethod
    def make_base_output_join_description(
        left_data_set: AnnotatedSqlDataSet,
        right_data_set: AnnotatedSqlDataSet,
        join_description: JoinDescription,
    ) -> SqlJoinDescription:
        """Make a join description to link two base output DataSets by matching entities.

        In addition to the entity equality condition, this will ensure datasets are joined on all partition
        columns and account for validity windows, if those are defined in one of the datasets.
        """
        join_on_entity = join_description.join_on_entity

        column_equality_descriptions = []
        if join_on_entity:
            # Figure out which columns in the "left" data set correspond to the entity that we want to join on.
            # The column associations tell us which columns correspond to which instances in the data set.
            left_data_set_entity_column_associations = left_data_set.data_set.column_associations_for_entity(
                join_on_entity
            )
            left_data_set_entity_cols = [c.column_name for c in left_data_set_entity_column_associations]

            # Figure out which columns in the "right" data set correspond to the entity that we want to join on.
            right_data_set_column_associations = right_data_set.data_set.column_associations_for_entity(join_on_entity)
            right_data_set_entity_cols = [c.column_name for c in right_data_set_column_associations]

            assert len(left_data_set_entity_cols) == len(right_data_set_entity_cols), (
                f"Cannot construct join - the number of columns on the left ({left_data_set_entity_cols}) side of "
                f"the join does not match the right ({right_data_set_entity_cols})"
            )

            # We have the columns that we need to "join on" in the query, so add it to the list of join descriptions to
            # use later.
            for idx in range(len(left_data_set_entity_cols)):
                column_equality_descriptions.append(
                    ColumnEqualityDescription(
                        left_column_alias=left_data_set_entity_cols[idx],
                        right_column_alias=right_data_set_entity_cols[idx],
                    )
                )

        # Add the partition columns as well.
        for dimension_join_description in join_description.join_on_partition_dimensions:
            column_equality_descriptions.append(
                ColumnEqualityDescription(
                    left_column_alias=left_data_set.data_set.column_association_for_dimension(
                        dimension_join_description.start_node_dimension_spec
                    ).column_name,
                    right_column_alias=right_data_set.data_set.column_association_for_dimension(
                        dimension_join_description.node_to_join_dimension_spec
                    ).column_name,
                )
            )

        for time_dimension_join_description in join_description.join_on_partition_time_dimensions:
            column_equality_descriptions.append(
                ColumnEqualityDescription(
                    left_column_alias=left_data_set.data_set.column_association_for_time_dimension(
                        time_dimension_join_description.start_node_time_dimension_spec
                    ).column_name,
                    right_column_alias=right_data_set.data_set.column_association_for_time_dimension(
                        time_dimension_join_description.node_to_join_time_dimension_spec
                    ).column_name,
                )
            )

        validity_conditions = SqlPlanJoinBuilder._make_validity_window_on_conditions(
            left_data_set=left_data_set, right_data_set=right_data_set, join_description=join_description
        )

        return SqlPlanJoinBuilder.make_column_equality_sql_join_description(
            right_source_node=right_data_set.data_set.checked_sql_select_node,
            left_source_alias=left_data_set.alias,
            right_source_alias=right_data_set.alias,
            column_equality_descriptions=column_equality_descriptions,
            join_type=join_description.join_type,
            additional_on_conditions=validity_conditions,
        )

    @staticmethod
    def _make_validity_window_on_conditions(
        left_data_set: AnnotatedSqlDataSet,
        right_data_set: AnnotatedSqlDataSet,
        join_description: JoinDescription,
    ) -> Tuple[SqlExpressionNode, ...]:
        """Build a time window join condition if the join description includes a validity window description.

        When the validity window is set, it means we are dealing with a dataset representing an SCD Type II
        style semantic model, with a start and end boundary on the window. A base output join against such data
        sources requires a metric_time dimension to process the join.

        By convention, the join description ties the validity window to the "right" side semantic model, and so
        we extract the metric time instance from the left data set.

        We use the instance with the smallest granularity and shortest entity link path, since it will be
        used in the ON statement for the join against the validity window.

        Note SCD joins are always evaluated against a standard time granularity. Subsequent conversion to
        custom granularities should happen after the join.
        """
        if join_description.validity_window is None:
            return tuple()

        left_data_set_metric_time_dimension_instances = sorted(
            [
                instance
                for instance in left_data_set.data_set.metric_time_dimension_instances
                if not instance.spec.time_granularity.is_custom_granularity
            ],
            key=lambda x: (x.spec.time_granularity.base_granularity.to_int(), len(x.spec.entity_links)),
        )
        assert left_data_set_metric_time_dimension_instances, (
            f"Cannot process join to data set with alias {right_data_set.alias} because it has a validity "
            f"window set: {join_description.validity_window}, but source data set with alias "
            f"{left_data_set.alias} does not have a metric time dimension we can use for the window join!"
        )
        left_data_set_time_dimension_name = left_data_set.data_set.column_association_for_time_dimension(
            left_data_set_metric_time_dimension_instances[0].spec,
        ).column_name
        window_start_dimension_name = right_data_set.data_set.column_association_for_time_dimension(
            join_description.validity_window.window_start_dimension
        ).column_name
        window_end_dimension_name = right_data_set.data_set.column_association_for_time_dimension(
            join_description.validity_window.window_end_dimension
        ).column_name
        window_join_condition = SqlPlanJoinBuilder._make_time_window_join_condition(
            left_source_alias=left_data_set.alias,
            left_source_time_dimension_name=left_data_set_time_dimension_name,
            right_source_alias=right_data_set.alias,
            window_start_dimension_name=window_start_dimension_name,
            window_end_dimension_name=window_end_dimension_name,
        )

        return (window_join_condition,)

    @staticmethod
    def _make_time_window_join_condition(
        left_source_alias: str,
        left_source_time_dimension_name: str,
        right_source_alias: str,
        window_start_dimension_name: str,
        window_end_dimension_name: str,
    ) -> SqlLogicalExpression:
        """Helper to generate a renderable SqlExpression for expressing a time window join condition.

        The output will render the following expression:

            {start_dimension_name} >= metric_time AND ({end_dimension_name} < metric_time OR {end_dimension_name} IS NULL)

        """
        left_time_column_expr = SqlColumnReferenceExpression.create(
            SqlColumnReference(table_alias=left_source_alias, column_name=left_source_time_dimension_name)
        )
        window_start_column_expr = SqlColumnReferenceExpression.create(
            SqlColumnReference(table_alias=right_source_alias, column_name=window_start_dimension_name)
        )
        window_end_column_expr = SqlColumnReferenceExpression.create(
            SqlColumnReference(table_alias=right_source_alias, column_name=window_end_dimension_name)
        )

        window_start_condition = SqlComparisonExpression.create(
            left_expr=left_time_column_expr,
            comparison=SqlComparison.GREATER_THAN_OR_EQUALS,
            right_expr=window_start_column_expr,
        )
        window_end_by_time = SqlComparisonExpression.create(
            left_expr=left_time_column_expr,
            comparison=SqlComparison.LESS_THAN,
            right_expr=window_end_column_expr,
        )
        window_end_is_null = SqlIsNullExpression.create(window_end_column_expr)
        window_end_condition = SqlLogicalExpression.create(
            operator=SqlLogicalOperator.OR, args=(window_end_by_time, window_end_is_null)
        )

        return SqlLogicalExpression.create(
            operator=SqlLogicalOperator.AND, args=(window_start_condition, window_end_condition)
        )

    @staticmethod
    def make_join_description_for_combining_datasets(
        from_data_set: AnnotatedSqlDataSet,
        join_data_set: AnnotatedSqlDataSet,
        join_type: SqlJoinType,
        column_names: Sequence[str],
        table_aliases_for_coalesce: Sequence[str],
    ) -> SqlJoinDescription:
        """Creates the sql join description for combining two separate output datasets.

        These might be combined in service of producing complete output for end user consumption, in which
        case the join type will be FULL OUTER in order to ensure all rows are included. In this case, the
        join must account for all past table aliases seen in prior joins in order to produce the final
        coalesce expression for processing the join correctly.

        Metric data sets might also be combined to serve as inputs to a derived metric, in which case the
        join type will not be a FULL OUTER, and we should use null-safe column equality comparisons with
        the relevant join type for
        """
        if join_type is SqlJoinType.FULL_OUTER:
            assert (
                len(column_names) > 0
            ), "Attempting to do a FULL OUTER JOIN to combine metrics, but no columns were provided for join keys!"
            equality_exprs = [
                SqlPlanJoinBuilder._make_equality_expression_for_full_outer_join(
                    table_aliases_for_coalesce, join_data_set.alias, colname
                )
                for colname in column_names
            ]
            on_condition = (
                SqlLogicalExpression.create(operator=SqlLogicalOperator.AND, args=tuple(equality_exprs))
                if len(equality_exprs) > 1
                else equality_exprs[0]
            )
            return SqlJoinDescription(
                right_source=join_data_set.data_set.checked_sql_select_node,
                right_source_alias=join_data_set.alias,
                on_condition=on_condition,
                join_type=join_type,
            )
        else:
            column_equality_descriptions = [
                ColumnEqualityDescription(left_column_alias=name, right_column_alias=name, treat_nulls_as_equal=True)
                for name in column_names
            ]
            return SqlPlanJoinBuilder.make_column_equality_sql_join_description(
                right_source_node=join_data_set.data_set.checked_sql_select_node,
                left_source_alias=from_data_set.alias,
                right_source_alias=join_data_set.alias,
                column_equality_descriptions=column_equality_descriptions,
                join_type=join_type,
            )

    @staticmethod
    def _make_equality_expression_for_full_outer_join(
        table_aliases_in_coalesce: Sequence[str], right_table_alias: str, column_alias: str
    ) -> SqlExpressionNode:
        """Creates an expression that can go in the ON condition when coalescing join keys with a FULL OUTER JOIN.

        e.g.

        dimension_specs = ["is_instant", "ds"]
        table_aliases_in_coalesce = ["a", "b"]
        table_alias_on_right_equality = ["c"]

        ->

        COALESCE(a.is_instant, b.is_instant) = c.is_instant
        AND COALESCE(a.ds, b.ds) = c.ds

        This is necessary for cases where 3 or more subqueries will be linked via FULL OUTER JOINs. If that happens,
        the set of join keys from subquery 3 must be compared to the join keys from both subquery 1 and subquery 2,
        otherwise duplicate rows might appear in the output.

        For example:

        table1: [('a', 10), ('b', 20)]
        table2: [('a', 100), ('c', 200)]
        table3: [('a', 1000), ('c', 2000)]

        ->

        output without COALESCE: [('a', 10, 100, 1000), ('c', NULL, 200, NULL), ('c', NULL, NULL, 2000)]
        output with COALESCE: [('a', 10, 100, 1000), ('c', NULL, 200, 2000)]

        The latter scenario consolidates the rows keyed by 'c' into a single entry.
        """
        return SqlComparisonExpression.create(
            left_expr=make_coalesced_expr(table_aliases_in_coalesce, column_alias),
            comparison=SqlComparison.EQUALS,
            right_expr=SqlColumnReferenceExpression.create(
                col_ref=SqlColumnReference(
                    table_alias=right_table_alias,
                    column_name=column_alias,
                )
            ),
        )

    @staticmethod
    def _make_time_range_window_join_condition(
        base_data_set: AnnotatedSqlDataSet,
        time_comparison_dataset: AnnotatedSqlDataSet,
        window: Optional[MetricTimeWindow] = None,
        grain_to_date: Optional[TimeGranularity] = None,
    ) -> SqlLogicalExpression:
        """Helper to generate a renderable SqlExpression for expressing a time range window join condition.

        The output will render the following expression:

            a.ds <= b.ds AND a.ds > b.ds - <window>
            If no window is present we join across all time -> "a.ds <= b.ds"
        """
        if window or grain_to_date:
            assert_exactly_one_arg_set(window=window, grain_to_date=grain_to_date)
        base_column_expr = SqlColumnReferenceExpression.create(
            SqlColumnReference(
                table_alias=base_data_set.alias,
                column_name=base_data_set.metric_time_column_name,
            )
        )
        time_comparison_column_expr = SqlColumnReferenceExpression.create(
            SqlColumnReference(
                table_alias=time_comparison_dataset.alias,
                column_name=time_comparison_dataset.metric_time_column_name,
            )
        )

        # Comparison expression against the endpoint of the cumulative time range,
        # meaning the base metrc time must always be BEFORE the comparison metric time
        end_of_range_comparison_expression = SqlComparisonExpression.create(
            left_expr=base_column_expr,
            comparison=SqlComparison.LESS_THAN_OR_EQUALS,
            right_expr=time_comparison_column_expr,
        )

        comparison_expressions: List[SqlComparisonExpression] = [end_of_range_comparison_expression]
        if window:
            start_of_range_comparison_expr = SqlComparisonExpression.create(
                left_expr=base_column_expr,
                comparison=SqlComparison.GREATER_THAN,
                right_expr=SqlSubtractTimeIntervalExpression.create(
                    arg=time_comparison_column_expr,
                    count=window.count,
                    granularity=window.granularity,
                ),
            )
            comparison_expressions.append(start_of_range_comparison_expr)
        elif grain_to_date:
            start_of_range_comparison_expr = SqlComparisonExpression.create(
                left_expr=base_column_expr,
                comparison=SqlComparison.GREATER_THAN_OR_EQUALS,
                right_expr=SqlDateTruncExpression.create(
                    arg=time_comparison_column_expr, time_granularity=grain_to_date
                ),
            )
            comparison_expressions.append(start_of_range_comparison_expr)

        return SqlLogicalExpression.create(
            operator=SqlLogicalOperator.AND,
            args=tuple(comparison_expressions),
        )

    @staticmethod
    def make_join_conversion_join_description(
        node: JoinConversionEventsNode,
        base_data_set: AnnotatedSqlDataSet,
        conversion_data_set: AnnotatedSqlDataSet,
        column_equality_descriptions: Sequence[ColumnEqualityDescription],
    ) -> SqlJoinDescription:
        """Make a join description for joining base-to-conversion data sets.

        A successful conversion is when a conversion event occurs after a corresponding base event
        under the condition of being within the time range and other conditions (such as constant properties).
        This builds the join description to satisfy all those conditions.
        """
        window_condition = SqlPlanJoinBuilder._make_time_range_window_join_condition(
            base_data_set=base_data_set,
            time_comparison_dataset=conversion_data_set,
            window=node.window,
        )
        return SqlPlanJoinBuilder.make_column_equality_sql_join_description(
            right_source_node=conversion_data_set.data_set.checked_sql_select_node,
            left_source_alias=base_data_set.alias,
            right_source_alias=conversion_data_set.alias,
            column_equality_descriptions=column_equality_descriptions,
            join_type=SqlJoinType.INNER,
            additional_on_conditions=(window_condition,),
        )

    @staticmethod
    def make_cumulative_metric_time_range_join_description(
        node: JoinOverTimeRangeNode,
        metric_data_set: AnnotatedSqlDataSet,
        time_spine_data_set: AnnotatedSqlDataSet,
    ) -> SqlJoinDescription:
        """Make a join description to connect a cumulative metric input to a time spine dataset.

        Cumulative metrics must be joined against a time spine in a backward-looking fashion, with
        a range determined by a time window (delta against metric_time) and optional cumulative grain.
        """
        cumulative_join_condition = SqlPlanJoinBuilder._make_time_range_window_join_condition(
            base_data_set=metric_data_set,
            time_comparison_dataset=time_spine_data_set,
            window=node.window,
            grain_to_date=node.grain_to_date,
        )

        return SqlJoinDescription(
            right_source=metric_data_set.data_set.checked_sql_select_node,
            right_source_alias=metric_data_set.alias,
            on_condition=cumulative_join_condition,
            join_type=SqlJoinType.INNER,
        )

    @staticmethod
    def make_join_to_time_spine_join_description(
        node: JoinToTimeSpineNode,
        time_spine_alias: str,
        agg_time_dimension_column_name: str,
        parent_sql_select_node: SqlSelectStatementNode,
        parent_alias: str,
    ) -> SqlJoinDescription:
        """Build join expression used to join a metric to a time spine dataset."""
        left_expr: SqlExpressionNode = SqlColumnReferenceExpression.create(
            col_ref=SqlColumnReference(table_alias=time_spine_alias, column_name=agg_time_dimension_column_name)
        )
        if node.offset_window:
            left_expr = SqlSubtractTimeIntervalExpression.create(
                arg=left_expr, count=node.offset_window.count, granularity=node.offset_window.granularity
            )
        elif node.offset_to_grain:
            left_expr = SqlDateTruncExpression.create(time_granularity=node.offset_to_grain, arg=left_expr)

        return SqlJoinDescription(
            right_source=parent_sql_select_node,
            right_source_alias=parent_alias,
            on_condition=SqlComparisonExpression.create(
                left_expr=left_expr,
                comparison=SqlComparison.EQUALS,
                right_expr=SqlColumnReferenceExpression.create(
                    col_ref=SqlColumnReference(table_alias=parent_alias, column_name=agg_time_dimension_column_name)
                ),
            ),
            join_type=node.join_type,
        )
