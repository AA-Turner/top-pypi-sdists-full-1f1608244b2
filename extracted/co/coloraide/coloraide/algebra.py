"""
Math related methods.

Includes various math related functions to aid in color translation and manipulation.

Matrix method APIs are implemented often to mimic the familiar `numpy` library or `scipy`.
The API for a given function may look very similar to those found in either of the two
scientific libraries. Our intent is not implement a full matrix library, but mainly the
parts that are most useful for what we do with colors. Functions may not have all the
features as found in the aforementioned libraries, but the API should be similar.

We actually really like `numpy`, and have only done this to keep dependencies lightweight
and available on non C Python based implementations. If we ever decide to switch to `numpy`,
we should be able to relatively easily as most of our API is modeled after `numpy` or `scipy`.

Some liberties are taken here and there. For instance, we are not as fast as `numpy`, so
we add some shortcuts to things that are used a lot (`dot`, `multiply`, `divide`, etc.).
In these cases, we provide new input to instruct the operation as to the dimensions of the
matrix so we don't waste time analyzing the matrix.

There is no requirement that external plugins need to use `algebra`, `numpy` could be
used as long as the final results are converted to normal types. It is certainly possible
that we could switch to using `numpy` in a major release in the future.
"""
from __future__ import annotations
import decimal
import sys
import cmath
import math
import operator
import functools
import itertools as it
from .deprecate import deprecated
from .types import (
    ArrayLike, MatrixLike, FloatShape, VectorShape, MatrixShape, TensorShape, ArrayShape, VectorLike,
    TensorLike, Array, Matrix, Tensor, Vector, VectorBool, MatrixBool, TensorBool, MatrixInt, ArrayType, Shape,
    DimHints, SupportsFloatOrInt
)
from typing import Callable, Sequence, Iterator, Any, Iterable, overload

RTOL = 4 * sys.float_info.epsilon
ATOL = 1e-12
NaN = math.nan
INF = math.inf
MAX_10_EXP = sys.float_info.max_10_exp

# Keeping for backwards compatibility
prod = math.prod
_all = all
_any = any

# Shortcut for math operations
# Specify one of these in divide, multiply, dot, etc.
# to bypass analyzing the shape to determine which path
# to take.
#
# `SC` = scalar, `D1` = 1-D array or vector, `D2` = 2-D
# matrix, and `DN_DM` means an N-D and M-D matrix.
#
# If just a single specifier is used, it is assumed that
# the operation is performed against another of the same.
# `SC` = scalar and a scalar, while `SC_D1` means a scalar
# and a vector
SC = (0, 0)
D1 = (1, 1)
D2 = (2, 2)
SC_D1 = (0, 1)
SC_D2 = (0, 2)
D1_SC = (1, 0)
D1_D2 = (1, 2)
D2_SC = (2, 0)
D2_D1 = (2, 1)
DN_DM = None

# Vector used to create a special matrix used in natural splines
M141 = [1, 4, 1]


################################
# General math
################################
def sign(x: float) -> float:
    """Return the sign of a given value."""

    if x and x == x:
        return x / abs(x)
    return x


def order(x: float) -> int:
    """Get the order of magnitude of a number."""

    _, digits, exponent = decimal.Decimal(x).as_tuple()
    return len(digits) + int(exponent) - 1


def round_half_up(n: float, scale: int = 0) -> float:
    """Round half up."""

    if not isinstance(scale, int):
        raise ValueError("'float' object cannot be interpreted as an integer")

    # Generally, Python reports the minimum float as 2.2250738585072014e-308,
    # but there are outliers as small as 5e-324. `mult` is limited by a scale of 308
    # due to overflow, but we could calculate greater values by splitting the `mult`
    # factor into two smaller factors when the scale exceeds 308. This would allow us
    # to round out to 324 decimal places for really small values like 5e-324, but
    # these values simply aren't practical enough to warrant the extra effort.
    mult = 10.0 ** scale
    return math.floor(n * mult + 0.5) / mult


def _round_location(
    f: float,
    p: int = 0,
    mode: str = 'digits'
) -> tuple[int, int]:
    """Return the start of the first significant digit and the digit targeted for rounding."""

    # Round to number of digits
    if mode == 'digits':
        # Less than zero we assume double precision
        if p < 0:
            p = 17
        d = p
        # If zero, assume integer rounding
        if p == 0:
            p = 17

    # Round to decimal place
    elif mode == 'decimal':
        d = p
        p = MAX_10_EXP

    # Round of significant digits
    elif mode == 'sigfig':
        d = MAX_10_EXP
        # Less than zero we assume double precision
        if p < 0 or p > 17:
            p = 17
        # If zero, assume integer rounding
        elif p == 0:
            p = 17
            d = 0

    else:
        raise ValueError("Unknown rounding mode '{mode}'")

    if f == 0 or not math.isfinite(f):
        return 0, 0

    # Round to specified significant figure or fractional digit, which ever is less
    v = -math.floor(math.log10(abs(f)))
    p = v + (p - 1)
    return v, d if d < p else p


def round_to(
    f: float,
    p: int = 0,
    mode: str = 'digits',
    rounding: Callable[[float, int], float]=round_half_up
) -> float:
    """Round to the specified precision using "half up" rounding by default."""

    _, p = _round_location(f, p, mode)

    # Return non-finite values without further processing
    if not math.isfinite(f):
        return f

    # Round to the specified location using the specified rounding function
    return rounding(f, p)


def minmax(value: VectorLike | Iterable[float]) -> tuple[float, float]:
    """Return the minimum and maximum value."""

    mn = math.inf
    mx = -math.inf
    e = -1

    for i in value:
        e += 1
        if i > mx:
            mx = i
        if i < mn:
            mn = i

    if e == -1:
        raise ValueError("minmax() arg is an empty sequence")

    return mn, mx


def clamp(
    value: SupportsFloatOrInt,
    mn: SupportsFloatOrInt | None = None,
    mx: SupportsFloatOrInt | None = None
) -> SupportsFloatOrInt:
    """Clamp the value to the given minimum and maximum."""

    if mn is not None and mx is not None:
        return max(min(value, mx), mn)
    elif mn is not None:
        return max(value, mn)
    elif mx is not None:
        return min(value, mx)
    else:
        return value


def zdiv(a: float, b: float, default: float = 0.0) -> float:
    """Protect against zero divide."""

    if b == 0:
        return default
    return a / b


def cbrt(n: float) -> float:
    """Calculate cube root."""

    return nth_root(n, 3)


def nth_root(n: float, p: float) -> float:
    """Calculate nth root while handling negative numbers."""

    if p == 0:  # pragma: no cover
        return math.inf

    if n == 0:
        # Can't do anything with zero
        return 0

    return math.copysign(abs(n) ** (p ** -1), n)


def spow(base: float, exp: float) -> float:
    """Perform `pow` with signed number."""

    return math.copysign(abs(base) ** exp, base)


def rect_to_polar(a: float, b: float) -> tuple[float, float]:
    """Take rectangular coordinates and make them polar."""

    c = math.sqrt(a ** 2 + b ** 2)
    h = math.degrees(math.atan2(b, a)) % 360
    return c, h


def polar_to_rect(c: float, h: float) -> tuple[float, float]:
    """Take rectangular coordinates and make them polar."""

    r = math.radians(h)
    a = c * math.cos(r)
    b = c * math.sin(r)
    return a, b


def solve_bisect(
    low:float,
    high: float,
    f: Callable[..., float],
    args: tuple[Any] | tuple[()] = (),
    start: float | None = None,
    maxiter: int = 50,
    rtol: float = RTOL,
    atol: float = ATOL,
) -> tuple[float, bool]:
    """
    Apply the bisect method to converge upon an answer.

    Return the best answer based on the specified limits and also
    return a boolean indicating if we confidently converged.
    """

    t = (high + low) * 0.5 if start is None else start

    x = math.nan
    for _ in range(maxiter):
        x = f(t, *args) if args else f(t)
        if math.isclose(x, 0, rel_tol=rtol, abs_tol=atol):
            return t, True
        if x > 0:
            high = t
        else:
            low = t
        t = (high + low) * 0.5

        if math.isclose(low, high, rel_tol=rtol, abs_tol=atol):  # pragma: no cover
            break

    return t, abs(x) < atol  # pragma: no cover


def _solve_quadratic(poly: Vector) -> Vector:
    """
    Solve a quadratic equation.

    a - c represent the coefficients of the polynomial and t equals the target value.

    All non-real roots are filtered out at the end.
    """

    a, b, c = poly

    # Scale coefficients by `a` so that `a` is 1 and drops out of future calculations
    if a != 1:
        b /= a
        c /= a

    m = -b * 0.5
    # Calculate the discriminant to determine number of roots and what type
    discriminant = m ** 2 - c
    # With `a` no longer a factor, we can greatly simplify the traditional quadratic formula
    # Solutions: `m +/- (m ** 2 - c) ** (1/2)`
    if discriminant < 0:
        # No real roots
        return []
    elif discriminant > 0:
        # Two real roots
        return [
            m + cmath.sqrt(discriminant).real,
            m - cmath.sqrt(discriminant).real
        ]
    # Double root
    return [m]


def _solve_cubic(poly:Vector) -> Vector:
    """
    Solve a cubic equation using Cardano's Method.

    a - d represent the coefficients of the polynomial and t equals the target value.

    All non-real roots are filtered out at the end.

    https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_formula
    """

    a, b, c, d = poly

    # Scale coefficients by `a` so that `a` is 1 and drops out of future calculations
    if a != 1:
        b /= a
        c /= a
        d /= a

    # Transform equation to a form removing the squared term: `t^3 + pt + q = 0`
    p = (3 * c - b ** 2) / 3
    q = (2 * b ** 3 - 9 * b * c + 27 * d) / 27

    # Calculate the discriminant to determine number of roots and what type
    discriminant = (q ** 2 / 4 + p ** 3 / 27)

    # Calculate `t = u^(1/3) + v^(1/3)`
    # Cube root must not use `** (1 / 3)` if real.
    # Should use `math.cbrt` or some signed power equivalent
    # on systems that don't support it.
    u3 = -q / 2 + cmath.sqrt(discriminant)
    v3 = -q / 2 - cmath.sqrt(discriminant)
    u = u3 ** (1 / 3) if u3.imag else nth_root(u3.real, 3)
    v = v3 ** (1 / 3) if v3.imag else nth_root(v3.real, 3)
    t = u + v

    # Precalculate conversion from `t` back to `x`
    # `x = t - b / 3`
    k = b / 3

    # Primitive roots: `pr = (-1 +/- -3 ** (1/2)) / 2 ~= -0.5 +/- 0.8660254037844386j`
    # The complex part (`prc`) equivalent calculation: `(0.8660254037844386j) = 3 ** (1/3) / 2j`
    prc = cmath.sqrt(3) / 2j

    # We can find the other two roots by multiplying u and v with the primitive roots:
    # ```
    # t2 = pr1 * u + pr2 * v
    # t3 = pr2 * u + pr1 * v
    # ```
    # With some algebraic manipulation and factoring the conversion to `x`
    # ```
    # x1 = (v + v) - k
    # x2 = -0.5 * (u + v) + (u - v) * prc - k
    # x3 = -0.5 * (u + v) - (u - v) * prc - k
    # ```
    td = (u - v)
    if discriminant > 0:
        # One real root
        return [(t - k).real]
    elif discriminant < 0:
        # Three real roots
        return [
            (t - k).real,
            (-0.5 * t + td * prc - k).real,
            (-0.5 * t - td * prc - k).real
        ]
    # Three real roots, two of which are doubles
    return [
        (t - k).real,
        (-0.5 * t + td * prc - k).real
    ]


def solve_poly(poly: Vector) -> Vector:
    """
    Solve the given polynomial.

    Currently, only up to 3rd degree polynomials are supported.
    """

    # Remove leading zeros
    count = 0
    for pi in poly:
        if pi == 0:
            count += 1
            continue
        break
    if count:
        poly = poly[count:]

    # Select the appropriate solver
    l = len(poly)
    if l > 4:
        raise ValueError('Polynomials of degrees great than 3 are not currently supported')
    elif l == 4:
        return _solve_cubic(poly)
    elif l == 3:
        return _solve_quadratic(poly)
    elif l == 2:
        return [-poly[1] / poly[0]]
    return []


def solve_newton(
    x0: float,
    f0: Callable[..., float],
    dx: Callable[..., float],
    dx2: Callable[..., float] | None = None,
    args: tuple[Any] | tuple[()] = (),
    maxiter: int = 50,
    rtol: float = RTOL,
    atol: float = ATOL,
    ostrowski: bool = False
) -> tuple[float, bool | None]:
    """
    Solve equation using Newton's method.

    If the second derivative is given, Halley's method will be used as an additional step.
    Newton provides 2nd order convergence and Halley provides 3rd order convergence.

    ```
    newton = yn = xn - f(xn) / f'(xn)
    halley = xn - (f(xn) * f'(xn)) / (f'(xn) ** 2 - 0.5 * f(xn) * f''(xn))
    ```

    Algebraically, we can pull the Newton stop out of the Halley method into two separate steps
    that can be applied on top of each other.

    ```
    Step1: yn = f(xn) / f'(xn)
    Step2: halley = xn - yn / (1 - 0.5 * yn * f''(xn) / f'(xn))
    ```

    If Ostrowski method is enabled, only one derivative is needed, but you can get 4th order convergence.

    ```
    yn = xn - f(xn) / f'(xn)
    ostrowski = yn - f(xn) / (f(xn) - 2 * f(yn)) * (f(yn) / f'(xn))
    ```

    Return result along with True if converged, False if did not converge, None if could not converge.
    """

    for _ in range(maxiter):
        # Get result form equation when setting value to expected result
        fx = f0(x0, *args) if args else f0(x0)
        prev = x0

        # If the result is zero, we've converged
        if fx == 0:
            return x0, True

        # Cannot find a solution if derivative is zero
        d1 = dx(x0, *args) if args else dx(x0)
        if d1 == 0:
            return x0, None  # pragma: no cover

        # Calculate new, hopefully closer value with Newton's method
        newton =  fx / d1

        # If second derivative is provided, apply the Halley's method step: 3rd order convergence
        if dx2 is not None and not ostrowski:
            d2 = dx2(x0, *args) if args else dx2(x0)
            value = (0.5 * newton * d2) / d1
            # If the value is greater than one, the solution is deviating away from the newton step
            if abs(value) < 1:
                newton /= 1 - value

        # If change is under our epsilon, we can consider the result converged.
        x0 -= newton
        if math.isclose(x0, prev, rel_tol=rtol, abs_tol=atol):
            return x0, True  # pragma: no cover
        # Use Ostrowski method: 4th order convergence
        if ostrowski:
            fy = f0(x0, *args) if args else f0(x0)
            if fy == 0:
                return x0, True
            fy_x2 = 2 * fy
            if fy_x2 == fx:  # pragma: no cover
                return x0, None
            x0 -= fx / (fx - fy_x2) * (fy / d1)

            if math.isclose(x0, prev, rel_tol=rtol, abs_tol=atol):  # pragma: no cover
                return x0, True

    return x0, False  # pragma: no cover


################################
# Interpolation and splines
################################
def lerp(p0: float, p1: float, t: float) -> float:
    """Linear interpolation."""

    return p0 + (p1 - p0) * t


def ilerp(p0: float, p1: float, t: float) -> float:
    """Inverse interpolation."""

    d = (p1 - p0)
    return (t - p0) / d if d else 0


def bilerp(p0: float, p1: float, p2: float, p3: float, tx: float, ty: float) -> float:
    """Bilinear interpolation."""

    return lerp(lerp(p0, p1, tx), lerp(p2, p3, tx), ty)


def lerp2d(vertices: Matrix, t: Vector) -> Vector:
    """
    Interpolate in 2D.

    Vertices should be in column form [[x...], [y...]].
    """

    return [bilerp(*vertices[i], *t) for i in range(2)]


def ilerp2d(
    vertices: Matrix,
    point: Vector,
    *,
    vertices_t: Matrix | None = None,
    max_iter: int = 20,
    tol: float = 1e-14
) -> Vector:
    """
    Inverse interpolation of a 2D point.

    Same algorithm as `ilerp3d` just for a 2D point. Based off the forward transform below.

    ```
    vxy = v00 (1 - x) (1 - y) +
        v10 x (1 - y) +
        v01 (1 - x) y +
        v11 x y
    ```
    """

    if vertices_t is None:  # pragma: no cover
        vertices_t = transpose(vertices)

    # Initial guess
    xy = [0.5, 0.5]

    try:
        for _ in range(max_iter):

            # Calculate the residual by using our guess to calculate the what should be the input and compare
            residual = subtract(lerp2d(vertices, xy), point, dims=D1)

            # If we are close enough to our input, we can quit
            if math.sqrt(residual[0] ** 2 + residual[1] ** 2) < tol:
                break

            # Build up the Jacobian matrix so we can solve for the next, closer guess.
            x, y = xy
            _x = [-(1 - y), 1 - y, -y, y]
            jx = [sum(i) for i in zip(*[[xi * c for c in ci] for ci, xi in zip(vertices_t, _x)])]

            _y = [-(1 - x), -x, x, 1 - x]
            jy = [sum(i) for i in zip(*[[yi * c for c in ci] for ci, yi in zip(vertices_t, _y)])]

            # Create the Jacobian matrix, but we need it in column form
            j = list(zip(jx, jy))

            # Solve for new guess
            xy = subtract(xy, solve(j, residual), dims=D1)
    except ValueError:  # pragma: no cover
        # The Jacobian matrix shouldn't fail inversion if we are in range.
        # Out of range may give us values we cannot invert. There are potential
        # ways to handle this to try and get moving again, but currently, we
        # just give up. We do not guarantee out of gamut conversions.
        pass

    return xy


def trilerp(
    p0: float,
    p1: float,
    p2: float,
    p3: float,
    p4: float,
    p5: float,
    p6: float,
    p7: float,
    tx: float,
    ty: float,
    tz: float
) -> float:
    """Trilinear interpolation."""

    return lerp(bilerp(p0, p1, p2, p3, tx, ty), bilerp(p4, p5, p6, p7, tx, ty), tz)


def lerp3d(
    vertices: Matrix,
    t: Vector
) -> Vector:
    """
    Interpolation in 3D.

    Vertices should be in column form [[x...], [y...], [z...]].
    """

    return [trilerp(*vertices[i], *t) for i in range(3)]


def ilerp3d(
    vertices: Matrix,
    point: Vector,
    *,
    vertices_t: Matrix | None = None,
    max_iter: int = 20,
    tol: float = 1e-14
) -> Vector:
    """
    Inverse trilinear interpolation.

    Uses Gauss-Newton method to compute the inverse of the trilinear interpolation.

    Original code by Nick Alger https://stackoverflow.com/a/18332009/3609487
    and adapted for our purposes. As stated in the link:

    > I release the 3D code to the public domain as well if anyone wants to use it.
    > - Nick Alger Jun 27, 2014 at 7:30

    Utilizes the trilinear interpolation method found here to get the inverse:
    http://paulbourke.net/miscellaneous/interpolation/. Results are the same as
    what we do in the forward, but easier to use for the inverse calculations.
    Forward transform found below with vertices ordered to match the order we store our
    vertices in.

    ```
    Vxyz = V000 (1 - x) (1 - y) (1 - z) +
        V100 x (1 - y) (1 - z) +
        V010 (1 - x) y (1 - z) +
        V110 x y (1 - z) +
        V001 (1 - x) (1 - y) z +
        V101 x (1 - y) z +
        V011 (1 - x) y z +
        V111 x y z
    ```

    NOTE: It does seem that selected vertices can have an impact on how well the
    reverse translation is. Certain combinations can cause us to fall short of
    resolving the interpolation all the way to 1 when it should. In some cases, it
    will just stop at `0.9xxxx`, etc. Some sets of vertices have no issues at all.
    """

    if vertices_t is None:  # pragma: no cover
        vertices_t = transpose(vertices)

    # Initial guess.
    xyz = [0.5, 0.5, 0.5]

    try:
        for _ in range(max_iter):

            # Calculate the residual by using our guess to calculate the what should be the input and compare
            residual = subtract(lerp3d(vertices, xyz), point, dims=D1)

            # If we are close enough to our input, we can quit
            if math.sqrt(residual[0] ** 2 + residual[1] ** 2 + residual[2] ** 2) < tol:
                break

            # Build up the Jacobian matrix so we can solve for the next, closer guess
            x, y, z = xyz
            _x = [
                -(1 - y) * (1 - z),
                (1 - y) * (1 - z),
                -y * (1 - z),
                y * (1 - z),
                -(1 - y) * z,
                (1 - y) * z,
                -y * z,
                y * z
            ]
            jx = [sum(i) for i in zip(*[[xi * c for c in ci] for ci, xi in zip(vertices_t, _x)])]

            _y = [
                -(1 - x) * (1 - z),
                -x * (1 - z),
                (1 - x) * (1 - z),
                x * (1 - z),
                -(1 - x) * z,
                -x * z,
                (1 - x) * z,
                x * z,
            ]
            jy = [sum(i) for i in zip(*[[yi * c for c in ci] for ci, yi in zip(vertices_t, _y)])]

            _z = [
                -(1 - x) * (1 - y),
                -x * (1 - y),
                -(1 - x) * y,
                -x * y,
                (1 - x) * (1 - y),
                x * (1 - y),
                (1 - x) * y,
                x * y
            ]
            jz = [sum(i) for i in zip(*[[zi * c for c in ci] for ci, zi in zip(vertices_t, _z)])]

            # Create the Jacobian matrix, but we need it in column form
            j = list(zip(jx, jy, jz))

            # Solve for new guess
            xyz = subtract(xyz, solve(j, residual), dims=D1)
    except ValueError:  # pragma: no cover
        # The Jacobian matrix shouldn't fail inversion if we are in range.
        # Out of range may give us values we cannot invert. There are potential
        # ways to handle this to try and get moving again, but currently, we
        # just give up. We do not guarantee out of gamut conversions.
        pass

    return xyz


@functools.lru_cache(maxsize=10)
def _matrix_141(n: int) -> Matrix:
    """Get matrix '1 4 1'."""

    m = [[0] * n for _ in range(n)]  # type: Matrix
    m[0][0:2] = M141[1:]
    m[-1][-2:] = M141[:-1]
    for x in range(n - 2):
        m[x + 1][x:x + 3] = M141
    return inv(m)


def naturalize_bspline_controls(coordinates: list[Vector]) -> None:
    """
    Given a set of B-spline control points in the Nth dimension, create new naturalized interpolation control points.

    Using the color points as `S0...Sn`, calculate `B0...Bn`, such that interpolation will
    pass through `S0...Sn`.

    When given 2 data points, the operation will be returned as linear, so there is nothing to do.
    """

    n = len(coordinates) - 2

    # Special case 3 data points
    if n == 1:
        coordinates[1] = [
            (a * 6 - (b + c)) / 4 for a, b, c in zip(coordinates[1], coordinates[0], coordinates[2])
        ]

    # Handle all other cases where n does not result in linear interpolation
    elif n > 1:
        # Create [1, 4, 1] matrix for size `n` set of control points
        m = _matrix_141(n)

        # Create C matrix from the data points
        c = []  # type: Matrix
        for r in range(1, n + 1):
            if r == 1:
                c.append([a * 6 - b for a, b in zip(coordinates[r], coordinates[r - 1])])
            elif r == n:
                c.append([a * 6 - b for a, b in zip(coordinates[n], coordinates[n + 1])])
            else:
                c.append([a * 6 for a in coordinates[r]])

        # Dot M^-1 and C to get B (control points)
        v = dot(m, c, dims=D2)
        for r in range(1, n + 1):
            coordinates[r] = v[r - 1]


def bspline(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
    """Calculate the new point using the provided values."""

    # Save some time calculating this once
    t2 = t ** 2
    t3 = t2 * t

    # Insert control points to algorithm
    return (
        ((1 - t) ** 3) * p0 +  # B0
        (3 * t3 - 6 * t2 + 4) * p1 +  # B1
        (-3 * t3 + 3 * t2 + 3 * t + 1) * p2 +  # B2
        t3 * p3  # B3
    ) / 6


def catrom(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
    """Calculate the new point using the provided values."""

    # Save some time calculating this once
    t2 = t ** 2
    t3 = t2 * t

    # Insert control points to algorithm
    return (
        (-t3 + 2 * t2 - t) * p0 +  # B0
        (3 * t3 - 5 * t2 + 2) * p1 +  # B1
        (-3 * t3 + 4 * t2 + t) * p2 +  # B2
        (t3 - t2) * p3  # B3
    ) / 2


def monotone(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
    """
    Monotone spline based on Hermite.

    We calculate our secants for our four samples (the center pair being our interpolation target).

    From those, we calculate an initial gradient, and test to see if it is needed. In the event
    that our there is no increase or decrease between the point, we can infer that the gradient
    should be horizontal. We also test if they have opposing signs, if so, we also consider the
    gradient to be zero.

    Lastly, we ensure that the gradient is confined within a circle with radius 3 as it has been
    observed that such a circle encapsulates the entire monotonicity region.

    Once gradients are calculated, we simply perform the Hermite spline calculation and clean up
    floating point math errors to ensure monotonicity.

    We could build up secant and gradient info ahead of time, but currently we do it on the fly.

    http://jbrd.github.io/2020/12/27/monotone-cubic-interpolation.html
    https://ui.adsabs.harvard.edu/abs/1990A%26A...239..443S/abstract
    https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.39.6720
    https://en.wikipedia.org/w/index.php?title=Monotone_cubic_interpolation&oldid=950478742
    """

    # Save some time calculating this once
    t2 = t ** 2
    t3 = t2 * t

    # Calculate the secants for the differing segments
    s0 = p1 - p0
    s1 = p2 - p1
    s2 = p3 - p2

    # Calculate initial gradients
    m1 = (s0 + s1) * 0.5
    m2 = (s1 + s2) * 0.5

    # Center segment should be horizontal as there is no increase/decrease between the two points
    if math.isclose(p1, p2):
        m1 = m2 = 0.0
    else:

        # Gradient is zero if segment is horizontal or if the left hand secant differs in sign from current.
        if math.isclose(p0, p1) or (math.copysign(1.0, s0) != math.copysign(1.0, s1)):
            m1 = 0.0

        # Ensure gradient magnitude is either 3 times the left or current secant (smaller being preferred).
        else:
            m1 *= min(3.0 * s0 / m1, min(3.0 * s1 / m1, 1.0))

        # Gradient is zero if segment is horizontal or if the right hand secant differs in sign from current.
        if math.isclose(p2, p3) or (math.copysign(1.0, s1) != math.copysign(1.0, s2)):
            m2 = 0.0

        # Ensure gradient magnitude is either 3 times the current or right secant (smaller being preferred).
        else:
            m2 *= min(3.0 * s1 / m2, min(3.0 * s2 / m2, 1.0))

    # Now we can evaluate the Hermite spline
    result = (
        (m1 + m2 - 2 * s1) * t3 +
        (3.0 * s1 - 2.0 * m1 - m2) * t2 +
        m1 * t +
        p1
    )

    # As the spline is monotonic, all interpolated values should be confined between the endpoints.
    # Floating point arithmetic can cause this to be out of bounds on occasions.
    mn = min(p1, p2)
    mx = max(p1, p2)
    return min(max(result, mn), mx)


SPLINES = {
    'natural': bspline,
    'bspline': bspline,
    'catrom': catrom,
    'monotone': monotone,
    'linear': lerp
}  # type: dict[str, Callable[..., float]]


class Interpolate:
    """Interpolation object."""

    def __init__(
        self,
        points: Sequence[VectorLike],
        callback: Callable[..., float],
        length: int,
        linear: bool = False
    ) -> None:
        """Initialize."""

        self.length = length
        self.num_coords = len(points[0])
        self.points = list(zip(*points))
        self.callback = callback
        self.linear = linear

    def steps(self, count: int) -> list[Vector]:
        """Generate steps."""

        divisor = count - 1
        return [self(r / divisor) for r in range(0, count)]

    def __call__(self, t: float) -> Vector:
        """Interpolate."""

        n = self.length - 1
        i = max(min(math.floor(t * n), n - 1), 0)
        t = (t - i / n) * n if 0 <= t <= 1 else t
        if not self.linear:
            i += 1

        # Iterate the coordinates and apply the spline to each component
        # returning the completed, interpolated coordinate set.
        coord = []
        for idx in range(self.num_coords):
            c = self.points[idx]
            if self.linear or t < 0 or t > 1:
                coord.append(lerp(c[i], c[i + 1], t))
            else:
                coord.append(
                    self.callback(
                        c[i - 1],
                        c[i],
                        c[i + 1],
                        c[i + 2],
                        t
                    )
                )

        return coord


def interpolate(points: list[Vector], method: str = 'linear') -> Interpolate:
    """Generic interpolation method."""

    points = points[:]
    length = len(points)

    # Natural requires some preprocessing of the B-spline points.
    if method == 'natural':
        naturalize_bspline_controls(points)

    # Get the spline method
    s = SPLINES[method]
    linear = method == 'linear'

    # Clamp end points
    if not linear:
        start = [2 * a - b for a, b in zip(points[0], points[1])]
        end = [2 * a - b for a, b in zip(points[-1], points[-2])]
        points.insert(0, start)
        points.append(end)

    return Interpolate(points, s, length, linear)


################################
# Matrix/linear algebra math
################################
def pretty(value: float | ArrayLike, *, _depth: int = 0, _shape: Shape | None = None) -> str:
    """Format the print output."""

    if _shape is None:
        _shape = shape(value)

    nl = len(_shape) - _depth - 1
    if isinstance(value, Sequence):
        seq = len(value) and isinstance(value[0], Sequence)
        values = [pretty(v, _depth=_depth + 1, _shape=_shape) for v in value]
        spacing = _depth + 1
        return '[{}]'.format((',{}{}'.format('\n' * nl, ' ' * spacing) if seq else ', ').join(values))

    return str(value)


def pprint(value: float | ArrayLike) -> None:
    """Print the matrix or value."""

    print(pretty(value))


def all(a: float | ArrayLike) -> bool:  # noqa: A001
    """Return true if all elements are "true"."""

    return _all(flatiter(a))


def any(a: float | ArrayLike) -> bool:  # noqa: A001
    """Return true if all elements are "true"."""

    return _any(flatiter(a))


def vdot(a: VectorLike, b: VectorLike) -> float:
    """Dot two vectors."""

    l = len(a)
    if l != len(b):
        raise ValueError(f'Vectors of size {l} and {len(b)} are not aligned')
    s = 0.0
    i = 0
    while i < l:
        s += a[i] * b[i]
        i += 1
    return s


def vcross(v1: VectorLike, v2: VectorLike) -> Any:  # pragma: no cover
    """
    Cross two vectors.

    Takes vectors of either 2 or 3 dimensions. If 2 dimensions, will return the z component.
    To mix 2 and 3 vector components, please use `cross` instead which will pad 2 dimension
    vectors if the other is of 3 dimensions. `cross` has more overhead, so use `vcross` if
    you don't need broadcasting of any kind.
    """

    l1 = len(v1)
    if l1 != len(v2):
        raise ValueError(f'Incompatible dimensions of {l1} and {len(v2)} for cross product')

    if l1 == 2:
        return v1[0] * v2[1] - v1[1] * v2[0]
    elif l1 == 3:
        return [
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v2[2] * v1[0],
            v1[0] * v2[1] - v1[1] * v2[0]
        ]
    else:
        raise ValueError(f'Expected vectors of shape (2,) or (3,) but got ({l1},) ({len(v2)},)')


@overload
def acopy(a: VectorLike) -> Vector:
    ...


@overload
def acopy(a: MatrixLike) -> Matrix:
    ...


@overload
def acopy(a: TensorLike) -> Tensor:
    ...


def acopy(a: ArrayLike) -> Array:
    """Array copy."""

    return [(acopy(i) if isinstance(i, Sequence) else i) for i in a]  # type: ignore[return-value]


@overload
def _cross_pad(a: VectorLike, s: ArrayShape) -> Vector:
    ...


@overload
def _cross_pad(a: MatrixLike, s: ArrayShape) -> Matrix:
    ...


@overload
def _cross_pad(a: TensorLike, s: ArrayShape) -> Tensor:
    ...


def _cross_pad(a: ArrayLike, s: ArrayShape) -> Array:
    """Pad an array with 2-D vectors."""

    m = acopy(a)

    # Initialize indexes so we can properly write our data
    total = prod(s[:-1])
    idx = [0] * (len(s) - 1)

    for c in range(total):
        t = m  # type: Any
        for i in idx:
            t = t[i]

        t.append(0)

        if c < (total - 1):
            for x in range(len(s) - 1):
                if (idx[x] + 1) % s[x] == 0:
                    idx[x] = 0
                    x += 1
                else:
                    idx[x] += 1
                    break
    return m


def cross(a: ArrayLike, b: ArrayLike) -> Any:
    """Vector cross product."""

    # Determine shape of arrays
    shape_a = shape(a)  # type: Shape
    shape_b = shape(b)  # type: Shape
    dims_a = len(shape_a)
    dims_b = len(shape_b)

    # Avoid crossing vectors of the wrong size or scalars
    if not shape_a or not shape_b or not (1 < shape_a[-1] < 4) or not (1 < shape_b[-1] < 4):
        raise ValueError('Values must contain vectors of dimensions 2 or 3')

    # Pad 2-D vectors
    if shape_a[-1] != shape_b[-1]:
        if shape_a[-1] == 2:
            a = _cross_pad(a, shape_a)
            shape_a = shape_a[:-1] + (3,)
        else:
            b = _cross_pad(b, shape_b)
            shape_b = shape_b[:-1] + (3,)

    # Cross two vectors
    if dims_a == 1 and dims_b == 1:
        return vcross(a, b)  # type: ignore[arg-type]

    # Calculate cases of vector crossed either 2-D or N-D matrix and vice versa
    if dims_a == 1 or dims_b == 1:
        # Calculate target shape
        mdim = max(dims_a, dims_b)
        new_shape = list(_broadcast_shape([shape_a, shape_b], mdim))
        if mdim > 1 and new_shape[-1] == 2:
            new_shape.pop(-1)

        if dims_a == 2:
            # Cross a 2-D matrix and a vector
            result = [vcross(r, b) for r in a]  # type: ignore[arg-type]

        elif dims_b == 2:
            # Cross a vector and a 2-D matrix
            result = [vcross(a, r) for r in b]  # type: ignore[arg-type]

        elif dims_a > 2:
            # Cross an N-D matrix and a vector
            result = [vcross(r, b) for r in _extract_rows(a, shape_a)]  # type: ignore[arg-type]

        else:
            # Cross a vector and an N-D matrix
            result = [vcross(a, r) for r in _extract_rows(b, shape_b)]  # type: ignore[arg-type]

        return reshape(result, tuple(new_shape))  # type: ignore[arg-type]

    # Cross an N-D and M-D matrix
    bcast = broadcast(a, b)
    a2 = []
    b2 = []
    data = []
    count = 1
    size = bcast.shape[-1]
    for x, y in bcast:
        a2.append(x)
        b2.append(y)
        if count == size:
            data.append(vcross(a2, b2))
            a2 = []
            b2 = []
            count = 0
        count += 1

    # Adjust shape for the way cross outputs data
    new_shape = list(bcast.shape)
    mdim = max(dims_a, dims_b)
    if mdim > 1 and new_shape[-1] == 2:
        new_shape.pop(-1)

    return reshape(data, tuple(new_shape))  # type: ignore[arg-type]


def _extract_rows(m: ArrayLike, s: ArrayShape, depth: int = 0) -> Iterator[Vector]:
    """Extract rows from an array."""

    if len(s) > 1 and s[1]:
        for m1 in m:
            yield from _extract_rows(m1, s[1:], depth + 1)  # type: ignore[arg-type]
    else:
        yield m  # type: ignore[misc]


def _extract_cols(m: ArrayLike, s: ArrayShape, depth: int = 0) -> Iterator[Vector]:
    """Extract columns from an array."""

    if len(s) > 2 and s[2]:
        for m1 in m:
            yield from _extract_cols(m1, s[1:], depth + 1)  # type: ignore[arg-type]
    elif not depth:
        yield m  # type: ignore[misc]
    else:
        yield from [[x[r] for x in m] for r in range(len(m[0]))]  # type: ignore[arg-type, index, misc]


@overload
def dot(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def dot(a: float, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot(a: VectorLike, b: float, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot(a: float, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def dot(a: MatrixLike, b: float, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def dot(a: float, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def dot(a: TensorLike, b: float, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def dot(a: VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def dot(a: VectorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot(a: MatrixLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot(a: VectorLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def dot(a: TensorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def dot(a: MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def dot(a: MatrixLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def dot(a: TensorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def dot(a: TensorLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


def dot(
    a: float | ArrayLike,
    b: float | ArrayLike,
    *,
    dims: DimHints | None = None,
) -> float | Array:
    """
    Perform dot product.

    Operations involving scalars will be the same as calling `multiply`.

    If you are doing matrix multiplication, equivalent to `@` in `numpy`,
    then you want to use `matmul` instead. Operations on arrays of dimension 2
    or less will act the same as `matmul`.
    """

    if dims is None or dims[0] > 2 or dims[1] > 2:
        shape_a = shape(a)  # type: Shape
        shape_b = shape(b)  # type: Shape
        dims_a = len(shape_a)
        dims_b = len(shape_b)

        # Handle matrices of N-D and M-D size
        if dims_a and dims_b and (dims_a > 2 or dims_b > 2):
            if dims_a == 1:
                # Dot product of vector and a M-D matrix
                shape_c = shape_b[:-2] + shape_b[-1:]
                return reshape([vdot(a, col) for col in _extract_cols(b, shape_b)], shape_c)  # type: ignore[arg-type]
            elif dims_b == 1:
                # Dot product of vector and a M-D matrix
                shape_c = shape_a[:-1]
                return reshape([vdot(row, b) for row in _extract_rows(a, shape_a)], shape_c)  # type: ignore[arg-type]
            else:
                # Dot product of N-D and M-D matrices
                # Resultant size: `dot(xy, yz) = xz` or `dot(nxy, myz) = nxmz`

                cols = list(_extract_cols(b, shape_b))  # type: ignore[arg-type]
                new_shape = shape_a[:-1] + shape_b[:-2] + shape_b[-1:]  # type: MatrixShape | TensorShape # type: ignore[assignment]
                return reshape(
                    [
                        [sum(multiply(row, col)) for col in cols]
                        for row in _extract_rows(a, shape_a)  # type: ignore[arg-type]
                    ],
                    new_shape
                )
    else:
        dims_a, dims_b = dims

    # Operations with scalars are the same as simply multiplying
    if not dims_a or not dims_b:
        return multiply(a, b, dims=(dims_a, dims_b))

    # Dot is identical to matrix multiply when dimensions are less than or equal to 2,
    return matmul(a, b, dims=(dims_a, dims_b))  # type: ignore[arg-type]


@overload
def matmul(a: VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def matmul(a: VectorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def matmul(a: MatrixLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def matmul(a: VectorLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def matmul(a: TensorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def matmul(a: MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def matmul(a: MatrixLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def matmul(a: TensorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Tensor | Matrix:
    ...


@overload
def matmul(a: TensorLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


def matmul(
    a: ArrayLike,
    b: ArrayLike,
    *,
    dims: DimHints | None = None,
) -> float | Array:
    """
    Perform matrix multiplication of two arrays.

    Similar behavior as dot product, but this is limited to non-scalar values only. Additionally,
    the behavior of dimensions greater than 2 will be different. Stacks of matrices are broadcast
    together as if the matrices were elements, respecting the signature `(n,k),(k,m)->(n,m)`.
    This follows `numpy` behavior and is equivalent to the `@` operation.
    """

    if dims is None or dims[0] > 2 or dims[1] > 2:
        shape_a = shape(a)  # type: ArrayShape
        shape_b = shape(b)  # type: ArrayShape
        dims_a = len(shape_a)
        dims_b = len(shape_b)

        # Handle matrices of N-D and M-D size
        if dims_a and dims_b and (dims_a > 2 or dims_b > 2):
            if dims_a == 1:
                # Matrix multiply of vector and a M-D matrix
                shape_c = shape_b[:-2] + shape_b[-1:]
                return reshape([vdot(a, col) for col in _extract_cols(b, shape_b)], shape_c)  # type: ignore[arg-type]
            elif dims_b == 1:
                # Matrix multiply of vector and a M-D matrix
                shape_c = shape_a[:-1]
                return reshape([vdot(row, b) for row in _extract_rows(a, shape_a)], shape_c)  # type: ignore[arg-type]
            elif shape_a[-1] == shape_b[-2]:
                # Stacks of matrices are broadcast together as if the matrices were elements,
                # respecting the signature `(n,k),(k,m)->(n,m)`.
                common = _broadcast_shape([shape_a[:-2], shape_b[:-2]], max(dims_a, dims_b) - 2)
                shape_a = common + shape_a[-2:]
                a = broadcast_to(a, shape_a)  # type: ignore[arg-type, assignment]
                shape_b = common + shape_b[-2:]
                b = broadcast_to(b, shape_b)  # type: ignore[arg-type, assignment]
                m2 = [
                    matmul(a1, b1, dims=D2)
                    for a1, b1 in zip(_extract_rows(a, shape_a[:-1]), _extract_rows(b, shape_b[:-1]))
                ]
                return reshape(m2, common + (shape_a[-2], shape_b[-1]))  # type: ignore[arg-type]

            raise ValueError(
                'Incompatible shapes in core dimensions (n?,k),(k,m?)->(n?,m?), {} != {}'.format(
                    shape_a[-1],
                    shape_b[-2]
                )
            )
    else:
        dims_a, dims_b = dims

    # Optimize to handle arrays <= 2-D
    if dims_a == 1:
        if dims_b == 1:
            # Matrix multiply of two vectors
            return vdot(a, b)  # type: ignore[arg-type]
        elif dims_b == 2:
            # Matrix multiply of vector and a matrix
            return [vdot(a, col) for col in it.zip_longest(*b)]  # type: ignore[arg-type]

    elif dims_a == 2:
        if dims_b == 1:
            # Matrix multiply of matrix and a vector
            return [vdot(row, b) for row in a]  # type: ignore[arg-type]
        elif dims_b == 2:
            # Matrix multiply of two matrices
            cols = list(it.zip_longest(*b))
            return [
                [vdot(row, col) for col in cols] for row in a  # type: ignore[arg-type]
            ]

    # Scalars are not allowed
    raise ValueError('Inputs require at least 1 dimension, scalars are not allowed')


@overload
def matmul_x3(a: VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def matmul_x3(a: VectorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def matmul_x3(a: MatrixLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def matmul_x3(a: MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


def matmul_x3(
    a: MatrixLike | VectorLike,
    b: MatrixLike | VectorLike,
    *,
    dims: DimHints | None = None,
) -> float | Vector | Matrix:
    """
    An optimized version of `matmul` that the total allowed dimensions to <= 2 and constrains dimensions lengths to 3.

    By limited to the total dimensions to < 2 and the dimension lengths of 3, loops are no longer required to handle
    an unknown number of dimensions or dimension lengths allowing for more optimized and faster performance at the
    cost of being able to handle any size arrays.

    For more flexibility with array sizes, use `matmul`.
    """

    if dims is None:
        shape_a = shape(a)
        shape_b = shape(b)
        dims_a = len(shape_a)
        dims_b = len(shape_b)
    else:
        dims_a, dims_b = dims

    # Optimize to handle arrays <= 2-D
    if dims_a == 1:
        if dims_b == 1:
            # Matrix multiply of two vectors
            return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]  # type: ignore[operator]
        elif dims_b == 2:
            # Matrix multiply of vector and a matrix
            return [
                a[0] * b[0][0] + a[1] * b[1][0] + a[2] * b[2][0],  # type: ignore[index, operator]
                a[0] * b[0][1] + a[1] * b[1][1] + a[2] * b[2][1],  # type: ignore[index, operator]
                a[0] * b[0][2] + a[1] * b[1][2] + a[2] * b[2][2]  # type: ignore[index, operator]
            ]

    elif dims_a == 2:
        if dims_b == 1:
            # Matrix multiply of matrix and a vector
            return [
                a[0][0] * b[0] + a[0][1] * b[1] + a[0][2] * b[2],  # type: ignore[index, operator]
                a[1][0] * b[0] + a[1][1] * b[1] + a[1][2] * b[2],  # type: ignore[index, operator]
                a[2][0] * b[0] + a[2][1] * b[1] + a[2][2] * b[2],  # type: ignore[index, operator]
            ]
        elif dims_b == 2:
            # Matrix and column vector
            if len(b[0]) == 1:  # type: ignore[arg-type]
                return [
                    [
                        a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0],  # type: ignore[index]
                    ],
                    [
                        a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0],  # type: ignore[index]
                    ],
                    [
                        a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0],  # type: ignore[index]
                    ]
                ]
            # Two full matrices
            return [
                [
                    a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0],  # type: ignore[index]
                    a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1],  # type: ignore[index]
                    a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2]  # type: ignore[index]
                ],
                [
                    a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0],  # type: ignore[index]
                    a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1],  # type: ignore[index]
                    a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2]  # type: ignore[index]
                ],
                [
                    a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0],  # type: ignore[index]
                    a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1],  # type: ignore[index]
                    a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2]  # type: ignore[index]
                ]
            ]

    # N > 2 dimensions are not allowed
    if dims_a > 2 or dims_b > 2:
        raise ValueError('Inputs cannot exceed 2 dimensions')

    # Scalars are not allowed
    raise ValueError('Inputs require at least 1 dimension, scalars are not allowed')


@overload
def dot_x3(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def dot_x3(a: float, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot_x3(a: VectorLike, b: float, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot_x3(a: float, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def dot_x3(a: MatrixLike, b: float, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def dot_x3(a: VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def dot_x3(a: VectorLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot_x3(a: MatrixLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def dot_x3(a: MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


def dot_x3(
    a: MatrixLike | VectorLike | float,
    b: MatrixLike | VectorLike | float,
    dims: DimHints | None = None
) -> float | Array:
    """
    An optimized version of `dot` that the total allowed dimensions to <= 2 and constrains dimensions lengths to 3.

    By limited to the total dimensions to < 2 and the dimension lengths of 3, loops are no longer required to handle
    an unknown number of dimensions or dimension lengths allowing for more optimized and faster performance at the
    cost of being able to handle any size arrays.

    For more flexibility with array sizes, use `dot`.
    """

    if dims is None:
        shape_a = shape(a)
        shape_b = shape(b)
        dims_a = len(shape_a)
        dims_b = len(shape_b)
    else:
        dims_a, dims_b = dims

    if not dims_a or not dims_b:
        return multiply_x3(a, b, dims=(dims_a, dims_b))

    return matmul_x3(a, b, dims=(dims_a, dims_b))  # type: ignore[arg-type]


def _matrix_chain_order(shapes: Sequence[ArrayShape]) -> MatrixInt:
    """
    Calculate chain order.

    Referenced the following sites:

    - https://en.wikipedia.org/wiki/Matrix_chain_multiplication
    - https://www.cs.cmu.edu/afs/cs/academic/class/15451-s04/www/Lectures/CRLS-DynamicProg.pdf

    This helped clarify `p` as that was not immediately clear:

    - https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

    We did adjust the looping. The algorithm originally called for looping from 2 - n,
    I can't see why though, so we've adjusted it to work from 1 - n.
    """

    n = len(shapes)
    m = full((n, n), 0)  # type: Any
    s = full((n, n), 0)  # type: MatrixInt # type: ignore[assignment]
    p = [a[0] for a in shapes] + [shapes[-1][1]]

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            m[i][j] = math.inf
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return s


def _multi_dot(arrays: Sequence[ArrayLike], indexes: MatrixInt, i: int, j: int) -> ArrayLike:
    """Recursively dot the matrices in the array."""

    if i != j:
        return dot(  # type: ignore[return-value]
            _multi_dot(arrays, indexes, i, int(indexes[i][j])),
            _multi_dot(arrays, indexes, int(indexes[i][j]) + 1, j),
            dims=D2
        )
    return arrays[i]


def multi_dot(arrays: Sequence[ArrayLike]) -> Any:
    """
    Multi-dot.

    Dots matrices using the most efficient groupings to reduce operations.
    """

    is_scalar = False
    is_vector = False

    # Must have at lest two arrays
    count = len(arrays)
    if count == 1:
        raise ValueError('At least 2 arrays must be provided')

    # If there are only 2 arrays, just send them through normal dot
    elif count == 2:
        return dot(arrays[0], arrays[1])

    # Calculate the shapes
    shapes = [shape(a) for a in arrays]

    # We need the list mutable if we are going to update the entries
    if not isinstance(arrays, list):
        arrays = list(arrays)

    # Row vector
    if len(shapes[0]) == 1:
        arrays[0] = [arrays[0]]
        shapes[0] = (1,) + shapes[0]
        is_vector = True

    # Column vector
    if len(shapes[-1]) == 1:
        arrays[-1] = transpose([arrays[-1]])
        shapes[-1] = shapes[-1] + (1,)
        if is_vector:
            is_scalar = True
        else:
            is_vector = True

    # Make sure everything is a 2-D matrix as the next calculations only work for 2-D.
    if not _all(len(s) == 2 for s in shapes):
        raise ValueError('All arrays must be 2-D matrices')

    # No need to do the expensive and complicated chain order algorithm for only 3.
    # We can easily calculate three with less complexity and in less time. Anything
    # greater than three becomes a headache.
    if count == 3:
        pa = prod(shapes[0])
        pc = prod(shapes[2])
        cost1 = pa * shapes[2][0] + pc * shapes[0][0]
        cost2 = pc * shapes[0][1] + pa * shapes[2][1]  # type: ignore[misc]
        if cost1 < cost2:
            value = dot(dot(arrays[0], arrays[1], dims=D2), arrays[2], dims=D2)
        else:
            value = dot(arrays[0], dot(arrays[1], arrays[2], dims=D2), dims=D2)

    # Calculate the fastest ordering with dynamic programming using memoization
    s = _matrix_chain_order([shape(a) for a in arrays])
    value = _multi_dot(arrays, s, 0, count - 1)

    # `numpy` returns the shape differently depending on if there is a row and/or column vector
    if is_scalar:
        return value[0][0]
    elif is_vector:
        return ravel(value)
    else:
        return value


class _BroadcastTo:
    """
    Broadcast to a shape.

    By flattening the data, we are able to slice out the bits we need in the order we need
    and duplicate them to expand the matrix to fit the provided shape.

    We need 3 things to do this:
    - The original array.
    - The stage 1 array shape (with prepended 1s). This helps us calculate our loop iterations.
    - The new shape.
    """

    def __init__(self, array: ArrayLike | float, old: Shape, new: Shape) -> None:
        """Initialize."""

        self._loop1 = 0
        self._loop2 = 0
        self._chunk_subindex = 0
        self._chunk_max = 0
        self._chunk_index = 0
        self._chunk = []  # type: Vector

        # Unravel the data as it will be quicker to slice the data in a flattened form
        # than iterating over the dimensions to replicate the data.
        self.data = ravel(array)
        self.shape = new

        # One of the common dimensions makes this result empty
        self.empty = 0 in new

        # Is the new shape actually different than the original?
        self.different = old != new

        if self.empty:
            # There is no data
            self.amount = self.length = self.expand = self.repeat = 0
        elif self.different:
            # Calculate the shape of the data.
            if len(old) > 1:
                self.amount = prod(old[:-1])
                self.length = old[-1]
            else:
                # Vectors have to be handled a bit special as they only have 1-D
                self.amount = old[-1]
                self.length = 1

            # Calculate how many times we should replicate data both horizontally and vertically
            # We need to flip them based on whether the original shape has an even or odd number of
            # dimensions.
            diff = [int(x / y) if y else y for x, y in zip(new, old)]
            repeat = prod(diff[:-1]) if len(old) > 1 else 1
            expand = diff[-1]
            if len(diff) > 1 and diff[-2] > 1:
                self.repeat = expand
                self.expand = repeat
            else:
                self.repeat = repeat
                self.expand = expand
        else:
            # There is no modifications that need to be made on this array,
            # So we'll be chunking it without any cleverness.
            self.amount = len(self.data)
            self.length = 1
            self.expand = 1
            self.repeat = 1

        self.reset()

    def reset(self) -> None:
        """Reset."""

        # Setup and return the iterator.
        self._loop1 = self.repeat
        self._loop2 = self.expand
        self._chunk_subindex = 0
        self._chunk_max = self.amount * self.length
        self._chunk_index = 0

    def __next__(self) -> float:
        """Next."""

        if self._loop1:
            # Get the data.
            d = self.data[self._chunk_index + self._chunk_subindex]

            self._chunk_subindex += 1
            if self._chunk_subindex >= self.length:
                # We've processed the entirety of the current chunk
                # Let's see if we need to process it again.
                self._loop2 -= 1
                self._chunk_subindex = 0
                if not self._loop2:
                    # We've finished processing this chunk, let's get the next.
                    self._chunk_index += self.length
                    self._loop2 = self.expand

                    if self._chunk_index >= self._chunk_max:
                        # We are actually at the end of all the data,
                        # let's see if we need to process all the data again.
                        self._loop1 -= 1
                        if self._loop1:
                            # We need to keep going
                            self._chunk_index = 0

            # Return the current data
            return d

        # We have nothing more to give
        raise StopIteration

    def __iter__(self) -> Iterator[float]:
        """Return the broadcasted array, piece by piece."""

        return self


class _SimpleBroadcast:
    """
    Special broadcast of less than 2 arrays or 2 small dimension arrays that is faster than the generalized approach.

    A single array can have any dimensions, but two arrays must have dimensions less than 2.
    """

    def __init__(
        self,
        arrays: Sequence[ArrayLike | float],
        shapes: Sequence[Shape],
        new: Shape
    ) -> None:
        """Initialize."""

        self.empty = 0 in new

        total = len(arrays)
        if total == 0:
            a, b = None, None  # type: tuple[Any, Any]
        elif total == 1:
            a, b = arrays[0], None
        else:
            a, b = arrays

        self.a = a
        self.dims_a = len(shapes[0]) if a is not None else 0

        self.b = b
        self.dims_b = len(shapes[1]) if b is not None else 0

        self.reset()

    def vector_broadcast(self, a: VectorLike, b: VectorLike) -> Iterator[tuple[float, ...]]:
        """Broadcast two vectors."""

        # Broadcast the vector
        if len(a) == 1:
            a = [a[0]] * len(b)
        elif len(b) == 1:
            b = [b[0]] * len(a)

        yield from it.zip_longest(a, b)

    def broadcast(
        self,
        a: ArrayLike | float | None,
        b: ArrayLike | float | None,
        dims_a: int, dims_b: int
    ) -> Iterator[tuple[float, ...]]:
        """Simple broadcast of a single array or two arrays with dimensions less than 2."""

        # One of the common dimensions makes this result empty
        if self.empty:
            return

        # Broadcast a single array case or empty set of arrays.
        if b is None:
            if a is not None:
                yield from ((i,) for i in flatiter(a))
            return

        # Inputs have matching dimensions.
        if dims_a == dims_b:
            if dims_a == 1:
                # Broadcast two vectors
                yield from self.vector_broadcast(a, b)  # type: ignore[arg-type]
            elif dims_a == 2:
                # Broadcast two 2-D matrices
                la = len(a)  # type: ignore[arg-type]
                lb = len(b)  # type: ignore[arg-type]
                if la == 1 and lb != 1:
                    ra = a[0]  # type: ignore[index]
                    for rb in b:  # type: ignore[union-attr]
                        yield from self.vector_broadcast(ra, rb)  # type: ignore[arg-type]
                elif lb == 1 and la != 1:
                    rb = b[0]  # type: ignore[index]
                    for ra in a:  # type: ignore[union-attr]
                        yield from self.vector_broadcast(ra, rb)  # type: ignore[arg-type]
                else:
                    for ra, rb in it.zip_longest(a, b):  # type: ignore[arg-type]
                        yield from self.vector_broadcast(ra, rb)  # type: ignore[arg-type]
            else:
                yield a, b  # type: ignore[misc]

        # Inputs containing a scalar on either side
        elif not dims_a or not dims_b:
            if dims_a == 1:
                # Apply math to a vector and number
                for i in a:  # type: ignore[union-attr]
                    yield i, b  # type: ignore[misc]
            elif dims_b == 1:
                # Apply math to a number and a vector
                for i in b:  # type: ignore[union-attr]
                    yield a, i  # type: ignore[misc]
            elif dims_a == 2:
                # Apply math to 2-D matrix and number
                for row in a:  # type: ignore[union-attr]
                    for i in row:  # type: ignore[union-attr]
                        yield i, b  # type: ignore[misc]
            else:
                for row in b:  # type: ignore[union-attr]
                    for i in row:  # type: ignore[union-attr]
                        yield a, i  # type: ignore[misc]

        # Inputs are at least 2-D dimensions or below on both sides
        elif dims_a == 1:
            # Broadcast a vector and 2-D matrix
            for row in b:  # type: ignore[union-attr]
                yield from self.vector_broadcast(a, row)  # type: ignore[arg-type]
        else:
            # Broadcast a 2-D matrix and a vector
            for row in a:  # type: ignore[union-attr]
                yield from self.vector_broadcast(row, b)  # type: ignore[arg-type]

    def reset(self) -> None:
        """Reset."""

        self._iter = self.broadcast(self.a, self.b, self.dims_a, self.dims_b)

    def __next__(self) -> tuple[float, ...]:
        """Next."""

        # Get the next chunk of data
        return next(self._iter)

    def __iter__(self) -> Iterator[tuple[float, ...]]:  # pragma: no cover
        """Iterate."""

        # Setup and return the iterator.
        return self


def _broadcast_shape(shapes: Sequence[Shape], max_dims: int, stage1_shapes: list[Shape] | None = None) -> Shape:
    """Find the common shape."""

    # Adjust array shapes by padding out with '1's until matches max dimensions
    if stage1_shapes is None:
        stage1_shapes = []

    for s in shapes:
        dims = len(s)
        stage1_shapes.append(((1,) * (max_dims - dims)) + s if dims < max_dims else s)

    # Determine a common shape, if possible
    s2 = []
    for dim in zip(*stage1_shapes):
        mx = 1
        for d in dim:
            if d != 1 and (d != mx and mx != 1):
                raise ValueError("Could not broadcast arrays as shapes are incompatible")
            if d != 1:
                mx = d
        s2.append(mx)
    return tuple(s2)


class Broadcast:
    """Broadcast."""

    def __init__(self, *arrays: ArrayLike | float) -> None:
        """Broadcast."""

        # Determine maximum dimensions
        shapes = []
        max_dims = 0
        for a in arrays:
            s = shape(a)
            dims = len(s)
            if dims > max_dims:
                max_dims = dims
            shapes.append(s)

        stage1_shapes = []  # type: list[Shape]
        common = _broadcast_shape(shapes, max_dims, stage1_shapes)

        # Create iterators to "broadcast to"
        total = len(arrays)
        self.simple = total < 2 or (total == 2 and len(common) <= 2)
        if self.simple:
            self.iters = [_SimpleBroadcast(arrays, shapes, common)]  # type: list[_BroadcastTo] | list[_SimpleBroadcast]
        else:
            self.iters = [_BroadcastTo(a, s1, common) for a, s1 in zip(arrays, stage1_shapes)]

        # I don't think this is done the same way as `numpy`.
        # But shouldn't matter for what we do.
        self.shape = common
        self.ndims = max_dims
        self.size = prod(common)
        self._init()

    def _init(self) -> None:
        """Setup main iterator."""

        self._iter = self.iters[0] if self.simple else it.zip_longest(*self.iters)

    def reset(self) -> None:
        """Reset iterator."""

        # Reset all the child iterators.
        for i in self.iters:
            i.reset()
        self._init()

    def __next__(self) -> tuple[float, ...]:
        """Next."""

        # Get the next chunk of data
        return next(self._iter)  # type: ignore[arg-type]

    def __iter__(self) -> Broadcast:
        """Iterate."""

        # Setup and return the iterator.
        return self


def broadcast(*arrays: ArrayLike | float) -> Broadcast:
    """Broadcast."""

    return Broadcast(*arrays)


@overload
def broadcast_to(a: ArrayLike | float, s: FloatShape) -> float:
    ...


@overload
def broadcast_to(a: ArrayLike | float, s: int | VectorShape) -> Vector:
    ...


@overload
def broadcast_to(a: ArrayLike | float, s: MatrixShape) -> Matrix:
    ...


@overload
def broadcast_to(a: ArrayLike | float, s: TensorShape) -> Tensor:
    ...


def broadcast_to(a: ArrayLike | float, s: int | Shape) -> float | Array:
    """Broadcast array to a shape."""

    _s = (s,) if not isinstance(s, Sequence) else tuple(s)

    s_orig = shape(a)
    ndim_orig = len(s_orig)
    ndim_target = len(_s)
    if ndim_orig > ndim_target:
        raise ValueError(f"Cannot broadcast {s_orig} to {_s}")

    if not ndim_target:
        return a  # type: ignore[return-value]

    s1 = list(s_orig)
    if ndim_orig < ndim_target:
        s1 = ([1] * (ndim_target - ndim_orig)) + s1

    for d1, d2 in zip(s1, _s):
        if d1 != d2 and (d1 != 1 or d1 > d2):
            raise ValueError(f"Cannot broadcast {s_orig} to {_s}")

    m = list(_BroadcastTo(a, tuple(s1), tuple(_s)))
    return reshape(m, _s) if len(_s) > 1 else m  # type: ignore[arg-type]


class vectorize:
    """
    Vectorize a call.

    We do not currently support signatures, caching, and none of our functions allow specifying output
    types. All are assumed floats. Specialized methods will be far more performant than using vectorize,
    but vectorize can be quick to use as far as convenience is concerned.

    There is no optimization for small matrices or matrices that are already the same size. This
    assumes worst case: N x M matrices of unknown quantity.

    Inputs and outputs are currently assumed to be scalars. We do not detect alternate sizes nor
    do we allow specifying function signatures to change it at this time.
    """

    def __init__(
        self,
        pyfunc: Callable[..., Any],
        doc: str | None = None,
        excluded: Sequence[str | int] | None = None
    ) -> None:
        """Initialize."""

        # Save the function and the exclude list
        self.func = pyfunc
        self.excluded = set() if excluded is None else set(excluded)

        # Setup function name and docstring
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__ if doc is None else doc

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call the function after once arguments are vectorized."""

        # No arguments to process, just call the function.
        if not args and not kwargs:
            return self.func()

        # Determine which keys and indexes we want to vectorize
        indexes = [a for a in range(len(args)) if a not in self.excluded]
        keys = [k for k in kwargs if k not in self.excluded]
        size = len(indexes)

        # Cast to a list so we can update the input arguments with vectorized inputs
        inputs = list(args)

        # Gather all the input values we need to vectorize so we can broadcast them together
        vinputs = [inputs[i] for i in indexes] + [kwargs[k] for k in keys]

        if vinputs:
            # We need to broadcast together the inputs for vectorization.
            # Once vectorized, use the wrapper function to replace each argument
            # with the vectorized iteration. Reshape the output to match the input shape.
            bcast = broadcast(*vinputs)
            m = []
            for vargs in bcast:
                # Update arguments with vectorized arguments
                for e, i in enumerate(indexes):
                    inputs[i] = vargs[e]

                # Update keyword arguments with vectorized keyword argument
                kwargs.update(zip(keys, vargs[size:]))

                # Call the function with vectorized inputs
                m.append(self.func(*inputs, **kwargs) if kwargs else self.func(*inputs))

            # Reshape return to match input shape
            return reshape(m, bcast.shape) if len(bcast.shape) != 1 else m  # type: ignore[arg-type]

        # Nothing to vectorize, just run the function with the arguments
        return self.func(*inputs, **kwargs) if kwargs else self.func(*inputs)


class _vectorize1:
    """
    An optimized version of vectorize that is hard coded to broadcast only the first input.

    This is faster than `vectorize` as it skips a lot of generalization code that allows a user
    to specify specific parameters to broadcast. Additionally, users can specify `dims` allowing
    us to skip analyzing the array to determine the size allowing for additional speedup.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""

        self.func = pyfunc

        # Setup function name and docstring
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__ if doc is None else doc

    def __call__(
        self,
        a: ArrayLike | float,
        dims: DimHints | None = None,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""

        if dims and 0 <= dims[0] <= 2:
            dims_a = dims[0]
        else:
            dims_a = len(shape(a))

        func = (lambda p1, kw=kwargs: self.func(p1, **kw)) if kwargs else self.func  # type: Callable[..., Any]

        # Fast paths for scalar, vectors, and 2D matrices
        # Scalar
        if dims_a == 0:
            return func(a)
        # Vector
        elif dims_a == 1:
            return [func(i) for i in a]  # type: ignore[union-attr]
        # 2D matrix
        elif dims_a == 2:
            return [[func(c) for c in r] for r in a]  # type: ignore[union-attr]

        # Unknown size or larger than 2D (slow)
        return reshape([func(f) for f in flatiter(a)], shape(a))


class _vectorize2:
    """
    An optimized version of vectorize that is hard coded to broadcast only the first two inputs.

    This is faster than `vectorize` as it skips a lot of generalization code that allows a user
    to specify specific parameters to broadcast. Additionally, users can specify `dims` allowing
    us to skip analyzing the array to determine the size allowing for additional speedup.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""

        self.func = pyfunc

        # Setup function name and docstring
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__ if doc is None else doc

    def _vector_apply(self, a: VectorLike, b: VectorLike, func: Callable[..., Any]) -> Any:
        """Apply a function to two vectors."""

        # Broadcast the vector
        if len(a) == 1:
            a = [a[0]] * len(b)
        elif len(b) == 1:
            b = [b[0]] * len(a)

        return [func(x, y) for x, y in it.zip_longest(a, b)]

    def __call__(
        self,
        a: ArrayLike | float,
        b: ArrayLike | float,
        dims: DimHints | None = None,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""

        func = (lambda p1, p2, kw=kwargs: self.func(p1, p2, **kw)) if kwargs else self.func  # type: Callable[..., Any]

        if not dims or dims[0] > 2 or dims[1] > 2:
            shape_a = shape(a)
            shape_b = shape(b)
            dims_a = len(shape_a)
            dims_b = len(shape_b)

            # Handle matrices of N-D and M-D size
            if dims_a > 2 or dims_b > 2:
                if dims_a == dims_b:
                    # Apply math to two N-D matrices
                    return reshape(
                        [func(x, y) for x, y in zip(flatiter(a), flatiter(b))],
                        shape_a
                    )
                elif not dims_a or not dims_b:
                    if not dims_a:
                        # Apply math to a number and an N-D matrix
                        return reshape([func(a, x) for x in flatiter(b)], shape_b)
                    # Apply math to an N-D matrix and a number
                    return reshape([func(x, b) for x in flatiter(a)], shape_a)

                # Apply math to an N-D matrix and an M-D matrix by broadcasting to a common shape.
                bcast = broadcast(a, b)
                return reshape([func(x, y) for x, y in bcast], bcast.shape)  # type: ignore[arg-type]
        else:
            dims_a, dims_b = dims

        # Inputs are of equal size and shape
        if dims_a == dims_b:
            if dims_a == 1:
                # Apply math to two vectors
                return self._vector_apply(a, b, func)  # type: ignore[arg-type]
            elif dims_a == 2:
                # Apply math to two 2-D matrices
                la = len(a)  # type: ignore[arg-type]
                lb = len(b)  # type: ignore[arg-type]
                if la == 1 and lb != 1:
                    ra = a[0]  # type: ignore[index]
                    return [self._vector_apply(ra, rb, func) for rb in b]  # type: ignore[arg-type, union-attr]
                elif lb == 1 and la != 1:
                    rb = b[0]  # type: ignore[index]
                    return [self._vector_apply(ra, rb, func) for ra in a]  # type: ignore[arg-type, union-attr]
                return [
                    self._vector_apply(ra, rb, func) for ra, rb in it.zip_longest(a, b)  # type: ignore[arg-type]
                ]
            # Apply math to two scalars
            return func(a, b)

        # Inputs containing a scalar on either side
        elif not dims_a or not dims_b:
            if dims_a == 1:
                # Apply math to a vector and number
                return [func(i, b) for i in a]  # type: ignore[union-attr]
            elif dims_b == 1:
                # Apply math to a number and a vector
                return [func(a, i) for i in b]  # type: ignore[union-attr]
            elif dims_a == 2:
                # Apply math to 2-D matrix and number
                return [[func(i, b) for i in row] for row in a]  # type: ignore[union-attr]
            # Apply math to a number and a matrix
            return [[func(a, i) for i in row] for row in b]  # type: ignore[union-attr]

        # Inputs are at least 2-D dimensions or below on both sides
        if dims_a == 1:
            # Apply math to vector and 2-D matrix
            return [self._vector_apply(a, row, func) for row in b]  # type: ignore[arg-type, union-attr]
        # Apply math to 2-D matrix and a vector
        return [self._vector_apply(row, b, func) for row in a]  # type: ignore[arg-type, union-attr]


class _vectorize1_x3:
    """
    A further optimized version of `_vectorize1` that limits arrays to dimensions of <= 2 and dimension to lengths of 3.

    Like `_vectorize1`, this limits the broadcasting to the first parameter and is faster than `vectorize` as it skips
    a lot of generalization code that allows a user to specify specific parameters to broadcast. Additionally, users
    can specify `dims` allowing us to skip analyzing the array to determine the size allowing for additional speedup.
    Lastly, dimensions are limited to a total less than 2 and the length of dimensions is limited to 3 which allows us
    to avoid looping since the dimension length is always the same.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""

        self.func = pyfunc

        # Setup function name and docstring
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__ if doc is None else doc

    def __call__(
        self,
        a: ArrayLike | float,
        dims: DimHints | None = None,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""

        if not dims:
            shape_a = shape(a)
            dims_a = len(shape_a)
        else:
            dims_a = dims[0]

        if not (0 <= dims_a <= 2):
            raise ValueError('Inputs cannot exceed 2 dimensions')

        func = (lambda p1, kw=kwargs: self.func(p1, **kw)) if kwargs else self.func  # type: Callable[..., Any]

        # Fast paths for scalar, vectors, and 2D matrices
        # Scalar
        if dims_a == 0:
            return func(a)
        # Vector
        elif dims_a == 1:
            return [func(a[0]), func(a[1]), func(a[2])]  # type: ignore[index]

        # Column vector
        if len(a[0]) == 1:  # type: ignore[arg-type, index]
            return [
                [func(a[0][0])],  # type: ignore[index]
                [func(a[1][0])],  # type: ignore[index]
                [func(a[2][0])]  # type: ignore[index]
            ]

        # 2D matrix
        return [
            [func(a[0][0]), func(a[0][1]), func(a[0][2])],  # type: ignore[index]
            [func(a[1][0]), func(a[1][1]), func(a[1][2])],  # type: ignore[index]
            [func(a[2][0]), func(a[2][1]), func(a[2][2])]  # type: ignore[index]
        ]


class _vectorize2_x3:
    """
    A further optimized version of `_vectorize2` that limits arrays to dimensions of <= 2 and dimension to lengths of 3.

    Like `_vectorize2`, this limits the broadcasting to the first two parameter and is faster than `vectorize` as it
    skips a lot of generalization code that allows a user to specify specific parameters to broadcast. Additionally,
    users can specify `dims` allowing us to skip analyzing the array to determine the size allowing for additional
    speedup. Lastly, dimensions are limited to a total less than 2 and the length of dimensions is limited to 3 which
    allows us to avoid looping since the dimension length is always the same.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""

        self.func = pyfunc

        # Setup function name and docstring
        self.__name__ = self.func.__name__
        self.__doc__ = self.func.__doc__ if doc is None else doc

    def __call__(
        self,
        a: MatrixLike | VectorLike | float,
        b: MatrixLike | VectorLike | float,
        dims: DimHints | None = None,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""

        if not dims:
            shape_a = shape(a)
            shape_b = shape(b)
            dims_a = len(shape_a)
            dims_b = len(shape_b)
        else:
            dims_a, dims_b = dims

        func = (lambda a, b, kw=kwargs: self.func(a, b, **kw)) if kwargs else self.func  # type: Callable[..., float]

        if dims_a > 2 or dims_b > 2:
            raise ValueError('Inputs cannot exceed 2 dimensions')

        # Inputs are of equal size and shape
        if dims_a == dims_b:
            if dims_a == 1:
                # Apply math to two vectors
                return [func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2])]  # type: ignore[index]
            elif dims_a == 2:
                l1 = len(a[0])  # type: ignore[arg-type, index]
                l2 = len(b[0])  # type: ignore[arg-type, index]
                if l1 != l2:
                    if l2 == 1:
                        # Column vector in first position
                        return [
                            [func(a[0][0], b[0][0]), func(a[0][1], b[0][0]), func(a[0][2], b[0][0])],  # type: ignore[index]
                            [func(a[1][0], b[1][0]), func(a[1][1], b[1][0]), func(a[1][2], b[1][0])],  # type: ignore[index]
                            [func(a[2][0], b[2][0]), func(a[2][1], b[2][0]), func(a[2][2], b[2][0])],  # type: ignore[index]
                        ]
                    elif l1 == 1:
                        # Column vector in second position
                        return [
                            [func(a[0][0], b[0][0]), func(a[0][0], b[0][1]), func(a[0][0], b[0][2])],  # type: ignore[index]
                            [func(a[1][0], b[1][0]), func(a[1][0], b[1][1]), func(a[1][0], b[1][2])],  # type: ignore[index]
                            [func(a[2][0], b[2][0]), func(a[2][0], b[2][1]), func(a[2][0], b[2][2])],  # type: ignore[index]
                        ]
                    raise ValueError(f'Vectors of size {l1} and {l2} are not aligned')
                elif l1 == 1:
                    # 2 column vectors
                    return [
                        [func(a[0][0], b[0][0])],  # type: ignore[index]
                        [func(a[1][0], b[1][0])],  # type: ignore[index]
                        [func(a[2][0], b[2][0])],  # type: ignore[index]
                    ]
                # Apply math to two 2-D matrices
                return [
                    [func(a[0][0], b[0][0]), func(a[0][1], b[0][1]), func(a[0][2], b[0][2])],  # type: ignore[index]
                    [func(a[1][0], b[1][0]), func(a[1][1], b[1][1]), func(a[1][2], b[1][2])],  # type: ignore[index]
                    [func(a[2][0], b[2][0]), func(a[2][1], b[2][1]), func(a[2][2], b[2][2])],  # type: ignore[index]
                ]
            # Apply math to two scalars
            return func(a, b)

        # Inputs containing a scalar on either side
        elif not dims_a or not dims_b:
            if dims_a == 1:
                # Apply math to a vector and number
                return [func(a[0], b), func(a[1], b), func(a[2], b)]  # type: ignore[index]
            elif dims_b == 1:
                # Apply math to a number and a vector
                return [func(a, b[0]), func(a, b[1]), func(a, b[2])]  # type: ignore[index]
            elif dims_a == 2:
                # Apply math to 2-D matrix and number
                return [
                    [func(a[0][0], b), func(a[0][1], b), func(a[0][2], b)],  # type: ignore[index]
                    [func(a[1][0], b), func(a[1][1], b), func(a[1][2], b)],  # type: ignore[index]
                    [func(a[2][0], b), func(a[2][1], b), func(a[2][2], b)]  # type: ignore[index]
                ]
            # Apply math to a number and a matrix
            return [
                [func(a, b[0][0]), func(a, b[0][1]), func(a, b[0][2])],  # type: ignore[index]
                [func(a, b[1][0]), func(a, b[1][1]), func(a, b[1][2])],  # type: ignore[index]
                [func(a, b[2][0]), func(a, b[2][1]), func(a, b[2][2])]  # type: ignore[index]
            ]

        # Inputs are at least 2-D dimensions or below on both sides
        if dims_a == 1:
            # Apply math to vector and 2-D matrix
            return [
                [func(a[0], b[0][0]), func(a[1], b[0][1]), func(a[2], b[0][2])],  # type: ignore[index]
                [func(a[0], b[1][0]), func(a[1], b[1][1]), func(a[2], b[1][2])],  # type: ignore[index]
                [func(a[0], b[2][0]), func(a[1], b[2][1]), func(a[2], b[2][2])]  # type: ignore[index]
            ]
        # Apply math to 2-D matrix and a vector
        return [
            [func(a[0][0], b[0]), func(a[0][1], b[1]), func(a[0][2], b[2])],  # type: ignore[index]
            [func(a[1][0], b[0]), func(a[1][1], b[1]), func(a[1][2], b[2])],  # type: ignore[index]
            [func(a[2][0], b[0]), func(a[2][1], b[1]), func(a[2][2], b[2])]  # type: ignore[index]
        ]


def vectorize2(
    pyfunc: Callable[..., Any],
    doc: str | None = None,
    params: int = 2,
    only_x3: bool = False
) -> Callable[..., Any]:
    """
    A more limited but faster version of `vectorize` that speed up performance at the cost of flexibility.

    1. Broadcasted parameters are limited to the first 1 or 2 parameters via the `params` option (default 2).
    2. Further limits the expectation of the array in the first 1 or 2 parameters to dimension lengths of 3.
       Additionally, the total number of dimensions cannot exceed 2. `only_x3` enables this behavior and will
       provide the most speed but provides the most limited environment for operations.

    The limitations above allows the avoidance of additional generalized code that can slow the operation down.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    if params == 2:
        return (_vectorize2_x3 if only_x3 else _vectorize2)(pyfunc, doc)
    elif params == 1:
        return (_vectorize1_x3 if only_x3 else _vectorize1)(pyfunc, doc)
    raise ValueError("'vectorize2' does not support dimensions greater than 2 or less than 1")


@deprecated("'vectorize1' is deprecated, use 'vectorize2(func, doc, params=1)' for the equivalent")
def vectorize1(pyfunc: Callable[..., Any], doc: str | None = None) -> Callable[..., Any]:  # pragma: no cover
    """An optimized version of vectorize that is hard coded to broadcast only the first input."""

    return vectorize2(pyfunc, doc, params=1)


@overload
def linspace(start: float, stop: float, num: int = 50, endpoint: bool = True) -> Vector:
    ...


@overload
def linspace(start: VectorLike, stop: VectorLike | float, num: int = 50, endpoint: bool = True) -> Matrix:
    ...


@overload
def linspace(start: VectorLike | float, stop: VectorLike, num: int = 50, endpoint: bool = True) -> Matrix:
    ...


@overload
def linspace(start: MatrixLike, stop: ArrayLike, num: int = 50, endpoint: bool = True) -> Tensor:
    ...


@overload
def linspace(start: ArrayLike, stop: MatrixLike, num: int = 50, endpoint: bool = True) -> Tensor:
    ...


def linspace(start: ArrayLike | float, stop: ArrayLike | float, num: int = 50, endpoint: bool = True) -> Array:
    """Create a series of points in a linear space."""

    if num < 0:
        raise ValueError('Cannot return a negative amount of values')

    # Return empty results over all the inputs for a request of 0
    if num == 0:
        return full(broadcast(start, stop).shape + (0,), [])  # type: ignore[return-value, arg-type]

    # Calculate denominator
    d = float(num - 1 if endpoint else num)

    s1 = shape(start)
    s2 = shape(stop)
    dim1 = len(s1)
    dim2 = len(s2)

    # Scalar case (faster)
    if dim1 == 0 and dim2 == 0:
        return [lerp(start, stop, r / d if d != 0 else 0.0) for r in range(num)]  # type: ignore[arg-type]

    # Vector case
    if dim1 <= 1 and dim2 <= 1:
        # Broadcast scalars to match vectors
        if dim1 == 0:
            start = [start] * s2[0]  # type: ignore[assignment, misc]
            s1 = s2
        if dim2 == 0:
            stop = [stop] * s1[0]  # type: ignore[assignment, misc]
            s2 = s1

        # Broadcast length 1 vectors to match other vector
        if s1[0] != s2[0]:  # type: ignore[misc]
            if s1[0] == 1:  # type: ignore[misc]
                start = start * s2[0]  # type: ignore[operator, misc]
            elif s2[0] == 1:  # type: ignore[misc]
                stop = stop * s1[0]  # type: ignore[operator, misc]
            else:
                raise ValueError(f'Cannot broadcast start ({s1}) and stop ({s2})')

        # Apply linear interpolation steps across the vectors
        values = list(zip(start, stop))  # type: ignore[arg-type]
        m1 = []  # type: Matrix
        for r in range(num):
            m1.append([])
            for a, b in values:
                m1[-1].append(lerp(a, b, r / d if d != 0 else 0.0))  # type: ignore[arg-type]
        return m1

    # To apply over N x M inputs, apply the steps over the broadcasted results (slower)
    m = []
    bcast = broadcast(start, stop)
    for r in range(num):
        bcast.reset()
        for a, b in bcast:
            m.append(lerp(a, b, r / d if d != 0 else 0.0))

    # Reshape to the expected shape
    return reshape(m, (num,) + bcast.shape)  # type: ignore[return-value, arg-type]


def _isclose(a: float, b: float, *, equal_nan: bool = False, **kwargs: Any) -> bool:
    """Check if values are close."""

    close = math.isclose(a, b, **kwargs) if kwargs else math.isclose(a, b)
    return (math.isnan(a) and math.isnan(b)) if not close and equal_nan else close


@overload  # type: ignore[no-overload-impl]
def isclose(a: float, b: float, *, dims: DimHints | None = ..., **kwargs: Any) -> bool:
    ...


@overload
def isclose(a: VectorLike, b: VectorLike, *, dims: DimHints | None = ..., **kwargs: Any) -> VectorBool:
    ...


@overload
def isclose(a: MatrixLike, b: MatrixLike, *, dims: DimHints | None = ..., **kwargs: Any) -> MatrixBool:
    ...


@overload
def isclose(a: TensorLike, b: TensorLike, *, dims: DimHints | None = ..., **kwargs: Any) -> TensorBool:
    ...


isclose = vectorize2(_isclose, doc="Test if a value or value(s) in an array are close to another value(s).")


@overload  # type: ignore[no-overload-impl]
def isnan(a: float, *, dims: DimHints | None = ..., **kwargs: Any) -> bool:
    ...


@overload
def isnan(a: VectorLike, *, dims: DimHints | None = ..., **kwargs: Any) -> VectorBool:
    ...


@overload
def isnan(a: MatrixLike, *, dims: DimHints | None = ..., **kwargs: Any) -> MatrixBool:
    ...


@overload
def isnan(a: TensorLike, *, dims: DimHints | None = ..., **kwargs: Any) -> TensorBool:
    ...


isnan = vectorize2(math.isnan, doc="Test if a value or values in an array are NaN.", params=1)


def allclose(a: ArrayType, b: ArrayType, **kwargs: Any) -> bool:
    """Test if all are close."""

    return all(isclose(a, b, **kwargs) if kwargs else isclose(a, b))


@overload  # type: ignore[no-overload-impl]
def multiply(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def multiply(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def multiply(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def multiply(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def multiply(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def multiply(a: TensorLike, b: float | ArrayLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def multiply(a: float | ArrayLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


multiply = vectorize2(operator.mul, doc="Multiply two arrays or floats.")


@overload  # type: ignore[no-overload-impl]
def divide(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def divide(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def divide(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def divide(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def divide(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def divide(a: TensorLike, b: float | ArrayLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def divide(a: float | ArrayLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


divide = vectorize2(operator.truediv, doc="Divide two arrays or floats.")


@overload  # type: ignore[no-overload-impl]
def add(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def add(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def add(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def add(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def add(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def add(a: TensorLike, b: float | ArrayLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def add(a: float | ArrayLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


add = vectorize2(operator.add, doc="Add two arrays or floats.")


@overload  # type: ignore[no-overload-impl]
def subtract(a: float, b: float, *, dims: DimHints | None = None) -> float:
    ...


@overload
def subtract(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def subtract(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def subtract(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def subtract(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def subtract(a: TensorLike, b: float | ArrayLike, *, dims: DimHints | None = ...) -> Tensor:
    ...


@overload
def subtract(a: float | ArrayLike, b: TensorLike, *, dims: DimHints | None = ...) -> Tensor:
    ...

subtract = vectorize2(operator.sub, doc="Subtract two arrays or floats.")


@overload  # type: ignore[no-overload-impl]
def multiply_x3(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def multiply_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def multiply_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def multiply_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def multiply_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


multiply_x3 = vectorize2(
    operator.mul,
    doc="Multiply two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
    only_x3=True
)


@overload  # type: ignore[no-overload-impl]
def divide_x3(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def divide_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def divide_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def divide_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def divide_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


divide_x3 = vectorize2(
    operator.truediv,
    doc="Divide two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
    only_x3=True
)


@overload  # type: ignore[no-overload-impl]
def add_x3(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def add_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def add_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def add_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def add_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


add_x3 = vectorize2(
    operator.add,
    doc="Add two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
    only_x3=True
)


@overload  # type: ignore[no-overload-impl]
def subtract_x3(a: float, b: float, *, dims: DimHints | None = ...) -> float:
    ...


@overload
def subtract_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def subtract_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints | None = ...) -> Vector:
    ...


@overload
def subtract_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


@overload
def subtract_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints | None = ...) -> Matrix:
    ...


subtract_x3 = vectorize2(
    operator.sub,
    doc="Subtract two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
    only_x3=True
)


@overload
def full(array_shape: FloatShape, fill_value: float | ArrayLike) -> float:
    ...

@overload
def full(array_shape: int | VectorShape, fill_value: float | ArrayLike) -> Vector:
    ...


@overload
def full(array_shape: MatrixShape, fill_value: float | ArrayLike) -> Matrix:
    ...


@overload
def full(array_shape: TensorShape, fill_value: float | ArrayLike) -> Tensor:
    ...


def full(array_shape: int | Shape, fill_value: float | ArrayLike) -> Array | float:
    """Create and fill a shape with the given values."""

    # Ensure `shape` is a sequence of sizes
    s = (array_shape,) if not isinstance(array_shape, Sequence) else tuple(array_shape)

    # Normalize `fill_value` to be an array.
    if not isinstance(fill_value, Sequence):
        return reshape([fill_value] * prod(s), s)  # type: ignore[arg-type]

    # If the shape doesn't fit the data, try and broadcast it.
    # If it does fit, just reshape it.
    if shape(fill_value) != s:
        return broadcast_to(fill_value, s)  # type: ignore[arg-type]
    return reshape(fill_value, s)  # type: ignore[arg-type]


@overload
def ones(array_shape: FloatShape) -> float:
    ...


@overload
def ones(array_shape: int | VectorShape) -> Vector:
    ...


@overload
def ones(array_shape: MatrixShape) -> Matrix:
    ...


@overload
def ones(array_shape: TensorShape) -> Tensor:
    ...


def ones(array_shape: int | Shape) -> Array | float:
    """Create and fill a shape with ones."""

    return full(array_shape, 1.0)  # type: ignore[arg-type]


@overload
def zeros(array_shape: FloatShape) -> float:
    ...

@overload
def zeros(array_shape: int | VectorShape) -> Vector:
    ...


@overload
def zeros(array_shape: MatrixShape) -> Matrix:
    ...


@overload
def zeros(array_shape: TensorShape) -> Tensor:
    ...


def zeros(array_shape: int | Shape) -> Array | float:
    """Create and fill a shape with zeros."""

    return full(array_shape, 0.0)  # type: ignore[arg-type]


def ndindex(*s: Shape) -> Iterator[tuple[int, ...]]:
    """Iterate dimensions."""

    yield from it.product(
        *(range(d) for d in (s[0] if not isinstance(s[0], int) and len(s) == 1 else s))  # type: ignore[arg-type]
    )


def flatiter(array: float | ArrayLike) -> Iterator[float]:
    """Traverse an array returning values."""

    for indices in ndindex(shape(array)):
        m = array  # type: Any
        for i in indices:
            m = m[i]
        yield m


def ravel(array: float | ArrayLike) -> Vector:
    """Return a flattened vector."""

    return list(flatiter(array))


def _frange(start: float, stop: float, step: float) -> Iterator[float]:
    """Float range."""

    x = start
    rev = step < 0.0
    limit = stop - step
    while x >= limit if rev else x <= limit:
        yield x
        x += step


def arange(
    start: SupportsFloatOrInt,
    stop: SupportsFloatOrInt | None = None,
    step: SupportsFloatOrInt = 1
) -> Vector:
    """
    Like arrange, but handles floats as well.

    Return will be a list instead of an iterator.
    Due to floating point precision, floats may be inaccurate to some degree.
    """

    if stop is None:
        stop = start
        start = 0

    if isinstance(start, int) and isinstance(stop, int) and isinstance(step, int):
        return list(range(start, stop, step))
    else:
        return list(_frange(float(start), float(stop), float(step)))


@overload
def transpose(array: float) -> float:
    ...


@overload
def transpose(array: VectorLike) -> Vector:
    ...


@overload
def transpose(array: MatrixLike) -> Matrix:
    ...


@overload
def transpose(array: TensorLike) -> Tensor:
    ...


def transpose(array: ArrayLike | float) -> float | Array:
    """
    A simple transpose of a matrix.

    `numpy` offers the ability to specify different axes, but right now,
    we don't have a need for that, nor the desire to figure it out :).
    """

    s = shape(array)[::-1]  # type: Shape
    l = len(s)

    # Number
    if l == 0:
        return array  # type: ignore[return-value]
    # Vector
    if l == 1:
        return list(array)  # type: ignore[return-value, arg-type]
    # 2 x 2 matrix
    if l == 2:
        return [list(z) for z in zip(*array)]  # type: ignore[misc]

    # N x M matrix
    if s and s[0] == 0:
        s = s[1:] + (0,)
        total = prod(s[:-1])
    else:
        total = prod(s)

    # Create the array
    m = []  # type: Array

    # Calculate data sizes
    dims = len(s)
    length = s[-1]  # type: ignore[misc]

    # Initialize indexes so we can properly write our data
    idx = [0] * dims
    data = flatiter(array)

    # Traverse the provided array filling our new array
    for i in range(total):

        # Navigate to the proper index to start writing data.
        # If the dimension hasn't been created yet, create it.
        t = m  # type: Any
        for d in range(dims - 1):
            if not t:
                for _ in range(s[d]):
                    t.append([])  # noqa: PERF401
            t = t[idx[d]]

        # Initialize the last dimension
        # so we can index at the correct position
        if not t:
            t[:] = [0] * length

        # Write the data
        if length:
            t[idx[-1]] = next(data)

        # Update the current indexes if we aren't done copying data.
        if i < (total - 1):
            for x in range(dims):
                if (idx[x] + 1) % s[x] == 0:
                    idx[x] = 0
                    x += 1
                else:
                    idx[x] += 1
                    break

    return m



@overload
def reshape(array: ArrayLike | float, new_shape: FloatShape) -> float:
    ...


@overload
def reshape(array: ArrayLike | float, new_shape: int | VectorShape) -> Vector:
    ...


@overload
def reshape(array: ArrayLike | float, new_shape: MatrixShape) -> Matrix:
    ...


@overload
def reshape(array: ArrayLike | float, new_shape: TensorShape) -> Tensor:
    ...


def reshape(array: ArrayLike | float, new_shape: int | Shape) -> float | Array:
    """Change the shape of an array."""

    # Ensure floats are arrays
    if not isinstance(array, Sequence):
        array = [array]

    # Normalize shape specifier to a sequence
    if not isinstance(new_shape, Sequence):
        new_shape = (new_shape,)

    # Shape to a scalar
    if not new_shape:
        v = ravel(array)
        if len(v) == 1:
            return v[0]
        # Kick out if the requested shape doesn't match the data
        raise ValueError(f'Shape {new_shape} does not match the data total of {shape(array)}')

    current_shape = shape(array)

    # Copy the array and quit if we are already the requested shape
    if current_shape == new_shape:
        return acopy(array)

    empty = (not new_shape or 0 in new_shape) and (not current_shape or 0 in current_shape)

    # Make sure we can actually reshape.
    total = prod(new_shape) if not empty else prod(new_shape[:-1])
    if not empty and total != prod(current_shape):
        raise ValueError(f'Shape {new_shape} does not match the data total of {shape(array)}')

    # Create the array
    m = []  # type: Array

    # Calculate data sizes
    dims = len(new_shape)

    # Create an iterator to traverse the data
    data = flatiter(array) if len(current_shape) > 1 else iter(array)  # type: ignore[arg-type]

    # Build the new array
    for idx in ndindex(new_shape[:-1] if new_shape and not new_shape[-1] else new_shape):
        # Navigate to the proper index to start writing data.
        # If the dimension hasn't been created yet, create it.
        t = m  # type: Any
        for d in range(dims - 1):
            if not t:
                for _ in range(new_shape[d]):
                    t.append([])  # noqa: PERF401
            t = t[idx[d]]

        # Create the final dimension, writing all the data
        if not empty:
            t.append(next(data))

    return m


def _shape(a: ArrayLike | float, s: Shape) -> Shape:
    """
    Get the shape of the array.

    We only test the first index at each depth for speed.
    """

    # Found a scalar input
    if not isinstance(a, Sequence):
        return s

    # Get the length
    size = len(a)

    # Array is empty, return the shape
    if not size:
        return (size,)

    # Recursively get the shape of the first entry and compare against the others
    first = _shape(a[0], s)
    for r in range(1, size):
        if _shape(a[r], s) != first:
            raise ValueError('Ragged lists are not supported')

    # Construct the final shape
    return (size,) + first


@overload
def _quick_shape(a: float) -> FloatShape:
    ...


@overload
def _quick_shape(a: VectorLike) -> VectorShape:
    ...


@overload
def _quick_shape(a: MatrixLike) -> MatrixShape:
    ...


@overload
def _quick_shape(a: TensorLike) -> TensorShape:
    ...


def _quick_shape(a: ArrayLike | float) -> Shape:
    """
    Acquire shape taking shortcuts by assume a non-ragged, consistently shaped array.

    No checking for consistency is performed allowing for a quicker check.
    """

    t = a  # type: Any
    s = []
    while isinstance(t, Sequence):
        l = len(t)
        s.append(l)
        if not l:
            break
        t = t[0]
    return tuple(s)


@overload
def shape(a: float) -> FloatShape:
    ...


@overload
def shape(a: VectorLike) -> VectorShape:
    ...


@overload
def shape(a: MatrixLike) -> MatrixShape:
    ...


@overload
def shape(a: TensorLike) -> TensorShape:
    ...


def shape(a: ArrayLike | float) -> Shape:
    """Get the shape of a list."""

    return _shape(a, ())


def fill_diagonal(matrix: Matrix | Tensor, val: float | ArrayLike, wrap: bool = False) -> None:
    """Fill an N-D matrix diagonal."""

    s = shape(matrix)
    if len(s) < 2:
        raise ValueError('Arrays must be 2D or greater')
    if len(s) != 2:
        wrap = False
        if min(s) != max(s):
            raise ValueError('Arrays larger than 2D must have all dimensions of equal length')

    val = [val] if not isinstance(val, Sequence) else ravel(val)
    mx = max(s)
    dlast = len(s) - 1
    dlen = len(val) - 1
    pos = 0

    x = [0] * len(s)
    while x[0] < mx:
        t = matrix  # type: Any
        for idx in range(len(s)):
            r = s[idx]
            current = x[idx]
            if current < r:
                if idx == dlast:
                    t[current] = val[pos]
                else:
                    t = t[current]
                x[idx] += 1
            elif wrap and idx and current == r:
                x[idx] = 0
            else:
                x[0] = mx
                break

        pos = pos + 1 if pos < dlen else 0


def eye(n: int, m: int | None = None, k: int = 0) -> Matrix:
    """Create a diagonal of ones in a zero initialized matrix at the specified position."""

    if m is None:
        m = n

    # Length of diagonal
    dlen = m if n > m and k < 0 else (m - abs(k))

    a = []  # type: Matrix
    for i in range(n):
        pos = i + k
        idx = i if k >= 0 else pos
        d = int(0 <= idx < dlen)  # Number of diagonals to insert (0 or 1)
        a.append(
            ([0.0] * clamp(pos, 0, m)) +
            ([1.0] * d) +
            ([0.0] * clamp(m - pos - d, 0, m))
        )
    return a


def identity(size: int) -> Matrix:
    """Create an identity matrix."""

    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]


@overload
def diag(array: VectorLike, k: int = 0) -> Matrix:
    ...


@overload
def diag(array: MatrixLike, k: int = 0) -> Vector:
    ...


def diag(array: VectorLike | MatrixLike, k: int = 0) -> Vector | Matrix:
    """Create a diagonal matrix from a vector or return a vector of the diagonal of a matrix."""

    s = shape(array)
    dims = len(s)
    if not dims or dims > 2:
        raise ValueError('Array must be 1-D or 2-D in shape')

    if dims == 1:
        # Calculate size of matrix to accommodate the diagonal
        size = s[0] - k if k < 0 else (s[0] + k if k else s[0])
        maximum = size - 1
        minimum = 0

        # Create a diagonal matrix with the provided vector
        m = []  # type: Matrix
        for i in range(size):
            pos = i + k
            idx = i if k >= 0 else pos
            m.append(
                ([0.0] * clamp(pos, minimum, maximum)) +
                [array[idx] if (0 <= pos < size) else 0.0] +  # type: ignore[arg-type]
                ([0.0] * clamp(size - pos - 1, minimum, maximum))
            )
        return m
    else:
        # Extract the requested diagonal from a rectangular 2-D matrix
        size = s[1]  # type: ignore[misc]
        d = []
        for i, r in enumerate(array):
            pos = i + k
            if (0 <= pos < size):
                d.append(r[pos])  # type: ignore[index]
        return d


def lu(
    matrix: MatrixLike | TensorLike,
    *,
    permute_l: bool = False,
    p_indices: bool = False,
    _shape: Shape | None = None
) ->  Any:
    """
    Calculate `LU` decomposition.

    P is returned as `PA = UL` or `A = P'UL` which follows `Matlab` and `Octave` opposed to `Scipy` which returns P as
    `A = PUL` or `P'A = UL`. For matrix inverse, we need P such that `PA = UL` and it is faster not having to invert
    P, even if we can invert it fairly fast as it is just a shuffled identity matrix.

    P is returned as a permutation matrix unless `p_indices` is true, in which case `P` would be returned as
    a vector containing the indexes such that `A[P,:] = L*U`.

    If `permute_l` is true, only L and U will be returned such that `P = LU`.

    Reference: https://www.statlect.com/matrix-algebra/Gaussian-elimination
               https://www.sciencedirect.com/topics/mathematics/partial-pivoting
    """

    s = shape(matrix) if _shape is None else _shape
    size = s[0]
    dims = len(s)

    # We need a rectangular N x M matrix
    if dims < 2:
        raise ValueError('LU decomposition requires an array larger than a vector')
    elif dims > 2:
        last = s[-2:]
        first = s[:-2]
        rows = list(_extract_rows(matrix, s))
        step = last[-2]
        results = []
        zipped = zip(
            *(
                lu(rows[r:r + step], permute_l=permute_l, p_indices=p_indices, _shape=last)
                for r in range(0, len(rows), step)
            )
        )
        for parts in zipped:
            results.append(reshape(parts, first + shape(parts[0])))   # type: ignore[arg-type]  # noqa: PERF401
        return tuple(results)

    # Wide or tall matrices
    wide = tall = False
    diff = s[0] - s[1]
    if diff:
        matrix = acopy(matrix)

        # Wide
        if diff < 0:
            diff = abs(diff)
            size = s[1]
            wide = True
            for _ in range(diff):
                matrix.append([0.0] * size)  # type: ignore[list-item]  # noqa: PERF401
        # Tall
        else:
            tall = True
            for row in matrix:
                row.extend([0.0] * diff)  # type: ignore[list-item]

    # Initialize the triangle matrices along with the permutation matrix.
    if p_indices or permute_l:
        p = list(range(size))  # type: Any
        l = identity(size)
    else:
        p = identity(size)
        l = [list(row) for row in p]
    u = [list(row) for row in matrix]

    # Create upper and lower triangle in 'u' and 'l'. 'p' tracks the permutation (relative position of rows)
    for i in range(size - 1):

        # Partial pivoting: identify the row with the maximal value in the column
        j = i
        maximum = abs(u[i][i])  # type: ignore[var-annotated, arg-type]
        for k in range(i + 1, size):
            a = abs(u[k][i])  # type: ignore[var-annotated, arg-type]
            if a > maximum:
                j = k
                maximum = a

        # Partial pivoting: Swap rows
        if j != i:
            # Exchange current upper triangle row with row with maximal value at pivot
            # Update permutation matrix as well
            u[i], u[j] = u[j], u[i]
            p[i], p[j] = p[j], p[i]

            # Only swap columns up to the pivot for the lower triangle,
            # if on first row, there is nothing to swap
            if i:
                l[i][:i], l[j][:i] = l[j][:i], l[i][:i]

        # Zero at pivot point, nothing to do
        elif not maximum:
            continue

        # We have a pivot point, let's zero out everything above and below
        # the 'l' and 'u' diagonal respectively
        for j in range(i + 1, size):
            scalar = u[j][i] / u[i][i]  # type: ignore[operator]
            for k in range(i, size):
                u[j][k] += -u[i][k] * scalar  # type: ignore[operator]
                l[j][k] += l[i][k] * scalar

    # Clean up the wide and tall matrices
    if tall:
        l = [r[:-diff] for r in l]
        u = [r[:-diff] for r in u][:-diff]
    elif wide:
        l = [r[:-diff] for r in l][:-diff]
        u = u[:-diff]
        p = p[:-diff] if p_indices else [r[:-diff] for r in p][:-diff]

    # Transpose the indexes and return LU after permuting L
    if permute_l:
        pt = [0] * size
        for e, i in enumerate(p):
            pt[i] = e
        p = pt

        return [l[i] for i in pt], u

    return p, l, u


def _forward_sub_vector(a: Matrix, b: Vector, size: int) -> Vector:
    """Forward substitution for solution of `L x = b`."""

    for i in range(size):
        v = b[i]
        for j in range(i):
            v -= a[i][j] * b[j]
        b[i] = v / a[i][i]
    return b


def _forward_sub_matrix(a: Matrix, b: Matrix, s: ArrayShape) -> Matrix:
    """Forward substitution for solution of `L x = b` where `b` is a matrix."""

    size1, size2 = s
    for i in range(size1):
        v = b[i]
        for j in range(i):
            for k in range(size2):
                v[k] -= a[i][j] * b[j][k]
        for j in range(size2):
            v[j] /= a[i][i]
    return b


def _back_sub_vector(a: Matrix, b: Vector, size: int) -> Vector:
    """Back substitution for solution of `U x = b`."""

    for i in range(size - 1, -1, -1):
        v = b[i]
        for j in range(i + 1, size):
            v -= a[i][j] * b[j]
        b[i] = v / a[i][i]
    return b


def _back_sub_matrix(a: Matrix, b: Matrix, s: ArrayShape) -> Matrix:
    """Back substitution for solution of `U x = b`."""

    size1, size2 = s
    for i in range(size1 - 1, -1, -1):
        v = b[i]  # type: Any
        for j in range(i + 1, size1):
            for k in range(size2):
                v[k] -= a[i][j] * b[j][k]
        for j in range(size2):
            b[i][j] /= a[i][i]
    return b


@overload
def solve(a: MatrixLike, b: VectorLike) -> Vector:
    ...


@overload
def solve(a: MatrixLike, b: MatrixLike) -> Matrix:
    ...


@overload
def solve(a: MatrixLike, b: TensorLike) -> Tensor:
    ...


@overload
def solve(a: TensorLike, b: MatrixLike | TensorLike) -> Tensor | Matrix:
    ...


def solve(a: MatrixLike | TensorLike, b: ArrayLike) -> Array:
    """
    Solve the system of equations.

    The return value always matches the shape of 'b' and `a' must be square
    in the last two dimensions.

    Broadcasting is not quite done in the traditional way.

    1. [M, M] and [M] will solve a set of linear equations against a vector
       of dependent variables.

    2. If we have [..., M, M] and [..., M, M] and it we have multiple sets of linear
       equations it will be treated as multiple [M, M] and [M] cases as described in 1).

       If we have only one set of linear equations, it will be treated as a [..., M, M] and
       [..., M, K] case as described in 3).

    3. If we have [..., M, M] and [..., M, K], we will either solve a single set of linear
       equations against multiple matrices of containing K dependent variable sets.

    4. Lastly, if we have [..., M, M] and [..., M], where we have N vectors that matches N [M, M]
       equation sets, then we will solve one matrix with one vector.

    Anything else "should" fail, one way or another.
    """

    s = shape(a)
    size = s[-1]
    dims = len(s)
    if len(s) < 2 or s[-1] != s[-2]:
        raise ValueError('Last two dimension must be square')

    # Fast simple cases: two 2 dimensional matrices or one 2 dimensional matrix and a vector
    dim1 = not isinstance(b[0], Sequence)
    dim2 = not dim1 and not isinstance(b[0][0], Sequence)  # type: ignore[index]
    if dims == 2 and (dim1 or dim2):
        # Get the LU decomposition
        p, l, u = lu(a, p_indices=True, _shape=s)

        # If determinant is zero, we can't solve. Really small determinant may give bad results.
        if prod(l[i][i] * u[i][i] for i in range(size)) == 0.0:
            raise ValueError('Matrix is singular')

        # Solve for x using forward substitution on U and back substitution on L
        if dim2:
            # Two matrices
            size2 = len(b[0])  # type: ignore[arg-type]
            if size != len(b):
                raise ValueError('Mismatched dimensions')

            ordered = []
            for i in p:
                r = b[i]
                if len(r) != size2:
                    raise ValueError('Mismatched dimensions')
                ordered.append(list(r))
            s2 = (size, size2)  # type: Shape
            return _back_sub_matrix(u, _forward_sub_matrix(l, ordered, s2), s2)

        # Matrix and one vector
        if len(b) != s[-2]:
            raise ValueError('Mismatched dimensions')
        b = [b[i] for i in p]
        return _back_sub_vector(u, _forward_sub_vector(l, b, size), size)  # type: ignore[arg-type]

    # More complex, deeply nested cases that require more analyzing
    s2 = shape(b)
    sol_m = sol_v = False
    x = []  # type: Any

    # Broadcast the solving
    if s2[-2] == size:  # type: ignore[misc]
        if s2[-1] == size:
            p1 = prod(s)
            p2 = prod(s2)
            # One matrix of equations with multiple series of M dependent variable sets (matrix)
            sol_m = not p2 % p1
            # Multiple equations sets with a single series of dependent variables per equation set (vectors)
            sol_v = not sol_m and not p1 % p2
        elif s2[-2] == size:  # type: ignore[misc]
            # One matrix of equations with multiple series of K dependent variable sets (matrix)
            p1 = prod(s[:-1])  # type: ignore[misc]
            p2 = prod(s2[:-1])  # type: ignore[misc]
            sol_m = not p2 % p1
    elif s2[-1] == size:
        # Multiple equations sets with a single series of dependent variables per equation set (vectors)
        p1 = prod(s[:-2])  # type: ignore[misc]
        p2 = prod(s2[:-1])  # type: ignore[misc]
        sol_v = p1 == p2

    # Matrix and matrices
    if sol_m:
        rows_equ = list(_extract_rows(a, s))
        ma = [rows_equ[r:r + size] for r in range(0, len(rows_equ), size)]
        rows_sol = list(_extract_rows(b, s2))
        mb = [rows_sol[r:r + size] for r in range(0, len(rows_sol), size)]
        ai_shape = s[-2:]  # type: ignore[misc]

        p, l, u = lu(ma[0], p_indices=True, _shape=ai_shape)

        if prod(l[i][i] * u[i][i] for i in range(size)) == 0.0:
            raise ValueError('Matrix is singular')

        for bi in mb:
            bi = [list(bi[i]) for i in p]
            s3 = (size, len(bi[0]))
            x.append(_back_sub_matrix(u, _forward_sub_matrix(l, bi, s3), s3))
        return reshape(x, s2)

    # Matrices and vectors
    elif sol_v:
        rows_equ = list(_extract_rows(a, s))
        ma = [rows_equ[r:r + size] for r in range(0, len(rows_equ), size)]
        mv = list(_extract_rows(b, s2))
        ai_shape = s[-2:]  # type: ignore[misc]

        for ai, vi in zip(ma, mv):
            p, l, u = lu(ai, p_indices=True, _shape=ai_shape)

            if prod(l[i][i] * u[i][i] for i in range(size)) == 0.0:
                raise ValueError('Matrix is singular')

            x.append(_back_sub_vector(u, _forward_sub_vector(l, [vi[i] for i in p], size), size))
        return reshape(x, s2)

    raise ValueError(f"Could not broadcast {s} and {s2}")


def trace(matrix: Matrix) -> float:
    """Sum the diagonal."""

    return sum(diag(matrix))


@overload
def det(array: MatrixLike) -> float:
    ...


@overload
def det(array: TensorLike) -> Vector:
    ...


def det(array: MatrixLike | TensorLike) -> float | Vector:
    """Get the determinant."""

    s = shape(array)
    if len(s) < 2 or s[-1] != s[-2]:
        raise ValueError('Last two dimensions must be square')
    if len(s) == 2:
        size = s[0]
        p, l, u = lu(array, _shape=s)
        swaps = size - trace(p)
        sign = (-1) ** (swaps - 1) if swaps else 1
        dt = sign * prod(l[i][i] * u[i][i] for i in range(size))
        return 0.0 if not dt else dt
    else:
        last = s[-2:]  # type: ignore[misc]
        rows = list(_extract_rows(array, s))
        step = last[-2]
        return [det(rows[r:r + step]) for r in range(0, len(rows), step)]


@overload
def inv(matrix: MatrixLike) -> Matrix:
    ...


@overload
def inv(matrix: TensorLike) -> Tensor:
    ...


def inv(matrix: MatrixLike | TensorLike) -> Matrix | Tensor:
    """Invert the matrix using `LU` decomposition."""

    # Ensure we have a square matrix
    s = shape(matrix)
    dims = len(s)
    last = s[-2:]  # type: ignore[misc]
    if dims < 2 or min(last) != max(last):
        raise ValueError('Matrix must be a N x N matrix')

    # Handle dimensions greater than 2 x 2
    elif dims > 2:
        invert = []
        rows = list(_extract_rows(matrix, s))
        step = last[-2]
        invert = [inv(rows[r:r + step]) for r in range(0, len(rows), step)]
        return reshape(invert, s)

    # Calculate the LU decomposition.
    size = s[0]
    p, l, u = lu(matrix, _shape=s)

    # Floating point math will produce very small, non-zero determinants for singular matrices.
    # This occurs with Numpy as well.
    # Don't bother calculating sign as we only care about how close to zero we are.
    if prod(l[i][i] * u[i][i] for i in range(size)) == 0.0:
        raise ValueError('Matrix is singular')

    # Solve for the identity matrix (will give us inverse)
    # Permutation matrix is the identity matrix, even if shuffled.
    s2 = (size, size)
    return _back_sub_matrix(u, _forward_sub_matrix(l, p, s2), s2)


def pinv(a: MatrixLike) -> Matrix:
    """
    Compute the (Moore-Penrose) pseudo-inverse of a matrix.

    We currently 'assume' the matrix if full rank. If not, a singular matrix error
    will be thrown. Such matrices may still be invertible, but they would require
    a more advanced approach that we do not currently implement.

    Negative results can be returned, use `fnnls` for a non-negative solution (if possible).
    """

    s = shape(a)
    if len(s) != 2:
        raise ValueError('Inputs can only be matrices, vectors or tensors are not allowed')

    t = transpose(a)
    if s[0] >= s[1]:
        p = matmul(inv(matmul(t, a, dims=D2)), t, dims=D2)
    else:
        p = matmul(t, inv(matmul(a, t, dims=D2)), dims=D2)
    return p


@overload
def vstack(arrays: Sequence[float | Vector | Matrix]) -> Matrix:
    ...


@overload
def vstack(arrays: Sequence[Tensor]) -> Tensor:
    ...


def vstack(arrays: Sequence[ArrayLike | float]) -> Matrix | Tensor:
    """Vertical stack."""

    m = []  # type: list[Any]
    dims = 0

    # Array tracking for verification
    axis = 0
    last = ()  # type: Shape
    last_dims = 0

    for a in arrays:
        s = shape(a)
        dims = len(s)

        # We need to be working with at least a 2D array
        if dims == 0:
            a = [[a]]  # type: ignore[assignment]
            s = (1, 1)
            dims = 2
        elif dims == 1:
            a = [a]  # type: ignore[assignment]
            s = (1, s[0])  # type: ignore[misc]
            dims = 2

        # Verify that we can apply the stacking
        if last:
            end2 = min(last_dims, dims)
            end1 = min(end2, axis)
            start = 1
            start2 = min(end1 + 1, end2)
            # All axes must match except for the concatenation axis
            if s[start:end1] + s[start2:end2] != last[start:end1] + last[start2:end2]:
                raise ValueError('All the input array dimensions except for the concatenation axis must match exactly')

        # Stack the arrays
        m.extend(reshape(a, (prod(s[:1 - dims]),) + s[1 - dims:-1] + s[-1:]))  # type: ignore[arg-type, misc]

        # Update the last array tracker
        if not last or len(last) > len(s):
            last = s
            last_dims = dims

    # Fail if we have nothing to stack
    if not m:
        raise ValueError("'vstack' requires at least one array")

    return m


def _hstack_extract(a: ArrayLike | float, s: ArrayShape) -> Iterator[Array]:
    """Extract data from the second axis."""

    data = flatiter(a)
    length = prod(s[1:])

    for _ in range(s[0]):
        yield [next(data) for _ in range(length)]


def hstack(arrays: Sequence[ArrayLike | float]) -> Array:
    """Horizontal stack."""

    # Gather up shapes
    columns = 0
    shapes = []

    # Array tracking for verification
    axis = 1
    last = ()  # type: Shape
    last_dims = 0
    largest = ()  # type: Shape
    largest_length = 0

    arrs = []
    for a in arrays:
        s = shape(a)
        dims = len(s)

        # Ensure we are at least 1-D
        if dims == 0:
            a = [a]  # type: ignore[assignment]
            s = (1,)
            dims = 1

        # Store modified arrays to use later
        arrs.append(a)

        # Get the largest
        l = len(s)
        if l > largest_length:
            largest = s
            largest_length = l

        # Verify that we can apply the stacking
        if last:
            end2 = min(last_dims, dims)
            end1 = min(end2, axis)
            start = 0
            start2 = min(end1 + 1, end2)
            max_dims = max(last_dims, dims)
            # All axes must match except for the concatenation axis. 1-D arrays can have different lengths.
            if (max_dims > 1 and s[start:end1] + s[start2:end2] != last[start:end1] + last[start2:end2]):
                raise ValueError('All the input array dimensions except for the concatenation axis must match exactly')

        # Gather up shapes and tally the size of axis 1, 1-D arrays do not need this.
        if dims > 1:
            columns += s[axis]

        shapes.append(s)

        # Update the last array tracker
        if not last or len(last) > len(s):
            last = s
            last_dims = dims

    # Fail if we have nothing to stack
    if not shapes:
        raise ValueError("'hstack' requires at least one array")

    # Handle 1-D vector cases
    if largest_length == 1:
        m1 = []  # type: Vector
        for a in arrays:
            m1.extend(ravel(a))
        return m1

    # Iterate the arrays returning the content per second axis
    m = []  # type: list[Any]
    for data in it.zip_longest(*[_hstack_extract(a, s) for a, s in it.zip_longest(arrs, shapes) if s != (0,)]):
        for d in data:
            m.extend(d)

    # Shape the data to the new shape
    new_shape = largest[:axis] + (columns,) + largest[axis + 1:] if len(largest) > 1 else (columns,)
    return reshape(m, new_shape)  # type: ignore[return-value, arg-type]


def outer(a: float | ArrayLike, b: float | ArrayLike) -> Matrix:
    """Compute the outer product of two vectors (or flattened matrices)."""

    v2 = ravel(b)
    return [[x * y for y in v2] for x in flatiter(a)]


@overload
def inner(a: float, b: float) -> float:
    ...


@overload
def inner(a: float, b: VectorLike) -> Vector:
    ...


@overload
def inner(a: VectorLike, b: float) -> Vector:
    ...


@overload
def inner(a: float, b: MatrixLike) -> Matrix:
    ...


@overload
def inner(a: MatrixLike, b: float) -> Matrix:
    ...


@overload
def inner(a: float, b: TensorLike) -> Tensor:
    ...


@overload
def inner(a: TensorLike, b: float) -> Tensor:
    ...


@overload
def inner(a: VectorLike, b: VectorLike) -> float:
    ...


@overload
def inner(a: VectorLike, b: MatrixLike) -> Vector:
    ...


@overload
def inner(a: MatrixLike, b: VectorLike) -> Vector:
    ...


@overload
def inner(a: VectorLike, b: TensorLike) -> Tensor | Matrix:
    ...


@overload
def inner(a: TensorLike, b: VectorLike) -> Tensor | Matrix:
    ...


@overload
def inner(a: MatrixLike, b: MatrixLike) -> Matrix:
    ...


@overload
def inner(a: MatrixLike, b: TensorLike) -> Tensor | Matrix:
    ...


@overload
def inner(a: TensorLike, b: MatrixLike) -> Tensor | Matrix:
    ...


@overload
def inner(a: TensorLike, b: TensorLike) -> Tensor:
    ...


def inner(a: float | ArrayLike, b: float | ArrayLike) -> float | Array:
    """Compute the inner product of two arrays."""

    shape_a = shape(a)
    shape_b = shape(b)
    dims_a = len(shape_a)
    dims_b = len(shape_b)

    # If both inputs are not scalars, the last dimension must match
    if (shape_a and shape_b and shape_a[-1] != shape_b[-1]):
        raise ValueError(f'The last dimensions {shape_a} and {shape_b} do not match')

    # If we have a scalar, we should just multiply
    if (not dims_a or not dims_b):
        return multiply(a, b, dims=(dims_a, dims_b))

    # Adjust the input so that they can properly be evaluated
    # Scalars will be broadcasted to properly match the last dimension
    # of the other input.
    if dims_a == 1:
        first = [a]  # type: Any
    elif dims_a > 2:
        first = _extract_rows(a, shape_a)  # type: ignore[arg-type]
    else:
        first = a

    if dims_b == 1:
        second = [b]  # type: Any
    elif dims_b > 2:
        second = list(_extract_rows(b, shape_b))  # type: ignore[arg-type]
    else:
        second = b

    # Perform the actual inner product
    m = [[sum([x * y for x, y in it.zip_longest(r1, r2)]) for r2 in second] for r1 in first]
    new_shape = shape_a[:-1] + shape_b[:-1]  # type: ignore[misc]

    # Shape the data.
    return reshape(m, new_shape)  # type: ignore[arg-type]


def fnnls(
    A: MatrixLike,
    b: VectorLike,
    epsilon: float = 1e-12,
    max_iters: int = 0
) -> tuple[Vector, float]:
    """
    Fast non-negative least squares.

    A fast non-negativity-constrained least squares
    https://www.researchgate.net/publication/230554373_A_Fast_Non-negativity-constrained_Least_Squares_Algorithm
    Rasmus Bro and Sijmen De Jong
    Journal of Chemometrics. 11, 393–401 (1997)
    """

    m, n = _quick_shape(A)

    if m != len(b):
        raise ValueError(f'Vector length of b must match first dimension of A: {m} != {len(b)}')

    if not max_iters:
        max_iters = n * 30

    AT = transpose(A)
    ATA = dot(AT, A, dims=D2)
    ATb = dot(AT, b, dims=D2_D1)

    x = [0.0] * n
    s = [0.0] * n
    w = subtract(ATb, dot(ATA, x, dims=D2_D1), dims=D1)  # type: Vector

    # P tracks positive elements in x
    # Does double duty as P and R vector outlined in the paper
    P = [False] * n

    # Continue until all values of x are positive (non-negative results only)
    # or we exhaust the iterations.
    count = 0
    while sum(P) < n and max(w[i] for i in range(n) if not P[i]) > epsilon and count < max_iters:
        # Find the index that maximizes w
        # This will be an index not in P
        imx = 0
        mx = -math.inf
        for i in range(n):
            if not P[i] and w[i] > mx:
                imx = i
                mx = w[i]

        P[imx] = True

        # Solve least squares problem for columns and rows not in P
        idx = [i for i in range(n) if P[i]]
        v = dot(inv([[ATA[i][j] for j in idx] for i in idx]), [ATb[i] for i in idx], dims=D2_D1)
        for i, _v in zip(idx, v):
            s[i] = _v

        # Deal with negative values
        while _any([s[i] <= epsilon for i in range(n) if P[i]]):
            count += 1

            # Calculate step size, alpha, to prevent any x from going negative
            alpha = min(
                [zdiv(x[i], (x[i] - s[i]), math.inf) for i in range(n) if P[i] * (s[i] <= epsilon)]
            )

            # Update the solution
            x = add(x, dot(alpha, subtract(s, x, dims=D1), dims=SC_D1), dims=D1)

            # Remove indexes in P where x == 0
            for i in range(n):
                if x[i] <= epsilon:
                    P[i] = False

            # Solve least squares problem again
            idx = [i for i in range(n) if P[i]]
            v = dot(inv([[ATA[i][j] for j in idx] for i in idx]), [ATb[i] for i in idx], dims=D2_D1)
            j = 0
            l = len(idx)
            for i in range(n):
                if j < l and i == idx[j]:
                    s[i] = v[j]
                    j += 1
                else:
                    s[i] = 0.0

        # Update the solution
        x = s[:]
        w = subtract(ATb, dot(ATA, x, dims=D2_D1), dims=D1)

    # Return our final result, for better or for worse
    res = math.hypot(*subtract(b, dot(A, x, dims=D2_D1), dims=D1))
    return x, res
