# This file is not meant for public use and will be removed in SciPy v2.0.0.

from typing_extensions import deprecated

import numpy as np

__all__ = ["LinAlgError", "cho_factor", "cho_solve", "cho_solve_banded", "cholesky", "cholesky_banded", "get_lapack_funcs"]

@deprecated("will be removed in SciPy v2.0.0")
class LinAlgError(np.linalg.LinAlgError): ...

@deprecated("will be removed in SciPy v2.0.0")
def get_lapack_funcs(names: object, arrays: object = ..., dtype: object = ..., ilp64: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def cholesky(a: object, lower: object = ..., overwrite_a: object = ..., check_finite: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def cho_factor(a: object, lower: object = ..., overwrite_a: object = ..., check_finite: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def cho_solve(c_and_lower: object, b: object, overwrite_b: object = ..., check_finite: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def cholesky_banded(ab: object, overwrite_ab: object = ..., lower: object = ..., check_finite: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def cho_solve_banded(cb_and_lower: object, b: object, overwrite_b: object = ..., check_finite: object = ...) -> object: ...
