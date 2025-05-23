"""Video extension to embed video in a html sphinx output."""

import urllib.parse
from pathlib import Path
from typing import Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, SphinxTranslator
from sphinx.writers.html import HTMLTranslator

__author__ = "Raphael Massabot"
__version__ = "0.2.1"

logger = logging.getLogger(__name__)

SUPPORTED_MIME_TYPES: Dict[str, str] = {
    ".mp4": "video/mp4",
    ".ogm": "video/ogg",
    ".ogv": "video/ogg",
    ".ogg": "video/ogg",
    ".webm": "video/webm",
}
"Supported mime types of the link tag"

SUPPORTED_OPTIONS: List[str] = [
    "autoplay",
    "controls",
    "height",
    "loop",
    "muted",
    "poster",
    "preload",
    "width",
    "playsinline",
    "controlslist",
]
"List of the supported options attributes"


def get_video(src: str, env: BuildEnvironment) -> Tuple[str, str, bool]:
    """Return video and suffix.

    Load the video to the static directory if necessary and process the suffix. Raise a warning if not supported but do not stop the computation.

    Args:
        src: The source of the video file (can be local or url)
        env: the build environment

    Returns:
        The src file, the extension suffix, whether the file is remote
    """
    suffix = Path(src).suffix
    if suffix not in SUPPORTED_MIME_TYPES:
        logger.warning(
            f'The provided file type ("{suffix}") is not a supported format. defaulting to ""'
        )
    type = SUPPORTED_MIME_TYPES.get(suffix, "")

    is_remote = bool(urllib.parse.urlparse(src).netloc)
    if not is_remote:
        # Map video paths to unique names (so that they can be put into a single
        # directory). This copies what is done for images by the process_docs method of
        # sphinx.environment.collectors.asset.ImageCollector.
        src, fullpath = env.relfn2path(src, env.docname)
        env.note_dependency(fullpath)
        env.images.add_file(env.docname, src)

    return (src, type, is_remote)


class video_node(nodes.General, nodes.Element):
    """Video node."""

    pass


class Video(SphinxDirective):
    """Video directive.

    Wrapper for the html <video> tag embeding all the supported options
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    option_spec = {
        "alt": directives.unchanged,
        "autoplay": directives.flag,
        "nocontrols": directives.flag,
        "controlslist": directives.unchanged,
        "height": directives.unchanged,
        "loop": directives.flag,
        "muted": directives.flag,
        "poster": directives.unchanged,
        "preload": directives.unchanged,
        "width": directives.unchanged,
        "class": directives.unchanged,
        "playsinline": directives.flag,
        "align": directives.unchanged,
        "caption": directives.unchanged,
        "figwidth": directives.unchanged,
    }

    def run(self) -> List[video_node]:
        """Return the video node based on the set options."""
        env: BuildEnvironment = self.env

        # check options that need to be specific values

        width: str = self.options.get("width", "")
        if width and not (width.isdigit() or str_is_percentage(width)):
            logger.warning(
                f'The provided width ("{width}") is ignored as it\'s not an integer '
                "or integer percentage"
            )
            width = ""

        height: str = self.options.get("height", "")
        if height:
            if width.endswith("%"):
                logger.warning(
                    f'The provided height ("{height}") is ignored as the provided '
                    f'width ("{width}") is relative'
                )
                height = ""
            elif not height.isdigit():
                logger.warning(
                    f'The provided height ("{height}") is ignored as it\'s not an '
                    "integer"
                )
                height = ""

        preload: str = self.options.get("preload", "auto")
        valid_preload = ["auto", "metadata", "none"]
        if preload not in valid_preload:
            logger.warning(
                f'The provided preload ("{preload}") is not an accepted value. defaulting to "auto"'
            )
            preload = "auto"

        controlslist: str = self.options.get("controlslist", "")
        if controlslist:
            controlslist_set = set(controlslist.split(","))
            valid_token = ["nodownload", "nofullscreen", "noremoteplayback"]
            if not controlslist_set.issubset(valid_token):
                logger.warning(
                    f"The controlslist can only contains value from: {valid_token}"
                )
                controlslist_set = set()
            controlslist = " ".join(controlslist_set)

        align: str = self.options.get("align", "left")
        if align not in ["left", "center", "right", "default"]:
            logger.warning(
                f'The align type ("{align}") is not a supported. defaulting to "left"'
            )
            align = "left"

        caption: str = self.options.get("caption", "")
        figwidth: str = self.options.get("figwidth", "")
        if not caption:
            figwidth = ""

        # add the primary video files as images in the builder
        sources = [get_video(self.arguments[0], env)]

        # add the secondary video files as images in the builder if necessary
        if len(self.arguments) == 2:
            sources.append(get_video(self.arguments[1], env))
        elif env.config.video_enforce_extra_source is True:
            logger.warning(
                f'A secondary source should be provided for "{self.arguments[0]}"'
            )

        return [
            video_node(
                sources=sources,
                alt=self.options.get("alt", ""),
                autoplay="autoplay" in self.options,
                controls="nocontrols" not in self.options,
                controlslist=controlslist,
                height=height,
                loop="loop" in self.options,
                muted="muted" in self.options,
                poster=self.options.get("poster", ""),
                preload=preload,
                width=width,
                klass=self.options.get("class", ""),
                playsinline="playsinline" in self.options,
                align=align,
                caption=caption,
                figwidth=figwidth,
            )
        ]


def str_is_percentage(string: str) -> bool:
    """Check if the string represent a valid percentage value."""
    return string[-1] == "%" and str_is_float(string[0:-1])


def str_is_float(string: str) -> bool:
    """Check if the string represent a valid float value."""
    try:
        float(string)
        return True
    except ValueError:
        return False


class VideoPostTransform(SphinxPostTransform):
    """Ensure video files are copied to build directory.

    This copies what is done for images in the post_process_image method of
    sphinx.builders.Builder, except as a Transform since we can't hook into that method
    directly.
    """

    default_priority = 200

    def run(self):
        """Add video files to Builder's image tracking.

        Doing so ensures that the builder copies the files to the output directory.
        """
        # TODO: This check can be removed when the minimum supported docutils version
        # is docutils>=0.18.1.
        traverse_or_findall = (
            self.document.findall
            if hasattr(self.document, "findall")
            else self.document.traverse
        )
        for node in traverse_or_findall(video_node):
            for src, _, is_remote in node["sources"]:
                if not is_remote:
                    self.app.builder.images[src] = self.env.images[src][1]


def visit_video_node_html(translator: HTMLTranslator, node: video_node) -> None:
    """Entry point of the html video node."""
    html: str = ""
    # has caption?
    if node["caption"]:
        html += "<figure "
    else:
        html += "<div "
    # align
    html += f' class="sphinx-contrib-video-container align-{node["align"]}"'
    # figwidth
    if node["figwidth"]:
        html += f' style="width: {node["figwidth"]}"><div class="align-center">'
    else:
        html += ">"
    # start the video block
    attr: List[str] = [f'{k}="{node[k]}"' for k in SUPPORTED_OPTIONS if node[k]]
    if node["klass"]:  # klass need to be special cased
        attr += [f"class=\"{node['klass']}\""]
    html += f"<video {' '.join(attr)}>"

    # build the sources
    builder = translator.builder
    html_source = '<source src="{}" type="{}">'
    for src, type_, _ in node["sources"]:
        # Rewrite the URI if the environment knows about it, as is done for images in the
        # HTML5 builder, in sphinx.writers.html5.HTML5Translator.visit_image.
        if src in builder.images:
            src = Path(
                builder.imgpath, urllib.parse.quote(builder.images[src])
            ).as_posix()
        html += html_source.format(src, type_)

    # add the alternative message
    html += node["alt"]

    translator.body.append(html)


def depart_video_node_html(translator: HTMLTranslator, node: video_node) -> None:
    """Exit of the html video node."""
    html_caption: str = ""
    if node["figwidth"]:
        html_caption += "</div>"
    if node["caption"]:
        html_caption += (
            '<figcaption class="align-center">'
            '<p style="text-align: left; display:inline-block">'
            f'<span class="caption-text">{node["caption"]}</span>'
            "</p></figcaption></figure>"
        )
    else:
        html_caption += "</div>"
    translator.body.append(f"</video>{html_caption}")


def visit_video_node_unsuported(translator: SphinxTranslator, node: video_node) -> None:
    """Entry point of the ignored video node."""
    logger.warning(
        f"video {node['sources'][0][0]}: unsupported output format (node skipped)"
    )
    raise nodes.SkipNode


def setup(app: Sphinx) -> Dict[str, bool]:
    """Add video node and parameters to the Sphinx builder."""
    app.add_config_value("video_enforce_extra_source", False, "html")
    app.add_node(
        video_node,
        html=(visit_video_node_html, depart_video_node_html),
        epub=(visit_video_node_unsuported, None),
        latex=(visit_video_node_unsuported, None),
        man=(visit_video_node_unsuported, None),
        texinfo=(visit_video_node_unsuported, None),
        text=(visit_video_node_unsuported, None),
    )
    app.add_directive("video", Video)
    app.add_post_transform(VideoPostTransform)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
