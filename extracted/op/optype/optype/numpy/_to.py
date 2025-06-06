import sys
from collections.abc import Sequence as Seq
from typing import Any, Literal, TypeAlias

if sys.version_info >= (3, 13):
    from typing import TypeAliasType, TypeVar
else:
    from typing_extensions import TypeAliasType, TypeVar

import numpy as np

import optype.numpy.compat as npc
from ._array import CanArray0D, CanArray1D, CanArray2D, CanArray3D, CanArrayND, Matrix
from ._compat import NP22
from ._sequence_nd import SequenceND as SeqND
from optype._core._just import JustComplex, JustFloat, JustInt

__all__ = [  # noqa: RUF022
    "ToScalar",
    "ToArray1D", "ToArrayStrict1D",
    "ToArray2D", "ToArrayStrict2D",
    "ToArray3D", "ToArrayStrict3D",
    "ToArrayND",

    "ToFalse", "ToTrue",
    "ToJustFalse", "ToJustTrue",

    "ToBool", "ToJustBool",
    "ToBool1D", "ToJustBool1D", "ToBoolStrict1D", "ToJustBoolStrict1D",
    "ToBool2D", "ToJustBool2D", "ToBoolStrict2D", "ToJustBoolStrict2D",
    "ToBool3D", "ToJustBool3D", "ToBoolStrict3D", "ToJustBoolStrict3D",
    "ToBoolND", "ToJustBoolND",

    "ToInt", "ToJustInt",
    "ToInt1D", "ToJustInt1D", "ToIntStrict1D", "ToJustIntStrict1D",
    "ToInt2D", "ToJustInt2D", "ToIntStrict2D", "ToJustIntStrict2D",
    "ToInt3D", "ToJustInt3D", "ToIntStrict3D", "ToJustIntStrict3D",
    "ToIntND", "ToJustIntND",

    "ToJustInt64",
    "ToJustInt64_1D", "ToJustInt64Strict1D",
    "ToJustInt64_2D", "ToJustInt64Strict2D",
    "ToJustInt64_3D", "ToJustInt64Strict3D",
    "ToJustInt64_ND",

    "ToFloat64", "ToJustFloat64",
    "ToFloat64_1D", "ToJustFloat64_1D", "ToFloat64Strict1D", "ToJustFloat64Strict1D",
    "ToFloat64_2D", "ToJustFloat64_2D", "ToFloat64Strict2D", "ToJustFloat64Strict2D",
    "ToFloat64_3D", "ToJustFloat64_3D", "ToFloat64Strict3D", "ToJustFloat64Strict3D",
    "ToFloat64_ND", "ToJustFloat64_ND",

    "ToFloat", "ToJustFloat",
    "ToFloat1D", "ToJustFloat1D", "ToFloatStrict1D", "ToJustFloatStrict1D",
    "ToFloat2D", "ToJustFloat2D", "ToFloatStrict2D", "ToJustFloatStrict2D",
    "ToFloat3D", "ToJustFloat3D", "ToFloatStrict3D", "ToJustFloatStrict3D",
    "ToFloatND", "ToJustFloatND",

    "ToComplex128", "ToJustComplex128",
    "ToComplex128_1D", "ToJustComplex128_1D",
    "ToComplex128_2D", "ToJustComplex128_2D",
    "ToComplex128_3D", "ToJustComplex128_3D",
    "ToComplex128_ND", "ToJustComplex128_ND",
    "ToComplex128Strict1D", "ToJustComplex128Strict1D",
    "ToComplex128Strict2D", "ToJustComplex128Strict2D",
    "ToComplex128Strict3D", "ToJustComplex128Strict3D",

    "ToComplex", "ToJustComplex",
    "ToComplex1D", "ToJustComplex1D", "ToComplexStrict1D", "ToJustComplexStrict1D",
    "ToComplex2D", "ToJustComplex2D", "ToComplexStrict2D", "ToJustComplexStrict2D",
    "ToComplex3D", "ToJustComplex3D", "ToComplexStrict3D", "ToJustComplexStrict3D",
    "ToComplexND", "ToJustComplexND",
]  # fmt: skip


def __dir__() -> list[str]:
    return __all__


###


_PyBool: TypeAlias = bool | Literal[0, 1]  # 0 and 1 are sometimes used as bool values
_PyScalar: TypeAlias = complex | bytes | str  # `complex` equivs `complex | float | int`

T = TypeVar("T", default=_PyScalar)
SCT = TypeVar("SCT", bound=np.generic, default=Any)

_To0D = TypeAliasType("_To0D", T | SCT | CanArray0D[SCT], type_params=(T, SCT))
_To1D = TypeAliasType(
    "_To1D",
    CanArrayND[SCT] | Seq[_To0D[T, SCT]],
    type_params=(T, SCT),
)
_To2D = TypeAliasType(
    "_To2D",
    CanArrayND[SCT] | Seq[_To1D[T, SCT]],
    type_params=(T, SCT),
)
_To3D = TypeAliasType(
    "_To3D",
    CanArrayND[SCT] | Seq[_To2D[T, SCT]],
    type_params=(T, SCT),
)
_ToND = TypeAliasType(
    "_ToND",
    CanArrayND[SCT] | SeqND[CanArrayND[SCT] | _To0D[T, SCT]],
    type_params=(T, SCT),
)

_ToStrict1D = TypeAliasType(
    "_ToStrict1D",
    CanArray1D[SCT] | Seq[_To0D[T, SCT]],
    type_params=(T, SCT),
)
_ToStrict2D = TypeAliasType(
    "_ToStrict2D",
    CanArray2D[SCT] | Seq[_ToStrict1D[T, SCT]] | Matrix[SCT],
    type_params=(T, SCT),
)
_ToStrict3D = TypeAliasType(
    "_ToStrict3D",
    CanArray3D[SCT] | Seq[_ToStrict2D[T, SCT]],
    type_params=(T, SCT),
)


###


# TODO: Export and document.

integer_co = TypeAliasType("integer_co", npc.integer | np.bool_)
floating_co = TypeAliasType("floating_co", npc.floating | integer_co)
complexfloating_co = TypeAliasType("complexfloating_co", npc.number | np.bool_)
float64_co = TypeAliasType(
    "float64_co",
    npc.floating64 | npc.floating32 | npc.floating16 | integer_co,
)
complex128_co = TypeAliasType(
    "complex128_co",
    npc.number64 | npc.number32 | npc.number16 | integer_co,
)


###


# scalar- and array-likes, with "coercible" shape-types

ToScalar: TypeAlias = _PyScalar | np.generic
ToArray1D: TypeAlias = _To1D[T, SCT]
ToArray2D: TypeAlias = _To2D[T, SCT]
ToArray3D: TypeAlias = _To3D[T, SCT]
ToArrayND: TypeAlias = _ToND[T, SCT]

if NP22:
    ToFalse = TypeAliasType("ToFalse", "Literal[False, 0] | np.bool[Literal[False]]")
    ToTrue = TypeAliasType("ToTrue", "Literal[True, 1] | np.bool[Literal[True]]")

    ToJustFalse = TypeAliasType(
        "ToJustFalse",
        "Literal[False] | np.bool[Literal[False]]",
    )
    ToJustTrue = TypeAliasType("ToJustTrue", "Literal[True] | np.bool[Literal[True]]")
else:
    ToFalse = TypeAliasType("ToFalse", Literal[False, 0])
    ToTrue = TypeAliasType("ToTrue", Literal[True, 1])

    ToJustFalse = TypeAliasType("ToJustFalse", Literal[False])
    ToJustTrue = TypeAliasType("ToJustTrue", Literal[True])

ToBool: TypeAlias = _PyBool | np.bool_
ToBool1D: TypeAlias = _To1D[_PyBool, np.bool_]
ToBool2D: TypeAlias = _To2D[_PyBool, np.bool_]
ToBool3D: TypeAlias = _To3D[_PyBool, np.bool_]
ToBoolND: TypeAlias = _ToND[_PyBool, np.bool_]

ToInt: TypeAlias = int | integer_co
ToInt1D: TypeAlias = _To1D[int, integer_co]
ToInt2D: TypeAlias = _To2D[int, integer_co]
ToInt3D: TypeAlias = _To3D[int, integer_co]
ToIntND: TypeAlias = _ToND[int, integer_co]

ToFloat64: TypeAlias = float | float64_co
ToFloat64_1D: TypeAlias = _To1D[float, float64_co]
ToFloat64_2D: TypeAlias = _To2D[float, float64_co]
ToFloat64_3D: TypeAlias = _To3D[float, float64_co]
ToFloat64_ND: TypeAlias = _ToND[float, float64_co]

ToFloat: TypeAlias = float | floating_co
ToFloat1D: TypeAlias = _To1D[float, floating_co]
ToFloat2D: TypeAlias = _To2D[float, floating_co]
ToFloat3D: TypeAlias = _To3D[float, floating_co]
ToFloatND: TypeAlias = _ToND[float, floating_co]

ToComplex: TypeAlias = complex | complexfloating_co
ToComplex1D: TypeAlias = _To1D[complex, complexfloating_co]
ToComplex2D: TypeAlias = _To2D[complex, complexfloating_co]
ToComplex3D: TypeAlias = _To3D[complex, complexfloating_co]
ToComplexND: TypeAlias = _ToND[complex, complexfloating_co]

ToComplex128: TypeAlias = complex | complex128_co
ToComplex128_1D: TypeAlias = _To1D[complex, complex128_co]
ToComplex128_2D: TypeAlias = _To2D[complex, complex128_co]
ToComplex128_3D: TypeAlias = _To3D[complex, complex128_co]
ToComplex128_ND: TypeAlias = _ToND[complex, complex128_co]

# scalar- and array-likes, with "just" that scalar type

ToJustBool: TypeAlias = bool | np.bool_
ToJustBool1D: TypeAlias = _To1D[bool, np.bool_]
ToJustBool2D: TypeAlias = _To2D[bool, np.bool_]
ToJustBool3D: TypeAlias = _To3D[bool, np.bool_]
ToJustBoolND: TypeAlias = _ToND[bool, np.bool_]

ToJustInt64: TypeAlias = JustInt | np.intp
ToJustInt64_1D: TypeAlias = _To1D[JustInt, np.intp]
ToJustInt64_2D: TypeAlias = _To2D[JustInt, np.intp]
ToJustInt64_3D: TypeAlias = _To3D[JustInt, np.intp]
ToJustInt64_ND: TypeAlias = _ToND[JustInt, np.intp]

ToJustInt: TypeAlias = JustInt | npc.integer
ToJustInt1D: TypeAlias = _To1D[JustInt, npc.integer]
ToJustInt2D: TypeAlias = _To2D[JustInt, npc.integer]
ToJustInt3D: TypeAlias = _To3D[JustInt, npc.integer]
ToJustIntND: TypeAlias = _ToND[JustInt, npc.integer]

ToJustFloat64: TypeAlias = JustFloat | npc.floating64
ToJustFloat64_1D: TypeAlias = _To1D[JustFloat, npc.floating64]
ToJustFloat64_2D: TypeAlias = _To2D[JustFloat, npc.floating64]
ToJustFloat64_3D: TypeAlias = _To3D[JustFloat, npc.floating64]
ToJustFloat64_ND: TypeAlias = _ToND[JustFloat, npc.floating64]

ToJustFloat: TypeAlias = JustFloat | npc.floating
ToJustFloat1D: TypeAlias = _To1D[JustFloat, npc.floating]
ToJustFloat2D: TypeAlias = _To2D[JustFloat, npc.floating]
ToJustFloat3D: TypeAlias = _To3D[JustFloat, npc.floating]
ToJustFloatND: TypeAlias = _ToND[JustFloat, npc.floating]

ToJustComplex: TypeAlias = JustComplex | npc.complexfloating
ToJustComplex1D: TypeAlias = _To1D[JustComplex, npc.complexfloating]
ToJustComplex2D: TypeAlias = _To2D[JustComplex, npc.complexfloating]
ToJustComplex3D: TypeAlias = _To3D[JustComplex, npc.complexfloating]
ToJustComplexND: TypeAlias = _ToND[JustComplex, npc.complexfloating]

ToJustComplex128: TypeAlias = JustComplex | npc.complexfloating128
ToJustComplex128_1D: TypeAlias = _To1D[JustComplex, npc.complexfloating128]
ToJustComplex128_2D: TypeAlias = _To2D[JustComplex, npc.complexfloating128]
ToJustComplex128_3D: TypeAlias = _To3D[JustComplex, npc.complexfloating128]
ToJustComplex128_ND: TypeAlias = _ToND[JustComplex, npc.complexfloating128]

# array-likes, with "coercible" shape-types, and "strict" shape-types

ToArrayStrict1D: TypeAlias = _ToStrict1D[T, SCT]
ToArrayStrict2D: TypeAlias = _ToStrict2D[T, SCT]
ToArrayStrict3D: TypeAlias = _ToStrict3D[T, SCT]

ToBoolStrict1D: TypeAlias = _ToStrict1D[_PyBool, np.bool_]
ToBoolStrict2D: TypeAlias = _ToStrict2D[_PyBool, np.bool_]
ToBoolStrict3D: TypeAlias = _ToStrict3D[_PyBool, np.bool_]

ToIntStrict1D: TypeAlias = _ToStrict1D[int, integer_co]
ToIntStrict2D: TypeAlias = _ToStrict2D[int, integer_co]
ToIntStrict3D: TypeAlias = _ToStrict3D[int, integer_co]

ToFloat64Strict1D: TypeAlias = _ToStrict1D[float, float64_co]
ToFloat64Strict2D: TypeAlias = _ToStrict2D[float, float64_co]
ToFloat64Strict3D: TypeAlias = _ToStrict3D[float, float64_co]

ToFloatStrict1D: TypeAlias = _ToStrict1D[float, floating_co]
ToFloatStrict2D: TypeAlias = _ToStrict2D[float, floating_co]
ToFloatStrict3D: TypeAlias = _ToStrict3D[float, floating_co]

ToComplex128Strict1D: TypeAlias = _ToStrict1D[complex, complex128_co]
ToComplex128Strict2D: TypeAlias = _ToStrict2D[complex, complex128_co]
ToComplex128Strict3D: TypeAlias = _ToStrict3D[complex, complex128_co]

ToComplexStrict1D: TypeAlias = _ToStrict1D[complex, complexfloating_co]
ToComplexStrict2D: TypeAlias = _ToStrict2D[complex, complexfloating_co]
ToComplexStrict3D: TypeAlias = _ToStrict3D[complex, complexfloating_co]

# array-likes, with "just" that scalar type, and "strict" shape-types

ToJustBoolStrict1D: TypeAlias = _ToStrict1D[bool, np.bool_]
ToJustBoolStrict2D: TypeAlias = _ToStrict2D[bool, np.bool_]
ToJustBoolStrict3D: TypeAlias = _ToStrict3D[bool, np.bool_]

ToJustInt64Strict1D: TypeAlias = _ToStrict1D[JustInt, np.int64]
ToJustInt64Strict2D: TypeAlias = _ToStrict2D[JustInt, np.int64]
ToJustInt64Strict3D: TypeAlias = _ToStrict3D[JustInt, np.int64]

ToJustIntStrict1D: TypeAlias = _ToStrict1D[JustInt, npc.integer]
ToJustIntStrict2D: TypeAlias = _ToStrict2D[JustInt, npc.integer]
ToJustIntStrict3D: TypeAlias = _ToStrict3D[JustInt, npc.integer]

ToJustFloat64Strict1D: TypeAlias = _ToStrict1D[JustFloat, npc.floating64]
ToJustFloat64Strict2D: TypeAlias = _ToStrict2D[JustFloat, npc.floating64]
ToJustFloat64Strict3D: TypeAlias = _ToStrict3D[JustFloat, npc.floating64]

ToJustFloatStrict1D: TypeAlias = _ToStrict1D[JustFloat, npc.floating]
ToJustFloatStrict2D: TypeAlias = _ToStrict2D[JustFloat, npc.floating]
ToJustFloatStrict3D: TypeAlias = _ToStrict3D[JustFloat, npc.floating]

ToJustComplex128Strict1D: TypeAlias = _ToStrict1D[JustComplex, npc.complexfloating128]
ToJustComplex128Strict2D: TypeAlias = _ToStrict2D[JustComplex, npc.complexfloating128]
ToJustComplex128Strict3D: TypeAlias = _ToStrict3D[JustComplex, npc.complexfloating128]

ToJustComplexStrict1D: TypeAlias = _ToStrict1D[JustComplex, npc.complexfloating]
ToJustComplexStrict2D: TypeAlias = _ToStrict2D[JustComplex, npc.complexfloating]
ToJustComplexStrict3D: TypeAlias = _ToStrict3D[JustComplex, npc.complexfloating]
