from __future__ import annotations

import argparse
import json
import logging
import sys
from collections.abc import Collection, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional, Union

import pandas
from annofabapi.parser import SimpleAnnotationParser, lazy_parse_simple_annotation_dir, lazy_parse_simple_annotation_zip
from dataclasses_json import DataClassJsonMixin
from PIL import Image, ImageColor, ImageDraw

import annofabcli
from annofabcli.common.cli import (
    COMMAND_LINE_ERROR_STATUS_CODE,
    ArgumentParser,
    CommandLineWithoutWebapi,
    get_json_from_args,
    get_list_from_args,
)
from annofabcli.common.facade import TaskQuery, match_annotation_with_task_query

logger = logging.getLogger(__name__)


Color = Union[str, tuple[int, int, int]]
IsParserFunc = Callable[[SimpleAnnotationParser], bool]


@dataclass(frozen=True)
class DrawingOptions(DataClassJsonMixin):
    line_width: int = 1
    """線の太さ[pixel]"""


class DrawingAnnotationForOneImage:
    _COLOR_PALETTE = [  # noqa: RUF012
        "red",
        "maroon",
        "yellow",
        "olive",
        "lime",
        "green",
        "aqua",
        "teal",
        "blue",
        "navy",
        "fuchsia",
        "purple",
        "black",
        "gray",
        "silver",
        "white",
    ]

    def __init__(
        self,
        label_color_dict: Optional[dict[str, Color]] = None,
        target_label_names: Optional[Collection[str]] = None,
        polyline_labels: Optional[Collection[str]] = None,
        drawing_options: Optional[DrawingOptions] = None,
    ) -> None:
        self.label_color_dict = label_color_dict if label_color_dict is not None else {}
        self.target_label_names = set(target_label_names) if target_label_names is not None else None
        self.polyline_labels = set(polyline_labels) if polyline_labels is not None else None
        self.drawing_options = drawing_options if drawing_options is not None else DrawingOptions()
        self._color_palette_index = 0

    def get_color(self, label_name: str) -> Color:
        if label_name in self.label_color_dict:
            return self.label_color_dict[label_name]
        else:
            color = self._COLOR_PALETTE[self._color_palette_index]
            self.label_color_dict[label_name] = color

            self._color_palette_index += 1
            self._color_palette_index = self._color_palette_index % len(self._COLOR_PALETTE)
            return color

    def _draw_annotations(
        self,
        draw: ImageDraw.ImageDraw,
        parser: SimpleAnnotationParser,
    ) -> ImageDraw.ImageDraw:
        """
        1個の入力データに属するアノテーションのみを描画する。

        Args:
            draw: draw: (IN/OUT) PillowのDrawing Object. 変更される。
            parser: Simple Annotationのparser

        Returns:
            アノテーションを描画した状態のDrawing Object
        """

        def draw_segmentation(data_uri: str, color: Color):  # noqa: ANN202
            # 外部ファイルを描画する
            with parser.open_outer_file(data_uri) as f:  # noqa: SIM117
                with Image.open(f) as outer_image:
                    draw.bitmap([0, 0], outer_image, fill=color)

        def draw_bounding_box(data: dict[str, Any], color: Color):  # noqa: ANN202
            xy = [
                (data["left_top"]["x"], data["left_top"]["y"]),
                (data["right_bottom"]["x"], data["right_bottom"]["y"]),
            ]
            draw.rectangle(xy, outline=color, width=self.drawing_options.line_width)

        def draw_single_point(data: dict[str, Any], color: Color, radius: int = 2):  # noqa: ANN202
            point_x = data["point"]["x"]
            point_y = data["point"]["y"]
            draw.ellipse([(point_x - radius, point_y - radius), (point_x + radius, point_y + radius)], fill=color)

        def draw_closed_polyline(data: dict[str, Any], color: Color):  # noqa: ANN202
            points = data["points"]
            first_point = points[0]
            xy = [(e["x"], e["y"]) for e in points] + [(first_point["x"], first_point["y"])]
            draw.line(xy, fill=color, width=self.drawing_options.line_width)

        def draw_polyline(data: dict[str, Any], color: Color):  # noqa: ANN202
            xy = [(e["x"], e["y"]) for e in data["points"]]
            draw.line(xy, fill=color, width=self.drawing_options.line_width)

        simple_annotation = parser.load_json()
        # 下層レイヤにあるアノテーションから順に画像化する
        # reversed関数を使う理由：`simple_annotation.details`は上層レイヤのアノテーションから順に格納されているため
        if self.target_label_names is not None:
            annotation_list = [e for e in reversed(simple_annotation["details"]) if e["label"] in self.target_label_names]
        else:
            annotation_list = list(reversed(simple_annotation["details"]))
        for annotation in annotation_list:
            data = annotation["data"]
            data_type = data["_type"]
            if data_type == "Classification":
                # 全体アノテーションなので描画できない
                continue

            label_name: str = annotation["label"]
            color = self.get_color(label_name)

            if data_type in {"SegmentationV2", "Segmentation"}:
                draw_segmentation(data["data_uri"], color=color)

            elif data_type == "BoundingBox":
                draw_bounding_box(data, color=color)

            elif data_type == "SinglePoint":
                draw_single_point(data, color=color)
            elif data_type == "Points":
                if self.polyline_labels is not None and label_name in self.polyline_labels:
                    draw_polyline(data, color=color)
                else:
                    draw_closed_polyline(data, color=color)

        return draw

    def main(  # noqa: ANN201
        self,
        parser: SimpleAnnotationParser,
        image_file: Optional[Path],
        output_file: Path,
        image_size: Optional[tuple[int, int]] = None,
    ):
        """画像にアノテーションを描画したファイルを出力する。

        Args:
            parser (SimpleAnnotationParser): [description]
            image_file (Path): [description]
            output_file (Path): [description]
        """
        assert image_file is not None or image_size is not None

        if image_file is not None:
            with Image.open(image_file) as image:
                draw = ImageDraw.Draw(image)
                self._draw_annotations(draw, parser)
                output_file.parent.mkdir(parents=True, exist_ok=True)
                image.save(output_file)

        elif image_size is not None:
            image = Image.new("RGBA", image_size, color="black")
            draw = ImageDraw.Draw(image)
            self._draw_annotations(draw, parser)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            image.save(output_file)


def create_is_target_parser_func(
    task_ids: Optional[Collection[str]] = None,
    task_query: Optional[TaskQuery] = None,
) -> Optional[IsParserFunc]:
    if task_ids is None and task_query is None:
        return None

    task_id_set = set(task_ids) if task_ids is not None else None

    def is_target_parser(parser: SimpleAnnotationParser) -> bool:
        if task_id_set is not None and len(task_id_set) > 0:  # noqa: SIM102
            if parser.task_id not in task_id_set:
                return False

        if task_query is not None:
            dict_simple_annotation = parser.load_json()
            if not match_annotation_with_task_query(dict_simple_annotation, task_query):
                return False

        return True

    return is_target_parser


def draw_annotation_all(  # noqa: ANN201, PLR0913
    iter_parser: Iterator[SimpleAnnotationParser],
    image_dir: Optional[Path],
    input_data_id_relation_dict: Optional[dict[str, str]],
    output_dir: Path,
    *,
    target_task_ids: Optional[Collection[str]] = None,
    task_query: Optional[TaskQuery] = None,
    label_color_dict: Optional[dict[str, Color]] = None,
    target_label_names: Optional[Collection[str]] = None,
    polyline_labels: Optional[Collection[str]] = None,
    drawing_options: Optional[DrawingOptions] = None,
    default_image_size: Optional[tuple[int, int]] = None,
):
    drawing = DrawingAnnotationForOneImage(
        label_color_dict=label_color_dict,
        target_label_names=target_label_names,
        polyline_labels=polyline_labels,
        drawing_options=drawing_options,
    )

    is_target_parser_func = create_is_target_parser_func(target_task_ids, task_query)

    total_count = 0
    success_count = 0

    for parser in iter_parser:
        logger.debug(f"{parser.json_file_path} を読み込みます。")
        if is_target_parser_func is not None and not is_target_parser_func(parser):
            continue

        total_count += 1
        input_data_id = parser.input_data_id
        if input_data_id_relation_dict is not None:  # noqa: SIM102
            if input_data_id not in input_data_id_relation_dict:
                logger.warning(f"input_data_id='{input_data_id}'に対応する画像ファイルのパスが見つかりませんでした。")
                continue

        image_file: Optional[Path] = None
        if image_dir is not None and input_data_id_relation_dict is not None:
            image_file = image_dir / input_data_id_relation_dict[input_data_id]
            if not image_file.exists():
                logger.warning(f"input_data_id='{input_data_id}'に対応する画像ファイル'{image_file}'が見つかりませんでした。")
                continue

        json_file = Path(parser.json_file_path)
        if image_file is not None:
            output_file = output_dir / f"{json_file.parent.name}/{json_file.stem}{image_file.suffix}"
        else:
            output_file = output_dir / f"{json_file.parent.name}/{json_file.stem}.png"

        try:
            drawing.main(parser, image_file=image_file, output_file=output_file, image_size=default_image_size)
            logger.debug(f"{success_count + 1}件目: {output_file!s} を出力しました。image_file={image_file}, アノテーションJSON={parser.json_file_path}")
            success_count += 1
        except Exception:  # pylint: disable=broad-except
            logger.warning(f"{parser.json_file_path} のアノテーションの描画に失敗しました。", exc_info=True)

    logger.info(f"{success_count} / {total_count} 件、アノテーションを描画しました。")

    new_label_color_dict = {label_name: ImageColor.getrgb(color) if isinstance(color, str) else color for label_name, color in drawing.label_color_dict.items()}
    logger.info(f"label_color={json.dumps(new_label_color_dict, ensure_ascii=False)}")


class DrawAnnotation(CommandLineWithoutWebapi):
    COMMON_MESSAGE = "annofabcli filesystem draw_annotation:"

    @staticmethod
    def _create_label_color(args_label_color: str) -> dict[str, Color]:
        label_color_dict = get_json_from_args(args_label_color)
        for label_name, color in label_color_dict.items():
            if isinstance(color, list):
                label_color_dict[label_name] = tuple(color)
        return label_color_dict

    def main(self) -> None:
        args = self.args

        default_image_size: Optional[tuple[int, int]] = None
        if args.default_image_size is not None:
            default_image_size = annofabcli.common.cli.get_input_data_size(args.default_image_size)
            if default_image_size is None:
                print(  # noqa: T201
                    f"{self.COMMON_MESSAGE} argument '--default_image_size': フォーマットが不正です。",
                    file=sys.stderr,
                )
                sys.exit(COMMAND_LINE_ERROR_STATUS_CODE)

        if args.default_image_size is None and args.input_data_id_csv is None:
            print(  # noqa: T201
                f"{self.COMMON_MESSAGE} '--default_image_size'または'--input_data_id_csv'のいずれかは必須です。",
                file=sys.stderr,
            )
            sys.exit(COMMAND_LINE_ERROR_STATUS_CODE)

        if args.image_dir is None and args.input_data_id_csv is not None:
            print(  # noqa: T201
                f"{self.COMMON_MESSAGE} argument '--image_dir': '--input_data_id_csv'を指定したときは必須です。",
                file=sys.stderr,
            )
            sys.exit(COMMAND_LINE_ERROR_STATUS_CODE)

        annotation_path: Path = args.annotation
        # Simpleアノテーションの読み込み
        if annotation_path.is_file():
            iter_parser = lazy_parse_simple_annotation_zip(annotation_path)
        else:
            iter_parser = lazy_parse_simple_annotation_dir(annotation_path)

        input_data_id_relation_dict: Optional[dict[str, str]] = None
        if args.input_data_id_csv is not None:
            df = pandas.read_csv(
                args.input_data_id_csv,
                sep=",",
                header=None,
                names=("input_data_id", "image_path"),
            )
            input_data_id_relation_dict = dict(zip(df["input_data_id"], df["image_path"]))

        task_query = TaskQuery.from_dict(annofabcli.common.cli.get_json_from_args(args.task_query)) if args.task_query is not None else None

        draw_annotation_all(
            iter_parser=iter_parser,
            image_dir=args.image_dir,
            input_data_id_relation_dict=input_data_id_relation_dict,
            output_dir=args.output_dir,
            target_task_ids=get_list_from_args(args.task_id) if args.task_id is not None else None,
            task_query=task_query,
            label_color_dict=self._create_label_color(args.label_color) if args.label_color is not None else None,
            target_label_names=get_list_from_args(args.label_name) if args.label_name is not None else None,
            polyline_labels=get_list_from_args(args.polyline_label) if args.polyline_label is not None else None,
            drawing_options=DrawingOptions.from_dict(get_json_from_args(args.drawing_options)) if args.drawing_options is not None else None,
            default_image_size=default_image_size,
        )


def main(args: argparse.Namespace) -> None:
    DrawAnnotation(args).main()


def parse_args(parser: argparse.ArgumentParser) -> None:
    argument_parser = ArgumentParser(parser)

    parser.add_argument(
        "--annotation",
        type=Path,
        required=True,
        help="Annofabからダウンロードしたアノテーションzip、またはzipを展開したディレクトリを指定してください。",
    )

    parser.add_argument("--image_dir", type=Path, help="画像が存在するディレクトリを指定してください。\n'--input_data_id_csv'を指定したときは必須です。")

    parser.add_argument(
        "--input_data_id_csv",
        type=Path,
        help="``input_data_id`` と ``--image_dir`` 配下の画像ファイルを紐付けたCSVを指定してください。\n"
        "``--default_image_size`` を指定しないときは必須です。\n"
        "CSVのフォーマットは、「1列目:input_data_id, 2列目:画像ファイルのパス」です。\n"
        "詳細は https://annofab-cli.readthedocs.io/ja/latest/command_reference/filesystem/draw_annotation.html を参照してください。",
    )

    parser.add_argument("--default_image_size", type=str, help="デフォルトの画像サイズ。 ``--input_data_id_csv`` を指定しないときは必須です。\n(例) 1280x720")

    LABEL_COLOR_SAMPLE = {"dog": [255, 128, 64], "cat": "blue"}  # noqa: N806
    parser.add_argument(
        "--label_color",
        type=str,
        help=f"label_nameとRGBの関係をJSON形式で指定します。\n(例) ``{json.dumps(LABEL_COLOR_SAMPLE)}``\n``file://`` を先頭に付けると、JSON形式のファイルを指定できます。",
    )

    parser.add_argument(
        "-o",
        "--output_dir",
        type=Path,
        required=True,
        help="出力先ディレクトリのパスを指定してください。ディレクトリの構造はアノテーションzipと同じです。",
    )

    parser.add_argument(
        "--label_name",
        type=str,
        nargs="+",
        required=False,
        help="描画対象のアノテーションのlabel_nameを指定します。指定しない場合は、すべてのlabel_nameが描画対象になります。"
        " ``file://`` を先頭に付けると、label_name の一覧が記載されたファイルを指定できます。",
    )

    parser.add_argument(
        "--polyline_label",
        type=str,
        nargs="+",
        required=False,
        help="ポリラインのlabel_nameを指定してください。"
        "2021/07時点ではアノテーションzipからポリラインかポリゴンか判断できないため、コマンドライン引数からポリラインのlabel_nameを指定する必要があります。"
        " ``file://`` を先頭に付けると、label_name の一覧が記載されたファイルを指定できます。 \n"
        "【注意】アノテーションzipでポリラインかポリゴンかを判断できるようになれば、このオプションは削除する予定です。",
    )

    DRAWING_OPTIONS_SAMPLE = {"line_width": 3}  # noqa: N806
    parser.add_argument(
        "--drawing_options",
        type=str,
        help=f"描画オプションをJSON形式で指定します。\n(例) ``{json.dumps(DRAWING_OPTIONS_SAMPLE)}``\n\n``file://`` を先頭に付けると、JSON形式のファイルを指定できます。",
    )

    argument_parser.add_task_id(
        required=False,
        help_message=(
            "描画対象であるタスクのtask_idを指定します。"
            "指定しない場合、すべてのタスクに含まれるアノテーションが描画されます。"
            " ``file://`` を先頭に付けると、task_idの一覧が記載されたファイルを指定できます。"
        ),
    )

    parser.add_argument(
        "-tq",
        "--task_query",
        type=str,
        help="描画対象のタスクを絞り込むためのクエリ条件をJSON形式で指定します。\n"
        "使用できるキーは task_id, status, phase, phase_stage です。\n"
        "``file://`` を先頭に付けると、JSON形式のファイルを指定できます。",
    )

    parser.set_defaults(subcommand_func=main)


def add_parser(subparsers: Optional[argparse._SubParsersAction] = None) -> argparse.ArgumentParser:
    subcommand_name = "draw_annotation"

    subcommand_help = "画像にアノテーションを描画します。"

    description = "画像にアノテーションを描画します。"

    parser = annofabcli.common.cli.add_parser(subparsers, subcommand_name, subcommand_help, description)
    parse_args(parser)
    return parser
