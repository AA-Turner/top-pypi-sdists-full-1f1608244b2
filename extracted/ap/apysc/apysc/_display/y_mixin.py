"""Class implementation for the y-coordinate mix-in.
"""

from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._animation.animation_move_mixin import AnimationMoveMixIn
from apysc._animation.animation_y_mixin import AnimationYMixIn
from apysc._display.y_interface import YInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._validation import arg_validation_decos


class YMixIn(
    YInterface,
    AnimationYMixIn,
    AnimationMoveMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if hasattr(self, "_y"):
            return
        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="y",
        )
        self._y = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_attr_linking_setting(self) -> None:
        """
        Append a y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._y, attr_name="y")
        self._append_attr_to_linking_stack(attr=self._y, attr_name="y")

    @property
    @add_debug_info_setting(module_name=__name__)
    def y(self) -> Number:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Number
            Y-coordinate.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.y = ap.Number(100)
        >>> rectangle.y
        Number(100.0)
        """
        from apysc._type import value_util

        self._initialize_y_if_not_initialized()
        y: Number = value_util.get_copy(value=self._y)
        return y

    @y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def y(self, value: Number) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Number
            Y-coordinate value.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa
        """
        self._initialize_y_if_not_initialized()
        self._y = value
        self._y._append_incremental_calc_substitution_expression()
        self._append_y_update_expression()

        self._append_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        self._initialize_y_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(value=self._y)
        expression: str = f"{self.variable_name}.y({value_str});"
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _update_y_and_skip_appending_exp(self, *, y: Union[float, Number]) -> None:
        """
        Update y-coordinate and skip appending an expression.

        Parameters
        ----------
        y : float or Number
            Y-coordinate value.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if isinstance(y, Number):
            y_: Number = y
        else:
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="y",
            )
            y_ = Number(y, variable_name_suffix=suffix)
        self._y = y_

    _y_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_y_snapshots",
            value=float(self._y._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._y._value = self._get_snapshot_val_if_exists(
            current_value=self._y._value,
            snapshot_dict=self._y_snapshots,
            snapshot_name=snapshot_name,
        )
