from typing import TYPE_CHECKING

from ..._content_data import Data
from ..._content_provider_layer import ContentUsageLoggerMixin
from ...._content_type import ContentType
from ...._tools import validate_bool_value, try_copy_to_list
from ..._header_type import get_header_type_by_use_field_names_in_headers
from ....delivery._data._data_provider import DataProviderLayer, Response

if TYPE_CHECKING:
    from ...._types import StrStrings, ExtendedParams


class Definition(
    ContentUsageLoggerMixin[Response[Data]],
    DataProviderLayer[Response[Data]],
):
    """
    Describes the parameters used to retrieve the estimated summary values for KPI measures for annual periods.

    Parameters
    ----------
    universe: str, list of str
        Single instrument or list of instruments.
    use_field_names_in_headers: bool, optional
        Boolean that indicates whether or not to display field names in the headers.
    extended_params: ExtendedParams, optional
        Specifies the parameters that will be merged with the request.

    Examples
    --------
    >>> from lseg.data.content import estimates
    >>> definition = estimates.view_summary_kpi.annual.Definition(universe="ORCL.N")
    >>> response = definition.get_data()
    """

    _USAGE_CLS_NAME = "Estimates.SummaryKPI.AnnualDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)
        header_type = get_header_type_by_use_field_names_in_headers(use_field_names_in_headers)

        super().__init__(
            ContentType.ESTIMATES_VIEW_SUMMARY_KPI_ANNUAL,
            universe=universe,
            header_type=header_type,
            extended_params=extended_params,
        )
