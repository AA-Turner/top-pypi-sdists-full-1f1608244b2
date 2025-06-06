# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Common Forms
"""

from rattail.db import model

import colander


@colander.deferred
def validate_user(node, kw):
    session = kw['session']
    def validate(node, value):
        user = session.get(model.User, value)
        if not user:
            raise colander.Invalid(node, "User not found")
        return user.uuid
    return validate


class Feedback(colander.Schema):
    """
    Form schema for user feedback.
    """
    email_key = colander.SchemaNode(colander.String(),
                                    missing=colander.null)

    referrer = colander.SchemaNode(colander.String())

    user = colander.SchemaNode(colander.String(),
                               missing=colander.null,
                               validator=validate_user)

    user_name = colander.SchemaNode(colander.String(),
                                    missing=colander.null)

    please_reply_to = colander.SchemaNode(colander.String(),
                                          missing=colander.null)

    message = colander.SchemaNode(colander.String())
