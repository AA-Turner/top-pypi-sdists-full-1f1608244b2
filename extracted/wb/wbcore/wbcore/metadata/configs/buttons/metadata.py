from rest_framework.metadata import SimpleMetadata


class ButtonMetadata(SimpleMetadata):
    def generate_metadata(self, request, view):
        if hasattr(super(), "generate_metadata"):
            yield from super().generate_metadata(request, view)
        yield "buttons", [btn.serialize(request=request) for btn in view.get_buttons(request)]
