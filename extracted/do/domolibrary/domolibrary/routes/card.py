# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routes/card.ipynb.

# %% auto 0
__all__ = ['Cards_API_Exception', 'CardSearch_NotFoundError', 'get_card_by_id', 'get_kpi_definition', 'Card_OptionalParts_Enum',
           'get_card_metadata', 'generate_body_search_cards_only_apps_filter',
           'generate_body_search_cards_admin_summary', 'search_cards_admin_summary']

# %% ../../nbs/routes/card.ipynb 2
from typing import List, Union
from enum import Enum

import httpx

import domolibrary.client.get_data as gd
import domolibrary.client.ResponseGetData as rgd
import domolibrary.client.DomoAuth as dmda
import domolibrary.client.DomoError as de

# %% ../../nbs/routes/card.ipynb 5
class Cards_API_Exception(de.DomoError):
    def __init__(self, res, message=None):

        super().__init__(res=res, message=message)

class CardSearch_NotFoundError(de.DomoError):
    def __init__(
        self,
        card_id,
        domo_instance,
        function_name,
        status,
        parent_class: str = None,
        message=None,
    ):
        super().__init__(
            status=status,
            message=message or f"card {card_id} not found",
            domo_instance=domo_instance,
            function_name=function_name,
            parent_class=parent_class,
        )

# %% ../../nbs/routes/card.ipynb 6
@gd.route_function
async def get_card_by_id(
    card_id,
    auth: dmda.DomoAuth,
    optional_parts="certification,datasources,drillPath,owners,properties,domoapp",
    debug_api: bool = False,
    debug_num_stacks_to_drop = 1,
    session : httpx.AsyncClient = None,
    parent_class :str = None,
    return_raw: bool = False,
):
    url = f"https://{auth.domo_instance}.domo.com/api/content/v1/cards/"

    params = {"parts": optional_parts, "urns": card_id}

    res = await gd.get_data(
        auth=auth,
        method="GET",
        url=url,
        session = session,
        num_stacks_to_drop = debug_num_stacks_to_drop,
        parent_class= parent_class,
        debug_api=debug_api,
        params=params,
    )

    if not res.is_success:
        raise Cards_API_Exception(res=res)

    if return_raw:
        return res

    res.response = res.response[0]

    return res

# %% ../../nbs/routes/card.ipynb 8
@gd.route_function
async def get_kpi_definition(
    auth: dmda.DomoAuth,
    card_id: str,
    debug_api: bool = False,
    session: httpx.AsyncClient = None,
    parent_class: str = None,
    debug_num_stacks_to_drop=2,
) -> rgd.ResponseGetData:
    
    url = f"https://{auth.domo_instance}.domo.com/api/content/v3/cards/kpi/definition"

    body = {"urn": card_id}

    res = await gd.get_data(
        auth=auth,
        url=url,
        method="PUT",
        body=body,
        debug_api=debug_api,
        session=session,
        parent_class=parent_class,
        num_stacks_to_drop=debug_num_stacks_to_drop,
    )

    if not res.is_success and res.response == "Not Found":
        raise CardSearch_NotFoundError(
            card_id=card_id,
            status=res.status,
            domo_instance=auth.domo_instance,
            function_name="get_kpi_definition",
        )

    return res

# %% ../../nbs/routes/card.ipynb 11
class Card_OptionalParts_Enum(Enum):
    CERTIFICATION = "certification"
    DATASOURCES = "datasources"
    DOMOAPP = "domoapp"
    DRILLPATH = "drillPath"
    MASONDATA = "masonData"
    METADATA = "metadata"
    OWNERS = "owners"
    PROBLEMS = "problems"
    PROPERTIES = "properties"


@gd.route_function
async def get_card_metadata(
    auth: dmda.DomoAuth,
    card_id: str,
    debug_api: bool = False,
    session: httpx.AsyncClient = None,
    parent_class: str = None,
    debug_num_stacks_to_drop=1,
    optional_parts: Union[
        List[Card_OptionalParts_Enum], str
    ] = "metadata,certification,datasources,owners,problems,domoapp",
) -> rgd.ResponseGetData:

    url = f"https://{auth.domo_instance}.domo.com/api/content/v1/cards"

    params = {"urns": card_id, "parts": optional_parts}

    res = await gd.get_data(
        auth=auth,
        url=url,
        method="GET",
        params=params,
        debug_api=debug_api,
        session=session,
        parent_class=parent_class,
        num_stacks_to_drop=debug_num_stacks_to_drop,
    )

    if not res.is_success:
        raise Cards_API_Exception(res=res)

    if res.is_success and len(res.response) == 0:

        raise CardSearch_NotFoundError(
            card_id=card_id,
            status=res.status,
            domo_instance=auth.domo_instance,
            parent_class=parent_class,
            function_name=res.traceback_details.function_name,
        )

    res.response = res.response[0]

    return res

# %% ../../nbs/routes/card.ipynb 14
def generate_body_search_cards_only_apps_filter():
    return {
        "includeCardTypeClause": True,
        "cardTypes": ["domoapp", "mason", "custom"],
        "ascending": True,
        "orderBy": "cardTitle",
    }

def generate_body_search_cards_admin_summary(
    page_ids: List[str] = None,
    #  searchPages: bool = True,
    card_search_text: str = None,
    page_search_text: str = None,
) -> dict:
    body = {"ascending": True, "orderBy": "cardTitle"}

    if card_search_text:
        body.update(
            {"cardTitleSearchText": card_search_text, "includeCardTitleClause": True}
        )

    if page_search_text:
        body.update(
            {
                "pageTitleSearchText": page_search_text,
                "includePageTitleClause": True,
                "notOnPage": False,
            }
        )

    if page_ids:
        body.update({"pageIds": page_ids})

    return body

# %% ../../nbs/routes/card.ipynb 15
@gd.route_function
async def search_cards_admin_summary(
    auth: dmda.DomoAuth,
    body: dict,
    maximum: int = None,
    optional_parts : str = 'certification,datasources,drillPath,owners,properties,domoapp',
    debug_api: bool = False,
    debug_loop: bool = False,
    session: httpx.AsyncClient = None,
    wait_sleep: int = 3,
    parent_class: str = None,
    debug_num_stacks_to_drop: int = 1,
) -> rgd.ResponseGetData:
    limit = 100
    offset = 0
    loop_until_end = False if maximum else True

    url = f"https://{auth.domo_instance}.domo.com/api/content/v2/cards/adminsummary"

    params = {'parts' : optional_parts}

    offset_params = {
        "offset": "skip",
        "limit": "limit",
    }

    def arr_fn(res):
        return res.response.get("cardAdminSummaries", [])

    res = await gd.looper(
        auth=auth,
        method="POST",
        url=url,
        arr_fn=arr_fn,
        offset_params=offset_params,
        offset_params_in_body= False,
        limit=limit,
        skip=offset,
        body=body,
        maximum=maximum,fixed_params = params,
        session=session,
        debug_api=debug_api,
        debug_loop=debug_loop,
        loop_until_end=loop_until_end,
        wait_sleep=wait_sleep,
        parent_class=parent_class,
        debug_num_stacks_to_drop=debug_num_stacks_to_drop,
    )

    if not res.is_success:
        raise Cards_API_Exception(res=res)
    
    return res
