from __future__ import annotations
from .formatter import BaseFormatter
from .exceptions import BaseExceptions
from .extractor import BaseExtractors
from .loaders import BaseLoaders
from .controller import BaseControllerUtils
from .query import BaseQueryUtils

class BaseUtils:
    Formatter = BaseFormatter
    Exceptions = BaseExceptions
    Extractors = BaseExtractors
    Loaders = BaseLoaders
    Controller = BaseControllerUtils
    Query = BaseQueryUtils