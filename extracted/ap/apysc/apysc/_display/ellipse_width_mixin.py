"""Class implementation for the ellipse width mix-in.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class EllipseWidthMixIn(
    RevertMixIn,
    AttrLinkingMixIn,
):
    _ellipse_width: Int

    @final
    def _initialize_ellipse_width_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_width attribute if this interface
        does not initialize it yet.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if hasattr(self, "_ellipse_width"):
            return
        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="ellipse_width",
        )
        self._ellipse_width = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_ellipse_width_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ellipse_width_attr_linking_setting(self) -> None:
        """
        Append an ellipse-height attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._ellipse_width, attr_name="ellipse_width"
        )
        self._append_attr_to_linking_stack(
            attr=self._ellipse_width, attr_name="ellipse_width"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def ellipse_width(self) -> Int:
        """
        Get ellipse width value.

        Returns
        -------
        ellipse_width : Int
            Ellipse width value.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.ellipse_width = ap.Int(10)
        >>> rectangle.ellipse_height = ap.Int(15)
        >>> rectangle.ellipse_width
        Int(10)
        """
        from apysc._type import value_util

        self._initialize_ellipse_width_if_not_initialized()
        return value_util.get_copy(value=self._ellipse_width)

    @ellipse_width.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def ellipse_width(self, value: Int) -> None:
        """
        Update ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        self._ellipse_width = value
        self._ellipse_width._append_incremental_calc_substitution_expression()
        self._append_ellipse_width_update_expression()

        self._append_ellipse_width_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ellipse_width_update_expression(self) -> None:
        """
        Append ellipse width updating expression.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self._initialize_ellipse_width_if_not_initialized()
        width_value_str: str = value_util.get_value_str_for_expression(
            value=self._ellipse_width
        )
        if hasattr(self, "_ellipse_height"):
            height_value_str: str = value_util.get_value_str_for_expression(
                value=getattr(self, "_ellipse_height")
            )
        else:
            height_value_str = value_util.get_value_str_for_expression(value=0)
        self_instance: VariableNameMixIn = validate_variable_name_mixin_type(
            instance=self
        )
        expression: str = (
            f"{self_instance.variable_name}.radius({width_value_str}, "
            f"{height_value_str});"
        )
        expression_data_util.append_js_expression(expression=expression)

    _ellipse_width_snapshots: Optional[Dict[str, int]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ellipse_width_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_ellipse_width_snapshots",
            value=int(self._ellipse_width._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._ellipse_width._value = self._get_snapshot_val_if_exists(
            current_value=self._ellipse_width._value,
            snapshot_dict=self._ellipse_width_snapshots,
            snapshot_name=snapshot_name,
        )
