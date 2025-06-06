"""
Management of MongoDB Databases
===============================

:depends:   - pymongo Python module

Only deletion is supported, creation doesn't make sense and can be done using
:py:func:`mongodb_user.present <salt.states.mongodb_user.present>`.
"""

# Define the module's virtual name
__virtualname__ = "mongodb_database"


def __virtual__():
    if "mongodb.db_exists" in __salt__:
        return __virtualname__
    return (False, "mongodb module could not be loaded")


def absent(name, user=None, password=None, host=None, port=None, authdb=None):
    """
    Ensure that the named database is absent. Note that creation doesn't make
    sense in MongoDB.

    name
        The name of the database to remove

    user
        The user to connect as (must be able to create the user)

    password
        The password of the user

    host
        The host to connect to

    port
        The port to connect to

    authdb
        The database in which to authenticate
    """
    ret = {"name": name, "changes": {}, "result": True, "comment": ""}

    if __salt__["mongodb.db_exists"](name, user, password, host, port, authdb=authdb):
        if __opts__["test"]:
            ret["result"] = None
            ret["comment"] = "Database {} is present and needs to be removed".format(
                name
            )
            return ret
        if __salt__["mongodb.db_remove"](
            name, user, password, host, port, authdb=authdb
        ):
            ret["comment"] = f"Database {name} has been removed"
            ret["changes"][name] = "Absent"
            return ret

    ret["comment"] = f"Database {name} is not present"
    return ret
