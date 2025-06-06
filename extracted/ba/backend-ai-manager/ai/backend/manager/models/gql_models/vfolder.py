from __future__ import annotations

import uuid
from collections.abc import Iterable, Mapping, Sequence
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Self,
)

import graphene
import graphql
import sqlalchemy as sa
import trafaret as t
from dateutil.parser import ParserError
from dateutil.parser import parse as dtparse
from graphene.types.datetime import DateTime as GQLDateTime
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError
from sqlalchemy.orm import joinedload

from ai.backend.common.config import model_definition_iv
from ai.backend.common.types import (
    VFolderID,
    VFolderUsageMode,
)

from ...defs import (
    DEFAULT_CHUNK_SIZE,
)
from ...errors.exceptions import (
    VFolderOperationFailed,
)
from ..base import (
    BigInt,
    FilterExprArg,
    OrderExprArg,
    batch_multiresult_in_scalar_stream,
    generate_sql_info_for_gql_connection,
)
from ..gql_relay import AsyncNode, Connection, ConnectionResolverResult
from ..group import GroupRow, ProjectType
from ..minilang.ordering import OrderSpecItem, QueryOrderParser
from ..minilang.queryfilter import FieldSpecItem, QueryFilterParser
from ..rbac import (
    ScopeType,
    SystemScope,
)
from ..rbac.context import ClientContext
from ..rbac.permission_defs import VFolderPermission as VFolderRBACPermission
from ..user import UserRole
from ..vfolder import (
    DEAD_VFOLDER_STATUSES,
    VFolderOperationStatus,
    VFolderOwnershipType,
    VFolderPermission,
    VFolderRow,
    VirtualFolder,
    get_permission_ctx,
    is_unmanaged,
)

if TYPE_CHECKING:
    from ..gql import GraphQueryContext


class VFolderPermissionValueField(graphene.Scalar):
    class Meta:
        description = f"Added in 24.09.0. One of {[val.value for val in VFolderRBACPermission]}."

    @staticmethod
    def serialize(val: VFolderRBACPermission) -> str:
        return val.value

    @staticmethod
    def parse_literal(node: Any, _variables=None):
        if isinstance(node, graphql.language.ast.StringValueNode):
            return VFolderRBACPermission(node.value)

    @staticmethod
    def parse_value(value: str) -> VFolderRBACPermission:
        return VFolderRBACPermission(value)


class VirtualFolderNode(graphene.ObjectType):
    class Meta:
        interfaces = (AsyncNode,)
        description = "Added in 24.03.4"

    row_id = graphene.UUID(description="Added in 24.03.4. ID of VFolder.")
    host = graphene.String()
    quota_scope_id = graphene.String()
    name = graphene.String()
    user = graphene.UUID()  # User.id (current owner, null in project vfolders)
    user_email = graphene.String()  # User.email (current owner, null in project vfolders)
    group = graphene.UUID()  # Group.id (current owner, null in user vfolders)
    group_name = graphene.String()  # Group.name (current owenr, null in user vfolders)
    creator = graphene.String()  # User.email (always set)
    unmanaged_path = graphene.String()
    usage_mode = graphene.String()
    permission = graphene.String()
    ownership_type = graphene.String()
    max_files = graphene.Int()
    max_size = BigInt()  # in MiB
    created_at = GQLDateTime()
    last_used = GQLDateTime()

    num_files = graphene.Int()
    cur_size = BigInt()
    # num_attached = graphene.Int()
    cloneable = graphene.Boolean()
    status = graphene.String()

    permissions = graphene.List(
        VFolderPermissionValueField,
        description=f"Added in 24.09.0. One of {[val.value for val in VFolderRBACPermission]}.",
    )

    _queryfilter_fieldspec: Mapping[str, FieldSpecItem] = {
        "id": ("id", uuid.UUID),
        "host": ("host", None),
        "quota_scope_id": ("quota_scope_id", None),
        "name": ("name", None),
        "group": ("group", uuid.UUID),
        "user": ("user", uuid.UUID),
        "creator": ("creator", None),
        "unmanaged_path": ("unmanaged_path", None),
        "usage_mode": (
            "usage_mode",
            VFolderUsageMode,
        ),
        "permission": (
            "permission",
            VFolderPermission,
        ),
        "ownership_type": (
            "ownership_type",
            VFolderOwnershipType,
        ),
        "max_files": ("max_files", None),
        "max_size": ("max_size", None),
        "created_at": ("created_at", dtparse),
        "last_used": ("last_used", dtparse),
        "cloneable": ("cloneable", None),
        "status": (
            "status",
            VFolderOperationStatus,
        ),
    }

    _queryorder_colmap: Mapping[str, OrderSpecItem] = {
        "id": ("id", None),
        "host": ("host", None),
        "quota_scope_id": ("quota_scope_id", None),
        "name": ("name", None),
        "group": ("group", None),
        "user": ("user", None),
        "creator": ("creator", None),
        "usage_mode": ("usage_mode", None),
        "permission": ("permission", None),
        "ownership_type": ("ownership_type", None),
        "max_files": ("max_files", None),
        "max_size": ("max_size", None),
        "created_at": ("created_at", None),
        "last_used": ("last_used", None),
        "cloneable": ("cloneable", None),
        "status": ("status", None),
        "cur_size": ("cur_size", None),
    }

    def resolve_created_at(
        self,
        info: graphene.ResolveInfo,
    ) -> datetime:
        if isinstance(self.created_at, datetime):
            return self.created_at

        try:
            return dtparse(self.created_at)
        except ParserError:
            return self.created_at

    @classmethod
    def from_row(
        cls,
        graph_ctx: GraphQueryContext,
        row: VFolderRow,
        *,
        permissions: Optional[Iterable[VFolderRBACPermission]] = None,
    ) -> Self:
        result = cls(
            id=row.id,
            row_id=row.id,
            host=row.host,
            quota_scope_id=row.quota_scope_id,
            name=row.name,
            user=row.user,
            user_email=row.user_row.email if row.user_row else None,
            group=row.group_row.id if row.group_row else None,
            group_name=row.group_row.name if row.group_row else None,
            creator=row.creator,
            unmanaged_path=row.unmanaged_path,
            usage_mode=row.usage_mode,
            permission=row.permission,
            ownership_type=row.ownership_type,
            max_files=row.max_files,
            max_size=row.max_size,  # in B
            created_at=row.created_at,
            last_used=row.last_used,
            cloneable=row.cloneable,
            status=row.status,
            cur_size=row.cur_size,
        )
        result.permissions = [] if permissions is None else permissions
        return result

    @classmethod
    async def batch_load_by_id(
        cls,
        graph_ctx: GraphQueryContext,
        folder_ids: Sequence[uuid.UUID],
    ) -> Sequence[Sequence[Self]]:
        query = (
            sa.select(VFolderRow)
            .where(VFolderRow.id.in_(folder_ids))
            .options(
                joinedload(VFolderRow.user_row),
                joinedload(VFolderRow.group_row),
            )
        )
        async with graph_ctx.db.begin_readonly_session() as db_session:
            return await batch_multiresult_in_scalar_stream(
                graph_ctx, db_session, query, cls, folder_ids, lambda row: row.id
            )

    @classmethod
    async def get_node(
        cls,
        info: graphene.ResolveInfo,
        id: str,
        scope_id: ScopeType = SystemScope(),
        permission: VFolderRBACPermission = VFolderRBACPermission.READ_ATTRIBUTE,
    ) -> Optional[Self]:
        graph_ctx: GraphQueryContext = info.context
        _, vfolder_row_id = AsyncNode.resolve_global_id(info, id)
        query = sa.select(VFolderRow).options(
            joinedload(VFolderRow.user_row),
            joinedload(VFolderRow.group_row),
        )
        async with graph_ctx.db.connect() as db_conn:
            user = graph_ctx.user
            client_ctx = ClientContext(
                graph_ctx.db, user["domain_name"], user["uuid"], user["role"]
            )
            permission_ctx = await get_permission_ctx(db_conn, client_ctx, scope_id, permission)
            cond = permission_ctx.query_condition
            if cond is None:
                return None
            query = query.where(sa.and_(cond, VFolderRow.id == uuid.UUID(vfolder_row_id)))
            async with graph_ctx.db.begin_readonly_session(db_conn) as db_session:
                vfolder_row = await db_session.scalar(query)
        return cls.from_row(
            graph_ctx,
            vfolder_row,
            permissions=await permission_ctx.calculate_final_permission(vfolder_row),
        )

    @classmethod
    async def get_connection(
        cls,
        info: graphene.ResolveInfo,
        filter_expr: str | None = None,
        order_expr: str | None = None,
        offset: int | None = None,
        after: str | None = None,
        first: int | None = None,
        before: str | None = None,
        last: int | None = None,
    ) -> ConnectionResolverResult[Self]:
        graph_ctx: GraphQueryContext = info.context
        _filter_arg = (
            FilterExprArg(filter_expr, QueryFilterParser(cls._queryfilter_fieldspec))
            if filter_expr is not None
            else None
        )
        _order_expr = (
            OrderExprArg(order_expr, QueryOrderParser(cls._queryorder_colmap))
            if order_expr is not None
            else None
        )
        (
            query,
            cnt_query,
            _,
            cursor,
            pagination_order,
            page_size,
        ) = generate_sql_info_for_gql_connection(
            info,
            VFolderRow,
            VFolderRow.id,
            _filter_arg,
            _order_expr,
            offset,
            after=after,
            first=first,
            before=before,
            last=last,
        )

        query = query.options(
            joinedload(VFolderRow.user_row),
            joinedload(VFolderRow.group_row),
        )
        async with graph_ctx.db.begin_readonly_session() as db_session:
            vfolder_rows = (await db_session.scalars(query)).all()
            total_cnt = await db_session.scalar(cnt_query)
        result: list[Self] = [cls.from_row(graph_ctx, vf) for vf in vfolder_rows]
        return ConnectionResolverResult(result, cursor, pagination_order, page_size, total_cnt)

    @classmethod
    async def get_accessible_connection(
        cls,
        info: graphene.ResolveInfo,
        scope_id: ScopeType,
        permission: VFolderRBACPermission,
        filter_expr: str | None = None,
        order_expr: str | None = None,
        offset: int | None = None,
        after: str | None = None,
        first: int | None = None,
        before: str | None = None,
        last: int | None = None,
    ) -> ConnectionResolverResult[Self]:
        graph_ctx: GraphQueryContext = info.context
        _filter_arg = (
            FilterExprArg(filter_expr, QueryFilterParser(cls._queryfilter_fieldspec))
            if filter_expr is not None
            else None
        )
        _order_expr = (
            OrderExprArg(order_expr, QueryOrderParser(cls._queryorder_colmap))
            if order_expr is not None
            else None
        )
        (
            query,
            cnt_query,
            _,
            cursor,
            pagination_order,
            page_size,
        ) = generate_sql_info_for_gql_connection(
            info,
            VFolderRow,
            VFolderRow.id,
            _filter_arg,
            _order_expr,
            offset,
            after=after,
            first=first,
            before=before,
            last=last,
        )

        query = query.options(
            joinedload(VFolderRow.user_row),
            joinedload(VFolderRow.group_row),
        )
        async with graph_ctx.db.connect() as db_conn:
            user = graph_ctx.user
            client_ctx = ClientContext(
                graph_ctx.db, user["domain_name"], user["uuid"], user["role"]
            )
            permission_ctx = await get_permission_ctx(db_conn, client_ctx, scope_id, permission)
            cond = permission_ctx.query_condition
            if cond is None:
                return ConnectionResolverResult([], cursor, pagination_order, page_size, 0)
            query = query.where(cond)
            cnt_query = cnt_query.where(cond)
            async with graph_ctx.db.begin_readonly_session(db_conn) as db_session:
                vfolder_rows = (await db_session.scalars(query)).all()
                total_cnt = await db_session.scalar(cnt_query)
        result: list[Self] = [
            cls.from_row(
                graph_ctx,
                vf,
                permissions=await permission_ctx.calculate_final_permission(vf),
            )
            for vf in vfolder_rows
        ]
        return ConnectionResolverResult(result, cursor, pagination_order, page_size, total_cnt)


class VirtualFolderConnection(Connection):
    class Meta:
        node = VirtualFolderNode
        description = "Added in 24.03.4"


class ModelCardProcessError(RuntimeError):
    msg: str

    def __init__(self, msg: str) -> None:
        self.msg = msg


class ModelCard(graphene.ObjectType):
    class Meta:
        interfaces = (AsyncNode,)

    name = graphene.String()
    row_id = graphene.UUID(description="Added in 24.03.8. ID of VFolder.")
    vfolder = graphene.Field(VirtualFolder)
    vfolder_node = graphene.Field(VirtualFolderNode, description="Added in 24.09.0.")
    author = graphene.String()
    title = graphene.String(description="Human readable name of the model.")
    version = graphene.String()
    created_at = GQLDateTime(description="The time the model was created.")
    modified_at = GQLDateTime(description="The last time the model was modified.")
    description = graphene.String()
    task = graphene.String()
    category = graphene.String()
    architecture = graphene.String()
    framework = graphene.List(lambda: graphene.String)
    label = graphene.List(lambda: graphene.String)
    license = graphene.String()
    min_resource = graphene.JSONString()
    readme = graphene.String()
    readme_filetype = graphene.String(
        description=(
            "Type (mostly extension of the filename) of the README file. e.g. md, rst, txt, ..."
        )
    )
    error_msg = graphene.String(description="Added in 24.03.8.")

    _queryfilter_fieldspec: Mapping[str, FieldSpecItem] = {
        "id": ("vfolders_id", uuid.UUID),
        "host": ("vfolders_host", None),
        "quota_scope_id": ("vfolders_quota_scope_id", None),
        "name": ("vfolders_name", None),
        "group": ("vfolders_group", uuid.UUID),
        "group_name": ("groups_name", None),
        "user": ("vfolders_user", uuid.UUID),
        "user_email": ("users_email", None),
        "creator": ("vfolders_creator", None),
        "unmanaged_path": ("vfolders_unmanaged_path", None),
        "usage_mode": (
            "vfolders_usage_mode",
            VFolderUsageMode,
        ),
        "permission": (
            "vfolders_permission",
            VFolderPermission,
        ),
        "ownership_type": (
            "vfolders_ownership_type",
            VFolderOwnershipType,
        ),
        "max_files": ("vfolders_max_files", None),
        "max_size": ("vfolders_max_size", None),
        "created_at": ("vfolders_created_at", dtparse),
        "last_used": ("vfolders_last_used", dtparse),
        "cloneable": ("vfolders_cloneable", None),
        "status": (
            "vfolders_status",
            VFolderOperationStatus,
        ),
    }

    _queryorder_colmap: Mapping[str, OrderSpecItem] = {
        "id": ("vfolders_id", None),
        "host": ("vfolders_host", None),
        "quota_scope_id": ("vfolders_quota_scope_id", None),
        "name": ("vfolders_name", None),
        "group": ("vfolders_group", None),
        "group_name": ("groups_name", None),
        "user": ("vfolders_user", None),
        "user_email": ("users_email", None),
        "creator": ("vfolders_creator", None),
        "usage_mode": ("vfolders_usage_mode", None),
        "permission": ("vfolders_permission", None),
        "ownership_type": ("vfolders_ownership_type", None),
        "max_files": ("vfolders_max_files", None),
        "max_size": ("vfolders_max_size", None),
        "created_at": ("vfolders_created_at", None),
        "last_used": ("vfolders_last_used", None),
        "cloneable": ("vfolders_cloneable", None),
        "status": ("vfolders_status", None),
        "cur_size": ("vfolders_cur_size", None),
    }

    def resolve_created_at(
        self,
        info: graphene.ResolveInfo,
    ) -> datetime:
        try:
            return dtparse(self.created_at)
        except (TypeError, ParserError):
            return self.created_at

    def resolve_modified_at(
        self,
        info: graphene.ResolveInfo,
    ) -> datetime:
        try:
            return dtparse(self.modified_at)
        except (TypeError, ParserError):
            return self.modified_at

    @classmethod
    def parse_model(
        cls,
        graph_ctx: GraphQueryContext,
        vfolder_row: VFolderRow,
        *,
        model_def: dict[str, Any] | None = None,
        readme: str | None = None,
        readme_filetype: str | None = None,
    ) -> Self:
        if model_def is not None:
            models = model_def["models"]
        else:
            models = []
        try:
            metadata = models[0]["metadata"]
            name = models[0]["name"]
        except (IndexError, KeyError):
            metadata = {}
            name = vfolder_row.name
        return cls(
            id=vfolder_row.id,
            row_id=vfolder_row.id,
            vfolder=VirtualFolder.from_orm_row(vfolder_row),
            vfolder_node=VirtualFolderNode.from_row(graph_ctx, vfolder_row),
            name=name,
            author=metadata.get("author") or vfolder_row.creator or "",
            title=metadata.get("title") or vfolder_row.name,
            version=metadata.get("version") or "",
            created_at=metadata.get("created") or vfolder_row.created_at,
            modified_at=metadata.get("last_modified") or vfolder_row.created_at,
            description=metadata.get("description") or "",
            task=metadata.get("task") or "",
            architecture=metadata.get("architecture") or "",
            framework=metadata.get("framework") or [],
            label=metadata.get("label") or [],
            category=metadata.get("category") or "",
            license=metadata.get("license") or "",
            min_resource=metadata.get("min_resource") or {},
            readme=readme,
            readme_filetype=readme_filetype,
        )

    @classmethod
    async def from_row(cls, graph_ctx: GraphQueryContext, vfolder_row: VFolderRow) -> Self | None:
        try:
            return await cls.parse_row(graph_ctx, vfolder_row)
        except Exception as e:
            if isinstance(e, ModelCardProcessError):
                error_msg = e.msg
            else:
                error_msg = "Unknown error"
            if (
                graph_ctx.user["role"] in (UserRole.SUPERADMIN, UserRole.ADMIN)
                or vfolder_row.creator == graph_ctx.user["email"]
            ):
                return cls(
                    id=vfolder_row.id,
                    row_id=vfolder_row.id,
                    name=vfolder_row.name,
                    author=vfolder_row.creator or "",
                    error_msg=error_msg,
                )
            else:
                return None

    @classmethod
    async def parse_row(cls, graph_ctx: GraphQueryContext, vfolder_row: VFolderRow) -> Self | None:
        async def _fetch_file(
            filename: str,
        ) -> bytes:  # FIXME: We should avoid fetching files from disk
            chunks = bytes()
            async with graph_ctx.storage_manager.request(
                proxy_name,
                "POST",
                "folder/file/fetch",
                json={
                    "volume": volume_name,
                    "vfid": str(vfolder_id),
                    "relpath": f"./{filename}",
                },
            ) as (_, storage_resp):
                while True:
                    chunk = await storage_resp.content.read(DEFAULT_CHUNK_SIZE)
                    if not chunk:
                        break
                    chunks += chunk
            return chunks

        vfolder_row_id = vfolder_row.id
        quota_scope_id = vfolder_row.quota_scope_id
        host = vfolder_row.host
        vfolder_id = VFolderID(quota_scope_id, vfolder_row_id)
        proxy_name, volume_name = graph_ctx.storage_manager.get_proxy_and_volume(
            host, is_unmanaged(vfolder_row.unmanaged_path)
        )
        try:
            async with graph_ctx.storage_manager.request(
                proxy_name,
                "POST",
                "folder/file/list",
                json={
                    "volume": volume_name,
                    "vfid": str(vfolder_id),
                    "relpath": ".",
                },
            ) as (_, storage_resp):
                vfolder_files = (await storage_resp.json())["items"]
        except VFolderOperationFailed as e:
            raise ModelCardProcessError(
                f"Failed to fetch definition file from folder. (detail:{e.extra_msg})"
            )

        model_definition_filename: str | None = None
        readme_idx: int | None = None

        for idx, item in enumerate(vfolder_files):
            if (item["name"] in ("model-definition.yml", "model-definition.yaml")) and (
                not model_definition_filename
            ):
                model_definition_filename = item["name"]
            if item["name"].lower().startswith("readme."):
                readme_idx = idx

        if model_definition_filename:
            try:
                chunks = await _fetch_file(model_definition_filename)
            except VFolderOperationFailed as e:
                raise ModelCardProcessError(
                    f"Failed to fetch model definition file (detail:{e.extra_msg})"
                )
            model_definition_yaml = chunks.decode("utf-8")
            try:
                yaml = YAML()
                model_definition_dict = yaml.load(model_definition_yaml)
            except YAMLError as e:
                raise ModelCardProcessError(
                    f"Invalid YAML syntax (data:{model_definition_yaml}, detail:{str(e)})"
                )
            try:
                model_definition = model_definition_iv.check(model_definition_dict)
            except t.DataError as e:
                raise ModelCardProcessError(
                    f"Failed to validate model definition file (data:{model_definition_dict}, detail:{str(e)})"
                )
            assert model_definition is not None
            model_definition["id"] = vfolder_row_id
        else:
            model_definition = None

        if readme_idx is not None:
            readme_filename: str = vfolder_files[readme_idx]["name"]
            try:
                chunks = await _fetch_file(readme_filename)
            except VFolderOperationFailed:
                readme = "Failed to fetch README file."
                readme_filetype = None
            else:
                readme = chunks.decode("utf-8")
                readme_filetype = readme_filename.split(".")[-1]
        else:
            readme = None
            readme_filetype = None

        return cls.parse_model(
            graph_ctx,
            vfolder_row,
            model_def=model_definition,
            readme=readme,
            readme_filetype=readme_filetype,
        )

    @classmethod
    async def get_node(cls, info: graphene.ResolveInfo, id: str) -> Self | None:
        graph_ctx: GraphQueryContext = info.context

        _, vfolder_row_id = AsyncNode.resolve_global_id(info, id)
        async with graph_ctx.db.begin_readonly_session() as db_session:
            vfolder_row = await VFolderRow.get(
                db_session, uuid.UUID(vfolder_row_id), load_user=True, load_group=True
            )
            if vfolder_row.usage_mode != VFolderUsageMode.MODEL:
                raise ValueError(
                    f"The vfolder is not model. expect: {VFolderUsageMode.MODEL.value}, got:"
                    f" {vfolder_row.usage_mode.value}. (id: {vfolder_row_id})"
                )
            if vfolder_row.status in DEAD_VFOLDER_STATUSES:
                raise ValueError(
                    f"The vfolder is deleted. (id: {vfolder_row_id}, status: {vfolder_row.status})"
                )
        return await cls.from_row(graph_ctx, vfolder_row)

    @classmethod
    async def get_connection(
        cls,
        info: graphene.ResolveInfo,
        filter_expr: str | None = None,
        order_expr: str | None = None,
        offset: int | None = None,
        after: str | None = None,
        first: int | None = None,
        before: str | None = None,
        last: int | None = None,
    ) -> ConnectionResolverResult[Self]:
        graph_ctx: GraphQueryContext = info.context
        _filter_arg = (
            FilterExprArg(filter_expr, QueryFilterParser(cls._queryfilter_fieldspec))
            if filter_expr is not None
            else None
        )
        _order_expr = (
            OrderExprArg(order_expr, QueryOrderParser(cls._queryorder_colmap))
            if order_expr is not None
            else None
        )
        (
            query,
            cnt_query,
            _,
            cursor,
            pagination_order,
            page_size,
        ) = generate_sql_info_for_gql_connection(
            info,
            VFolderRow,
            VFolderRow.id,
            _filter_arg,
            _order_expr,
            offset,
            after=after,
            first=first,
            before=before,
            last=last,
        )
        async with graph_ctx.db.begin_readonly_session() as db_session:
            model_store_project_gids = (
                (
                    await db_session.execute(
                        sa.select([GroupRow.id]).where(
                            (GroupRow.type == ProjectType.MODEL_STORE)
                            & (GroupRow.domain_name == graph_ctx.user["domain_name"])
                        )
                    )
                )
                .scalars()
                .all()
            )
            additional_cond = (VFolderRow.status.not_in(DEAD_VFOLDER_STATUSES)) & (
                VFolderRow.group.in_(model_store_project_gids)
            )
            query = query.where(additional_cond)
            cnt_query = cnt_query.where(additional_cond)
            query = query.options(
                joinedload(VFolderRow.user_row),
                joinedload(VFolderRow.group_row),
            )
            vfolder_rows = (await db_session.scalars(query)).all()
            total_cnt = await db_session.scalar(cnt_query)
        result = []
        for vf in vfolder_rows:
            if (_node := await cls.from_row(graph_ctx, vf)) is not None:
                result.append(_node)
            else:
                total_cnt -= 1
        return ConnectionResolverResult(result, cursor, pagination_order, page_size, total_cnt)


class ModelCardConnection(Connection):
    class Meta:
        node = ModelCard
        description = "Added in 24.03.4"
