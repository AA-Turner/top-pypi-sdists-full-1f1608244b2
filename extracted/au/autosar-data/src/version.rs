use crate::AutosarDataError;
use pyo3::prelude::*;
use std::str::FromStr;

#[allow(non_camel_case_types)]
#[pyclass(eq, eq_int, ord, module = "autosar_data.autosar_data")]
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub(crate) enum AutosarVersion {
    #[pyo3(name = "AUTOSAR_4_0_1")]
    Autosar_4_0_1,
    #[pyo3(name = "AUTOSAR_4_0_2")]
    Autosar_4_0_2,
    #[pyo3(name = "AUTOSAR_4_0_3")]
    Autosar_4_0_3,
    #[pyo3(name = "AUTOSAR_4_1_1")]
    Autosar_4_1_1,
    #[pyo3(name = "AUTOSAR_4_1_2")]
    Autosar_4_1_2,
    #[pyo3(name = "AUTOSAR_4_1_3")]
    Autosar_4_1_3,
    #[pyo3(name = "AUTOSAR_4_2_1")]
    Autosar_4_2_1,
    #[pyo3(name = "AUTOSAR_4_2_2")]
    Autosar_4_2_2,
    #[pyo3(name = "AUTOSAR_4_3_0")]
    Autosar_4_3_0,
    #[pyo3(name = "AUTOSAR_00042")]
    Autosar_00042,
    #[pyo3(name = "AUTOSAR_00043")]
    Autosar_00043,
    #[pyo3(name = "AUTOSAR_00044")]
    Autosar_00044,
    #[pyo3(name = "AUTOSAR_00045")]
    Autosar_00045,
    #[pyo3(name = "AUTOSAR_00046")]
    Autosar_00046,
    #[pyo3(name = "AUTOSAR_00047")]
    Autosar_00047,
    #[pyo3(name = "AUTOSAR_00048")]
    Autosar_00048,
    #[pyo3(name = "AUTOSAR_00049")]
    Autosar_00049,
    #[pyo3(name = "AUTOSAR_00050")]
    Autosar_00050,
    #[pyo3(name = "AUTOSAR_00051")]
    Autosar_00051,
    #[pyo3(name = "AUTOSAR_00052")]
    Autosar_00052,
    #[pyo3(name = "AUTOSAR_00053")]
    Autosar_00053,
    #[pyo3(name = "LATEST")]
    Latest,
}

#[pymethods]
impl AutosarVersion {
    #[new]
    fn new(input: &str) -> PyResult<AutosarVersion> {
        let spec_ver =
            autosar_data_specification::AutosarVersion::from_str(input).or_else(|_| {
                PyResult::Err(AutosarDataError::new_err(format!(
                    "Cannot convert \"{input}\" to AutosarVersion"
                )))
            })?;
        Ok(spec_ver.into())
    }

    fn __str__(&self) -> String {
        let ver: autosar_data_specification::AutosarVersion = (*self).into();
        ver.to_string()
    }
}

impl From<AutosarVersion> for autosar_data_specification::AutosarVersion {
    fn from(val: AutosarVersion) -> Self {
        match val {
            AutosarVersion::Autosar_4_0_1 => Self::Autosar_4_0_1,
            AutosarVersion::Autosar_4_0_2 => Self::Autosar_4_0_2,
            AutosarVersion::Autosar_4_0_3 => Self::Autosar_4_0_3,
            AutosarVersion::Autosar_4_1_1 => Self::Autosar_4_1_1,
            AutosarVersion::Autosar_4_1_2 => Self::Autosar_4_1_2,
            AutosarVersion::Autosar_4_1_3 => Self::Autosar_4_1_3,
            AutosarVersion::Autosar_4_2_1 => Self::Autosar_4_2_1,
            AutosarVersion::Autosar_4_2_2 => Self::Autosar_4_2_2,
            AutosarVersion::Autosar_4_3_0 => Self::Autosar_4_3_0,
            AutosarVersion::Autosar_00042 => Self::Autosar_00042,
            AutosarVersion::Autosar_00043 => Self::Autosar_00043,
            AutosarVersion::Autosar_00044 => Self::Autosar_00044,
            AutosarVersion::Autosar_00045 => Self::Autosar_00045,
            AutosarVersion::Autosar_00046 => Self::Autosar_00046,
            AutosarVersion::Autosar_00047 => Self::Autosar_00047,
            AutosarVersion::Autosar_00048 => Self::Autosar_00048,
            AutosarVersion::Autosar_00049 => Self::Autosar_00049,
            AutosarVersion::Autosar_00050 => Self::Autosar_00050,
            AutosarVersion::Autosar_00051 => Self::Autosar_00051,
            AutosarVersion::Autosar_00052 => Self::Autosar_00052,
            AutosarVersion::Autosar_00053 => Self::Autosar_00053,
            AutosarVersion::Latest => Self::LATEST,
        }
    }
}

impl From<autosar_data_specification::AutosarVersion> for AutosarVersion {
    fn from(value: autosar_data_specification::AutosarVersion) -> Self {
        match value {
            autosar_data_specification::AutosarVersion::Autosar_4_0_1 => Self::Autosar_4_0_1,
            autosar_data_specification::AutosarVersion::Autosar_4_0_2 => Self::Autosar_4_0_2,
            autosar_data_specification::AutosarVersion::Autosar_4_0_3 => Self::Autosar_4_0_3,
            autosar_data_specification::AutosarVersion::Autosar_4_1_1 => Self::Autosar_4_1_1,
            autosar_data_specification::AutosarVersion::Autosar_4_1_2 => Self::Autosar_4_1_2,
            autosar_data_specification::AutosarVersion::Autosar_4_1_3 => Self::Autosar_4_1_3,
            autosar_data_specification::AutosarVersion::Autosar_4_2_1 => Self::Autosar_4_2_1,
            autosar_data_specification::AutosarVersion::Autosar_4_2_2 => Self::Autosar_4_2_2,
            autosar_data_specification::AutosarVersion::Autosar_4_3_0 => Self::Autosar_4_3_0,
            autosar_data_specification::AutosarVersion::Autosar_00042 => Self::Autosar_00042,
            autosar_data_specification::AutosarVersion::Autosar_00043 => Self::Autosar_00043,
            autosar_data_specification::AutosarVersion::Autosar_00044 => Self::Autosar_00044,
            autosar_data_specification::AutosarVersion::Autosar_00045 => Self::Autosar_00045,
            autosar_data_specification::AutosarVersion::Autosar_00046 => Self::Autosar_00046,
            autosar_data_specification::AutosarVersion::Autosar_00047 => Self::Autosar_00047,
            autosar_data_specification::AutosarVersion::Autosar_00048 => Self::Autosar_00048,
            autosar_data_specification::AutosarVersion::Autosar_00049 => Self::Autosar_00049,
            autosar_data_specification::AutosarVersion::Autosar_00050 => Self::Autosar_00050,
            autosar_data_specification::AutosarVersion::Autosar_00051 => Self::Autosar_00051,
            autosar_data_specification::AutosarVersion::Autosar_00052 => Self::Autosar_00052,
            autosar_data_specification::AutosarVersion::Autosar_00053 => Self::Autosar_00053,

            _ => Self::Autosar_00053,
        }
    }
}

impl std::fmt::Debug for AutosarVersion {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(self.__pyo3__repr__())
    }
}
