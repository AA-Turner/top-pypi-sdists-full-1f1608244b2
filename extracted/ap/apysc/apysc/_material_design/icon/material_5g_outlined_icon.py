"""The class implementation for the outlined `5g` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class Material5GOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `5g` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><path d="M16.5,13H19v2h-5V9h7c0-1.1-0.9-2-2-2h-5c-1.1,0-2,0.9-2,2v6c0,1.1,0.9,2,2,2h5c1.1,0,2-0.9,2-2v-4h-4.5V13z"/><path d="M3,13h5v2H3v2h5c1.1,0,2-0.9,2-2v-2c0-1.1-0.9-2-2-2H5V9h5V7H3V13z"/></g></g></svg>'  # noqa
