import dataclasses
import difflib
import logging
from enum import Enum
from io import StringIO
from pathlib import Path
from typing import Optional, Union

import fastapi
import fastapi.staticfiles
import fastapi.templating
import uvicorn

from rhoknp import Document
from rhoknp.cli.show import draw_tree
from rhoknp.processors import KNP, KWJA, Jumanpp

logger = logging.getLogger(__name__)

here = Path(__file__).parent


class AnalyzerType(Enum):
    """解析器の種類．"""

    JUMANPP = "jumanpp"
    KNP = "knp"
    KWJA = "kwja"


@dataclasses.dataclass
class _Span:
    text: str
    label: Optional[str] = None


class _HTTPExceptionForIndex(fastapi.HTTPException):
    pass


class _HTTPExceptionForAnalyze(fastapi.HTTPException):
    pass


def _get_string_diff(pre_text: str, post_text: str) -> list[_Span]:
    """編集前後の文字列の差分を取得．

    Args:
        pre_text: 前の文字列．
        post_text: 後の文字列．

    Returns:
        差分．
    """
    spans = []
    span = _Span("", label="=")
    for diff in difflib.ndiff(pre_text, post_text):
        tag, character = diff[0], diff[2:]
        if tag == " ":
            tag = "="
        if tag == span.label:
            span.text += character
        else:
            if span.text:
                spans.append(span)
            span = _Span(character, tag)
    spans.append(span)
    return spans


def _draw_tree(document: Document, show_rel: bool = False, show_pas: bool = False) -> str:
    """rhoknp.cli.show.draw_tree の wrapper．

    Args:
        document: 解析結果．
        show_rel: True なら <rel> タグの内容を表示．
        show_pas: True なら述語項構造を表示．

    Returns:
        構文木．
    """
    with StringIO() as buffer:
        for sentence in document.sentences:
            draw_tree(sentence.base_phrases, buffer, show_rel=show_rel, show_pas=show_pas)
        return buffer.getvalue()


def _get_entity_spans(document: Document) -> list[_Span]:
    """文書をスパンに分割．

    Args:
        document: 解析結果．

    Returns:
        スパンのリスト．
    """
    spans: list[_Span] = []
    offset = 0
    for named_entity in document.named_entities:
        start, _ = named_entity.morphemes[0].global_span
        _, end = named_entity.morphemes[-1].global_span
        label = named_entity.category.value
        if start > offset:
            spans.append(_Span(document.text[offset:start]))
        spans.append(_Span(document.text[start:end], label))
        offset = end
    if offset < len(document.text):
        spans.append(_Span(document.text[offset:]))
    return spans


def create_app(analyzer: AnalyzerType, base_url: str = "/", *args, **kwargs) -> "fastapi.FastAPI":
    """解析器を起動し，HTTP サーバとして提供．

    Args:
        analyzer: 解析器の種類．
        base_url: ベース URL．
        args: 解析器のオプション．
        kwargs: 解析器のオプション．
    """
    processor: Union[Jumanpp, KNP, KWJA]
    title: str
    template_name: str
    version: str
    if analyzer == AnalyzerType.JUMANPP:
        title = "Juman++ Demo"
        template_name = "jumanpp.jinja2"
        processor = Jumanpp(*args, **kwargs)
    elif analyzer == AnalyzerType.KNP:
        title = "KNP Demo"
        template_name = "knp.jinja2"
        processor = KNP(*args, **kwargs)
    elif analyzer == AnalyzerType.KWJA:
        title = "KWJA Demo"
        template_name = "kwja.jinja2"
        processor = KWJA(*args, **kwargs)
    else:
        raise AssertionError  # unreachable
    version = processor.get_version()

    app = fastapi.FastAPI()
    app.mount("/static", fastapi.staticfiles.StaticFiles(directory=here.joinpath("static")), name="static")

    templates = fastapi.templating.Jinja2Templates(directory=here.joinpath("templates"))
    templates.env.globals["get_string_diff"] = _get_string_diff
    templates.env.globals["draw_tree"] = _draw_tree
    templates.env.globals["get_entity_spans"] = _get_entity_spans
    templates.env.globals["title"] = title
    templates.env.globals["version"] = version
    templates.env.globals["base_url"] = base_url

    @app.exception_handler(_HTTPExceptionForIndex)
    async def http_exception_handler_for_index(
        request: fastapi.Request, exc: _HTTPExceptionForIndex
    ) -> fastapi.Response:
        return templates.TemplateResponse(
            request=request,
            name=template_name,
            context={"error": exc.detail},
            status_code=exc.status_code,
        )

    @app.get("/", response_class=fastapi.responses.HTMLResponse)
    async def index(request: fastapi.Request, text: str = "") -> fastapi.Response:
        analyzed_document: Optional[Document] = None
        if text != "":
            try:
                analyzed_document = processor.apply(text)
            except Exception as e:
                raise _HTTPExceptionForIndex(fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
        return templates.TemplateResponse(
            request=request,
            name=template_name,
            context={"text": text, "analyzed_document": analyzed_document},
        )

    @app.exception_handler(_HTTPExceptionForAnalyze)
    async def http_exception_handler_for_analyze(_: fastapi.Request, exc: _HTTPExceptionForAnalyze) -> fastapi.Response:
        return fastapi.responses.JSONResponse(
            content={"error": {"code": exc.status_code, "message": exc.detail}},
            status_code=exc.status_code,
        )

    @app.get("/analyze", response_class=fastapi.responses.JSONResponse)
    async def analyze(text: str) -> fastapi.Response:
        if text == "":
            raise _HTTPExceptionForAnalyze(fastapi.status.HTTP_400_BAD_REQUEST, detail="text is empty")
        try:
            analyzed_document = processor.apply(text)
            if analyzer == AnalyzerType.JUMANPP:
                result = analyzed_document.to_jumanpp()
            else:
                result = analyzed_document.to_knp()
            return fastapi.responses.JSONResponse(content={"text": text, "result": result})
        except Exception as e:
            raise _HTTPExceptionForAnalyze(fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e

    return app


def serve_analyzer(
    analyzer: AnalyzerType, host: str, port: int, base_url: str, analyzer_args: Optional[list[str]]
) -> None:  # pragma: no cover
    """解析器を起動し，HTTP サーバとして提供．

    Args:
        analyzer: 解析器の種類．
        host: ホスト．
        port: ポート．
        base_url: ベース URL．
        analyzer_args: 解析器のオプション．
    """
    app = create_app(analyzer, base_url, options=analyzer_args)
    config = uvicorn.Config(app, host=host, port=port)
    server = uvicorn.Server(config)
    server.run()
