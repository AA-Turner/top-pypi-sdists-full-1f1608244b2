"""The class implementation for the outlined `video_settings` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialVideoSettingsOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `video_settings` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><path d="M3,6h18v5h2V6c0-1.1-0.9-2-2-2H3C1.9,4,1,4.9,1,6v12c0,1.1,0.9,2,2,2h9v-2H3V6z"/><polygon points="15,12 9,8 9,16"/><path d="M22.71,18.43c0.03-0.29,0.04-0.58,0.01-0.86l1.07-0.85c0.1-0.08,0.12-0.21,0.06-0.32l-1.03-1.79 c-0.06-0.11-0.19-0.15-0.31-0.11L21.23,15c-0.23-0.17-0.48-0.31-0.75-0.42l-0.2-1.36C20.26,13.09,20.16,13,20.03,13h-2.07 c-0.12,0-0.23,0.09-0.25,0.21l-0.2,1.36c-0.26,0.11-0.51,0.26-0.74,0.42l-1.28-0.5c-0.12-0.05-0.25,0-0.31,0.11l-1.03,1.79 c-0.06,0.11-0.04,0.24,0.06,0.32l1.07,0.86c-0.03,0.29-0.04,0.58-0.01,0.86l-1.07,0.85c-0.1,0.08-0.12,0.21-0.06,0.32l1.03,1.79 c0.06,0.11,0.19,0.15,0.31,0.11l1.27-0.5c0.23,0.17,0.48,0.31,0.75,0.42l0.2,1.36c0.02,0.12,0.12,0.21,0.25,0.21h2.07 c0.12,0,0.23-0.09,0.25-0.21l0.2-1.36c0.26-0.11,0.51-0.26,0.74-0.42l1.28,0.5c0.12,0.05,0.25,0,0.31-0.11l1.03-1.79 c0.06-0.11,0.04-0.24-0.06-0.32L22.71,18.43z M19,19.5c-0.83,0-1.5-0.67-1.5-1.5s0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5 S19.83,19.5,19,19.5z"/></g></g></svg>'  # noqa
