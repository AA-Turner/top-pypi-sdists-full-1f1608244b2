from enum import Enum


class EditWorkspaceDeployUISettingsJsonBodyDeployUiSettingsIncludeTypeItem(str, Enum):
    APP = "app"
    FLOW = "flow"
    RESOURCE = "resource"
    SCRIPT = "script"
    SECRET = "secret"
    TRIGGER = "trigger"
    VARIABLE = "variable"

    def __str__(self) -> str:
        return str(self.value)
