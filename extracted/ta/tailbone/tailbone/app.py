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
Application Entry Point
"""

import os

from sqlalchemy.orm import sessionmaker, scoped_session

from wuttjamaican.util import parse_list

from rattail.config import make_config
from rattail.exceptions import ConfigurationError

from pyramid.config import Configurator
from zope.sqlalchemy import register

import tailbone.db
from tailbone.auth import TailboneSecurityPolicy
from tailbone.config import csrf_token_name, csrf_header_name
from tailbone.util import get_effective_theme, get_theme_template_path
from tailbone.providers import get_all_providers


def make_rattail_config(settings):
    """
    Make a Rattail config object from the given settings.
    """
    rattail_config = settings.get('rattail_config')
    if not rattail_config:

        # initialize rattail config and embed in settings dict, to make
        # available for web requests later
        path = settings.get('rattail.config')
        if not path or not os.path.exists(path):
            raise ConfigurationError("Please set 'rattail.config' in [app:main] section of config "
                                     "to the path of your config file.  Lame, but necessary.")
        rattail_config = make_config(path)
        settings['rattail_config'] = rattail_config

    # nb. this is for compaibility with wuttaweb
    settings['wutta_config'] = rattail_config

    # must import all sqlalchemy models before things get rolling,
    # otherwise can have errors about continuum TransactionMeta class
    # not yet mapped, when relevant pages are first requested...
    # cf. https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/database/sqlalchemy.html#importing-all-sqlalchemy-models
    # hat tip to https://stackoverflow.com/a/59241485
    if getattr(rattail_config, 'tempmon_engine', None):
        from rattail_tempmon.db import model as tempmon_model, Session as TempmonSession
        tempmon_session = TempmonSession()
        tempmon_session.query(tempmon_model.Appliance).first()
        tempmon_session.close()

    # configure database sessions
    if hasattr(rattail_config, 'appdb_engine'):
        tailbone.db.Session.configure(bind=rattail_config.appdb_engine)
    if hasattr(rattail_config, 'trainwreck_engine'):
        tailbone.db.TrainwreckSession.configure(bind=rattail_config.trainwreck_engine)
    if hasattr(rattail_config, 'tempmon_engine'):
        tailbone.db.TempmonSession.configure(bind=rattail_config.tempmon_engine)

    # maybe set "future" behavior for SQLAlchemy
    if rattail_config.getbool('rattail.db', 'sqlalchemy_future_mode', usedb=False):
        tailbone.db.Session.configure(future=True)

    # create session wrappers for each "extra" Trainwreck engine
    for key, engine in rattail_config.trainwreck_engines.items():
        if key != 'default':
            Session = scoped_session(sessionmaker(bind=engine))
            register(Session)
            tailbone.db.ExtraTrainwreckSessions[key] = Session

    # Make sure rattail config object uses our scoped session, to avoid
    # unnecessary connections (and pooling limits).
    rattail_config._session_factory = lambda: (tailbone.db.Session(), False)

    return rattail_config


def provide_postgresql_settings(settings):
    """
    Add some PostgreSQL-specific settings to the app config.  Specifically,
    this enables retrying transactions a second time, in an attempt to
    gracefully handle database restarts.
    """
    try:
        import pyramid_retry
    except ImportError:
        settings.setdefault('tm.attempts', 2)
    else:
        settings.setdefault('retry.attempts', 2)


class Root(dict):
    """
    Root factory for Pyramid.  This is necessary to make the current request
    available to the authorization policy object, which needs it to check if
    the current request "is root".
    """

    def __init__(self, request):
        self.request = request


def make_pyramid_config(settings, configure_csrf=True):
    """
    Make a Pyramid config object from the given settings.
    """
    rattail_config = settings['rattail_config']

    config = settings.pop('pyramid_config', None)
    if config:
        config.set_root_factory(Root)
    else:

        # declare this web app of the "classic" variety
        settings.setdefault('tailbone.classic', 'true')

        # we want the new themes feature!
        establish_theme(settings)

        settings.setdefault('fanstatic.versioning', 'true')
        settings.setdefault('pyramid_deform.template_search_path', 'tailbone:templates/deform')
        config = Configurator(settings=settings, root_factory=Root)

    # add rattail config directly to registry, for access throughout the app
    config.registry['rattail_config'] = rattail_config

    # configure user authorization / authentication
    config.set_security_policy(TailboneSecurityPolicy())

    # maybe require CSRF token protection
    if configure_csrf:
        config.set_default_csrf_options(require_csrf=True,
                                        token=csrf_token_name(rattail_config),
                                        header=csrf_header_name(rattail_config))

    # Bring in some Pyramid goodies.
    config.include('tailbone.beaker')
    config.include('pyramid_deform')
    config.include('pyramid_fanstatic')
    config.include('pyramid_mako')
    config.include('pyramid_tm')

    # TODO: this may be a good idea some day, if wanting to leverage
    # deform resources for component JS?  cf. also base.mako template
    # # override default script mapping for deform
    # from deform import Field
    # from deform.widget import ResourceRegistry, default_resources
    # registry = ResourceRegistry(use_defaults=False)
    # for key in default_resources:
    #     registry.set_js_resources(key, None, {'js': []})
    # Field.set_default_resource_registry(registry)

    # bring in the pyramid_retry logic, if available
    # TODO: pretty soon we can require this package, hopefully..
    try:
        import pyramid_retry
    except ImportError:
        pass
    else:
        config.include('pyramid_retry')

    # fetch all tailbone providers
    providers = get_all_providers(rattail_config)
    for provider in providers.values():

        # configure DB sessions associated with transaction manager
        provider.configure_db_sessions(rattail_config, config)

        # add any static includes
        includes = provider.get_static_includes()
        if includes:
            for spec in includes:
                config.include(spec)

    # add some permissions magic
    config.add_directive('add_wutta_permission_group',
                         'wuttaweb.auth.add_permission_group')
    config.add_directive('add_wutta_permission',
                         'wuttaweb.auth.add_permission')
    # TODO: deprecate / remove these
    config.add_directive('add_tailbone_permission_group',
                         'wuttaweb.auth.add_permission_group')
    config.add_directive('add_tailbone_permission',
                         'wuttaweb.auth.add_permission')

    # and some similar magic for certain master views
    config.add_directive('add_tailbone_index_page', 'tailbone.app.add_index_page')
    config.add_directive('add_tailbone_config_page', 'tailbone.app.add_config_page')
    config.add_directive('add_tailbone_model_view', 'tailbone.app.add_model_view')
    config.add_directive('add_tailbone_view_supplement', 'tailbone.app.add_view_supplement')

    config.add_directive('add_tailbone_websocket', 'tailbone.app.add_websocket')

    return config


def add_websocket(config, name, view, attr=None):
    """
    Register a websocket entry point for the app.
    """
    def action():
        rattail_config = config.registry.settings['rattail_config']
        rattail_app = rattail_config.get_app()

        if isinstance(view, str):
            view_callable = rattail_app.load_object(view)
        else:
            view_callable = view
        view_callable = view_callable(config)
        if attr:
            view_callable = getattr(view_callable, attr)

        # register route
        path = '/ws/{}'.format(name)
        route_name = 'ws.{}'.format(name)
        config.add_route(route_name, path, static=True)

        # register view callable
        websockets = config.registry.setdefault('tailbone_websockets', {})
        websockets[path] = view_callable

    config.action('tailbone-add-websocket-{}'.format(name), action,
                  # nb. since this action adds routes, it must happen
                  # sooner in the order than it normally would, hence
                  # we declare that
                  order=-20)


def add_index_page(config, route_name, label, permission):
    """
    Register a config page for the app.
    """
    def action():
        pages = config.get_settings().get('tailbone_index_pages', [])
        pages.append({'label': label, 'route': route_name,
                      'permission': permission})
        config.add_settings({'tailbone_index_pages': pages})
    config.action(None, action)


def add_config_page(config, route_name, label, permission):
    """
    Register a config page for the app.
    """
    def action():
        pages = config.get_settings().get('tailbone_config_pages', [])
        pages.append({'label': label, 'route': route_name,
                      'permission': permission})
        config.add_settings({'tailbone_config_pages': pages})
    config.action(None, action)


def add_model_view(config, model_name, label, route_prefix, permission_prefix):
    """
    Register a model view for the app.
    """
    def action():
        all_views = config.get_settings().get('tailbone_model_views', {})

        model_views = all_views.setdefault(model_name, [])
        model_views.append({
            'label': label,
            'route_prefix': route_prefix,
            'permission_prefix': permission_prefix,
        })

        config.add_settings({'tailbone_model_views': all_views})

    config.action(None, action)


def add_view_supplement(config, route_prefix, cls):
    """
    Register a master view supplement for the app.
    """
    def action():
        supplements = config.get_settings().get('tailbone_view_supplements', {})
        supplements.setdefault(route_prefix, []).append(cls)
        config.add_settings({'tailbone_view_supplements': supplements})
    config.action(None, action)


def establish_theme(settings):
    rattail_config = settings['rattail_config']

    theme = get_effective_theme(rattail_config)
    settings['tailbone.theme'] = theme

    directories = settings['mako.directories']
    if isinstance(directories, str):
        directories = parse_list(directories)

    path = get_theme_template_path(rattail_config)
    directories.insert(0, path)
    settings['mako.directories'] = directories


def configure_postgresql(pyramid_config):
    """
    Add some PostgreSQL-specific tweaks to the final app config.  Specifically,
    adds the tween necessary for graceful handling of database restarts.
    """
    pyramid_config.add_tween('tailbone.tweens.sqlerror_tween_factory',
                             under='pyramid_tm.tm_tween_factory')


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    settings.setdefault('mako.directories', ['tailbone:templates',
                                             'wuttaweb:templates'])
    rattail_config = make_rattail_config(settings)
    pyramid_config = make_pyramid_config(settings)
    pyramid_config.include('tailbone')
    return pyramid_config.make_wsgi_app()
