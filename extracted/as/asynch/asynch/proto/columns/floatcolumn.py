from ctypes import c_float

from ..utils import compat
from .base import FormatColumn


class FloatColumn(FormatColumn):
    py_types = (float,) + compat.integer_types


class Float32(FloatColumn):
    ch_type = "Float32"
    format = "f"

    def __init__(self, types_check=False, **kwargs):
        super().__init__(types_check=types_check, **kwargs)

        if types_check:
            # Chop only bytes that fit current type.
            # Cast to -nan or nan if overflows.
            def before_write_items(items, nulls_map=None):
                null_value = self.null_value

                for i, item in enumerate(items):
                    if nulls_map and nulls_map[i]:
                        items[i] = null_value
                    else:
                        items[i] = c_float(item).value

            self.before_write_items = before_write_items


class Float64(FloatColumn):
    ch_type = "Float64"
    format = "d"
