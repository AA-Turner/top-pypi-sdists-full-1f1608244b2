# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/classes/50_DomoInstanceConfig_InstanceSwitcher.ipynb.

# %% auto 0
__all__ = ['DomoInstanceConfig_InstanceSwitcher_Mapping', 'DomoInstanceConfig_InstanceSwitcher']

# %% ../../nbs/classes/50_DomoInstanceConfig_InstanceSwitcher.ipynb 2
from ..routes.instance_config_instance_switcher import (InstanceSwitcherMapping_GET_Error,InstanceSwitcherMapping_CRUD_Error) 

# %% ../../nbs/classes/50_DomoInstanceConfig_InstanceSwitcher.ipynb 3
from dataclasses import dataclass, field
from typing import List

import httpx

import domolibrary.client.DomoAuth as dmda

import domolibrary.routes.instance_config_instance_switcher as instance_switcher_routes

# %% ../../nbs/classes/50_DomoInstanceConfig_InstanceSwitcher.ipynb 6
@dataclass
class DomoInstanceConfig_InstanceSwitcher_Mapping:
    user_attribute: str
    target_instance: str  # instance user is granted access to / can switch to

    def __post_init__(self):
        self.target_instance = self.target_instance.replace(".domo.com", "")
        
    def __eq__(self, other):  # dunder method allows us to test for equality
        if type(self) != type(other):
            return False
        else:
            return (
                self.target_instance == other.target_instance
                and self.user_attribute == other.user_attribute
            )

    def __lt__(self, other):
        return (
            self.target_instance < other.target_instance
            and self.user_attribute < other.user_attribute
        )

    @classmethod
    def from_obj(cls, obj: dict):
        return cls(
            user_attribute=obj["userAttribute"],
            target_instance=obj["instance"],
        )

    def to_json(self):
        return {
            "userAttribute": self.user_attribute,
            "instance": self.target_instance + ".domo.com",
        }

# %% ../../nbs/classes/50_DomoInstanceConfig_InstanceSwitcher.ipynb 7
@dataclass
class DomoInstanceConfig_InstanceSwitcher:
    auth: dmda.DomoAuth = field(repr=False)
    domo_instance_switcher_mapping: List[
        DomoInstanceConfig_InstanceSwitcher_Mapping
    ] = field(default_factory=list)

    def _add_mapping_to_ls(
        self,
        domo_instance_switcher_mapping: DomoInstanceConfig_InstanceSwitcher_Mapping,
    ):
        """deduplication when adding to existing mapping"""

        if domo_instance_switcher_mapping not in self.domo_instance_switcher_mapping:
            self.domo_instance_switcher_mapping.append(domo_instance_switcher_mapping)
        return self.domo_instance_switcher_mapping

    async def get_mapping(
        self,
        debug_api: bool = False,
        return_raw: bool = False,
        session: httpx.AsyncClient = None,
        debug_num_stacks_to_drop=2,
    ):
        res = await instance_switcher_routes.get_instance_switcher_mapping(
            auth=self.auth,
            debug_api=debug_api,
            session=session,
            parent_class=self.__class__.__name__,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop,
        )

        if return_raw:
            return res

        for obj in res.response:
            self._add_mapping_to_ls(
                DomoInstanceConfig_InstanceSwitcher_Mapping.from_obj(
                    obj=obj
                )
            )

        return self.domo_instance_switcher_mapping

    async def set_mapping(
        self,
        mapping_ls: List[
            DomoInstanceConfig_InstanceSwitcher_Mapping
        ] = None,  # will default to self.domo_instance_switcher_mapping
        session: httpx.AsyncClient = None,
        debug_api: bool = False,
        return_raw: bool = False,
        debug_num_stacks_to_drop=2,
    ):
        """overwrite existing mapping and sets mapping_ls as new mapping"""

        # structure payload appropriately
        mapping_ls = mapping_ls or self.domo_instance_switcher_mapping

        mapping_payloads = [domo_mapping.to_json() for domo_mapping in mapping_ls]

        # update routing mappings
        res = await instance_switcher_routes.set_instance_switcher_mapping(
            auth=self.auth,
            mapping_payloads=mapping_payloads,
            session=session,
            debug_api=debug_api,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop,
        )

        if return_raw:  # returns api response
            return res

        return await self.get_mapping(
            session=session, debug_api=debug_api
        )  # returns updated list of classes

    async def add_mapping(
        self,
        mapping_to_add_ls: List[DomoInstanceConfig_InstanceSwitcher_Mapping],
        session: httpx.AsyncClient = None,
        debug_api: bool = False,
        debug_num_stacks_to_drop=2,
    ):
        """takes mapping_ls and adds to existing mapping"""

        # get existing mapping
        await self.get_mapping(
            debug_api=debug_api,
            session=session,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop + 1,
        )

        for domo_mapping in mapping_to_add_ls:
            self._add_mapping_to_ls(domo_mapping)

        # update routing mappings
        return await self.set_mapping(
            session=session,
            debug_api=debug_api,
            debug_num_stacks_to_drop=debug_num_stacks_to_drop + 1,
        )
