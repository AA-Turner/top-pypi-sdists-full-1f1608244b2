# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from parsenodes.h @ 17-6.1.0-0-g1c1a32e
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2025 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass


class A_Expr_Kind(IntEnum):
    AEXPR_OP = 0
    AEXPR_OP_ANY = auto()
    AEXPR_OP_ALL = auto()
    AEXPR_DISTINCT = auto()
    AEXPR_NOT_DISTINCT = auto()
    AEXPR_NULLIF = auto()
    AEXPR_IN = auto()
    AEXPR_LIKE = auto()
    AEXPR_ILIKE = auto()
    AEXPR_SIMILAR = auto()
    AEXPR_BETWEEN = auto()
    AEXPR_NOT_BETWEEN = auto()
    AEXPR_BETWEEN_SYM = auto()
    AEXPR_NOT_BETWEEN_SYM = auto()


class AlterPublicationAction(IntEnum):
    AP_AddObjects = 0
    AP_DropObjects = auto()
    AP_SetObjects = auto()


class AlterSubscriptionType(IntEnum):
    ALTER_SUBSCRIPTION_OPTIONS = 0
    ALTER_SUBSCRIPTION_CONNECTION = auto()
    ALTER_SUBSCRIPTION_SET_PUBLICATION = auto()
    ALTER_SUBSCRIPTION_ADD_PUBLICATION = auto()
    ALTER_SUBSCRIPTION_DROP_PUBLICATION = auto()
    ALTER_SUBSCRIPTION_REFRESH = auto()
    ALTER_SUBSCRIPTION_ENABLED = auto()
    ALTER_SUBSCRIPTION_SKIP = auto()


class AlterTSConfigType(IntEnum):
    ALTER_TSCONFIG_ADD_MAPPING = 0
    ALTER_TSCONFIG_ALTER_MAPPING_FOR_TOKEN = auto()
    ALTER_TSCONFIG_REPLACE_DICT = auto()
    ALTER_TSCONFIG_REPLACE_DICT_FOR_TOKEN = auto()
    ALTER_TSCONFIG_DROP_MAPPING = auto()


class AlterTableType(IntEnum):
    AT_AddColumn = 0
    AT_AddColumnToView = auto()
    AT_ColumnDefault = auto()
    AT_CookedColumnDefault = auto()
    AT_DropNotNull = auto()
    AT_SetNotNull = auto()
    AT_SetExpression = auto()
    AT_DropExpression = auto()
    AT_CheckNotNull = auto()
    AT_SetStatistics = auto()
    AT_SetOptions = auto()
    AT_ResetOptions = auto()
    AT_SetStorage = auto()
    AT_SetCompression = auto()
    AT_DropColumn = auto()
    AT_AddIndex = auto()
    AT_ReAddIndex = auto()
    AT_AddConstraint = auto()
    AT_ReAddConstraint = auto()
    AT_ReAddDomainConstraint = auto()
    AT_AlterConstraint = auto()
    AT_ValidateConstraint = auto()
    AT_AddIndexConstraint = auto()
    AT_DropConstraint = auto()
    AT_ReAddComment = auto()
    AT_AlterColumnType = auto()
    AT_AlterColumnGenericOptions = auto()
    AT_ChangeOwner = auto()
    AT_ClusterOn = auto()
    AT_DropCluster = auto()
    AT_SetLogged = auto()
    AT_SetUnLogged = auto()
    AT_DropOids = auto()
    AT_SetAccessMethod = auto()
    AT_SetTableSpace = auto()
    AT_SetRelOptions = auto()
    AT_ResetRelOptions = auto()
    AT_ReplaceRelOptions = auto()
    AT_EnableTrig = auto()
    AT_EnableAlwaysTrig = auto()
    AT_EnableReplicaTrig = auto()
    AT_DisableTrig = auto()
    AT_EnableTrigAll = auto()
    AT_DisableTrigAll = auto()
    AT_EnableTrigUser = auto()
    AT_DisableTrigUser = auto()
    AT_EnableRule = auto()
    AT_EnableAlwaysRule = auto()
    AT_EnableReplicaRule = auto()
    AT_DisableRule = auto()
    AT_AddInherit = auto()
    AT_DropInherit = auto()
    AT_AddOf = auto()
    AT_DropOf = auto()
    AT_ReplicaIdentity = auto()
    AT_EnableRowSecurity = auto()
    AT_DisableRowSecurity = auto()
    AT_ForceRowSecurity = auto()
    AT_NoForceRowSecurity = auto()
    AT_GenericOptions = auto()
    AT_AttachPartition = auto()
    AT_DetachPartition = auto()
    AT_DetachPartitionFinalize = auto()
    AT_AddIdentity = auto()
    AT_SetIdentity = auto()
    AT_DropIdentity = auto()
    AT_ReAddStatistics = auto()


class CTEMaterialize(IntEnum):
    CTEMaterializeDefault = 0
    CTEMaterializeAlways = auto()
    CTEMaterializeNever = auto()


class ConstrType(IntEnum):
    CONSTR_NULL = 0
    CONSTR_NOTNULL = auto()
    CONSTR_DEFAULT = auto()
    CONSTR_IDENTITY = auto()
    CONSTR_GENERATED = auto()
    CONSTR_CHECK = auto()
    CONSTR_PRIMARY = auto()
    CONSTR_UNIQUE = auto()
    CONSTR_EXCLUSION = auto()
    CONSTR_FOREIGN = auto()
    CONSTR_ATTR_DEFERRABLE = auto()
    CONSTR_ATTR_NOT_DEFERRABLE = auto()
    CONSTR_ATTR_DEFERRED = auto()
    CONSTR_ATTR_IMMEDIATE = auto()


class DefElemAction(IntEnum):
    DEFELEM_UNSPEC = 0
    DEFELEM_SET = auto()
    DEFELEM_ADD = auto()
    DEFELEM_DROP = auto()


class DiscardMode(IntEnum):
    DISCARD_ALL = 0
    DISCARD_PLANS = auto()
    DISCARD_SEQUENCES = auto()
    DISCARD_TEMP = auto()


class DropBehavior(IntEnum):
    DROP_RESTRICT = 0
    DROP_CASCADE = auto()


class FetchDirection(IntEnum):
    FETCH_FORWARD = 0
    FETCH_BACKWARD = auto()
    FETCH_ABSOLUTE = auto()
    FETCH_RELATIVE = auto()


class FunctionParameterMode(StrEnum):
    FUNC_PARAM_IN = 'i'
    FUNC_PARAM_OUT = 'o'
    FUNC_PARAM_INOUT = 'b'
    FUNC_PARAM_VARIADIC = 'v'
    FUNC_PARAM_TABLE = 't'
    FUNC_PARAM_DEFAULT = 'd'


class GrantTargetType(IntEnum):
    ACL_TARGET_OBJECT = 0
    ACL_TARGET_ALL_IN_SCHEMA = auto()
    ACL_TARGET_DEFAULTS = auto()


class GroupingSetKind(IntEnum):
    GROUPING_SET_EMPTY = 0
    GROUPING_SET_SIMPLE = auto()
    GROUPING_SET_ROLLUP = auto()
    GROUPING_SET_CUBE = auto()
    GROUPING_SET_SETS = auto()


class ImportForeignSchemaType(IntEnum):
    FDW_IMPORT_SCHEMA_ALL = 0
    FDW_IMPORT_SCHEMA_LIMIT_TO = auto()
    FDW_IMPORT_SCHEMA_EXCEPT = auto()


class JsonQuotes(IntEnum):
    JS_QUOTES_UNSPEC = 0
    JS_QUOTES_KEEP = auto()
    JS_QUOTES_OMIT = auto()


class JsonTableColumnType(IntEnum):
    JTC_FOR_ORDINALITY = 0
    JTC_REGULAR = auto()
    JTC_EXISTS = auto()
    JTC_FORMATTED = auto()
    JTC_NESTED = auto()


class ObjectType(IntEnum):
    OBJECT_ACCESS_METHOD = 0
    OBJECT_AGGREGATE = auto()
    OBJECT_AMOP = auto()
    OBJECT_AMPROC = auto()
    OBJECT_ATTRIBUTE = auto()
    OBJECT_CAST = auto()
    OBJECT_COLUMN = auto()
    OBJECT_COLLATION = auto()
    OBJECT_CONVERSION = auto()
    OBJECT_DATABASE = auto()
    OBJECT_DEFAULT = auto()
    OBJECT_DEFACL = auto()
    OBJECT_DOMAIN = auto()
    OBJECT_DOMCONSTRAINT = auto()
    OBJECT_EVENT_TRIGGER = auto()
    OBJECT_EXTENSION = auto()
    OBJECT_FDW = auto()
    OBJECT_FOREIGN_SERVER = auto()
    OBJECT_FOREIGN_TABLE = auto()
    OBJECT_FUNCTION = auto()
    OBJECT_INDEX = auto()
    OBJECT_LANGUAGE = auto()
    OBJECT_LARGEOBJECT = auto()
    OBJECT_MATVIEW = auto()
    OBJECT_OPCLASS = auto()
    OBJECT_OPERATOR = auto()
    OBJECT_OPFAMILY = auto()
    OBJECT_PARAMETER_ACL = auto()
    OBJECT_POLICY = auto()
    OBJECT_PROCEDURE = auto()
    OBJECT_PUBLICATION = auto()
    OBJECT_PUBLICATION_NAMESPACE = auto()
    OBJECT_PUBLICATION_REL = auto()
    OBJECT_ROLE = auto()
    OBJECT_ROUTINE = auto()
    OBJECT_RULE = auto()
    OBJECT_SCHEMA = auto()
    OBJECT_SEQUENCE = auto()
    OBJECT_SUBSCRIPTION = auto()
    OBJECT_STATISTIC_EXT = auto()
    OBJECT_TABCONSTRAINT = auto()
    OBJECT_TABLE = auto()
    OBJECT_TABLESPACE = auto()
    OBJECT_TRANSFORM = auto()
    OBJECT_TRIGGER = auto()
    OBJECT_TSCONFIGURATION = auto()
    OBJECT_TSDICTIONARY = auto()
    OBJECT_TSPARSER = auto()
    OBJECT_TSTEMPLATE = auto()
    OBJECT_TYPE = auto()
    OBJECT_USER_MAPPING = auto()
    OBJECT_VIEW = auto()


class PartitionRangeDatumKind(IntEnum):
    PARTITION_RANGE_DATUM_MINVALUE = -1
    PARTITION_RANGE_DATUM_VALUE = 0
    PARTITION_RANGE_DATUM_MAXVALUE = 1


class PartitionStrategy(StrEnum):
    PARTITION_STRATEGY_LIST = 'l'
    PARTITION_STRATEGY_RANGE = 'r'
    PARTITION_STRATEGY_HASH = 'h'


class PublicationObjSpecType(IntEnum):
    PUBLICATIONOBJ_TABLE = 0
    PUBLICATIONOBJ_TABLES_IN_SCHEMA = auto()
    PUBLICATIONOBJ_TABLES_IN_CUR_SCHEMA = auto()
    PUBLICATIONOBJ_CONTINUATION = auto()


class QuerySource(IntEnum):
    QSRC_ORIGINAL = 0
    QSRC_PARSER = auto()
    QSRC_INSTEAD_RULE = auto()
    QSRC_QUAL_INSTEAD_RULE = auto()
    QSRC_NON_INSTEAD_RULE = auto()


class RTEKind(IntEnum):
    RTE_RELATION = 0
    RTE_SUBQUERY = auto()
    RTE_JOIN = auto()
    RTE_FUNCTION = auto()
    RTE_TABLEFUNC = auto()
    RTE_VALUES = auto()
    RTE_CTE = auto()
    RTE_NAMEDTUPLESTORE = auto()
    RTE_RESULT = auto()


class ReindexObjectType(IntEnum):
    REINDEX_OBJECT_INDEX = 0
    REINDEX_OBJECT_TABLE = auto()
    REINDEX_OBJECT_SCHEMA = auto()
    REINDEX_OBJECT_SYSTEM = auto()
    REINDEX_OBJECT_DATABASE = auto()


class RoleSpecType(IntEnum):
    ROLESPEC_CSTRING = 0
    ROLESPEC_CURRENT_ROLE = auto()
    ROLESPEC_CURRENT_USER = auto()
    ROLESPEC_SESSION_USER = auto()
    ROLESPEC_PUBLIC = auto()


class RoleStmtType(IntEnum):
    ROLESTMT_ROLE = 0
    ROLESTMT_USER = auto()
    ROLESTMT_GROUP = auto()


class SetOperation(IntEnum):
    SETOP_NONE = 0
    SETOP_UNION = auto()
    SETOP_INTERSECT = auto()
    SETOP_EXCEPT = auto()


class SetQuantifier(IntEnum):
    SET_QUANTIFIER_DEFAULT = 0
    SET_QUANTIFIER_ALL = auto()
    SET_QUANTIFIER_DISTINCT = auto()


class SortByDir(IntEnum):
    SORTBY_DEFAULT = 0
    SORTBY_ASC = auto()
    SORTBY_DESC = auto()
    SORTBY_USING = auto()


class SortByNulls(IntEnum):
    SORTBY_NULLS_DEFAULT = 0
    SORTBY_NULLS_FIRST = auto()
    SORTBY_NULLS_LAST = auto()


class TableLikeOption(IntFlag):
    CREATE_TABLE_LIKE_COMMENTS = 1 << 0
    CREATE_TABLE_LIKE_COMPRESSION = 1 << 1
    CREATE_TABLE_LIKE_CONSTRAINTS = 1 << 2
    CREATE_TABLE_LIKE_DEFAULTS = 1 << 3
    CREATE_TABLE_LIKE_GENERATED = 1 << 4
    CREATE_TABLE_LIKE_IDENTITY = 1 << 5
    CREATE_TABLE_LIKE_INDEXES = 1 << 6
    CREATE_TABLE_LIKE_STATISTICS = 1 << 7
    CREATE_TABLE_LIKE_STORAGE = 1 << 8
    CREATE_TABLE_LIKE_ALL = 0x7FFFFFFF


class TransactionStmtKind(IntEnum):
    TRANS_STMT_BEGIN = 0
    TRANS_STMT_START = auto()
    TRANS_STMT_COMMIT = auto()
    TRANS_STMT_ROLLBACK = auto()
    TRANS_STMT_SAVEPOINT = auto()
    TRANS_STMT_RELEASE = auto()
    TRANS_STMT_ROLLBACK_TO = auto()
    TRANS_STMT_PREPARE = auto()
    TRANS_STMT_COMMIT_PREPARED = auto()
    TRANS_STMT_ROLLBACK_PREPARED = auto()


class VariableSetKind(IntEnum):
    VAR_SET_VALUE = 0
    VAR_SET_DEFAULT = auto()
    VAR_SET_CURRENT = auto()
    VAR_SET_MULTI = auto()
    VAR_RESET = auto()
    VAR_RESET_ALL = auto()


class ViewCheckOption(IntEnum):
    NO_CHECK_OPTION = 0
    LOCAL_CHECK_OPTION = auto()
    CASCADED_CHECK_OPTION = auto()


class WCOKind(IntEnum):
    WCO_VIEW_CHECK = 0
    WCO_RLS_INSERT_CHECK = auto()
    WCO_RLS_UPDATE_CHECK = auto()
    WCO_RLS_CONFLICT_CHECK = auto()
    WCO_RLS_MERGE_UPDATE_CHECK = auto()
    WCO_RLS_MERGE_DELETE_CHECK = auto()


# #define-ed constants

ACL_INSERT = 1<<0

ACL_SELECT = 1<<1

ACL_UPDATE = 1<<2

ACL_DELETE = 1<<3

ACL_TRUNCATE = 1<<4

ACL_REFERENCES = 1<<5

ACL_TRIGGER = 1<<6

ACL_EXECUTE = 1<<7

ACL_USAGE = 1<<8

ACL_CREATE = 1<<9

ACL_CREATE_TEMP = 1<<10

ACL_CONNECT = 1<<11

ACL_SET = 1<<12

ACL_ALTER_SYSTEM = 1<<13

ACL_MAINTAIN = 1<<14

N_ACL_RIGHTS = 15

ACL_NO_RIGHTS = 0

FRAMEOPTION_NONDEFAULT = 0x00001

FRAMEOPTION_RANGE = 0x00002

FRAMEOPTION_ROWS = 0x00004

FRAMEOPTION_GROUPS = 0x00008

FRAMEOPTION_BETWEEN = 0x00010

FRAMEOPTION_START_UNBOUNDED_PRECEDING = 0x00020

FRAMEOPTION_END_UNBOUNDED_PRECEDING = 0x00040

FRAMEOPTION_START_UNBOUNDED_FOLLOWING = 0x00080

FRAMEOPTION_END_UNBOUNDED_FOLLOWING = 0x00100

FRAMEOPTION_START_CURRENT_ROW = 0x00200

FRAMEOPTION_END_CURRENT_ROW = 0x00400

FRAMEOPTION_START_OFFSET_PRECEDING = 0x00800

FRAMEOPTION_END_OFFSET_PRECEDING = 0x01000

FRAMEOPTION_START_OFFSET_FOLLOWING = 0x02000

FRAMEOPTION_END_OFFSET_FOLLOWING = 0x04000

FRAMEOPTION_EXCLUDE_CURRENT_ROW = 0x08000

FRAMEOPTION_EXCLUDE_GROUP = 0x10000

FRAMEOPTION_EXCLUDE_TIES = 0x20000

FKCONSTR_ACTION_NOACTION = 'a'

FKCONSTR_ACTION_RESTRICT = 'r'

FKCONSTR_ACTION_CASCADE = 'c'

FKCONSTR_ACTION_SETNULL = 'n'

FKCONSTR_ACTION_SETDEFAULT = 'd'

FKCONSTR_MATCH_FULL = 'f'

FKCONSTR_MATCH_PARTIAL = 'p'

FKCONSTR_MATCH_SIMPLE = 's'

OPCLASS_ITEM_OPERATOR = 1

OPCLASS_ITEM_FUNCTION = 2

OPCLASS_ITEM_STORAGETYPE = 3

CURSOR_OPT_BINARY = 0x0001

CURSOR_OPT_SCROLL = 0x0002

CURSOR_OPT_NO_SCROLL = 0x0004

CURSOR_OPT_INSENSITIVE = 0x0008

CURSOR_OPT_ASENSITIVE = 0x0010

CURSOR_OPT_HOLD = 0x0020

CURSOR_OPT_FAST_PLAN = 0x0100

CURSOR_OPT_GENERIC_PLAN = 0x0200

CURSOR_OPT_CUSTOM_PLAN = 0x0400

CURSOR_OPT_PARALLEL_OK = 0x0800
