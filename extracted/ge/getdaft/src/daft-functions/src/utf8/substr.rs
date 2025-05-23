use common_error::{DaftError, DaftResult};
use daft_core::{
    prelude::{DataType, Field, Schema},
    series::Series,
};
use daft_dsl::{
    functions::{ScalarFunction, ScalarUDF},
    ExprRef,
};
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub struct Utf8Substr {}

#[typetag::serde]
impl ScalarUDF for Utf8Substr {
    fn evaluate(&self, inputs: daft_dsl::functions::FunctionArgs<Series>) -> DaftResult<Series> {
        let inner = inputs.into_inner();
        self.evaluate_from_series(&inner)
    }

    fn name(&self) -> &'static str {
        "substr"
    }

    fn to_field(&self, inputs: &[ExprRef], schema: &Schema) -> DaftResult<Field> {
        match inputs {
            [data, start, length] => {
                let data = data.to_field(schema)?;
                let start = start.to_field(schema)?;
                let length = length.to_field(schema)?;

                if data.dtype == DataType::Utf8
                    && start.dtype.is_integer()
                    && (length.dtype.is_integer() || length.dtype.is_null())
                {
                    Ok(Field::new(data.name, DataType::Utf8))
                } else {
                    Err(DaftError::TypeError(format!(
                        "Expects inputs to substr to be utf8, integer and integer or null but received {}, {} and {}",
                        data.dtype, start.dtype, length.dtype
                    )))
                }
            }
            _ => Err(DaftError::SchemaMismatch(format!(
                "Expected 3 input args, got {}",
                inputs.len()
            ))),
        }
    }

    fn evaluate_from_series(&self, inputs: &[Series]) -> DaftResult<Series> {
        match inputs {
            [data, start, length] => data.utf8_substr(start, length),
            _ => Err(DaftError::ValueError(format!(
                "Expected 3 input args, got {}",
                inputs.len()
            ))),
        }
    }
}

#[must_use]
pub fn utf8_substr(input: ExprRef, start: ExprRef, length: ExprRef) -> ExprRef {
    ScalarFunction::new(Utf8Substr {}, vec![input, start, length]).into()
}
