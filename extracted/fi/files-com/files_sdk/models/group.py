import builtins  # noqa: F401
from files_sdk.api import Api  # noqa: F401
from files_sdk.list_obj import ListObj
from files_sdk.error import (  # noqa: F401
    InvalidParameterError,
    MissingParameterError,
    NotImplementedError,
)


class Group:
    default_attributes = {
        "id": None,  # int64 - Group ID
        "name": None,  # string - Group name
        "allowed_ips": None,  # string - A list of allowed IPs if applicable.  Newline delimited
        "admin_ids": None,  # string - Comma-delimited list of user IDs who are group administrators (separated by commas)
        "notes": None,  # string - Notes about this group
        "user_ids": None,  # string - Comma-delimited list of user IDs who belong to this group (separated by commas)
        "usernames": None,  # string - Comma-delimited list of usernames who belong to this group (separated by commas)
        "ftp_permission": None,  # boolean - If true, users in this group can use FTP to login.  This will override a false value of `ftp_permission` on the user level.
        "sftp_permission": None,  # boolean - If true, users in this group can use SFTP to login.  This will override a false value of `sftp_permission` on the user level.
        "dav_permission": None,  # boolean - If true, users in this group can use WebDAV to login.  This will override a false value of `dav_permission` on the user level.
        "restapi_permission": None,  # boolean - If true, users in this group can use the REST API to login.  This will override a false value of `restapi_permission` on the user level.
        "site_id": None,  # int64 - Site ID
    }

    def __init__(self, attributes=None, options=None):
        if not isinstance(attributes, dict):
            attributes = {}
        if not isinstance(options, dict):
            options = {}
        self.set_attributes(attributes)
        self.options = options

    def set_attributes(self, attributes):
        for attribute, default_value in Group.default_attributes.items():
            setattr(self, attribute, attributes.get(attribute, default_value))

    def get_attributes(self):
        return {
            k: getattr(self, k, None)
            for k in Group.default_attributes
            if getattr(self, k, None) is not None
        }

    # Parameters:
    #   notes - string - Group notes.
    #   user_ids - string - A list of user ids. If sent as a string, should be comma-delimited.
    #   admin_ids - string - A list of group admin user ids. If sent as a string, should be comma-delimited.
    #   ftp_permission - boolean - If true, users in this group can use FTP to login.  This will override a false value of `ftp_permission` on the user level.
    #   sftp_permission - boolean - If true, users in this group can use SFTP to login.  This will override a false value of `sftp_permission` on the user level.
    #   dav_permission - boolean - If true, users in this group can use WebDAV to login.  This will override a false value of `dav_permission` on the user level.
    #   restapi_permission - boolean - If true, users in this group can use the REST API to login.  This will override a false value of `restapi_permission` on the user level.
    #   allowed_ips - string - A list of allowed IPs if applicable.  Newline delimited
    #   name - string - Group name.
    def update(self, params=None):
        if not isinstance(params, dict):
            params = {}

        if hasattr(self, "id") and self.id:
            params["id"] = self.id
        else:
            raise MissingParameterError("Current object doesn't have a id")
        if "id" not in params:
            raise MissingParameterError("Parameter missing: id")
        if "id" in params and not isinstance(params["id"], int):
            raise InvalidParameterError("Bad parameter: id must be an int")
        if "notes" in params and not isinstance(params["notes"], str):
            raise InvalidParameterError("Bad parameter: notes must be an str")
        if "user_ids" in params and not isinstance(params["user_ids"], str):
            raise InvalidParameterError(
                "Bad parameter: user_ids must be an str"
            )
        if "admin_ids" in params and not isinstance(params["admin_ids"], str):
            raise InvalidParameterError(
                "Bad parameter: admin_ids must be an str"
            )
        if "allowed_ips" in params and not isinstance(
            params["allowed_ips"], str
        ):
            raise InvalidParameterError(
                "Bad parameter: allowed_ips must be an str"
            )
        if "name" in params and not isinstance(params["name"], str):
            raise InvalidParameterError("Bad parameter: name must be an str")
        response, _options = Api.send_request(
            "PATCH",
            "/groups/{id}".format(id=params["id"]),
            params,
            self.options,
        )
        return response.data

    def delete(self, params=None):
        if not isinstance(params, dict):
            params = {}

        if hasattr(self, "id") and self.id:
            params["id"] = self.id
        else:
            raise MissingParameterError("Current object doesn't have a id")
        if "id" not in params:
            raise MissingParameterError("Parameter missing: id")
        if "id" in params and not isinstance(params["id"], int):
            raise InvalidParameterError("Bad parameter: id must be an int")
        Api.send_request(
            "DELETE",
            "/groups/{id}".format(id=params["id"]),
            params,
            self.options,
        )

    def destroy(self, params=None):
        self.delete(params)

    def save(self):
        if hasattr(self, "id") and self.id:
            new_obj = self.update(self.get_attributes())
            self.set_attributes(new_obj.get_attributes())
            return True
        else:
            new_obj = create(self.get_attributes(), self.options)
            self.set_attributes(new_obj.get_attributes())
            return True


# Parameters:
#   cursor - string - Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
#   per_page - int64 - Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
#   sort_by - object - If set, sort records by the specified field in either `asc` or `desc` direction. Valid fields are `site_id` and `name`.
#   filter - object - If set, return records where the specified field is equal to the supplied value. Valid fields are `name`.
#   filter_prefix - object - If set, return records where the specified field is prefixed by the supplied value. Valid fields are `name`.
#   ids - string - Comma-separated list of group ids to include in results.
#   include_parent_site_groups - boolean - Include groups from the parent site.
def list(params=None, options=None):
    if not isinstance(params, dict):
        params = {}
    if not isinstance(options, dict):
        options = {}
    if "cursor" in params and not isinstance(params["cursor"], str):
        raise InvalidParameterError("Bad parameter: cursor must be an str")
    if "per_page" in params and not isinstance(params["per_page"], int):
        raise InvalidParameterError("Bad parameter: per_page must be an int")
    if "sort_by" in params and not isinstance(params["sort_by"], dict):
        raise InvalidParameterError("Bad parameter: sort_by must be an dict")
    if "filter" in params and not isinstance(params["filter"], dict):
        raise InvalidParameterError("Bad parameter: filter must be an dict")
    if "filter_prefix" in params and not isinstance(
        params["filter_prefix"], dict
    ):
        raise InvalidParameterError(
            "Bad parameter: filter_prefix must be an dict"
        )
    if "ids" in params and not isinstance(params["ids"], str):
        raise InvalidParameterError("Bad parameter: ids must be an str")
    if "include_parent_site_groups" in params and not isinstance(
        params["include_parent_site_groups"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: include_parent_site_groups must be an bool"
        )
    return ListObj(Group, "GET", "/groups", params, options)


def all(params=None, options=None):
    list(params, options)


# Parameters:
#   id (required) - int64 - Group ID.
def find(id, params=None, options=None):
    if not isinstance(params, dict):
        params = {}
    if not isinstance(options, dict):
        options = {}
    params["id"] = id
    if "id" in params and not isinstance(params["id"], int):
        raise InvalidParameterError("Bad parameter: id must be an int")
    if "id" not in params:
        raise MissingParameterError("Parameter missing: id")
    response, options = Api.send_request(
        "GET", "/groups/{id}".format(id=params["id"]), params, options
    )
    return Group(response.data, options)


def get(id, params=None, options=None):
    find(id, params, options)


# Parameters:
#   notes - string - Group notes.
#   user_ids - string - A list of user ids. If sent as a string, should be comma-delimited.
#   admin_ids - string - A list of group admin user ids. If sent as a string, should be comma-delimited.
#   ftp_permission - boolean - If true, users in this group can use FTP to login.  This will override a false value of `ftp_permission` on the user level.
#   sftp_permission - boolean - If true, users in this group can use SFTP to login.  This will override a false value of `sftp_permission` on the user level.
#   dav_permission - boolean - If true, users in this group can use WebDAV to login.  This will override a false value of `dav_permission` on the user level.
#   restapi_permission - boolean - If true, users in this group can use the REST API to login.  This will override a false value of `restapi_permission` on the user level.
#   allowed_ips - string - A list of allowed IPs if applicable.  Newline delimited
#   name (required) - string - Group name.
def create(params=None, options=None):
    if not isinstance(params, dict):
        params = {}
    if not isinstance(options, dict):
        options = {}
    if "notes" in params and not isinstance(params["notes"], str):
        raise InvalidParameterError("Bad parameter: notes must be an str")
    if "user_ids" in params and not isinstance(params["user_ids"], str):
        raise InvalidParameterError("Bad parameter: user_ids must be an str")
    if "admin_ids" in params and not isinstance(params["admin_ids"], str):
        raise InvalidParameterError("Bad parameter: admin_ids must be an str")
    if "ftp_permission" in params and not isinstance(
        params["ftp_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: ftp_permission must be an bool"
        )
    if "sftp_permission" in params and not isinstance(
        params["sftp_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: sftp_permission must be an bool"
        )
    if "dav_permission" in params and not isinstance(
        params["dav_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: dav_permission must be an bool"
        )
    if "restapi_permission" in params and not isinstance(
        params["restapi_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: restapi_permission must be an bool"
        )
    if "allowed_ips" in params and not isinstance(params["allowed_ips"], str):
        raise InvalidParameterError(
            "Bad parameter: allowed_ips must be an str"
        )
    if "name" in params and not isinstance(params["name"], str):
        raise InvalidParameterError("Bad parameter: name must be an str")
    if "name" not in params:
        raise MissingParameterError("Parameter missing: name")
    response, options = Api.send_request("POST", "/groups", params, options)
    return Group(response.data, options)


# Parameters:
#   notes - string - Group notes.
#   user_ids - string - A list of user ids. If sent as a string, should be comma-delimited.
#   admin_ids - string - A list of group admin user ids. If sent as a string, should be comma-delimited.
#   ftp_permission - boolean - If true, users in this group can use FTP to login.  This will override a false value of `ftp_permission` on the user level.
#   sftp_permission - boolean - If true, users in this group can use SFTP to login.  This will override a false value of `sftp_permission` on the user level.
#   dav_permission - boolean - If true, users in this group can use WebDAV to login.  This will override a false value of `dav_permission` on the user level.
#   restapi_permission - boolean - If true, users in this group can use the REST API to login.  This will override a false value of `restapi_permission` on the user level.
#   allowed_ips - string - A list of allowed IPs if applicable.  Newline delimited
#   name - string - Group name.
def update(id, params=None, options=None):
    if not isinstance(params, dict):
        params = {}
    if not isinstance(options, dict):
        options = {}
    params["id"] = id
    if "id" in params and not isinstance(params["id"], int):
        raise InvalidParameterError("Bad parameter: id must be an int")
    if "notes" in params and not isinstance(params["notes"], str):
        raise InvalidParameterError("Bad parameter: notes must be an str")
    if "user_ids" in params and not isinstance(params["user_ids"], str):
        raise InvalidParameterError("Bad parameter: user_ids must be an str")
    if "admin_ids" in params and not isinstance(params["admin_ids"], str):
        raise InvalidParameterError("Bad parameter: admin_ids must be an str")
    if "ftp_permission" in params and not isinstance(
        params["ftp_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: ftp_permission must be an bool"
        )
    if "sftp_permission" in params and not isinstance(
        params["sftp_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: sftp_permission must be an bool"
        )
    if "dav_permission" in params and not isinstance(
        params["dav_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: dav_permission must be an bool"
        )
    if "restapi_permission" in params and not isinstance(
        params["restapi_permission"], bool
    ):
        raise InvalidParameterError(
            "Bad parameter: restapi_permission must be an bool"
        )
    if "allowed_ips" in params and not isinstance(params["allowed_ips"], str):
        raise InvalidParameterError(
            "Bad parameter: allowed_ips must be an str"
        )
    if "name" in params and not isinstance(params["name"], str):
        raise InvalidParameterError("Bad parameter: name must be an str")
    if "id" not in params:
        raise MissingParameterError("Parameter missing: id")
    response, options = Api.send_request(
        "PATCH", "/groups/{id}".format(id=params["id"]), params, options
    )
    return Group(response.data, options)


def delete(id, params=None, options=None):
    if not isinstance(params, dict):
        params = {}
    if not isinstance(options, dict):
        options = {}
    params["id"] = id
    if "id" in params and not isinstance(params["id"], int):
        raise InvalidParameterError("Bad parameter: id must be an int")
    if "id" not in params:
        raise MissingParameterError("Parameter missing: id")
    Api.send_request(
        "DELETE", "/groups/{id}".format(id=params["id"]), params, options
    )


def destroy(id, params=None, options=None):
    delete(id, params, options)


def new(*args, **kwargs):
    return Group(*args, **kwargs)
