"""The class implementation for the `cell_wifi` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialCellWifiIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `cell_wifi` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><rect fill="none" height="24" width="24"/><path d="M18,9.98L6,22h12h4V5.97L18,9.98z M20,20h-2v-7.22l2-2V20z M5.22,7.22L3.93,5.93c3.9-3.91,10.24-3.91,14.15,0l-1.29,1.29 C13.6,4.03,8.41,4.03,5.22,7.22z M12.93,11.07L11,13l-1.93-1.93C10.14,10.01,11.86,10.01,12.93,11.07z M14.22,9.79 c-1.78-1.77-4.66-1.77-6.43,0L6.5,8.5c2.48-2.48,6.52-2.48,9,0L14.22,9.79z"/></svg>'  # noqa
