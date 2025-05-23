use std::fmt::Formatter;
use std::ops::Deref;

use dyn_clone::clone_box;
use kernel_selection::wire_packing;
use tract_itertools::{izip, multiunzip};
use tract_linalg::block_quant::BlockQuantValue;
use tract_linalg::mmm::MMMInputFormat;
use tract_linalg::WeightType;

use super::*;
use crate::ops::cast::cast;
use crate::ops::math::add;
use crate::ops::matmul::optimized::{
    AddMatMulGeometry, MapOutputAxisToInput, OptMatMul, ProtoFusedSpec,
};
use crate::ops::matmul::quant::{
    combine_scales, compensate_zero_points, requant, wire_ensure_q8_flavour,
};
use crate::ops::nn::{Reduce, Reducer};

#[derive(Debug)]
#[allow(clippy::large_enum_variant)]
pub enum AxesOrPatch<'a> {
    Annotated(EinSumAnnotatedAsMatMul<'a>),
    Patch(TypedModelPatch),
    NotAMatMul(&'static str, Vec<&'a Axis>),
}

pub struct EinSumAnnotatedAsMatMul<'a> {
    pub op: &'a EinSum,
    pub m_axis: &'a Axis,
    pub k_axis: &'a Axis,
    pub n_axis: &'a Axis,
    pub m: TDim,
    pub k: TDim,
    pub n: TDim,
}

impl EinSumAnnotatedAsMatMul<'_> {
    pub fn a_m(&self) -> usize {
        self.m_axis.inputs[0][0]
    }
    pub fn a_k(&self) -> usize {
        self.k_axis.inputs[0][0]
    }
    pub fn b_k(&self) -> usize {
        self.k_axis.inputs[1][0]
    }
    pub fn b_n(&self) -> usize {
        self.n_axis.inputs[1][0]
    }
    pub fn c_m(&self) -> usize {
        *self.m_axis.outputs[0].first().unwrap_or(&self.a_m())
    }
    pub fn c_n(&self) -> usize {
        *self.n_axis.outputs[0].first().unwrap_or(&self.b_n())
    }
}

impl Debug for EinSumAnnotatedAsMatMul<'_> {
    fn fmt(&self, f: &mut Formatter) -> std::fmt::Result {
        write!(
            f,
            "EinsumAsMatMul: {} {:?} m: {}={}; k: {}={}; n: {}={}",
            self.op.axes,
            self.op.operating_dt,
            self.m_axis.repr,
            self.m,
            self.k_axis.repr,
            self.k,
            self.n_axis.repr,
            self.n
        )
    }
}

impl Deref for EinSumAnnotatedAsMatMul<'_> {
    type Target = EinSum;
    fn deref(&self) -> &Self::Target {
        self.op
    }
}

pub struct EinSumAnnotatedAsLinear<'a> {
    pub op: &'a EinSum,
    pub m_axis: &'a Axis,
    pub k_axis: &'a Axis,
    pub n_axes: Vec<&'a Axis>,
    pub m: usize,
    pub k: usize,
    pub ns: Vec<&'a TDim>,
    pub act_dt: DatumType,
    pub weight_type: WeightType,
}

impl Debug for EinSumAnnotatedAsLinear<'_> {
    fn fmt(&self, f: &mut Formatter) -> std::fmt::Result {
        write!(
            f,
            "EinsumAsLinear: {} w:{:?} acc:{:?} m: {}={}; k: {}={}; n: {}={}",
            self.op.axes,
            self.weight_type,
            self.op.operating_dt,
            self.m_axis.repr,
            self.m,
            self.k_axis.repr,
            self.k,
            self.n_axes.iter().map(|ax| ax.repr).join(","),
            self.ns.iter().map(|d| d.to_string()).join("•"),
        )
    }
}

impl<'a> EinSumAnnotatedAsLinear<'a> {
    pub fn from(
        model: &'a TypedModel,
        node: &'a TypedNode,
        op: &'a EinSum,
    ) -> TractResult<Option<Self>> {
        if node.inputs.len() != 2 {
            return Ok(None);
        }
        let input_facts = model.node_input_facts(node.id)?;
        if input_facts[0].konst.is_none() {
            return Ok(None);
        }
        let mut n_axes = vec![];
        let mut ns = Vec::<&'a TDim>::new();

        let Some(m_axis) = op.axes.iter_all_axes().find(|axis| {
            axis.inputs[0].len() == 1 && axis.inputs[1].len() == 0 && axis.outputs[0].len() == 1
        }) else {
            return Ok(None);
        };
        let Some(k_axis) = op.axes.iter_all_axes().find(|axis| {
            axis.inputs[0].len() == 1 && axis.inputs[1].len() == 1 && axis.outputs[0].len() == 0
        }) else {
            return Ok(None);
        };
        for axis in op.axes.iter_all_axes() {
            if axis != k_axis
                && axis != m_axis
                && axis.inputs[0].len() == 0
                && axis.inputs[1].len() == 1
                && axis.outputs[0].len() == 1
            {
                n_axes.push(axis);
                ns.push(&node.outputs[0].fact.shape[axis.outputs[0][0]]);
            }
        }
        let act_dt = input_facts[1].datum_type;
        let bqv = input_facts[0]
            .konst
            .as_ref()
            .unwrap()
            .to_scalar::<Opaque>()
            .ok()
            .and_then(|a| a.downcast_ref::<BlockQuantValue>());
        let weight_type = if let Some(a_payload) = bqv {
            WeightType::BlockQuant(a_payload.fact.format.clone())
        } else {
            input_facts[0].datum_type.into()
        };
        let weight_shape = block_quant_aware_input_shape(input_facts[0])?;
        let m = weight_shape[m_axis.inputs[0][0]].to_usize()?;
        let k = weight_shape[k_axis.inputs[0][0]].to_usize()?;
        Ok(Some(EinSumAnnotatedAsLinear {
            op,
            m_axis,
            k_axis,
            n_axes,
            m,
            k,
            ns,
            act_dt,
            weight_type,
        }))
    }

    pub fn weight_m_axis(&self) -> usize {
        self.m_axis.inputs[0][0]
    }

    pub fn weight_k_axis(&self) -> usize {
        self.k_axis.inputs[0][0]
    }

    pub fn input_k_axis(&self) -> usize {
        self.k_axis.inputs[1][0]
    }

    pub fn output_m_axis(&self) -> usize {
        self.m_axis.outputs[0][0]
    }

    pub fn need_mmv(&self) -> bool {
        self.ns.is_empty() || self.ns.iter().any(|n| n.as_i64().map(|n| n == 1).unwrap_or(true))
    }

    pub fn need_mmm(&self) -> bool {
        self.ns.iter().any(|n| n.as_i64().map(|n| n > 1).unwrap_or(true))
    }

    pub fn cost_for_weights(&self, format: &dyn MMMInputFormat) -> Option<usize> {
        let acc = self.op.acceptable_accumulators();
        let able = tract_linalg::ops()
            .filter_impls(format, &acc, self.act_dt, self.op.operating_dt)
            .collect_vec();
        if able.len() == 0 {
            return None;
        }
        let mut cost = 0;
        if self.need_mmv() {
            cost += able
                .iter()
                .map(|(mmm, _, _, pe, _)| {
                    1_000_000 + mmm.quality().cost() * 1000 + mmm.nr() * 10 - mmm.mr() * 10
                        + pe.is_some() as usize
                })
                .min()
                .unwrap();
        };
        if self.need_mmm() {
            cost += able
                .iter()
                .map(|(mmm, _, _, pe, _)| {
                    1_000_000 + mmm.quality().cost() * 1000 - mmm.nr() * 10 - mmm.mr() * 10
                        + pe.is_some() as usize
                })
                .min()
                .unwrap();
        };
        Some(cost)
    }

    pub fn preferred_packing(&self) -> Box<dyn MMMInputFormat> {
        if self.act_dt == self.acceptable_accumulators()[0]
            && self.weight_type == self.act_dt.into()
        {
            if let Ok(n) = self.ns.iter().cloned().product::<TDim>().to_usize() {
                let mmm = tract_linalg::ops()
                    .mmm(self.acceptable_accumulators()[0], Some(self.m), Some(self.k), Some(n))
                    .unwrap();
                return mmm.packings()[0].0.clone();
            }
        }
        if self.act_dt.is_integer() && self.weight_type == self.act_dt.into() {
            if let Ok(n) = self.ns.iter().cloned().product::<TDim>().to_usize() {
                let mmm = tract_linalg::ops()
                    .mmm(i32::datum_type(), Some(self.m), Some(self.k), Some(n))
                    .unwrap();
                if let Some(packing) =
                    mmm.packings().iter().find(|(a, _)| a.precursor() == self.weight_type)
                {
                    return packing.0.clone();
                }
            }
        }
        clone_box(
            tract_linalg::ops()
                .all_possible_packing(self.weight_type.clone())
                .filter_map(|p| self.cost_for_weights(p).map(|cost| (p, cost)))
                .min_by_key(|(_p, cost)| *cost)
                .unwrap()
                .0,
        )
    }
}

impl Deref for EinSumAnnotatedAsLinear<'_> {
    type Target = EinSum;
    fn deref(&self) -> &Self::Target {
        self.op
    }
}

pub(crate) fn optimize(
    op: &EinSum,
    model: &TypedModel,
    node: &TypedNode,
) -> TractResult<Option<TypedModelPatch>> {
    if (op.q_params.is_none() && node.inputs.len() != 2)
        || (op.q_params.is_some() && node.inputs.len() != 9)
    {
        return Ok(None);
    }

    let input_facts = model.node_input_facts(node.id)?;
    if node.inputs.len() == 2 && input_facts[1].konst.is_some() {
        return Ok(Some(transpose(op, model, node)?));
    }

    let annotated = match ensure_mkn_axes(op, model, node)? {
        AxesOrPatch::Annotated(op) => op,
        AxesOrPatch::Patch(p) => return Ok(Some(p)),
        AxesOrPatch::NotAMatMul(_, _) => return Ok(None),
    };
    if op.q_params.is_none() {
        optimized_mat_mul(model, node, &annotated).context("Translating to OptMatMul")
    } else {
        dequant(model, node, annotated).context("Dequantize")
    }
}

fn transpose(op: &EinSum, model: &TypedModel, node: &TypedNode) -> TractResult<TypedModelPatch> {
    let mut patch = TypedModelPatch::default();
    let mut taps = patch.taps(model, &node.inputs)?;
    taps.swap(0, 1);
    let mut op = op.clone();
    op.axes.iter_all_axes_mut().for_each(|axis| axis.inputs.swap(0, 1));
    let wire = patch.wire_node(&node.name, op, &taps)?[0];
    patch.shunt_outside(model, node.id.into(), wire)?;
    Ok(patch)
}

pub(crate) fn ensure_mkn_axes<'a>(
    op: &'a EinSum,
    model: &TypedModel,
    node: &TypedNode,
) -> TractResult<AxesOrPatch<'a>> {
    let input_facts = model.node_input_facts(node.id)?;
    let input_shapes = op.actual_input_shapes_from_facts(&input_facts)?;
    let output_shape = super::eval::output_shape(&op.axes, &input_shapes)?;
    let k_axes: TVec<&Axis> = op
        .axes
        .iter_all_axes()
        // Filter possible candidates (should be one time in each inputs but not in output)
        .filter(|a| a.inputs[0].len() == 1 && a.inputs[1].len() == 1 && a.outputs[0].is_empty())
        .collect();

    let non_trivial_k_axis = k_axes
        .iter()
        .filter(|a| {
            !input_shapes[0][a.inputs[0][0]].is_one() || !input_shapes[1][a.inputs[1][0]].is_one()
        })
        .collect::<TVec<_>>();

    let k_axis = if non_trivial_k_axis.len() > 1 {
        // TODO: handle case where multiple consecutive k in the same order in both input.
        return Ok(AxesOrPatch::NotAMatMul(
            "multiple k-axis candidate found",
            non_trivial_k_axis.into_iter().cloned().collect_vec(),
        ));
    } else {
        non_trivial_k_axis.first().copied().or_else(|| k_axes.first()).copied()
    };
    let Some(k_axis) = k_axis else {
        return Ok(AxesOrPatch::Patch(inject_k_axis(op, model, node)?));
    };

    let mut possible_m_axes: Vec<_> = op
        .axes
        .iter_all_axes()
        .filter(|a| {
            a.inputs[0].len() == 1
                && (a.inputs[1].is_empty() || input_shapes[1][a.inputs[1][0]].is_one())
                && (a.outputs[0].len() == 1
                    || (input_shapes[0][a.inputs[0][0]].is_one() && a.inputs[1].is_empty()))
        })
        .collect();

    // Prioritize obvious m-axes
    if possible_m_axes.iter().any(|a| !a.outputs[0].is_empty()) {
        possible_m_axes.retain(|a| !a.outputs[0].is_empty());
    }

    let m_axis = possible_m_axes
        .into_iter()
        .max_by_key(|a| input_shapes[0][a.inputs[0][0]].as_i64().unwrap_or(i64::MAX));

    let Some(m_axis) = m_axis else {
        return Ok(AxesOrPatch::Patch(inject_m_or_n_axis(op, model, node, false)?));
    };

    let n_axis = op
        .axes
        .iter_all_axes()
        .filter(|a| {
            (a.inputs[0].is_empty() || input_shapes[0][a.inputs[0][0]].is_one())
                && a.inputs[1].len() == 1
                && a.outputs[0].len() == 1
                && *a != m_axis
        })
        .max_by_key(|a| input_shapes[1][a.inputs[1][0]].as_i64().unwrap_or(i64::MAX));
    let Some(n_axis) = n_axis else {
        return Ok(AxesOrPatch::Patch(inject_m_or_n_axis(op, model, node, true)?));
    };
    for axis in op.axes.iter_all_axes() {
        let one = TDim::one();
        let in_left =
            axis.inputs[0].first().map(|pos| &input_shapes[0][*pos]).unwrap_or(&one) != &one;
        let in_right =
            axis.inputs[1].first().map(|pos| &input_shapes[1][*pos]).unwrap_or(&one) != &one;
        let in_out = axis.outputs[0].first().map(|pos| &output_shape[*pos]).unwrap_or(&one) != &one;
        if (in_left ^ in_right) && !in_out {
            return Ok(AxesOrPatch::NotAMatMul(
                "non trivial single-side disappearing axis",
                vec![axis],
            ));
        }
    }
    let m = input_shapes[0][m_axis.inputs[0][0]].clone();
    let k = input_shapes[0][k_axis.inputs[0][0]].clone();
    let n = input_shapes[1][n_axis.inputs[1][0]].clone();
    Ok(AxesOrPatch::Annotated(EinSumAnnotatedAsMatMul { op, m_axis, k_axis, n_axis, m, k, n }))
}

pub(super) fn inject_k_axis(
    op: &EinSum,
    model: &TypedModel,
    node: &TypedNode,
) -> TractResult<TypedModelPatch> {
    let mut new_axes = op.axes.clone();
    let name = &node.name;
    let mut patch = TypedModelPatch::new("inject k axis");
    let mut wire = patch.taps(model, &node.inputs)?;
    let repr = new_axes.available_label();
    new_axes = new_axes.with_extra_axis(repr, InOut::In(0), 0)?.with_extra_axis_occurency(
        repr,
        InOut::In(1),
        0,
    )?;
    wire[0] = patch.wire_node(format!("{name}.add_k.0"), AxisOp::Add(0), &[wire[0]])?[0];
    wire[1] = patch.wire_node(format!("{name}.add_k.1"), AxisOp::Add(0), &[wire[1]])?[0];
    wire = patch.wire_node(&node.name, EinSum { axes: new_axes, ..op.clone() }, &wire)?;
    patch.shunt_outside(model, node.id.into(), wire[0])?;
    Ok(patch)
}

pub(super) fn inject_m_or_n_axis(
    op: &EinSum,
    model: &TypedModel,
    node: &TypedNode,
    is_n: bool,
) -> TractResult<TypedModelPatch> {
    let input_to_fix = is_n as usize;
    let label = if is_n { "n" } else { "m" };
    let name = &node.name;
    let mut patch = TypedModelPatch::new("Injecting m or n axis");
    let mut wire = patch.taps(model, &node.inputs)?;
    let repr = op.axes.available_label();
    let new_axes = op
        .axes
        .clone()
        .with_extra_axis(repr, InOut::In(input_to_fix), 0)?
        .with_extra_axis_occurency(repr, InOut::Out(0), 0)?;
    wire[input_to_fix] =
        patch.wire_node(format!("{name}.add_{label}"), AxisOp::Add(0), &[wire[input_to_fix]])?[0];
    wire = patch.wire_node(name, EinSum { axes: new_axes, ..op.clone() }, &wire)?;
    wire = patch.wire_node(&node.name, AxisOp::Rm(0), &wire)?;
    patch.shunt_outside(model, node.id.into(), wire[0])?;
    Ok(patch)
}

fn wire_axes_fix(
    patch: &mut TypedModelPatch,
    name: &str,
    var: &str,
    mapping: &AxesMapping,
    mut outlet: TVec<OutletId>,
) -> TractResult<TVec<OutletId>> {
    for (ix, axis_op) in mapping.translate_to_axis_ops()?.into_iter().enumerate() {
        outlet = patch.wire_node(format!("{name}.fix_{var}.{ix})"), axis_op, &outlet)?;
    }
    Ok(outlet)
}

fn dequant(
    model: &TypedModel,
    node: &TypedNode,
    op: EinSumAnnotatedAsMatMul,
) -> TractResult<Option<TypedModelPatch>> {
    let name = &node.name;
    let mut patch = TypedModelPatch::new("Dequantizing einsum");

    let mut taps = patch.taps(model, &node.inputs)?;
    for ab in [0, 1] {
        let scale_input = 4 + ab * 2;
        if !patch.outlet_fact(taps[scale_input])?.shape.volume().is_one() {
            let q_axis_in_output = op.axes.axis((InOut::In(scale_input), 0))?.outputs[0][0];
            let output_rank = node.outputs[0].fact.rank();
            for i in 1..(output_rank - q_axis_in_output) {
                taps[scale_input] = patch.wire_node(
                    format!("{name}.scale_input{ab}_axis_fix_{i}"),
                    AxisOp::Add(i),
                    &[taps[scale_input]],
                )?[0];
            }
        }
    }

    let [mut a, mut b, bias, mut a0, a_scale, mut b0, b_scale, c0, c_scale] = *taps else {
        bail!("Expect exactly 9 inputs")
    };

    wire_ensure_q8_flavour(&mut patch, &node.name, &mut a, "a", &mut a0, i8::datum_type())?;
    wire_ensure_q8_flavour(&mut patch, &node.name, &mut b, "b", &mut b0, i8::datum_type())?;

    let mut output = patch.wire_node(
        &node.name,
        EinSum {
            q_params: None,
            axes: op.axes.extract_sub_mapping(&[0, 1], &[0])?,
            operating_dt: op.operating_dt,
        },
        &[a, b],
    )?;

    let a_i32 = patch.wire_node(format!("{name}.a_as_i32"), cast(i32::datum_type()), &[a])?[0];
    let b_i32 = patch.wire_node(format!("{name}.b_as_i32"), cast(i32::datum_type()), &[b])?[0];
    let sum_a = patch.wire_node(
        format!("{name}.sum_a"),
        Reduce::new(tvec!(op.k_axis.inputs[0][0]), Reducer::Sum),
        &[a_i32],
    )?;
    let sum_b = patch.wire_node(
        format!("{name}.sum_b"),
        Reduce::new(tvec!(op.k_axis.inputs[1][0]), Reducer::Sum),
        &[b_i32],
    )?;

    let sum_a =
        wire_axes_fix(&mut patch, name, "sum_a", &op.axes.extract_sub_mapping(&[0], &[0])?, sum_a)?;
    let sum_b =
        wire_axes_fix(&mut patch, name, "sum_b", &op.axes.extract_sub_mapping(&[1], &[0])?, sum_b)?;
    let bias = tvec!(bias);
    let bias =
        wire_axes_fix(&mut patch, name, "bias", &op.axes.extract_sub_mapping(&[2], &[0])?, bias)?;

    let abc_scale = combine_scales(&mut patch, name, a_scale, b_scale, c_scale)?;

    output = patch.wire_node(format!("{name}.add_bias"), add(), &[output[0], bias[0]])?;

    let k = model.outlet_fact(node.inputs[0])?.shape[op.k_axis.inputs[0][0]].clone();
    let output = compensate_zero_points(&mut patch, name, output[0], k, a0, b0, sum_a[0], sum_b[0])
        .context("Zero point compensation")?;
    let output = requant(&mut patch, name, output, op.q_params.unwrap(), abc_scale, c0)?;
    patch.shunt_outside(model, node.id.into(), output)?;
    Ok(Some(patch))
}

fn optimized_mat_mul(
    model: &TypedModel,
    node: &TypedNode,
    op: &EinSumAnnotatedAsMatMul,
) -> TractResult<Option<TypedModelPatch>> {
    let input_facts = model.node_input_facts(node.id)?;
    let input_shapes = op.actual_input_shapes_from_facts(&input_facts)?;
    let must_transpose = input_facts[0].konst.is_none()
        && match (op.m.as_i64(), op.n.as_i64()) {
            (Some(m), Some(n)) => m < n,
            (None, Some(n)) => n >= 8,
            _ => false,
        };
    if must_transpose {
        return Ok(Some(transpose(op, model, node)?));
    }

    if input_facts[0].konst.is_some()
        && (input_facts[0].datum_type.is_number()
            || input_facts[0].opaque_fact().is_some_and(|of| of.is::<BlockQuantFact>()))
    {
        return Ok(None);
    }

    let mut patch = TypedModelPatch::new("Einsum to OptMatMul");
    let name = &node.name;
    let taps = patch.taps(model, &node.inputs)?;
    let (a, b, mmms, mode_picker) =
        wire_packing(&mut patch, name, &taps[0..2], op).context("Wiring packing")?;

    let mut c_to_a_axis_mapping = tvec!();
    let mut c_to_b_axis_mapping = tvec!();
    for axis in op
        .op
        .axes
        .iter_all_axes()
        .filter(|&axis| ![op.m_axis, op.k_axis, op.n_axis].contains(&axis))
    {
        if let (&[c], &[a]) = (&*axis.outputs[0], &*axis.inputs[0]) {
            if input_shapes[0][a] != 1.to_dim() {
                let a = a - (a > op.a_m()) as usize - (a > op.a_k()) as usize;
                c_to_a_axis_mapping.push((c, a));
            }
        }
        if let (&[c], &[b]) = (&*axis.outputs[0], &*axis.inputs[1]) {
            if input_shapes[1][b] != 1.to_dim() {
                let b = b - (b > op.b_n()) as usize - (b > op.b_k()) as usize;
                c_to_b_axis_mapping.push((c, b));
            }
        }
    }

    let c_fact = op.output_facts(&input_facts)?.remove(0);
    let geo = AddMatMulGeometry {
        k: op.k.clone(),
        c_to_a_axis_mapping: MapOutputAxisToInput(c_to_a_axis_mapping),
        c_to_b_axis_mapping: MapOutputAxisToInput(c_to_b_axis_mapping),
    };
    let (mmms, packings, extractor): (Vec<_>, Vec<_>, Vec<_>) = multiunzip(mmms);
    let outputs = mmms.iter().map(|mmm| unsafe { mmm.c_view(op.c_m(), op.c_n()) }).collect();
    let trivial_packing =
        mmms.len() == 1 && packings[0] == 0 && patch.outlet_fact(a)?.opaque_fact.is_none();
    let opt = OptMatMul::new(
        mmms,
        mode_picker,
        c_fact,
        op.c_m(),
        op.c_n(),
        vec![
            ProtoFusedSpec::AddMatMul {
                geo,
                a: 0,
                b: 1,
                packings: izip!(packings, extractor).collect_vec(),
            },
            ProtoFusedSpec::Store(outputs),
        ],
        trivial_packing,
    )
    .context("Creating OptMatMul")?;
    let output = patch.wire_node(name, opt, &[a, b])?[0];
    patch.shunt_outside(model, node.id.into(), output)?;
    Ok(Some(patch))
}
