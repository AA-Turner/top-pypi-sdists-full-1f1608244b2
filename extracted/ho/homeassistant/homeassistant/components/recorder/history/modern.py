"""Provide pre-made queries on top of the recorder component."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from typing import TYPE_CHECKING, Any, cast

from sqlalchemy import (
    CompoundSelect,
    Select,
    StatementLambdaElement,
    Subquery,
    and_,
    func,
    lambda_stmt,
    literal,
    select,
    union_all,
)
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.session import Session

from homeassistant.const import COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE
from homeassistant.core import HomeAssistant, State, split_entity_id
from homeassistant.helpers.recorder import get_instance
from homeassistant.util import dt as dt_util
from homeassistant.util.collection import chunked_or_all

from ..const import LAST_REPORTED_SCHEMA_VERSION, MAX_IDS_FOR_INDEXED_GROUP_BY
from ..db_schema import (
    SHARED_ATTR_OR_LEGACY_ATTRIBUTES,
    StateAttributes,
    States,
    StatesMeta,
)
from ..filters import Filters
from ..models import (
    LazyState,
    datetime_to_timestamp_or_none,
    extract_metadata_ids,
    row_to_compressed_state,
)
from ..util import execute_stmt_lambda_element, session_scope
from .const import (
    LAST_CHANGED_KEY,
    NEED_ATTRIBUTE_DOMAINS,
    SIGNIFICANT_DOMAINS,
    STATE_KEY,
)

_FIELD_MAP = {
    "metadata_id": 0,
    "state": 1,
    "last_updated_ts": 2,
}


def _stmt_and_join_attributes(
    no_attributes: bool,
    include_last_changed: bool,
    include_last_reported: bool,
) -> Select:
    """Return the statement and if StateAttributes should be joined."""
    _select = select(States.metadata_id, States.state, States.last_updated_ts)
    if include_last_changed:
        _select = _select.add_columns(States.last_changed_ts)
    if include_last_reported:
        _select = _select.add_columns(States.last_reported_ts)
    if not no_attributes:
        _select = _select.add_columns(SHARED_ATTR_OR_LEGACY_ATTRIBUTES)
    return _select


def _stmt_and_join_attributes_for_start_state(
    no_attributes: bool,
    include_last_changed: bool,
    include_last_reported: bool,
) -> Select:
    """Return the statement and if StateAttributes should be joined."""
    _select = select(States.metadata_id, States.state)
    _select = _select.add_columns(literal(value=0).label("last_updated_ts"))
    if include_last_changed:
        _select = _select.add_columns(literal(value=0).label("last_changed_ts"))
    if include_last_reported:
        _select = _select.add_columns(literal(value=0).label("last_reported_ts"))
    if not no_attributes:
        _select = _select.add_columns(SHARED_ATTR_OR_LEGACY_ATTRIBUTES)
    return _select


def _select_from_subquery(
    subquery: Subquery | CompoundSelect,
    no_attributes: bool,
    include_last_changed: bool,
    include_last_reported: bool,
) -> Select:
    """Return the statement to select from the union."""
    base_select = select(
        subquery.c.metadata_id,
        subquery.c.state,
        subquery.c.last_updated_ts,
    )
    if include_last_changed:
        base_select = base_select.add_columns(subquery.c.last_changed_ts)
    if include_last_reported:
        base_select = base_select.add_columns(subquery.c.last_reported_ts)
    if no_attributes:
        return base_select
    return base_select.add_columns(subquery.c.attributes)


def get_significant_states(
    hass: HomeAssistant,
    start_time: datetime,
    end_time: datetime | None = None,
    entity_ids: list[str] | None = None,
    filters: Filters | None = None,
    include_start_time_state: bool = True,
    significant_changes_only: bool = True,
    minimal_response: bool = False,
    no_attributes: bool = False,
    compressed_state_format: bool = False,
) -> dict[str, list[State | dict[str, Any]]]:
    """Wrap get_significant_states_with_session with an sql session."""
    with session_scope(hass=hass, read_only=True) as session:
        return get_significant_states_with_session(
            hass,
            session,
            start_time,
            end_time,
            entity_ids,
            filters,
            include_start_time_state,
            significant_changes_only,
            minimal_response,
            no_attributes,
            compressed_state_format,
        )


def _significant_states_stmt(
    start_time_ts: float,
    end_time_ts: float | None,
    single_metadata_id: int | None,
    metadata_ids: list[int],
    metadata_ids_in_significant_domains: list[int],
    significant_changes_only: bool,
    no_attributes: bool,
    include_start_time_state: bool,
    run_start_ts: float | None,
    slow_dependent_subquery: bool,
) -> Select | CompoundSelect:
    """Query the database for significant state changes."""
    include_last_changed = not significant_changes_only
    stmt = _stmt_and_join_attributes(no_attributes, include_last_changed, False)
    if significant_changes_only:
        # Since we are filtering on entity_id (metadata_id) we can avoid
        # the join of the states_meta table since we already know which
        # metadata_ids are in the significant domains.
        if metadata_ids_in_significant_domains:
            stmt = stmt.filter(
                States.metadata_id.in_(metadata_ids_in_significant_domains)
                | (States.last_changed_ts == States.last_updated_ts)
                | States.last_changed_ts.is_(None)
            )
        else:
            stmt = stmt.filter(
                (States.last_changed_ts == States.last_updated_ts)
                | States.last_changed_ts.is_(None)
            )
    stmt = stmt.filter(States.metadata_id.in_(metadata_ids)).filter(
        States.last_updated_ts > start_time_ts
    )
    if end_time_ts:
        stmt = stmt.filter(States.last_updated_ts < end_time_ts)
    if not no_attributes:
        stmt = stmt.outerjoin(
            StateAttributes, States.attributes_id == StateAttributes.attributes_id
        )
    if not include_start_time_state or not run_start_ts:
        return stmt.order_by(States.metadata_id, States.last_updated_ts)
    unioned_subquery = union_all(
        _select_from_subquery(
            _get_start_time_state_stmt(
                start_time_ts,
                single_metadata_id,
                metadata_ids,
                no_attributes,
                include_last_changed,
                slow_dependent_subquery,
            ).subquery(),
            no_attributes,
            include_last_changed,
            False,
        ),
        _select_from_subquery(
            stmt.subquery(), no_attributes, include_last_changed, False
        ),
    ).subquery()
    return _select_from_subquery(
        unioned_subquery,
        no_attributes,
        include_last_changed,
        False,
    ).order_by(unioned_subquery.c.metadata_id, unioned_subquery.c.last_updated_ts)


def get_significant_states_with_session(
    hass: HomeAssistant,
    session: Session,
    start_time: datetime,
    end_time: datetime | None = None,
    entity_ids: list[str] | None = None,
    filters: Filters | None = None,
    include_start_time_state: bool = True,
    significant_changes_only: bool = True,
    minimal_response: bool = False,
    no_attributes: bool = False,
    compressed_state_format: bool = False,
) -> dict[str, list[State | dict[str, Any]]]:
    """Return states changes during UTC period start_time - end_time.

    entity_ids is an optional iterable of entities to include in the results.

    filters is an optional SQLAlchemy filter which will be applied to the database
    queries unless entity_ids is given, in which case its ignored.

    Significant states are all states where there is a state change,
    as well as all states from certain domains (for instance
    thermostat so that we get current temperature in our graphs).
    """
    if filters is not None:
        raise NotImplementedError("Filters are no longer supported")
    if not entity_ids:
        raise ValueError("entity_ids must be provided")
    entity_id_to_metadata_id: dict[str, int | None] | None = None
    metadata_ids_in_significant_domains: list[int] = []
    instance = get_instance(hass)
    if not (
        entity_id_to_metadata_id := instance.states_meta_manager.get_many(
            entity_ids, session, False
        )
    ) or not (possible_metadata_ids := extract_metadata_ids(entity_id_to_metadata_id)):
        return {}
    metadata_ids = possible_metadata_ids
    if significant_changes_only:
        metadata_ids_in_significant_domains = [
            metadata_id
            for entity_id, metadata_id in entity_id_to_metadata_id.items()
            if metadata_id is not None
            and split_entity_id(entity_id)[0] in SIGNIFICANT_DOMAINS
        ]
    oldest_ts: float | None = None
    if include_start_time_state and not (
        oldest_ts := _get_oldest_possible_ts(hass, start_time)
    ):
        include_start_time_state = False
    start_time_ts = start_time.timestamp()
    end_time_ts = datetime_to_timestamp_or_none(end_time)
    single_metadata_id = metadata_ids[0] if len(metadata_ids) == 1 else None
    rows: list[Row] = []
    if TYPE_CHECKING:
        assert instance.database_engine is not None
    slow_dependent_subquery = instance.database_engine.optimizer.slow_dependent_subquery
    if include_start_time_state and slow_dependent_subquery:
        # https://github.com/home-assistant/core/issues/137178
        # If we include the start time state we need to limit the
        # number of metadata_ids we query for at a time to avoid
        # hitting limits in the MySQL optimizer that prevent
        # the start time state query from using an index-only optimization
        # to find the start time state.
        iter_metadata_ids = chunked_or_all(metadata_ids, MAX_IDS_FOR_INDEXED_GROUP_BY)
    else:
        iter_metadata_ids = (metadata_ids,)
    for metadata_ids_chunk in iter_metadata_ids:
        stmt = _generate_significant_states_with_session_stmt(
            start_time_ts,
            end_time_ts,
            single_metadata_id,
            metadata_ids_chunk,
            metadata_ids_in_significant_domains,
            significant_changes_only,
            no_attributes,
            include_start_time_state,
            oldest_ts,
            slow_dependent_subquery,
        )
        row_chunk = cast(
            list[Row],
            execute_stmt_lambda_element(session, stmt, None, end_time, orm_rows=False),
        )
        if rows:
            rows += row_chunk
        else:
            # If we have no rows yet, we can just assign the chunk
            # as this is the common case since its rare that
            # we exceed the MAX_IDS_FOR_INDEXED_GROUP_BY limit
            rows = row_chunk
    return _sorted_states_to_dict(
        rows,
        start_time_ts if include_start_time_state else None,
        entity_ids,
        entity_id_to_metadata_id,
        minimal_response,
        compressed_state_format,
        no_attributes=no_attributes,
    )


def _generate_significant_states_with_session_stmt(
    start_time_ts: float,
    end_time_ts: float | None,
    single_metadata_id: int | None,
    metadata_ids: list[int],
    metadata_ids_in_significant_domains: list[int],
    significant_changes_only: bool,
    no_attributes: bool,
    include_start_time_state: bool,
    oldest_ts: float | None,
    slow_dependent_subquery: bool,
) -> StatementLambdaElement:
    return lambda_stmt(
        lambda: _significant_states_stmt(
            start_time_ts,
            end_time_ts,
            single_metadata_id,
            metadata_ids,
            metadata_ids_in_significant_domains,
            significant_changes_only,
            no_attributes,
            include_start_time_state,
            oldest_ts,
            slow_dependent_subquery,
        ),
        track_on=[
            bool(single_metadata_id),
            bool(metadata_ids_in_significant_domains),
            bool(end_time_ts),
            significant_changes_only,
            no_attributes,
            include_start_time_state,
            slow_dependent_subquery,
        ],
    )


def get_full_significant_states_with_session(
    hass: HomeAssistant,
    session: Session,
    start_time: datetime,
    end_time: datetime | None = None,
    entity_ids: list[str] | None = None,
    filters: Filters | None = None,
    include_start_time_state: bool = True,
    significant_changes_only: bool = True,
    no_attributes: bool = False,
) -> dict[str, list[State]]:
    """Variant of get_significant_states_with_session.

    Difference with get_significant_states_with_session is that it does not
    return minimal responses.
    """
    return cast(
        dict[str, list[State]],
        get_significant_states_with_session(
            hass=hass,
            session=session,
            start_time=start_time,
            end_time=end_time,
            entity_ids=entity_ids,
            filters=filters,
            include_start_time_state=include_start_time_state,
            significant_changes_only=significant_changes_only,
            minimal_response=False,
            no_attributes=no_attributes,
        ),
    )


def _state_changed_during_period_stmt(
    start_time_ts: float,
    end_time_ts: float | None,
    single_metadata_id: int,
    no_attributes: bool,
    limit: int | None,
    include_start_time_state: bool,
    run_start_ts: float | None,
    include_last_reported: bool,
) -> Select | CompoundSelect:
    stmt = (
        _stmt_and_join_attributes(no_attributes, False, include_last_reported)
        .filter(
            (
                (States.last_changed_ts == States.last_updated_ts)
                | States.last_changed_ts.is_(None)
            )
            & (States.last_updated_ts > start_time_ts)
        )
        .filter(States.metadata_id == single_metadata_id)
    )
    if end_time_ts:
        stmt = stmt.filter(States.last_updated_ts < end_time_ts)
    if not no_attributes:
        stmt = stmt.outerjoin(
            StateAttributes, States.attributes_id == StateAttributes.attributes_id
        )
    if limit:
        stmt = stmt.limit(limit)
    stmt = stmt.order_by(States.metadata_id, States.last_updated_ts)
    if not include_start_time_state or not run_start_ts:
        # If we do not need the start time state or the
        # oldest possible timestamp is newer than the start time
        # we can return the statement as is as there will
        # never be a start time state.
        return stmt
    return _select_from_subquery(
        union_all(
            _select_from_subquery(
                _get_single_entity_start_time_stmt(
                    start_time_ts,
                    single_metadata_id,
                    no_attributes,
                    False,
                    include_last_reported,
                ).subquery(),
                no_attributes,
                False,
                include_last_reported,
            ),
            _select_from_subquery(
                stmt.subquery(),
                no_attributes,
                False,
                include_last_reported,
            ),
        ).subquery(),
        no_attributes,
        False,
        include_last_reported,
    )


def state_changes_during_period(
    hass: HomeAssistant,
    start_time: datetime,
    end_time: datetime | None = None,
    entity_id: str | None = None,
    no_attributes: bool = False,
    descending: bool = False,
    limit: int | None = None,
    include_start_time_state: bool = True,
) -> dict[str, list[State]]:
    """Return states changes during UTC period start_time - end_time."""
    has_last_reported = (
        get_instance(hass).schema_version >= LAST_REPORTED_SCHEMA_VERSION
    )
    if not entity_id:
        raise ValueError("entity_id must be provided")
    entity_ids = [entity_id.lower()]

    with session_scope(hass=hass, read_only=True) as session:
        instance = get_instance(hass)
        if not (
            possible_metadata_id := instance.states_meta_manager.get(
                entity_id, session, False
            )
        ):
            return {}
        single_metadata_id = possible_metadata_id
        entity_id_to_metadata_id: dict[str, int | None] = {
            entity_id: single_metadata_id
        }
        oldest_ts: float | None = None
        if include_start_time_state and not (
            oldest_ts := _get_oldest_possible_ts(hass, start_time)
        ):
            include_start_time_state = False
        start_time_ts = start_time.timestamp()
        end_time_ts = datetime_to_timestamp_or_none(end_time)
        stmt = lambda_stmt(
            lambda: _state_changed_during_period_stmt(
                start_time_ts,
                end_time_ts,
                single_metadata_id,
                no_attributes,
                limit,
                include_start_time_state,
                oldest_ts,
                has_last_reported,
            ),
            track_on=[
                bool(end_time_ts),
                no_attributes,
                bool(limit),
                include_start_time_state,
                has_last_reported,
            ],
        )
        return cast(
            dict[str, list[State]],
            _sorted_states_to_dict(
                execute_stmt_lambda_element(
                    session, stmt, None, end_time, orm_rows=False
                ),
                start_time_ts if include_start_time_state else None,
                entity_ids,
                entity_id_to_metadata_id,
                descending=descending,
                no_attributes=no_attributes,
            ),
        )


def _get_last_state_changes_single_stmt(metadata_id: int) -> Select:
    return (
        _stmt_and_join_attributes(False, False, False)
        .join(
            (
                lastest_state_for_metadata_id := (
                    select(
                        States.metadata_id.label("max_metadata_id"),
                        func.max(States.last_updated_ts).label("max_last_updated"),
                    )
                    .filter(States.metadata_id == metadata_id)
                    .group_by(States.metadata_id)
                    .subquery()
                )
            ),
            and_(
                States.metadata_id == lastest_state_for_metadata_id.c.max_metadata_id,
                States.last_updated_ts
                == lastest_state_for_metadata_id.c.max_last_updated,
            ),
        )
        .outerjoin(
            StateAttributes, States.attributes_id == StateAttributes.attributes_id
        )
        .order_by(States.state_id.desc())
    )


def _get_last_state_changes_multiple_stmt(
    number_of_states: int, metadata_id: int, include_last_reported: bool
) -> Select:
    return (
        _stmt_and_join_attributes(False, False, include_last_reported)
        .where(
            States.state_id
            == (
                select(States.state_id)
                .filter(States.metadata_id == metadata_id)
                .order_by(States.last_updated_ts.desc())
                .limit(number_of_states)
                .subquery()
            ).c.state_id
        )
        .outerjoin(
            StateAttributes, States.attributes_id == StateAttributes.attributes_id
        )
        .order_by(States.state_id.desc())
    )


def get_last_state_changes(
    hass: HomeAssistant, number_of_states: int, entity_id: str
) -> dict[str, list[State]]:
    """Return the last number_of_states."""
    has_last_reported = (
        get_instance(hass).schema_version >= LAST_REPORTED_SCHEMA_VERSION
    )
    entity_id_lower = entity_id.lower()
    entity_ids = [entity_id_lower]

    # Calling this function with number_of_states > 1 can cause instability
    # because it has to scan the table to find the last number_of_states states
    # because the metadata_id_last_updated_ts index is in ascending order.

    with session_scope(hass=hass, read_only=True) as session:
        instance = get_instance(hass)
        if not (
            possible_metadata_id := instance.states_meta_manager.get(
                entity_id, session, False
            )
        ):
            return {}
        metadata_id = possible_metadata_id
        entity_id_to_metadata_id: dict[str, int | None] = {entity_id_lower: metadata_id}
        if number_of_states == 1:
            stmt = lambda_stmt(
                lambda: _get_last_state_changes_single_stmt(metadata_id),
            )
        else:
            stmt = lambda_stmt(
                lambda: _get_last_state_changes_multiple_stmt(
                    number_of_states, metadata_id, has_last_reported
                ),
                track_on=[has_last_reported],
            )
        states = list(execute_stmt_lambda_element(session, stmt, orm_rows=False))
        return cast(
            dict[str, list[State]],
            _sorted_states_to_dict(
                reversed(states),
                None,
                entity_ids,
                entity_id_to_metadata_id,
                no_attributes=False,
            ),
        )


def _get_start_time_state_for_entities_stmt_dependent_sub_query(
    epoch_time: float,
    metadata_ids: list[int],
    no_attributes: bool,
    include_last_changed: bool,
) -> Select:
    """Baked query to get states for specific entities."""
    # Engine has a fast dependent subquery optimizer
    # This query is the result of significant research in
    # https://github.com/home-assistant/core/issues/132865
    # A reverse index scan with a limit 1 is the fastest way to get the
    # last state change before a specific point in time for all supported
    # databases. Since all databases support this query as a join
    # condition we can use it as a subquery to get the last state change
    # before a specific point in time for all entities.
    stmt = (
        _stmt_and_join_attributes_for_start_state(
            no_attributes=no_attributes,
            include_last_changed=include_last_changed,
            include_last_reported=False,
        )
        .select_from(StatesMeta)
        .join(
            States,
            and_(
                States.last_updated_ts
                == (
                    select(States.last_updated_ts)
                    .where(
                        (StatesMeta.metadata_id == States.metadata_id)
                        & (States.last_updated_ts < epoch_time)
                    )
                    .order_by(States.last_updated_ts.desc())
                    .limit(1)
                )
                .scalar_subquery()
                .correlate(StatesMeta),
                States.metadata_id == StatesMeta.metadata_id,
            ),
        )
        .where(StatesMeta.metadata_id.in_(metadata_ids))
    )
    if no_attributes:
        return stmt
    return stmt.outerjoin(
        StateAttributes, (States.attributes_id == StateAttributes.attributes_id)
    )


def _get_start_time_state_for_entities_stmt_group_by(
    epoch_time: float,
    metadata_ids: list[int],
    no_attributes: bool,
    include_last_changed: bool,
) -> Select:
    """Baked query to get states for specific entities."""
    # Simple group-by for MySQL, must use less
    # than 1000 metadata_ids in the IN clause for MySQL
    # or it will optimize poorly. Callers are responsible
    # for ensuring that the number of metadata_ids is less
    # than 1000.
    most_recent_states_for_entities_by_date = (
        select(
            States.metadata_id.label("max_metadata_id"),
            func.max(States.last_updated_ts).label("max_last_updated"),
        )
        .filter(
            (States.last_updated_ts < epoch_time) & States.metadata_id.in_(metadata_ids)
        )
        .group_by(States.metadata_id)
        .subquery()
    )
    stmt = (
        _stmt_and_join_attributes_for_start_state(
            no_attributes=no_attributes,
            include_last_changed=include_last_changed,
            include_last_reported=False,
        )
        .join(
            most_recent_states_for_entities_by_date,
            and_(
                States.metadata_id
                == most_recent_states_for_entities_by_date.c.max_metadata_id,
                States.last_updated_ts
                == most_recent_states_for_entities_by_date.c.max_last_updated,
            ),
        )
        .filter(
            (States.last_updated_ts < epoch_time) & States.metadata_id.in_(metadata_ids)
        )
    )
    if no_attributes:
        return stmt
    return stmt.outerjoin(
        StateAttributes, (States.attributes_id == StateAttributes.attributes_id)
    )


def _get_oldest_possible_ts(
    hass: HomeAssistant, utc_point_in_time: datetime
) -> float | None:
    """Return the oldest possible timestamp.

    Returns None if there are no states as old as utc_point_in_time.
    """

    oldest_ts = get_instance(hass).states_manager.oldest_ts
    if oldest_ts is not None and oldest_ts < utc_point_in_time.timestamp():
        return oldest_ts
    return None


def _get_start_time_state_stmt(
    epoch_time: float,
    single_metadata_id: int | None,
    metadata_ids: list[int],
    no_attributes: bool,
    include_last_changed: bool,
    slow_dependent_subquery: bool,
) -> Select:
    """Return the states at a specific point in time."""
    if single_metadata_id:
        # Use an entirely different (and extremely fast) query if we only
        # have a single entity id
        return _get_single_entity_start_time_stmt(
            epoch_time,
            single_metadata_id,
            no_attributes,
            include_last_changed,
            False,
        )
    # We have more than one entity to look at so we need to do a query on states
    # since the last recorder run started.
    if slow_dependent_subquery:
        return _get_start_time_state_for_entities_stmt_group_by(
            epoch_time,
            metadata_ids,
            no_attributes,
            include_last_changed,
        )

    return _get_start_time_state_for_entities_stmt_dependent_sub_query(
        epoch_time,
        metadata_ids,
        no_attributes,
        include_last_changed,
    )


def _get_single_entity_start_time_stmt(
    epoch_time: float,
    metadata_id: int,
    no_attributes: bool,
    include_last_changed: bool,
    include_last_reported: bool,
) -> Select:
    # Use an entirely different (and extremely fast) query if we only
    # have a single entity id
    stmt = (
        _stmt_and_join_attributes_for_start_state(
            no_attributes, include_last_changed, include_last_reported
        )
        .filter(
            States.last_updated_ts < epoch_time,
            States.metadata_id == metadata_id,
        )
        .order_by(States.last_updated_ts.desc())
        .limit(1)
    )
    if no_attributes:
        return stmt
    return stmt.outerjoin(
        StateAttributes, States.attributes_id == StateAttributes.attributes_id
    )


def _sorted_states_to_dict(
    states: Iterable[Row],
    start_time_ts: float | None,
    entity_ids: list[str],
    entity_id_to_metadata_id: dict[str, int | None],
    minimal_response: bool = False,
    compressed_state_format: bool = False,
    descending: bool = False,
    no_attributes: bool = False,
) -> dict[str, list[State | dict[str, Any]]]:
    """Convert SQL results into JSON friendly data structure.

    This takes our state list and turns it into a JSON friendly data
    structure {'entity_id': [list of states], 'entity_id2': [list of states]}

    States must be sorted by entity_id and last_updated

    We also need to go back and create a synthetic zero data point for
    each list of states, otherwise our graphs won't start on the Y
    axis correctly.
    """
    field_map = _FIELD_MAP
    state_class: Callable[
        [Row, dict[str, dict[str, Any]], float | None, str, str, float | None, bool],
        State | dict[str, Any],
    ]
    if compressed_state_format:
        state_class = row_to_compressed_state
        attr_time = COMPRESSED_STATE_LAST_UPDATED
        attr_state = COMPRESSED_STATE_STATE
    else:
        state_class = LazyState
        attr_time = LAST_CHANGED_KEY
        attr_state = STATE_KEY

    # Set all entity IDs to empty lists in result set to maintain the order
    result: dict[str, list[State | dict[str, Any]]] = {
        entity_id: [] for entity_id in entity_ids
    }
    metadata_id_to_entity_id: dict[int, str] = {}
    metadata_id_to_entity_id = {
        v: k for k, v in entity_id_to_metadata_id.items() if v is not None
    }
    # Get the states at the start time
    if len(entity_ids) == 1:
        metadata_id = entity_id_to_metadata_id[entity_ids[0]]
        assert metadata_id is not None  # should not be possible if we got here
        states_iter: Iterable[tuple[int, Iterator[Row]]] = (
            (metadata_id, iter(states)),
        )
    else:
        key_func = itemgetter(field_map["metadata_id"])
        states_iter = groupby(states, key_func)

    state_idx = field_map["state"]
    last_updated_ts_idx = field_map["last_updated_ts"]

    # Append all changes to it
    for metadata_id, group in states_iter:
        entity_id = metadata_id_to_entity_id[metadata_id]
        attr_cache: dict[str, dict[str, Any]] = {}
        ent_results = result[entity_id]
        if (
            not minimal_response
            or split_entity_id(entity_id)[0] in NEED_ATTRIBUTE_DOMAINS
        ):
            ent_results.extend(
                [
                    state_class(
                        db_state,
                        attr_cache,
                        start_time_ts,
                        entity_id,
                        db_state[state_idx],
                        db_state[last_updated_ts_idx],
                        False,
                    )
                    for db_state in group
                ]
            )
            continue

        prev_state: str | None = None
        # With minimal response we only provide a native
        # State for the first and last response. All the states
        # in-between only provide the "state" and the
        # "last_changed".
        if not ent_results:
            if (first_state := next(group, None)) is None:
                continue
            prev_state = first_state[state_idx]
            ent_results.append(
                state_class(
                    first_state,
                    attr_cache,
                    start_time_ts,
                    entity_id,
                    prev_state,
                    first_state[last_updated_ts_idx],
                    no_attributes,
                )
            )

        #
        # minimal_response only makes sense with last_updated == last_updated
        #
        # We use last_updated for for last_changed since its the same
        #
        # With minimal response we do not care about attribute
        # changes so we can filter out duplicate states
        if compressed_state_format:
            # Compressed state format uses the timestamp directly
            ent_results.extend(
                [
                    {
                        attr_state: (prev_state := state),
                        attr_time: row[last_updated_ts_idx],
                    }
                    for row in group
                    if (state := row[state_idx]) != prev_state
                ]
            )
            continue

        # Non-compressed state format returns an ISO formatted string
        _utc_from_timestamp = dt_util.utc_from_timestamp
        ent_results.extend(
            [
                {
                    attr_state: (prev_state := state),
                    attr_time: _utc_from_timestamp(
                        row[last_updated_ts_idx]
                    ).isoformat(),
                }
                for row in group
                if (state := row[state_idx]) != prev_state
            ]
        )

    if descending:
        for ent_results in result.values():
            ent_results.reverse()

    # Filter out the empty lists if some states had 0 results.
    return {key: val for key, val in result.items() if val}
