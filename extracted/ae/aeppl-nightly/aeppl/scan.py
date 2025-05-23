from copy import copy
from typing import Callable, Dict, Iterable, List, Tuple, cast

import aesara
import aesara.tensor as at
import numpy as np
from aesara.graph.basic import Variable
from aesara.graph.fg import FunctionGraph
from aesara.graph.op import compute_test_value
from aesara.graph.rewriting.basic import node_rewriter
from aesara.graph.rewriting.db import RewriteDatabaseQuery
from aesara.scan.op import Scan
from aesara.scan.rewriting import scan_eqopt1, scan_eqopt2
from aesara.scan.utils import ScanArgs
from aesara.tensor.random.type import RandomType
from aesara.tensor.subtensor import Subtensor, indices_from_subtensor
from aesara.tensor.var import TensorVariable
from aesara.updates import OrderedUpdates

from aeppl.abstract import MeasurableVariable, _get_measurable_outputs
from aeppl.joint_logprob import conditional_logprob
from aeppl.logprob import _logprob
from aeppl.rewriting import (
    inc_subtensor_ops,
    logprob_rewrites_db,
    measurable_ir_rewrites_db,
)


class MeasurableScan(Scan):
    """A placeholder used to specify a log-likelihood for a scan sub-graph."""


MeasurableVariable.register(MeasurableScan)


def convert_outer_out_to_in(
    input_scan_args: ScanArgs,
    outer_out_vars: Iterable[TensorVariable],
    new_outer_input_vars: Dict[TensorVariable, TensorVariable],
    inner_out_fn: Callable[
        [Dict[TensorVariable, TensorVariable]], Iterable[TensorVariable]
    ],
) -> ScanArgs:
    r"""Convert outer-graph outputs into outer-graph inputs.

    Parameters
    ==========
    input_scan_args:
        The source `Scan` arguments.
    outer_out_vars:
        The outer-graph output variables that are to be converted into an
        outer-graph input.
    new_outer_input_vars:
        The variables used for the new outer-graph input computed for
        `outer_out_vars`.
    inner_out_fn:
        A function that takes the remapped outer-out variables and produces new
        inner-graph outputs.  This can be used to transform the
        `outer_out_vars`\s' corresponding inner-graph outputs into something
        else entirely, like log-probabilities.

    Outputs
    =======
    A `ScanArgs` object for a `Scan` in which `outer_out_vars` has been converted to an
    outer-graph input.
    """

    output_scan_args = copy(input_scan_args)
    inner_outs_to_new_inner_ins = {}

    # Map inner-outputs to outer-outputs
    old_inner_outs_to_outer_outs = {}

    for oo_var in outer_out_vars:

        var_info = output_scan_args.find_among_fields(
            oo_var, field_filter=lambda x: x.startswith("outer_out")
        )

        assert var_info is not None
        assert oo_var in new_outer_input_vars

        io_var = output_scan_args.get_alt_field(var_info, "inner_out")
        old_inner_outs_to_outer_outs[io_var] = oo_var

    # In this loop, we gather information about the new inner-inputs that have
    # been created and what their corresponding inner-outputs were, and we
    # update the outer and inner-inputs to reflect the addition of new
    # inner-inputs.
    for old_inner_out_var, oo_var in old_inner_outs_to_outer_outs.items():

        # Couldn't one do the same with `var_info`?
        inner_out_info = output_scan_args.find_among_fields(
            old_inner_out_var, field_filter=lambda x: x.startswith("inner_out")
        )

        output_scan_args.remove_from_fields(old_inner_out_var, rm_dependents=False)

        # Remove the old outer-output variable.
        # Not sure if this really matters, since we don't use the outer-outputs
        # when building a new `Scan`, but doing it keeps the `ScanArgs` object
        # consistent.
        output_scan_args.remove_from_fields(oo_var, rm_dependents=False)

        # Use the index for the specific inner-graph sub-collection to which this
        # variable belongs (e.g. index `1` among the inner-graph sit-sot terms)
        var_idx = inner_out_info.index

        # The old inner-output variable becomes the a new inner-input
        new_inner_in_var = old_inner_out_var.clone()
        if new_inner_in_var.name:
            new_inner_in_var.name = f"{new_inner_in_var.name}_vv"

        inner_outs_to_new_inner_ins[old_inner_out_var] = new_inner_in_var

        # We want to remove elements from both lists and tuples, because the
        # members of `ScanArgs` could switch from being `list`s to `tuple`s
        # soon
        def remove(x, i):
            return x[:i] + x[i + 1 :]

        # If we're replacing a [m|s]it-sot, then we need to add a new nit-sot
        add_nit_sot = False
        if inner_out_info.name.endswith("mit_sot"):
            inner_in_mit_sot_var = cast(
                Tuple[int, ...], tuple(output_scan_args.inner_in_mit_sot[var_idx])
            )
            new_inner_in_seqs = inner_in_mit_sot_var + (new_inner_in_var,)
            new_inner_in_mit_sot = remove(output_scan_args.inner_in_mit_sot, var_idx)
            new_outer_in_mit_sot = remove(output_scan_args.outer_in_mit_sot, var_idx)
            new_inner_in_sit_sot = tuple(output_scan_args.inner_in_sit_sot)
            new_outer_in_sit_sot = tuple(output_scan_args.outer_in_sit_sot)
            add_nit_sot = True
        elif inner_out_info.name.endswith("sit_sot"):
            new_inner_in_seqs = (output_scan_args.inner_in_sit_sot[var_idx],) + (
                new_inner_in_var,
            )
            new_inner_in_sit_sot = remove(output_scan_args.inner_in_sit_sot, var_idx)
            new_outer_in_sit_sot = remove(output_scan_args.outer_in_sit_sot, var_idx)
            new_inner_in_mit_sot = tuple(output_scan_args.inner_in_mit_sot)
            new_outer_in_mit_sot = tuple(output_scan_args.outer_in_mit_sot)
            add_nit_sot = True
        else:
            new_inner_in_seqs = (new_inner_in_var,)
            new_inner_in_mit_sot = tuple(output_scan_args.inner_in_mit_sot)
            new_outer_in_mit_sot = tuple(output_scan_args.outer_in_mit_sot)
            new_inner_in_sit_sot = tuple(output_scan_args.inner_in_sit_sot)
            new_outer_in_sit_sot = tuple(output_scan_args.outer_in_sit_sot)

        output_scan_args.inner_in_mit_sot = list(new_inner_in_mit_sot)
        output_scan_args.inner_in_sit_sot = list(new_inner_in_sit_sot)
        output_scan_args.outer_in_mit_sot = list(new_outer_in_mit_sot)
        output_scan_args.outer_in_sit_sot = list(new_outer_in_sit_sot)

        if inner_out_info.name.endswith("mit_sot"):
            mit_sot_var_taps = cast(
                Tuple[int, ...], tuple(output_scan_args.mit_sot_in_slices[var_idx])
            )
            taps = mit_sot_var_taps + (0,)
            new_mit_sot_in_slices = remove(output_scan_args.mit_sot_in_slices, var_idx)
        elif inner_out_info.name.endswith("sit_sot"):
            taps = (-1, 0)
            new_mit_sot_in_slices = tuple(output_scan_args.mit_sot_in_slices)
        else:
            taps = (0,)
            new_mit_sot_in_slices = tuple(output_scan_args.mit_sot_in_slices)

        output_scan_args.mit_sot_in_slices = list(new_mit_sot_in_slices)

        taps, new_inner_in_seqs = zip(
            *sorted(zip(taps, new_inner_in_seqs), key=lambda x: x[0])
        )

        new_inner_in_seqs = tuple(output_scan_args.inner_in_seqs) + tuple(
            reversed(new_inner_in_seqs)
        )

        output_scan_args.inner_in_seqs = list(new_inner_in_seqs)

        slice_seqs = zip(
            -np.asarray(taps), [n if n < 0 else None for n in reversed(taps)]
        )

        # XXX: If the caller passes the variables output by `aesara.scan`, it's
        # likely that this will fail, because those variables can sometimes be
        # slices of the actual outer-inputs (e.g. `out[1:]` instead of `out`
        # when `taps=[-1]`).
        var_slices = [new_outer_input_vars[oo_var][b:e] for b, e in slice_seqs]
        n_steps = at.min([at.shape(n)[0] for n in var_slices])

        output_scan_args.n_steps = n_steps

        new_outer_in_seqs = tuple(output_scan_args.outer_in_seqs) + tuple(
            v[:n_steps] for v in var_slices
        )

        output_scan_args.outer_in_seqs = list(new_outer_in_seqs)

        if add_nit_sot:
            new_outer_in_nit_sot = tuple(output_scan_args.outer_in_nit_sot) + (n_steps,)
        else:
            new_outer_in_nit_sot = tuple(output_scan_args.outer_in_nit_sot)

        output_scan_args.outer_in_nit_sot = list(new_outer_in_nit_sot)

    # Now, we can add new inner-outputs for the custom calculations.
    # We don't need to create corresponding outer-outputs, because `Scan` will
    # do that when we call `Scan.make_node`.  All we need is a consistent
    # outer-inputs and inner-graph spec., which we should have in
    # `output_scan_args`.
    remapped_io_to_ii = inner_outs_to_new_inner_ins
    new_inner_out_nit_sot = tuple(output_scan_args.inner_out_nit_sot) + tuple(
        inner_out_fn(remapped_io_to_ii)
    )

    output_scan_args.inner_out_nit_sot = list(new_inner_out_nit_sot)

    return output_scan_args


def get_random_outer_outputs(
    scan_args: ScanArgs,
) -> List[Tuple[int, TensorVariable, TensorVariable]]:
    """Get the `MeasurableVariable` outputs of a `Scan` (well, its `ScanArgs`).

    Returns
    =======
    A tuple of tuples containing the index of each outer-output variable, the
    outer-output variable itself, and the inner-output variable that
    is an instance of `MeasurableVariable`.
    """
    rv_vars = []
    for n, oo_var in enumerate(
        [o for o in scan_args.outer_outputs if not isinstance(o.type, RandomType)]
    ):
        oo_info = scan_args.find_among_fields(oo_var)
        io_type = oo_info.name[(oo_info.name.index("_", 6) + 1) :]
        inner_out_type = "inner_out_{}".format(io_type)
        io_var = getattr(scan_args, inner_out_type)[oo_info.index]
        if io_var.owner and isinstance(io_var.owner.op, MeasurableVariable):
            rv_vars.append((n, oo_var, io_var))
    return rv_vars


def construct_scan(
    scan_args: ScanArgs, **kwargs
) -> Tuple[List[TensorVariable], OrderedUpdates]:
    scan_op = Scan(
        scan_args.inner_inputs, scan_args.inner_outputs, scan_args.info, **kwargs
    )
    node = scan_op.make_node(*scan_args.outer_inputs)
    updates = OrderedUpdates(zip(scan_args.outer_in_shared, scan_args.outer_out_shared))
    return node.outputs, updates


@_logprob.register(MeasurableScan)
def logprob_ScanRV(op, values, *inputs, name=None, **kwargs):

    new_node = op.make_node(*inputs)
    scan_args = ScanArgs.from_node(new_node)
    rv_outer_outs = get_random_outer_outputs(scan_args)

    var_indices, rv_vars, io_vars = zip(*rv_outer_outs)
    value_map = {_rv: _val for _rv, _val in zip(rv_vars, values)}

    def create_inner_out_logp(
        value_map: Dict[TensorVariable, TensorVariable]
    ) -> TensorVariable:
        """Create a log-likelihood inner-output for a `Scan`."""
        logp_parts, _ = conditional_logprob(realized=value_map, warn_missing_rvs=False)
        return logp_parts.values()

    logp_scan_args = convert_outer_out_to_in(
        scan_args,
        rv_vars,
        value_map,
        inner_out_fn=create_inner_out_logp,
    )

    # Remove the shared variables corresponding to replaced terms.

    # TODO FIXME: This is a really dirty approach, because it effectively
    # assumes that all sampling is being removed, and, thus, all shared updates
    # relating to `RandomType`s.  Instead, we should be more precise and only
    # remove the `RandomType`s associated with `values`.
    logp_scan_args.outer_in_shared = [
        i for i in logp_scan_args.outer_in_shared if not isinstance(i.type, RandomType)
    ]
    logp_scan_args.inner_in_shared = [
        i for i in logp_scan_args.inner_in_shared if not isinstance(i.type, RandomType)
    ]
    logp_scan_args.inner_out_shared = [
        i for i in logp_scan_args.inner_out_shared if not isinstance(i.type, RandomType)
    ]
    # XXX TODO: Remove this properly
    # logp_scan_args.outer_out_shared = []

    logp_scan_out, updates = construct_scan(logp_scan_args, mode=op.mode)

    # Automatically pick up updates so that we don't have to pass them around
    for key, value in updates.items():
        key.default_update = value

    return logp_scan_out


@node_rewriter([Scan])
def find_measurable_scans(fgraph, node):
    r"""Finds `Scan`\s for which a `logprob` can be computed.

    This will convert said `Scan`\s into `MeasurableScan`\s.  It also updates
    random variable and value variable mappings that have been specified for
    parts of a `Scan`\s outputs (e.g. everything except the initial values).
    """

    if not isinstance(node.op, Scan):
        return None

    if isinstance(node.op, MeasurableScan):
        return None

    if not hasattr(fgraph, "shape_feature"):
        return None  # pragma: no cover

    rv_map_feature = getattr(fgraph, "preserve_rv_mappings", None)

    if rv_map_feature is None:
        return None  # pragma: no cover

    curr_scanargs = ScanArgs.from_node(node)

    # Find the un-output `MeasurableVariable`s created in the inner-graph
    clients: Dict[Variable, List[Variable]] = {}

    local_fgraph_topo = aesara.graph.basic.io_toposort(
        curr_scanargs.inner_inputs,
        [o for o in curr_scanargs.inner_outputs if not isinstance(o.type, RandomType)],
        clients=clients,
    )
    for n in local_fgraph_topo:
        if isinstance(n.op, MeasurableVariable):
            non_output_node_clients = [
                c for c in clients[n] if c not in curr_scanargs.inner_outputs
            ]

            if non_output_node_clients:
                # This node is a `MeasurableVariable`, but it depends on
                # variable that's not being output?
                # TODO: Why can't we make this a `MeasurableScan`?
                return None

    if not any(out in rv_map_feature.rv_values for out in node.outputs):
        # We need to remap user inputs that have been specified in terms of
        # `Subtensor`s of this `Scan`'s node's outputs.
        #
        # For example, the output that the user got was something like
        # `out[1:]` for `outputs_info = [{"initial": x0, "taps": [-1]}]`, so
        # they likely passed `{out[1:]: x_1T_vv}` to `joint_logprob`.
        # Since `out[1:]` isn't really the output of a `Scan`, but a
        # `Subtensor` of the output `out` of a `Scan`, we need to account for
        # that.

        # Get any `Subtensor` outputs that have been applied to outputs of this
        # `Scan` (and get the corresponding indices of the outputs from this
        # `Scan`)
        output_clients: List[Tuple[Variable, int]] = sum(
            [
                [
                    # This is expected to work for `Subtensor` `Op`s,
                    # because they only ever have one output
                    (cl.default_output(), i)
                    for cl, _ in fgraph.get_clients(out)
                    if isinstance(cl.op, Subtensor)
                ]
                for i, out in enumerate(node.outputs)
            ],
            [],
        )

        # The second items in these tuples are the value variables mapped to
        # the *user-specified* measurable variables (i.e. the first items) that
        # are `Subtensor`s of the outputs of this `Scan`.  The second items are
        # the index of the corresponding output of this `Scan` node.
        indirect_rv_vars = [
            (out, rv_map_feature.rv_values[out], out_idx)
            for out, out_idx in output_clients
            if out in rv_map_feature.rv_values
        ]

        if not indirect_rv_vars:
            return None

        # We need this for the `clone` in the loop that follows
        if aesara.config.compute_test_value != "off":
            compute_test_value(node)

        # We're going to replace the user's random variable/value variable mappings
        # with ones that map directly to outputs of this `Scan`.
        for rv_var, val_var, out_idx in indirect_rv_vars:

            # The full/un-`Subtensor`ed `Scan` output that we need to use
            full_out = node.outputs[out_idx]

            assert rv_var.owner.inputs[0] == full_out

            # A new value variable that spans the full output.
            # We don't want the old graph to appear in the new log-probability
            # graph, so we use the shape feature to (hopefully) get the shape
            # without the entire `Scan` itself.
            full_out_shape = tuple(
                fgraph.shape_feature.get_shape(full_out, i)
                for i in range(full_out.ndim)
            )
            new_val_var = at.empty(full_out_shape, dtype=full_out.dtype)

            # Set the parts of this new value variable that applied to the
            # user-specified value variable to the user's value variable
            subtensor_indices = indices_from_subtensor(
                rv_var.owner.inputs[1:], rv_var.owner.op.idx_list
            )
            # E.g. for a single `-1` TAPS, `s_0T[1:] = s_1T` where `s_0T` is
            # `new_val_var` and `s_1T` is the user-specified value variable
            # that only spans times `t=1` to `t=T`.
            new_val_var = at.set_subtensor(new_val_var[subtensor_indices], val_var)

            # This is the outer-input that sets `s_0T[i] = taps[i]` where `i`
            # is a TAP index (e.g. a TAP of `-1` maps to index `0` in a vector
            # of the entire series).
            var_info = curr_scanargs.find_among_fields(full_out)
            alt_type = var_info.name[(var_info.name.index("_", 6) + 1) :]
            outer_input_var = getattr(curr_scanargs, f"outer_in_{alt_type}")[
                var_info.index
            ]

            # These outer-inputs are using by `aesara.scan.utils.expand_empty`, and
            # are expected to consist of only a single `set_subtensor` call.
            # That's why we can simply replace the first argument of the node.
            assert isinstance(outer_input_var.owner.op, inc_subtensor_ops)

            # We're going to set those values on our `new_val_var` so that it can
            # serve as a complete replacement for the old input `outer_input_var`.
            # from aesara.graph import clone_replace
            #
            new_val_var = outer_input_var.owner.clone_with_new_inputs(
                [new_val_var] + outer_input_var.owner.inputs[1:]
            ).default_output()

            # Replace the mapping
            rv_map_feature.update_rv_maps(rv_var, new_val_var, full_out)

    op = MeasurableScan(
        curr_scanargs.inner_inputs,
        curr_scanargs.inner_outputs,
        curr_scanargs.info,
        mode=node.op.mode,
    )
    new_node = op.make_node(*curr_scanargs.outer_inputs)

    return dict(zip(node.outputs, new_node.outputs))


@node_rewriter([Scan])
def add_opts_to_inner_graphs(fgraph, node):
    """Update the `Mode`(s) used to compile the inner-graph of a `Scan` `Op`.

    This is how we add the measurable IR rewrites to the "body"
    (i.e. inner-graph) of a `Scan` loop.
    """

    if not isinstance(node.op, Scan):
        return None

    # Avoid unnecessarily re-applying this rewrite
    if getattr(node.op.mode, "had_logprob_rewrites", False):
        return None

    inner_fgraph = FunctionGraph(
        node.op.inner_inputs,
        node.op.inner_outputs,
        clone=True,
        copy_inputs=False,
        copy_orphans=False,
    )

    logprob_rewrites_db.query(RewriteDatabaseQuery(include=["basic"])).rewrite(
        inner_fgraph
    )

    new_outputs = list(inner_fgraph.outputs)

    # TODO FIXME: This is pretty hackish.
    new_mode = copy(node.op.mode)
    new_mode.had_logprob_rewrites = True

    op = Scan(node.op.inner_inputs, new_outputs, node.op.info, mode=new_mode)
    new_node = op.make_node(*node.inputs)

    return dict(zip(node.outputs, new_node.outputs))


@_get_measurable_outputs.register(MeasurableScan)
def _get_measurable_outputs_MeasurableScan(op, node):
    # TODO: This should probably use `get_random_outer_outputs`
    # scan_args = ScanArgs.from_node(node)
    # rv_outer_outs = get_random_outer_outputs(scan_args)
    return [o for o in node.outputs if not isinstance(o.type, RandomType)]


measurable_ir_rewrites_db.register(
    "add_opts_to_inner_graphs",
    add_opts_to_inner_graphs,
    # out2in(
    #     add_opts_to_inner_graphs, name="add_opts_to_inner_graphs", ignore_newtrees=True
    # ),
    -100,
    "basic",
    "scan",
)

measurable_ir_rewrites_db.register(
    "find_measurable_scans",
    find_measurable_scans,
    0,
    "basic",
    "scan",
)

# Add scan canonicalizations that aren't in the canonicalization DB
logprob_rewrites_db.register("scan_eqopt1", scan_eqopt1, -9, "basic", "scan")
logprob_rewrites_db.register("scan_eqopt2", scan_eqopt2, -9, "basic", "scan")
