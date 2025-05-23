"""a class based approach to handling role hierarchy"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/integrations/RoleHierarchy.ipynb.

# %% auto 0
__all__ = ['extract_role_hierarchy', 'get_roles_w_hierarchy', 'calc_role']

# %% ../../nbs/integrations/RoleHierarchy.ipynb 2
import domolibrary.classes.DomoRole as dmdr

# %% ../../nbs/integrations/RoleHierarchy.ipynb 4
def extract_role_hierarchy(
    role: dmdr.DomoRole, hierarchy_delimiter, debug_prn: bool = False
) -> dmdr.DomoRole:  # augments the domo role with a hierarchy INT attribute

    description_arr = role.description.split(hierarchy_delimiter)

    if len(description_arr) != 1:
        hierarchy = int(description_arr[1])

    elif role.is_system_role:
        hierarchy = (5 - role.id) * 2 + 1

    else:
        hierarchy = 0

    role.hierarchy = hierarchy

    if debug_prn:
        print(
            {
                "description_arr": description_arr,
                "role_id": role.id,
                "hierarchy": hierarchy,
            }
        )

    return role

# %% ../../nbs/integrations/RoleHierarchy.ipynb 5
async def get_roles_w_hierarchy(
    auth,
    hierarchy_delimiter=" - h",  # post fix to delimit hierarchy number.  assumes scale of 1:10, system accounts will be included.
    debug_prn: bool = False,
    debug_api: bool = False,
):
    """gets instance roles and adds an attribute hierarchy"""

    domo_config = dmdr.DomoRoles(auth=auth)
    domo_roles = await domo_config.get( debug_api=debug_api)
    return [
        extract_role_hierarchy(
            role=role, hierarchy_delimiter=hierarchy_delimiter, debug_prn=debug_prn
        )
        for role in domo_roles
    ]

# %% ../../nbs/integrations/RoleHierarchy.ipynb 7
async def calc_role(
    current_role_id,
    new_role_name,
    auth,
    hierarchy_delimiter=" - h",
    is_alter_system_roles: bool = False,  # by default calc role will not apply to system roles and will always update to a system role
    debug_prn: bool = False,
):
    """compares current role to new role hierarchy and returns the higher one.  will not adjust system roles"""

    instance_roles = await get_roles_w_hierarchy(
        auth=auth, hierarchy_delimiter=hierarchy_delimiter
    )

    current_role = next((role for role in instance_roles if role.id == current_role_id))

    if current_role.is_system_role and not is_alter_system_roles:
        print(f"{current_role.name} is a system role -- no changes")
        return current_role

    expected_role = next(
        (role for role in instance_roles if role.name == new_role_name), None
    )

    if not expected_role:
        raise Exception(f"{new_role_name} not found in {auth.domo_instance}")

    if current_role.hierarchy >= expected_role.hierarchy:
        if debug_prn:
            print(
                f"do nothing:  {current_role.name} - {current_role.hierarchy} exceeds or equals {expected_role.name} - {expected_role.hierarchy}"
            )
        return current_role

    if debug_prn:
        print(
            f"upgrade role: {current_role.name} - {current_role.hierarchy} to a {expected_role.name} - {expected_role.hierarchy}"
        )
    return expected_role
