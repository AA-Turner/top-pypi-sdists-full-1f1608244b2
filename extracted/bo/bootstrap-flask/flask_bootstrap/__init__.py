import warnings

from flask import current_app, Blueprint, url_for
from markupsafe import Markup
from wtforms import BooleanField, HiddenField

CDN_BASE = 'https://cdn.jsdelivr.net/npm'


def is_hidden_field_filter(field):
    return isinstance(field, HiddenField)


def raise_helper(message):
    raise RuntimeError(message)


def get_table_titles(data, primary_key, primary_key_title):
    """Detect and build the table titles tuple from ORM object, currently only support SQLAlchemy.

    .. versionadded:: 1.4.0
    """
    if not data:
        return []
    titles = []
    for k in data[0].__table__.columns.keys():
        if not k.startswith('_'):  # pragma: no branch
            titles.append((k, k.replace('_', ' ').title()))
    titles[0] = (primary_key, primary_key_title)
    return titles


class _Bootstrap:
    """
    Base extension class for different Bootstrap versions.

    .. versionadded:: 2.0.0
    """

    bootstrap_version = None
    jquery_version = None
    popper_version = None
    icons_version = None
    bootstrap_css_integrity = None
    bootstrap_js_integrity = None
    jquery_integrity = None
    popper_integrity = None
    static_folder = None
    bootstrap_css_filename = 'bootstrap.min.css'
    bootstrap_js_filename = 'bootstrap.min.js'
    jquery_filename = 'jquery.min.js'
    popper_filename = 'popper.min.js'

    def __init__(self, app=None):
        if app is not None:  # pragma: no branch
            self.init_app(app)

    def init_app(self, app):

        if not hasattr(app, 'extensions'):
            app.extensions = {}  # pragma: no cover
        app.extensions['bootstrap'] = self

        blueprint = Blueprint('bootstrap', __name__, static_folder=f'static/{self.static_folder}',
                              static_url_path=f'/bootstrap{app.static_url_path}',
                              template_folder='templates')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['bootstrap'] = self
        app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter
        app.jinja_env.globals['get_table_titles'] = get_table_titles
        app.jinja_env.globals['warn'] = warnings.warn
        app.jinja_env.globals['raise'] = raise_helper
        app.jinja_env.add_extension('jinja2.ext.do')
        # default settings
        app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False)
        app.config.setdefault('BOOTSTRAP_BTN_STYLE', 'primary')
        app.config.setdefault('BOOTSTRAP_BTN_SIZE', 'md')
        app.config.setdefault('BOOTSTRAP_BOOTSWATCH_THEME', None)
        app.config.setdefault('BOOTSTRAP_ICON_SIZE', '1em')
        app.config.setdefault('BOOTSTRAP_ICON_COLOR', None)
        app.config.setdefault('BOOTSTRAP_ICON_USE_FONT', False)
        app.config.setdefault('BOOTSTRAP_MSG_CATEGORY', 'primary')
        app.config.setdefault('BOOTSTRAP_TABLE_VIEW_TITLE', 'View')
        app.config.setdefault('BOOTSTRAP_TABLE_EDIT_TITLE', 'Edit')
        app.config.setdefault('BOOTSTRAP_TABLE_DELETE_TITLE', 'Delete')
        app.config.setdefault('BOOTSTRAP_TABLE_NEW_TITLE', 'New')
        app.config.setdefault('BOOTSTRAP_FORM_GROUP_CLASSES', 'mb-3')  # Bootstrap 5 only
        app.config.setdefault(
            'BOOTSTRAP_FORM_INLINE_CLASSES',
            'row row-cols-lg-auto g-3 align-items-center'
        )  # Bootstrap 5 only

    def load_css(self, version=None, bootstrap_sri=None, bootswatch_theme=None):
        """Load Bootstrap's css resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        :param bootswatch_theme: Set the bootswatch theme at the request/session level.
        """
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        bootswatch_theme = bootswatch_theme or current_app.config['BOOTSTRAP_BOOTSWATCH_THEME']
        if version is None:
            version = self.bootstrap_version
        bootstrap_sri = self._get_sri('bootstrap_css', version, bootstrap_sri)

        if serve_local:
            if not bootswatch_theme:
                base_path = 'css'
            else:
                base_path = f'css/bootswatch/{bootswatch_theme.lower()}'
            bootstrap_url = url_for('bootstrap.static', filename=f'{base_path}/{self.bootstrap_css_filename}')
        else:
            if not bootswatch_theme:
                base_path = f'{CDN_BASE}/bootstrap@{version}/dist/css'
            else:
                base_path = f'{CDN_BASE}/bootswatch@{version}/dist/{bootswatch_theme.lower()}'
            bootstrap_url = f'{base_path}/{self.bootstrap_css_filename}'

        if bootstrap_sri and not bootswatch_theme:
            css = f'<link rel="stylesheet" href="{bootstrap_url}" integrity="{bootstrap_sri}" crossorigin="anonymous">'
        else:
            css = f'<link rel="stylesheet" href="{bootstrap_url}">'
        return Markup(css)

    def load_icon_font_css(self):
        """Load Bootstrap's css icon font resource.

        .. versionadded:: 2.4.2
        """
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        if serve_local:
            icons_url = url_for('bootstrap.static', filename='css/font/bootstrap-icons.min.css')
        else:
            icons_url = f'{CDN_BASE}/bootstrap-icons@{self.icons_version}/font/bootstrap-icons.min.css'
        css = f'<link rel="stylesheet" href="{icons_url}">'
        return Markup(css)

    def _get_js_script(self, version, name, sri, nonce):
        """Get <script> tag for JavaScript resources."""
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        paths = {
            'bootstrap': f'js/{self.bootstrap_js_filename}',
            'jquery': f'{self.jquery_filename}',
            '@popperjs/core': f'umd/{self.popper_filename}',
            'popper.js': f'umd/{self.popper_filename}',
        }
        if serve_local:
            url = url_for('bootstrap.static', filename=paths[name])
        else:
            url = f'{CDN_BASE}/{name}@{version}/dist/{paths[name]}'
        nonce_attribute = f' nonce="{nonce}"' if nonce else ''
        sri_attributes = f' integrity="{sri}" crossorigin="anonymous"' if sri else ''
        return f'<script src="{url}"{sri_attributes}{nonce_attribute}></script>'

    def _get_sri(self, name, version, sri):
        serve_local = current_app.config['BOOTSTRAP_SERVE_LOCAL']
        sris = {
            'bootstrap_css': self.bootstrap_css_integrity,
            'bootstrap_js': self.bootstrap_js_integrity,
            'jquery': self.jquery_integrity,
            'popper': self.popper_integrity,
        }
        versions = {
            'bootstrap_css': self.bootstrap_version,
            'bootstrap_js': self.bootstrap_version,
            'jquery': self.jquery_version,
            'popper': self.popper_version
        }
        if sri is not None:
            return sri
        if version == versions[name] and serve_local is False:
            return sris[name]
        return None

    def load_js(self, version=None, jquery_version=None,  # noqa: C901
                popper_version=None, with_jquery=True, with_popper=True,
                bootstrap_sri=None, jquery_sri=None, popper_sri=None,
                nonce=None):
        """Load Bootstrap and related library's js resources with given version.

        .. versionadded:: 0.1.0

        :param version: The version of Bootstrap.
        :param jquery_version: The version of jQuery (only needed with Bootstrap 4).
        :param popper_version: The version of Popper.js.
        :param with_jquery: Include jQuery or not (only needed with Bootstrap 4).
        :param with_popper: Include Popper.js or not.
        :param bootstrap_sri: The integrity attribute value of Bootstrap for SRI
        :param jquery_sri: The integrity attribute value of jQuery for SRI
        :param popper_sri: The integrity attribute value of Popper.js for SRI
        :param nonce: The nonce attribute value for use with strict CSP
        """
        if version is None:
            version = self.bootstrap_version
        if popper_version is None:
            popper_version = self.popper_version

        bootstrap_sri = self._get_sri('bootstrap_js', version, bootstrap_sri)
        popper_sri = self._get_sri('popper', popper_version, popper_sri)
        bootstrap = self._get_js_script(version, 'bootstrap', bootstrap_sri, nonce)
        popper = self._get_js_script(popper_version, self.popper_name, popper_sri, nonce) if with_popper else ''
        if version.startswith('4'):
            if jquery_version is None:
                jquery_version = self.jquery_version
            jquery_sri = self._get_sri('jquery', jquery_version, jquery_sri)
            jquery = self._get_js_script(jquery_version, 'jquery', jquery_sri, nonce) if with_jquery else ''
            return Markup(f'''{jquery}
        {popper}
        {bootstrap}''')
        return Markup(f'''{popper}
        {bootstrap}''')


class Bootstrap4(_Bootstrap):
    """
    Extension class for Bootstrap 4.

    Initialize the extension::

        from flask import Flask
        from flask_bootstrap import Bootstrap4

        app = Flask(__name__)
        bootstrap = Bootstrap4(app)

    Or with the application factory::

        from flask import Flask
        from flask_bootstrap import Bootstrap4

        bootstrap = Bootstrap4()

        def create_app():
            app = Flask(__name__)
            bootstrap.init_app(app)

    .. versionchanged:: 2.0.0
       Move common logic to base class ``_Bootstrap``.
    """

    bootstrap_version = '4.6.1'
    jquery_version = '3.5.1'
    popper_version = '1.16.1'
    icons_version = '1.11.3'
    bootstrap_css_integrity = 'sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn'
    bootstrap_js_integrity = 'sha384-VHvPCCyXqtD5DqJeNxl2dtTyhF78xXNXdkwX1CZeRusQfRKp+tA7hAShOK/B/fQ2'
    jquery_integrity = 'sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0='
    popper_integrity = 'sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN'
    popper_name = 'popper.js'
    static_folder = 'bootstrap4'


class Bootstrap5(_Bootstrap):
    """
    Base class for Bootstrap 5.

    Initialize the extension::

        from flask import Flask
        from flask_bootstrap import Bootstrap5

        app = Flask(__name__)
        bootstrap = Bootstrap5(app)

    Or with the application factory::

        from flask import Flask
        from flask_bootstrap import Bootstrap5

        bootstrap = Bootstrap5()

        def create_app():
            app = Flask(__name__)
            bootstrap.init_app(app)

    .. versionadded:: 2.0.0
    """
    bootstrap_version = '5.3.5'
    popper_version = '2.11.8'
    icons_version = '1.11.3'
    bootstrap_css_integrity = 'sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7'
    bootstrap_js_integrity = 'sha384-VQqxDN0EQCkWoxt/0vsQvZswzTHUVOImccYmSyhJTp7kGtPed0Qcx8rK9h9YEgx+'
    popper_integrity = 'sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r'
    popper_name = '@popperjs/core'
    static_folder = 'bootstrap5'


class Bootstrap(Bootstrap4):
    def __init__(self, app=None):
        super().__init__(app=app)
        warnings.warn(
            'For Bootstrap 4, please import and use "Bootstrap4" class, the "Bootstrap" class '
            'is deprecated and will be removed in 3.0.',
            stacklevel=2
        )


class SwitchField(BooleanField):
    """
    A wrapper field for ``BooleanField`` that renders as a Bootstrap switch.

    .. versionadded:: 2.0.0
    """

    def __init__(self, label=None, **kwargs):
        super().__init__(label, **kwargs)
