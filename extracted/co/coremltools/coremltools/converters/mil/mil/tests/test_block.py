#  Copyright (c) 2020, Apple Inc. All rights reserved.
#
#  Use of this source code is governed by a BSD-3-clause license that can be
#  found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause

import copy

import numpy as np
import pytest

from coremltools.converters.mil.mil import Builder as mb
from coremltools.converters.mil.mil.passes.tests.test_passes import CONSTEXPR_FUNCS
from coremltools.converters.mil.mil.utils import CacheDoublyLinkedList
from coremltools.converters.mil.testing_utils import (
    assert_same_output_names,
    assert_same_output_shapes,
    get_op_types_in_program,
)

"""
Test manipulating variable and operations in the Block.

In the test, we are actually testing Function, which is a child class of
Block. Technically Function should not inherit from Block, which is a
debt to be resolved in the future.

Function has some different behaviors from Block that are irrelevant to
the core API being tested here.
"""

def test_empty_block():
    """
    Test an empty program
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        return x0

    block = prog.functions["main"]
    assert len(block.operations) == 0
    assert len(block.inputs) == 1
    assert len(block.outputs) == 1
    assert block.inputs["x0"] == block.outputs[0]


def test_add_op():
    """
    Test add statement to an empty program, also change the output
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        return x0

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    x0 = block.inputs["x0"]
    with block:
        x1 = mb.log(x=x0)
    block.set_outputs([x1])
    print("after:\n{}".format(prog))
    assert block.inputs["x0"] == block.find_ops(op_type="log")[0].inputs["x"]
    assert len(block.operations) == 2 # const op for epsilon + log
    assert list(block.operations)[1].op_type == "log"
    assert block.outputs[0] == x1


def test_remove_op():
    """
    Test remove all ops and return empty program
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.log(x=x0)
        return x1

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    assert len(block.operations) == 2
    x0 = block.inputs["x0"]
    ops = block.find_ops(op_type="log")
    block.set_outputs([x0])
    block.remove_ops(ops)
    print("after:\n{}".format(prog))
    assert len(block.operations) == 1
    assert len(block.inputs) == 1
    assert len(block.outputs) == 1
    assert block.inputs["x0"] == block.outputs[0]


def test_remove_op2():
    """
    Test remove ops with multiple identical inputs
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.add(x=x0, y=x0)
        return x1

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    x0 = block.inputs["x0"]
    ops = block.find_ops(op_type="add")
    block.set_outputs([x0])
    block.remove_ops(ops)
    print("after:\n{}".format(prog))
    assert len(block.operations) == 0
    assert len(block.inputs) == 1
    assert len(block.outputs) == 1
    assert block.inputs["x0"] == block.outputs[0]


def test_remove_duplicate_ops():
    """Test remove duplicated ops."""

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.add(x=x0, y=x0)
        return x1

    block = prog.functions["main"]
    x0 = block.inputs["x0"]
    ops = block.find_ops(op_type="add")
    duplicate_ops = ops + ops
    block.set_outputs([x0])
    block.remove_ops(duplicate_ops)
    assert len(block.operations) == 0
    assert len(block.inputs) == 1
    assert len(block.outputs) == 1
    assert block.inputs["x0"] == block.outputs[0]


def test_remove_duplicate_ops_not_affect_others():
    """
    Test remove duplicated ops doesn't affect other ops. We add another `add` op here, but keep
    the input to remove_ops only restricted to the first `add` op. This test is for checking that
    the second add op doesn't get removed.
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.add(x=x0, y=x0)
        x2 = mb.add(x=x0, y=x0)
        return x1, x2

    block = prog.functions["main"]
    x0 = block.inputs["x0"]
    ops = [block.find_ops(op_type="add")[0]]
    block.set_outputs([x0])
    block.remove_ops(ops)
    # Deleting one add operation should not affect the other one.
    assert len(block.operations) == 1
    assert len(block.inputs) == 1
    assert len(block.outputs) == 1


def test_remove_ops_fail_for_block_output():
    """Block's output cannot be removed."""

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.add(x=x0, y=x0)
        x2 = mb.add(x=x0, y=x0)
        return x1, x2

    block = prog.functions["main"]
    ops = block.find_ops(op_type="add")
    expected_err_str = "cannot delete op add_.* with output 0: add_.* that's block block.*'s output"
    with pytest.raises(ValueError, match=expected_err_str):
        block.remove_ops(ops)
    assert len(block.operations) == 2
    assert len(block.inputs) == 1
    assert len(block.outputs) == 2


def test_op_removal_and_insertion():
    """
    Remove a transpose pair and materialize one transpose before another op
    Given:
        %x1 = transpose(%x)
        %x2 = relu(%x1)
        %out1 = avg_pool(%x2)
        %x3 = transpose(%x2)
        %out2 = log(%x3)

    After removing both transposes:
        %x2 = relu(%x)
        %out1 = avg_pool(%x2)
        %out2 = log(%x2)

    After inserting a transpose:
        %x2 = relu(%x)
        %x4 = transpose(%x2)
        %out1 = avg_pool(%x4)
        %out2 = log(%x2)

    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(1, 2, 6, 6))])
    def prog(x):
        x1 = mb.transpose(x=x, perm=[0, 2, 3, 1])
        x2 = mb.relu(x=x1)
        out1 = mb.avg_pool(x=x2, kernel_sizes=[1, 1], strides=[1, 1], pad_type="valid")
        x3 = mb.transpose(x=x2, perm=[0, 3, 1, 2])
        out2 = mb.log(x=x3)
        return out1, out2

    prev_prog = copy.deepcopy(prog)

    print("before:\n{}".format(prog))
    assert get_op_types_in_program(prog) == [
        "transpose",
        "relu",
        "avg_pool",
        "transpose",
        "log",
    ]
    block = prog.functions["main"]

    def remove_transpose(block):
        op = block.find_ops(op_type="transpose")[0]
        block.replace_uses_of_var_after_op(
            anchor_op=op.inputs["x"].op,
            old_var=op.outputs[0],
            new_var=op.inputs["x"],
            no_check_var_types=True,
        )
        block.remove_ops([op])

    with block:
        # remove 1st transpose
        remove_transpose(block)
        assert get_op_types_in_program(prog) == ["relu", "avg_pool", "transpose", "log"]

        # remove 2nd transpose
        remove_transpose(block)
        assert get_op_types_in_program(prog) == ["relu", "avg_pool", "log"]

        print("after transpose ops removal:\n{}".format(prog))

        # insert transpose before pool
        pool_op = block.find_ops(op_type="avg_pool")[0]
        with block:
            y = mb.transpose(x=pool_op.inputs["x"], perm=[0, 2, 3, 1], before_op=pool_op)

        block.replace_uses_of_var_after_op(
            anchor_op=y.op,
            end_op=pool_op,
            old_var=pool_op.inputs["x"],
            new_var=y,
            no_check_var_types=True,
        )

        print("after transpose insertion:\n{}".format(prog))
        assert get_op_types_in_program(prog) == ["relu", "transpose", "avg_pool", "log"]

        for op in block.operations:
            op.type_value_inference(overwrite_output=True)

        assert_same_output_names(prev_prog, prog)
        assert_same_output_shapes(prev_prog, prog)


def test_replace_nonreplaceable_vars():
    """
    The conversion should error out if an invalid replacement is invoked with nonreplaceable vars
    """
    constexpr_op = "constexpr_sparse_to_dense"
    @mb.program(input_specs=[mb.TensorSpec(shape=(4, 2))])
    def prog(x):
        constexpr = CONSTEXPR_FUNCS[constexpr_op]((4, 2))
        return mb.add(x=x, y=constexpr)

    block = prog.functions["main"]
    constexpr_op = block.find_ops(op_type=constexpr_op)[0]

    with block:
        const = mb.const(val=np.random.rand(4, 2), before_op=constexpr_op)
        expected_err_str = "might potentially be removed during the replacement of those vars."
        with pytest.raises(ValueError, match=expected_err_str):
            block.replace_uses_of_var_after_op(
                anchor_op=constexpr_op,
                old_var=constexpr_op.outputs[0],
                new_var=const
            )


def test_replace_nonreplaceable_vars_force():
    """
    The conversion should not error out if the replace_uses_of_vars_after_op is executed with
    force_replace=True Also we test that, the new nonreplaceable_vars_upstream is propagated
    after the code exist `with block`.
    """
    constexpr_op = "constexpr_sparse_to_dense"
    @mb.program(input_specs=[mb.TensorSpec(shape=(4, 2))])
    def prog(x):
        constexpr = CONSTEXPR_FUNCS[constexpr_op]((4, 2))
        return mb.add(x=x, y=constexpr)

    block = prog.functions["main"]
    constexpr_op = block.find_ops(op_type=constexpr_op)[0]
    add_op = block.find_ops(op_type="add")[0]

    assert len(add_op.outputs[0].nonreplaceable_vars_upstream) == 1

    with block:
        const = mb.const(val=np.random.rand(4, 2), before_op=constexpr_op)
        block.replace_uses_of_var_after_op(
            anchor_op=constexpr_op,
            old_var=constexpr_op.outputs[0],
            new_var=const,
            force_replace=True,
        )
        block.remove_ops([constexpr_op])

    assert len(add_op.outputs[0].nonreplaceable_vars_upstream) == 0


def test_simple_substituion():
    """
    Replace log(x+y) with log(x*y)
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4)), mb.TensorSpec(shape=(2, 4))])
    def prog(x0, y0):
        x1 = mb.add(x=x0, y=y0)
        z = mb.log(x=x1)
        return z

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    assert len(block.find_ops(op_type="log")) == 1
    assert len(block.find_ops(op_type="add")) == 1
    assert len(block.find_ops(op_type="mul")) == 0

    add = block.find_ops(op_type="add")[0]

    x0 = add.inputs["x"]
    y0 = add.inputs["y"]
    x1 = add.outputs[0]

    with block:
        # It's important to add 'mul' before 'add' (its even better to do it
        # immediately after 'add' but we don't have the API)
        # because we need to replace any op affected by add with 'mul'
        x2 = mb.mul(x=x0, y=y0, before_op=add)

    assert len(block.find_ops(op_type="mul")) == 1
    assert len(block.find_ops(op_type="add")) == 1
    assert len(block.find_ops(op_type="log")) == 1

    # It's important to set anchor_op = 'mul' because new_var is only visible
    # after 'mul'.
    block.replace_uses_of_var_after_op(anchor_op=x2.op, old_var=x1, new_var=x2)
    block.remove_ops([add])

    print("after:\n{}".format(prog))
    assert len(block.find_ops(op_type="add")) == 0
    assert len(block.find_ops(op_type="mul")) == 1
    assert len(block.find_ops(op_type="log")) == 1


def test_substitute_nested_op():
    """"
    Replace an conditional op with nested block
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4)), mb.TensorSpec(shape=(2, 4))])
    def prog(x0, y0):
        pred = mb.less(x=x0, y=y0)
        z = mb.cond(
            pred=pred, _true_fn=lambda: mb.abs(x=x0), _false_fn=lambda: mb.abs(x=y0)
        )
        z1 = mb.log(x=z)
        return z1

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    assert len(block.find_ops(op_type="less")) == 1
    assert len(block.find_ops(op_type="abs")) == 2
    assert len(block.find_ops(op_type="cond")) == 1
    assert len(block.find_ops(op_type="log")) == 1

    cond = block.find_ops(op_type="cond")[0]
    x0 = block.inputs["x0"]
    z = cond.outputs[0]
    block.replace_uses_of_var_after_op(anchor_op=None, old_var=z, new_var=x0)

    # removing cond will also remove the abs ops within its block
    block.remove_ops([cond])

    print("after:\n{}".format(prog))
    assert len(block.find_ops(op_type="less")) == 1
    assert len(block.find_ops(op_type="log")) == 1
    assert len(block.find_ops(op_type="cond")) == 0
    assert len(block.find_ops(op_type="abs")) == 0


def test_simple_transpose_squash():
    """
    Test eliminate consecutive transpose can be canceled
    """

    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4))])
    def prog(x0):
        x1 = mb.transpose(x=x0, perm=[1, 0])
        x2 = mb.transpose(x=x1, perm=[1, 0])
        x3 = mb.log(x=x2)
        x4 = mb.transpose(x=x3, perm=[1, 0])
        x5 = mb.transpose(x=x4, perm=[1, 0])
        x6 = mb.transpose(x=x5, perm=[1, 0])
        x7 = mb.transpose(x=x6, perm=[1, 0])
        return x7

    print("before:\n{}".format(prog))
    block = prog.functions["main"]
    assert len(block.find_ops(op_type="transpose")) == 6

    def can_squash(trans1, trans2):
        return (
            len(trans1.outputs) == 1
            and len(trans2.outputs) == 1
            and all(trans1.perm.val == trans2.perm.val)
        )

    # Find all candidate pairs transposes
    # we ignore all const (transpose_perm_%x), and add pairs of transpose op as
    # candidate. This won't generalize to more complicated program with other
    # shape invariant ops in between.
    candidates = []
    non_const_ops = [op for op in block.operations if op.op_type != "const"]
    for i in range(len(non_const_ops) - 1):
        op = non_const_ops[i]
        if len(candidates) and op == candidates[-1][1]:
            # op is already a squash candidate
            continue
        next_op = non_const_ops[i + 1]
        if (
            op.op_type == "transpose"
            and next_op.op_type == "transpose"
            and can_squash(op, next_op)
        ):
            candidates.append((op, next_op))

    # Remove each candidate pairs
    for (trans1, trans2) in candidates:
        before = trans1.inputs["x"]
        after = trans2.outputs[0]
        block.replace_uses_of_var_after_op(
            anchor_op=trans2, old_var=after, new_var=before
        )
        block.remove_ops([trans1, trans2])

    print("after:\n{}".format(prog))
    assert len(block.find_ops(op_type="transpose")) == 0


def test_duplicate_outputs_add_consuming_block_once():
    """The same consuming block should only be added once."""
    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4)), mb.TensorSpec(shape=(2, 4))])
    def prog(x0, y0):
        x1 = mb.add(x=x0, y=y0)
        return x1, x1, x1

    block = prog.functions["main"]
    assert len(block.outputs[0].consuming_blocks) == 1
    assert len(block.outputs[1].consuming_blocks) == 1
    assert len(block.outputs[2].consuming_blocks) == 1


def test_duplicate_outputs_substituion():
    """Replaces var that appears more than once in outputs."""
    @mb.program(input_specs=[mb.TensorSpec(shape=(2, 4)), mb.TensorSpec(shape=(2, 4))])
    def prog(x0, y0):
        x1 = mb.add(x=x0, y=y0)
        z = mb.log(x=x1)
        return x1, x1, z

    block = prog.functions["main"]
    add = block.find_ops(op_type="add")[0]
    x0 = add.inputs["x"]
    y0 = add.inputs["y"]
    x1 = add.outputs[0]

    with block:
        x2 = mb.mul(x=x0, y=y0, before_op=add, name="new_output")

    block.replace_uses_of_var_after_op(anchor_op=x2.op, old_var=x1, new_var=x2)
    block.remove_ops([add])
    assert block.outputs[0].op.name == "new_output"
    assert block.outputs[1].op.name == "new_output"
    assert len(block.outputs[0].consuming_blocks) == 1


class TestCacheDoublyLinkedList:
    def test_basic(self):
        operations = CacheDoublyLinkedList()

        operations.insert_op_before(1)
        assert list(operations) == [1]

        operations.insert_op_before(2, before_op=1)
        assert list(operations) == [2, 1]

        operations.insert_op_before(3)
        assert list(operations) == [2, 1, 3]

        operations.insert_op_before(4, before_op=1)
        assert list(operations) == [2, 4, 1, 3]

        operations.remove(2)
        assert list(operations) == [4, 1, 3]

        operations.remove(3)
        assert list(operations) == [4, 1]

        operations.remove(4)
        assert list(operations) == [1]

        node = operations._get_node_from_op(1)
        operations.remove(1)
        assert list(operations) == []
        assert node.prev is CacheDoublyLinkedList.INVALID_NODE
        assert node.next is CacheDoublyLinkedList.INVALID_NODE

        operations.insert_op_before(0)
        assert list(operations) == [0]

        operations = CacheDoublyLinkedList([1, 2, 3])
        assert list(operations) == [1, 2, 3]

        operations = CacheDoublyLinkedList([])
        assert list(operations) == []

    def test_reversed(self):
        operations = CacheDoublyLinkedList([1, 2, 3])
        assert list(reversed(operations)) == [3, 2, 1]

    def test_error(self):
        operations = CacheDoublyLinkedList([1, 2, 3])
        assert operations[0] == 1
        assert operations[-1] == 3
        # Indexing doubly linked list is super expensive, we need to error out.
        with pytest.raises(
            ValueError, match="Doubly linked list does not support indexing other than 0, -1."
        ):
            operations[1]

    def test_deep_copy(self):
        operations = CacheDoublyLinkedList([x for x in range(0, 5000)])
        copy_operations = copy.deepcopy(operations)
        assert list(copy_operations) == [x for x in range(0, 5000)]
