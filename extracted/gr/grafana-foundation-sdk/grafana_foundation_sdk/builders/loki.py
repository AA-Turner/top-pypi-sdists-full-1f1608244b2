# Code generated - EDITING IS FUTILE. DO NOT EDIT.

import typing
from ..cog import builder as cogbuilder
from ..models import loki
from ..models import dashboard


class Dataquery(cogbuilder.Builder[loki.Dataquery]):
    _internal: loki.Dataquery

    def __init__(self):
        self._internal = loki.Dataquery()

    def build(self) -> loki.Dataquery:
        """
        Builds the object.
        """
        return self._internal    
    
    def expr(self, expr: str) -> typing.Self:    
        """
        The LogQL query.
        """
            
        self._internal.expr = expr
    
        return self
    
    def legend_format(self, legend_format: str) -> typing.Self:    
        """
        Used to override the name of the series.
        """
            
        self._internal.legend_format = legend_format
    
        return self
    
    def max_lines(self, max_lines: int) -> typing.Self:    
        """
        Used to limit the number of log rows returned.
        """
            
        self._internal.max_lines = max_lines
    
        return self
    
    def resolution(self, resolution: int) -> typing.Self:    
        """
        @deprecated, now use step.
        """
            
        self._internal.resolution = resolution
    
        return self
    
    def editor_mode(self, editor_mode: loki.QueryEditorMode) -> typing.Self:    
        self._internal.editor_mode = editor_mode
    
        return self
    
    def range(self, range_val: bool) -> typing.Self:    
        """
        @deprecated, now use queryType.
        """
            
        self._internal.range_val = range_val
    
        return self
    
    def instant(self, instant: bool) -> typing.Self:    
        """
        @deprecated, now use queryType.
        """
            
        self._internal.instant = instant
    
        return self
    
    def step(self, step: str) -> typing.Self:    
        """
        Used to set step value for range queries.
        """
            
        self._internal.step = step
    
        return self
    
    def ref_id(self, ref_id: str) -> typing.Self:    
        """
        A unique identifier for the query within the list of targets.
        In server side expressions, the refId is used as a variable name to identify results.
        By default, the UI will assign A->Z; however setting meaningful names may be useful.
        """
            
        self._internal.ref_id = ref_id
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        """
        true if query is disabled (ie should not be returned to the dashboard)
        Note this does not always imply that the query should not be executed since
        the results from a hidden query may be used as the input to other queries (SSE etc)
        """
            
        self._internal.hide = hide
    
        return self
    
    def query_type(self, query_type: str) -> typing.Self:    
        """
        Specify the query flavor
        TODO make this required and give it a default
        """
            
        self._internal.query_type = query_type
    
        return self
    
    def datasource(self, datasource: dashboard.DataSourceRef) -> typing.Self:    
        """
        For mixed data sources the selected datasource is on the query level.
        For non mixed scenarios this is undefined.
        TODO find a better way to do this ^ that's friendly to schema
        TODO this shouldn't be unknown but DataSourceRef | null
        """
            
        self._internal.datasource = datasource
    
        return self
    
