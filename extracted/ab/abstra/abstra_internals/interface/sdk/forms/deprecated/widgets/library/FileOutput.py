import io
from typing import Union

from abstra_internals.interface.sdk.forms.deprecated.widgets.file_utils import (
    upload_widget_file,
)
from abstra_internals.interface.sdk.forms.deprecated.widgets.widget_base import Output


class FileOutput(Output):
    type = "file-output"

    def __init__(self, file: Union[str, io.IOBase], **kwargs):
        self.set_props(dict(file=file, **kwargs))

    def set_props(self, props):
        self.file = upload_widget_file(props.get("file", ""))
        self.download_text = props.get("download_text", "Download")
        self.full_width = props.get("full_width", False)
        super().set_props(props)

    def render(self, ctx: dict):
        return {
            "type": self.type,
            "fileUrl": self.file,
            "downloadText": self.download_text,
            "fullWidth": self.full_width,
        }
