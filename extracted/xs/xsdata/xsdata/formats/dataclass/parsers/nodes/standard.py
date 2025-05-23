from typing import Optional

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType


class StandardNode(XmlNode):
    """XmlNode for elements with a standard xsi:type.

    Args:
        meta: The parent xml meta instance
        var: The xml var instance
        datatype: The element standard xsi data type
        ns_map: The element namespace prefix-URI map
        config: The parser config instance
        nillable: Specifies whether nil content is allowed
        derived_factory: The derived element factory
    """

    __slots__ = (
        "config",
        "datatype",
        "derived_factory",
        "meta",
        "nillable",
        "ns_map",
        "var",
    )

    def __init__(
        self,
        meta: XmlMeta,
        var: XmlVar,
        datatype: DataType,
        ns_map: dict,
        config: ParserConfig,
        nillable: bool,
        derived_factory: Optional[type],
    ):
        """Initialize the xml node."""
        self.meta = meta
        self.var = var
        self.datatype = datatype
        self.ns_map = ns_map
        self.config = config
        self.nillable = nillable
        self.derived_factory = derived_factory

    def bind(
        self,
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: list,
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element text content.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Always true, it's not possible to fail during parsing
            for this node.
        """
        obj = ParserUtils.parse_var(
            meta=self.meta,
            var=self.var,
            config=self.config,
            value=text,
            types=[self.datatype.type],
            ns_map=self.ns_map,
            format=self.datatype.format,
        )

        if obj is None and not self.nillable:
            obj = ""

        if self.datatype.wrapper:
            obj = self.datatype.wrapper(obj)

        if self.derived_factory:
            obj = self.derived_factory(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
        """Raise an exception if there is a child element inside this node."""
        raise XmlContextError("StandardNode node doesn't support child nodes!")
