#!/usr/bin/env python3
from _ast import Expr
from _ast import ImportFrom
import ast
import copy
import os
import sys
from typing import Any
from typing import Dict  # noqa:F401
from typing import List
from typing import Set
from typing import Text
from typing import Tuple  # noqa:F401

from ..._constants import IAST
from .._metrics import _set_metric_iast_instrumented_propagation
from ..constants import DEFAULT_PATH_TRAVERSAL_FUNCTIONS
from ..constants import DEFAULT_SOURCE_IO_FUNCTIONS
from ..constants import DEFAULT_WEAK_RANDOMNESS_FUNCTIONS


PY39_PLUS = sys.version_info >= (3, 9, 0)

_PREFIX = IAST.PATCH_ADDED_SYMBOL_PREFIX
CODE_TYPE_FIRST_PARTY = "first_party"
CODE_TYPE_DD = "datadog"
CODE_TYPE_SITE_PACKAGES = "site_packages"
CODE_TYPE_STDLIB = "stdlib"
TAINT_SINK_FUNCTION_REPLACEMENT = _PREFIX + "taint_sinks.ast_function"
SOURCES_FUNCTION_REPLACEMENT = _PREFIX + "sources.ast_function"


def _mark_avoid_convert_recursively(node):
    if node is not None:
        node.avoid_convert = True
        for child in ast.iter_child_nodes(node):
            _mark_avoid_convert_recursively(child)


_ASPECTS_SPEC: Dict[Text, Any] = {
    "definitions_module": "ddtrace.appsec._iast._taint_tracking.aspects",
    "alias_module": _PREFIX + "aspects",
    "functions": {
        "StringIO": _PREFIX + "aspects.stringio_aspect",
        "BytesIO": _PREFIX + "aspects.bytesio_aspect",
        "str": _PREFIX + "aspects.str_aspect",
        "bytes": _PREFIX + "aspects.bytes_aspect",
        "bytearray": _PREFIX + "aspects.bytearray_aspect",
        "ddtrace_iast_flask_patch": _PREFIX + "aspects.empty_func",  # To avoid recursion
    },
    "stringalike_methods": {
        "StringIO": _PREFIX + "aspects.stringio_aspect",
        "BytesIO": _PREFIX + "aspects.bytesio_aspect",
        "decode": _PREFIX + "aspects.decode_aspect",
        "join": _PREFIX + "aspects.join_aspect",
        "encode": _PREFIX + "aspects.encode_aspect",
        "extend": _PREFIX + "aspects.bytearray_extend_aspect",
        "upper": _PREFIX + "aspects.upper_aspect",
        "lower": _PREFIX + "aspects.lower_aspect",
        "replace": _PREFIX + "aspects.replace_aspect",
        "swapcase": _PREFIX + "aspects.swapcase_aspect",
        "title": _PREFIX + "aspects.title_aspect",
        "capitalize": _PREFIX + "aspects.capitalize_aspect",
        "casefold": _PREFIX + "aspects.casefold_aspect",
        "translate": _PREFIX + "aspects.translate_aspect",
        "format": _PREFIX + "aspects.format_aspect",
        "format_map": _PREFIX + "aspects.format_map_aspect",
        "zfill": _PREFIX + "aspects.zfill_aspect",
        "ljust": _PREFIX + "aspects.ljust_aspect",
        "split": _PREFIX + "aspects.split_aspect",  # Both regular split and re.split
        "rsplit": _PREFIX + "aspects.rsplit_aspect",
        "splitlines": _PREFIX + "aspects.splitlines_aspect",
        "lstrip": _PREFIX + "aspects.lstrip_aspect",
        "rstrip": _PREFIX + "aspects.rstrip_aspect",
        "strip": _PREFIX + "aspects.strip_aspect",
        # re module and re.Match methods
        "findall": _PREFIX + "aspects.re_findall_aspect",
        "finditer": _PREFIX + "aspects.re_finditer_aspect",
        "fullmatch": _PREFIX + "aspects.re_fullmatch_aspect",
        "expand": _PREFIX + "aspects.re_expand_aspect",
        "group": _PREFIX + "aspects.re_group_aspect",
        "groups": _PREFIX + "aspects.re_groups_aspect",
        "match": _PREFIX + "aspects.re_match_aspect",
        "search": _PREFIX + "aspects.re_search_aspect",
        "sub": _PREFIX + "aspects.re_sub_aspect",
        "subn": _PREFIX + "aspects.re_subn_aspect",
    },
    # Replacement function for indexes and ranges
    "slices": {
        "index": _PREFIX + "aspects.index_aspect",
        "slice": _PREFIX + "aspects.slice_aspect",
    },
    # Replacement functions for modules
    "module_functions": {
        "os.path": {
            "basename": _PREFIX + "aspects.ospathbasename_aspect",
            "dirname": _PREFIX + "aspects.ospathdirname_aspect",
            "join": _PREFIX + "aspects.ospathjoin_aspect",
            "normcase": _PREFIX + "aspects.ospathnormcase_aspect",
            "split": _PREFIX + "aspects.ospathsplit_aspect",
            "splitext": _PREFIX + "aspects.ospathsplitext_aspect",
        }
    },
    "operators": {
        ast.Add: _PREFIX + "aspects.add_aspect",
        "INPLACE_ADD": _PREFIX + "aspects.add_inplace_aspect",
        "FORMAT_VALUE": _PREFIX + "aspects.format_value_aspect",
        ast.Mod: _PREFIX + "aspects.modulo_aspect",
        "BUILD_STRING": _PREFIX + "aspects.build_string_aspect",
    },
    "excluded_from_patching": {
        # Key: module being patched
        # Value: dict with more info
        "django.utils.formats": {
            # Key: called functions that won't be patched. E.g.: for this module
            # not a single call for format on any function will be patched.
            #
            # Value: function definitions. E.g.: we won't patch any Call node inside
            # the iter_format_modules(). If we, for example, had 'foo': ('bar', 'baz')
            # it would mean that we wouldn't patch any call to foo() done inside the
            # bar() or baz() function definitions.
            "format": ("",),
            "": ("iter_format_modules",),
        },
        "django.utils.log": {
            "": ("",),
        },
        "django.utils.html": {"": ("format_html", "format_html_join")},
        "sqlalchemy.sql.compiler": {"": ("_requires_quotes",)},
        # Our added functions
        "": {"": (f"{_PREFIX}dir", f"{_PREFIX}set_dir_filter")},
    },
    # This is a set since all functions will be replaced by taint_sink_functions
    "taint_sinks": {
        "weak_randomness": DEFAULT_WEAK_RANDOMNESS_FUNCTIONS,
        "path_traversal": DEFAULT_PATH_TRAVERSAL_FUNCTIONS,
        # These explicitly WON'T be replaced by taint_sink_function:
        "disabled": {
            "__new__",
            "__init__",
            "__dir__",
            "__repr__",
            "super",
        },
    },
    "sources": {"io": DEFAULT_SOURCE_IO_FUNCTIONS, "disabled": {}},
}


if sys.version_info >= (3, 12):
    _ASPECTS_SPEC["module_functions"]["os.path"]["splitroot"] = _PREFIX + "aspects.ospathsplitroot_aspect"

if sys.version_info >= (3, 12) or os.name == "nt":
    _ASPECTS_SPEC["module_functions"]["os.path"]["splitdrive"] = _PREFIX + "aspects.ospathsplitdrive_aspect"


class AstVisitor(ast.NodeTransformer):
    def __init__(
        self,
        filename="",
        module_name="",
    ):
        self._sinkpoints_spec = {
            "definitions_module": "ddtrace.appsec._iast.taint_sinks",
            "alias_module": _PREFIX + "taint_sinks",
        }
        self._source_spec = {
            "definitions_module": "ddtrace.appsec._iast.sources",
            "alias_module": _PREFIX + "sources",
        }

        self._aspect_index = _ASPECTS_SPEC["slices"]["index"]
        self._aspect_slice = _ASPECTS_SPEC["slices"]["slice"]
        self._aspect_functions = _ASPECTS_SPEC["functions"]
        self._aspect_operators = _ASPECTS_SPEC["operators"]
        self._aspect_methods = _ASPECTS_SPEC["stringalike_methods"]
        self._aspect_modules = _ASPECTS_SPEC["module_functions"]
        self._aspect_format_value = _ASPECTS_SPEC["operators"]["FORMAT_VALUE"]
        self._aspect_build_string = _ASPECTS_SPEC["operators"]["BUILD_STRING"]

        # Sink points
        self._taint_sink_replace_any = self._merge_dicts(
            _ASPECTS_SPEC["taint_sinks"]["weak_randomness"],
            *[functions for module, functions in _ASPECTS_SPEC["taint_sinks"]["path_traversal"].items()],
        )
        self._source_replace_any = self._merge_dicts(
            *[functions for module, functions in _ASPECTS_SPEC["sources"]["io"].items()],
        )

        self._taint_sink_replace_disabled = _ASPECTS_SPEC["taint_sinks"]["disabled"]

        self.update_location(filename, module_name)

    def update_location(self, filename: str = "", module_name: str = ""):
        self.filename = filename
        self.module_name = module_name
        self.ast_modified = False

        excluded_from_patching: Dict[str, Dict[str, Tuple[str]]] = _ASPECTS_SPEC["excluded_from_patching"]
        self.excluded_functions = excluded_from_patching.get(self.module_name, {})
        self.dont_patch_these_functionsdefs = set()
        for _, v in self.excluded_functions.items():
            if v:
                for i in v:
                    self.dont_patch_these_functionsdefs.add(i)

        # This will be enabled when we find a module and function where we avoid doing
        # replacements and enabled again on all the others
        self.replacements_disabled_for_functiondef = False

        self.codetype = CODE_TYPE_FIRST_PARTY
        if "ast/tests/fixtures" in self.filename:
            self.codetype = CODE_TYPE_FIRST_PARTY
        elif "ddtrace" in self.filename and ("site-packages" in self.filename or "dist-packages" in self.filename):
            self.codetype = CODE_TYPE_DD
        elif "site-packages" in self.filename or "dist-packages" in self.filename:
            self.codetype = CODE_TYPE_SITE_PACKAGES
        elif "lib/python" in self.filename:
            self.codetype = CODE_TYPE_STDLIB

    @staticmethod
    def _merge_dicts(*args_functions: Set[str]) -> Set[str]:
        merged_set = set()

        for functions in args_functions:
            merged_set.update(functions)

        return merged_set

    @staticmethod
    def _is_string_node(node: Any) -> bool:
        if isinstance(node, ast.Constant) and isinstance(node.value, IAST.TEXT_TYPES):
            return True

        return False

    @staticmethod
    def _is_numeric_node(node: Any) -> bool:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return True

        return False

    @staticmethod
    def _get_function_name(call_node: ast.Call, is_function: bool) -> Text:
        if is_function:
            return call_node.func.id  # type: ignore[attr-defined]
        # If the call is to a method
        elif type(call_node.func) == ast.Name:
            return call_node.func.id

        return call_node.func.attr  # type: ignore[attr-defined]

    def _is_node_constant_or_binop(self, node: Any) -> bool:
        return self._is_string_node(node) or self._is_numeric_node(node) or isinstance(node, ast.BinOp)

    def _is_call_excluded(self, func_name_node: Text) -> bool:
        if not self.excluded_functions:
            return False
        excluded_for_caller = self.excluded_functions.get(func_name_node, tuple()) + self.excluded_functions.get(
            "", tuple()
        )
        return "" in excluded_for_caller or self._current_function_name in excluded_for_caller

    def _is_string_format_with_literals(self, call_node: ast.Call) -> bool:
        return (
            self._is_string_node(call_node.func.value)  # type: ignore[attr-defined]
            and call_node.func.attr == "format"  # type: ignore[attr-defined]
            and all(map(self._is_node_constant_or_binop, call_node.args))
            and all(map(lambda x: self._is_node_constant_or_binop(x.value), call_node.keywords))
        )

    def _should_replace_with_taint_sink(self, call_node: ast.Call, is_function: bool) -> bool:
        function_name = self._get_function_name(call_node, is_function)

        if function_name in self._taint_sink_replace_disabled:
            return False

        return function_name in self._taint_sink_replace_any

    def _should_replace_with_source(self, call_node: ast.Call, is_function: bool) -> bool:
        function_name = self._get_function_name(call_node, is_function)

        return function_name in self._source_replace_any

    def _add_original_function_as_arg(self, call_node: ast.Call, is_function: bool) -> Any:
        """
        Creates the arguments for the original function
        """
        function_name = self._get_function_name(call_node, is_function)
        function_name_arg = (
            self._name_node(call_node, function_name, ctx=ast.Load()) if is_function else copy.copy(call_node.func)
        )

        # Arguments for stack info change from:
        # my_function(self, *args, **kwargs)
        # to:
        # _add_original_function_as_arg(function_name=my_function, self, *args, **kwargs)
        new_args = [
            function_name_arg,
        ] + call_node.args

        return new_args

    @staticmethod
    def _node(type_: Any, pos_from_node: Any, **kwargs: Any) -> Any:
        """
        Abstract some basic differences in node structure between versions
        """

        # Some nodes (like Module) dont have position
        lineno = getattr(pos_from_node, "lineno", 1)
        col_offset = getattr(pos_from_node, "col_offset", 0)

        # Py38+
        end_lineno = getattr(pos_from_node, "end_lineno", 1)
        end_col_offset = getattr(pos_from_node, "end_col_offset", 0)

        return type_(
            lineno=lineno, end_lineno=end_lineno, col_offset=col_offset, end_col_offset=end_col_offset, **kwargs
        )

    def _name_node(self, from_node: Any, _id: Text, ctx: Any = ast.Load()) -> ast.Name:  # noqa: B008
        return self._node(
            ast.Name,
            from_node,
            id=_id,
            ctx=ctx,
        )

    def _attr_node(self, from_node: Any, attr: Text, ctx: Any = ast.Load()) -> ast.Name:  # noqa: B008
        attr_attr = ""
        name_attr = ""
        if attr:
            aspect_split = attr.split(".")
            if len(aspect_split) > 1:
                attr_attr = aspect_split[1]
                name_attr = aspect_split[0]

        name_node = self._name_node(from_node, name_attr, ctx=ctx)
        return self._node(ast.Attribute, from_node, attr=attr_attr, ctx=ctx, value=name_node)

    def _assign_node(self, from_node: Any, targets: List[Any], value: Any) -> Any:
        return self._node(
            ast.Assign,
            from_node,
            targets=targets,
            value=value,
            type_comment=None,
        )

    @staticmethod
    def find_insert_position(module_node: ast.Module) -> int:
        insert_position = 0
        from_future_import_found = False
        import_found = False

        # Check all nodes that are "from __future__ import...", as we must insert after them.
        #
        # Caveat:
        # - body_node.lineno doesn't work because a large docstring changes the lineno
        #   but not the position in the nodes (i.e. this can happen: lineno==52, position==2)
        # TODO: Test and implement cases with docstrings before future imports, etc.
        for body_node in module_node.body:
            insert_position += 1
            if isinstance(body_node, ImportFrom) and body_node.module == "__future__":
                import_found = True
                from_future_import_found = True
            # As soon as we start a non-futuristic import we can stop looking
            elif isinstance(body_node, ImportFrom):
                import_found = True
            elif isinstance(body_node, Expr) and not import_found:
                continue
            elif from_future_import_found:
                insert_position -= 1
                break
            else:
                break

        if not from_future_import_found:
            # No futuristic import found, reset the position to 0
            insert_position = 0

        return insert_position

    @staticmethod
    def _none_constant(from_node: Any) -> Any:  # noqa: B008
        # 3.8+
        return ast.Constant(
            lineno=from_node.lineno,
            col_offset=from_node.col_offset,
            end_lineno=from_node.end_lineno,
            end_col_offset=from_node.end_col_offset,
            value=None,
            kind=None,
        )

    @staticmethod
    def _int_constant(from_node, value):
        return ast.Constant(
            lineno=from_node.lineno,
            col_offset=from_node.col_offset,
            end_lineno=getattr(from_node, "end_lineno", from_node.lineno),
            end_col_offset=from_node.col_offset + 1,
            value=value,
            kind=None,
        )

    def _call_node(self, from_node: Any, func: Any, args: List[Any]) -> Any:
        return self._node(ast.Call, from_node, func=func, args=args, keywords=[])

    def visit_Module(self, module_node: ast.Module) -> Any:
        """
        Insert the import statement for the replacements module
        """
        insert_position = self.find_insert_position(module_node)

        definitions_module = _ASPECTS_SPEC["definitions_module"]
        replacements_import = self._node(
            ast.Import,
            module_node,
            names=[
                ast.alias(
                    lineno=1,
                    col_offset=0,
                    name=definitions_module,
                    asname=_ASPECTS_SPEC["alias_module"],
                )
            ],
        )
        module_node.body.insert(insert_position, replacements_import)

        definitions_module = self._sinkpoints_spec["definitions_module"]
        replacements_import = self._node(
            ast.Import,
            module_node,
            names=[
                ast.alias(
                    lineno=1,
                    col_offset=0,
                    name=definitions_module,
                    asname=self._sinkpoints_spec["alias_module"],
                )
            ],
        )
        module_node.body.insert(insert_position, replacements_import)

        definitions_module = self._source_spec["definitions_module"]
        replacements_import = self._node(
            ast.Import,
            module_node,
            names=[
                ast.alias(
                    lineno=1,
                    col_offset=0,
                    name=definitions_module,
                    asname=self._source_spec["alias_module"],
                )
            ],
        )
        module_node.body.insert(insert_position, replacements_import)
        # Must be called here instead of the start so the line offset is already
        # processed
        return self.generic_visit(module_node)

    def visit_FunctionDef(self, def_node: ast.FunctionDef) -> Any:
        """
        Special case for some tests which would enter in a patching
        loop otherwise when visiting the check functions
        """
        if f"{_PREFIX}dir" in def_node.name or f"{_PREFIX}set_dir_filter" in def_node.name:
            return def_node

        self.replacements_disabled_for_functiondef = def_node.name in self.dont_patch_these_functionsdefs

        if hasattr(def_node.args, "vararg") and def_node.args.vararg:
            if def_node.args.vararg.annotation:
                _mark_avoid_convert_recursively(def_node.args.vararg.annotation)

        if hasattr(def_node.args, "kwarg") and def_node.args.kwarg:
            if def_node.args.kwarg.annotation:
                _mark_avoid_convert_recursively(def_node.args.kwarg.annotation)

        if hasattr(def_node, "returns"):
            _mark_avoid_convert_recursively(def_node.returns)

        for i in def_node.args.args:
            if hasattr(i, "annotation"):
                _mark_avoid_convert_recursively(i.annotation)

        if hasattr(def_node.args, "kwonlyargs"):
            for i in def_node.args.kwonlyargs:
                if hasattr(i, "annotation"):
                    _mark_avoid_convert_recursively(i.annotation)

        if hasattr(def_node.args, "posonlyargs"):
            for i in def_node.args.posonlyargs:
                if hasattr(i, "annotation"):
                    _mark_avoid_convert_recursively(i.annotation)

        self.generic_visit(def_node)
        self._current_function_name = None

        return def_node

    def visit_Call(self, call_node: ast.Call) -> Any:
        """
        Replace a call or method
        """
        self.generic_visit(call_node)
        func_member = call_node.func
        call_modified = False
        if self.replacements_disabled_for_functiondef:
            return call_node

        if isinstance(func_member, ast.Name) and func_member.id:
            # Normal function call with func=Name(...), just change the name
            func_name_node = func_member.id
            aspect = self._aspect_functions.get(func_name_node)
            if aspect:
                # Send 0 as flag_added_args value
                call_node.args.insert(0, self._int_constant(call_node, 0))
                # Insert original function name as first parameter
                call_node.args = self._add_original_function_as_arg(call_node, True)
                # Substitute function call
                call_node.func = self._attr_node(call_node, aspect)
                self.ast_modified = call_modified = True

        # Call [attr] -> Attribute [value]-> Attribute [value]-> Attribute
        # a.b.c.method()
        # replaced_method(a.b.c)
        elif isinstance(func_member, ast.Attribute):
            # Method call:
            method_name = func_member.attr

            if self._is_call_excluded(method_name):
                # Early return if method is excluded
                return call_node

            if self._is_string_format_with_literals(call_node):
                return call_node

            # This resolve moduleparent.modulechild.name
            # TODO: use the better Hdiv method with a decorator
            func_value = getattr(func_member, "value", None)
            func_value_value = getattr(func_value, "value", None) if func_value else None
            func_value_value_id = getattr(func_value_value, "id", None) if func_value_value else None
            func_value_attr = getattr(func_value, "attr", None) if func_value else None
            func_attr = getattr(func_member, "attr", None)
            aspect = None
            is_module_symbol = False

            if func_value_value_id or func_attr:
                if func_value_value_id and func_value_attr:
                    # e.g. "os.path" or "one.two.three.whatever" (all dotted previous tokens with be in the id)
                    key = func_value_value_id + "." + func_value_attr
                elif func_value_attr:
                    # e.g os
                    key = func_attr
                else:
                    key = None

                if key:
                    module_dict = self._aspect_modules.get(key, None)
                    # using "is not None" here because we want to mark is_module_symbol even if the dict is
                    # empty (e.g. we don't have an aspect for this specific function but we plan to, or we create
                    # empty dicts for some modules to avoid checking for string methods on their symbols)
                    if module_dict is not None:
                        aspect = module_dict.get(func_attr, None)
                        # since this is a module symbol, even if we don't have an aspect for this specific function,
                        # set this, so we don't try to replace as a string method
                        is_module_symbol = True
                        if aspect:
                            # Create a new Name node for the replacement and set it as node.func
                            call_node.func = self._attr_node(call_node, aspect)
                            self.ast_modified = call_modified = True
                    else:
                        aspect = None

            if (not is_module_symbol) and (not aspect):
                # Not a module symbol, check if it's a known string method
                aspect = self._aspect_methods.get(method_name)

                if aspect:
                    # Move the Attribute.value to 'args'
                    new_arg = func_member.value
                    call_node.args.insert(0, new_arg)
                    # Send 1 as flag_added_args value
                    call_node.args.insert(0, self._int_constant(call_node, 1))

                    # Insert None as first parameter instead of a.b.c.method
                    # to avoid unexpected side effects such as a.b.read(4).method
                    call_node.args.insert(0, self._none_constant(call_node))

                    # Create a new Name node for the replacement and set it as node.func
                    call_node.func = self._attr_node(call_node, aspect)
                    self.ast_modified = call_modified = True
                else:
                    aspect = self._should_replace_with_source(call_node, False)
                    if aspect:
                        # Send 0 as flag_added_args value
                        call_node.args.insert(0, self._int_constant(call_node, 0))
                        call_node.args = self._add_original_function_as_arg(call_node, False)
                        call_node.func = self._attr_node(call_node, SOURCES_FUNCTION_REPLACEMENT)
                        self.ast_modified = call_modified = True

        if self.codetype == CODE_TYPE_FIRST_PARTY:
            # Function replacement case
            if isinstance(call_node.func, ast.Name):
                aspect = self._should_replace_with_taint_sink(call_node, True)
                if aspect:
                    # Send 0 as flag_added_args value
                    call_node.args.insert(0, self._int_constant(call_node, 0))
                    call_node.args = self._add_original_function_as_arg(call_node, False)
                    call_node.func = self._attr_node(call_node, TAINT_SINK_FUNCTION_REPLACEMENT)
                    self.ast_modified = call_modified = True

            # Method replacement case
            elif isinstance(call_node.func, ast.Attribute):
                aspect = self._should_replace_with_taint_sink(call_node, False)
                if aspect:
                    # Send 0 as flag_added_args value
                    call_node.args.insert(0, self._int_constant(call_node, 0))
                    # Create a new Name node for the replacement and set it as node.func
                    call_node.args = self._add_original_function_as_arg(call_node, False)
                    call_node.func = self._attr_node(call_node, TAINT_SINK_FUNCTION_REPLACEMENT)
                    self.ast_modified = call_modified = True

        if call_modified:
            _set_metric_iast_instrumented_propagation()

        return call_node

    def visit_BinOp(self, call_node: ast.BinOp) -> Any:
        """
        Replace a binary operator
        """
        self.generic_visit(call_node)
        operator = call_node.op

        aspect = self._aspect_operators.get(operator.__class__)
        if aspect:
            self.ast_modified = True
            _set_metric_iast_instrumented_propagation()

            return ast.Call(self._attr_node(call_node, aspect), [call_node.left, call_node.right], [])

        return call_node

    def visit_AugAssign(self, augassign_node: ast.AugAssign) -> Any:
        """
        Replace an inplace add or multiply (+= / *=)
        """
        self.generic_visit(augassign_node)

        if augassign_node.op.__class__ == ast.Add:
            # Optimization: ignore augassigns where the right side term is an integer since
            # they can't apply to strings
            if self._is_numeric_node(augassign_node.value):
                return augassign_node

            replacement_func = self._aspect_operators["INPLACE_ADD"]

            # Regular inplace add for non-subscript targets
            func_arg1 = copy.deepcopy(augassign_node.target)
            func_arg1.ctx = ast.Load()
            func_arg2 = copy.deepcopy(augassign_node.value)
            if hasattr(func_arg2, "ctx"):
                func_arg2.ctx = ast.Load()

            call_node = self._call_node(
                augassign_node,
                func=self._attr_node(augassign_node, replacement_func),
                args=[func_arg1, func_arg2],
            )

            self.ast_modified = True
            return self._node(
                ast.Assign,
                augassign_node,
                targets=[augassign_node.target],
                value=call_node,
                type_comment=None,
            )

        return augassign_node

    def visit_FormattedValue(self, fmt_value_node: ast.FormattedValue) -> Any:
        """
        Visit a FormattedValue node which are the constituent atoms for the
        JoinedStr which are used to implement f-strings.
        """

        self.generic_visit(fmt_value_node)

        if hasattr(fmt_value_node, "value") and self._is_node_constant_or_binop(fmt_value_node.value):
            return fmt_value_node

        func_name_node = self._attr_node(fmt_value_node, self._aspect_format_value)

        options_int = self._node(
            ast.Constant,
            fmt_value_node,
            value=fmt_value_node.conversion,
            kind=None,
        )

        format_spec = fmt_value_node.format_spec if fmt_value_node.format_spec else self._none_constant(fmt_value_node)
        call_node = self._call_node(
            fmt_value_node,
            func=func_name_node,
            args=[fmt_value_node.value, options_int, format_spec],
        )

        self.ast_modified = True
        _set_metric_iast_instrumented_propagation()
        return call_node

    def visit_JoinedStr(self, joinedstr_node: ast.JoinedStr) -> Any:
        """
        Replaced the JoinedStr AST node with a Call to the replacement function. Most of
        the work inside fstring is done by visit_FormattedValue above.
        """
        self.generic_visit(joinedstr_node)

        if all(
            map(
                lambda x: isinstance(x, ast.FormattedValue) or self._is_node_constant_or_binop(x),
                joinedstr_node.values,
            )
        ):
            return joinedstr_node

        func_name_node = self._attr_node(
            joinedstr_node,
            self._aspect_build_string,
            ctx=ast.Load(),
        )
        call_node = self._call_node(
            joinedstr_node,
            func=func_name_node,
            args=joinedstr_node.values,
        )

        self.ast_modified = True
        _set_metric_iast_instrumented_propagation()
        return call_node

    def visit_Assign(self, assign_node: ast.Assign) -> Any:
        """
        Add the ignore marks for left-side subscripts or list/tuples to avoid problems
        later with the visit_Subscript node.
        """
        if isinstance(assign_node.value, ast.Subscript):
            if hasattr(assign_node.value, "value") and hasattr(assign_node.value.value, "id"):
                # Best effort to avoid converting type definitions
                if assign_node.value.value.id in (
                    "Callable",
                    "Dict",
                    "Generator",
                    "List",
                    "Optional",
                    "Sequence",
                    "Tuple",
                    "Type",
                    "TypeVar",
                    "Union",
                ):
                    _mark_avoid_convert_recursively(assign_node.value)

        for target in assign_node.targets:
            if isinstance(target, ast.Subscript):
                # We can't assign to a function call, which is anyway going to rewrite
                # the index destination so we just ignore that target
                target.avoid_convert = True  # type: ignore[attr-defined]
            elif isinstance(target, (List, ast.Tuple)):
                # Same for lists/tuples on the left side of the assignment
                for element in target.elts:
                    if isinstance(element, ast.Subscript):
                        element.avoid_convert = True  # type: ignore[attr-defined]

            # Create a normal assignment. This way we decompose multiple assignments
        self.generic_visit(assign_node)
        return assign_node

    def visit_Delete(self, assign_node: ast.Delete) -> Any:
        # del replaced_index(foo, bar) would fail so avoid converting the right hand side
        # since it's going to be deleted anyway

        for target in assign_node.targets:
            if isinstance(target, ast.Subscript):
                target.avoid_convert = True  # type: ignore[attr-defined]

        self.generic_visit(assign_node)
        return assign_node

    def visit_AnnAssign(self, node: ast.AnnAssign) -> Any:
        # AnnAssign is a type annotation, we don't need to convert it
        # and we avoid converting any subscript inside it.
        _mark_avoid_convert_recursively(node)
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        for i in node.bases:
            _mark_avoid_convert_recursively(i)

        self.generic_visit(node)
        return node

    def visit_Subscript(self, subscr_node: ast.Subscript) -> Any:
        """
        Turn an indexes[1] and slices[0:1:2] into the replacement function call
        Optimization: dont convert if the indexes are strings
        """
        self.generic_visit(subscr_node)

        # We mark nodes to avoid_convert (check visit_Delete, visit_AugAssign, visit_Assign) due to complex
        # expressions that raise errors when try to replace with index aspects
        if hasattr(subscr_node, "avoid_convert"):
            return subscr_node

        # We only want to convert subscript nodes that are being used as a load.
        # That means, no Delete or Store contexts.
        if not isinstance(subscr_node.ctx, ast.Load):
            return subscr_node

        # Optimization: String literal slices and indexes are not patched
        if self._is_string_node(subscr_node.value):
            return subscr_node

        attr_node = self._attr_node(subscr_node, "")

        call_node = self._call_node(
            subscr_node,
            func=attr_node,
            args=[],
        )
        if isinstance(subscr_node.slice, ast.Slice):
            # Slice[0:1:2]. The other cases in this if are Indexes[0]
            aspect_split = self._aspect_slice.split(".")
            call_node.func.attr = aspect_split[1]
            call_node.func.value.id = aspect_split[0]
            none_node = self._none_constant(subscr_node)
            lower = none_node if subscr_node.slice.lower is None else subscr_node.slice.lower
            upper = none_node if subscr_node.slice.upper is None else subscr_node.slice.upper
            step = none_node if subscr_node.slice.step is None else subscr_node.slice.step
            call_node.args.extend([subscr_node.value, lower, upper, step])
            self.ast_modified = True
        elif PY39_PLUS:
            if self._is_string_node(subscr_node.slice):
                return subscr_node
            # In Py39+ the if subscr_node.slice member is not a Slice, is directly an unwrapped value
            # for the index (e.g. Constant for a number, Name for a var, etc)
            aspect_split = self._aspect_index.split(".")
            call_node.func.attr = aspect_split[1]
            call_node.func.value.id = aspect_split[0]
            call_node.args.extend([subscr_node.value, subscr_node.slice])
        # TODO: python 3.8 isn't working correctly with index_aspect, tests raise:
        #  corrupted size vs. prev_size in fastbins
        #  Test failed with exit code -6
        #  https://app.circleci.com/pipelines/github/DataDog/dd-trace-py/46665/workflows/3cf1257c-feaf-4653-bb9c-fb840baa1776/jobs/3031799
        # elif isinstance(subscr_node.slice, ast.Index):
        #     if self._is_string_node(subscr_node.slice.value):  # type: ignore[attr-defined]
        #         return subscr_node
        #     aspect_split = self._aspect_index.split(".")
        #     call_node.func.attr = aspect_split[1]
        #     call_node.func.value.id = aspect_split[0]
        #     call_node.args.extend([subscr_node.value, subscr_node.slice.value])  # type: ignore[attr-defined]
        else:
            return subscr_node

        self.ast_modified = True
        return call_node
