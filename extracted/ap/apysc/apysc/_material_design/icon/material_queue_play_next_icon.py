"""The class implementation for the `queue_play_next` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialQueuePlayNextIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `queue_play_next` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24" x="0"/></g><g><g><g><path d="M21,3H3C1.89,3,1,3.89,1,5v12c0,1.1,0.89,2,2,2h5v2h8v-2h2v-2H3V5h18v8h2V5C23,3.89,22.1,3,21,3z M13,10V7h-2v3H8v2h3v3 h2v-3h3v-2H13z M24,18l-4.5,4.5L18,21l3-3l-3-3l1.5-1.5L24,18z"/></g></g></g></svg>'  # noqa
