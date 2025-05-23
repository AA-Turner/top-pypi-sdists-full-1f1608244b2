# Code generated - EDITING IS FUTILE. DO NOT EDIT.

import enum
from ..cog import variants as cogvariants
import typing
from ..models import dashboard
from ..cog import runtime as cogruntime


class QueryEditorMode(enum.StrEnum):
    CODE = "code"
    BUILDER = "builder"


class LokiQueryType(enum.StrEnum):
    RANGE = "range"
    INSTANT = "instant"
    STREAM = "stream"


class SupportingQueryType(enum.StrEnum):
    LOGS_VOLUME = "logsVolume"
    LOGS_SAMPLE = "logsSample"
    DATA_SAMPLE = "dataSample"


class LokiQueryDirection(enum.StrEnum):
    FORWARD = "forward"
    BACKWARD = "backward"


class Dataquery(cogvariants.Dataquery):
    # The LogQL query.
    expr: str
    # Used to override the name of the series.
    legend_format: typing.Optional[str]
    # Used to limit the number of log rows returned.
    max_lines: typing.Optional[int]
    # @deprecated, now use step.
    resolution: typing.Optional[int]
    editor_mode: typing.Optional['QueryEditorMode']
    # @deprecated, now use queryType.
    range_val: typing.Optional[bool]
    # @deprecated, now use queryType.
    instant: typing.Optional[bool]
    # Used to set step value for range queries.
    step: typing.Optional[str]
    # A unique identifier for the query within the list of targets.
    # In server side expressions, the refId is used as a variable name to identify results.
    # By default, the UI will assign A->Z; however setting meaningful names may be useful.
    ref_id: str
    # true if query is disabled (ie should not be returned to the dashboard)
    # Note this does not always imply that the query should not be executed since
    # the results from a hidden query may be used as the input to other queries (SSE etc)
    hide: typing.Optional[bool]
    # Specify the query flavor
    # TODO make this required and give it a default
    query_type: typing.Optional[str]
    # For mixed data sources the selected datasource is on the query level.
    # For non mixed scenarios this is undefined.
    # TODO find a better way to do this ^ that's friendly to schema
    # TODO this shouldn't be unknown but DataSourceRef | null
    datasource: typing.Optional[dashboard.DataSourceRef]

    def __init__(self, expr: str = "", legend_format: typing.Optional[str] = None, max_lines: typing.Optional[int] = None, resolution: typing.Optional[int] = None, editor_mode: typing.Optional['QueryEditorMode'] = None, range_val: typing.Optional[bool] = None, instant: typing.Optional[bool] = None, step: typing.Optional[str] = None, ref_id: str = "", hide: typing.Optional[bool] = None, query_type: typing.Optional[str] = None, datasource: typing.Optional[dashboard.DataSourceRef] = None):
        self.expr = expr
        self.legend_format = legend_format
        self.max_lines = max_lines
        self.resolution = resolution
        self.editor_mode = editor_mode
        self.range_val = range_val
        self.instant = instant
        self.step = step
        self.ref_id = ref_id
        self.hide = hide
        self.query_type = query_type
        self.datasource = datasource

    def to_json(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "expr": self.expr,
            "refId": self.ref_id,
        }
        if self.legend_format is not None:
            payload["legendFormat"] = self.legend_format
        if self.max_lines is not None:
            payload["maxLines"] = self.max_lines
        if self.resolution is not None:
            payload["resolution"] = self.resolution
        if self.editor_mode is not None:
            payload["editorMode"] = self.editor_mode
        if self.range_val is not None:
            payload["range"] = self.range_val
        if self.instant is not None:
            payload["instant"] = self.instant
        if self.step is not None:
            payload["step"] = self.step
        if self.hide is not None:
            payload["hide"] = self.hide
        if self.query_type is not None:
            payload["queryType"] = self.query_type
        if self.datasource is not None:
            payload["datasource"] = self.datasource
        return payload

    @classmethod
    def from_json(cls, data: dict[str, typing.Any]) -> typing.Self:
        args: dict[str, typing.Any] = {}
        
        if "expr" in data:
            args["expr"] = data["expr"]
        if "legendFormat" in data:
            args["legend_format"] = data["legendFormat"]
        if "maxLines" in data:
            args["max_lines"] = data["maxLines"]
        if "resolution" in data:
            args["resolution"] = data["resolution"]
        if "editorMode" in data:
            args["editor_mode"] = data["editorMode"]
        if "range" in data:
            args["range_val"] = data["range"]
        if "instant" in data:
            args["instant"] = data["instant"]
        if "step" in data:
            args["step"] = data["step"]
        if "refId" in data:
            args["ref_id"] = data["refId"]
        if "hide" in data:
            args["hide"] = data["hide"]
        if "queryType" in data:
            args["query_type"] = data["queryType"]
        if "datasource" in data:
            args["datasource"] = dashboard.DataSourceRef.from_json(data["datasource"])        

        return cls(**args)





def variant_config() -> cogruntime.DataqueryConfig:
    return cogruntime.DataqueryConfig(
        identifier="loki",
        from_json_hook=Dataquery.from_json,
    )

