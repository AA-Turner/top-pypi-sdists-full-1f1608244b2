"""The class implementation for the outlined `hearing_disabled` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialHearingDisabledOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `hearing_disabled` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><path d="M6.03,3.2C7.15,2.44,8.51,2,10,2c3.93,0,7,3.07,7,7c0,1.26-0.38,2.65-1.07,3.9c-0.02,0.04-0.05,0.08-0.08,0.13l-1.48-1.48 C14.77,10.69,15,9.8,15,9c0-2.8-2.2-5-5-5C9.08,4,8.24,4.26,7.5,4.67L6.03,3.2z M17.21,14.38l1.43,1.43C20.11,13.93,21,11.57,21,9 c0-3.04-1.23-5.79-3.22-7.78l-1.42,1.42C17.99,4.26,19,6.51,19,9C19,11.02,18.33,12.88,17.21,14.38z M10,6.5 c-0.21,0-0.4,0.03-0.59,0.08l3.01,3.01C12.47,9.4,12.5,9.21,12.5,9C12.5,7.62,11.38,6.5,10,6.5z M21.19,21.19L2.81,2.81L1.39,4.22 l2.13,2.13C3.19,7.16,3,8.05,3,9h2c0-0.36,0.05-0.71,0.12-1.05l6.61,6.61c-0.88,0.68-1.78,1.41-2.27,2.9c-0.5,1.5-1,2.01-1.71,2.38 C7.56,19.94,7.29,20,7,20c-1.1,0-2-0.9-2-2H3c0,2.21,1.79,4,4,4c0.57,0,1.13-0.12,1.64-0.35c1.36-0.71,2.13-1.73,2.73-3.55 c0.32-0.98,0.9-1.43,1.71-2.05c0.03-0.02,0.05-0.04,0.08-0.06l6.62,6.62L21.19,21.19z"/></g></svg>'  # noqa
