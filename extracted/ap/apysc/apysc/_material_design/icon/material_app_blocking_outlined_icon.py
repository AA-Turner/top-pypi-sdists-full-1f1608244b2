"""The class implementation for the outlined `app_blocking` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialAppBlockingOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `app_blocking` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><g><path d="M18,8c-2.21,0-4,1.79-4,4c0,2.21,1.79,4,4,4s4-1.79,4-4C22,9.79,20.21,8,18,8z M15.5,12c0-1.38,1.12-2.5,2.5-2.5 c0.42,0,0.8,0.11,1.15,0.29l-3.36,3.36C15.61,12.8,15.5,12.42,15.5,12z M18,14.5c-0.42,0-0.8-0.11-1.15-0.29l3.36-3.36 c0.18,0.35,0.29,0.73,0.29,1.15C20.5,13.38,19.38,14.5,18,14.5z"/><path d="M17,18H7V6h10v1h2V6V5V3c0-1.1-0.9-2-2-2H7C5.9,1,5,1.9,5,3v18c0,1.1,0.9,2,2,2h10c1.1,0,2-0.9,2-2v-2v-1v-1h-2V18z M7,3 h10v1H7V3z M17,21H7v-1h10V21z"/></g></g></svg>'  # noqa
