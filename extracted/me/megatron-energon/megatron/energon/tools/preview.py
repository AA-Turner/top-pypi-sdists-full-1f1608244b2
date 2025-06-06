# Copyright (c) 2025, NVIDIA CORPORATION.
# SPDX-License-Identifier: BSD-3-Clause

import dataclasses
import shutil
import traceback
from typing import Any

import click
import torch

from megatron.energon import Sample, StandardWebdatasetFactory
from megatron.energon.dataset_config import load_config
from megatron.energon.epathlib import EPath
from megatron.energon.flavors.webdataset import MAIN_FOLDER_NAME
from megatron.energon.flavors.webdataset.empty_dataset_error import EmptyDatasetError
from megatron.energon.loader import get_loader
from megatron.energon.worker import WorkerConfig


def to_str(value: Any, indent: str) -> str:
    if isinstance(value, torch.Tensor):
        orig_value = value
        # Probably image?
        if value.ndim == 3 and value.shape[0] in [1, 3, 4]:
            # Convert to grayscale
            if value.shape[0] == 1:
                value = value[0]
            elif value.shape[0] == 3:
                value = value.to(dtype=torch.float32).mean(dim=0)
            elif value.shape[0] == 4:
                value = value[:3].to(dtype=torch.float32).mean(dim=0)
        if value.ndim == 2:
            # 2d image -> ascii print
            # Resize to fit terminal
            dst_w, dst_h = shutil.get_terminal_size((80, 24))
            orig_h, orig_w = value.shape
            dst_w -= len(indent)
            procrustes = 0.3
            # keep aspect ratio
            if orig_w / orig_h < dst_w / dst_h:
                dst_h = int(dst_w * procrustes * orig_h / orig_w)
            else:
                dst_w = int(dst_h / procrustes * orig_w / orig_h)
            value = torch.nn.functional.interpolate(
                value[None, None, :, :].to(dtype=torch.float32), size=(dst_h, dst_w), mode="area"
            )[0, 0]
            # normalize
            value = (value - value.min()) / (value.max() - value.min())
            # to ascii text
            return (
                f"Tensor(shape={orig_value.shape}, dtype={orig_value.dtype}):\n{indent}"
                + f"\n{indent}".join(
                    "".join(" .:-=+*#%@@"[int(v * 10)] for v in row) for row in value.tolist()
                )
                + "\n"
            )
        elif value.ndim == 1:
            # 1d array... print it?
            return f"Tensor(shape={value.shape}, dtype={value.dtype}): {value[:128].tolist()}"
        else:
            return f"Tensor(shape={value.shape}, dtype={value.dtype})"
    elif isinstance(value, (str, int, float, bool, type(None))):
        return repr(value)
    elif isinstance(value, (list, tuple)):
        if hasattr(value, "_fields"):
            return (
                f"{type(value).__name__}(\n{indent}"
                + f",\n{indent}  ".join(
                    f"{field.name}={to_str(value, indent + '    ')}"
                    for value, field in zip(value, value._fields)
                )
                + f"\n{indent})"
            )
        if len(value) > 0 and isinstance(value, (str, int, float, bool)):
            return repr(type(value)(to_str(v, indent) for v in value))
        else:
            return (
                f"[\n{indent}"
                + f"\n{indent}  ".join(to_str(v, indent + "    ") for v in value)
                + f"\n{indent}]"
            )
    elif isinstance(value, bytes):
        return f"bytes(length={len(value)}, value={value[:128]!r})"
    return repr(value)


def pprint(idx: int, sample: Sample):
    click.echo(f"Sample {idx}")
    for field in dataclasses.fields(sample):
        if field.name in ("__restore_key__", "__subflavors__", "__sources__"):
            continue
        click.echo(f" - {field.name} ({field.type}): {to_str(getattr(sample, field.name), '')}")


@click.command(name="preview")
@click.argument(
    "path",
    type=click.Path(file_okay=False, dir_okay=True, path_type=EPath),
)
@click.option(
    "--split-parts", default="train,val,test", help="The splits to verify", show_default=True
)
@click.option(
    "--dataset-config", default="dataset.yaml", help="Dataset config file name", show_default=True
)
def command(path: EPath, split_parts: str, dataset_config: str):
    """Preview samples of a dataset on the console."""

    worker_config = WorkerConfig(rank=0, world_size=1, num_workers=0)

    for split_part in split_parts.split(","):
        try:
            dataset = load_config(
                EPath(path) / MAIN_FOLDER_NAME / dataset_config,
                default_kwargs=dict(
                    path=path,
                    split_part=split_part,
                    training=False,
                    worker_config=worker_config,
                ),
                default_type=StandardWebdatasetFactory,
            )
        except EmptyDatasetError:
            click.echo(f"Dataset {split_part} is empty. Skipping.")
            continue

        try:
            for idx, sample in enumerate(get_loader(dataset.build())):
                pprint(idx, sample)
                click.confirm("Continue?", abort=True)
        except click.Abort:
            click.echo("Exiting Preview")
        except BaseException:
            traceback.print_exc()
            raise click.ClickException("Validation failed with errors, see logs for details.")


if __name__ == "__main__":
    command()
