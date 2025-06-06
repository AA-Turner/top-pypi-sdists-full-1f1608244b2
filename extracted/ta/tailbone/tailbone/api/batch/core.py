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
Tailbone Web API - Batch Views
"""

import logging
import warnings

from cornice import Service

from tailbone.api import APIMasterView


log = logging.getLogger(__name__)


class APIBatchMixin(object):
    """
    Base class for all API views which are meant to handle "batch" *and/or*
    "batch row" data.
    """

    def get_batch_class(self):
        model_class = self.get_model_class()
        if hasattr(model_class, '__batch_class__'):
            return model_class.__batch_class__
        return model_class

    def get_handler(self):
        """
        Returns a `BatchHandler` instance for the view.  All (?) custom batch
        API views should define a default handler class; however this may in all
        (?)  cases be overridden by config also.  The specific setting required
        to do so will depend on the 'key' for the type of batch involved, e.g.
        assuming the 'vendor_catalog' batch:

        .. code-block:: ini

           [rattail.batch]
           vendor_catalog.handler = myapp.batch.vendorcatalog:CustomCatalogHandler

        Note that the 'key' for a batch is generally the same as its primary
        table name, although technically it is whatever value returns from the
        ``batch_key`` attribute of the main batch model class.
        """
        app = self.get_rattail_app()
        key = self.get_batch_class().batch_key
        return app.get_batch_handler(key, default=self.default_handler_spec)


class APIBatchView(APIBatchMixin, APIMasterView):
    """
    Base class for all API views which are meant to handle "batch" *and/or*
    "batch row" data.
    """
    supports_toggle_complete = False
    supports_execute = False

    def __init__(self, request, **kwargs):
        super(APIBatchView, self).__init__(request, **kwargs)
        self.batch_handler = self.get_handler()

    @property
    def handler(self):
        warnings.warn("the `handler` property is deprecated; "
                      "please use `batch_handler` instead",
                      DeprecationWarning, stacklevel=2)
        return self.batch_handler

    def normalize(self, batch):
        app = self.get_rattail_app()
        created = app.localtime(batch.created, from_utc=True)

        executed = None
        if batch.executed:
            executed = app.localtime(batch.executed, from_utc=True)

        return {
            'uuid': batch.uuid,
            '_str': str(batch),
            'id': batch.id,
            'id_str': batch.id_str,
            'description': batch.description,
            'notes': batch.notes,
            'params': batch.params or {},
            'rowcount': batch.rowcount,
            'created': str(created),
            'created_display': self.pretty_datetime(created),
            'created_by_uuid': batch.created_by.uuid,
            'created_by_display': str(batch.created_by),
            'complete': batch.complete,
            'status_code': batch.status_code,
            'status_display': batch.STATUS.get(batch.status_code,
                                               str(batch.status_code)),
            'executed': str(executed) if executed else None,
            'executed_display': self.pretty_datetime(executed) if executed else None,
            'executed_by_uuid': batch.executed_by_uuid,
            'executed_by_display': str(batch.executed_by or ''),
            'mutable': self.batch_handler.is_mutable(batch),
        }

    def create_object(self, data):
        """
        Create a new object instance and populate it with the given data.

        Here we'll invoke the handler for actual batch creation, instead of
        typical logic used for simple records.
        """
        user = self.request.user
        kwargs = dict(data)
        kwargs['user'] = user
        batch = self.batch_handler.make_batch(self.Session(), **kwargs)
        if self.batch_handler.should_populate(batch):
            self.batch_handler.do_populate(batch, user)
        return batch

    def update_object(self, batch, data):
        """
        Logic for updating a main object record.

        Here we want to make sure we set "created by" to the current user, when
        creating a new batch.
        """
        # we're only concerned with *new* batches here
        if not batch.uuid:

            # assign creator; initialize row count
            batch.created_by_uuid = self.request.user.uuid
            if batch.rowcount is None:
                batch.rowcount = 0

        # then go ahead with usual logic
        return super(APIBatchView, self).update_object(batch, data)

    def mark_complete(self):
        """
        Mark the given batch as "complete".
        """
        batch = self.get_object()

        if batch.executed:
            return {'error': "Batch {} has already been executed: {}".format(
                batch.id_str, batch.description)}

        if batch.complete:
            return {'error': "Batch {} is already marked complete: {}".format(
                batch.id_str, batch.description)}

        batch.complete = True
        return self._get(obj=batch)

    def mark_incomplete(self):
        """
        Mark the given batch as "incomplete".
        """
        batch = self.get_object()

        if batch.executed:
            return {'error': "Batch {} has already been executed: {}".format(
                batch.id_str, batch.description)}

        if not batch.complete:
            return {'error': "Batch {} is already marked incomplete: {}".format(
                batch.id_str, batch.description)}

        batch.complete = False
        return self._get(obj=batch)

    def execute(self):
        """
        Execute the given batch.
        """
        batch = self.get_object()

        if batch.executed:
            return {'error': "Batch {} has already been executed: {}".format(
                batch.id_str, batch.description)}

        kwargs = dict(self.request.json_body)
        kwargs.pop('user', None)
        kwargs.pop('progress', None)
        result = self.batch_handler.do_execute(batch, self.request.user, **kwargs)
        return {'ok': bool(result), 'batch': self.normalize(batch)}

    @classmethod
    def defaults(cls, config):
        cls._defaults(config)
        cls._batch_defaults(config)

    @classmethod
    def _batch_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        permission_prefix = cls.get_permission_prefix()
        collection_url_prefix = cls.get_collection_url_prefix()
        object_url_prefix = cls.get_object_url_prefix()

        if cls.supports_toggle_complete:

            # mark complete
            mark_complete = Service(name='{}.mark_complete'.format(route_prefix),
                                    path='{}/{{uuid}}/mark-complete'.format(object_url_prefix))
            mark_complete.add_view('POST', 'mark_complete', klass=cls,
                                   permission='{}.edit'.format(permission_prefix))
            config.add_cornice_service(mark_complete)

            # mark incomplete
            mark_incomplete = Service(name='{}.mark_incomplete'.format(route_prefix),
                                      path='{}/{{uuid}}/mark-incomplete'.format(object_url_prefix))
            mark_incomplete.add_view('POST', 'mark_incomplete', klass=cls,
                                     permission='{}.edit'.format(permission_prefix))
            config.add_cornice_service(mark_incomplete)

        if cls.supports_execute:

            # execute batch
            execute = Service(name='{}.execute'.format(route_prefix),
                              path='{}/{{uuid}}/execute'.format(object_url_prefix))
            execute.add_view('POST', 'execute', klass=cls,
                             permission='{}.execute'.format(permission_prefix))
            config.add_cornice_service(execute)


# TODO: deprecate / remove this
BatchAPIMasterView = APIBatchView


class APIBatchRowView(APIBatchMixin, APIMasterView):
    """
    Base class for all API views which are meant to handle "batch rows" data.
    """
    editable = False
    supports_quick_entry = False

    def __init__(self, request, **kwargs):
        super(APIBatchRowView, self).__init__(request, **kwargs)
        self.batch_handler = self.get_handler()

    @property
    def handler(self):
        warnings.warn("the `handler` property is deprecated; "
                      "please use `batch_handler` instead",
                      DeprecationWarning, stacklevel=2)
        return self.batch_handler

    def normalize(self, row):
        batch = row.batch
        return {
            'uuid': row.uuid,
            '_str': str(row),
            '_parent_str': str(batch),
            '_parent_uuid': batch.uuid,
            'batch_uuid': batch.uuid,
            'batch_id': batch.id,
            'batch_id_str': batch.id_str,
            'batch_description': batch.description,
            'batch_complete': batch.complete,
            'batch_executed': bool(batch.executed),
            'batch_mutable': self.batch_handler.is_mutable(batch),
            'sequence': row.sequence,
            'status_code': row.status_code,
            'status_display': row.STATUS.get(row.status_code, str(row.status_code)),
        }

    def update_object(self, row, data):
        """
        Supplements the default logic as follows:

        Invokes the batch handler's ``refresh_row()`` method after updating the
        row's field data per usual.
        """
        if not self.batch_handler.is_mutable(row.batch):
            return {'error': "Batch is not mutable"}

        # update row per usual
        row = super(APIBatchRowView, self).update_object(row, data)

        # okay now we apply handler refresh logic
        self.batch_handler.refresh_row(row)
        return row

    def delete_object(self, row):
        """
        Overrides the default logic as follows:

        Delegates deletion of the row to the batch handler.
        """
        self.batch_handler.do_remove_row(row)

    def quick_entry(self):
        """
        View for handling "quick entry" user input, for a batch.
        """
        data = self.request.json_body

        uuid = data['batch_uuid']
        batch = self.Session.get(self.get_batch_class(), uuid)
        if not batch:
            raise self.notfound()

        entry = data['quick_entry']

        try:
            row = self.batch_handler.quick_entry(self.Session(), batch, entry)
        except Exception as error:
            log.warning("quick entry failed for '%s' batch %s: %s",
                        self.batch_handler.batch_key, batch.id_str, entry,
                        exc_info=True)
            msg = str(error)
            if not msg and isinstance(error, NotImplementedError):
                msg = "Feature is not implemented"
            return {'error': msg}

        if not row:
            return {'error': "Could not identify product"}

        self.Session.flush()
        result = self._get(obj=row)
        result['ok'] = True
        return result

    @classmethod
    def defaults(cls, config):
        cls._defaults(config)
        cls._batch_row_defaults(config)

    @classmethod
    def _batch_row_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        permission_prefix = cls.get_permission_prefix()
        collection_url_prefix = cls.get_collection_url_prefix()

        if cls.supports_quick_entry:

            # quick entry
            quick_entry = Service(name='{}.quick_entry'.format(route_prefix),
                                  path='{}/quick-entry'.format(collection_url_prefix))
            quick_entry.add_view('POST', 'quick_entry', klass=cls,
                                 permission='{}.edit'.format(permission_prefix))
            config.add_cornice_service(quick_entry)
