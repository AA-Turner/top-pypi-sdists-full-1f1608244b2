from __future__ import annotations
from pydantic import model_validator
from maleo_foundation.models.schemas.general import BaseGeneralSchemas
from maleo_foundation.models.schemas.result import BaseResultSchemas

class BaseServiceQueryResultsTransfers:
    class Row(
        BaseGeneralSchemas.Status,
        BaseGeneralSchemas.Timestamps,
        BaseGeneralSchemas.Identifiers,
        BaseResultSchemas.BaseRow
    ): pass

    class Fail(BaseResultSchemas.Fail): pass

    class NotFound(BaseResultSchemas.NotFound): pass

    class NoData(BaseResultSchemas.NoData): pass

    class SingleData(BaseResultSchemas.SingleData):
        data:BaseServiceQueryResultsTransfers.Row

    class UnpaginatedMultipleData(BaseResultSchemas.UnpaginatedMultipleData):
        data:list[BaseServiceQueryResultsTransfers.Row]

    class PaginatedMultipleData(BaseResultSchemas.PaginatedMultipleData):
        data:list[BaseServiceQueryResultsTransfers.Row]

        @model_validator(mode="before")
        @classmethod
        def calculate_pagination(cls, values: dict) -> dict:
            """Calculates pagination metadata before validation."""
            total_data = values.get("total_data", 0)
            data = values.get("data", [])

            #* Get pagination values from inherited SimplePagination
            page = values.get("page", 1)
            limit = values.get("limit", 10)

            #* Calculate total pages
            total_pages = (total_data // limit) + (1 if total_data % limit > 0 else 0)

            #* Assign computed pagination object before validation
            values["pagination"] = BaseGeneralSchemas.ExtendedPagination(
                page=page,
                limit=limit,
                data_count=len(data),
                total_data=total_data,
                total_pages=total_pages
            )
            return values