# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2024 Lance Edgar
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
Base views for maintaining "new-style" batches.
"""

import os
import sys
import json
import datetime
import logging
import socket
import subprocess
import tempfile
import warnings

import json
import markdown
import sqlalchemy as sa
from sqlalchemy import orm

from rattail.threads import Thread
from rattail.util import simple_error

import colander
from deform import widget as dfwidget
from webhelpers2.html import HTML, tags

from wuttaweb.util import render_csrf_token

from tailbone import forms, grids
from tailbone.db import Session
from tailbone.views import MasterView


log = logging.getLogger(__name__)


class BatchMasterView(MasterView):
    """
    Base class for all "batch master" views.
    """
    default_handler_spec = None
    batch_handler_class = None
    has_rows = True
    rows_deletable = True
    rows_deletable_if_executed = False
    rows_bulk_deletable = True
    rows_downloadable_csv = True
    rows_downloadable_xlsx = True
    refreshable = True
    refresh_after_create = False
    cloneable = False
    executable = True
    results_refreshable = False
    results_executable = False
    has_worksheet = False
    has_worksheet_file = False
    delete_requires_progress = True

    input_file_template_config_section = 'rattail.batch'

    grid_columns = [
        'id',
        'description',
        'created',
        'created_by',
        'rowcount',
        # 'status_code',
        # 'complete',
        'executed',
        'executed_by',
    ]

    form_fields = [
        'id',
        'description',
        'notes',
        'params',
        'rowcount',
        'status_code',
        'created',
        'created_by',
        'executed',
        'executed_by',
    ]

    row_labels = {
        'upc': "UPC",
        'item_id': "Item ID",
        'status_code': "Status",
    }

    def __init__(self, request):
        super().__init__(request)
        self.batch_handler = self.get_handler()
        # TODO: deprecate / remove this (?)
        self.handler = self.batch_handler

    @classmethod
    def get_handler_factory(cls, rattail_config):
        """
        Returns the "factory" (class) which will be used to create the batch
        handler.  All (?) custom batch views should define a default handler
        class; however this may in all (?) cases be overridden by config also.
        The specific setting required to do so will depend on the 'key' for the
        type of batch involved, e.g.  assuming the 'inventory' batch:

        .. code-block:: ini

           [rattail.batch]
           inventory.handler = poser.batch.inventory:InventoryBatchHandler

        Note that the 'key' for a batch is generally the same as its primary
        table name, although technically it is whatever value returns from the
        ``batch_key`` attribute of the main batch model class.
        """
        # first try to figure out if config defines a factory class
        app = rattail_config.get_app()
        model_class = cls.get_model_class()
        batch_key = model_class.batch_key
        handler = app.get_batch_handler(batch_key,
                                        default=cls.default_handler_spec)
        if handler:
            return handler.__class__

        # fall back to whatever class was defined statically
        return cls.batch_handler_class

    def get_handler(self):
        """
        Returns a batch handler instance to be used by the view.  Note that
        this will use the factory provided by :meth:`get_handler_factory()` to
        create the handler instance.
        """
        factory = self.get_handler_factory(self.rattail_config)
        return factory(self.rattail_config)

    @property
    def input_file_template_config_prefix(self):
        return '{}.input_file_template'.format(self.batch_handler.batch_key)

    def download_path(self, batch, filename):
        return self.rattail_config.batch_filepath(batch.batch_key, batch.uuid, filename)

    def template_kwargs_view(self, **kwargs):
        kwargs = super().template_kwargs_view(**kwargs)
        batch = kwargs['instance']
        kwargs['batch'] = batch
        kwargs['handler'] = self.handler

        if self.has_worksheet_file and self.allow_worksheet(batch) and self.has_perm('worksheet'):
            kwargs['upload_worksheet_form'] = self.make_upload_worksheet_form(batch)

        kwargs['execute_title'] = self.get_execute_title(batch)
        kwargs['execute_enabled'] = self.instance_executable(batch)
        if kwargs['execute_enabled']:
            url = self.get_action_url('execute', batch)
            kwargs['execute_form'] = self.make_execute_form(batch, action_url=url)
            description = (self.handler.describe_execution(batch)
                           or "TODO: handler does not provide a description for this batch")
            kwargs['execution_described'] = markdown.markdown(
                description, extensions=['fenced_code', 'codehilite'])
        else:
            kwargs['why_not_execute'] = self.handler.why_not_execute(batch)

        breakdown = self.make_status_breakdown(batch)

        factory = self.get_grid_factory()
        g = factory(self.request,
                    key='batch_row_status_breakdown',
                    data=[],
                    columns=['title', 'count'])
        g.set_click_handler('title', "autoFilterStatus(props.row)")
        kwargs['status_breakdown_data'] = breakdown
        kwargs['status_breakdown_grid'] = HTML.literal(
            g.render_table_element(data_prop='statusBreakdownData',
                                   empty_labels=True))

        return kwargs

    def make_upload_worksheet_form(self, batch):
        action_url = self.get_action_url('upload_worksheet', batch)
        form = forms.Form(schema=UploadWorksheet(),
                          request=self.request,
                          action_url=action_url,
                          component='upload-worksheet-form')
        form.set_type('worksheet_file', 'file')
        # TODO: must set these to avoid some default code
        form.auto_disable = False
        form.auto_disable_save = False
        return form

    def download_worksheet(self):
        batch = self.get_instance()
        path = self.handler.write_worksheet(batch)
        root, ext = os.path.splitext(path)
        # we present a more descriptive filename for download
        filename = '{}.worksheet.{}{}'.format(batch.batch_key, batch.id_str, ext)
        return self.file_response(path, filename=filename)

    def upload_worksheet(self):
        batch = self.get_instance()
        form = self.make_upload_worksheet_form(batch)
        if self.validate_form(form):
            uploads = self.normalize_uploads(form)
            path = uploads['worksheet_file']['temp_path']
            return self.handler_action(batch, 'update_from_worksheet', path=path)
        self.request.session.flash("Upload form did not validate!", 'error')
        return self.redirect(self.get_action_url('view', batch))

    def update_from_worksheet_thread(self, batch_uuid, user_uuid, progress, path=None):
        """
        Thread target for updating a batch from worksheet.
        """
        session = self.make_isolated_session()
        batch = session.get(self.model_class, batch_uuid)
        try:
            self.handler.update_from_worksheet(batch, path, progress=progress)

        except Exception as error:
            session.rollback()
            log.exception("upload/update failed for '{}' batch: {}".format(self.batch_key, batch))
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Upload processing failed: {}".format(
                    simple_error(error))
                progress.session.save()

        else:
            session.commit()
            success_msg = "Batch has been updated: {}".format(batch)
            success_url = self.get_action_url('view', batch)
            session.close()

            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_msg'] = success_msg
                progress.session['success_url'] = success_url
                progress.session.save()

    def make_status_breakdown(self, batch, rows=None, status_enum=None):
        """
        Returns a simple list of 2-tuples, each of which has the status display
        title as first member, and number of rows with that status as second
        member.
        """
        breakdown = {}
        if rows is None:
            rows = batch.active_rows()
        for row in rows:
            if row.status_code is not None:
                if row.status_code not in breakdown:
                    status = status_enum or row.STATUS
                    breakdown[row.status_code] = {
                        'code': row.status_code,
                        'title': status[row.status_code],
                        'count': 0,
                    }
                breakdown[row.status_code]['count'] += 1
        return list(breakdown.values())

    def allow_worksheet(self, batch):
        return not batch.executed and not batch.complete

    def configure_grid(self, g):
        super().configure_grid(g)
        model = self.model

        # created_by
        CreatedBy = orm.aliased(model.User)
        g.set_joiner('created_by', lambda q: q.join(CreatedBy,
                                                    CreatedBy.uuid == self.model_class.created_by_uuid))
        g.set_sorter('created_by', CreatedBy.username)
        g.set_filter('created_by', CreatedBy.username)
        g.set_label('created_by', "Created by")

        # executed
        g.filters['executed'].default_active = True
        g.filters['executed'].default_verb = 'is_null'

        # executed_by
        ExecutedBy = orm.aliased(model.User)
        g.set_joiner('executed_by', lambda q: q.outerjoin(ExecutedBy,
                                                          ExecutedBy.uuid == self.model_class.executed_by_uuid))
        g.set_sorter('executed_by', ExecutedBy.username)
        g.set_filter('executed_by', ExecutedBy.username)
        g.set_label('executed_by', "Executed by")

        g.set_sort_defaults('id', 'desc')

        g.set_enum('status_code', self.model_class.STATUS)

        g.set_renderer('id', self.render_id_str)

        g.set_link('id')
        g.set_link('description')
        g.set_link('executed')

        g.set_label('id', "Batch ID")
        g.set_label('rowcount', "Rows")
        g.set_label('status_code', "Status")

    def template_kwargs_index(self, **kwargs):
        route_prefix = self.get_route_prefix()
        if self.results_executable:
            url = self.request.route_url('{}.execute_results'.format(route_prefix))
            kwargs['execute_form'] = self.make_execute_form(action_url=url)
        return kwargs

    def get_instance_title(self, batch):
        if batch.description:
            return "{} {}".format(batch.id_str, batch.description)
        return batch.id_str

    def configure_form(self, f):
        super().configure_form(f)

        # id
        f.set_readonly('id')
        f.set_renderer('id', self.render_id_str)
        f.set_label('id', "Batch ID")

        # params
        if self.creating:
            f.remove('params')
        else:
            f.set_readonly('params')
            f.set_renderer('params', self.render_params)

        # created
        f.set_readonly('created')
        f.set_readonly('created_by')
        f.set_renderer('created_by', self.render_user)
        f.set_label('created_by', "Created by")

        # cognized
        f.set_renderer('cognized_by', self.render_user)
        f.set_label('cognized_by', "Cognized by")

        # row count
        f.set_readonly('rowcount')
        f.set_label('rowcount', "Row Count")

        # status_code
        if self.creating:
            f.remove_field('status_code')
        else:
            f.set_readonly('status_code')
            f.set_renderer('status_code', self.make_status_renderer(self.model_class.STATUS))
            f.set_label('status_code', "Status")

        # complete
        if self.viewing:
            f.set_renderer('complete', self.render_complete)

        # executed
        f.set_readonly('executed')
        f.set_readonly('executed_by')
        f.set_renderer('executed_by', self.render_user)
        f.set_label('executed_by', "Executed by")

        # notes
        f.set_type('notes', 'text_wrapped')

        # if self.creating and self.request.user:
        #     batch = fs.model
        #     batch.created_by_uuid = self.request.user.uuid

        if self.creating:
            f.remove_fields('id',
                            'rowcount',
                            'created',
                            'created_by',
                            'cognized',
                            'cognized_by',
                            'executed',
                            'executed_by',
                            'purge')

        else: # not creating
            batch = self.get_instance()
            if not batch.executed:
                f.remove_fields('executed',
                                'executed_by')

    def render_params(self, batch, field):
        params = self.get_visible_params(batch)
        if not params:
            return

        return params

    def get_visible_params(self, batch):
        return dict(batch.params or {})

    def render_complete(self, batch, field):
        text = "Yes" if batch.complete else "No"

        if batch.executed or not self.has_perm('edit'):
            return text

        if batch.complete:
            label = "Mark Incomplete"
            value = 'false'
        else:
            label = "Mark Complete"
            value = 'true'

        url = self.get_action_url('toggle_complete', batch)
        kwargs = {'@submit': 'togglingBatchComplete = true'}
        begin_form = tags.form(url, **kwargs)

        label = HTML.literal(
            '{{{{ togglingBatchComplete ? "Working, please wait..." : "{}" }}}}'.format(label))
        submit = self.make_button(label, is_primary=True,
                                  native_type='submit',
                                  **{':disabled': 'togglingBatchComplete'})

        form = [
            begin_form,
            render_csrf_token(self.request),
            tags.hidden('complete', value=value),
            submit,
            tags.end_form(),
        ]

        text = HTML.tag('div', class_='control', c=text)
        form = HTML.tag('div', class_='control', c=form)
        content = [
            HTML.tag('nav', class_='level',
                     c=[HTML.tag('div', class_='level-left', c=[
                         text,
                         HTML.literal(' &nbsp; &nbsp; '),
                         form,
                     ])]),
        ]

        return HTML.tag('div', c=content)

    def render_user(self, batch, field):
        user = getattr(batch, field)
        if not user:
            return ""
        title = str(user)
        url = self.request.route_url('users.view', uuid=user.uuid)
        return tags.link_to(title, url)

    def save_create_form(self, form):
        uploads = self.normalize_uploads(form)
        self.before_create(form)

        session = self.Session()
        with session.no_autoflush:

            # transfer form data to batch instance
            batch = self.objectify(form, self.form_deserialized)

            # current user is batch creator
            batch.created_by = self.request.user or self.late_login_user()

            # obtain kwargs for making batch via handler, below
            kwargs = self.get_batch_kwargs(batch)

            # TODO: this needs work yet surely...why is this an issue?
            # treat 'filename' field specially, for some reason it can be a filedict?
            if 'filename' in kwargs and not isinstance(kwargs['filename'], str):
                kwargs['filename'] = '' # null not allowed

            # TODO: is this still necessary with colander?
            # destroy initial batch and re-make using handler
            # if batch in self.Session:
            #     self.Session.expunge(batch)
            batch = self.handler.make_batch(session, **kwargs)

        self.Session.flush()
        self.process_uploads(batch, form, uploads)
        return batch

    def process_uploads(self, batch, form, uploads):

        def process(upload, key):
            self.handler.set_input_file(batch, upload['temp_path'], attr=key)
            os.remove(upload['temp_path'])
            os.rmdir(upload['tempdir'])

        for key, upload in uploads.items():
            if isinstance(upload, dict):
                process(upload, key)
            else:
                uploads = upload
                for upload in uploads:
                    if isinstance(upload, dict):
                        process(upload, key)

    def get_batch_kwargs(self, batch, **kwargs):
        """
        Return a kwargs dict for use with ``self.handler.make_batch()``, using
        the given batch as a template.
        """
        kwargs = {}
        if batch.created_by:
            kwargs['created_by'] = batch.created_by
        elif batch.created_by_uuid:
            kwargs['created_by_uuid'] = batch.created_by_uuid
        kwargs['description'] = batch.description
        kwargs['notes'] = batch.notes
        if hasattr(batch, 'filename'):
            kwargs['filename'] = batch.filename
        kwargs['complete'] = batch.complete
        return kwargs

    # TODO: deprecate / remove this (is it used at all now?)
    def init_batch(self, batch):
        """
        Initialize a new batch.  Derived classes can override this to
        effectively provide default values for a batch, etc.  This method is
        invoked after a batch has been fully prepared for insertion to the
        database, but before the push to the database occurs.

        Note that the return value of this function matters; if it is boolean
        false then the batch will not be persisted at all, and the user will be
        redirected to the "create batch" page.
        """
        return True

    def redirect_after_create(self, batch, **kwargs):
        if self.handler.should_populate(batch):
            return self.redirect(self.get_action_url('prefill', batch))
        elif self.refresh_after_create:
            return self.redirect(self.get_action_url('refresh', batch))
        else:
            return self.redirect(self.get_action_url('view', batch))

    def template_kwargs_edit(self, **kwargs):
        batch = kwargs['instance']
        kwargs['batch'] = batch
        return kwargs

    def toggle_complete(self):
        batch = self.get_instance()
        if batch.executed:
            self.request.session.flash("Request ignored, since batch has already been executed")
        else:
            form = forms.Form(schema=ToggleComplete(), request=self.request)
            if form.validate():
                if form.validated['complete']:
                    self.mark_batch_complete(batch)
                else:
                    self.mark_batch_incomplete(batch)
        return self.redirect(self.get_action_url('view', batch))

    def mark_batch_complete(self, batch):
        self.handler.mark_complete(batch)

    def mark_batch_incomplete(self, batch):
        self.handler.mark_incomplete(batch)

    def rows_creatable_for(self, batch):
        """
        Only allow creating new rows on a batch if it hasn't yet been executed
        or marked complete.
        """
        if batch.executed:
            return False
        if batch.complete:
            return False
        return True

    def rows_quickable_for(self, batch):
        """
        Must return boolean indicating whether the "quick row" feature should
        be allowed for the given batch.  By default, returns ``False`` if batch
        has already been executed or marked complete, and ``True`` otherwise.
        """
        if batch.executed:
            return False
        if batch.complete:
            return False
        return True

    def configure_row_grid(self, g):
        super().configure_row_grid(g)

        g.set_sort_defaults('sequence')
        g.set_link('sequence')
        g.set_label('sequence', "Seq.")
        if 'sequence' in g.filters:
            g.filters['sequence'].label = "Sequence"

        if 'status_code' in g.filters:
            g.filters['status_code'].set_value_renderer(grids.filters.EnumValueRenderer(self.model_row_class.STATUS))

        if self.model_row_class:
            g.set_enum('status_code', self.model_row_class.STATUS)

        g.set_renderer('status_code', self.render_row_status)

    def get_row_status_enum(self):
        return self.model_row_class.STATUS

    def render_upc_pretty(self, row, field):
        upc = getattr(row, field)
        if upc:
            return upc.pretty()

    def render_row_status(self, row, column):
        code = row.status_code
        if code is None:
            return ""
        text = self.get_row_status_enum().get(code, str(code))
        if row.status_text:
            return HTML.tag('span', title=row.status_text, c=text)
        return text

    def create_row(self):
        """
        Only allow creating a new row if the batch hasn't yet been executed.
        """
        batch = self.get_instance()
        if batch.executed:
            self.request.session.flash("You cannot add new rows to a batch which has been executed")
            return self.redirect(self.get_action_url('view', batch))
        return super().create_row()

    def save_create_row_form(self, form):
        batch = self.get_instance()
        row = self.objectify(form, self.form_deserialized)
        self.handler.add_row(batch, row)
        self.Session.flush()
        return row

    def after_create_row(self, row):
        self.handler.refresh_row(row)

    def configure_row_form(self, f):
        super().configure_row_form(f)

        # sequence
        f.set_readonly('sequence')

        # upc (default rendering, just in case there is such a field
        # on our row model)
        f.set_renderer('upc', self.render_upc_pretty)

        # status_code
        if self.model_row_class:
            f.set_enum('status_code', self.model_row_class.STATUS)
        f.set_renderer('status_code', self.render_row_status)
        f.set_readonly('status_code')
        f.set_label('status_code', "Status")

        # status text
        f.set_readonly('status_text')

    def make_default_row_grid_tools(self, batch):
        if self.rows_creatable and not batch.executed and not batch.complete:
            permission_prefix = self.get_permission_prefix()
            if self.request.has_perm('{}.create_row'.format(permission_prefix)):
                url = self.get_action_url('create_row', batch)
                return self.make_button("New Row", url=url,
                                        is_primary=True,
                                        icon_left='plus')

    def make_batch_row_grid_tools(self, batch):
        pass

    def make_row_grid_kwargs(self, **kwargs):
        """
        Whether or not rows may be edited or deleted will depend partially on
        whether the parent batch has been executed.
        """
        batch = self.get_instance()

        # TODO: most of this logic is copied from MasterView, should refactor/merge somehow...
        if 'actions' not in kwargs:
            actions = []

            # view action
            if self.rows_viewable:
                view = lambda r, i: self.get_row_action_url('view', r)
                actions.append(self.make_action('view', icon='eye', url=view))

            # edit and delete are NOT allowed if batch is "complete"
            if not batch.complete:

                # edit action
                if self.rows_editable and not batch.executed and self.has_perm('edit_row'):
                    actions.append(self.make_action('edit', icon='edit',
                                                    url=self.row_edit_action_url))

                # delete action
                if self.rows_deletable and self.has_perm('delete_row'):
                    actions.append(self.make_action('delete', icon='trash', url=self.row_delete_action_url))
                    kwargs.setdefault('delete_speedbump', self.rows_deletable_speedbump)

            kwargs['actions'] = actions

        return super().make_row_grid_kwargs(**kwargs)

    def make_row_grid_tools(self, batch):
        return (self.make_default_row_grid_tools(batch) or '') + (self.make_batch_row_grid_tools(batch) or '')

    def redirect_after_edit(self, batch):
        """
        If refresh flag is set, do that; otherwise go (back) to view/edit page.
        """
        if self.request.params.get('refresh') == 'true':
            return self.redirect(self.get_action_url('refresh', batch))
        return self.redirect(self.get_action_url('view', batch))

    def delete_instance(self, batch):
        """
        Delete all data (files etc.) for the batch.
        """
        app = self.get_rattail_app()
        session = app.get_session(batch)
        self.batch_handler.do_delete(batch)
        session.flush()

    def delete_instance_with_progress(self, batch):
        """
        Delete all data (files etc.) for the batch.
        """
        return self.handler_action(batch, 'delete')

    def delete_thread(self, key, user_uuid, progress, **kwargs):
        """
        Thread target for deleting a batch with progress indicator.
        """
        app = self.get_rattail_app()
        model = self.model
        # nb. must make new session, separate from main thread
        session = app.make_session()
        batch = self.get_instance_for_key(key, session)
        batch_str = str(batch)

        try:
            # try to delete batch
            self.handler.do_delete(batch, progress=progress, **kwargs)

        except Exception as error:
            # error; log that and rollback
            log.exception("delete failed for batch: %s", batch)
            session.rollback()
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Batch deletion failed: {}".format(
                    simple_error(error))
                progress.session.save()

        else:
            # no error; finish up
            session.commit()
            session.close()
            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = self.get_index_url()
                progress.session['success_msg'] = "Batch has been deleted: {}".format(
                    batch_str)
                progress.session.save()

    def get_fallback_templates(self, template, **kwargs):
        return [
            '/batch/{}.mako'.format(template),
            '/master/{}.mako'.format(template),
        ]

    def editable_instance(self, batch):
        return not bool(batch.executed)

    def after_edit_row(self, row):
        self.handler.refresh_row(row)

    def instance_executable(self, batch=None):
        return self.handler.executable(batch)

    def batch_refreshable(self, batch):
        """
        Return a boolean indicating whether the given batch should allow a
        refresh operation.
        """
        # TODO: deprecate/remove this?
        if not self.refreshable:
            return False

        # (this is how it should be done i think..)
        if callable(self.handler.refreshable):
            return self.handler.refreshable(batch)

        # TODO: deprecate/remove this
        return self.handler.refreshable and not batch.executed

    def has_execution_options(self, batch=None):
        return bool(self.execution_options_schema)

    # TODO
    execution_options_schema = None

    def make_execute_schema(self, batch):
        return self.execution_options_schema().bind(batch=batch)

    def make_execute_form(self, batch=None, **kwargs):
        """
        Return a proper Form for execution options.
        """
        defaults = {}
        route_prefix = self.get_route_prefix()

        schema = None
        if self.has_execution_options(batch):
            if batch is None:
                batch = self.model_class
            schema = self.make_execute_schema(batch)
            if schema:
                for field in schema:

                    # if field does not yet have a default, maybe provide one from session storage
                    if field.default is colander.null:
                        key = 'batch.{}.execute_option.{}'.format(batch.batch_key, field.name)
                        if key in self.request.session:
                            defaults[field.name] = self.request.session[key]

                    # make sure field label is preserved
                    if field.title:
                        labels = kwargs.setdefault('labels', {})
                        labels[field.name] = field.title

                    # auto-convert select widgets for theme
                    if isinstance(field.widget, forms.widgets.PlainSelectWidget):
                        warnings.warn("PlainSelectWidget is deprecated; "
                                      "please use deform.widget.SelectWidget instead",
                                      DeprecationWarning, stacklevel=2)
                        field.widget = dfwidget.SelectWidget(values=field.widget.values)

        if not schema:
            schema = colander.Schema()

        kwargs['vue_tagname'] = 'execute-form'
        form = forms.Form(schema=schema, request=self.request, defaults=defaults, **kwargs)
        self.configure_execute_form(form)
        return form

    def configure_execute_form(self, form):
        pass

    def get_execute_title(self, batch):
        if hasattr(self.handler, 'get_execute_title'):
            return self.handler.get_execute_title(batch)
        return "Execute Batch"

    def handler_action(self, batch, batch_action, **kwargs):
        """
        View which will attempt to refresh all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        route_prefix = self.get_route_prefix()
        permission_prefix = self.get_permission_prefix()

        user = self.request.user
        user_uuid = user.uuid if user else None
        username = user.username if user else None

        key = '{}.{}'.format(self.model_class.__tablename__, batch_action)
        progress = self.make_progress(key)

        # must ensure versioning is *disabled* during action, if handler says so
        allow_versioning = self.handler.allow_versioning(batch_action)
        if not allow_versioning and self.rattail_config.versioning_enabled():
            can_cancel = False

            # make socket for progress thread to listen to action thread
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', 0))
            sock.listen(1)
            port = sock.getsockname()[1]

            # launch thread to monitor progress
            success_url = self.get_action_url('view', batch)
            thread = Thread(target=self.progress_thread, args=(sock, success_url, progress))
            thread.start()

            # launch thread to invoke handler action
            thread = Thread(target=self.action_subprocess_thread,
                            args=((batch.uuid,), port, username, batch_action, progress),
                            kwargs=kwargs)
            thread.start()

        else: # either versioning is disabled, or handler doesn't mind
            can_cancel = True

            # launch thread to populate batch; that will update session progress directly
            target = getattr(self, '{}_thread'.format(batch_action))
            thread = Thread(target=target, args=((batch.uuid,), user_uuid, progress), kwargs=kwargs)
            thread.start()

        return self.render_progress(progress, {
            'can_cancel': can_cancel,
            'cancel_url': self.get_action_url('view', batch),
            'cancel_msg': "{} of batch was canceled.".format(batch_action.capitalize()),
        })

    def launch_subprocess(self, port=None, username=None,
                          command='rattail', command_args=None,
                          subcommand=None, subcommand_args=None):

        # construct command
        prefix = self.rattail_config.get('rattail', 'command_prefix',
                                         default=sys.prefix)
        cmd = [os.path.join(prefix, 'bin/{}'.format(command))]
        for path in self.rattail_config.prioritized_files:
            cmd.extend(['--config', path])
        if username:
            cmd.extend(['--runas', username])
        if command_args:
            cmd.extend(command_args)
        cmd.extend([
            '--progress',
            '--progress-socket', '127.0.0.1:{}'.format(port),
            subcommand,
        ])
        if subcommand_args:
            cmd.extend(subcommand_args)

        # run command in subprocess
        log.debug("launching command in subprocess: %s", cmd)
        try:
            # nb. we do not capture stderr, but on failure the stdout
            # will contain a simple error string
            subprocess.check_output(cmd)
        except subprocess.CalledProcessError as error:
            log.warning("command failed with exit code %s!  output was:",
                        error.returncode)
            output = error.output.decode('utf_8')
            log.warning(output)
            raise Exception(output)

    def action_subprocess_thread(self, key, port, username, handler_action, progress, **kwargs):
        """
        This method is sort of an alternative thread target for batch actions,
        to be used in the event versioning is enabled for the main process but
        the handler says versioning must be avoided during the action.  It must
        launch a separate process with versioning disabled in order to act on
        the batch.
        """
        batch_uuid = key[0]

        # figure out the (sub)command args we'll be passing
        if handler_action == 'auto_receive':
            subcommand = 'auto-receive'
        else:
            subcommand = f'{handler_action}-batch'
        subargs = [
            '--batch-type',
            self.handler.batch_key,
            batch_uuid,
        ]
        if handler_action == 'execute' and kwargs:
            subargs.extend([
                '--kwargs',
                json.dumps(kwargs),
            ])

        # invoke command to act on batch in separate process
        try:
            self.launch_subprocess(port=port, username=username,
                                   command='rattail',
                                   command_args=[
                                       '--no-versioning',
                                   ],
                                   subcommand=subcommand,
                                   subcommand_args=subargs)
        except Exception as error:
            log.warning("%s of '%s' batch failed: %s", handler_action, self.handler.batch_key, batch_uuid, exc_info=True)

            # TODO: write minimal error info to socket
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = (
                    "{} of '{}' batch failed: {} (see logs for more info)").format(
                        handler_action, self.handler.batch_key, error)
                progress.session.save()

            return

        models = getattr(self.handler, 'version_catchup_{}'.format(handler_action), None)
        if models:
            self.catchup_versions(port, batch_uuid, username, *models)

        suffix = "\n\n.".encode('utf_8')
        cxn = socket.create_connection(('127.0.0.1', port))
        data = json.dumps({
            'everything_complete': True,
        })
        data = data.encode('utf_8')
        cxn.send(data)
        cxn.send(suffix)
        cxn.close()

    def catchup_versions(self, port, batch_uuid, username, *models):
        app = self.get_rattail_app()
        with app.short_session() as s:
            batch = s.get(self.model_class, batch_uuid)
            batch_id = batch.id_str
            description = str(batch)

        self.launch_subprocess(
            port=port, username=username,
            command='rattail',
            subcommand='import-versions',
            subcommand_args=[
                '--comment',
                "version catch-up for '{}' batch {}: {}".format(self.handler.batch_key, batch_id, description),
            ] + list(models))

    def prefill(self):
        """
        View which will attempt to prefill all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        batch = self.get_instance()
        return self.handler_action(batch, 'populate')

    def populate_thread(self, batch_uuid, user_uuid, progress, **kwargs):
        """
        Thread target for populating batch data with progress indicator.
        """
        app = self.get_rattail_app()
        model = self.model
        # mustn't use tailbone web session here
        session = app.make_session()
        batch = session.get(self.model_class, batch_uuid)
        user = session.get(model.User, user_uuid)
        try:
            self.handler.do_populate(batch, user, progress=progress)
            session.flush()
        except Exception as error:
            session.rollback()
            log.warning("population failed for batch %s: %s", batch.uuid, batch,
                        exc_info=True)
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = simple_error(error)
                progress.session.save()
            return

        session.commit()
        session.refresh(batch)
        session.close()

        # finalize progress
        if progress:
            progress.session.load()
            progress.session['complete'] = True
            progress.session['success_url'] = self.get_action_url('view', batch)
            progress.session.save()

    def refresh(self):
        """
        View which will attempt to refresh all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        batch = self.get_instance()
        return self.handler_action(batch, 'refresh')

    def refresh_data(self, session, batch, user, progress=None):
        """
        Instruct the batch handler to refresh all data for the batch.
        """
        # TODO: deprecate/remove this
        if hasattr(self.handler, 'refresh_data'):
            self.handler.refresh_data(session, batch, progress=progress)
            batch.cognized = datetime.datetime.utcnow()
            batch.cognized_by = cognizer or session.merge(self.request.user)

        else: # the future
            user = user or session.merge(self.request.user)
            self.handler.do_refresh(batch, user, progress=progress)

    def refresh_thread(self, batch_uuid, user_uuid, progress, **kwargs):
        """
        Thread target for refreshing batch data with progress indicator.
        """
        # Refresh data for the batch, with progress.  Note that we must use the
        # rattail session here; can't use tailbone because it has web request
        # transaction binding etc.
        app = self.get_rattail_app()
        model = self.model
        session = app.make_session()
        batch = session.get(self.model_class, batch_uuid)
        cognizer = session.get(model.User, user_uuid) if user_uuid else None
        try:
            self.refresh_data(session, batch, cognizer, progress=progress)
            session.flush()
        except Exception as error:
            session.rollback()
            log.warning("refreshing data for batch failed: {}".format(batch), exc_info=True)
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Data refresh failed: {}".format(
                    simple_error(error))
                progress.session.save()
            return

        session.commit()
        session.refresh(batch)
        session.close()

        # Finalize progress indicator.
        if progress:
            progress.session.load()
            progress.session['complete'] = True
            progress.session['success_url'] = self.get_action_url('view', batch)
            progress.session.save()

    def refresh_results(self):
        """
        Refresh all batches which are returned from the current index query.
        Starts a separate thread for the refresh, and displays a progress
        indicator page.
        """
        key = '{}.refresh_results'.format(self.get_route_prefix())
        batches = self.get_effective_data()
        progress = self.make_progress(key)
        kwargs = {'progress': progress}
        thread = Thread(target=self.refresh_results_thread,
                        args=(batches, self.request.user.uuid),
                        kwargs=kwargs)
        thread.start()

        return self.render_progress(progress, {
            'cancel_url': self.get_index_url(),
            'cancel_msg': "Batch execution was canceled",
        })

    def refresh_results_thread(self, batches, user_uuid, progress=None):
        """
        Thread target for refreshing multiple batches with progress indicator.
        """
        app = self.get_rattail_app()
        model = self.model
        session = app.make_session()
        batches = batches.with_session(session).all()
        user = session.get(model.User, user_uuid)
        try:
            self.handler.refresh_many(batches, user=user, progress=progress)

        except Exception as error:
            session.rollback()
            log.exception("refresh failed for batch(es)!")
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = self.refresh_error_message(error)
                progress.session.save()

        else:
            session.commit()
            self.request.session.flash("{} {} were refreshed".format(
                len(batches), self.get_model_title_plural()))
            success_url = self.get_refresh_results_success_url()
            session.close()
            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = success_url
                progress.session.save()

    def refresh_error_message(self, error):
        return "Batch refresh failed: {}".format(simple_error(error))

    def get_refresh_results_success_url(self):
        return self.get_index_url()

    ########################################
    # batch rows
    ########################################

    def get_row_instance_title(self, row):
        return "Row {}".format(row.sequence)

    hide_row_status_codes = []

    def get_row_data(self, batch):
        """
        Generate the base data set for a rows grid.
        """
        query = self.Session.query(self.model_row_class)\
                            .filter(self.model_row_class.batch == batch)\
                            .filter(self.model_row_class.removed == False)
        if self.hide_row_status_codes:
            query = query.filter(~self.model_row_class.status_code.in_(self.hide_row_status_codes))
        return query

    def row_editable(self, row):
        """
        Batch rows are editable only until batch is complete or executed.
        """
        if not (self.rows_editable or self.rows_editable_but_not_directly):
            return False

        batch = self.get_parent(row)
        if batch.complete or batch.executed:
            return False

        return True

    def row_deletable(self, row):
        """
        Batch rows are deletable only until batch is complete or executed.
        """
        if not self.rows_deletable:
            return False

        batch = self.get_parent(row)

        if batch.complete:
            return False

        if batch.executed:
            if not self.rows_deletable_if_executed:
                return False
            if not self.has_perm('delete_row_if_executed'):
                return False

        return True

    def template_kwargs_view_row(self, **kwargs):
        kwargs['batch_model_title'] = kwargs['parent_model_title']
        # TODO: should these be set somewhere else?
        kwargs['row'] = kwargs['instance']
        kwargs['batch'] = kwargs['row'].batch
        return kwargs

    def get_parent(self, row):
        return row.batch

    def delete_row_object(self, row):
        """
        Perform the actual deletion of given row object.
        """
        self.handler.do_remove_row(row)

    def delete_row_objects(self, rows):
        deleted = super().delete_row_objects(rows)
        batch = self.get_instance()

        # decrement rowcount for batch
        if batch.rowcount is not None:
            batch.rowcount -= deleted

        # refresh batch status
        self.Session.refresh(batch)
        self.handler.refresh_batch_status(batch)

        return deleted

    def execute(self):
        """
        Execute a batch.  Starts a separate thread for the execution, and
        displays a progress indicator page.
        """
        batch = self.get_instance()
        self.executing = True
        form = self.make_execute_form(batch)
        if form.validate():
            kwargs = dict(form.validated)

            # cache options to use as defaults next time
            for key, value in form.validated.items():
                self.request.session['batch.{}.execute_option.{}'.format(batch.batch_key, key)] = value

            return self.handler_action(batch, 'execute', **kwargs)

        self.request.session.flash("Invalid request: {}".format(form.make_deform_form().error), 'error')
        return self.redirect(self.get_action_url('view', batch))

    def execute_error_message(self, error):
        return "Batch execution failed: {}".format(simple_error(error))

    def execute_thread(self, key, user_uuid, progress, **kwargs):
        """
        Thread target for executing a batch with progress indicator.
        """
        # Execute the batch, with progress.  Note that we must use the rattail
        # session here; can't use tailbone because it has web request
        # transaction binding etc.
        app = self.get_rattail_app()
        model = self.model
        session = app.make_session()
        batch = self.get_instance_for_key(key, session)
        user = session.get(model.User, user_uuid)
        try:
            result = self.handler.do_execute(batch, user=user, progress=progress, **kwargs)

        # If anything goes wrong, rollback and log the error etc.
        except Exception as error:
            session.rollback()
            log.exception("execution failed for batch: {}".format(batch))
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = self.execute_error_message(error)
                progress.session.save()

        # If no error, check result flag (false means user canceled).
        else:
            success_msg = None
            if result:
                session.commit()
                success_msg = "{} has been executed: {}".format(
                    self.get_model_title(), batch.id_str)
            else:
                session.rollback()

            session.refresh(batch)
            success_url = self.get_execute_success_url(batch, result, **kwargs)
            session.close()

            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = success_url
                if success_msg:
                    progress.session['success_msg'] = success_msg
                progress.session.save()

    def get_execute_success_url(self, batch, result, **kwargs):
        return self.get_action_url('view', batch)

    def execute_results(self):
        """
        Execute all batches which are returned from the current index query.
        Starts a separate thread for the execution, and displays a progress
        indicator page.
        """
        form = self.make_execute_form()
        if form.validate():
            kwargs = dict(form.validated)

            # cache options to use as defaults next time
            for key, value in form.validated.items():
                self.request.session['batch.{}.execute_option.{}'.format(self.model_class.batch_key, key)] = value

            key = '{}.execute_results'.format(self.model_class.__tablename__)
            batches = self.get_effective_data()
            progress = self.make_progress(key)
            kwargs['progress'] = progress
            thread = Thread(target=self.execute_results_thread, args=(batches, self.request.user.uuid), kwargs=kwargs)
            thread.start()

            return self.render_progress(progress, {
                'cancel_url': self.get_index_url(),
                'cancel_msg': "Batch execution was canceled",
            })

        self.request.session.flash("Invalid request: {}".format(form.make_deform_form().error), 'error')
        return self.redirect(self.get_index_url())

    def execute_results_thread(self, batches, user_uuid, progress=None, **kwargs):
        """
        Thread target for executing multiple batches with progress indicator.
        """
        app = self.get_rattail_app()
        model = self.model
        session = app.make_session()
        batches = batches.with_session(session).all()
        user = session.get(model.User, user_uuid)
        try:
            result = self.handler.execute_many(batches, user=user, progress=progress, **kwargs)

        # If anything goes wrong, rollback and log the error etc.
        except Exception as error:
            session.rollback()
            log.exception("execution failed for batch results")
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = self.execute_error_message(error)
                progress.session.save()

        # If no error, check result flag (false means user canceled).
        else:
            if result:
                session.commit()
                # TODO: this doesn't always work...?
                self.request.session.flash("{} {} were executed".format(
                    len(batches), self.get_model_title_plural()))
                success_url = self.get_execute_results_success_url(result, **kwargs)
            else:
                session.rollback()
                success_url = self.get_index_url()
            session.close()

            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = success_url
                progress.session.save()

    def get_execute_results_success_url(self, result, **kwargs):
        return self.get_index_url()

    def get_row_csv_fields(self):
        fields = super().get_row_csv_fields()
        fields = [field for field in fields
                  if field not in ('uuid', 'batch_uuid', 'removed')]
        return fields

    def get_row_results_csv_filename(self, batch):
        return '{}.{}.csv'.format(self.get_route_prefix(), batch.id_str)

    def get_row_results_xlsx_filename(self, batch):
        return '{}.{}.xlsx'.format(self.get_route_prefix(), batch.id_str)

    def clone(self):
        """
        Clone current batch as new batch
        """
        batch = self.get_instance()
        batch = self.handler.clone(batch, created_by=self.request.user)
        return self.redirect(self.get_action_url('view', batch))

    @classmethod
    def defaults(cls, config):
        cls._batch_defaults(config)
        cls._defaults(config)

    @classmethod
    def _batch_defaults(cls, config):
        rattail_config = config.registry.settings.get('rattail_config')
        model_key = cls.get_model_key()
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()
        instance_url_prefix = cls.get_instance_url_prefix()
        permission_prefix = cls.get_permission_prefix()
        model_title = cls.get_model_title()
        model_title_plural = cls.get_model_title_plural()

        # TODO: currently must do this here (in addition to `_defaults()` or
        # else the perm group label will not display correctly...
        config.add_tailbone_permission_group(permission_prefix, model_title_plural, overwrite=False)

        # populate row data
        config.add_route('{}.prefill'.format(route_prefix), '{}/{{uuid}}/prefill'.format(url_prefix))
        config.add_view(cls, attr='prefill', route_name='{}.prefill'.format(route_prefix),
                        permission='{}.create'.format(permission_prefix))

        # worksheet
        if cls.has_worksheet or cls.has_worksheet_file:
            config.add_tailbone_permission(permission_prefix, '{}.worksheet'.format(permission_prefix),
                                           "Edit {} data as worksheet".format(model_title))
        if cls.has_worksheet:
            config.add_route('{}.worksheet'.format(route_prefix), '{}/{{{}}}/worksheet'.format(url_prefix, model_key))
            config.add_view(cls, attr='worksheet', route_name='{}.worksheet'.format(route_prefix),
                            permission='{}.worksheet'.format(permission_prefix))
            config.add_route('{}.worksheet_update'.format(route_prefix), '{}/{{{}}}/worksheet/update'.format(url_prefix, model_key),
                             request_method='POST')
            config.add_view(cls, attr='worksheet_update', route_name='{}.worksheet_update'.format(route_prefix),
                            renderer='json', permission='{}.worksheet'.format(permission_prefix))

        # worksheet file
        if cls.has_worksheet_file:

            # download worksheet
            config.add_route('{}.download_worksheet'.format(route_prefix), '{}/download-worksheet'.format(instance_url_prefix))
            config.add_view(cls, attr='download_worksheet', route_name='{}.download_worksheet'.format(route_prefix),
                            permission='{}.worksheet'.format(permission_prefix))

            # upload worksheet
            config.add_route('{}.upload_worksheet'.format(route_prefix), '{}/upload-worksheet'.format(instance_url_prefix),
                             request_method='POST')
            config.add_view(cls, attr='upload_worksheet', route_name='{}.upload_worksheet'.format(route_prefix),
                            permission='{}.worksheet'.format(permission_prefix))

        # refresh batch data
        if cls.refreshable:
            config.add_route('{}.refresh'.format(route_prefix), '{}/{{uuid}}/refresh'.format(url_prefix))
            config.add_view(cls, attr='refresh', route_name='{}.refresh'.format(route_prefix),
                            permission='{}.refresh'.format(permission_prefix))
            config.add_tailbone_permission(permission_prefix, '{}.refresh'.format(permission_prefix),
                                           "Refresh data for {}".format(model_title))

        # delete row if executed
        if cls.rows_deletable_if_executed:
            config.add_tailbone_permission(permission_prefix,
                                           f'{permission_prefix}.delete_row_if_executed',
                                           "Delete rows after batch is executed")

        # toggle complete
        config.add_route('{}.toggle_complete'.format(route_prefix), '{}/{{{}}}/toggle-complete'.format(url_prefix, model_key))
        config.add_view(cls, attr='toggle_complete', route_name='{}.toggle_complete'.format(route_prefix),
                        permission='{}.edit'.format(permission_prefix))

        # refresh multiple batches (results)
        if cls.results_refreshable:
            config.add_route('{}.refresh_results'.format(route_prefix), '{}/refresh-results'.format(url_prefix),
                             request_method='POST')
            config.add_view(cls, attr='refresh_results', route_name='{}.refresh_results'.format(route_prefix),
                            permission='{}.refresh'.format(permission_prefix))

        # execute (multiple) batch results
        if cls.results_executable:
            config.add_route('{}.execute_results'.format(route_prefix), '{}/execute-results'.format(url_prefix),
                             request_method='POST')
            config.add_view(cls, attr='execute_results', route_name='{}.execute_results'.format(route_prefix),
                            permission='{}.execute_multiple'.format(permission_prefix))
            config.add_tailbone_permission(permission_prefix, '{}.execute_multiple'.format(permission_prefix),
                                           "Execute multiple {}".format(model_title_plural))


class FileBatchMasterView(BatchMasterView):
    """
    Base class for all file-based "batch master" views.
    """
    downloadable = True

    @property
    def upload_dir(self):
        """
        The path to the root upload folder, to be used as the ``storage_path``
        argument for the file field renderer.
        """
        uploads = os.path.join(
            self.rattail_config.require('rattail', 'batch.files'),
            'uploads')
        uploads = self.rattail_config.get('tailbone', 'batch.uploads',
                                          default=uploads)
        if not os.path.exists(uploads):
            os.makedirs(uploads)
        return uploads

    def configure_form(self, f):
        super().configure_form(f)
        batch = f.model_instance

        # filename
        if self.creating:
            # TODO: what's up with this re-insertion again..?
            # if 'filename' not in f.fields:
            #     f.fields.insert(0, 'filename')
            f.set_type('filename', 'file')
        else:
            f.set_readonly('filename')
            f.set_renderer('filename', self.render_downloadable_file)


class UploadWorksheet(colander.Schema):

    # this node is actually "replaced" when form is configured
    worksheet_file = colander.SchemaNode(colander.String())


class ToggleComplete(colander.MappingSchema):

    complete = colander.SchemaNode(colander.Boolean())
