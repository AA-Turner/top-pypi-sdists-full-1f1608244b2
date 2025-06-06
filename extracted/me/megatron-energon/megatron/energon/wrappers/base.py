# Copyright (c) 2025, NVIDIA CORPORATION.
# SPDX-License-Identifier: BSD-3-Clause

from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, Generator, Generic, Iterable, Optional, Tuple, Type, TypeVar, Union

from megatron.energon.flavors.base_dataset import (
    FlexState,
    Sample,
    SavableDataset,
    add_sample_restore_key,
)
from megatron.energon.savable import Savable
from megatron.energon.worker import WorkerConfig

T = TypeVar("T")
T_sample = TypeVar("T_sample", covariant=True)
T_sample_out = TypeVar("T_sample_out", covariant=True)
T_sample_in = TypeVar("T_sample_in", covariant=True)


class BaseWrapperDataset(SavableDataset[T_sample_out], Generic[T_sample_in, T_sample_out], ABC):
    """Base class for dataset wrappers. All dataset wrappers should derive from this. A dataset
    wrapper takes one dataset and modifies its samples to make a new dataset. This can be for
    shuffling samples or applying custom functions to the data. Some wrappers only modify the
    length of the dataset or how it's repeated."""

    datasets: Tuple[SavableDataset[T_sample_in], ...]

    def __init__(
        self,
        datasets: Union[SavableDataset[T_sample_in], Iterable[SavableDataset[T_sample_in]]],
        *,
        worker_config: WorkerConfig,
    ):
        super().__init__(worker_config=worker_config)

        if isinstance(datasets, SavableDataset):
            self.datasets = (datasets,)
        else:
            self.datasets = tuple(datasets)

        for d in self.datasets:
            # Check that the dataset worker configs are the same as the wrapper worker config
            assert d.worker_config == self.worker_config, (
                "Dataset and wrapper worker configs must match."
            )

    @property
    def dataset(self) -> SavableDataset:
        """Convenience property, if only one dataset is wrapped."""

        assert len(self.datasets) == 1
        return self.datasets[0]

    def can_restore_sample(self) -> bool:
        return all(ds.can_restore_sample() for ds in self.datasets)

    def assert_can_restore(self) -> None:
        for ds in self.datasets:
            ds.assert_can_restore()

    def worker_has_samples(self) -> bool:
        return any(ds.worker_has_samples() for ds in self.datasets)

    def _find_wrapped_dataset(self, cls: Type[SavableDataset]) -> Optional[SavableDataset]:
        """Find the outermost dataset wrapped in this dataset that is of type cls."""

        for ds in self.datasets:
            if isinstance(ds, cls):
                return ds
            elif isinstance(ds, BaseWrapperDataset):
                res = ds._find_wrapped_dataset(cls)
                if res is not None:
                    return res
        return None

    def restore_sample(self, restore_key: Tuple[Union[str, int, tuple], ...]) -> T_sample_out:
        if len(self.datasets) == 1:
            return self.datasets[0].restore_sample(restore_key)
        else:
            id, ds_idx = restore_key[:2]
            assert id == type(self).__name__
            restore_key = restore_key[2:]
            assert isinstance(ds_idx, int)
            return add_sample_restore_key(
                self.datasets[ds_idx].restore_sample(restore_key),
                ds_idx,
                src=self,
            )

    def save_state(self) -> FlexState:
        own_state = super().save_state()

        return FlexState(datasets=[ds.save_state() for ds in self.datasets], **own_state)

    def restore_state(self, state: FlexState) -> None:
        assert len(self.datasets) == len(state["datasets"])
        for dataset, dstate in zip(self.datasets, state["datasets"]):
            dataset.restore_state(dstate)

        super().restore_state(state)

    def reset_state_deep(self) -> None:
        """Resets the state of the inner datasets and then the own state."""

        for ds in self.datasets:
            if isinstance(ds, BaseWrapperDataset):
                ds.reset_state_deep()
            else:
                ds.reset_state_own()

        self.reset_state_own()

    @abstractmethod
    def reset_state_own(self) -> None:
        """Resets the state of the dataset, excl. the inner datasets."""
        ...


class SampleIndex(Savable):
    """A simple class to hold the sample index for one worker."""

    worker_config: WorkerConfig
    current_idx: int

    actives = 0

    def __init__(self, worker_config: WorkerConfig, *, src: Any) -> None:
        self.worker_config = worker_config
        self.current_idx = 0
        self.src = src

    def get_next(self) -> int:
        res = self.current_idx
        self.current_idx += 1
        return res

    @contextmanager
    def ctx(self, sample_idx: Optional[int] = None):
        if sample_idx is None:
            sample_idx = self.get_next()
        assert WorkerConfig.active_worker_config is not None
        WorkerConfig.active_worker_config.worker_push_sample_index(sample_idx)
        # print("  " * SampleIndex.actives + f"Activated from {type(self.src).__name__}({id(self.src)}) {sample_idx} -> {WorkerConfig.active_worker_config._sample_index_stack}")
        SampleIndex.actives += 1
        try:
            yield sample_idx
        finally:
            assert WorkerConfig.active_worker_config is not None
            popped = WorkerConfig.active_worker_config.worker_pop_sample_index()
            SampleIndex.actives -= 1
            # print("  " * SampleIndex.actives + f"Deactivate from {type(self.src).__name__}({id(self.src)}) {sample_idx} -> {WorkerConfig.active_worker_config._sample_index_stack}")
            assert popped == sample_idx, f"Expected {sample_idx}, got {popped}"

    def iter_ctx(
        self,
        it: Iterable[T_sample],
        sample_idx: Optional[int] = None,
    ) -> Generator[Tuple[int, T_sample], None, None]:
        it = iter(it)
        try:
            while True:
                try:
                    with self.ctx(sample_idx) as res_sample_idx:
                        x = next(it)
                    yield res_sample_idx, x
                except StopIteration:
                    break
        finally:
            if hasattr(it, "close"):
                it.close()

    def save_state(self) -> int:
        return self.current_idx

    def restore_state(self, state: Optional[int]) -> None:
        if state is None:
            self.current_idx = 0
        else:
            self.current_idx = state


def get_sample_restore_key(sample: Any) -> Optional[Union[str, int]]:
    """Gets the restore key from an arbitrary sample."""
    if isinstance(sample, Sample) or hasattr(sample, "__restore_key__"):
        return sample.__restore_key__
    elif isinstance(sample, dict) and "__restore_key__" in sample:
        return sample["__restore_key__"]
    else:
        return None
