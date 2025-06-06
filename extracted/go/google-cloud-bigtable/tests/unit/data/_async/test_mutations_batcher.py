# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import mock
import asyncio
import time
import google.api_core.exceptions as core_exceptions
import google.api_core.retry
from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete
from google.cloud.bigtable.data.mutations import RowMutationEntry
from google.cloud.bigtable.data.mutations import DeleteAllFromRow
from google.cloud.bigtable.data import TABLE_DEFAULT

from google.cloud.bigtable.data._cross_sync import CrossSync

__CROSS_SYNC_OUTPUT__ = "tests.unit.data._sync_autogen.test_mutations_batcher"


@CrossSync.convert_class(sync_name="Test_FlowControl")
class Test_FlowControlAsync:
    @staticmethod
    @CrossSync.convert
    def _target_class():
        return CrossSync._FlowControl

    def _make_one(self, max_mutation_count=10, max_mutation_bytes=100):
        return self._target_class()(max_mutation_count, max_mutation_bytes)

    @staticmethod
    def _make_mutation(count=1, size=1):
        mutation = RowMutationEntry("k", DeleteAllFromRow())
        mutation.mutations = [DeleteAllFromRow() for _ in range(count)]
        mutation.size = lambda: size
        return mutation

    def test_ctor(self):
        max_mutation_count = 9
        max_mutation_bytes = 19
        instance = self._make_one(max_mutation_count, max_mutation_bytes)
        assert instance._max_mutation_count == max_mutation_count
        assert instance._max_mutation_bytes == max_mutation_bytes
        assert instance._in_flight_mutation_count == 0
        assert instance._in_flight_mutation_bytes == 0
        assert isinstance(instance._capacity_condition, CrossSync.Condition)

    def test_ctor_invalid_values(self):
        """Test that values are positive, and fit within expected limits"""
        with pytest.raises(ValueError) as e:
            self._make_one(0, 1)
            assert "max_mutation_count must be greater than 0" in str(e.value)
        with pytest.raises(ValueError) as e:
            self._make_one(1, 0)
            assert "max_mutation_bytes must be greater than 0" in str(e.value)

    @pytest.mark.parametrize(
        "max_count,max_size,existing_count,existing_size,new_count,new_size,expected",
        [
            (1, 1, 0, 0, 0, 0, True),
            (1, 1, 1, 1, 1, 1, False),
            (10, 10, 0, 0, 0, 0, True),
            (10, 10, 0, 0, 9, 9, True),
            (10, 10, 0, 0, 11, 9, True),
            (10, 10, 0, 1, 11, 9, True),
            (10, 10, 1, 0, 11, 9, False),
            (10, 10, 0, 0, 9, 11, True),
            (10, 10, 1, 0, 9, 11, True),
            (10, 10, 0, 1, 9, 11, False),
            (10, 1, 0, 0, 1, 0, True),
            (1, 10, 0, 0, 0, 8, True),
            (float("inf"), float("inf"), 0, 0, 1e10, 1e10, True),
            (8, 8, 0, 0, 1e10, 1e10, True),
            (12, 12, 6, 6, 5, 5, True),
            (12, 12, 5, 5, 6, 6, True),
            (12, 12, 6, 6, 6, 6, True),
            (12, 12, 6, 6, 7, 7, False),
            # allow capacity check if new_count or new_size exceeds limits
            (12, 12, 0, 0, 13, 13, True),
            (12, 12, 12, 0, 0, 13, True),
            (12, 12, 0, 12, 13, 0, True),
            # but not if there's already values in flight
            (12, 12, 1, 1, 13, 13, False),
            (12, 12, 1, 1, 0, 13, False),
            (12, 12, 1, 1, 13, 0, False),
        ],
    )
    def test__has_capacity(
        self,
        max_count,
        max_size,
        existing_count,
        existing_size,
        new_count,
        new_size,
        expected,
    ):
        """
        _has_capacity should return True if the new mutation will will not exceed the max count or size
        """
        instance = self._make_one(max_count, max_size)
        instance._in_flight_mutation_count = existing_count
        instance._in_flight_mutation_bytes = existing_size
        assert instance._has_capacity(new_count, new_size) == expected

    @CrossSync.pytest
    @pytest.mark.parametrize(
        "existing_count,existing_size,added_count,added_size,new_count,new_size",
        [
            (0, 0, 0, 0, 0, 0),
            (2, 2, 1, 1, 1, 1),
            (2, 0, 1, 0, 1, 0),
            (0, 2, 0, 1, 0, 1),
            (10, 10, 0, 0, 10, 10),
            (10, 10, 5, 5, 5, 5),
            (0, 0, 1, 1, -1, -1),
        ],
    )
    async def test_remove_from_flow_value_update(
        self,
        existing_count,
        existing_size,
        added_count,
        added_size,
        new_count,
        new_size,
    ):
        """
        completed mutations should lower the inflight values
        """
        instance = self._make_one()
        instance._in_flight_mutation_count = existing_count
        instance._in_flight_mutation_bytes = existing_size
        mutation = self._make_mutation(added_count, added_size)
        await instance.remove_from_flow(mutation)
        assert instance._in_flight_mutation_count == new_count
        assert instance._in_flight_mutation_bytes == new_size

    @CrossSync.pytest
    async def test__remove_from_flow_unlock(self):
        """capacity condition should notify after mutation is complete"""
        instance = self._make_one(10, 10)
        instance._in_flight_mutation_count = 10
        instance._in_flight_mutation_bytes = 10

        async def task_routine():
            async with instance._capacity_condition:
                await instance._capacity_condition.wait_for(
                    lambda: instance._has_capacity(1, 1)
                )

        if CrossSync.is_async:
            # for async class, build task to test flow unlock
            task = asyncio.create_task(task_routine())

            def task_alive():
                return not task.done()

        else:
            # this branch will be tested in sync version of this test
            import threading

            thread = threading.Thread(target=task_routine)
            thread.start()
            task_alive = thread.is_alive
        await CrossSync.sleep(0.05)
        # should be blocked due to capacity
        assert task_alive() is True
        # try changing size
        mutation = self._make_mutation(count=0, size=5)

        await instance.remove_from_flow([mutation])
        await CrossSync.sleep(0.05)
        assert instance._in_flight_mutation_count == 10
        assert instance._in_flight_mutation_bytes == 5
        assert task_alive() is True
        # try changing count
        instance._in_flight_mutation_bytes = 10
        mutation = self._make_mutation(count=5, size=0)
        await instance.remove_from_flow([mutation])
        await CrossSync.sleep(0.05)
        assert instance._in_flight_mutation_count == 5
        assert instance._in_flight_mutation_bytes == 10
        assert task_alive() is True
        # try changing both
        instance._in_flight_mutation_count = 10
        mutation = self._make_mutation(count=5, size=5)
        await instance.remove_from_flow([mutation])
        await CrossSync.sleep(0.05)
        assert instance._in_flight_mutation_count == 5
        assert instance._in_flight_mutation_bytes == 5
        # task should be complete
        assert task_alive() is False

    @CrossSync.pytest
    @pytest.mark.parametrize(
        "mutations,count_cap,size_cap,expected_results",
        [
            # high capacity results in no batching
            ([(5, 5), (1, 1), (1, 1)], 10, 10, [[(5, 5), (1, 1), (1, 1)]]),
            # low capacity splits up into batches
            ([(1, 1), (1, 1), (1, 1)], 1, 1, [[(1, 1)], [(1, 1)], [(1, 1)]]),
            # test count as limiting factor
            ([(1, 1), (1, 1), (1, 1)], 2, 10, [[(1, 1), (1, 1)], [(1, 1)]]),
            # test size as limiting factor
            ([(1, 1), (1, 1), (1, 1)], 10, 2, [[(1, 1), (1, 1)], [(1, 1)]]),
            # test with some bloackages and some flows
            (
                [(1, 1), (5, 5), (4, 1), (1, 4), (1, 1)],
                5,
                5,
                [[(1, 1)], [(5, 5)], [(4, 1), (1, 4)], [(1, 1)]],
            ),
        ],
    )
    async def test_add_to_flow(self, mutations, count_cap, size_cap, expected_results):
        """
        Test batching with various flow control settings
        """
        mutation_objs = [self._make_mutation(count=m[0], size=m[1]) for m in mutations]
        instance = self._make_one(count_cap, size_cap)
        i = 0
        async for batch in instance.add_to_flow(mutation_objs):
            expected_batch = expected_results[i]
            assert len(batch) == len(expected_batch)
            for j in range(len(expected_batch)):
                # check counts
                assert len(batch[j].mutations) == expected_batch[j][0]
                # check sizes
                assert batch[j].size() == expected_batch[j][1]
            # update lock
            await instance.remove_from_flow(batch)
            i += 1
        assert i == len(expected_results)

    @CrossSync.pytest
    @pytest.mark.parametrize(
        "mutations,max_limit,expected_results",
        [
            ([(1, 1)] * 11, 10, [[(1, 1)] * 10, [(1, 1)]]),
            ([(1, 1)] * 10, 1, [[(1, 1)] for _ in range(10)]),
            ([(1, 1)] * 10, 2, [[(1, 1), (1, 1)] for _ in range(5)]),
        ],
    )
    async def test_add_to_flow_max_mutation_limits(
        self, mutations, max_limit, expected_results
    ):
        """
        Test flow control running up against the max API limit
        Should submit request early, even if the flow control has room for more
        """
        subpath = "_async" if CrossSync.is_async else "_sync_autogen"
        path = f"google.cloud.bigtable.data.{subpath}.mutations_batcher._MUTATE_ROWS_REQUEST_MUTATION_LIMIT"
        with mock.patch(path, max_limit):
            mutation_objs = [
                self._make_mutation(count=m[0], size=m[1]) for m in mutations
            ]
            # flow control has no limits except API restrictions
            instance = self._make_one(float("inf"), float("inf"))
            i = 0
            async for batch in instance.add_to_flow(mutation_objs):
                expected_batch = expected_results[i]
                assert len(batch) == len(expected_batch)
                for j in range(len(expected_batch)):
                    # check counts
                    assert len(batch[j].mutations) == expected_batch[j][0]
                    # check sizes
                    assert batch[j].size() == expected_batch[j][1]
                # update lock
                await instance.remove_from_flow(batch)
                i += 1
            assert i == len(expected_results)

    @CrossSync.pytest
    async def test_add_to_flow_oversize(self):
        """
        mutations over the flow control limits should still be accepted
        """
        instance = self._make_one(2, 3)
        large_size_mutation = self._make_mutation(count=1, size=10)
        large_count_mutation = self._make_mutation(count=10, size=1)
        results = [out async for out in instance.add_to_flow([large_size_mutation])]
        assert len(results) == 1
        await instance.remove_from_flow(results[0])
        count_results = [
            out async for out in instance.add_to_flow(large_count_mutation)
        ]
        assert len(count_results) == 1


@CrossSync.convert_class(sync_name="TestMutationsBatcher")
class TestMutationsBatcherAsync:
    @CrossSync.convert
    def _get_target_class(self):
        return CrossSync.MutationsBatcher

    def _make_one(self, table=None, **kwargs):
        from google.api_core.exceptions import DeadlineExceeded
        from google.api_core.exceptions import ServiceUnavailable

        if table is None:
            table = mock.Mock()
            table._request_path = {"table_name": "table"}
            table.app_profile_id = None
            table.default_mutate_rows_operation_timeout = 10
            table.default_mutate_rows_attempt_timeout = 10
            table.default_mutate_rows_retryable_errors = (
                DeadlineExceeded,
                ServiceUnavailable,
            )

        return self._get_target_class()(table, **kwargs)

    @staticmethod
    def _make_mutation(count=1, size=1):
        mutation = RowMutationEntry("k", DeleteAllFromRow())
        mutation.size = lambda: size
        mutation.mutations = [DeleteAllFromRow() for _ in range(count)]
        return mutation

    @CrossSync.pytest
    async def test_ctor_defaults(self):
        with mock.patch.object(
            self._get_target_class(), "_timer_routine", return_value=CrossSync.Future()
        ) as flush_timer_mock:
            table = mock.Mock()
            table.default_mutate_rows_operation_timeout = 10
            table.default_mutate_rows_attempt_timeout = 8
            table.default_mutate_rows_retryable_errors = [Exception]
            async with self._make_one(table) as instance:
                assert instance._target == table
                assert instance.closed is False
                assert instance._flush_jobs == set()
                assert len(instance._staged_entries) == 0
                assert len(instance._oldest_exceptions) == 0
                assert len(instance._newest_exceptions) == 0
                assert instance._exception_list_limit == 10
                assert instance._exceptions_since_last_raise == 0
                assert instance._flow_control._max_mutation_count == 100000
                assert instance._flow_control._max_mutation_bytes == 104857600
                assert instance._flow_control._in_flight_mutation_count == 0
                assert instance._flow_control._in_flight_mutation_bytes == 0
                assert instance._entries_processed_since_last_raise == 0
                assert (
                    instance._operation_timeout
                    == table.default_mutate_rows_operation_timeout
                )
                assert (
                    instance._attempt_timeout
                    == table.default_mutate_rows_attempt_timeout
                )
                assert (
                    instance._retryable_errors
                    == table.default_mutate_rows_retryable_errors
                )
                await CrossSync.yield_to_event_loop()
                assert flush_timer_mock.call_count == 1
                assert flush_timer_mock.call_args[0][0] == 5
                assert isinstance(instance._flush_timer, CrossSync.Future)

    @CrossSync.pytest
    async def test_ctor_explicit(self):
        """Test with explicit parameters"""
        with mock.patch.object(
            self._get_target_class(), "_timer_routine", return_value=CrossSync.Future()
        ) as flush_timer_mock:
            table = mock.Mock()
            flush_interval = 20
            flush_limit_count = 17
            flush_limit_bytes = 19
            flow_control_max_mutation_count = 1001
            flow_control_max_bytes = 12
            operation_timeout = 11
            attempt_timeout = 2
            retryable_errors = [Exception]
            async with self._make_one(
                table,
                flush_interval=flush_interval,
                flush_limit_mutation_count=flush_limit_count,
                flush_limit_bytes=flush_limit_bytes,
                flow_control_max_mutation_count=flow_control_max_mutation_count,
                flow_control_max_bytes=flow_control_max_bytes,
                batch_operation_timeout=operation_timeout,
                batch_attempt_timeout=attempt_timeout,
                batch_retryable_errors=retryable_errors,
            ) as instance:
                assert instance._target == table
                assert instance.closed is False
                assert instance._flush_jobs == set()
                assert len(instance._staged_entries) == 0
                assert len(instance._oldest_exceptions) == 0
                assert len(instance._newest_exceptions) == 0
                assert instance._exception_list_limit == 10
                assert instance._exceptions_since_last_raise == 0
                assert (
                    instance._flow_control._max_mutation_count
                    == flow_control_max_mutation_count
                )
                assert (
                    instance._flow_control._max_mutation_bytes == flow_control_max_bytes
                )
                assert instance._flow_control._in_flight_mutation_count == 0
                assert instance._flow_control._in_flight_mutation_bytes == 0
                assert instance._entries_processed_since_last_raise == 0
                assert instance._operation_timeout == operation_timeout
                assert instance._attempt_timeout == attempt_timeout
                assert instance._retryable_errors == retryable_errors
                await CrossSync.yield_to_event_loop()
                assert flush_timer_mock.call_count == 1
                assert flush_timer_mock.call_args[0][0] == flush_interval
                assert isinstance(instance._flush_timer, CrossSync.Future)

    @CrossSync.pytest
    async def test_ctor_no_flush_limits(self):
        """Test with None for flush limits"""
        with mock.patch.object(
            self._get_target_class(), "_timer_routine", return_value=CrossSync.Future()
        ) as flush_timer_mock:
            table = mock.Mock()
            table.default_mutate_rows_operation_timeout = 10
            table.default_mutate_rows_attempt_timeout = 8
            table.default_mutate_rows_retryable_errors = ()
            flush_interval = None
            flush_limit_count = None
            flush_limit_bytes = None
            async with self._make_one(
                table,
                flush_interval=flush_interval,
                flush_limit_mutation_count=flush_limit_count,
                flush_limit_bytes=flush_limit_bytes,
            ) as instance:
                assert instance._target == table
                assert instance.closed is False
                assert instance._staged_entries == []
                assert len(instance._oldest_exceptions) == 0
                assert len(instance._newest_exceptions) == 0
                assert instance._exception_list_limit == 10
                assert instance._exceptions_since_last_raise == 0
                assert instance._flow_control._in_flight_mutation_count == 0
                assert instance._flow_control._in_flight_mutation_bytes == 0
                assert instance._entries_processed_since_last_raise == 0
                await CrossSync.yield_to_event_loop()
                assert flush_timer_mock.call_count == 1
                assert flush_timer_mock.call_args[0][0] is None
                assert isinstance(instance._flush_timer, CrossSync.Future)

    @CrossSync.pytest
    async def test_ctor_invalid_values(self):
        """Test that timeout values are positive, and fit within expected limits"""
        with pytest.raises(ValueError) as e:
            self._make_one(batch_operation_timeout=-1)
        assert "operation_timeout must be greater than 0" in str(e.value)
        with pytest.raises(ValueError) as e:
            self._make_one(batch_attempt_timeout=-1)
        assert "attempt_timeout must be greater than 0" in str(e.value)

    @CrossSync.convert
    def test_default_argument_consistency(self):
        """
        We supply default arguments in MutationsBatcherAsync.__init__, and in
        table.mutations_batcher. Make sure any changes to defaults are applied to
        both places
        """
        import inspect

        get_batcher_signature = dict(
            inspect.signature(CrossSync.Table.mutations_batcher).parameters
        )
        get_batcher_signature.pop("self")
        batcher_init_signature = dict(
            inspect.signature(self._get_target_class()).parameters
        )
        batcher_init_signature.pop("table")
        # both should have same number of arguments
        assert len(get_batcher_signature.keys()) == len(batcher_init_signature.keys())
        assert len(get_batcher_signature) == 8  # update if expected params change
        # both should have same argument names
        assert set(get_batcher_signature.keys()) == set(batcher_init_signature.keys())
        # both should have same default values
        for arg_name in get_batcher_signature.keys():
            assert (
                get_batcher_signature[arg_name].default
                == batcher_init_signature[arg_name].default
            )

    @CrossSync.pytest
    @pytest.mark.parametrize("input_val", [None, 0, -1])
    async def test__start_flush_timer_w_empty_input(self, input_val):
        """Empty/invalid timer should return immediately"""
        with mock.patch.object(
            self._get_target_class(), "_schedule_flush"
        ) as flush_mock:
            # mock different method depending on sync vs async
            async with self._make_one() as instance:
                if CrossSync.is_async:
                    sleep_obj, sleep_method = asyncio, "wait_for"
                else:
                    sleep_obj, sleep_method = instance._closed, "wait"
                with mock.patch.object(sleep_obj, sleep_method) as sleep_mock:
                    result = await instance._timer_routine(input_val)
                    assert sleep_mock.call_count == 0
                    assert flush_mock.call_count == 0
                    assert result is None

    @CrossSync.pytest
    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    async def test__start_flush_timer_call_when_closed(
        self,
    ):
        """closed batcher's timer should return immediately"""
        with mock.patch.object(
            self._get_target_class(), "_schedule_flush"
        ) as flush_mock:
            async with self._make_one() as instance:
                await instance.close()
                flush_mock.reset_mock()
                # mock different method depending on sync vs async
                if CrossSync.is_async:
                    sleep_obj, sleep_method = asyncio, "wait_for"
                else:
                    sleep_obj, sleep_method = instance._closed, "wait"
                with mock.patch.object(sleep_obj, sleep_method) as sleep_mock:
                    await instance._timer_routine(10)
                    assert sleep_mock.call_count == 0
                    assert flush_mock.call_count == 0

    @CrossSync.pytest
    @pytest.mark.parametrize("num_staged", [0, 1, 10])
    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    async def test__flush_timer(self, num_staged):
        """Timer should continue to call _schedule_flush in a loop"""
        from google.cloud.bigtable.data._cross_sync import CrossSync

        with mock.patch.object(
            self._get_target_class(), "_schedule_flush"
        ) as flush_mock:
            expected_sleep = 12
            async with self._make_one(flush_interval=expected_sleep) as instance:
                loop_num = 3
                instance._staged_entries = [mock.Mock()] * num_staged
                with mock.patch.object(CrossSync, "event_wait") as sleep_mock:
                    sleep_mock.side_effect = [None] * loop_num + [TabError("expected")]
                    with pytest.raises(TabError):
                        await self._get_target_class()._timer_routine(
                            instance, expected_sleep
                        )
                    if CrossSync.is_async:
                        # replace with np-op so there are no issues on close
                        instance._flush_timer = CrossSync.Future()
                    assert sleep_mock.call_count == loop_num + 1
                    sleep_kwargs = sleep_mock.call_args[1]
                    assert sleep_kwargs["timeout"] == expected_sleep
                    assert flush_mock.call_count == (0 if num_staged == 0 else loop_num)

    @CrossSync.pytest
    async def test__flush_timer_close(self):
        """Timer should continue terminate after close"""
        with mock.patch.object(self._get_target_class(), "_schedule_flush"):
            async with self._make_one() as instance:
                # let task run in background
                assert instance._flush_timer.done() is False
                # close the batcher
                await instance.close()
                # task should be complete
                assert instance._flush_timer.done() is True

    @CrossSync.pytest
    async def test_append_closed(self):
        """Should raise exception"""
        instance = self._make_one()
        await instance.close()
        with pytest.raises(RuntimeError):
            await instance.append(mock.Mock())

    @CrossSync.pytest
    async def test_append_wrong_mutation(self):
        """
        Mutation objects should raise an exception.
        Only support RowMutationEntry
        """
        from google.cloud.bigtable.data.mutations import DeleteAllFromRow

        async with self._make_one() as instance:
            expected_error = "invalid mutation type: DeleteAllFromRow. Only RowMutationEntry objects are supported by batcher"
            with pytest.raises(ValueError) as e:
                await instance.append(DeleteAllFromRow())
            assert str(e.value) == expected_error

    @CrossSync.pytest
    async def test_append_outside_flow_limits(self):
        """entries larger than mutation limits are still processed"""
        async with self._make_one(
            flow_control_max_mutation_count=1, flow_control_max_bytes=1
        ) as instance:
            oversized_entry = self._make_mutation(count=0, size=2)
            await instance.append(oversized_entry)
            assert instance._staged_entries == [oversized_entry]
            assert instance._staged_count == 0
            assert instance._staged_bytes == 2
            instance._staged_entries = []
        async with self._make_one(
            flow_control_max_mutation_count=1, flow_control_max_bytes=1
        ) as instance:
            overcount_entry = self._make_mutation(count=2, size=0)
            await instance.append(overcount_entry)
            assert instance._staged_entries == [overcount_entry]
            assert instance._staged_count == 2
            assert instance._staged_bytes == 0
            instance._staged_entries = []

    @CrossSync.pytest
    async def test_append_flush_runs_after_limit_hit(self):
        """
        If the user appends a bunch of entries above the flush limits back-to-back,
        it should still flush in a single task
        """
        with mock.patch.object(
            self._get_target_class(), "_execute_mutate_rows"
        ) as op_mock:
            async with self._make_one(flush_limit_bytes=100) as instance:
                # mock network calls
                async def mock_call(*args, **kwargs):
                    return []

                op_mock.side_effect = mock_call
                # append a mutation just under the size limit
                await instance.append(self._make_mutation(size=99))
                # append a bunch of entries back-to-back in a loop
                num_entries = 10
                for _ in range(num_entries):
                    await instance.append(self._make_mutation(size=1))
                # let any flush jobs finish
                await instance._wait_for_batch_results(*instance._flush_jobs)
                # should have only flushed once, with large mutation and first mutation in loop
                assert op_mock.call_count == 1
                sent_batch = op_mock.call_args[0][0]
                assert len(sent_batch) == 2
                # others should still be pending
                assert len(instance._staged_entries) == num_entries - 1

    @pytest.mark.parametrize(
        "flush_count,flush_bytes,mutation_count,mutation_bytes,expect_flush",
        [
            (10, 10, 1, 1, False),
            (10, 10, 9, 9, False),
            (10, 10, 10, 1, True),
            (10, 10, 1, 10, True),
            (10, 10, 10, 10, True),
            (1, 1, 10, 10, True),
            (1, 1, 0, 0, False),
        ],
    )
    @CrossSync.pytest
    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    async def test_append(
        self, flush_count, flush_bytes, mutation_count, mutation_bytes, expect_flush
    ):
        """test appending different mutations, and checking if it causes a flush"""
        async with self._make_one(
            flush_limit_mutation_count=flush_count, flush_limit_bytes=flush_bytes
        ) as instance:
            assert instance._staged_count == 0
            assert instance._staged_bytes == 0
            assert instance._staged_entries == []
            mutation = self._make_mutation(count=mutation_count, size=mutation_bytes)
            with mock.patch.object(instance, "_schedule_flush") as flush_mock:
                await instance.append(mutation)
            assert flush_mock.call_count == bool(expect_flush)
            assert instance._staged_count == mutation_count
            assert instance._staged_bytes == mutation_bytes
            assert instance._staged_entries == [mutation]
            instance._staged_entries = []

    @CrossSync.pytest
    async def test_append_multiple_sequentially(self):
        """Append multiple mutations"""
        async with self._make_one(
            flush_limit_mutation_count=8, flush_limit_bytes=8
        ) as instance:
            assert instance._staged_count == 0
            assert instance._staged_bytes == 0
            assert instance._staged_entries == []
            mutation = self._make_mutation(count=2, size=3)
            with mock.patch.object(instance, "_schedule_flush") as flush_mock:
                await instance.append(mutation)
                assert flush_mock.call_count == 0
                assert instance._staged_count == 2
                assert instance._staged_bytes == 3
                assert len(instance._staged_entries) == 1
                await instance.append(mutation)
                assert flush_mock.call_count == 0
                assert instance._staged_count == 4
                assert instance._staged_bytes == 6
                assert len(instance._staged_entries) == 2
                await instance.append(mutation)
                assert flush_mock.call_count == 1
                assert instance._staged_count == 6
                assert instance._staged_bytes == 9
                assert len(instance._staged_entries) == 3
            instance._staged_entries = []

    @CrossSync.pytest
    async def test_flush_flow_control_concurrent_requests(self):
        """
        requests should happen in parallel if flow control breaks up single flush into batches
        """
        import time

        num_calls = 10
        fake_mutations = [self._make_mutation(count=1) for _ in range(num_calls)]
        async with self._make_one(flow_control_max_mutation_count=1) as instance:
            with mock.patch.object(
                instance, "_execute_mutate_rows", CrossSync.Mock()
            ) as op_mock:
                # mock network calls
                async def mock_call(*args, **kwargs):
                    await CrossSync.sleep(0.1)
                    return []

                op_mock.side_effect = mock_call
                start_time = time.monotonic()
                # flush one large batch, that will be broken up into smaller batches
                instance._staged_entries = fake_mutations
                instance._schedule_flush()
                await CrossSync.sleep(0.01)
                # make room for new mutations
                for i in range(num_calls):
                    await instance._flow_control.remove_from_flow(
                        [self._make_mutation(count=1)]
                    )
                    await CrossSync.sleep(0.01)
                # allow flushes to complete
                await instance._wait_for_batch_results(*instance._flush_jobs)
                duration = time.monotonic() - start_time
                assert len(instance._oldest_exceptions) == 0
                assert len(instance._newest_exceptions) == 0
                # if flushes were sequential, total duration would be 1s
                assert duration < 0.5
                assert op_mock.call_count == num_calls

    @CrossSync.pytest
    async def test_schedule_flush_no_mutations(self):
        """schedule flush should return None if no staged mutations"""
        async with self._make_one() as instance:
            with mock.patch.object(instance, "_flush_internal") as flush_mock:
                for i in range(3):
                    assert instance._schedule_flush() is None
                    assert flush_mock.call_count == 0

    @CrossSync.pytest
    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    async def test_schedule_flush_with_mutations(self):
        """if new mutations exist, should add a new flush task to _flush_jobs"""
        async with self._make_one() as instance:
            with mock.patch.object(instance, "_flush_internal") as flush_mock:
                if not CrossSync.is_async:
                    # simulate operation
                    flush_mock.side_effect = lambda x: time.sleep(0.1)
                for i in range(1, 4):
                    mutation = mock.Mock()
                    instance._staged_entries = [mutation]
                    instance._schedule_flush()
                    assert instance._staged_entries == []
                    # let flush task run
                    await asyncio.sleep(0)
                    assert instance._staged_entries == []
                    assert instance._staged_count == 0
                    assert instance._staged_bytes == 0
                    assert flush_mock.call_count == 1
                    flush_mock.reset_mock()

    @CrossSync.pytest
    async def test__flush_internal(self):
        """
        _flush_internal should:
          - await previous flush call
          - delegate batching to _flow_control
          - call _execute_mutate_rows on each batch
          - update self.exceptions and self._entries_processed_since_last_raise
        """
        num_entries = 10
        async with self._make_one() as instance:
            with mock.patch.object(instance, "_execute_mutate_rows") as execute_mock:
                with mock.patch.object(
                    instance._flow_control, "add_to_flow"
                ) as flow_mock:
                    # mock flow control to always return a single batch
                    async def gen(x):
                        yield x

                    flow_mock.side_effect = lambda x: gen(x)
                    mutations = [self._make_mutation(count=1, size=1)] * num_entries
                    await instance._flush_internal(mutations)
                    assert instance._entries_processed_since_last_raise == num_entries
                    assert execute_mock.call_count == 1
                    assert flow_mock.call_count == 1
                    instance._oldest_exceptions.clear()
                    instance._newest_exceptions.clear()

    @CrossSync.pytest
    async def test_flush_clears_job_list(self):
        """
        a job should be added to _flush_jobs when _schedule_flush is called,
        and removed when it completes
        """
        async with self._make_one() as instance:
            with mock.patch.object(
                instance, "_flush_internal", CrossSync.Mock()
            ) as flush_mock:
                if not CrossSync.is_async:
                    # simulate operation
                    flush_mock.side_effect = lambda x: time.sleep(0.1)
                mutations = [self._make_mutation(count=1, size=1)]
                instance._staged_entries = mutations
                assert instance._flush_jobs == set()
                new_job = instance._schedule_flush()
                assert instance._flush_jobs == {new_job}
                if CrossSync.is_async:
                    await new_job
                else:
                    new_job.result()
                assert instance._flush_jobs == set()

    @pytest.mark.parametrize(
        "num_starting,num_new_errors,expected_total_errors",
        [
            (0, 0, 0),
            (0, 1, 1),
            (0, 2, 2),
            (1, 0, 1),
            (1, 1, 2),
            (10, 2, 12),
            (10, 20, 20),  # should cap at 20
        ],
    )
    @CrossSync.pytest
    async def test__flush_internal_with_errors(
        self, num_starting, num_new_errors, expected_total_errors
    ):
        """
        errors returned from _execute_mutate_rows should be added to internal exceptions
        """
        from google.cloud.bigtable.data import exceptions

        num_entries = 10
        expected_errors = [
            exceptions.FailedMutationEntryError(mock.Mock(), mock.Mock(), ValueError())
        ] * num_new_errors
        async with self._make_one() as instance:
            instance._oldest_exceptions = [mock.Mock()] * num_starting
            with mock.patch.object(instance, "_execute_mutate_rows") as execute_mock:
                execute_mock.return_value = expected_errors
                with mock.patch.object(
                    instance._flow_control, "add_to_flow"
                ) as flow_mock:
                    # mock flow control to always return a single batch
                    async def gen(x):
                        yield x

                    flow_mock.side_effect = lambda x: gen(x)
                    mutations = [self._make_mutation(count=1, size=1)] * num_entries
                    await instance._flush_internal(mutations)
                    assert instance._entries_processed_since_last_raise == num_entries
                    assert execute_mock.call_count == 1
                    assert flow_mock.call_count == 1
                    found_exceptions = instance._oldest_exceptions + list(
                        instance._newest_exceptions
                    )
                    assert len(found_exceptions) == expected_total_errors
                    for i in range(num_starting, expected_total_errors):
                        assert found_exceptions[i] == expected_errors[i - num_starting]
                        # errors should have index stripped
                        assert found_exceptions[i].index is None
            # clear out exceptions
            instance._oldest_exceptions.clear()
            instance._newest_exceptions.clear()

    @CrossSync.convert
    async def _mock_gapic_return(self, num=5):
        from google.cloud.bigtable_v2.types import MutateRowsResponse
        from google.rpc import status_pb2

        @CrossSync.convert
        async def gen(num):
            for i in range(num):
                entry = MutateRowsResponse.Entry(
                    index=i, status=status_pb2.Status(code=0)
                )
                yield MutateRowsResponse(entries=[entry])

        return gen(num)

    @CrossSync.pytest
    async def test_timer_flush_end_to_end(self):
        """Flush should automatically trigger after flush_interval"""
        num_mutations = 10
        mutations = [self._make_mutation(count=2, size=2)] * num_mutations

        async with self._make_one(flush_interval=0.05) as instance:
            instance._target.default_operation_timeout = 10
            instance._target.default_attempt_timeout = 9
            with mock.patch.object(
                instance._target.client._gapic_client, "mutate_rows"
            ) as gapic_mock:
                gapic_mock.side_effect = (
                    lambda *args, **kwargs: self._mock_gapic_return(num_mutations)
                )
                for m in mutations:
                    await instance.append(m)
                assert instance._entries_processed_since_last_raise == 0
                # let flush trigger due to timer
                await CrossSync.sleep(0.1)
                assert instance._entries_processed_since_last_raise == num_mutations

    @CrossSync.pytest
    async def test__execute_mutate_rows(self):
        with mock.patch.object(CrossSync, "_MutateRowsOperation") as mutate_rows:
            mutate_rows.return_value = CrossSync.Mock()
            start_operation = mutate_rows().start
            table = mock.Mock()
            table.table_name = "test-table"
            table.app_profile_id = "test-app-profile"
            table.default_mutate_rows_operation_timeout = 17
            table.default_mutate_rows_attempt_timeout = 13
            table.default_mutate_rows_retryable_errors = ()
            async with self._make_one(table) as instance:
                batch = [self._make_mutation()]
                result = await instance._execute_mutate_rows(batch)
                assert start_operation.call_count == 1
                args, kwargs = mutate_rows.call_args
                assert args[0] == table.client._gapic_client
                assert args[1] == table
                assert args[2] == batch
                kwargs["operation_timeout"] == 17
                kwargs["attempt_timeout"] == 13
                assert result == []

    @CrossSync.pytest
    async def test__execute_mutate_rows_returns_errors(self):
        """Errors from operation should be retruned as list"""
        from google.cloud.bigtable.data.exceptions import (
            MutationsExceptionGroup,
            FailedMutationEntryError,
        )

        with mock.patch.object(CrossSync._MutateRowsOperation, "start") as mutate_rows:
            err1 = FailedMutationEntryError(0, mock.Mock(), RuntimeError("test error"))
            err2 = FailedMutationEntryError(1, mock.Mock(), RuntimeError("test error"))
            mutate_rows.side_effect = MutationsExceptionGroup([err1, err2], 10)
            table = mock.Mock()
            table.default_mutate_rows_operation_timeout = 17
            table.default_mutate_rows_attempt_timeout = 13
            table.default_mutate_rows_retryable_errors = ()
            async with self._make_one(table) as instance:
                batch = [self._make_mutation()]
                result = await instance._execute_mutate_rows(batch)
                assert len(result) == 2
                assert result[0] == err1
                assert result[1] == err2
                # indices should be set to None
                assert result[0].index is None
                assert result[1].index is None

    @CrossSync.pytest
    async def test__raise_exceptions(self):
        """Raise exceptions and reset error state"""
        from google.cloud.bigtable.data import exceptions

        expected_total = 1201
        expected_exceptions = [RuntimeError("mock")] * 3
        async with self._make_one() as instance:
            instance._oldest_exceptions = expected_exceptions
            instance._entries_processed_since_last_raise = expected_total
            try:
                instance._raise_exceptions()
            except exceptions.MutationsExceptionGroup as exc:
                assert list(exc.exceptions) == expected_exceptions
                assert str(expected_total) in str(exc)
            assert instance._entries_processed_since_last_raise == 0
            instance._oldest_exceptions, instance._newest_exceptions = ([], [])
            # try calling again
            instance._raise_exceptions()

    @CrossSync.pytest
    @CrossSync.convert(
        sync_name="test___enter__", replace_symbols={"__aenter__": "__enter__"}
    )
    async def test___aenter__(self):
        """Should return self"""
        async with self._make_one() as instance:
            assert await instance.__aenter__() == instance

    @CrossSync.pytest
    @CrossSync.convert(
        sync_name="test___exit__", replace_symbols={"__aexit__": "__exit__"}
    )
    async def test___aexit__(self):
        """aexit should call close"""
        async with self._make_one() as instance:
            with mock.patch.object(instance, "close") as close_mock:
                await instance.__aexit__(None, None, None)
                assert close_mock.call_count == 1

    @CrossSync.pytest
    async def test_close(self):
        """Should clean up all resources"""
        async with self._make_one() as instance:
            with mock.patch.object(instance, "_schedule_flush") as flush_mock:
                with mock.patch.object(instance, "_raise_exceptions") as raise_mock:
                    await instance.close()
                    assert instance.closed is True
                    assert instance._flush_timer.done() is True
                    assert instance._flush_jobs == set()
                    assert flush_mock.call_count == 1
                    assert raise_mock.call_count == 1

    @CrossSync.pytest
    async def test_close_w_exceptions(self):
        """Raise exceptions on close"""
        from google.cloud.bigtable.data import exceptions

        expected_total = 10
        expected_exceptions = [RuntimeError("mock")]
        async with self._make_one() as instance:
            instance._oldest_exceptions = expected_exceptions
            instance._entries_processed_since_last_raise = expected_total
            try:
                await instance.close()
            except exceptions.MutationsExceptionGroup as exc:
                assert list(exc.exceptions) == expected_exceptions
                assert str(expected_total) in str(exc)
            assert instance._entries_processed_since_last_raise == 0
            # clear out exceptions
            instance._oldest_exceptions, instance._newest_exceptions = ([], [])

    @CrossSync.pytest
    async def test__on_exit(self, recwarn):
        """Should raise warnings if unflushed mutations exist"""
        async with self._make_one() as instance:
            # calling without mutations is noop
            instance._on_exit()
            assert len(recwarn) == 0
            # calling with existing mutations should raise warning
            num_left = 4
            instance._staged_entries = [mock.Mock()] * num_left
            with pytest.warns(UserWarning) as w:
                instance._on_exit()
                assert len(w) == 1
                assert "unflushed mutations" in str(w[0].message).lower()
                assert str(num_left) in str(w[0].message)
            # calling while closed is noop
            instance._closed.set()
            instance._on_exit()
            assert len(recwarn) == 0
            # reset staged mutations for cleanup
            instance._staged_entries = []

    @CrossSync.pytest
    async def test_atexit_registration(self):
        """Should run _on_exit on program termination"""
        import atexit

        with mock.patch.object(atexit, "register") as register_mock:
            assert register_mock.call_count == 0
            async with self._make_one():
                assert register_mock.call_count == 1

    @CrossSync.pytest
    async def test_timeout_args_passed(self):
        """
        batch_operation_timeout and batch_attempt_timeout should be used
        in api calls
        """
        with mock.patch.object(
            CrossSync, "_MutateRowsOperation", return_value=CrossSync.Mock()
        ) as mutate_rows:
            expected_operation_timeout = 17
            expected_attempt_timeout = 13
            async with self._make_one(
                batch_operation_timeout=expected_operation_timeout,
                batch_attempt_timeout=expected_attempt_timeout,
            ) as instance:
                assert instance._operation_timeout == expected_operation_timeout
                assert instance._attempt_timeout == expected_attempt_timeout
                # make simulated gapic call
                await instance._execute_mutate_rows([self._make_mutation()])
                assert mutate_rows.call_count == 1
                kwargs = mutate_rows.call_args[1]
                assert kwargs["operation_timeout"] == expected_operation_timeout
                assert kwargs["attempt_timeout"] == expected_attempt_timeout

    @pytest.mark.parametrize(
        "limit,in_e,start_e,end_e",
        [
            (10, 0, (10, 0), (10, 0)),
            (1, 10, (0, 0), (1, 1)),
            (10, 1, (0, 0), (1, 0)),
            (10, 10, (0, 0), (10, 0)),
            (10, 11, (0, 0), (10, 1)),
            (3, 20, (0, 0), (3, 3)),
            (10, 20, (0, 0), (10, 10)),
            (10, 21, (0, 0), (10, 10)),
            (2, 1, (2, 0), (2, 1)),
            (2, 1, (1, 0), (2, 0)),
            (2, 2, (1, 0), (2, 1)),
            (3, 1, (3, 1), (3, 2)),
            (3, 3, (3, 1), (3, 3)),
            (1000, 5, (999, 0), (1000, 4)),
            (1000, 5, (0, 0), (5, 0)),
            (1000, 5, (1000, 0), (1000, 5)),
        ],
    )
    def test__add_exceptions(self, limit, in_e, start_e, end_e):
        """
        Test that the _add_exceptions function properly updates the
        _oldest_exceptions and _newest_exceptions lists
        Args:
          - limit: the _exception_list_limit representing the max size of either list
          - in_e: size of list of exceptions to send to _add_exceptions
          - start_e: a tuple of ints representing the initial sizes of _oldest_exceptions and _newest_exceptions
          - end_e: a tuple of ints representing the expected sizes of _oldest_exceptions and _newest_exceptions
        """
        from collections import deque

        input_list = [RuntimeError(f"mock {i}") for i in range(in_e)]
        mock_batcher = mock.Mock()
        mock_batcher._oldest_exceptions = [
            RuntimeError(f"starting mock {i}") for i in range(start_e[0])
        ]
        mock_batcher._newest_exceptions = deque(
            [RuntimeError(f"starting mock {i}") for i in range(start_e[1])],
            maxlen=limit,
        )
        mock_batcher._exception_list_limit = limit
        mock_batcher._exceptions_since_last_raise = 0
        self._get_target_class()._add_exceptions(mock_batcher, input_list)
        assert len(mock_batcher._oldest_exceptions) == end_e[0]
        assert len(mock_batcher._newest_exceptions) == end_e[1]
        assert mock_batcher._exceptions_since_last_raise == in_e
        # make sure that the right items ended up in the right spots
        # should fill the oldest slots first
        oldest_list_diff = end_e[0] - start_e[0]
        # new items should by added on top of the starting list
        newest_list_diff = min(max(in_e - oldest_list_diff, 0), limit)
        for i in range(oldest_list_diff):
            assert mock_batcher._oldest_exceptions[i + start_e[0]] == input_list[i]
        # then, the newest slots should be filled with the last items of the input list
        for i in range(1, newest_list_diff + 1):
            assert mock_batcher._newest_exceptions[-i] == input_list[-i]

    @CrossSync.pytest
    # test different inputs for retryable exceptions
    @pytest.mark.parametrize(
        "input_retryables,expected_retryables",
        [
            (
                TABLE_DEFAULT.READ_ROWS,
                [
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                    core_exceptions.Aborted,
                ],
            ),
            (
                TABLE_DEFAULT.DEFAULT,
                [core_exceptions.DeadlineExceeded, core_exceptions.ServiceUnavailable],
            ),
            (
                TABLE_DEFAULT.MUTATE_ROWS,
                [core_exceptions.DeadlineExceeded, core_exceptions.ServiceUnavailable],
            ),
            ([], []),
            ([4], [core_exceptions.DeadlineExceeded]),
        ],
    )
    @CrossSync.convert
    async def test_customizable_retryable_errors(
        self, input_retryables, expected_retryables
    ):
        """
        Test that retryable functions support user-configurable arguments, and that the configured retryables are passed
        down to the gapic layer.
        """
        with mock.patch.object(
            google.api_core.retry, "if_exception_type"
        ) as predicate_builder_mock:
            with mock.patch.object(CrossSync, "retry_target") as retry_fn_mock:
                table = None
                with mock.patch("asyncio.create_task"):
                    table = CrossSync.Table(mock.Mock(), "instance", "table")
                async with self._make_one(
                    table, batch_retryable_errors=input_retryables
                ) as instance:
                    assert instance._retryable_errors == expected_retryables
                    expected_predicate = expected_retryables.__contains__
                    predicate_builder_mock.return_value = expected_predicate
                    retry_fn_mock.side_effect = RuntimeError("stop early")
                    mutation = self._make_mutation(count=1, size=1)
                    await instance._execute_mutate_rows([mutation])
                    # passed in errors should be used to build the predicate
                    predicate_builder_mock.assert_called_once_with(
                        *expected_retryables, _MutateRowsIncomplete
                    )
                    retry_call_args = retry_fn_mock.call_args_list[0].args
                    # output of if_exception_type should be sent in to retry constructor
                    assert retry_call_args[1] is expected_predicate

    @CrossSync.pytest
    async def test_large_batch_write(self):
        """
        Test that a large batch of mutations can be written
        """
        import math

        num_mutations = 10_000
        flush_limit = 1000
        mutations = [self._make_mutation(count=1, size=1)] * num_mutations
        async with self._make_one(flush_limit_mutation_count=flush_limit) as instance:
            operation_mock = mock.Mock()
            rpc_call_mock = CrossSync.Mock()
            operation_mock().start = rpc_call_mock
            CrossSync._MutateRowsOperation = operation_mock
            for m in mutations:
                await instance.append(m)
        expected_calls = math.ceil(num_mutations / flush_limit)
        assert rpc_call_mock.call_count == expected_calls
        assert instance._entries_processed_since_last_raise == num_mutations
        assert len(instance._staged_entries) == 0
