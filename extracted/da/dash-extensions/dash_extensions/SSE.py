# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class SSE(Component):
    """A SSE component.
The SSE component makes it possible to collect data from e.g. a ResponseStream. It's a wrapper around the SSE.js library.
https://github.com/mpetazzoni/sse.js

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- animate_chunk (number; optional):
    Chunk size (i.e. number of characters) for the animation.

- animate_delay (number; optional):
    If set, each character is delayed by some amount of time. Used to
    animate the stream.

- animate_prefix (string; optional):
    Prefix to be excluded from the animation.

- animate_suffix (string; optional):
    Suffix to be excluded from the animation.

- animation (string; optional):
    The animation of the data.

- concat (boolean; optional):
    A boolean indicating if the stream values should be concatenated.

- done (boolean; optional):
    A boolean indicating if the (current) stream has ended.

- options (dict; optional):
    Options passed to the SSE constructor.

    `options` is a dict with keys:

    - headers (dict with strings as keys and values of type string; optional):
        - headers.

    - payload (string; optional):
        - payload as a Blob, ArrayBuffer, Dataview, FormData,
        URLSearchParams, or string.

    - method (string; optional):
        - HTTP Method.

    - withCredentials (boolean; optional):
        - flag, if credentials needed.

    - start (boolean; optional):
        - flag, if streaming should start automatically.

    - debug (boolean; optional):
        - debugging flag.

- url (string; optional):
    URL of the endpoint.

- value (string; optional):
    The data value. Either the latest, or the concatenated depending
    on the `concat` property."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_extensions'
    _type = 'SSE'
    Options = TypedDict(
        "Options",
            {
            "headers": NotRequired[typing.Dict[typing.Union[str, float, int], str]],
            "payload": NotRequired[typing.Union[str]],
            "method": NotRequired[str],
            "withCredentials": NotRequired[bool],
            "start": NotRequired[bool],
            "debug": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        options: typing.Optional["Options"] = None,
        url: typing.Optional[str] = None,
        concat: typing.Optional[bool] = None,
        animate_delay: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        animate_chunk: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        animate_prefix: typing.Optional[str] = None,
        animate_suffix: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        animation: typing.Optional[str] = None,
        done: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'animate_chunk', 'animate_delay', 'animate_prefix', 'animate_suffix', 'animation', 'concat', 'done', 'options', 'url', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animate_chunk', 'animate_delay', 'animate_prefix', 'animate_suffix', 'animation', 'concat', 'done', 'options', 'url', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SSE, self).__init__(**args)
