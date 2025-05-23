"""The class implementation for the outlined `surround_sound` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialSurroundSoundOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `surround_sound` material icon.
    """

    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.

        References
        ----------
        - Material icon document
            - https://simon-ritchie.github.io/apysc/en/material_icon.html
        - Material Symbols & Icons, APACHE LICENSE, VERSION 2.0
            - https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed
            - https://www.apache.org/licenses/LICENSE-2.0.html
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><rect fill="none" height="24" width="24"/><rect fill="none" height="24" width="24"/></g><g><g/><g><path d="M20,4H4C2.9,4,2,4.9,2,6v12c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V6C22,4.9,21.1,4,20,4z M20,18H4V6h16V18z"/><path d="M8.29,15.71C7.27,14.69,6.75,13.35,6.75,12c0-1.35,0.52-2.69,1.53-3.72L7.05,7.05C5.68,8.41,5,10.21,5,12 s0.68,3.59,2.06,4.94L8.29,15.71z"/><path d="M12,15.5c1.93,0,3.5-1.57,3.5-3.5c0-1.93-1.57-3.5-3.5-3.5c-1.93,0-3.5,1.57-3.5,3.5C8.5,13.93,10.07,15.5,12,15.5z M12,10.5c0.83,0,1.5,0.67,1.5,1.5s-0.67,1.5-1.5,1.5s-1.5-0.67-1.5-1.5S11.17,10.5,12,10.5z"/><path d="M15.72,15.72l1.23,1.23C18.32,15.59,19,13.79,19,12s-0.68-3.59-2.06-4.94l-1.23,1.23c1.02,1.02,1.54,2.36,1.54,3.71 C17.25,13.35,16.73,14.69,15.72,15.72z"/></g></g></svg>'  # noqa
