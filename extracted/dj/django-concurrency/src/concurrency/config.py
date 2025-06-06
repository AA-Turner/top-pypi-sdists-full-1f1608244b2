from django.core.exceptions import ImproperlyConfigured
from django.test.signals import setting_changed
from django.utils.module_loading import import_string

from .compat import get_callable

# List Editable Policy
# 1 do not save updated records, save others, show message to the user
# 2 abort whole transaction
CONCURRENCY_LIST_EDITABLE_POLICY_SILENT = 1
CONCURRENCY_LIST_EDITABLE_POLICY_ABORT_ALL = 2
CONCURRENCY_POLICY_RAISE = 4
CONCURRENCY_POLICY_CALLBACK = 8

LIST_EDITABLE_POLICIES = [
    CONCURRENCY_LIST_EDITABLE_POLICY_SILENT,
    CONCURRENCY_LIST_EDITABLE_POLICY_ABORT_ALL,
]


class AppSettings:
    defaults = {
        "ENABLED": True,
        "AUTO_CREATE_TRIGGERS": True,
        "FIELD_SIGNER": "concurrency.forms.VersionFieldSigner",
        "POLICY": CONCURRENCY_LIST_EDITABLE_POLICY_SILENT,
        "CALLBACK": "concurrency.views.callback",
        "HANDLER409": "concurrency.views.conflict",
        "VERSION_FIELD_REQUIRED": True,
        "TRIGGERS_FACTORY": {
            "postgresql": "concurrency.triggers.PostgreSQL",
            "mysql": "concurrency.triggers.MySQL",
            "sqlite3": "concurrency.triggers.Sqlite3",
            "sqlite": "concurrency.triggers.Sqlite3",
        },
    }

    def __init__(self, prefix) -> None:
        """
        Loads our settings from django.conf.settings, applying defaults for any
        that are omitted.
        """
        self.prefix = prefix
        from django.conf import settings

        for name, default in self.defaults.items():
            prefix_name = (self.prefix + "_" + name).upper()
            value = getattr(settings, prefix_name, default)
            self._set_attr(prefix_name, value)
            setattr(settings, prefix_name, value)
            setting_changed.send(self.__class__, setting=prefix_name, value=value, enter=True)

        setting_changed.connect(self._handler)

    def _set_attr(self, prefix_name, value) -> None:
        name = prefix_name[1 + len(self.prefix) :]
        if name == "IGNORE_DEFAULT":
            raise ImproperlyConfigured(
                "IGNORE_DEFAULT has been removed in django-concurrency 1.5. Use VERSION_FIELD_REQUIRED instead"
            )
        if name == "CALLBACK":
            if isinstance(value, str):
                func = get_callable(value)
            elif callable(value):
                func = value
            else:
                msg = f"{value} is not a valid value for `CALLBACK`. It must be a callable or a fullpath to callable. "
                raise ImproperlyConfigured(msg)
            self._callback = func
        elif name == "TRIGGERS_FACTORY":
            original = dict(value)
            for k, v in original.items():
                try:
                    value[k] = import_string(v)
                except ImportError as e:
                    raise ImproperlyConfigured(f"Unable to load {k} TriggerFactory. Invalid fqn '{v}': {e}")

        setattr(self, name, value)

    def _handler(self, sender, setting, value, **kwargs) -> None:
        """
            handler for ``setting_changed`` signal.

        @see :ref:`django:setting-changed`_
        """
        if setting.startswith(self.prefix):
            self._set_attr(setting, value)


conf = AppSettings("CONCURRENCY")
