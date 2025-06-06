# Copyright (c) 2025, NVIDIA CORPORATION.
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import multiprocessing
from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, Iterable, List, Optional, TypeVar

T_result = TypeVar("T_result")
T_aggregation_data = TypeVar("T_aggregation_data")
T_input_data = TypeVar("T_input_data")


class BaseAggregator(ABC, Generic[T_aggregation_data, T_result]):
    """
    Base class for a user-defined aggregator.
    Implement on_start, on_item, and on_finish to handle aggregator logic.
    """

    def on_start(self, aggregator_pool: AggregatorPool) -> None:
        """
        Called exactly once in the aggregator process before receiving any items.
        """
        pass

    @abstractmethod
    def on_item(self, item: T_aggregation_data, aggregator_pool: AggregatorPool) -> None:
        """
        Called for each item produced by the workers.
        """
        ...

    def on_finish(self, aggregator_pool: AggregatorPool) -> None:
        """
        Called once when all workers have signaled completion (i.e. all items are processed).
        """
        pass

    def get_final_result_data(self) -> T_result:
        """
        Called after on_finish to retrieve any final data produced by the aggregator.
        """
        return None


class AggregatorPool(Generic[T_input_data, T_aggregation_data, T_result]):
    """
    A pool that manages multiple worker processes sending results to
    a single aggregator process.

    The user must provide:
      - user_produce_data(task) -> yields items (streaming results)
      - aggregator: an instance of a class derived from BaseAggregator
                    which implements on_start, on_item, on_finish, etc.
    """

    num_workers: int
    user_produce_data: Callable[[T_input_data], Iterable[Any]]
    aggregator: BaseAggregator[T_aggregation_data, T_result]

    task_queue: multiprocessing.Queue[Optional[T_input_data]]
    result_queue: multiprocessing.Queue[Optional[T_aggregation_data]]

    def __init__(
        self,
        num_workers: int,
        user_produce_data: Callable[[T_input_data], Iterable[Any]],
        aggregator: BaseAggregator[T_aggregation_data, T_result],
    ) -> None:
        """
        Args:
            num_workers: Number of worker processes.
            user_produce_data: Function that takes a task and yields items (the "large" data stream).
            aggregator: An instance of a user-defined class for handling aggregator logic.
        """
        self.num_workers = num_workers
        self.user_produce_data = user_produce_data
        self.aggregator = aggregator

        # Queues for tasks and results
        self.task_queue = multiprocessing.Queue()
        self.result_queue = multiprocessing.Queue()

        # Queue to pass final aggregator data back to the main process
        self._final_result_data_queue = multiprocessing.Queue()

        # Will store whatever is pulled from _final_data_queue in close()
        self._aggregator_final_result_data: Optional[Any] = None

    def _worker(self, worker_id: int) -> None:
        """Function that runs inside each worker process."""
        while True:
            task = self.task_queue.get()
            if task is None:
                # No more tasks, signal aggregator that this worker is done
                break

            # Produce data in a streaming fashion
            for item in self.user_produce_data(task):
                self.result_queue.put(item)

        # After finishing all tasks, send a sentinel to the aggregator
        self.result_queue.put(None)

    def _aggregator_run(self) -> T_result:
        """
        Function that runs in the aggregator process.
        Keeps reading items from result_queue.
        - If an item is None, that means a worker finished all of its tasks.
        - Otherwise, call aggregator.on_item(...) with that item.
        """
        # Let the aggregator do any initialization it needs
        self.aggregator.on_start(self)

        finished_workers = 0

        while finished_workers < self.num_workers:
            item = self.result_queue.get()
            if item is None:
                # A worker has finished all of its tasks
                finished_workers += 1
            else:
                # Process the item in the aggregator
                self.aggregator.on_item(item, self)

        # All workers done, aggregator can finalize
        self.aggregator.on_finish(self)

        # After finishing, serialize the aggregator's final data
        return self.aggregator.get_final_result_data()

    def submit_task(self, task: T_input_data) -> None:
        """
        Submit a task to be processed by a worker.
        """
        self.task_queue.put(task)

    def process(self) -> T_result:
        """
        Starts the worker processes and runs the aggregation in the main process.
        Waits for all workers to finish and retrieves the aggregator's final data.
        """
        workers: List[multiprocessing.Process] = []

        # Start worker processes
        for w_id in range(self.num_workers):
            p = multiprocessing.Process(target=self._worker, args=(w_id,), daemon=True)
            p.start()
            workers.append(p)

        # Send the sentinel (None) to each worker
        for _ in range(self.num_workers):
            self.task_queue.put(None)

        # Now wait for aggregator to finish reading the queue
        result = self._aggregator_run()

        # Wait for all workers to finish
        for p in workers:
            p.join()

        return result
