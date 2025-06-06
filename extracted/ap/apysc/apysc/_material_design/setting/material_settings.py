"""The static class implementation for the material design settings.
"""

from typing import List
from typing import Optional
from typing import Union

from apysc._converter.list_of_strs_to_array import list_of_strs_to_array_of_string
from apysc._material_design.color.material_brightness import MaterialBrightness
from apysc._material_design.color.material_color_scheme import MaterialColorScheme
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.string import String


class MaterialSettings:

    @classmethod
    def _reset_settings(cls) -> None:
        """
        Reset all settings of this class.
        """
        cls._delete_current_brightness_string_attr()
        cls._light_color_scheme = None
        cls._dark_color_scheme = None
        if hasattr(cls, "_light_color_scheme_str"):
            del cls._light_color_scheme_str
        if hasattr(cls, "_dark_color_scheme_str"):
            del cls._dark_color_scheme_str
        if hasattr(cls, "_color_scheme_setting_is_enabled"):
            del cls._color_scheme_setting_is_enabled
        cls._font_family = None

    _light_color_scheme: Optional[MaterialColorScheme] = None

    @classmethod
    def _initialize_attrs(cls) -> None:
        """
        Initialize each attribute if it has not been initialized yet.
        """
        cls._initialize_current_brightness_string_if_not_initialized()
        if not hasattr(cls, "_light_color_scheme_str"):
            cls._light_color_scheme_str = String(
                value=MaterialBrightness.LIGHT.value,
                variable_name_suffix="light_color_scheme_str",
            )
        if not hasattr(cls, "_dark_color_scheme_str"):
            cls._dark_color_scheme_str = String(
                value=MaterialBrightness.DARK.value,
                variable_name_suffix="dark_color_scheme_str",
            )
        cls._initialize_color_scheme_setting_is_enabled_if_not_initialized()

    @classmethod
    def get_light_color_scheme(cls) -> Optional[MaterialColorScheme]:
        """
        Get a light color scheme setting.

        Returns
        -------
        color_scheme : MaterialColorScheme or None
            A light color scheme setting. If the color scheme is not set,
            this property becomes None.
        """
        cls._initialize_attrs()
        return cls._light_color_scheme

    @classmethod
    def set_light_color_scheme(cls, *, color_scheme: MaterialColorScheme) -> None:
        """
        Set a color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme
            Color scheme to set.

        Raises
        ------
        ValueError
            If you call this class method multiple times.
        """
        cls._initialize_attrs()
        cls._enable_color_scheme_setting()
        if cls._light_color_scheme is not None:
            raise ValueError(
                "The `set_light_color_scheme` class method can only be called once."
            )
        cls._light_color_scheme = color_scheme

    _dark_color_scheme: Optional[MaterialColorScheme] = None

    @classmethod
    def get_dark_color_scheme(cls) -> Optional[MaterialColorScheme]:
        """
        Get a dark color scheme setting.

        Returns
        -------
        color_scheme : MaterialColorScheme or None
            A dark color scheme setting. If the color scheme is not set,
            this property becomes None.
        """
        cls._initialize_attrs()
        return cls._dark_color_scheme

    @classmethod
    def set_dark_color_scheme(cls, *, color_scheme: MaterialColorScheme) -> None:
        """
        Set a dark color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme
            Color scheme to set.

        Raises
        ------
        ValueError
            If you call this class method multiple times.
        """
        cls._initialize_attrs()
        cls._enable_color_scheme_setting()
        if cls._dark_color_scheme is not None:
            raise ValueError(
                "The `set_dark_color_scheme` class method can only be called once."
            )
        cls._dark_color_scheme = color_scheme

    _current_brightness_string: String

    @classmethod
    def _initialize_current_brightness_string_if_not_initialized(cls) -> None:
        """
        Initialize the `_current_brightness_string` attribute string
        if it has not been initialized yet.
        """
        if hasattr(cls, "_current_brightness_string"):
            return
        cls._current_brightness_string = String(
            value=MaterialBrightness.LIGHT.value,
            variable_name_suffix="current_brightness_string",
        )

    @classmethod
    def _delete_current_brightness_string_attr(cls) -> None:
        """
        Delete the `_current_brightness_string` attribute.
        """
        if hasattr(cls, "_current_brightness_string"):
            del cls._current_brightness_string

    @classmethod
    def switch_to_light_color_scheme(cls) -> None:
        """
        Switch the current color scheme to the light color scheme.
        """
        cls._initialize_attrs()
        cls._current_brightness_string.value = MaterialBrightness.LIGHT.value

    @classmethod
    def switch_to_dark_color_scheme(cls) -> None:
        """
        Switch the current color scheme to the dark color scheme.
        """
        cls._initialize_attrs()
        cls._current_brightness_string.value = MaterialBrightness.DARK.value

    _light_color_scheme_str: String

    @classmethod
    def current_color_scheme_is_light_color_scheme(cls) -> Boolean:
        """
        Get whether the current color scheme is the light color scheme or not.

        Returns
        -------
        result : Boolean
            If the current color scheme is the light color scheme, then
            this method returns True.
        """
        cls._initialize_attrs()
        return cls._current_brightness_string == cls._light_color_scheme_str

    _dark_color_scheme_str: String

    @classmethod
    def current_color_scheme_is_dark_color_scheme(cls) -> Boolean:
        """
        Get a boolean whether the current color scheme
        is the dark color scheme or not.

        Returns
        -------
        result : Boolean
            If the current color scheme is the dark color scheme, then
            this method returns True.
        """
        cls._initialize_attrs()
        return cls._current_brightness_string == cls._dark_color_scheme_str

    _color_scheme_setting_is_enabled: Boolean

    @classmethod
    def _initialize_color_scheme_setting_is_enabled_if_not_initialized(cls) -> None:
        """
        Initialize the `_color_scheme_setting_is_enabled` attribute if it has
        not been initialized yet.
        """
        if hasattr(cls, "_color_scheme_setting_is_enabled"):
            return
        cls._color_scheme_setting_is_enabled = Boolean(
            False, variable_name_suffix="color_scheme_setting_is_enabled"
        )

    @classmethod
    def _enable_color_scheme_setting(cls) -> None:
        """
        Enable the color scheme setting.
        """
        cls._initialize_attrs()
        if cls._color_scheme_setting_is_enabled._value:
            return
        cls._color_scheme_setting_is_enabled.value = True
        cls._color_scheme_setting_is_enabled.disable_value_modification()

    @classmethod
    def color_scheme_setting_is_enabled(cls) -> Boolean:
        """
        Get a boolean whether the color scheme setting is enabled or not.

        Returns
        -------
        result : Boolean
            If the color scheme setting is enabled, then this method
            returns True.
        """
        cls._initialize_attrs()
        return cls._color_scheme_setting_is_enabled

    _font_family: Optional[Array[String]] = None

    @classmethod
    def set_font_family(cls, *, font_family: Union[Array[String], List[str]]) -> None:
        """
        Set a font-family setting.

        Parameters
        ----------
        font_family : Union[Array[String], List[str]]
            A font-family setting.
        """
        cls._initialize_attrs()
        font_family_: Optional[Array[String]] = list_of_strs_to_array_of_string(
            optional_list_or_arr=font_family
        )
        cls._font_family = font_family_

    @classmethod
    def get_font_family(cls) -> Optional[Array[String]]:
        """
        Get a font-family setting.

        Returns
        -------
        font_family : Array[String] or None
            A font-family setting.
        """
        cls._initialize_attrs()
        if cls._font_family is None:
            return None
        return cls._font_family.copy()
