use pyo3::{prelude::*, wrap_pymodule};

pub mod triangle_mesh;

#[cfg(not(tarpaulin_include))]
#[pymodule]
pub(crate) fn geometry(m: Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pymodule!(triangle_mesh::triangle_mesh))?;
    Ok(())
}
