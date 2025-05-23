use std::convert::Infallible;
use std::fmt::Display;
use std::fmt::Formatter;
use std::fmt::Result as FmtResult;
use std::rc::Rc;
use std::str::FromStr;
use std::string::ToString;

use pyo3::class::basic::CompareOp;
use pyo3::class::gc::PyVisit;
use pyo3::exceptions::PyValueError;
use pyo3::gc::PyTraverseError;
use pyo3::prelude::*;
use pyo3::types::PyAny;
use pyo3::types::PyIterator;
use pyo3::types::PyList;
use pyo3::types::PyString;
use pyo3::AsPyPointer;
use pyo3::PyTypeInfo;

use super::id::Ident;
use super::xref::XrefList;
use crate::utils::ClonePy;
use crate::utils::EqPy;
use crate::utils::IntoPy;

// --- Module export ---------------------------------------------------------

#[pymodule]
#[pyo3(name = "syn")]
pub fn init<'py>(_py: Python<'py>, m: &Bound<'py, PyModule>) -> PyResult<()> {
    m.add_class::<self::Synonym>()?;
    m.add("__name__", "fastobo.syn")?;
    Ok(())
}

// --- SynonymScope ----------------------------------------------------------

// #[pyclass(module = "fastobo.syn")] // FIXME(@althonos): probably not needed since it is not exposed.
#[derive(Clone, ClonePy, Debug, Eq, PartialEq, EqPy)]
pub struct SynonymScope {
    inner: fastobo::ast::SynonymScope,
}

impl SynonymScope {
    pub fn new(scope: fastobo::ast::SynonymScope) -> Self {
        Self { inner: scope }
    }
}

impl Display for SynonymScope {
    fn fmt(&self, f: &mut Formatter) -> FmtResult {
        self.inner.fmt(f)
    }
}

impl From<fastobo::ast::SynonymScope> for SynonymScope {
    fn from(scope: fastobo::ast::SynonymScope) -> Self {
        Self::new(scope)
    }
}

impl From<SynonymScope> for fastobo::ast::SynonymScope {
    fn from(scope: SynonymScope) -> Self {
        scope.inner
    }
}

impl FromStr for SynonymScope {
    type Err = PyErr;
    fn from_str(s: &str) -> PyResult<Self> {
        match s {
            "EXACT" => Ok(Self::new(fastobo::ast::SynonymScope::Exact)),
            "BROAD" => Ok(Self::new(fastobo::ast::SynonymScope::Broad)),
            "NARROW" => Ok(Self::new(fastobo::ast::SynonymScope::Narrow)),
            "RELATED" => Ok(Self::new(fastobo::ast::SynonymScope::Related)),
            invalid => Err(PyValueError::new_err(format!(
                "expected 'EXACT', 'BROAD', 'NARROW' or 'RELATED', found {:?}",
                invalid
            ))),
        }
    }
}

impl IntoPy<SynonymScope> for fastobo::ast::SynonymScope {
    fn into_py(self, _py: Python) -> SynonymScope {
        SynonymScope::from(self)
    }
}

impl IntoPy<fastobo::ast::SynonymScope> for SynonymScope {
    fn into_py(self, _py: Python) -> fastobo::ast::SynonymScope {
        self.inner
    }
}

impl ToPyObject for SynonymScope {
    fn to_object(&self, py: Python) -> PyObject {
        self.to_string().to_object(py)
    }
}

impl<'py> IntoPyObject<'py> for &SynonymScope {
    type Error = Infallible;
    type Target = PyString;
    type Output = Bound<'py, PyString>;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self.inner {
            fastobo::ast::SynonymScope::Exact => Ok(pyo3::intern!(py, "EXACT").clone()),
            fastobo::ast::SynonymScope::Broad => Ok(pyo3::intern!(py, "BROAD").clone()),
            fastobo::ast::SynonymScope::Narrow => Ok(pyo3::intern!(py, "NARROW").clone()),
            fastobo::ast::SynonymScope::Related => Ok(pyo3::intern!(py, "RELATED").clone()),
            _ => unimplemented!(),
        }
    }
}

impl<'py> IntoPyObject<'py> for SynonymScope {
    type Error = Infallible;
    type Target = PyString;
    type Output = Bound<'py, PyString>;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (&self).into_pyobject(py)
    }
}

// --- Synonym ---------------------------------------------------------------

#[pyclass(module = "fastobo.syn")]
#[derive(Debug, EqPy)]
pub struct Synonym {
    desc: fastobo::ast::QuotedString,
    scope: SynonymScope,
    ty: Option<Ident>,
    #[pyo3(get, set)]
    xrefs: Py<XrefList>,
}

impl ClonePy for Synonym {
    fn clone_py(&self, py: Python) -> Self {
        Self {
            desc: self.desc.clone(),
            scope: self.scope.clone_py(py),
            ty: self.ty.clone_py(py),
            xrefs: self.xrefs.clone_py(py),
        }
    }
}

impl Display for Synonym {
    fn fmt(&self, f: &mut Formatter) -> FmtResult {
        let syn: fastobo::ast::Synonym = Python::with_gil(|py| self.clone_py(py).into_py(py));
        syn.fmt(f)
    }
}

impl IntoPy<Synonym> for fastobo::ast::Synonym {
    fn into_py(mut self, py: Python) -> Synonym {
        Synonym {
            desc: std::mem::take(self.description_mut()),
            scope: SynonymScope::new(self.scope().clone()),
            ty: self.ty().map(|id| id.clone().into_py(py)),
            xrefs: Py::new(py, std::mem::take(self.xrefs_mut()).into_py(py))
                .expect("failed allocating memory on Python heap"),
        }
    }
}

impl IntoPy<fastobo::ast::Synonym> for Synonym {
    fn into_py(self, py: Python) -> fastobo::ast::Synonym {
        fastobo::ast::Synonym::with_type_and_xrefs(
            self.desc,
            self.scope.inner,
            self.ty.map(|ty| ty.into_py(py)),
            (&*self.xrefs.bind(py).borrow()).into_py(py),
        )
    }
}

#[pymethods]
impl Synonym {
    #[new]
    #[pyo3(signature = (desc, scope, ty = None, xrefs = None))]
    pub fn __init__<'py>(
        desc: String,
        scope: &str,
        ty: Option<Ident>,
        xrefs: Option<Bound<'py, PyAny>>,
    ) -> PyResult<Self> {
        let xrefs = Python::with_gil(|py| {
            let list = xrefs
                .map(|x| XrefList::collect(py, &x))
                .transpose()?
                .unwrap_or_default();
            Py::new(py, list)
        })?;
        Ok(Self {
            desc: fastobo::ast::QuotedString::new(desc),
            scope: SynonymScope::from_str(scope)?,
            xrefs,
            ty,
        })
    }

    fn __repr__(&self) -> PyResult<PyObject> {
        impl_repr!(self, Synonym(self.desc, self.scope))
    }

    fn __str__(&self) -> PyResult<String> {
        Ok(self.to_string())
    }

    fn __richcmp__<'py>(&self, other: &Bound<'py, PyAny>, op: CompareOp) -> PyResult<PyObject> {
        impl_richcmp_py!(
            self,
            other,
            op,
            self.desc && self.scope && self.ty && self.xrefs
        )
    }

    #[getter]
    pub fn get_desc(&self) -> PyResult<String> {
        Ok(self.desc.as_str().to_owned())
    }

    #[setter]
    pub fn set_desc(&mut self, desc: String) -> PyResult<()> {
        self.desc = fastobo::ast::QuotedString::new(desc);
        Ok(())
    }

    #[getter]
    pub fn get_scope(&self) -> PyResult<String> {
        Ok(self.scope.to_string())
    }

    #[setter]
    pub fn set_scope(&mut self, scope: &str) -> PyResult<()> {
        self.scope = scope.parse()?;
        Ok(())
    }

    #[getter]
    pub fn get_type(&self) -> PyResult<Option<&Ident>> {
        Ok(self.ty.as_ref())
    }

    #[setter]
    pub fn set_type(&mut self, ty: Option<Ident>) -> PyResult<()> {
        self.ty = ty;
        Ok(())
    }
}
