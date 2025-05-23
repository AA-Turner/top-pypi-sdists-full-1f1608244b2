import inspect
import threading
import allure_commons
from allure_commons.logger import AllureFileLogger
from allure_behave.listener import AllureListener
from behave.configuration import Configuration

HOOKS = [
    "after_all",
    "before_feature",
    "after_feature",
    "before_scenario",
    "after_scenario",
    "before_step",
    "after_step"
]

_storage = threading.local()


def wrapper(original, allured):
    def hook(*args, **kwargs):
        allured(*args, **kwargs)
        return original(*args, **kwargs)

    return hook


def allure_report(result_dir="allure_results"):
    allure_hooks = AllureHooks(result_dir)
    frame = inspect.currentframe()
    try:
        for hook_name in HOOKS:
            if hook_name in frame.f_back.f_locals:
                frame.f_back.f_locals[hook_name] = wrapper(frame.f_back.f_locals[hook_name],
                                                           getattr(allure_hooks, hook_name))
            else:
                frame.f_back.f_locals[hook_name] = getattr(allure_hooks, hook_name)
    finally:
        del frame


class AllureHooks:
    def __init__(self, result_dir):
        self.listener = AllureListener(Configuration())
        self.plugins = []

        if not hasattr(_storage, 'file_logger'):
            logger = AllureFileLogger(result_dir)
            _storage.file_logger = logger
            allure_commons.plugin_manager.register(logger)
            self.plugins.append(logger)

        allure_commons.plugin_manager.register(self.listener)
        self.plugins.append(self.listener)

    def after_all(self, context):
        for plugin in self.plugins:
            name = allure_commons.plugin_manager.get_name(plugin)
            if allure_commons.plugin_manager.has_plugin(name):
                allure_commons.plugin_manager.unregister(name=name)

    def before_feature(self, context, feature):
        self.listener.start_file()

    def after_feature(self, context, feature):
        self.listener.stop_feature()

    def before_scenario(self, context, scenario):
        self.listener.start_scenario(scenario)

    def after_scenario(self, context, scenario):
        self.listener.stop_scenario(scenario)

    def before_step(self, context, step):
        self.listener.start_behave_step(step)

    def after_step(self, context, step):
        self.listener.stop_behave_step(step)
