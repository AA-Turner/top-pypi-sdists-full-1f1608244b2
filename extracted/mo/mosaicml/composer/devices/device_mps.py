# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""The Apple M-series device used for training."""

from __future__ import annotations

from typing import TypeVar

import torch
import torch.cuda.amp
import torch.utils.data

from composer.devices.device import Device

__all__ = ['DeviceMPS']

T_nnModule = TypeVar('T_nnModule', bound=torch.nn.Module)


class DeviceMPS(Device):
    """Device to support MPS, for training on Apple's M-series chips.

    This class takes no arguments.
    """
    dist_backend = ''
    name = 'mps'

    def __init__(self) -> None:
        if not torch.backends.mps.is_available():  # type: ignore (version guarded)
            raise RuntimeError('MPS requires MAC OSX >= 12.3')
        if not torch.backends.mps.is_built():  # type: ignore (version guarded)
            raise RuntimeError('torch was not build with MPS support.')

        self._device = torch.device('mps')

    def module_to_device(self, module: T_nnModule) -> T_nnModule:
        return module.to(self._device)

    def tensor_to_device(self, tensor: torch.Tensor) -> torch.Tensor:
        return tensor.to(self._device)
