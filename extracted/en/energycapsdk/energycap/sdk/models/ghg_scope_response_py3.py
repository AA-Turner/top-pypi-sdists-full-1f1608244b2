# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GHGScopeResponse(Model):
    """GHGScopeResponse.

    :param scope_id: The Scope Identifier
    :type scope_id: int
    :param scope_info: The Scope Info
    :type scope_info: str
    :param scope_categories: The list of Scope Categories under this scope
    :type scope_categories: list[~energycap.sdk.models.GHGScopeCategoryChild]
    """

    _attribute_map = {
        'scope_id': {'key': 'scopeId', 'type': 'int'},
        'scope_info': {'key': 'scopeInfo', 'type': 'str'},
        'scope_categories': {'key': 'scopeCategories', 'type': '[GHGScopeCategoryChild]'},
    }

    def __init__(self, *, scope_id: int=None, scope_info: str=None, scope_categories=None, **kwargs) -> None:
        super(GHGScopeResponse, self).__init__(**kwargs)
        self.scope_id = scope_id
        self.scope_info = scope_info
        self.scope_categories = scope_categories
