# coding=utf-8
"""SVG Desc class."""
from . import _mixins as m
from ._types import _str, _list_of_objs
from .element import Element


class Desc(Element, m.GraphicsElementEvents):
    """The <desc> element provides an accessible, long-text description of any element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/desc
    """
    element_name = 'desc'

    def __init__(self, content=None, class_=None):
        super(Desc, self).__init__()
        self.content = content
        self.class_ = class_

    @property
    def content(self):
        """[str]

        https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/content
        """
        return self._content

    @content.setter
    def content(self, value):
        self._content = _str(value, 'content', True)

    @property
    def class_(self):
        """[list of objs]

        https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/class
        """
        return self._class_

    @class_.setter
    def class_(self, value):
        self._class_ = _list_of_objs(value, str, 'class_', True)
