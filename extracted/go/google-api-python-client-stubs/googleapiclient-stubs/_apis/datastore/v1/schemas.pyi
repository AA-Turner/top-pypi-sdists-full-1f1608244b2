import typing

import typing_extensions

_list = list

@typing.type_check_only
class Aggregation(typing_extensions.TypedDict, total=False):
    alias: str
    avg: Avg
    count: Count
    sum: Sum

@typing.type_check_only
class AggregationQuery(typing_extensions.TypedDict, total=False):
    aggregations: _list[Aggregation]
    nestedQuery: Query

@typing.type_check_only
class AggregationResult(typing_extensions.TypedDict, total=False):
    aggregateProperties: dict[str, typing.Any]

@typing.type_check_only
class AggregationResultBatch(typing_extensions.TypedDict, total=False):
    aggregationResults: _list[AggregationResult]
    moreResults: typing_extensions.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    readTime: str

@typing.type_check_only
class AllocateIdsRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    keys: _list[Key]

@typing.type_check_only
class AllocateIdsResponse(typing_extensions.TypedDict, total=False):
    keys: _list[Key]

@typing.type_check_only
class ArrayValue(typing_extensions.TypedDict, total=False):
    values: _list[Value]

@typing.type_check_only
class Avg(typing_extensions.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    transactionOptions: TransactionOptions

@typing.type_check_only
class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class CommitRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "TRANSACTIONAL", "NON_TRANSACTIONAL"
    ]
    mutations: _list[Mutation]
    singleUseTransaction: TransactionOptions
    transaction: str

@typing.type_check_only
class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    indexUpdates: int
    mutationResults: _list[MutationResult]

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: _list[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND", "OR"]

@typing.type_check_only
class Count(typing_extensions.TypedDict, total=False):
    upTo: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    key: Key
    properties: dict[str, typing.Any]

@typing.type_check_only
class EntityResult(typing_extensions.TypedDict, total=False):
    createTime: str
    cursor: str
    entity: Entity
    updateTime: str
    version: str

@typing.type_check_only
class ExecutionStats(typing_extensions.TypedDict, total=False):
    debugStats: dict[str, typing.Any]
    executionDuration: str
    readOperations: str
    resultsReturned: str

@typing.type_check_only
class ExplainMetrics(typing_extensions.TypedDict, total=False):
    executionStats: ExecutionStats
    planSummary: PlanSummary

@typing.type_check_only
class ExplainOptions(typing_extensions.TypedDict, total=False):
    analyze: bool

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    compositeFilter: CompositeFilter
    propertyFilter: PropertyFilter

@typing.type_check_only
class FindNearest(typing_extensions.TypedDict, total=False):
    distanceMeasure: typing_extensions.Literal[
        "DISTANCE_MEASURE_UNSPECIFIED", "EUCLIDEAN", "COSINE", "DOT_PRODUCT"
    ]
    distanceResultProperty: str
    distanceThreshold: float
    limit: int
    queryVector: Value
    vectorProperty: PropertyReference

@typing.type_check_only
class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata(
    typing_extensions.TypedDict, total=False
):
    migrationState: typing_extensions.Literal[
        "MIGRATION_STATE_UNSPECIFIED", "RUNNING", "PAUSED", "COMPLETE"
    ]
    migrationStep: typing_extensions.Literal[
        "MIGRATION_STEP_UNSPECIFIED",
        "PREPARE",
        "START",
        "APPLY_WRITES_SYNCHRONOUSLY",
        "COPY_AND_VERIFY",
        "REDIRECT_EVENTUALLY_CONSISTENT_READS",
        "REDIRECT_STRONGLY_CONSISTENT_READS",
        "REDIRECT_WRITES",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    labels: dict[str, typing.Any]
    outputUrlPrefix: str

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1ImportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class GoogleDatastoreAdminV1Index(typing_extensions.TypedDict, total=False):
    ancestor: typing_extensions.Literal[
        "ANCESTOR_MODE_UNSPECIFIED", "NONE", "ALL_ANCESTORS"
    ]
    indexId: str
    kind: str
    projectId: str
    properties: _list[GoogleDatastoreAdminV1IndexedProperty]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR"
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1IndexedProperty(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    name: str

@typing.type_check_only
class GoogleDatastoreAdminV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleDatastoreAdminV1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleDatastoreAdminV1MigrationProgressEvent(
    typing_extensions.TypedDict, total=False
):
    prepareStepDetails: GoogleDatastoreAdminV1PrepareStepDetails
    redirectWritesStepDetails: GoogleDatastoreAdminV1RedirectWritesStepDetails
    step: typing_extensions.Literal[
        "MIGRATION_STEP_UNSPECIFIED",
        "PREPARE",
        "START",
        "APPLY_WRITES_SYNCHRONOUSLY",
        "COPY_AND_VERIFY",
        "REDIRECT_EVENTUALLY_CONSISTENT_READS",
        "REDIRECT_STRONGLY_CONSISTENT_READS",
        "REDIRECT_WRITES",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1MigrationStateEvent(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "MIGRATION_STATE_UNSPECIFIED", "RUNNING", "PAUSED", "COMPLETE"
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1PrepareStepDetails(
    typing_extensions.TypedDict, total=False
):
    concurrencyMode: typing_extensions.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "PESSIMISTIC",
        "OPTIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleDatastoreAdminV1RedirectWritesStepDetails(
    typing_extensions.TypedDict, total=False
):
    concurrencyMode: typing_extensions.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "PESSIMISTIC",
        "OPTIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GqlQuery(typing_extensions.TypedDict, total=False):
    allowLiterals: bool
    namedBindings: dict[str, typing.Any]
    positionalBindings: _list[GqlQueryParameter]
    queryString: str

@typing.type_check_only
class GqlQueryParameter(typing_extensions.TypedDict, total=False):
    cursor: str
    value: Value

@typing.type_check_only
class Key(typing_extensions.TypedDict, total=False):
    partitionId: PartitionId
    path: _list[PathElement]

@typing.type_check_only
class KindExpression(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LookupRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    keys: _list[Key]
    propertyMask: PropertyMask
    readOptions: ReadOptions

@typing.type_check_only
class LookupResponse(typing_extensions.TypedDict, total=False):
    deferred: _list[Key]
    found: _list[EntityResult]
    missing: _list[EntityResult]
    readTime: str
    transaction: str

@typing.type_check_only
class Mutation(typing_extensions.TypedDict, total=False):
    baseVersion: str
    conflictResolutionStrategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED", "SERVER_VALUE", "FAIL"
    ]
    delete: Key
    insert: Entity
    propertyMask: PropertyMask
    propertyTransforms: _list[PropertyTransform]
    update: Entity
    updateTime: str
    upsert: Entity

@typing.type_check_only
class MutationResult(typing_extensions.TypedDict, total=False):
    conflictDetected: bool
    createTime: str
    key: Key
    transformResults: _list[Value]
    updateTime: str
    version: str

@typing.type_check_only
class PartitionId(typing_extensions.TypedDict, total=False):
    databaseId: str
    namespaceId: str
    projectId: str

@typing.type_check_only
class PathElement(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class PlanSummary(typing_extensions.TypedDict, total=False):
    indexesUsed: _list[dict[str, typing.Any]]

@typing.type_check_only
class Projection(typing_extensions.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class PropertyFilter(typing_extensions.TypedDict, total=False):
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "EQUAL",
        "IN",
        "NOT_EQUAL",
        "HAS_ANCESTOR",
        "NOT_IN",
    ]
    property: PropertyReference
    value: Value

@typing.type_check_only
class PropertyMask(typing_extensions.TypedDict, total=False):
    paths: _list[str]

@typing.type_check_only
class PropertyOrder(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    property: PropertyReference

@typing.type_check_only
class PropertyReference(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class PropertyTransform(typing_extensions.TypedDict, total=False):
    appendMissingElements: ArrayValue
    increment: Value
    maximum: Value
    minimum: Value
    property: str
    removeAllFromArray: ArrayValue
    setToServerValue: typing_extensions.Literal[
        "SERVER_VALUE_UNSPECIFIED", "REQUEST_TIME"
    ]

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    distinctOn: _list[PropertyReference]
    endCursor: str
    filter: Filter
    findNearest: FindNearest
    kind: _list[KindExpression]
    limit: int
    offset: int
    order: _list[PropertyOrder]
    projection: _list[Projection]
    startCursor: str

@typing.type_check_only
class QueryResultBatch(typing_extensions.TypedDict, total=False):
    endCursor: str
    entityResultType: typing_extensions.Literal[
        "RESULT_TYPE_UNSPECIFIED", "FULL", "PROJECTION", "KEY_ONLY"
    ]
    entityResults: _list[EntityResult]
    moreResults: typing_extensions.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    readTime: str
    skippedCursor: str
    skippedResults: int
    snapshotVersion: str

@typing.type_check_only
class ReadOnly(typing_extensions.TypedDict, total=False):
    readTime: str

@typing.type_check_only
class ReadOptions(typing_extensions.TypedDict, total=False):
    newTransaction: TransactionOptions
    readConsistency: typing_extensions.Literal[
        "READ_CONSISTENCY_UNSPECIFIED", "STRONG", "EVENTUAL"
    ]
    readTime: str
    transaction: str

@typing.type_check_only
class ReadWrite(typing_extensions.TypedDict, total=False):
    previousTransaction: str

@typing.type_check_only
class ReserveIdsRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    keys: _list[Key]

@typing.type_check_only
class ReserveIdsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RollbackRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    transaction: str

@typing.type_check_only
class RollbackResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RunAggregationQueryRequest(typing_extensions.TypedDict, total=False):
    aggregationQuery: AggregationQuery
    databaseId: str
    explainOptions: ExplainOptions
    gqlQuery: GqlQuery
    partitionId: PartitionId
    readOptions: ReadOptions

@typing.type_check_only
class RunAggregationQueryResponse(typing_extensions.TypedDict, total=False):
    batch: AggregationResultBatch
    explainMetrics: ExplainMetrics
    query: AggregationQuery
    transaction: str

@typing.type_check_only
class RunQueryRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    explainOptions: ExplainOptions
    gqlQuery: GqlQuery
    partitionId: PartitionId
    propertyMask: PropertyMask
    query: Query
    readOptions: ReadOptions

@typing.type_check_only
class RunQueryResponse(typing_extensions.TypedDict, total=False):
    batch: QueryResultBatch
    explainMetrics: ExplainMetrics
    query: Query
    transaction: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Sum(typing_extensions.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class TransactionOptions(typing_extensions.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    arrayValue: ArrayValue
    blobValue: str
    booleanValue: bool
    doubleValue: float
    entityValue: Entity
    excludeFromIndexes: bool
    geoPointValue: LatLng
    integerValue: str
    keyValue: Key
    meaning: int
    nullValue: typing_extensions.Literal["NULL_VALUE"]
    stringValue: str
    timestampValue: str
